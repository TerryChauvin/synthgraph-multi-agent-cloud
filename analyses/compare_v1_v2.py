"""Comparaison des extractions v1 (extractions/, pipeline complet : extraction + 2 critiques + correction) et v2
(extractions_v2/, architecture v2 : une extraction au format 3 avec vocabulaire contrôlé).

    python3 -I analyses/compare_v1_v2.py            # publications de audits/v2/tirage.json ayant une v2
    → docs/audit_contenu/data/compare_v1_v2.json et audits/v2/comparaison_v1_v2.md

Mesures par publication et en total : volumes (voies, étapes, paramètres, résultats, mesures, réglages,
littérature, calculs, cases « non cité »), couverture des nombres de l'article (analyses/couverture_valeurs.py),
normalisation des noms (part dans le vocabulaire), grille de mesure, lien résultat → mesure, concordance des
valeurs (analyses/compare_blind.py : v1 prise comme référence), noms ajoutés au vocabulaire, jetons.
"""
import csv
import json
import os
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path[:0] = [HERE, ROOT]
os.chdir(ROOT)
import compare_blind  # noqa: E402
import couverture_valeurs as cv  # noqa: E402
import vocab  # noqa: E402

idx, entries = vocab.index_noms()


def in_vocab(typ, name, prefix=False):
    n = vocab.norm(name or "")
    if n in idx[typ]:
        return True
    if prefix:
        parts = n.split("_")
        return any("_".join(parts[:k]) in idx[typ] for k in range(len(parts) - 1, 0, -1))
    return False


def volumes(d):
    R = d.get("routes") or []
    V = dict(voies=len(R), branches=sum(1 for r in R if r.get("parent")), voies_calcul=sum(1 for r in R if r.get("kind") == "calcul"),
             etapes=0, parametres=0, reactifs=0, resultats=0, mesures=0, reglages=0, reglages_absents=0,
             not_stated=0, litterature=len(d.get("comparisons") or []), doutes=len(d.get("doubts") or []),
             annotations=len(d.get("annotations") or []), resultats_lies=0, resultats_mesure_non_citee=0,
             mesures_avec_conditions=0)
    acts, pars, props, techs, meths = [], [], [], [], []
    for r in R:
        V["not_stated"] += len(r.get("not_stated") or [])
        meths += r.get("methods") or ([r["method"]] if r.get("method") else [])
        for g in r.get("reagents") or []:
            V["reactifs"] += 1
            V["not_stated"] += len(g.get("not_stated") or [])
        for s in r.get("steps") or []:
            V["etapes"] += 1
            acts.append(s.get("action"))
            V["not_stated"] += len(s.get("not_stated") or [])
            for p in s.get("parameters") or []:
                V["parametres"] += 1
                pars.append(p.get("name"))
        for ch in r.get("characterizations") or []:
            V["mesures"] += 1
            techs.append(ch.get("technique"))
            V["reglages"] += len(ch.get("settings") or [])
            V["reglages_absents"] += len(ch.get("not_stated") or [])
            if ch.get("settings") or ch.get("conditions") or ch.get("instrument"):
                V["mesures_avec_conditions"] += 1
        for o in r.get("outcomes") or []:
            V["resultats"] += 1
            props.append(o.get("property"))
            mb = o.get("measured_by")
            if mb == "not_stated":
                V["resultats_mesure_non_citee"] += 1
            elif mb:
                V["resultats_lies"] += 1
    noms = dict(actions=(sum(in_vocab("action", a) for a in acts), len(acts), len(set(acts))),
                parametres=(sum(in_vocab("parametre", p, True) for p in pars), len(pars), len(set(pars))),
                proprietes=(sum(in_vocab("propriete", p, True) for p in props), len(props), len(set(props))),
                techniques=(sum(in_vocab("technique", t) for t in techs), len(techs), len(set(techs))),
                methodes=(sum(in_vocab("methode", m) for m in meths), len(meths), len(set(meths))))
    return V, noms


