# Architecture v2 : évaluation sur 50 publications (28–29/10/2026)

Demande de l'utilisateur : appliquer les changements de `AMELIORATION.md`, lancer une extraction complète sur 50 publications déjà étudiées, noter la nouvelle architecture (v2), comparer v1 et v2. Architecture : `ARCHITECTURE_V2.md`. Consigne : `RUNBOOK_V2.md`. Données : `extractions_v2/`, `synthese_v2.db` (non versionnée, régénérable). Détails chiffrés : `audits/v2/comparaison_v1_v2.md`, `audits/v2/critiques_v1_v2.md`. Constats publication par publication : `audits/v2/notes_v2.md`.

## 1. En bref

- **Plus complet.** Une seule passe v2 reprend 95,6 % des cellules de tableaux de l'article (v1 après 4 passes : 71,6 %) et 95,5 % des nombres avec unité des résultats (v1 : 87,9 %). Elle contient 1,7 fois plus de résultats que la v1, plus 2 088 réglages de mesure cités, 505 valeurs de la littérature et 10 voies de calcul que la v1 n'avait pas.
- **Aussi juste.** La critique de fidélité, faite sur 10 extractions avec la même consigne qu'en v1, trouve 42 constats contre 84 en v1 sur ce que les deux versions contiennent, et 6 graves (2 faux, 4 attributions) contre 10. Les 2 « faux » de la v2 sont deux annotations d'interprétation, aucune valeur extraite. Toutes les citations sont exactes (50/50 publications à 0 erreur au contrôle).
- **Nommé de façon homogène.** 100 % des noms d'actions, de paramètres, de propriétés et de techniques, et 98 % des méthodes, sont dans le vocabulaire contrôlé (v1 : 2 % des méthodes, 15 % des propriétés). Les agents ont ajouté 153 noms définis (≈ 3 par publication) ; aucun nom générique ne passe depuis l'interdiction.
- **Moins cher.** 233 k jetons par publication (médiane) pour l'extraction v2, contre 640 k pour les 4 passes de la v1 ; 430 k avec la critique de fidélité ajoutée.
- **Pas encore prêt à remplacer la v1 tel quel.** Six défauts de conception sont à corriger d'abord (section 5), dont deux importants : les grilles de synthèse des actions courantes sont plus pauvres qu'en v1, et il n'existe pas de place pour les témoins et échantillons commerciaux.

## 2. Ce qui a été fait

| Étape | Détail |
|---|---|
| Tirage | 50 publications closes en v1, réparties par famille, hors pilote et hors test de complétude (`audits/v2/tirage.json`, graine 2910) |
| Extraction v2 | 50 agents Sonnet, effort `high`, 3 en parallèle, consigne `audits/v2/T_ext_v2.txt` ; lecture indépendante (interdiction de lire la v1) ; une limite d'usage (22 h 40 UTC), 2 agents repris par message |
| Contrôle et chargement | `load.py check` format 3 puis chargement dans `synthese_v2.db` (`audits/v2/charger_v2.sh`) ; 0 erreur sur les 50 |
| Règle ajoutée en cours de route | à la demande de l'utilisateur : noms génériques (`other`, `autre`, `misc`, `unknown`, `mode`…) refusés par `load.py` et `vocab.py` ; `other` retiré du vocabulaire initial ; 2 extractions déjà faites corrigées |
| Critique de fidélité | 10 publications, Sonnet `high`, consigne `CRITIQUE.md` + contrôles du format 3 (`audits/v2/T_fid_v2.txt`), sortie `critiques_v2/` |
| Fusion du vocabulaire | `vocab.py fusion --decisions audits/v2/fusion_decisions.json` : version 2 (476 entrées), 151 noms promus, 1 synonyme, 1 refus, 20 propriétés reliées à leurs nouvelles techniques ; 50 extractions rechargées, 0 erreur |
| Comparaison | `analyses/compare_v1_v2.py`, `analyses/compare_critiques_v1_v2.py` |

## 3. Résultats

### 3.1 Volumes (50 publications)

