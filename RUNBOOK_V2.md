# Consignes d'extraction, architecture v2 (format 3)

Ce document **complète** `RUNBOOK.md` : toutes ses règles restent valables (citation exacte, rien de déduit, toutes les variations, inventaire des échantillons, grille de reproductibilité, figures, annexes, `method_sources`, annotations, journal). En cas de différence, ce document l'emporte. Architecture décrite dans `ARCHITECTURE_V2.md`.

## 1. Fichiers et contrôle

- Sortie : `extractions_v2/<PMCID>.json`, avec `"format": 3`.
- Contrôle, à relancer jusqu'à 0 erreur :
  `SYNTHESE_EXTRACT_DIR=extractions_v2 SYNTHESE_DB=synthese_v2.db python3 -I load.py check <PMCID>`
- Journal : `journaux/<PMCID>_extraction_v2.md`.
- Ne lance jamais `load.py load`.

## 2. Vocabulaire contrôlé (nouveau)

Lis `vocabulaire/contexte_agents.md` en entier **avant d'écrire** : c'est la liste des noms permis, chacun avec sa définition. Elle couvre les méthodes de synthèse, les actions d'étape (avec leurs cases de grille), les paramètres d'étape, les techniques de mesure (avec leurs réglages attendus), les réglages de mesure et les propriétés (avec les techniques qui les mesurent).