def all_values(d):
    """(valeur, unité normalisée, sorte) de tous les nombres extraits : paramètres, quantités, résultats, réglages, littérature."""
    out = []
    nu = compare_blind.norm_unit
    for r in d.get("routes") or []:
        for g in r.get("reagents") or []:
            if isinstance(g.get("amount"), (int, float)):
                out.append((float(g["amount"]), nu(g.get("unit")), "reactif"))
        for s in r.get("steps") or []:
            for x in s.get("parameters") or []:
                if isinstance(x.get("value_num"), (int, float)):
                    out.append((float(x["value_num"]), nu(x.get("unit")), "parametre"))
        for v in r.get("variations") or []:
            if isinstance(v.get("value_num"), (int, float)):
                out.append((float(v["value_num"]), nu(v.get("unit")), "parametre"))
        for o in r.get("outcomes") or []:
            if isinstance(o.get("value_num"), (int, float)):
                out.append((float(o["value_num"]), nu(o.get("unit")), "resultat"))
        for ch in r.get("characterizations") or []:
            for st in ch.get("settings") or []:
                if isinstance(st.get("value_num"), (int, float)):
                    out.append((float(st["value_num"]), nu(st.get("unit")), "reglage"))
    return out


def value_recall(A, B):
    """Part des valeurs de A retrouvées dans B (même valeur à 2 %, même unité), sans tenir compte du nom."""
    pool = list(B)
    found = 0
    for v, u, _ in A:
        for i, (w, u2, _) in enumerate(pool):
            if u == u2 and compare_blind.close(v, w):
                found += 1
                pool.pop(i)
                break
    return found, len(A)


def tokens():
    T = {}
    for r in csv.DictReader(open("audits/jetons.csv", encoding="utf-8-sig")):
        p = r["publication"]
        T.setdefault(p, {}).setdefault(r["passe"], 0)
        T[p][r["passe"]] += int(r["jetons"] or 0)
    return T


def manquantes(p):
    v1 = json.load(open(f"extractions/{p}.json", encoding="utf-8"))
    v2 = json.load(open(f"extractions_v2/{p}.json", encoding="utf-8"))
    B = all_values(v2)
    for r in v1.get("routes") or []:
        for kind, items in (("résultat", r.get("outcomes") or []), ("paramètre", [x for s in r.get("steps") or [] for x in s.get("parameters") or []]), ("réactif", r.get("reagents") or [])):
            for x in items:
                v = x.get("value_num", x.get("amount"))
                if not isinstance(v, (int, float)):
                    continue
                u = compare_blind.norm_unit(x.get("unit"))
                if not any(u == u2 and compare_blind.close(float(v), w) for w, u2, _ in B):
                    print(f"{r['label']} | {kind} {x.get('property') or x.get('name')} = {v} {x.get('unit') or ''} | « {(x.get('quote') or '')[:110]} »")