| | v1 (4 passes) | v2 (1 passe) |
|---|---|---|
| voies / branches | 407 / 277 | 414 / 286 |
| résultats | 3 278 | 5 568 |
| résultats liés à leur mesure | — | 5 406 (97 %) ; 57 à mesure non citée |
| réglages de mesure cités / déclarés absents | — | 2 088 / 1 105 |
| valeurs de la littérature | — | 505 |
| voies de calcul | 0 | 10 |
| doutes | 597 | 631 |
| annotations | 1 023 | 676 |

### 3.2 Couverture des nombres de l'article

| Source | v1 | v2 |
|---|---|---|
| cellules de tableaux (1 433) | 71,6 % | 95,6 % |
| nombres avec unité, résultats (4 489) | 87,9 % | 95,5 % |
| nombres avec unité, partie expérimentale (1 183) | 95,0 % | 98,5 % |

### 3.3 Concordance des valeurs

- 84,5 % des valeurs numériques de la v1 se retrouvent dans la v2 (même valeur à 2 %, même unité), 89,4 % sans exiger la même écriture d'unité. Les valeurs restantes sont surtout des lectures de figure différentes (la v1 lit 11 %, la v2 arrondit à 5 près ; PMC13209189 en concentre 81) et des unités écrites autrement.
- 55 % des valeurs v2 étaient déjà dans la v1 : le reste est nouveau.
- Les 66 « conflits » relevés par la comparaison par nom sont des artefacts d'appariement des voies (libellés différents entre v1 et v2) : vérifiés sur PMC9369949 et PMC7578857, les valeurs v1 et v2 sont identiques et justes, rangée par rangée.

### 3.4 Critiques de fidélité (10 publications)

Même consigne qu'en v1 (`CRITIQUE.md`) ; la v1 est critiquée avant sa correction, la v2 telle qu'extraite.