1. **Prends toujours un nom de la liste**, en suivant sa définition plutôt que le mot de l'article : « kept in a Teflon-lined autoclave at 180 °C » → action `hydrothermal_treatment` ; « FE-SEM » → technique `SEM` ; « specific surface area » → propriété `BET_surface_area`. Un paramètre ou une propriété peut porter un suffixe de précision après le nom de la liste (`temperature_final`, `lattice_parameter_a`, `specific_capacity_1C`).
2. **En cas d'hésitation, cherche** : `python3 -I vocab.py cherche <PMCID> "<termes en anglais ou en français>" --type <methode|action|parametre|propriete|technique|reglage>`. La recherche porte sur la liste officielle et sur les ajouts déjà faits par les autres agents.
3. **Seulement si rien ne convient, ajoute** :
   `python3 -I vocab.py ajoute <PMCID> --type <type> --nom <nom_snake_case> --definition "<une phrase qui dit ce que le nom désigne>" [--cases "a,b"] [--reglages "a,b"] [--techniques "A,B"] [--unite U] --ecarte "<nom proche>: <pourquoi il ne convient pas>; …"`
   - une action ajoutée donne ses cases de grille (`--cases`, paramètres de la liste) ; une technique ajoutée donne ses réglages attendus (`--reglages`) ; une propriété ajoutée donne les techniques qui la mesurent (`--techniques`, vide si ce n'est pas une mesure) ;
   - l'outil refuse un ajout sans recherche préalable, un nom qui existe déjà, ou un nom proche non écarté avec une raison ;
   - un ajout est accepté tout de suite et visible par les autres agents ; il sera relu à la fusion du palier. **Ajoute peu** : un ou deux noms par article au plus, et jamais pour une simple variante d'écriture d'un nom existant (`other` existe pour l'exceptionnel).

## 3. Nouvelles clés du format 3

### 3.1 Méthodes de la voie

Toute voie de base (sauf `kind: calcul`) porte `"methods": ["hydrothermal", "thermal_treatment"]` : une ou plusieurs méthodes de la liste, dans l'ordre où elles interviennent. `method` (texte libre court) reste permis comme description.

### 3.2 Grille de synthèse par action

La grille d'une étape est celle de son **action** dans le vocabulaire (ses cases). Chaque case est extraite (paramètre de même nom, suffixe permis) ou déclarée dans `not_stated` de l'étape. Les cases sont plus nombreuses qu'en format 2 (agitation, refroidissement, volume et remplissage d'autoclave, puissance, mode d'addition…) : cherche chacune dans tout l'article avant de la déclarer absente. Le contrôle **avertit** quand une case déclarée absente a un indice dans la citation de l'étape (« three times », « 500 rpm », « at 80 °C ») : vérifie et extrais.

### 3.3 Mesures : identifiant, réglages structurés, grille par technique

Chaque entrée de `characterizations` porte :
- `"id"` : identifiant unique dans l'article (`"xrd_1"`, `"bet_HCN"`), repris par les résultats ;
- `"technique"` : un nom de technique de la liste ;
- `"instrument"` : appareil tel qu'écrit, ou `null` ;
- `"settings"` : **un réglage par entrée**, chacun avec sa citation : `{"name": "radiation", "value_text": "Cu Kα (λ = 1.5406 Å)", "quote": "…"}`, `{"name": "scan_range", "value_text": "10–80°", "quote": "…"}`, `{"name": "degassing", "value_text": "150 °C for 6 h under vacuum", "quote": "…"}`. Les noms viennent de la liste des réglages ; un nombre seul va dans `value_num` avec `unit` ;
- `"not_stated"` : les réglages attendus de la technique que l'article ne donne pas. Le contrôle exige que chaque réglage attendu soit dans `settings` ou dans `not_stated` ;
- `"result"` et `"quote"` comme avant. **N'utilise plus `conditions`** (texte libre non vérifié).

Une même technique peut avoir plusieurs entrées (mesures différentes, échantillons différents). Les valeurs d'étalonnage d'une analyse (temps de rétention, droites d'étalonnage) tiennent dans une seule entrée par technique. Une valeur de référence utilisée pour calculer un résultat (densité théorique, facteur de Scherrer, coefficient d'extinction, fiche JCPDS) est un réglage de la mesure qui la calcule.

Une mesure décrite une fois pour toute la série (section « Characterization ») va sur la voie de base ; les branches l'utilisent par héritage.

### 3.4 Lien résultat → mesure

Chaque résultat dont la propriété est une mesure (la liste indique les techniques qui la mesurent) porte `"measured_by": "<id>"` : l'id d'une mesure de **cette voie ou d'une voie parente**. Si l'article ne dit pas comment la valeur a été obtenue, `"measured_by": "not_stated"`. Le contrôle avertit quand la technique est inhabituelle pour la propriété.

### 3.5 Périmètre complet (rappel du test de complétude)

Extrais aussi, avec citation :
- **tous les résultats de chaque échantillon** : valeurs du texte, des tableaux et des annexes, positions de pics (XRD, XPS, FTIR, Raman) attribuées à un échantillon, paramètres d'ajustement de modèles (isothermes, cinétique, thermodynamique), mesures sur dispositifs ;
- **les statistiques** de l'article (R², p, écarts-types, ANOVA) en `outcomes` de la voie, propriété `statistic` avec suffixe (`statistic_r2_langmuir`) et `measured_by` de la mesure concernée si elle existe ;
- **les valeurs de la littérature** citées pour comparer, dans la liste de premier niveau `"comparisons"` (`material`, `property`, `value_num` ou `value_text`, `unit`, `conditions`, `ref_id` si l'article donne le renvoi, `route` facultatif, `quote`), jamais en `outcomes` ;
- **les calculs** (DFT, simulation, modèle) dans une voie à part `"kind": "calcul"`, sans parent, `methods` facultatif, étapes = paramètres de calcul, `outcomes` avec la propriété `calculated_value` (suffixe permis) et `measured_by` vers une mesure de technique `calculation`.

Ne sont pas des sources : les fichiers de réponses aux relecteurs (« Peer Review File », « response to reviewers ») ; n'en extrais rien. Pas pertinent : numéros de figures, de références, d'équations ; barres d'échelle ; constantes universelles.

## 4. Exemple (extrait)

```json
{
  "pmcid": "PMC0000000",
  "format": 3,
  "routes": [
    {"label": "ZnO-120", "parent": null, "methods": ["hydrothermal"], "method": "hydrothermal growth of ZnO nanorods",
     "steps": [
       {"order": 2, "action": "hydrothermal_treatment", "quote": "transferred into a 100 mL Teflon-lined autoclave and kept at 120 °C for 12 h",
        "parameters": [
          {"name": "temperature", "value_num": 120, "unit": "°C", "quote": "kept at 120 °C for 12 h"},
          {"name": "duration", "value_num": 12, "unit": "h", "quote": "kept at 120 °C for 12 h"},
          {"name": "autoclave_volume", "value_num": 100, "unit": "mL", "quote": "transferred into a 100 mL Teflon-lined autoclave"}],
        "not_stated": ["fill_fraction", "heating_rate", "cooling"]}],
     "characterizations": [
       {"id": "xrd_1", "technique": "XRD", "instrument": "Rigaku D/MAX-2500", "result": "pure wurtzite",
        "quote": "all diffraction peaks can be indexed to wurtzite ZnO",
        "settings": [{"name": "radiation", "value_text": "Cu Kα", "quote": "using Cu Kα radiation"},
                     {"name": "crystallite_size_method", "value_text": "Scherrer equation", "quote": "calculated by the Scherrer equation"}],
        "not_stated": ["scan_range", "scan_step"]}],
     "outcomes": [
       {"property": "crystallite_size", "value_num": 28, "unit": "nm", "measured_by": "xrd_1", "quote": "the crystallite size was 28 nm"},
       {"property": "yield", "value_num": 85, "unit": "%", "quote": "with a yield of 85%"}]}
  ],
  "comparisons": [
    {"material": "ZnO nanorods (ref. 12)", "property": "band_gap", "value_num": 3.37, "unit": "eV", "ref_id": "B12", "quote": "…"}
  ]
}
```

## 5. Réponse finale

Texte brut, court : nombre de voies, de branches, de doutes ; nombre de mesures, de réglages extraits et de réglages déclarés absents ; nombre de résultats liés à une mesure et de `measured_by: not_stated` ; noms ajoutés au vocabulaire (avec leur type) ; résultat du dernier `load.py check` ; ce qui t'a semblé fragile.