def main():
    if "--manquantes" in sys.argv:
        manquantes(sys.argv[-1])
        return
    pubs = [p for p in json.load(open("audits/v2/tirage.json"))["publications"] if os.path.exists(f"extractions_v2/{p}.json")]
    T = tokens()
    ajouts = {}
    for f in list(vocab.AJOUTS.glob("PMC*.json")) + list(vocab.VDIR.glob("ajouts_fusionnes_v*/PMC*.json")):
        ajouts[f.stem] = len(json.load(open(f, encoding="utf-8")).get("ajouts", []))
    rows = []
    for p in pubs:
        v1 = json.load(open(f"extractions/{p}.json", encoding="utf-8"))
        v2 = json.load(open(f"extractions_v2/{p}.json", encoding="utf-8"))
        V1, N1 = volumes(v1)
        V2, N2 = volumes(v2)
        c1, _, _ = cv.cover(p, v1)
        c2, _, _ = cv.cover(p, v2)
        conc = compare_blind.compare(p, v1, v2)
        a1, a2 = all_values(v1), all_values(v2)
        f12, n1 = value_recall(a1, a2)
        f21, n2 = value_recall(a2, a1)
        t = T.get(p, {})
        rows.append(dict(pmcid=p, v1=V1, v2=V2, noms_v1=N1, noms_v2=N2,
                         couverture_v1={k: c1[k]["pct"] for k in c1}, couverture_v2={k: c2[k]["pct"] for k in c2},
                         manquants_v1={k: c1[k]["manquants"] for k in c1}, manquants_v2={k: c2[k]["manquants"] for k in c2},
                         totaux={k: c1[k]["total"] for k in c1},
                         concordance=dict(voies_appariees=conc["voies_appariees"], rappel_params=conc["rappel_params_global"],
                                          precision_params=conc["precision_params"], rappel_resultats=conc["rappel_resultats_global"],
                                          precision_resultats=conc["precision_resultats"], rappel_reactifs=conc["rappel_reactifs_global"],
                                          conflits_params=conc["params_conflits"], conflits_resultats=conc["resultats_conflits"]),
                         valeurs=dict(v1=n1, v2=n2, v1_dans_v2=f12, v2_dans_v1=f21),
                         ajouts_vocabulaire=ajouts.get(p, 0),
                         jetons_v1=sum(v for k, v in t.items() if not k.startswith(("v2", "complement", "test_", "critique_ajouts"))),
                         jetons_v2=t.get("v2_extraction", 0), jetons_v2_critique=t.get("v2_critique", 0)))
    json.dump(rows, open("docs/audit_contenu/data/compare_v1_v2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if not rows:
        print("aucune publication v2")
        return
    S = lambda side, k: sum(r[side][k] for r in rows)
    med = lambda f: statistics.median([f(r) for r in rows])
    L = ["# Comparaison v1 / v2", "", f"{len(rows)} publications (`audits/v2/tirage.json`). v1 = pipeline complet (extraction, critique de fidélité, critique scientifique, correction) ; v2 = une seule extraction au format 3 (`RUNBOOK_V2.md`, vocabulaire contrôlé). Script : `analyses/compare_v1_v2.py`.", "",
         "## Volumes (total sur les publications)", "", "| | v1 | v2 | v2 / v1 |", "|---|---|---|---|"]
    for k, lab in (("voies", "voies"), ("branches", "branches"), ("voies_calcul", "voies de calcul"), ("etapes", "étapes"), ("parametres", "paramètres d'étape"),
                   ("reactifs", "réactifs"), ("resultats", "résultats"), ("mesures", "mesures (caractérisations)"), ("mesures_avec_conditions", "mesures avec appareil ou réglages"),
                   ("reglages", "réglages de mesure structurés"), ("reglages_absents", "réglages de mesure déclarés absents"), ("litterature", "valeurs de la littérature"),
                   ("not_stated", "cases « non cité » (synthèse)"), ("resultats_lies", "résultats liés à leur mesure"), ("resultats_mesure_non_citee", "résultats à mesure non citée"),
                   ("doutes", "doutes"), ("annotations", "annotations")):
        a, b = S("v1", k), S("v2", k)
        L.append(f"| {lab} | {a} | {b} | {round(b / a, 2) if a else '—'} |")
    L += ["", "## Couverture des nombres de l'article", "", "| Source | Nombres | Absents v1 | Absents v2 | Couverture v1 | Couverture v2 |", "|---|---|---|---|---|---|"]
    for k, lab in (("tableaux", "cellules de tableaux"), ("resultats_texte", "nombres avec unité, résultats"), ("experimental", "nombres avec unité, expérimental")):
        tot = sum(r["totaux"][k] for r in rows)
        m1 = sum(r["manquants_v1"][k] for r in rows)
        m2 = sum(r["manquants_v2"][k] for r in rows)
        L.append(f"| {lab} | {tot} | {m1} | {m2} | {round(100 * (tot - m1) / max(tot, 1), 1)} % | {round(100 * (tot - m2) / max(tot, 1), 1)} % |")
    L += ["", "## Normalisation des noms (part des occurrences dans le vocabulaire v2 ; noms distincts)", "", "| Type | v1 dans le vocabulaire | v2 dans le vocabulaire | noms distincts v1 | noms distincts v2 |", "|---|---|---|---|---|"]
    for k in ("methodes", "actions", "parametres", "proprietes", "techniques"):
        a = sum(r["noms_v1"][k][0] for r in rows); n1 = sum(r["noms_v1"][k][1] for r in rows)
        b = sum(r["noms_v2"][k][0] for r in rows); n2 = sum(r["noms_v2"][k][1] for r in rows)
        d1 = len({x for r in rows for x in [r["noms_v1"][k][2]]})
        L.append(f"| {k} | {round(100 * a / max(n1, 1))} % ({a}/{n1}) | {round(100 * b / max(n2, 1))} % ({b}/{n2}) | {sum(r['noms_v1'][k][2] for r in rows)} | {sum(r['noms_v2'][k][2] for r in rows)} |")
    n1 = sum(r["valeurs"]["v1"] for r in rows); n2 = sum(r["valeurs"]["v2"] for r in rows)
    f12 = sum(r["valeurs"]["v1_dans_v2"] for r in rows); f21 = sum(r["valeurs"]["v2_dans_v1"] for r in rows)
    L += ["", "## Concordance des valeurs, indépendante des noms", "",
          f"- valeurs numériques v1 retrouvées dans la v2 (même valeur à 2 %, même unité, quel que soit le nom) : {f12} / {n1} ({round(100 * f12 / max(n1, 1), 1)} %)",
          f"- valeurs numériques v2 déjà présentes dans la v1 : {f21} / {n2} ({round(100 * f21 / max(n2, 1), 1)} %) ; le reste est nouveau en v2",
          "- les valeurs v1 non retrouvées sont listées par `python3 -I analyses/compare_v1_v2.py --manquantes <PMCID>`"]
    L += ["", "## Concordance par nom canonique (v1 comme référence, méthode de `compare_blind.py`)", "",
          "Cette mesure exige le même nom canonique : elle sous-estime l'accord quand la v1 a mal nommé une valeur (par exemple des teneurs XPS en % atomique rangées sous « énergie de liaison »).", "",
          f"- voies v1 appariées à une voie v2 : {sum(r['concordance']['voies_appariees'] for r in rows)} sur {S('v1', 'voies')}",
          f"- paramètres numériques v1 retrouvés en v2 (rappel, médiane par publication) : {med(lambda r: r['concordance']['rappel_params'] or 0)} %",
          f"- paramètres numériques v2 retrouvés en v1 (médiane) : {med(lambda r: r['concordance']['precision_params'] or 0)} %",
          f"- résultats numériques v1 retrouvés en v2 (médiane) : {med(lambda r: r['concordance']['rappel_resultats'] or 0)} %",
          f"- résultats numériques v2 retrouvés en v1 (médiane) : {med(lambda r: r['concordance']['precision_resultats'] or 0)} %",
          f"- quantités de réactifs v1 retrouvées en v2 (médiane) : {med(lambda r: r['concordance']['rappel_reactifs'] or 0)} %",
          f"- conflits sur valeurs univoques (même grandeur, même voie appariée, valeurs différentes) : paramètres {sum(r['concordance']['conflits_params'] for r in rows)}, résultats {sum(r['concordance']['conflits_resultats'] for r in rows)}",
          "", "## Vocabulaire et coût", "",
          f"- noms ajoutés au vocabulaire par les agents v2 : {sum(r['ajouts_vocabulaire'] for r in rows)} (médiane {med(lambda r: r['ajouts_vocabulaire'])} par publication)",
          f"- jetons par publication, médiane : v1 {med(lambda r: r['jetons_v1'])} (toutes passes, quand mesurées) ; v2 {med(lambda r: r['jetons_v2'])} (extraction seule)", "",
          "## Par publication", "", "| PMCID | voies v1/v2 | résultats v1/v2 | réglages v2 | liés v2 | littérature v2 | couverture tableaux v1/v2 | rappel résultats v1→v2 | ajouts vocab. |", "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| {r['pmcid']} | {r['v1']['voies']}/{r['v2']['voies']} | {r['v1']['resultats']}/{r['v2']['resultats']} | {r['v2']['reglages']} | {r['v2']['resultats_lies']} | {r['v2']['litterature']} | {r['couverture_v1']['tableaux']}/{r['couverture_v2']['tableaux']} | {r['concordance']['rappel_resultats']} | {r['ajouts_vocabulaire']} |")
    open("audits/v2/comparaison_v1_v2.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L[:60]))


if __name__ == "__main__":
    main()
