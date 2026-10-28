# Comparaison v1 / v2

50 publications (`audits/v2/tirage.json`). v1 = pipeline complet (extraction, critique de fidélité, critique scientifique, correction) ; v2 = une seule extraction au format 3 (`RUNBOOK_V2.md`, vocabulaire contrôlé). Script : `analyses/compare_v1_v2.py`.

## Volumes (total sur les publications)

| | v1 | v2 | v2 / v1 |
|---|---|---|---|
| voies | 407 | 414 | 1.02 |
| branches | 277 | 286 | 1.03 |
| voies de calcul | 0 | 10 | — |
| étapes | 966 | 909 | 0.94 |
| paramètres d'étape | 1211 | 1350 | 1.11 |
| réactifs | 650 | 663 | 1.02 |
| résultats | 3278 | 5568 | 1.7 |
| mesures (caractérisations) | 924 | 731 | 0.79 |
| mesures avec appareil ou réglages | 878 | 691 | 0.79 |
| réglages de mesure structurés | 0 | 2084 | — |
| réglages de mesure déclarés absents | 0 | 1105 | — |
| valeurs de la littérature | 0 | 505 | — |
| cases « non cité » (synthèse) | 2847 | 1738 | 0.61 |
| résultats liés à leur mesure | 0 | 5406 | — |
| résultats à mesure non citée | 0 | 57 | — |
| doutes | 597 | 630 | 1.06 |
| annotations | 1023 | 674 | 0.66 |

## Couverture des nombres de l'article

| Source | Nombres | Absents v1 | Absents v2 | Couverture v1 | Couverture v2 |
|---|---|---|---|---|---|
| cellules de tableaux | 1433 | 407 | 63 | 71.6 % | 95.6 % |
| nombres avec unité, résultats | 4489 | 543 | 200 | 87.9 % | 95.5 % |
| nombres avec unité, expérimental | 1183 | 59 | 18 | 95.0 % | 98.5 % |

## Normalisation des noms (part des occurrences dans le vocabulaire v2 ; noms distincts)

| Type | v1 dans le vocabulaire | v2 dans le vocabulaire | noms distincts v1 | noms distincts v2 |
|---|---|---|---|---|
| methodes | 2 % (2/132) | 98 % (165/168) | 127 | 138 |
| actions | 95 % (916/966) | 100 % (909/909) | 470 | 481 |
| parametres | 95 % (1149/1211) | 100 % (1350/1350) | 392 | 511 |
| proprietes | 15 % (487/3278) | 100 % (5568/5568) | 1814 | 3519 |
| techniques | 56 % (515/924) | 100 % (731/731) | 438 | 367 |

## Concordance des valeurs, indépendante des noms

