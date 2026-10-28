"""Vocabulaire contrôlé de l'architecture v2 : chercher, ajouter, fusionner, produire le contexte des agents.

    python3 -I vocab.py construire                         # vocabulaire/vocabulaire.json depuis vocabulaire/initial.py
    python3 -I vocab.py contexte                           # vocabulaire/contexte_agents.md (version courte donnée aux agents)
    python3 -I vocab.py cherche PMCID "<termes>" [--type T] # 5 entrées les plus proches (officiel + ajouts en attente)
    python3 -I vocab.py ajoute PMCID --type T --nom N --definition "…" [--cases "a,b"] [--reglages "a,b"]
                                    [--techniques "A,B"] [--unite U] --ecarte "nom1: raison; nom2: raison"
    python3 -I vocab.py attente                            # ajouts en attente, avec quasi-doublons
    python3 -I vocab.py fusion [--renomme "ancien=nouveau" ...] [--decisions F.json]   # promotion des ajouts (orchestrateur, à chaque palier)

Types : methode, action, parametre, propriete, technique, reglage.
Les ajouts d'un agent vont dans vocabulaire/ajouts/<PMCID>.json (un fichier par publication : pas de conflit
d'écriture entre agents parallèles) ; `cherche` les lit tous, ils sont donc visibles tout de suite.
Un ajout est refusé sans recherche préalable du même type pour la même publication, ou si un nom proche
(score >= SEUIL) n'est pas écarté avec une raison dans --ecarte.
"""
import difflib
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VDIR = ROOT / "vocabulaire"
OFFICIEL = VDIR / "vocabulaire.json"
AJOUTS = VDIR / "ajouts"
CONTEXTE = VDIR / "contexte_agents.md"
TYPES = ("methode", "action", "parametre", "propriete", "technique", "reglage")
SEUIL = 0.55


def norm(s):
    return re.sub(r"[^a-z0-9]+", "_", (s or "").lower()).strip("_")


def charger_officiel():
    if not OFFICIEL.exists():
        raise SystemExit("vocabulaire/vocabulaire.json absent : lancer `python3 -I vocab.py construire`")
    return json.loads(OFFICIEL.read_text(encoding="utf-8"))


def charger_ajouts():
    out = []
    if AJOUTS.exists():
        for f in sorted(AJOUTS.glob("PMC*.json")):
            d = json.loads(f.read_text(encoding="utf-8"))
            for e in d.get("ajouts", []):
                out.append(dict(e, origine=f.stem, statut="en_attente"))
    return out


def toutes_entrees():
    v = charger_officiel()
    return [dict(e, statut="officiel") for e in v["entrees"]] + charger_ajouts(), v["version"]


def index_noms():
    """{type: {nom normalisé ou synonyme: nom}} pour les contrôles de load.py."""
    ent, _ = toutes_entrees()
    idx = {t: {} for t in TYPES}
    for e in ent:
        idx[e["type"]][norm(e["nom"])] = e["nom"]
        for s in e.get("synonymes") or []:
            idx[e["type"]].setdefault(norm(s), e["nom"])
    return idx, {(e["type"], e["nom"]): e for e in ent}


def score(requete, e):
    q = norm(requete)
    qt = set(q.split("_"))
    noms = [e["nom"]] + list(e.get("synonymes") or [])
    s_nom = max(difflib.SequenceMatcher(None, q, norm(n)).ratio() for n in noms)
    mots = set(norm(" ".join(noms) + " " + e.get("definition", "")).split("_"))
    s_mots = len(qt & mots) / max(len(qt), 1)
    return round(max(s_nom, 0.85 * s_mots), 3)


def chercher(requete, typ=None, n=5):
    ent, _ = toutes_entrees()
    ent = [e for e in ent if typ is None or e["type"] == typ]
    return sorted(((score(requete, e), e) for e in ent), key=lambda x: -x[0])[:n]


def fmt(e):
    extra = ""
    if e.get("cases"):
        extra += f" | cases : {', '.join(e['cases'])}"
    if e.get("reglages"):
        extra += f" | réglages : {', '.join(e['reglages'])}"
    if e.get("techniques"):
        extra += f" | mesurée par : {', '.join(e['techniques'])}"
    if e.get("unite"):
        extra += f" | unité : {e['unite']}"
    if e.get("synonymes"):
        extra += f" | synonymes : {', '.join(e['synonymes'])}"
    st = "" if e.get("statut") == "officiel" else f" [ajout en attente, {e.get('origine')}]"
    return f"{e['type']} `{e['nom']}`{st} — {e['definition']}{extra}"


