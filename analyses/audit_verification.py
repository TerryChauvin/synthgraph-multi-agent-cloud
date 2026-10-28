#!/usr/bin/env python3
"""Contrôles de vérification de la base (points 2 à 7 de l'audit de contenu) :
2. branches sans résultat propre ; 3. stœchiométrie nominale des précurseurs contre la formule du produit ;
4. complétude contre verdict de la critique scientifique ; 5. variation d'une branche → effet mesuré ;
6. synonymes de noms de paramètres ; 7. couverture des conversions SI.
Usage : python3 -I analyses/audit_verification.py → docs/audit_contenu/data/verif_*.json. Ne modifie pas la base."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path[:0] = [HERE, ROOT]
os.chdir(ROOT)  # chemins relatifs à la racine du dépôt
import collections, json, math, os, re, sqlite3, statistics, sys
from audit_contenu import canon_prop, norm_unit, METHOD_RE

MASSES = {"H": 1.008, "He": 4.003, "Li": 6.94, "Be": 9.012, "B": 10.81, "C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998, "Ne": 20.18, "Na": 22.99, "Mg": 24.305, "Al": 26.982, "Si": 28.085, "P": 30.974, "S": 32.06, "Cl": 35.45, "Ar": 39.95, "K": 39.098, "Ca": 40.078, "Sc": 44.956, "Ti": 47.867, "V": 50.942, "Cr": 51.996, "Mn": 54.938, "Fe": 55.845, "Co": 58.933, "Ni": 58.693, "Cu": 63.546, "Zn": 65.38, "Ga": 69.723, "Ge": 72.63, "As": 74.922, "Se": 78.971, "Br": 79.904, "Kr": 83.798, "Rb": 85.468, "Sr": 87.62, "Y": 88.906, "Zr": 91.224, "Nb": 92.906, "Mo": 95.95, "Ru": 101.07, "Rh": 102.906, "Pd": 106.42, "Ag": 107.868, "Cd": 112.414, "In": 114.818, "Sn": 118.71, "Sb": 121.76, "Te": 127.6, "I": 126.904, "Cs": 132.905, "Ba": 137.327, "La": 138.905, "Ce": 140.116, "Pr": 140.908, "Nd": 144.242, "Sm": 150.36, "Eu": 151.964, "Gd": 157.25, "Tb": 158.925, "Dy": 162.5, "Ho": 164.93, "Er": 167.259, "Tm": 168.934, "Yb": 173.045, "Lu": 174.967, "Hf": 178.49, "Ta": 180.948, "W": 183.84, "Re": 186.207, "Os": 190.23, "Ir": 192.217, "Pt": 195.084, "Au": 196.967, "Hg": 200.592, "Tl": 204.38, "Pb": 207.2, "Bi": 208.98, "Th": 232.038, "U": 238.029}
NONMETAL = {"H", "O", "C", "N"}
TOK = re.compile(r"([A-Z][a-z]?)(\d*\.?\d*)|(\()|(\))(\d*\.?\d*)")


def parse_formula(f):
    """Composition élémentaire d'une formule simple (parenthèses, hydrates '·xH2O'). None si non lisible."""
    if not f:
        return None
    f = f.replace("−", "-").replace("–", "-").split("@")[0].strip()
    if re.search(r"[a-z]{3,}|\s|/|\[|=|%", f):
        return None
    parts = re.split(r"[·•.]", f)
    total = collections.Counter()
    for part in parts:
        m = re.match(r"^(\d*\.?\d*)(.*)$", part)
        mult = float(m.group(1)) if m.group(1) else 1.0
        s = m.group(2)
        stack = [collections.Counter()]
        pos = 0
        while pos < len(s):
            t = TOK.match(s, pos)
            if not t:
                return None
            pos = t.end()
            if t.group(1):
                el, n = t.group(1), float(t.group(2)) if t.group(2) else 1.0
                if el not in MASSES:
                    return None
                stack[-1][el] += n
            elif t.group(3):
                stack.append(collections.Counter())
            elif t.group(4):
                if len(stack) < 2:
                    return None
                inner = stack.pop()
                n = float(t.group(5)) if t.group(5) else 1.0
                for k, v in inner.items():
                    stack[-1][k] += v * n
        if len(stack) != 1 or not stack[0]:
            return None
        for k, v in stack[0].items():
            total[k] += v * mult
    return total if total else None


