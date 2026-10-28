# Amélioration de la base : état des lieux, décisions et pistes

Document de travail ouvert le 28/10/2026 (discussion avec l'utilisateur, rien n'est encore implémenté de ce qui est marqué « à faire »). Il rassemble ce que les tests ont montré, les décisions prises, le fonctionnement actuel du pipeline et les changements envisagés. Résultats chiffrés et verdicts des tests : `audits/registre_tests.md`.

## 1. Objectif

Une extraction **complète** de chaque article, sur trois axes :

1. **les paramètres de synthèse** qui permettent de refaire le matériau ;
2. **les propriétés** du matériau synthétisé ;
3. **les réglages de mesure** qui ont conduit à chaque propriété (appareil, conditions, méthode de calcul), reliés à la valeur qu'ils ont produite.

Tout ce que l'article ne donne pas est **marqué comme absent**, pour pouvoir plus tard étudier ces trous (recombinaison, imputation, lecture des références citées).

## 2. Ce que les tests ont montré (28/10/2026)

| Axe | État | Source |
|---|---|---|
| Paramètres de synthèse | quasi complet : « synthèse complète » dans 20 publications sur 20 du test | `audits/test_completude.md` |
| Propriétés | résultats principaux présents ; résultats secondaires absents (positions de pics, tableaux d'annexe, ajustements de modèles, mesures sur dispositifs : 15 à 130 ajouts par publication) | `audits/test_completude.md`, `audits/couverture_valeurs.md` |
| Réglages de mesure | point faible : réglages présents dans la base très en dessous de ce que disent les articles ; aucun lien entre une valeur et sa mesure | `audits/audit_grilles.md` |
| Littérature, statistiques, calculs | absents avant le test (périmètre élargi à la demande de l'utilisateur) | `audits/test_completude.md` |
| Sélection des publications à compléter | inutile : les publications témoins sont aussi lacunaires que les autres | `audits/test_completude.md` |

Chiffres clés :
- couverture des nombres de l'article : 81 % des cellules de tableaux, 88 % des nombres avec unité du texte (500 publications) ; 99,9 % et 98,8 % après complétion sur les 20 du test ;
- grille de synthèse : remplie à 100 % (imposée par `load.py`), mais ≈ 10 % des cases « non cité » suspectes (la valeur figure dans la citation de l'étape) ;
- réglages hors grille ni extraits ni déclarés absents : remplissage d'autoclave 95 %, vitesse d'agitation 84 %, refroidissement 53 %, pression ou vide 43 % ;
- réglages de caractérisation dans la base contre dans l'article : plage 2θ 46 % / 97 %, électrolyte 33 % / 99 %, masse active 1 % / 44 %, dégazage BET 32 % / 45 % ;
- fidélité des ajouts du test : 1 faux sur 630 contrôlés, hors une erreur de source corrigée (réponses aux relecteurs prises pour l'article).

## 3. Fonctionnement actuel du pipeline

### 3.1 Circuit d'une publication

```
article (XML Europe PMC)
  │ sections.py + enrich.py : texte, légendes, annexes, références, figures
  ▼
1. Extracteur (Sonnet) ──► extractions/PMCID.json
  │ load.py check (automatique, bloquant)
  ▼ load.py load → synthese.db (+ canon.py : noms canoniques)
2. Critique de fidélité (Sonnet)   ┐ en parallèle,
3. Critique scientifique (Opus)    ┘ chacun écrit un fichier critique
  │ critic_load.py → table critiques
  ▼
4. Orchestrateur : tranche chaque constat (corriger / rejeter), écrit les décisions
  ▼
5. Agent de correction (Sonnet) : applique les décisions dans le JSON
  │ load.py check + load + contrôle de quelques ajouts par l'orchestrateur
  ▼
Clôture. Tous les 50 articles : audit.py + relecture intégrale de 1 publication sur 5 (agent en lecture seule)
```

### 3.2 Contexte reçu par chaque agent

| Tour | Modèle | Ce qu'il lit | Ce qu'il ne voit pas | Ce qu'il écrit |
|---|---|---|---|---|
| 1. Extraction | Sonnet, `high` | `RUNBOOK.md` (26 ko : règles, grille, format JSON), l'article en entier (texte, annexes, légendes), la liste des références, les figures utiles, une extraction modèle (`PMC6199062.json`) | aucune critique, aucune autre publication, **aucune liste de méthodes ni de paramètres** (seulement des exemples de noms dans le RUNBOOK) | le JSON et un journal de décisions |
| 2. Fidélité | Sonnet, `high` | `CRITIQUE.md`, l'article **d'abord** (sa propre liste d'échantillons), puis l'extraction, et les figures pour les valeurs lues sur figure | le web, le journal de l'extracteur | des constats typés : faux, manquant, déduit, attribution, « non cité » à tort, mineur |
| 3. Science | Opus, `high` | `PLAUSIBILITE.md`, une vue de l'extraction sans citations, l'article, `references/fondateurs.md` et `constantes.md`, une dizaine de recherches web | — (il ne corrige rien) | un verdict par voie, des calculs de stœchiométrie, des problèmes avec sources |
| 4. Décision | orchestrateur (Opus) | les deux critiques, l'article aux passages concernés | — | les décisions par constat |
| 5. Correction | Sonnet, `high` | `PROMPT_CORRECTION.md`, les deux critiques, les décisions, les passages de l'article | — | le JSON corrigé ; chaque constat marqué corrigé ou rejeté, avec la raison |

Passes ajoutées le 28/10/2026 : complément (`PROMPT_COMPLEMENT.md`, guidé par la sonde), test de complétude (`PROMPT_TEST_COMPLETUDE.md`, lecture intégrale et ajout seulement), critique des ajouts (`audits/pilote_complement/CRITIQUE_AJOUTS.md`).

### 3.3 Création et vérification d'une donnée

1. **Création** : l'extracteur écrit chaque valeur avec la valeur (`value_num` ou `value_text`), l'unité telle qu'écrite et la citation mot pour mot.
2. **Vérification mécanique** (`load.py check`, refus si erreur) :
   - la citation existe exactement dans le texte de l'article (après normalisation des espaces) ;
   - le nombre apparaît dans sa propre citation, sauf valeur lue sur figure ;
   - unités présentes, bornes physiques (pH entre 0 et 14, température possible, durée positive) ;
   - structure cohérente : parents, branches avec leur variation, étapes numérotées ;
   - grille de synthèse remplie : chaque case est citée ou déclarée « non cité ».
3. **Normalisation** au chargement : `canon.py` rattache le nom brut à un nom canonique, et la conversion SI est faite, chacun dans une colonne séparée.
4. **Deux lectures indépendantes** : la critique de fidélité relit l'article (bonne valeur, bonne voie, rien d'oublié) ; la critique scientifique juge la vraisemblance. C'est la seule vérification de **l'attribution** (bon échantillon, bonne étape).
5. **Audit de palier** : citations et nombres revérifiés, relecture intégrale de 20 % des publications, échantillon de 30 valeurs relu.

### 3.4 Ce qui n'est pas vérifié aujourd'hui

- **Les noms** : rien n'impose un nom de méthode, de paramètre ou de propriété (682 noms de paramètres pour 37 concepts, 16 577 noms de propriétés).
- **Les « non cité »** : `load.py` vérifie qu'une case est remplie, pas que l'absence est réelle.
- **Les chaînes `conditions`** et les `value_text` ne sont pas comparées au texte au-delà de la citation globale.
- **Le lien résultat → mesure** n'existe pas.
- **La grille de synthèse** ne dépend pas de la méthode (7 familles d'étapes, mêmes cases pour une hydrothermale, un sol-gel ou un dépôt de film) ; **il n'existe aucune grille de caractérisation**. La liste par méthode (`ESS` dans `analyses/audit_parametres.py`) ne sert qu'à l'audit. Le nom de méthode est du texte libre ; son classement en 29 classes ne concorde qu'à 69 % avec la signature des étapes.
- **Omission plutôt qu'hallucination** : le modèle prend les réglages saillants (puissance, mode d'addition) et laisse les routiniers (« stirred at 500 rpm ») quand ils ne sont pas dans la grille. L'erreur inverse porte sur les « non cité » déclarés à tort (≈ 10 %).

## 4. Décisions de l'utilisateur (28/10/2026)

1. **Grilles aussi complètes que possible**, de synthèse (par étape et par méthode) et de caractérisation (par technique). Tout réglage absent de l'article est **marqué**.
2. **Vocabulaire contrôlé extensible** : l'agent prend d'abord un nom de la liste ; s'il en ajoute un (méthode, paramètre, propriété, technique), le nom est **accepté directement**, avec une **définition rédigée par l'agent**.
3. **Toutes les méthodes ont une définition** ; la liste des noms avec leurs définitions est donnée **en contexte à chaque agent**.
4. **Revue continue** des noms ajoutés (à chaque chargement, pas seulement en fin de passe) ; un nom ajouté devient disponible pour les agents suivants.
5. **Les trous seront étudiés plus tard**, avec les références citées par les articles.
6. **Périmètre élargi** (déjà en place) : valeurs de référence dans `characterizations.conditions`, statistiques en `outcomes`, valeurs de la littérature dans la table `comparisons`, calculs DFT en voies `kind: calcul`.

## 5. Changements envisagés (à discuter puis valider)

### 5.1 Vocabulaire avec définitions

- Table `vocabulaire` étendue : nom, type (méthode, paramètre, propriété, technique, réglage de mesure), **définition**, unité attendue, synonymes, origine (liste initiale ou ajouté par un agent, avec la publication), version.
- Liste initiale construite à partir de `canon.py` (37 paramètres, 95 propriétés, 29 méthodes) ; une définition pour chaque entrée.
- Fichier de contexte généré pour les agents (par exemple `docs/vocabulaire/contexte_agents.md`), regénéré à chaque ajout.
- `load.py check` : un nom absent de la liste doit porter une définition ; il est alors inscrit dans la table et la liste suivante le contient.
- La critique de fidélité vérifie aussi qu'un nom ajouté ne doublonne pas un nom existant.
- Point ouvert : avec plusieurs agents en parallèle, deux noms peuvent être créés en même temps pour le même concept ; la revue continue les fusionne à la fin du lot.

### 5.2 Grilles

- **Synthèse, deux niveaux** : par type d'étape (grille actuelle élargie : agitation, refroidissement, pression ou vide, vitesse d'addition, etc.) et par méthode (autoclave : volume, remplissage, refroidissement ; micro-ondes : puissance, pression ; dépôt par centrifugation : vitesse, durée…). Les deux niveaux sont nécessaires, car une voie mêle souvent plusieurs méthodes (hydrothermale puis calcination). Méthode choisie dans la liste, ou ajoutée avec définition.
- **Caractérisation, par technique** : réglages attendus (XRD : rayonnement, plage, pas, méthode de taille ; BET : gaz, température, dégazage ; électrochimie : électrolyte, électrodes, masse active, vitesse de balayage ; catalyse : masse, concentration, source lumineuse ; etc.), chacun cité ou déclaré absent.
- **Lien résultat → mesure** : colonne `outcomes.characterization_id` (ou équivalent), remplie par l'agent, vérifiée par `load.py` (technique compatible avec la propriété).
- **États d'une case** : cité / non cité (cherché, absent de l'article) / **non cherché** (la case n'existait pas quand l'article a été extrait). Sans ce troisième état, l'élargissement d'une grille transforme des cases jamais regardées en faux trous. Typage possible plus tard : « non applicable », « renvoyé à une référence ».
- **Contrôle des « non cité »** au chargement : signaler une case déclarée absente quand la citation de l'étape contient un motif de cette case (°C, rpm, « three times »…).

### 5.3 Passe de complétion sur toute la base

- Consigne du test de complétude, corrigée des cinq défauts relevés : fichiers de relecture par les pairs exclus ; une condition ajoutée = une entrée avec sa citation ; valeurs d'étalonnage en une entrée par technique ; conditions de mesure absentes en doute, pas en `not_stated` ; lien résultat → mesure.
- Sur les 480 publications restantes (les 20 du test sont faites), avec les nouvelles grilles et le vocabulaire en contexte ; critique des ajouts sur 1 publication sur 5.
- Coût mesuré : 160–175 k jetons par publication (jusqu'à 395 k pour une publication avec annexes et calculs lourds), soit ≈ 80 M pour 480 publications, plus ≈ 15 M de critiques (≈ 10 à 12 fenêtres de 5 h).
- Préalable : régler le poids du dépôt (`.git` ≈ 3 Go, `synthese.db` ≈ 63 Mo pour une limite GitHub de 100 Mo), car la base sera rechargée en entier.

### 5.4 Ordre proposé

1. Vocabulaire avec définitions et grilles (sans agent, une session).
2. Pilote de 10 publications avec la nouvelle consigne.
3. Décision sur la passe complète, après règlement du poids du dépôt.

### 5.5 Corrections proposées pour les quatre défauts (discussion du 28/10/2026)

**a. « Non cité » à tort**
- Détection automatique au chargement (`load.py`, avertissement, pas erreur : faux positifs possibles) : une case déclarée absente dont la citation de l'étape contient un motif de la case (°C, h, rpm, « three times », atmosphère) ; pureté ou fournisseur déclarés absents alors qu'une phrase de l'article nomme le réactif avec un grade ou un fournisseur, ou qu'une phrase générale couvre tous les réactifs. Mesure actuelle : ≈ 10 % des « non cité » de température, durée et pureté (`audits/audit_grilles.md`).
- Correction de l'existant : passe ciblée par agent, qui ne reçoit que la liste des cases suspectes avec leur passage ; pour chacune, valeur extraite avec citation ou absence confirmée avec raison. Petit coût (quelques dizaines de milliers de jetons par publication concernée).
- Prévention : la règle et le contrôle automatique empêchent la récidive ; la critique de fidélité garde sa catégorie « non cité à tort ».

**b. Chaînes `conditions` des mesures**
- Problème : texte libre sans citation propre, non vérifié (les agents y ajoutent du texte en fin de chaîne).
- Structure proposée : chaque caractérisation porte une liste de réglages `settings`, un par réglage (`name` pris dans le vocabulaire des réglages de la technique, `value_num` ou `value_text`, `unit`, `quote`), vérifiés comme les paramètres de synthèse (citation exacte, nombre dans la citation). Les réglages attendus de la technique absents de l'article vont dans un `not_stated` de la caractérisation. L'ancienne chaîne reste en lecture (`conditions_text`), sans être utilisée pour l'analyse.
- Correction de l'existant : pas de découpage automatique fiable ; fait par la passe de complétion (l'agent retrouve la citation de chaque réglage).

**c. Lien résultat → mesure**
- Structure proposée : chaque résultat porte la référence de la caractérisation qui l'a produit (même voie ou voie parente, comme l'héritage des étapes). `load.py` vérifie que la caractérisation existe et que la technique est compatible avec la propriété (table propriété → techniques admises dans le vocabulaire : surface BET → BET ; taille de cristallite → XRD ; bande interdite → UV-vis…).
- Correction de l'existant, en deux temps : (1) lien automatique quand une seule caractérisation compatible existe dans la voie ou ses parents ; (2) les cas ambigus ou sans mesure vont à la passe de complétion. Estimation sur la base actuelle (39 527 résultats) : 56 % ont une propriété rattachable à une technique ; parmi eux, 40 % ont une seule mesure candidate (lien automatique), 41 % plusieurs (choix par agent), 19 % aucune (mesure à créer ou à déclarer absente).

**d. Grille de synthèse indépendante de la méthode**
- Idée : la méthode se réalise dans une étape. Le vocabulaire des actions d'étape s'enrichit d'actions propres à une méthode (traitement hydrothermal ou solvothermal, chauffage micro-ondes, dépôt par centrifugation, broyage, pyrolyse sous gaz…), chacune avec sa définition et ses cases (autoclave : volume, remplissage, température, durée, refroidissement ; micro-ondes : puissance, température, pression ; dépôt par centrifugation : vitesse, durée, volume déposé ; broyage : vitesse, durée, rapport billes/poudre). La voie porte la liste de ses méthodes, prise dans le vocabulaire.
- Les deux niveaux (étape générique et méthode) se rejoignent ainsi dans une seule grille par action, plus simple à contrôler dans `load.py`.
- Correction de l'existant : reclassement automatique des actions existantes (par exemple « heat » avec un autoclave en équipement → traitement hydrothermal), vérifié par échantillon ; les nouvelles cases sont marquées « non cherché » jusqu'à la passe de complétion.

**Ordre** : (0) relecture du vocabulaire initial avec l'utilisateur ; (1) vocabulaire avec définitions et outil `vocab.py` (méthodes, actions, réglages par technique, table propriété → techniques) ; (2) évolutions de `load.py` (avertissements « non cité », réglages structurés, lien résultat → mesure, grille par action, état « non cherché ») ; (3) liens automatiques et reclassement des actions sur l'existant ; (4) pilote de 10 publications ; (5) passe de complétion, qui traite en même temps les « non cité » suspects, les réglages structurés et les liens ambigus.

### 5.6 Vocabulaire contrôlé en pratique : outil, déroulé de l'agent, fusion par palier (discussion du 28/10/2026)

**Constat** : 1 383 noms de méthode différents pour 1 382 voies de base (chaque agent écrit sa phrase) ; 176 actions d'étape, dont 30 couvrent 92 % des étapes et 53 n'apparaissent qu'une fois (doublons d'orthographe comme `recrystallize` / `recrystallise`). Sans garde-fou, un agent crée son propre nom dès qu'il hésite.

