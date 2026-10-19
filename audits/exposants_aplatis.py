"""Liste les exposants <sup> numeriques aplatis par sections.py (lecture seule).
Usage : python3 -I audits/exposants_aplatis.py  -> ecrit audits/exposants_aplatis.md
Candidat 'chiffre' : <sup> numerique precede d'un chiffre (10<sup>5</sup> -> 105), ambigu.
Candidat 'unite'   : <sup> signe, ex. 10<sup>-7</sup> -> 10-7 ou cm-3 (signe conserve, lisible mais fragile).
Croisement : la chaine aplatie apparait-elle dans extractions/<PMCID>.json (citations) ?"""
import re, glob, os, json
import xml.etree.ElementTree as ET
from collections import defaultdict

NUM = re.compile(r"^[−–-]?\d+([.,]\d+)?$")
SIGN = re.compile(r"^[−–-]\d+$")
res = defaultdict(list)

def local(t): return t.rsplit("}", 1)[-1]

def walk(e, out):
    """Texte aplati avec marqueurs de position des sup."""
    n = local(e.tag)
    if n in ("xref", "fig", "table-wrap", "supplementary-material", "graphic", "ref-list", "back"):
        if n in ("xref",):
            pass
        else:
            return
    if n == "xref" and e.get("ref-type") == "bibr":
        return
    if e.text: out.append(e.text)
    for c in e:
        if local(c.tag) == "sup":
            out.append(("SUP", "".join(c.itertext())))
        else:
            walk(c, out)
        if c.tail: out.append(c.tail)

for path in sorted(glob.glob("corpus/xml/*.xml")):
    pm = os.path.basename(path)[:-4]
    try: root = ET.parse(path).getroot()
    except Exception: continue
    out = []
    body = next((x for x in root.iter() if local(x.tag) == "body"), None)
    if body is None: continue
    walk(body, out)
    s = ""; marks = []
    for x in out:
        if isinstance(x, tuple):
            marks.append((len(s), x[1])); s += x[1]
        else: s += x
    for pos, t in marks:
        t = t.strip()
        if not NUM.match(t): continue
        prev = s[max(0, pos-1):pos]
        kind = "unite" if SIGN.match(t) else ("chiffre" if prev.isdigit() else None)
        if not kind: continue
        ctx = re.sub(r"\s+", " ", s[max(0, pos-14):pos+len(t)+10])
        res[pm].append((kind, ctx, t))

exts = {}
for p in glob.glob("extractions/*.json"):
    exts[os.path.basename(p)[:-5]] = open(p, encoding="utf-8").read()

L = ["# Exposants aplatis par `sections.py`", "",
     "Genere par `audits/exposants_aplatis.py` (lecture seule ; rien dans `synthese.db`, `extractions/`, `critiques/`).", ""]
tot = {"chiffre": 0, "unite": 0}; touched = {"chiffre": set(), "unite": set()}; rows = []
for pm, lst in res.items():
    for kind, ctx, t in lst:
        tot[kind] += 1; touched[kind].add(pm)
        flat = ctx[14-0:] if False else ctx
        # chaine aplatie minimale : derniers chiffres avant + exposant
        m = re.search(r"(\S*\d)" + re.escape(t) , ctx)
        key = ctx
        cited = None
        if pm in exts:
            i = ctx.find(t, max(0, len(ctx) - len(t) - 10 - 3))
            i = len(ctx) - 10 - len(t)
            probe = ctx[max(0, i - 6):i + len(t) + 3]
            cited = probe in re.sub(r"\s+", " ", exts[pm])
        rows.append((pm, kind, ctx, cited))
ext_ids = set(exts)
nc = {k: len({pm for pm, kk, c, ci in rows if kk == k and ci}) for k in tot}
L += [f"- XML analyses : {len(glob.glob('corpus/xml/*.xml'))}, extractions : {len(exts)}",
      f"- Candidats « chiffre » (10^5 -> 105) : {tot['chiffre']} occurrences dans {len(touched['chiffre'])} publications "
      f"({len(touched['chiffre'] & ext_ids)} extraites)",
      f"- Candidats « unite » (signe conservé : 10^-7 -> 10−7, cm^-3 -> cm−3) : {tot['unite']} occurrences dans {len(touched['unite'])} publications "
      f"({len(touched['unite'] & ext_ids)} extraites)",
      f"- Publications extraites dont le JSON contient la chaîne aplatie : chiffre {nc['chiffre']}, unité {nc['unite']}",
      "", "Colonne *cité* : la chaîne aplatie (contexte) apparaît telle quelle dans le JSON d'extraction (citation ou valeur potentiellement affectée). Vide = publication non extraite.", ""]
for kind, title in (("chiffre", "Exposant précédé d'un chiffre (risque élevé)"), ("unite", "Exposant signé conservé (10−7, cm−3 : risque faible, lisible)")):
    L += [f"## {title}", "", "| PMCID | contexte aplati | cité |", "|---|---|---|"]
    for pm, k, ctx, cited in sorted(rows):
        if k == kind:
            L.append(f"| {pm} | `{ctx}` | {'oui' if cited else ('non' if cited is False else '')} |")
    L.append("")
open("audits/exposants_aplatis.md", "w", encoding="utf-8").write("\n".join(L))
print(tot, {k: len(v) for k, v in touched.items()})
