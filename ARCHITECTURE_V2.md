# Architecture v2 de l'extraction (28/10/2026)

Mise en œuvre des décisions de `AMELIORATION.md` (§ 4 et 5). La v1 (format 2, `RUNBOOK.md`) reste la base de production ; la v2 est évaluée sur 50 publications déjà extraites en v1, puis comparée (`audits/v2/comparaison_v1_v2.md`).

## 1. Ce qui change par rapport à la v1

| Point | v1 (format 2) | v2 (format 3) |
|---|---|---|
| Noms (méthodes, actions, paramètres, propriétés, techniques) | texte libre, normalisé après coup par `canon.py` (1 383 noms de méthode pour 1 382 voies) | **vocabulaire contrôlé avec définitions** (`vocabulaire/vocabulaire.json`, 324 entrées en version 1), donné en contexte à l'agent ; nom hors liste refusé par `load.py` |
| Ajout d'un nom | — | outil `vocab.py ajoute` : recherche préalable obligatoire, définition, justification face aux noms proches ; accepté directement, visible tout de suite par les autres agents, fusionné à chaque palier de 50 |
| Méthode de synthèse | une chaîne `method` | `methods` : liste de méthodes du vocabulaire (une voie mêle souvent plusieurs méthodes) |
| Grille de synthèse | 7 familles d'actions, mêmes cases quelle que soit la méthode | **une grille par action** du vocabulaire, dont les actions propres à une méthode (traitement hydrothermal : volume d'autoclave, remplissage, refroidissement… ; micro-ondes : puissance, pression ; dépôt par centrifugation : vitesse…) |
| « Non cité » | case remplie ou déclarée, sans vérification de l'absence | idem, plus **avertissement** quand la citation de l'étape contient un indice de la case |
| Réglages de mesure | `conditions` en texte libre, sans citation propre | **`settings`** : un réglage par entrée (nom du vocabulaire, valeur, unité, citation vérifiée) ; **grille par technique** : chaque réglage attendu est extrait ou déclaré absent (`not_stated` de la mesure) |
| Lien résultat → mesure | aucun | `measured_by` : id de la mesure (même voie ou voie parente), ou `not_stated` ; compatibilité technique / propriété vérifiée |
| Périmètre | synthèse et résultats principaux ; littérature, calculs et statistiques ajoutés le 28/10 (table `comparisons`, voies `calcul`) | périmètre complet dès l'extraction : tous les résultats par échantillon (tableaux d'annexe compris), statistiques, littérature, calculs, valeurs de référence en réglages ; réponses aux relecteurs exclues |
| Pipeline évalué | extraction + critique de fidélité + critique scientifique + correction | extraction v2 seule (une passe), critique de fidélité sur un échantillon pour mesurer la justesse |

## 2. Fichiers

| Fichier | Rôle |
|---|---|
| `vocabulaire/initial.py` | vocabulaire initial : méthodes, actions et leurs cases, paramètres, techniques et leurs réglages, réglages, propriétés et les techniques qui les mesurent, mots-clés anglais de recherche |
| `vocabulaire/vocabulaire.json` | vocabulaire officiel versionné (construit par `vocab.py construire`, enrichi par `vocab.py fusion`) |
| `vocabulaire/contexte_agents.md` | version courte (nom + définition d'une ligne, ≈ 9 k jetons) donnée à chaque agent |
| `vocabulaire/ajouts/<PMCID>.json` | ajouts en attente, un fichier par publication (pas de conflit d'écriture entre agents) |
| `vocab.py` | `construire`, `contexte`, `cherche`, `ajoute`, `attente`, `fusion` |
| `RUNBOOK_V2.md` | consigne v2 (complète `RUNBOOK.md`) |
| `load.py` | format 3 : `validate_v3` (noms, méthodes, grille par action, réglages et grille par technique, lien résultat → mesure, avertissements « non cité ») et chargement (`route_methods`, `char_settings`, `characterizations.char_key`, `outcomes.measured_by`, `outcomes.measured_status`) |
| `db.py`, `schema.sql` | chemins surchargeables (`SYNTHESE_DB`, `SYNTHESE_EXTRACT_DIR`), nouvelles tables et colonnes |
| `extractions_v2/` | extractions v2 (format 3) |
| `synthese_v2.db` | base v2 (copie de la base v1 où les publications v2 sont rechargées) ; non versionnée, régénérable : `cp synthese.db synthese_v2.db` puis `SYNTHESE_DB=synthese_v2.db SYNTHESE_EXTRACT_DIR=extractions_v2 python3 -I load.py load <PMCID>` |
| `analyses/compare_v1_v2.py` | comparaison v1 / v2 → `audits/v2/comparaison_v1_v2.md` |
| `audits/v2/` | tirage des 50 publications, modèles de prompts, rapport |

## 3. Déroulé d'une extraction v2

| Moment | L'agent reçoit ou fait | Contrôle |
|---|---|---|
| 1. Démarrage | `RUNBOOK.md`, `RUNBOOK_V2.md`, `vocabulaire/contexte_agents.md`, modèle d'extraction | — |
| 2. Lecture | article entier (annexes, tableaux, légendes), références, figures utiles ; inventaire des échantillons | — |
| 3. Voies | `methods` pris dans la liste ; en cas de doute `vocab.py cherche` | méthode hors liste refusée |
| 4. Étapes | action de la liste, sa grille (cases) remplie ou déclarée absente | grille par action ; avertissement « non cité » suspect |
| 5. Mesures | `id`, technique de la liste, `settings` cités, réglages attendus absents en `not_stated` | grille par technique ; citations des réglages vérifiées |
| 6. Résultats | propriété de la liste, `measured_by` | lien vérifié (id, voie, compatibilité) |
| 7. Littérature, calculs, statistiques | `comparisons`, voies `calcul`, propriété `statistic` | citations vérifiées |
| 8. `load.py check` (format 3) | 0 erreur exigée | — |
| 9. Orchestrateur | contrôle, chargement dans `synthese_v2.db`, revue des ajouts au vocabulaire | fusion du vocabulaire tous les 50 |

## 4. Évaluation sur 50 publications

- Tirage : 50 publications closes en v1, hors pilote de complément et hors test de complétude, réparties par famille au prorata (`audits/v2/tirage.json`, graine 2910).
- Mesures : volumes, couverture des nombres de l'article, normalisation des noms, grilles, liens résultat → mesure, concordance des valeurs avec la v1, ajouts au vocabulaire, jetons ; critique de fidélité (`CRITIQUE.md`) sur un échantillon des extractions v2, comparée aux critiques de la v1.
- Résultats : `audits/v2/comparaison_v1_v2.md` et `audits/v2/rapport.md`.