def journal(pmcid):
    return AJOUTS / f".recherches_{pmcid}.log"


def cmd_construire():
    sys.path.insert(0, str(VDIR))
    import initial as I  # noqa: E402
    ent = []
    mots = getattr(I, "MOTS", {})
    for n, d in I.METHODES.items():
        ent.append(dict(type="methode", nom=n, definition=d, synonymes=mots.get(n, [])))
    for n, d, cases in I.ACTIONS:
        ent.append(dict(type="action", nom=n, definition=d, cases=cases, synonymes=mots.get(n, [])))
    for n, d, u in I.PARAMETRES:
        ent.append(dict(type="parametre", nom=n, definition=d, unite=u))
    for n, d, regl, syn in I.TECHNIQUES:
        ent.append(dict(type="technique", nom=n, definition=d, reglages=regl, synonymes=syn))
    for n, d in I.REGLAGES.items():
        ent.append(dict(type="reglage", nom=n, definition=d))
    for n, d, tech in I.PROPRIETES:
        ent.append(dict(type="propriete", nom=n, definition=d, techniques=tech))
    noms = {(e["type"], e["nom"]) for e in ent}
    for e in ent:  # cohérence interne
        for c in e.get("cases") or []:
            assert ("parametre", c) in noms, f"case {c} de {e['nom']} absente des paramètres"
        for r in e.get("reglages") or []:
            assert ("reglage", r) in noms, f"réglage {r} de {e['nom']} absent"
        for t in e.get("techniques") or []:
            assert ("technique", t) in noms, f"technique {t} de {e['nom']} absente"
    old = json.loads(OFFICIEL.read_text(encoding="utf-8")) if OFFICIEL.exists() else None
    v = dict(version=(old["version"] if old else 1), date=time.strftime("%Y-%m-%d"), entrees=ent)
    OFFICIEL.write_text(json.dumps(v, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"ok : {len(ent)} entrées, version {v['version']}")
    cmd_contexte()


def cmd_contexte():
    v = charger_officiel()
    L = [f"# Vocabulaire contrôlé (version {v['version']}, {v['date']})", "",
         "Prends toujours un nom de cette liste. Si aucun ne convient : `python3 -I vocab.py cherche <PMCID> \"<termes>\" --type <type>`, "
         "puis, seulement si rien ne convient, `python3 -I vocab.py ajoute …` avec une définition (voir RUNBOOK_V2.md).", ""]
    titres = dict(methode="Méthodes de synthèse (`methods` de la voie)", action="Actions d'étape (`action`) et leurs cases de grille",
                  parametre="Paramètres d'étape (`parameters[].name`, suffixe de précision permis : `temperature_final`)",
                  technique="Techniques de mesure (`characterizations[].technique`) et leurs réglages attendus",
                  reglage="Réglages de mesure (`characterizations[].settings[].name`)",
                  propriete="Propriétés (`outcomes[].property`, suffixe de précision permis : `lattice_parameter_a`) et techniques qui les mesurent")
    for t in ("methode", "action", "parametre", "technique", "reglage", "propriete"):
        L += [f"## {titres[t]}", ""]
        for e in v["entrees"]:
            if e["type"] != t:
                continue
            extra = ""
            if e.get("cases"):
                extra = f" [cases : {', '.join(e['cases'])}]"
            elif e.get("reglages"):
                extra = f" [réglages : {', '.join(e['reglages'])}]"
            elif e.get("techniques") is not None and t == "propriete":
                extra = f" [{', '.join(e['techniques']) or 'aucune mesure'}]"
            L.append(f"- `{e['nom']}` — {e['definition']}{extra}")
        L.append("")
    CONTEXTE.write_text("\n".join(L), encoding="utf-8")
    print(f"ok : {CONTEXTE.relative_to(ROOT)} ({len(L)} lignes)")


def cmd_cherche(pmcid, requete, typ):
    if typ and typ not in TYPES:
        raise SystemExit(f"type inconnu {typ!r} ; types : {', '.join(TYPES)}")
    AJOUTS.mkdir(parents=True, exist_ok=True)
    with open(journal(pmcid), "a", encoding="utf-8") as f:
        f.write(json.dumps(dict(type=typ, requete=requete, t=time.time())) + "\n")
    for s, e in chercher(requete, typ):
        print(f"{s:.2f}  {fmt(e)}")


def cmd_ajoute(pmcid, args):
    def opt(k, req=False):
        if k in args:
            return args[args.index(k) + 1]
        if req:
            raise SystemExit(f"{k} obligatoire")
        return None
    typ, nom, df = opt("--type", True), opt("--nom", True), opt("--definition", True)
    if typ not in TYPES:
        raise SystemExit(f"type inconnu {typ!r} ; types : {', '.join(TYPES)}")
    if norm(nom) != nom.lower().replace("-", "_") and typ != "technique":
        raise SystemExit("nom en anglais snake_case (lettres, chiffres, _)")
    if re.match(r"^(other|others|autre|misc|miscellaneous|unknown|generic|various)(_|$)", nom, re.I):
        raise SystemExit("refusé : nom générique (other, autre…) ; donner un nom qui dit ce que c'est")
    if len(df) < 25:
        raise SystemExit("définition trop courte : une phrase qui dise ce que le nom désigne")
    log = journal(pmcid)
    recherches = [json.loads(l) for l in log.read_text(encoding="utf-8").splitlines()] if log.exists() else []
    if not any(r.get("type") in (typ, None) for r in recherches):
        raise SystemExit(f"refusé : aucune recherche préalable (`vocab.py cherche {pmcid} \"…\" --type {typ}`)")
    idx, _ = index_noms()
    if norm(nom) in idx[typ]:
        raise SystemExit(f"refusé : `{idx[typ][norm(nom)]}` existe déjà (nom ou synonyme) : l'utiliser")
    ecarte = opt("--ecarte") or ""
    proches = [(s, e) for s, e in chercher(nom + " " + df, typ) if s >= SEUIL]
    manquants = [e["nom"] for s, e in proches if e["nom"].lower() not in ecarte.lower()]
    if manquants:
        raise SystemExit("refusé : noms proches à utiliser ou à écarter avec une raison dans --ecarte "
                         f"(\"nom: raison; …\") : {', '.join(manquants)}\n" + "\n".join(f"  {s:.2f} {fmt(e)}" for s, e in proches))
    e = dict(type=typ, nom=nom, definition=df, ecarte=ecarte, date=time.strftime("%Y-%m-%d %H:%M"))
    if opt("--cases"):
        e["cases"] = [c.strip() for c in opt("--cases").split(",") if c.strip()]
    if opt("--reglages"):
        e["reglages"] = [c.strip() for c in opt("--reglages").split(",") if c.strip()]
    if opt("--techniques"):
        e["techniques"] = [c.strip() for c in opt("--techniques").split(",") if c.strip()]
    if opt("--unite"):
        e["unite"] = opt("--unite")
    for c in e.get("cases") or []:
        if norm(c) not in idx["parametre"]:
            raise SystemExit(f"case {c!r} : paramètre absent du vocabulaire (l'ajouter d'abord, type parametre)")
    for c in e.get("reglages") or []:
        if norm(c) not in idx["reglage"]:
            raise SystemExit(f"réglage {c!r} absent du vocabulaire (l'ajouter d'abord, type reglage)")
    f = AJOUTS / f"{pmcid}.json"
    d = json.loads(f.read_text(encoding="utf-8")) if f.exists() else dict(pmcid=pmcid, ajouts=[])
    d["ajouts"].append(e)
    f.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"ajouté (en attente de fusion, visible tout de suite) : {fmt(dict(e, statut='en_attente', origine=pmcid))}")