def molar_mass(comp):
    return sum(MASSES[k] * v for k, v in comp.items())


def moles(amount, unit, comp):
    u = (unit or "").strip().lower().replace("μ", "µ")
    if amount is None:
        return None
    if u in ("mol",):
        return amount
    if u in ("mmol",):
        return amount / 1e3
    if u in ("µmol", "umol"):
        return amount / 1e6
    if comp and u in ("g", "mg", "kg"):
        m = molar_mass(comp)
        return amount / m * {"g": 1, "mg": 1e-3, "kg": 1e3}[u]
    return None


def num(s):
    if s is None:
        return None
    m = re.search(r"-?\d+(?:[.,]\d+)?", str(s))
    return float(m.group().replace(",", ".")) if m else None


def spearman(x, y):
    n = len(x)
    if n < 3:
        return None
    rx = {v: i for i, v in enumerate(sorted(x))}
    ry = {v: i for i, v in enumerate(sorted(y))}
    a = [rx[v] for v in x]
    b = [ry[v] for v in y]
    ma, mb = sum(a) / n, sum(b) / n
    num_ = sum((p - ma) * (q - mb) for p, q in zip(a, b))
    den = math.sqrt(sum((p - ma) ** 2 for p in a) * sum((q - mb) ** 2 for q in b))
    return num_ / den if den else None


PARAM_RULES = [("temperature", r"^temp|temperature|_temp$|^t_"), ("duration", r"duration|^time$|_time$|^time_|dwell|hold"), ("heating_rate", r"heating_rate|ramp|heat_rate"), ("cooling_rate", r"cooling|quench_rate"),
    ("stirring_speed", r"stir|agitation|shaking|rpm$"), ("milling_speed", r"milling|rotation_speed|^speed$"), ("centrifuge_speed", r"centrifug"), ("spin_speed", r"spin"), ("atmosphere", r"atmosph|^gas$|ambient|environment"),
    ("gas_flow", r"flow"), ("pressure", r"pressure|vacuum_level"), ("ph", r"^ph$|^ph_|_ph$"), ("concentration", r"concentration|molarity|^conc"), ("volume", r"volume|^vol_|_vol$"), ("molar_ratio", r"ratio"),
    ("power", r"power|wattage"), ("frequency", r"frequency"), ("potential_current", r"potential|voltage|current|bias"), ("addition_rate", r"addition|injection_rate|drip|dropwise"), ("repetitions", r"repetition|cycles?$|number_of|^n_"),
    ("wash_solvent", r"wash_solvent|solvent$"), ("thickness", r"thickness"), ("fill_fraction", r"fill"), ("wavelength_irradiation", r"wavelength|irradiance|light|lamp|laser"), ("distance", r"distance|gap"), ("mass", r"^mass|weight|loading")]
PARAM_RE = [(c, re.compile(r)) for c, r in PARAM_RULES]


def canon_param(n):
    n = (n or "").lower()
    for c, r in PARAM_RE:
        if r.search(n):
            return c
    return "autre"


