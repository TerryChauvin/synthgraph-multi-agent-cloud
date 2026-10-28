#!/usr/bin/env python3
"""Concordance entre l'extraction en base (extractions/<PMCID>.json) et une ré-extraction à l'aveugle (verification/blind/<PMCID>.json).
Usage : python3 -I compare_blind.py [PMCID ...]  (sans argument : tous les fichiers de verification/blind/) → docs/audit_contenu/data/verif_reextraction.json
Mesures : voies appariées, rappel et précision des valeurs numériques de paramètres, de résultats et de quantités de réactifs (même nom canonique, même unité normalisée, valeur à ±2 %), conflits (même nom et même voie, valeur différente)."""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_contenu import canon_prop, norm_unit
from audit_verification import canon_param

TOKRE = re.compile(r"[a-z0-9]+")


def toks(*s):
    return set(t for x in s if x for t in TOKRE.findall(str(x).lower()) if len(t) > 1)


def jac(a, b):
    return len(a & b) / len(a | b) if a | b else 0.0


def close(a, b):
    return abs(a - b) <= max(1e-9, 0.02 * max(abs(a), abs(b)))


def route_items(r):
    """(paramètres, résultats, réactifs) numériques d'une voie : listes de (clé, valeur, unité, nom brut)."""
    P, O, R = [], [], []
    for st in r.get("steps") or []:
        for p in st.get("parameters") or []:
            if p.get("value_num") is not None:
                P.append((canon_param(p.get("name")), float(p["value_num"]), norm_unit(p.get("unit")), p.get("name")))
    for o in r.get("outcomes") or []:
        if o.get("value_num") is not None:
            O.append((canon_prop(o.get("property"))[0], float(o["value_num"]), norm_unit(o.get("unit")), o.get("property")))
    for g in r.get("reagents") or []:
        if g.get("amount") is not None:
            R.append((frozenset(toks(g.get("name"), g.get("formula"))), float(g["amount"]), norm_unit(g.get("unit")), g.get("name")))
    return P, O, R


def match_values(A, B, reagent=False):
    """Pour chaque élément de A, existe-t-il dans B un élément de même clé (ou réactif proche), même unité (ou unité absente d'un côté) et valeur à ±2 % ? Renvoie (trouvés, conflits)."""
    found = 0; conflicts = 0; used = set()
    for k, v, u, raw in A:
        best = None
        for j, (k2, v2, u2, raw2) in enumerate(B):
            if j in used:
                continue
            same_key = (jac(k, k2) >= 0.5) if reagent else (k == k2 and k != "autre") or (k == "autre" and k2 == "autre")
            if not same_key or (u and u2 and u != u2):
                continue
            if close(v, v2):
                best = j; break
            if best is None and not reagent:
                best = ("conflict", j)
        if isinstance(best, int):
            found += 1; used.add(best)
        elif best is not None:
            conflicts += 1
    return found, conflicts


def compare(pmcid):
    O = json.load(open(f"extractions/{pmcid}.json")); B = json.load(open(f"verification/blind/{pmcid}.json"))
    ro, rb = O.get("routes") or [], B.get("routes") or []
    key = lambda r: toks(r.get("label"), (r.get("material") or {}).get("name"), (r.get("material") or {}).get("formula"))
    pairs = []; usedb = set()
    for i, r in enumerate(ro):
        best, bs = None, 0.0
        for j, r2 in enumerate(rb):
            if j in usedb:
                continue
            s = jac(key(r), key(r2))
            if s > bs:
                best, bs = j, s
        if best is not None and bs >= 0.2:
            pairs.append((i, best)); usedb.add(best)
    stats = dict(pmcid=pmcid, voies_base=len(ro), voies_aveugle=len(rb), voies_appariees=len(pairs), branches_base=sum(1 for r in ro if r.get("parent")), branches_aveugle=sum(1 for r in rb if r.get("parent")),
                 doutes_base=len(O.get("doubts") or []), doutes_aveugle=len(B.get("doubts") or []))
    tot = dict(params_base=0, params_trouves=0, params_aveugle=0, params_trouves_inv=0, params_conflits=0, resultats_base=0, resultats_trouves=0, resultats_aveugle=0, resultats_trouves_inv=0, resultats_conflits=0, reactifs_base=0, reactifs_trouves=0, reactifs_aveugle=0, reactifs_trouves_inv=0)
    allP_b, allO_b, allR_b = [], [], []
    for r2 in rb:
        p, o, g = route_items(r2); allP_b += p; allO_b += o; allR_b += g
    allP_o, allO_o, allR_o = [], [], []
    for r in ro:
        p, o, g = route_items(r); allP_o += p; allO_o += o; allR_o += g
    # appariement par voie (rappel strict) puis global (la valeur existe quelque part)
    for i, j in pairs:
        Po, Oo, Ro = route_items(ro[i]); Pb, Ob, Rb = route_items(rb[j])
        f, c = match_values(Po, Pb); tot["params_base"] += len(Po); tot["params_trouves"] += f; tot["params_conflits"] += c
        f, c = match_values(Oo, Ob); tot["resultats_base"] += len(Oo); tot["resultats_trouves"] += f; tot["resultats_conflits"] += c
        f, _ = match_values(Ro, Rb, reagent=True); tot["reactifs_base"] += len(Ro); tot["reactifs_trouves"] += f
    unmatched_o = [i for i in range(len(ro)) if i not in {i for i, _ in pairs}]
    for i in unmatched_o:
        Po, Oo, Ro = route_items(ro[i]); tot["params_base"] += len(Po); tot["resultats_base"] += len(Oo); tot["reactifs_base"] += len(Ro)
    gP, _ = match_values(allP_o, allP_b); gO, _ = match_values(allO_o, allO_b); gR, _ = match_values(allR_o, allR_b, reagent=True)
    iP, _ = match_values(allP_b, allP_o); iO, _ = match_values(allO_b, allO_o); iR, _ = match_values(allR_b, allR_o, reagent=True)
    tot.update(params_aveugle=len(allP_b), params_trouves_inv=iP, resultats_aveugle=len(allO_b), resultats_trouves_inv=iO, reactifs_aveugle=len(allR_b), reactifs_trouves_inv=iR)
    stats.update(tot)
    pct = lambda a, b: round(100 * a / b, 1) if b else None
    stats.update(rappel_voies=pct(len(pairs), len(ro)), rappel_params=pct(tot["params_trouves"], tot["params_base"]), rappel_params_global=pct(gP, len(allP_o)), precision_params=pct(iP, len(allP_b)),
                 rappel_resultats=pct(tot["resultats_trouves"], tot["resultats_base"]), rappel_resultats_global=pct(gO, len(allO_o)), precision_resultats=pct(iO, len(allO_b)),
                 rappel_reactifs=pct(tot["reactifs_trouves"], tot["reactifs_base"]), rappel_reactifs_global=pct(gR, len(allR_o)), precision_reactifs=pct(iR, len(allR_b)))
    return stats


