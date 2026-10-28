"""Compare les critiques de fidélité de la v1 (critiques/<PMCID>.json, faites sur l'extraction v1 avant correction)
et de la v2 (critiques_v2/<PMCID>.json, sur l'extraction v2 en une passe).

Usage : python3 -I analyses/compare_critiques_v1_v2.py  → audits/v2/critiques_v1_v2.md
"""
import collections
import json
import os

SEV = ["faux", "attribution", "manquant", "non_cite_a_tort", "deduit", "mineur"]


def load(path):
    if not os.path.exists(path):
        return None
    d = json.load(open(path, encoding="utf-8"))
    c = collections.Counter(f.get("severity") for f in d.get("findings") or [])
    v3 = sum(1 for f in d.get("findings") or [] if str(f.get("where", "")).startswith("v3:"))
    return d.get("verdict"), c, v3, len(d.get("findings") or [])


def main():
    pubs = sorted(f[:-5] for f in os.listdir("critiques_v2") if f.startswith("PMC") and f.endswith(".json"))
    L = ["# Critiques de fidélité : v1 contre v2", "",
         "v1 : critique de l'extraction v1 avant correction (même consigne `CRITIQUE.md`). "
         "v2 : critique de l'extraction v2 en une passe (`audits/v2/T_fid_v2.txt`, qui ajoute les contrôles propres au format 3, préfixés `v3:`).", "",
         "| Publication | verdict v1 | verdict v2 | " + " | ".join(f"{s} v1/v2" for s in SEV) + " | total v1/v2 | dont v3: |",
         "|---|---|---|" + "---|" * len(SEV) + "---|---|"]
    T1, T2, V3 = collections.Counter(), collections.Counter(), 0
    n1 = n2 = 0
    for p in pubs:
        a = load(f"critiques/{p}.json")
        b = load(f"critiques_v2/{p}.json")
        if not b:
            continue
        va, ca, _, na = a if a else ("—", collections.Counter(), 0, 0)
        vb, cb, v3, nb = b
        T1 += ca; T2 += cb; V3 += v3; n1 += na; n2 += nb
        L.append(f"| {p} | {va} | {vb} | " + " | ".join(f"{ca[s]}/{cb[s]}" for s in SEV) + f" | {na}/{nb} | {v3} |")
    L.append("| **total** | | | " + " | ".join(f"{T1[s]}/{T2[s]}" for s in SEV) + f" | {n1}/{n2} | {V3} |")
    L += ["", f"Constats graves (faux + attribution) : v1 {T1['faux'] + T1['attribution']}, v2 {T2['faux'] + T2['attribution']}.",
          "Les constats `v3:` portent sur ce qui n'existe pas en v1 (réglages, lien résultat → mesure, nom du vocabulaire) : ils ne sont pas comparables un à un."]
    open("audits/v2/critiques_v1_v2.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L[-4:]))


if __name__ == "__main__":
    main()