def main():
    c = sqlite3.connect("synthese.db"); q = lambda s, *a: c.execute(s, a).fetchall()
    out = "docs/audit_contenu/data/"
    papers = {r[0]: r[1] for r in q("select id,pmcid from papers where critic_status='done'")}
    routes = {r[0]: dict(id=r[0], paper=r[1], parent=r[2], label=r[3], kind=r[4], method=r[5] or "", comp=r[6], family=r[7] or "autre", formula=r[8], material=r[9]) for r in q("select r.id,r.paper_id,r.parent_route_id,r.branch_label,r.kind,r.method,r.completeness_score,m.family,m.formula,m.name from synthesis_routes r left join materials m on m.id=r.material_id") if r[1] in papers}
    children = collections.defaultdict(list)
    for r in routes.values():
        if r["parent"]:
            children[r["parent"]].append(r["id"])
    outcomes = collections.defaultdict(list)
    for rid, prop, vn, unit in q("select route_id,property,value_num,unit from outcomes"):
        if rid in routes:
            outcomes[rid].append((canon_prop(prop)[0], vn, norm_unit(unit), prop))
    carac = collections.Counter(r[0] for r in q("select route_id from characterizations"))
    variations = collections.defaultdict(list)
    for rid, p, vn, vt, unit, pv in q("select route_id,parameter,value_num,value_text,unit,parent_value from route_variations"):
        if rid in routes:
            variations[rid].append(dict(parameter=p, vn=vn, vt=vt, unit=unit, pv=pv))
    plaus = {r[0]: (r[1] or "").replace("invérifiable", "inverifiable") for r in q("select route_id,verdict from plausibility")}
    feas = {r[0]: r[1] for r in q("select route_id,feasibility from plausibility")}
    D = {}

    # ---------------- 2. branches mortes
    br = [r for r in routes.values() if r["parent"]]
    rows = []
    for r in br:
        own = [o for o in outcomes[r["id"]]]
        rows.append(dict(pmcid=papers[r["paper"]], voie=r["label"], famille=r["family"], n_resultats=len(own), n_numeriques=sum(1 for o in own if o[1] is not None), n_carac=carac.get(r["id"], 0), n_variations=len(variations[r["id"]]), morte=len(own) == 0 and carac.get(r["id"], 0) == 0, sans_variation=len(variations[r["id"]]) == 0))
    byf = collections.defaultdict(list)
    for x in rows:
        byf[x["famille"]].append(x)
    D["verif_branches"] = [dict(famille=f, branches=len(xs), sans_resultat=sum(1 for x in xs if x["n_resultats"] == 0), pct_sans_resultat=round(100 * sum(1 for x in xs if x["n_resultats"] == 0) / len(xs), 1), mortes=sum(1 for x in xs if x["morte"]), pct_mortes=round(100 * sum(1 for x in xs if x["morte"]) / len(xs), 1), sans_variation=sum(1 for x in xs if x["sans_variation"]), resultats_par_branche=round(sum(x["n_resultats"] for x in xs) / len(xs), 1)) for f, xs in sorted(byf.items(), key=lambda x: -len(x[1]))]
    D["verif_branches"].append(dict(famille="toutes", branches=len(rows), sans_resultat=sum(1 for x in rows if x["n_resultats"] == 0), pct_sans_resultat=round(100 * sum(1 for x in rows if x["n_resultats"] == 0) / len(rows), 1), mortes=sum(1 for x in rows if x["morte"]), pct_mortes=round(100 * sum(1 for x in rows if x["morte"]) / len(rows), 1), sans_variation=sum(1 for x in rows if x["sans_variation"]), resultats_par_branche=round(sum(x["n_resultats"] for x in rows) / len(rows), 1)))
    D["verif_branches_mortes_liste"] = [dict(pmcid=x["pmcid"], voie=x["voie"], famille=x["famille"], n_variations=x["n_variations"]) for x in rows if x["morte"]]

    # ---------------- 3. stœchiométrie nominale contre formule du produit
    reag = collections.defaultdict(list)
    for rid, name, formula, role, amount, unit in q("select route_id,name,formula,role,amount,unit from reagents"):
        if rid in routes:
            reag[rid].append(dict(name=name, formula=formula, role=role, amount=amount, unit=unit))
    st = []
    nb_base = 0; nb_formule = 0; nb_quant = 0
    for r in routes.values():
        if r["parent"] or r["kind"] != "material":
            continue
        nb_base += 1
        prod = parse_formula(r["formula"])
        if not prod:
            continue
        nb_formule += 1
        metals = [e for e in prod if e not in NONMETAL and prod[e] > 0]
        if len(metals) < 2:
            continue
        el_moles = collections.Counter(); nprec = 0
        for g in reag[r["id"]]:
            if g["role"] not in ("precursor", "dopant"):
                continue
            comp = parse_formula(g["formula"])
            n = moles(g["amount"], g["unit"], comp)
            if n is None or not comp:
                continue
            nprec += 1
            for e, k in comp.items():
                if e in metals:
                    el_moles[e] += n * k
        have = [e for e in metals if el_moles[e] > 0]
        if len(have) < 2:
            continue
        nb_quant += 1
        e1, e2 = sorted(have, key=lambda e: -prod[e])[:2]
        r_prod = prod[e1] / prod[e2]
        r_nom = el_moles[e1] / el_moles[e2]
        dev = math.log(r_nom / r_prod)
        st.append(dict(pmcid=papers[r["paper"]], voie=r["label"], famille=r["family"], formule=r["formula"], elements=f"{e1}/{e2}", rapport_formule=round(r_prod, 3), rapport_nominal=round(r_nom, 3), ecart_pct=round(100 * (r_nom / r_prod - 1), 1), classe="≤10 %" if abs(dev) <= math.log(1.1) else "10–50 %" if abs(dev) <= math.log(1.5) else "50–200 %" if abs(dev) <= math.log(3) else ">200 %", n_precurseurs=nprec))
    st.sort(key=lambda x: -abs(x["ecart_pct"]))
    D["verif_stoechiometrie"] = st
    D["verif_stoechiometrie_resume"] = [dict(voies_base=nb_base, formule_lisible=nb_formule, controlables=nb_quant, **{k: sum(1 for x in st if x["classe"] == k) for k in ("≤10 %", "10–50 %", "50–200 %", ">200 %")})]

    # ---------------- 4. complétude contre verdict
    vc = collections.defaultdict(list)
    for rid, v in plaus.items():
        if rid in routes and routes[rid]["comp"] is not None:
            vc[v].append(routes[rid]["comp"])
    D["verif_completude_verdict"] = [dict(verdict=v, voies=len(xs), completude_moyenne=round(statistics.mean(xs), 2), completude_mediane=round(statistics.median(xs), 2), pct_sup_0_8=round(100 * sum(1 for x in xs if x >= 0.8) / len(xs), 1), pct_inf_0_5=round(100 * sum(1 for x in xs if x < 0.5) / len(xs), 1)) for v, xs in sorted(vc.items(), key=lambda x: -len(x[1]))]
    fc = collections.defaultdict(list)
    for rid, v in feas.items():
        if rid in routes and routes[rid]["comp"] is not None:
            fc[v].append(routes[rid]["comp"])
    D["verif_completude_faisabilite"] = [dict(faisabilite=v, voies=len(xs), completude_moyenne=round(statistics.mean(xs), 2), pct_sup_0_8=round(100 * sum(1 for x in xs if x >= 0.8) / len(xs), 1), pct_inf_0_5=round(100 * sum(1 for x in xs if x < 0.5) / len(xs), 1)) for v, xs in sorted(fc.items(), key=lambda x: -len(x[1]))]
    allc = [(routes[rid]["comp"], 1 if v == "non_reproductible" else 0) for rid, v in feas.items() if rid in routes and routes[rid]["comp"] is not None]
    rho = spearman([a for a, _ in allc], [b for _, b in allc]) if allc else None
    D["verif_completude_verdict"].append(dict(verdict="corrélation complétude × non reproductible (Spearman)", voies=len(allc), completude_moyenne=round(rho, 3) if rho is not None else None, completude_mediane=None, pct_sup_0_8=None, pct_inf_0_5=None))

    # ---------------- 5. variation → effet
    pairs = 0; var_num = 0; var_with_pair = 0; cmp_rows = []
    series = collections.defaultdict(list)  # (parent, parameter) -> [(value, branch id)]
    for rid, vs in variations.items():
        r = routes[rid]
        par = r["parent"]
        if not par:
            continue
        for v in vs:
            pv = num(v["pv"])
            if v["vn"] is None or pv is None:
                continue
            var_num += 1
            po = {(cp, u): vn for cp, vn, u, _ in outcomes[par] if vn is not None}
            bo = {(cp, u): vn for cp, vn, u, _ in outcomes[rid] if vn is not None}
            shared = [k for k in bo if k in po and k[0] != "autre"]
            if shared:
                var_with_pair += 1
                pairs += len(shared)
                for k in shared:
                    if po[k]:
                        cmp_rows.append(dict(pmcid=papers[r["paper"]], voie=r["label"], parametre=v["parameter"], valeur=v["vn"], valeur_parent=pv, propriete=k[0], unite=k[1], resultat_parent=po[k], resultat_branche=bo[k], variation_pct=round(100 * (bo[k] / po[k] - 1), 1)))
            series[(par, v["parameter"])].append((v["vn"], rid))
    ser_rows = []
    for (par, p), lst in series.items():
        if len(lst) < 2:
            continue
        members = [(val, rid) for val, rid in lst]
        props = collections.Counter(k for _, rid in members for k in {(cp, u) for cp, vn, u, _ in outcomes[rid] if vn is not None and cp != "autre"})
        for k, n in props.items():
            if n < 3:
                continue
            xs, ys = [], []
            for val, rid in members:
                vals = [vn for cp, vn, u, _ in outcomes[rid] if (cp, u) == k and vn is not None]
                if vals:
                    xs.append(val); ys.append(statistics.median(vals))
            if len(xs) >= 3 and len(set(xs)) >= 3:
                rho_ = spearman(xs, ys)
                ser_rows.append(dict(pmcid=papers[routes[par]["paper"]], voie_parente=routes[par]["label"], famille=routes[par]["family"], parametre=p, propriete=k[0], unite=k[1], n=len(xs), spearman=round(rho_, 2) if rho_ is not None else None, monotone=rho_ is not None and abs(rho_) >= 0.8, etendue_parametre=f"{min(xs):g}–{max(xs):g}", etendue_propriete=f"{min(ys):g}–{max(ys):g}"))
    ser_rows.sort(key=lambda x: (-(x["n"]), -(abs(x["spearman"]) if x["spearman"] is not None else 0)))
    D["verif_series"] = ser_rows
    D["verif_variation_resume"] = [dict(variations_numeriques=var_num, avec_resultat_comparable=var_with_pair, pct=round(100 * var_with_pair / var_num, 1) if var_num else None, paires_comparables=pairs, series_3_points=len(ser_rows), series_monotones=sum(1 for s in ser_rows if s["monotone"]), pct_monotones=round(100 * sum(1 for s in ser_rows if s["monotone"]) / len(ser_rows), 1) if ser_rows else None)]
    D["verif_paires"] = cmp_rows[:3000]
    # effet par type de paramètre
    eff = collections.defaultdict(list)
    for x in cmp_rows:
        cp_ = canon_param(x["parametre"]); eff[(cp_ if cp_ != "autre" else "reactif (quantite ou nature)", x["propriete"])].append(abs(x["variation_pct"]))
    D["verif_effet_param_prop"] = [dict(parametre=k[0], propriete=k[1], paires=len(v), variation_mediane_pct=round(statistics.median(v), 1)) for k, v in sorted(eff.items(), key=lambda x: -len(x[1])) if len(v) >= 5]

    # ---------------- 6. synonymes de noms de paramètres
    pc = collections.Counter(r[0] for r in q("select name from parameters"))
    groups = collections.defaultdict(list)
    for n, k in pc.items():
        groups[canon_param(n)].append((n, k))
    D["verif_param_synonymes"] = [dict(canonique=g, noms_bruts=len(v), occurrences=sum(k for _, k in v), nom_principal=max(v, key=lambda x: x[1])[0], pct_nom_principal=round(100 * max(k for _, k in v) / sum(k for _, k in v), 1), exemples=", ".join(n for n, _ in sorted(v, key=lambda x: -x[1])[:6])) for g, v in sorted(groups.items(), key=lambda x: -sum(k for _, k in x[1]))]
    D["verif_param_synonymes_resume"] = [dict(noms_distincts=len(pc), groupes=len(groups), occurrences=sum(pc.values()), pct_sous_nom_principal=round(100 * sum(max(k for _, k in v) for v in groups.values()) / sum(pc.values()), 1), noms_vus_une_fois=sum(1 for k in pc.values() if k == 1))]

    # ---------------- 7. conversions SI
    si = collections.defaultdict(lambda: [0, 0])
    units_nc = collections.Counter()
    for n, vn, vs, unit in q("select name,value_num,value_si,unit from parameters where value_num is not null"):
        g = canon_param(n)
        si[g][0] += 1
        if vs is not None:
            si[g][1] += 1
        else:
            units_nc[(g, unit or "(sans unité)")] += 1
    D["verif_si"] = [dict(canonique=g, numeriques=v[0], convertis_si=v[1], pct_si=round(100 * v[1] / v[0], 1), unites_non_converties=", ".join(f"{u} ({k})" for (gg, u), k in units_nc.most_common() if gg == g)[:200]) for g, v in sorted(si.items(), key=lambda x: -x[1][0])]
    tot = sum(v[0] for v in si.values()); tsi = sum(v[1] for v in si.values())
    D["verif_si_resume"] = [dict(parametres_numeriques=tot, convertis=tsi, pct=round(100 * tsi / tot, 1), unites_manquantes=sum(k for (g, u), k in units_nc.items() if u == "(sans unité)"))]

    for k, v in D.items():
        json.dump(v, open(out + k + ".json", "w"), ensure_ascii=False, separators=(",", ":"))
    bundle(D, out)
    print("2. BRANCHES", D["verif_branches"][-1])
    print("3. STOECHIO", D["verif_stoechiometrie_resume"][0]); print("   pires", [(x["pmcid"], x["formule"], x["elements"], x["rapport_formule"], x["rapport_nominal"], x["ecart_pct"]) for x in st[:6]])
    print("4. COMPLETUDE×VERDICT", [(x["verdict"], x["voies"], x["completude_moyenne"], x["pct_sup_0_8"], x["pct_inf_0_5"]) for x in D["verif_completude_verdict"]]); print("   FAISABILITE", [(x["faisabilite"], x["voies"], x["completude_moyenne"], x["pct_sup_0_8"]) for x in D["verif_completude_faisabilite"]])
    print("5. VARIATION", D["verif_variation_resume"][0]); print("   effets", D["verif_effet_param_prop"][:8]); print("   series", [(s["pmcid"], s["parametre"], s["propriete"], s["n"], s["spearman"]) for s in ser_rows[:6]])
    print("6. PARAM SYN", D["verif_param_synonymes_resume"][0]); print("   groupes", [(g["canonique"], g["noms_bruts"], g["occurrences"], g["pct_nom_principal"]) for g in D["verif_param_synonymes"][:12]])
    print("7. SI", D["verif_si_resume"][0]); print("   par type", [(g["canonique"], g["numeriques"], g["pct_si"]) for g in D["verif_si"][:10]])