**Outil `vocab.py`** (script lancé par l'agent, comme `load.py check`) :
- `vocab.py cherche "<termes>"` : les 5 entrées les plus proches, avec définition, cases de grille et synonymes ; cherche dans le vocabulaire officiel **et** dans les ajouts en attente de tous les agents ;
- `vocab.py ajoute --type <méthode|action|paramètre|propriété|technique|réglage> --nom … --definition "…" [--cases "…"] --ecarte "nom1: raison, nom2: raison"` : refusé sans recherche préalable ou sans justification face aux noms proches ; signale les quasi-doublons ; une fois justifié, le nom est accepté directement (décision de l'utilisateur) et écrit dans le fichier d'ajouts de l'agent (`vocabulaire/ajouts/<PMCID>.json`), pas dans la table commune (aucun conflit d'écriture entre agents parallèles).

**Déroulé de l'agent extracteur** :

| Moment | Ce que l'agent reçoit ou fait | Garde-fou |
|---|---|---|
| 1. Démarrage | `RUNBOOK.md` + vocabulaire officiel en version courte (nom + définition d'une ligne ; ≈ 400 entrées, ≈ 10 k jetons) | il connaît la liste avant de lire l'article |
| 2. Lecture de l'article | inventaire des échantillons | — |
| 3. Méthode de chaque voie | choix dans la liste ; `vocab.py cherche` en cas de doute | méthode hors liste = `vocab.py ajoute` |
| 4. Chaque étape | action choisie dans la liste ; la définition de l'action porte sa grille (cases attendues) | action hors liste = ajout avec définition et cases |
| 5. Paramètres, réglages, propriétés | nom de la liste en priorité, sinon ajout justifié | idem |
| 6. `load.py check` | refuse un nom absent de la liste et des ajouts ; contrôle la grille de chaque action et de chaque technique ; avertit sur les « non cité » suspects et les quasi-doublons | aucun nom sans définition |
| 7. Chargement (orchestrateur) | contrôle mécanique seulement ; les quasi-doublons sont notés pour la fusion du palier | — |
| 8. Agents suivants du lot | voient les ajouts en attente via `vocab.py cherche` | pas de doublon pendant le lot |

**Deux rythmes** (proposition de l'utilisateur, avec la condition de visibilité immédiate) :
- **visibilité immédiate** : les ajouts en attente sont lus par `vocab.py cherche` dès leur écriture, sans fusion ;
- **fusion tous les 50 publications**, à l'audit de palier : relecture des ajouts, fusion des doublons (l'ancien nom devient synonyme), correction des définitions floues, promotion dans le vocabulaire officiel avec un numéro de version, régénération du fichier de contexte, remplacement automatique des noms fusionnés dans les extractions du lot et rechargement ; les cases de grille apportées par une action nouvelle sont marquées « non cherché » dans les publications antérieures, pour une passe ciblée ultérieure.
- Avantages : vocabulaire officiel stable sur un lot (même version pour tous les agents du lot, lot comparable et reproductible) ; pas de doublon dans le lot ; revue groupée au rythme de l'audit.

**Ce qui empêche l'agent de recréer ses noms** : (1) la liste est donnée d'entrée, avec des définitions ; (2) créer coûte un effort (recherche, définition, justification face aux noms proches), choisir est plus simple ; (3) la grille est attachée à l'action : un nom inventé n'apporte pas de cases et doit en définir ; (4) `load.py` refuse un nom sans définition et `vocab.py` signale les quasi-doublons ; (5) la critique de fidélité vérifie qu'un ajout ne double pas un nom existant, et la fusion du palier rattrape le reste.

**Mesure de réussite au pilote** : nombre de noms ajoutés par publication (cible : un ou deux au plus) et part des ajouts fusionnés à la revue.

## 6. Fichiers liés

`audits/registre_tests.md` (tous les tests et leur verdict), `audits/test_completude.md`, `audits/audit_grilles.md`, `audits/couverture_valeurs.md`, `audits/pilote_complement.md`, `audits/sonde_manques.md`, `audits/audit_verification.md`, `audits/audit_contenu.md`, `canon.py`, `docs/vocabulaire/`, `PROMPT_COMPLEMENT.md`, `PROMPT_TEST_COMPLETUDE.md`.