def cmd_attente():
    aj = charger_ajouts()
    print(f"{len(aj)} ajouts en attente")
    v = charger_officiel()
    for e in aj:
        proches = [(s, x) for s, x in chercher(e["nom"] + " " + e["definition"], e["type"]) if x is not e and x["nom"] != e["nom"] and s >= SEUIL]
        print(f"- {fmt(e)}")
        for s, x in proches[:3]:
            print(f"    proche {s:.2f} : {x['nom']} ({x.get('statut')})")
    return aj, v


def renomme_extractions(dossier, ren):
    """Applique les renommages (nom exact, ou nom suivi d'un suffixe `_…`) aux extractions d'un dossier."""
    def nv(x):
        if not isinstance(x, str):
            return x
        for a, b in ren.items():
            if x == a:
                return b
            if x.startswith(a + "_"):
                return b + x[len(a):]
        return x
    n = 0
    for f in sorted((ROOT / dossier).glob("PMC*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        avant = json.dumps(d, ensure_ascii=False)
        for r in d.get("routes") or []:
            r["methods"] = [nv(m) for m in r.get("methods") or []] if "methods" in r else r.get("methods")
            if "methods" in r and r["methods"] is None:
                del r["methods"]
            for st in r.get("steps") or []:
                st["action"] = nv(st.get("action"))
                for x in st.get("parameters") or []:
                    x["name"] = nv(x.get("name"))
                if st.get("not_stated"):
                    st["not_stated"] = [nv(x) for x in st["not_stated"]]
            for c in r.get("characterizations") or []:
                c["technique"] = nv(c.get("technique"))
                for x in c.get("settings") or []:
                    x["name"] = nv(x.get("name"))
                if c.get("not_stated"):
                    c["not_stated"] = [nv(x) for x in c["not_stated"]]
            for o in r.get("outcomes") or []:
                o["property"] = nv(o.get("property"))
        for c in d.get("comparisons") or []:
            c["property"] = nv(c.get("property"))
        if json.dumps(d, ensure_ascii=False) != avant:
            f.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
            n += 1
    return n


def cmd_fusion(args):
    """Promeut les ajouts en attente.

    --renomme ancien=nouveau : fusionne un ajout dans un nom existant ou promu (devient synonyme).
    --decisions F.json : {"renomme": {ancien: nouveau}, "refuse": {nom: raison}, "redefinit": {nom: définition},
                          "etend_techniques": {propriété: [techniques]}, "extractions": "dossier"} ;
                          les renommages sont aussi appliqués aux extractions du dossier donné.
    """
    dec = {}
    if "--decisions" in args:
        dec = json.loads(Path(args[args.index("--decisions") + 1]).read_text(encoding="utf-8"))
    ren = dict(dec.get("renomme", {}))
    ren.update(dict(a.split("=", 1) for a in args if "=" in a and not a.endswith(".json")))
    refuse = dec.get("refuse", {})
    v = charger_officiel()
    noms = {(e["type"], e["nom"]): e for e in v["entrees"]}
    n_prom = n_fus = n_ref = 0
    attente = charger_ajouts()
    for e in attente:  # 1. promotion de ce qui n'est ni renommé ni refusé
        if e["nom"] in refuse:
            n_ref += 1
            continue
        if e["nom"] not in ren and (e["type"], e["nom"]) not in noms:
            e2 = {k: e[k] for k in ("type", "nom", "definition", "cases", "reglages", "techniques", "unite") if k in e}
            e2["origine"] = e["origine"]
            v["entrees"].append(e2)
            noms[(e["type"], e["nom"])] = e2
            n_prom += 1
    for e in attente:  # 2. renommages vers un nom officiel ou promu
        if e["nom"] in ren:
            cible = noms.get((e["type"], ren[e["nom"]]))
            if cible is None:
                raise SystemExit(f"cible {ren[e['nom']]!r} introuvable pour {e['nom']!r}")
            cible.setdefault("synonymes", []).append(e["nom"])
            n_fus += 1
    for nom, d in dec.get("redefinit", {}).items():
        cibles = [e for e in v["entrees"] if e["nom"] == nom]
        if not cibles:
            raise SystemExit(f"redefinit : {nom!r} introuvable")
        for e in cibles:
            e["definition"] = d
    for prop, techs in dec.get("etend_techniques", {}).items():
        e = noms.get(("propriete", prop))
        if e is None:
            raise SystemExit(f"etend_techniques : propriété {prop!r} introuvable")
        for t in techs:
            if ("technique", t) not in noms:
                raise SystemExit(f"etend_techniques : technique {t!r} introuvable")
            if t not in (e.get("techniques") or []):
                e.setdefault("techniques", []).append(t)
    v["version"] += 1
    v["date"] = time.strftime("%Y-%m-%d")
    v.setdefault("refuses", {}).update(refuse)
    OFFICIEL.write_text(json.dumps(v, ensure_ascii=False, indent=1), encoding="utf-8")
    arch = VDIR / f"ajouts_fusionnes_v{v['version'] - 1}"
    arch.mkdir(exist_ok=True)
    for f in AJOUTS.glob("PMC*.json"):
        f.rename(arch / f.name)
    n_ext = renomme_extractions(dec["extractions"], ren) if dec.get("extractions") and ren else 0
    print(f"version {v['version']} : {n_prom} promus, {n_fus} fusionnés en synonymes, {n_ref} refusés, "
          f"{len(dec.get('etend_techniques', {}))} propriétés étendues ; {n_ext} extractions renommées")
    cmd_contexte()


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        return
    c = a[0]
    if c == "construire":
        cmd_construire()
    elif c == "contexte":
        cmd_contexte()
    elif c == "cherche":
        typ = a[a.index("--type") + 1] if "--type" in a else None
        cmd_cherche(a[1], a[2], typ)
    elif c == "ajoute":
        cmd_ajoute(a[1], a[2:])
    elif c == "attente":
        cmd_attente()
    elif c == "fusion":
        cmd_fusion([x for x in a[1:] if x != "--renomme"])
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
