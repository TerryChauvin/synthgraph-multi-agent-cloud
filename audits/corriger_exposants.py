"""Calcule les corrections d'exposants aplatis (10<sup>5</sup> -> 10^5) pour les publications listees.
Usage : python3 -I audits/corriger_exposants.py <fichier_pmcids> [--apply]
Sans --apply : liste seulement les edits (pmcid, ancien -> nouveau, occurrences dans corpus/text)."""
import re, sys, os, json
import xml.etree.ElementTree as ET
sys.path.insert(0, os.getcwd())
NUM = re.compile(r"^\d+([.,]\d+)?$")
def local(t): return t.rsplit("}", 1)[-1]

def collect(path):
    root = ET.parse(path).getroot()
    body = next(x for x in root.iter() if local(x.tag) == "body")
    out = []
    def walk(e):
        n = local(e.tag)
        if n in ("fig", "table-wrap", "supplementary-material", "graphic"): return
        if n == "xref" and e.get("ref-type") == "bibr": return
        if e.text: out.append(e.text)
        for c in e:
            if local(c.tag) == "sup": out.append(("S", "".join(c.itertext())))
            else: walk(c)
            if c.tail: out.append(c.tail)
    walk(body)
    s = ""; marks = []
    for x in out:
        if isinstance(x, tuple): marks.append((len(s), x[1].strip())); s += x[1]
        else: s += x
    s = re.sub(r"\s+", " ", s)  # approximatif : positions recalculees par recherche de contexte
    return out

def edits_for(pm):
    out = collect(f"corpus/xml/{pm}.xml")
    # reconstruire avec marqueurs
    s = ""; marks = []
    for x in out:
        if isinstance(x, tuple): marks.append((len(s), x[1].strip())); s += x[1]
        else: s += x
    res = set()
    for pos, t in marks:
        if not NUM.match(t) or pos == 0 or not s[pos-1].isdigit(): continue
        b = re.sub(r"\s+", " ", s[max(0, pos-9):pos]); a = re.sub(r"\s+", " ", s[pos+len(t):pos+len(t)+5])
        res.add((b + t + a, b + "^" + t + a))
    return res

# faux positifs : degre (70.9<sup>0</sup>), charges d'ions, renvois en exposant
EXCLUDE = {"PMC12455581", "PMC6678425"}
EXCLUDE_OLD = ("AgNO325", "Ag059")
MANUAL = {"PMC8255795": [("(100\u2013105)", "(10^0\u201310^5)")]}
GENERIC = re.compile(r"(?<=[\u00d7X])(\s*)10(\d{1,2})(?!\d)")

def all_edits(pm, text):
    ed = [(o, n) for o, n in edits_for(pm) if not any(x in o for x in EXCLUDE_OLD)]
    ed += MANUAL.get(pm, [])
    ed.sort(key=lambda e: -len(e[0]))
    return ed

def fix(pm, text):
    if pm in EXCLUDE: return text
    for o, n in all_edits(pm, text):
        if o == "(100\u2013105)" or True:
            text = text.replace(o, n)
    return GENERIC.sub(lambda m: m.group(1) + "10^" + m.group(2), text)

if __name__ == "__main__":
    pms = open(sys.argv[1]).read().split(); apply = "--apply" in sys.argv
    for pm in pms:
        tp = f"corpus/text/{pm}.txt"; text = open(tp, encoding="utf-8").read(); new = fix(pm, text)
        jp = f"extractions/{pm}.json"; js = open(jp, encoding="utf-8").read() if os.path.exists(jp) else None
        njs = fix(pm, js) if js else None
        print(pm, "texte", sum(1 for a, b in zip(text, new) if a != b) if len(text)==len(new) else "len+%d" % (len(new)-len(text)),
              "json", None if js is None else ("len+%d" % (len(njs)-len(js))))
        if apply:
            open(tp, "w", encoding="utf-8").write(new)
            if js: open(jp, "w", encoding="utf-8").write(njs)