def main():
    ids = sys.argv[1:] or sorted(os.path.basename(f)[:-5] for f in glob.glob("verification/blind/*.json"))
    rows = [compare(p) for p in ids if os.path.exists(f"extractions/{p}.json")]
    out = "docs/audit_contenu/data/verif_reextraction.json"
    if rows:
        s = lambda k: sum(r[k] for r in rows)
        pct = lambda a, b: round(100 * a / b, 1) if b else None
        rows.append(dict(pmcid="TOTAL", voies_base=s("voies_base"), voies_aveugle=s("voies_aveugle"), voies_appariees=s("voies_appariees"), branches_base=s("branches_base"), branches_aveugle=s("branches_aveugle"), doutes_base=s("doutes_base"), doutes_aveugle=s("doutes_aveugle"),
                         params_base=s("params_base"), params_trouves=s("params_trouves"), params_aveugle=s("params_aveugle"), params_trouves_inv=s("params_trouves_inv"), params_conflits=s("params_conflits"), resultats_base=s("resultats_base"), resultats_trouves=s("resultats_trouves"), resultats_aveugle=s("resultats_aveugle"), resultats_trouves_inv=s("resultats_trouves_inv"), resultats_conflits=s("resultats_conflits"),
                         reactifs_base=s("reactifs_base"), reactifs_trouves=s("reactifs_trouves"), reactifs_aveugle=s("reactifs_aveugle"), reactifs_trouves_inv=s("reactifs_trouves_inv"), rappel_voies=pct(s("voies_appariees"), s("voies_base")), rappel_params=pct(s("params_trouves"), s("params_base")), rappel_params_global=None, precision_params=pct(s("params_trouves_inv"), s("params_aveugle")),
                         rappel_resultats=pct(s("resultats_trouves"), s("resultats_base")), rappel_resultats_global=None, precision_resultats=pct(s("resultats_trouves_inv"), s("resultats_aveugle")), rappel_reactifs=pct(s("reactifs_trouves"), s("reactifs_base")), rappel_reactifs_global=None, precision_reactifs=pct(s("reactifs_trouves_inv"), s("reactifs_aveugle")), publications=len(rows)))
    json.dump(rows, open(out, "w"), ensure_ascii=False, separators=(",", ":"))
    rows = rows[:-1]
    for r in rows:
        print(f"{r['pmcid']}: voies {r['voies_base']}/{r['voies_aveugle']} appariées {r['voies_appariees']} | params rappel {r['rappel_params']}% (global {r['rappel_params_global']}%) précision {r['precision_params']}% conflits {r['params_conflits']} | résultats rappel {r['rappel_resultats']}% (global {r['rappel_resultats_global']}%) précision {r['precision_resultats']}% conflits {r['resultats_conflits']} | réactifs rappel {r['rappel_reactifs']}% précision {r['precision_reactifs']}%")
    if rows:
        s = lambda k: sum(r[k] for r in rows)
        print(f"TOTAL {len(rows)} publications : voies appariées {s('voies_appariees')}/{s('voies_base')} ; params rappel {round(100*s('params_trouves')/s('params_base'),1)}% précision {round(100*s('params_trouves_inv')/s('params_aveugle'),1)}% conflits {s('params_conflits')} ; résultats rappel {round(100*s('resultats_trouves')/s('resultats_base'),1)}% précision {round(100*s('resultats_trouves_inv')/s('resultats_aveugle'),1)}% conflits {s('resultats_conflits')} ; réactifs rappel {round(100*s('reactifs_trouves')/max(1,s('reactifs_base')),1)}%")


if __name__ == "__main__":
    main()