| Constats | v1 | v2, périmètre commun | v2, propres au format 3 (`v3:`) |
|---|---|---|---|
| faux | 2 | 2 (deux annotations d'interprétation) | 0 |
| attribution | 8 | 4 | 12 |
| manquant | 21 | 11 | 29 |
| non cité à tort | 3 | 1 | 9 |
| déduit | 13 | 8 | 6 |
| mineur | 37 | 16 | 40 |
| **total** | **84** | **42** | **96** |

Verdict des 10 critiques v2 : « corrections mineures » partout. Les 12 attributions `v3:` viennent surtout de deux causes : des résultats de témoins ou d'essais à blanc rangés sur la voie du composite (PMC9057400, PMC7447784, PMC6769153), et des liens résultat → mesure trop larges (une seule mesure pour une série qui fait varier la condition de la mesure). Les défauts de valeur rapportés sont rares : couple XPS inversé que l'article lui-même contredit (PMC9667963), une capacité d'échange rangée sur la mauvaise voie (PMC6025012).

### 3.5 Vocabulaire

| | |
|---|---|
| vocabulaire initial | 324 entrées (version 1) |
| ajouts des agents | 153 (63 propriétés, 59 réglages, 14 techniques, 8 méthodes, 7 actions, 2 paramètres) ; médiane 2 par publication, maximum 16 (PMC9041118 : diffraction neutronique, PDF, RMN à gradient) |
| après fusion | 476 entrées (version 2) |
| avertissements « technique inhabituelle » | ≈ 145 avant la fusion, 0 après (les propriétés existantes ne connaissaient pas les techniques ajoutées) |
| avertissements restants | 62, tous structurels : variation qui ajoute un réactif absent du parent (45), branche sans résultat dans l'article (11), voie sans réactif (6) |
| effet visible | méthode choisie selon la définition et non le mot de l'article (PMC4531889 : « hydrothermal » à 90 °C en étuve → `chemical_bath_deposition`) |

### 3.6 Coût

| Passe | Jetons (médiane par publication) | Total |
|---|---|---|
| v1 : extraction + fidélité + science + correction | 640 k | — |
| v2 : extraction | 233 k | 11,8 M (50) |
| v2 : critique de fidélité | 198 k | 2,0 M (10) |

## 4. Ce qui marche

1. La grille par technique (réglages cités ou déclarés absents) et le lien résultat → mesure sont remplis à 97 % sans erreur de contrôle ; les critiques qui les ont contrôlés un à un les trouvent justes (PMC6199062 : 125 liens cohérents ; PMC9667963 : 130 liens, 0 erreur ; PMC8866530 : liens corrects).
2. L'agent lit beaucoup plus de tableaux et d'annexes : c'est la principale différence de contenu avec la v1.
3. La recherche obligatoire avant ajout (`vocab.py cherche`) empêche les doublons d'écriture ; un seul vrai doublon de sens en 153 ajouts (`biomass_extraction` / `precursor_preparation`), un refus automatique justifié (SAXS proposé alors que « saxs » était, à tort, synonyme de XRD).
4. L'interdiction des noms génériques tient : aucun `other_…` après la règle.

## 5. Ce qui ne marche pas encore (à corriger avant de généraliser)

| # | Défaut | Constat | Correction proposée |
|---|---|---|---|
| 1 | **Grilles de synthèse trop pauvres pour les actions courantes** | 2,6 cases par étape en v2 contre 3,3 en v1 ; `dissolve`, `filter` sans case, `mix` et `disperse` avec la seule durée, `add` sans débit ni température, `stir` sans température ; d'où 1 738 cases « non cité » contre 2 847 en v1 | enrichir les cases des 15 actions les plus employées (température, durée, agitation, volume, débit d'ajout, nombre de lavages…) avant toute généralisation |
| 2 | **Pas de place pour les témoins et les échantillons sans voie** | 10 publications sur 50 : résultats de témoins (Pt/C commercial, CoFe2O4, P25, essais à blanc, antibiotiques de référence) rangés sur la voie du composite avec un suffixe, mis dans `comparisons` (réservé à la littérature), en annotation, ou en voie `commercial_material` ; c'est la première source d'attributions fausses des critiques | une voie `kind: reference` sans étapes (fournisseur, pureté), qui peut porter mesures et résultats |
| 3 | **Mesures communes dupliquées** | une section « Characterization » est recopiée sur chaque voie de base (4 publications) | mesures de niveau article, que `measured_by` peut viser depuis toute voie |
| 4 | **Pas d'état « sans objet »** | une case de grille qui n'a pas de sens (lumière d'un essai thermique) est déclarée « non citée » | troisième état `not_applicable` dans la grille |
| 5 | **Réglages fourre-tout du vocabulaire initial** | `measurement_conditions` (« Autres conditions… », 18 emplois), `method` (14), `analysis_method` (91) : contraires à la règle « aucun nom générique », écrits par l'orchestrateur ; un agent a aussi créé `acquisition_parameters` (refusé à la fusion, 5 entrées découpées à la main) | remplacer par des réglages précis ; refuser un réglage dont la valeur énumère plusieurs grandeurs |
| 6 | **Contrôles de `load.py` incomplets** | nombres avec signe ou milliers séparés par une espace (« − 19.5 », « 87 685.45 ») et nombres en lettres non reconnus ; citations de moins de 8 caractères refusées (valeurs isolées de tableaux aplatis) ; une seule citation par réactif (pureté perdue quand quantité et pureté sont à deux endroits, 3 cas) ; noms de propriété de `comparisons` non vérifiés ; champ `role` de `method_sources` non contrôlé (« autre ») | corriger ces cinq points dans `load.py` |

Défauts du corpus vus en passant (déjà connus) : exposants aplatis par `sections.py` (« × 108 ») et doubles liaisons remplacées par des images SVG (C=O, C=C) dans 2 publications.

Points de règle à fixer : un réglage visible seulement sur une figure (tension MEB sur le bandeau d'image) est lu par un agent et déclaré « non cité » par un autre ; une unité absente de l'article (« at 2θ » sans « ° ») a été ajoutée par un agent.

## 6. Recommandation

1. Corriger les défauts 1, 2, 5 et 6 (vocabulaire initial et `load.py`, sans agent), puis 3 et 4 (format) : c'est une v2.1.
2. Refaire l'extraction v2.1 sur 10 des 50 publications (≈ 2,5 M jetons) et vérifier que les cases « non cité » remontent au moins au niveau de la v1 et que les témoins ont leur voie.
3. Si le test tient, généraliser aux 500 publications avec le pipeline extraction v2.1 + critique de fidélité + correction (≈ 0,58 M jetons par publication en comptant une correction, ≈ 290 M en tout, contre ≈ 320 M pour refaire la v1), fusion du vocabulaire tous les 50.

La base v1 (`synthese.db`) reste la base de production : rien n'y a été modifié.