- valeurs numériques v1 retrouvées dans la v2 (même valeur à 2 %, même unité, quel que soit le nom) : 3355 / 3972 (84.5 %)
- même mesure sans exiger la même unité (unités écrites autrement, sans unité d'un côté) : 3552 / 3972 (89.4 %)
- valeurs numériques v2 déjà présentes dans la v1 : 3355 / 6126 (54.8 %) ; le reste est nouveau en v2
- les valeurs v1 non retrouvées sont listées par `python3 -I analyses/compare_v1_v2.py --manquantes <PMCID>`

## Concordance par nom canonique (v1 comme référence, méthode de `compare_blind.py`)

Cette mesure exige le même nom canonique : elle sous-estime l'accord quand la v1 a mal nommé une valeur (par exemple des teneurs XPS en % atomique rangées sous « énergie de liaison »).

- voies v1 appariées à une voie v2 : 360 sur 407
- paramètres numériques v1 retrouvés en v2 (rappel, médiane par publication) : 89.45 %
- paramètres numériques v2 retrouvés en v1 (médiane) : 77.6 %
- résultats numériques v1 retrouvés en v2 (médiane) : 65.95 %
- résultats numériques v2 retrouvés en v1 (médiane) : 42.4 %
- quantités de réactifs v1 retrouvées en v2 (médiane) : 67.75 %
- conflits sur valeurs univoques (même grandeur, même voie appariée, valeurs différentes) : paramètres 0, résultats 66

## Vocabulaire et coût

- noms ajoutés au vocabulaire par les agents v2 : 153 (médiane 2.0 par publication)
- jetons par publication, médiane : v1 639531.0 (toutes passes, quand mesurées) ; v2 233329.0 (extraction seule)

## Par publication

| PMCID | voies v1/v2 | résultats v1/v2 | réglages v2 | liés v2 | littérature v2 | couverture tableaux v1/v2 | rappel résultats v1→v2 | ajouts vocab. |
|---|---|---|---|---|---|---|---|---|
| PMC6769153 | 5/7 | 25/79 | 17 | 71 | 4 | None/None | 18.2 | 1 |
| PMC7447784 | 2/2 | 79/84 | 45 | 84 | 20 | 90.0/100.0 | 70.0 | 0 |
| PMC9323265 | 1/1 | 34/64 | 27 | 63 | 8 | None/None | 75.0 | 2 |
| PMC6812203 | 3/2 | 24/40 | 38 | 40 | 3 | None/None | 57.9 | 1 |
| PMC13315215 | 1/1 | 82/123 | 33 | 122 | 8 | 94.2/100.0 | 17.5 | 1 |
| PMC5238663 | 5/5 | 31/98 | 68 | 96 | 17 | 85.7/100.0 | 77.3 | 0 |
| PMC7254238 | 7/7 | 110/151 | 51 | 151 | 3 | 95.8/100.0 | 65.1 | 3 |
| PMC8866530 | 8/7 | 125/147 | 43 | 146 | 18 | None/None | 50.0 | 2 |
| PMC9419793 | 8/8 | 93/133 | 29 | 122 | 0 | None/None | 70.9 | 7 |
| PMC5680254 | 9/9 | 39/45 | 16 | 43 | 5 | 100.0/100.0 | 86.7 | 4 |
| PMC10523092 | 8/8 | 28/58 | 10 | 49 | 5 | None/None | 100.0 | 2 |
| PMC10077337 | 1/1 | 20/165 | 32 | 165 | 20 | 8.2/100.0 | 55.6 | 2 |
| PMC6994313 | 1/1 | 15/57 | 34 | 57 | 0 | 9.1/72.7 | 93.3 | 3 |
| PMC9908928 | 2/2 | 25/78 | 40 | 68 | 1 | 22.6/100.0 | 50.0 | 4 |
| PMC6301278 | 11/11 | 35/68 | 15 | 66 | 15 | None/None | 78.8 | 1 |
| PMC6199062 | 6/9 | 35/125 | 47 | 125 | 25 | 55.6/100.0 | 17.4 | 0 |
| PMC3503618 | 19/19 | 58/82 | 22 | 81 | 4 | None/None | 75.0 | 3 |
| PMC3414225 | 4/4 | 58/88 | 73 | 82 | 0 | None/None | 75.0 | 3 |
| PMC9667963 | 24/24 | 125/131 | 60 | 130 | 1 | None/None | 85.1 | 6 |
| PMC9061421 | 1/1 | 29/75 | 21 | 70 | 22 | 40.9/100.0 | 54.2 | 2 |
| PMC9041118 | 17/17 | 130/269 | 99 | 265 | 6 | 100.0/100.0 | 61.1 | 16 |
| PMC12191741 | 5/5 | 25/58 | 24 | 58 | 2 | 9.3/66.7 | 81.0 | 2 |
| PMC8434467 | 20/20 | 162/185 | 17 | 185 | 0 | 100.0/100.0 | 70.0 | 1 |
| PMC8717625 | 5/6 | 27/72 | 40 | 72 | 17 | None/None | 61.5 | 5 |
| PMC5593864 | 3/6 | 32/69 | 22 | 69 | 25 | 41.7/100.0 | 76.2 | 5 |
| PMC8495851 | 3/3 | 127/390 | 83 | 384 | 16 | 78.2/94.2 | 43.9 | 4 |
| PMC13209189 | 20/20 | 98/127 | 28 | 107 | 20 | None/None | 16.5 | 3 |
| PMC4531889 | 12/9 | 21/24 | 13 | 24 | 2 | None/None | 42.1 | 5 |
| PMC6025012 | 40/42 | 84/101 | 27 | 95 | 10 | 63.2/100.0 | 75.0 | 1 |
| PMC6562340 | 4/4 | 24/81 | 58 | 78 | 0 | None/None | 22.7 | 5 |
| PMC9054292 | 3/3 | 63/180 | 18 | 178 | 7 | 80.6/100.0 | 71.1 | 1 |
| PMC9612319 | 14/14 | 100/140 | 90 | 130 | 4 | 100.0/100.0 | 82.2 | 1 |
| PMC9057400 | 5/5 | 205/219 | 110 | 212 | 19 | 100.0/100.0 | 69.4 | 1 |
| PMC6154307 | 4/4 | 97/149 | 52 | 147 | 7 | 54.9/100.0 | 15.4 | 10 |
| PMC7503881 | 4/4 | 55/98 | 49 | 98 | 3 | None/None | 63.4 | 5 |
| PMC5727554 | 5/5 | 30/49 | 17 | 48 | 2 | 66.7/44.4 | 76.2 | 5 |
| PMC9079727 | 5/5 | 49/56 | 19 | 56 | 9 | 100.0/100.0 | 62.8 | 2 |
| PMC9059895 | 9/9 | 106/231 | 109 | 231 | 3 | None/None | 62.3 | 3 |
| PMC7672297 | 3/3 | 24/85 | 31 | 81 | 7 | 66.7/100.0 | 73.3 | 2 |
| PMC10262014 | 10/10 | 49/64 | 8 | 64 | 1 | None/None | 66.7 | 0 |
| PMC7578857 | 14/12 | 105/151 | 31 | 149 | 33 | None/None | 41.2 | 2 |
| PMC9369949 | 10/10 | 90/140 | 45 | 133 | 73 | 55.0/97.5 | 85.9 | 1 |
| PMC10169762 | 1/1 | 82/108 | 43 | 90 | 8 | 95.2/100.0 | 57.1 | 0 |
| PMC9418622 | 18/18 | 79/91 | 19 | 91 | 1 | 100.0/100.0 | 100.0 | 1 |
| PMC9136838 | 14/14 | 77/96 | 83 | 92 | 27 | None/None | 65.2 | 4 |
| PMC4973716 | 6/6 | 43/71 | 38 | 69 | 5 | 93.2/100.0 | 50.0 | 0 |
| PMC9999475 | 8/10 | 74/139 | 69 | 137 | 1 | 46.2/100.0 | 56.4 | 5 |
| PMC5882680 | 5/5 | 41/64 | 26 | 63 | 6 | None/None | 51.4 | 0 |
| PMC7563594 | 4/5 | 56/104 | 37 | 104 | 0 | 0.0/0.0 | 91.1 | 9 |
| PMC11931415 | 10/10 | 53/66 | 58 | 65 | 12 | 83.0/83.0 | 100.0 | 7 |