def bundle(D, data):
    """Jeux regroupés pour l'onglet Vérification du tableau de bord (docs/audit_contenu/dash/)."""
    dash = os.path.join(os.path.dirname(data.rstrip("/")), "dash")
    os.makedirs(dash, exist_ok=True)
    L = lambda k: json.load(open(os.path.join(data, k + ".json"))) if os.path.exists(os.path.join(data, k + ".json")) else []
    tag = lambda rows, t: [dict(table=t, **r) for r in rows]
    M = tag(L("profil_parametres"), "profil") + tag(L("essentiels_methode"), "essentiels") + tag(L("homogeneite_methodes"), "homogeneite") + tag(L("reactifs_quantites"), "reactifs")
    stc = collections.Counter(x["classe"] for x in D["verif_stoechiometrie"])
    C = tag(D["verif_branches"], "branches") + tag([dict(cle=k, n=v) for k, v in stc.items()], "stoech_classe") + tag(D["verif_stoechiometrie"][:60], "stoech") + tag(D["verif_stoechiometrie_resume"], "stoech_resume") \
        + tag(D["verif_completude_verdict"], "completude_verdict") + tag(D["verif_completude_faisabilite"], "completude_faisabilite") + tag(D["verif_variation_resume"], "variation_resume") + tag(D["verif_effet_param_prop"], "effet") \
        + tag(D["verif_param_synonymes"], "param_syn") + tag(D["verif_param_synonymes_resume"], "param_syn_resume") + tag(D["verif_si"], "si") + tag(D["verif_si_resume"], "si_resume")
    json.dump(M, open(os.path.join(dash, "verif_methodes.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    json.dump(C, open(os.path.join(dash, "verif_controles.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    json.dump(D["verif_series"], open(os.path.join(dash, "verif_series.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    R = L("verif_reextraction")
    if R:
        json.dump(R, open(os.path.join(dash, "verif_reextraction.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    print("dash:", dict(verif_methodes=len(M), verif_controles=len(C), verif_series=len(D["verif_series"]), verif_reextraction=len(R)))


if __name__ == "__main__":
    main()
