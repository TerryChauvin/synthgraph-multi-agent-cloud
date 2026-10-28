# Comparaison v1 / v2

1 publications (`audits/v2/tirage.json`). v1 = pipeline complet (extraction, critique de fidélité, critique scientifique, correction) ; v2 = une seule extraction au format 3 (`RUNBOOK_V2.md`, vocabulaire contrôlé). Script : `analyses/compare_v1_v2.py`.

## Volumes (total sur les publications)

| | v1 | v2 | v2 / v1 |
|---|---|---|---|
| voies | 5 | 7 | 1.4 |
| branches | 4 | 5 | 1.25 |
| voies de calcul | 0 | 1 | — |
| étapes | 9 | 16 | 1.78 |
| paramètres d'étape | 8 | 22 | 2.75 |
| réactifs | 2 | 2 | 1.0 |
| résultats | 25 | 79 | 3.16 |
| mesures (caractérisations) | 10 | 15 | 1.5 |
| mesures avec appareil ou réglages | 10 | 15 | 1.5 |
| réglages de mesure structurés | 0 | 17 | — |
| réglages de mesure déclarés absents | 0 | 26 | — |
| valeurs de la littérature | 0 | 4 | — |
| cases « non cité » (synthèse) | 23 | 28 | 1.22 |
| résultats liés à leur mesure | 0 | 71 | — |
| résultats à mesure non citée | 0 | 2 | — |
| doutes | 3 | 11 | 3.67 |
| annotations | 12 | 11 | 0.92 |

## Couverture des nombres de l'article

| Source | Nombres | Absents v1 | Absents v2 | Couverture v1 | Couverture v2 |
|---|---|---|---|---|---|
| cellules de tableaux | 0 | 0 | 0 | 0.0 % | 0.0 % |
| nombres avec unité, résultats | 93 | 16 | 0 | 82.8 % | 100.0 % |
| nombres avec unité, expérimental | 7 | 0 | 0 | 100.0 % | 100.0 % |

## Normalisation des noms (part des occurrences dans le vocabulaire v2 ; noms distincts)

| Type | v1 dans le vocabulaire | v2 dans le vocabulaire | noms distincts v1 | noms distincts v2 |
|---|---|---|---|---|
| methodes | 0 % (0/1) | 100 % (2/2) | 1 | 2 |
| actions | 100 % (9/9) | 100 % (16/16) | 9 | 9 |
| parametres | 75 % (6/8) | 100 % (22/22) | 5 | 11 |
| proprietes | 20 % (5/25) | 100 % (79/79) | 25 | 78 |
| techniques | 70 % (7/10) | 100 % (15/15) | 10 | 10 |

## Concordance des valeurs, indépendante des noms

- valeurs numériques v1 retrouvées dans la v2 (même valeur à 2 %, même unité, quel que soit le nom) : 22 / 22 (100.0 %)
- valeurs numériques v2 déjà présentes dans la v1 : 22 / 67 (32.8 %) ; le reste est nouveau en v2
- les valeurs v1 non retrouvées sont listées par `python3 -I analyses/compare_v1_v2.py --manquantes <PMCID>`

## Concordance par nom canonique (v1 comme référence, méthode de `compare_blind.py`)

Cette mesure exige le même nom canonique : elle sous-estime l'accord quand la v1 a mal nommé une valeur (par exemple des teneurs XPS en % atomique rangées sous « énergie de liaison »).

- voies v1 appariées à une voie v2 : 1 sur 5
- paramètres numériques v1 retrouvés en v2 (rappel, médiane par publication) : 100.0 %
- paramètres numériques v2 retrouvés en v1 (médiane) : 50.0 %
- résultats numériques v1 retrouvés en v2 (médiane) : 18.2 %
- résultats numériques v2 retrouvés en v1 (médiane) : 4.1 %
- quantités de réactifs v1 retrouvées en v2 (médiane) : 100.0 %
- conflits sur valeurs univoques (même grandeur, même voie appariée, valeurs différentes) : paramètres 0, résultats 0

## Vocabulaire et coût

- noms ajoutés au vocabulaire par les agents v2 : 1 (médiane 1 par publication)
- jetons par publication, médiane : v1 0 (toutes passes, quand mesurées) ; v2 0 (extraction seule)

## Par publication

| PMCID | voies v1/v2 | résultats v1/v2 | réglages v2 | liés v2 | littérature v2 | couverture tableaux v1/v2 | rappel résultats v1→v2 | ajouts vocab. |
|---|---|---|---|---|---|---|---|---|
| PMC6769153 | 5/7 | 25/79 | 17 | 71 | 4 | None/None | 18.2 | 1 |
