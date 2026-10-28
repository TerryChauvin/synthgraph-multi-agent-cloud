# Journal d'extraction v2 — PMC6994313 (Zn-MOF par micelle inverse assistée par ultrasons)

- Une seule voie de base `Zn-MOF_UARM` : l'article ne décrit qu'un échantillon, préparé dans des « conditions optimales » ; le résumé parle de l'effet des paramètres UARM mais aucune autre condition n'est décrite ni mesurée. Autres échantillons (conditions UARM variées, ampicilline) inscrits dans `sample_inventory` avec `route: null` et la raison.
- Méthode : `sonochemical` (seule méthode de la liste qui rende les ultrasons de puissance en solution). La micelle inverse (SDS/hexane/eau) n'a pas de nom propre dans la liste ; mécanisme discuté en `mecanisme_analyse` (SDS anionique sans co-tensioactif : plutôt une émulsion).
- Étape 5 (`age`, 30 min) : « After 30 min, the Zn-MOF crystals are formed » est lu littéralement comme une durée de 30 min, température non citée ; le point de départ est ambigu (doute noté).
- Aucune étape de séchage, aucun rendement, ni vitesse de centrifugation ni nombre de lavages au DMF : déclarés `not_stated` ou `missing_fields`, après relecture du texte (pas d'annexe, pas de figure disponible).
- Montant « 0,120 mmol » (virgule décimale) : `amount: 0.12`, accepté par le contrôle (forme « 0,12 » dans la citation).
- Pureté et fournisseur des trois solides pris dans la phrase unique de « material characterization » ; l'eau et l'hexane ne sont pas couverts par cette phrase (réactifs nommés seulement) : `not_stated`.
- DRX : « average crystalline size of MnO2 nanoparticle is found as 20 nm » est un reste d'un autre article ; seul 41 nm (Zn-MOF) est extrait. Formule de Scherrer : `crystallite_size_method = Scherer formula` ; K = 0,94 apparaît dans la formule du texte mais pas dans un réglage séparé (pas de nom de réglage adapté, valeur non recopiée).
- Réglages XRD : radiation, plage et pas déclarés `not_stated` (rien dans le texte) ; logiciel et fiche JCPD cités ; `reference_pattern` ajouté au vocabulaire pour cette fiche.
- EDS : le texte écrit « X-ray diffraction spectroscopy » pour la figure 4A ; lu comme EDS d'après la légende ; unité « weight percentage » gardée telle qu'écrite.
- Pore « less than 200 nm » attribué au MET par les auteurs, incohérent avec la BET (3,4 nm) : gardé tel quel avec `measured_by: tem_1` (avertissement de technique inhabituelle accepté). De même `purity` par EDS : « no other impurities » est la formulation des auteurs, la propriété `purity` n'a pas de technique EDS.
- Essais biologiques : trois mesures `biological_test` (halo en gélose, dilution en série, biofilm). Table 1 : une valeur par souche (moyenne), la rangée entière en citation porte les trois répétitions. Table 2 : un résultat par souche avec le bloc entier de la souche en citation (les rangées partielles seraient ambiguës entre souches) ; aucune CMI par souche n'est déduite du tableau. Table 3 : une rangée par concentration de tétracycline, rattachée à la mesure de dilution en série bien que son protocole ne soit pas décrit.
- Contradictions de l'article gardées sans réparation (CMI 0,006 g/100 cc du texte contre croissance à 0,006 en Table 2 ; concentrations Méthodes/Table 2 ; 24 h/48 h ; g/100 cc/μg/mL) : doutes détaillés.
- Exposant aplati : « 1.5 × 108 cfu/ml » recopié tel quel (probablement 10^8).
- Vocabulaire ajouté (3 réglages) : `inoculum`, `tested_material_dose`, `reference_pattern`, chacun après recherche et avec les noms proches écartés.
- Figures : le dossier `corpus/fig/PMC6994313` n'existe pas ; aucune valeur lue sur figure, signalé en `limite_reproductibilite`.
- `method_sources` vide : les renvois aux travaux UARM antérieurs (bib19, bib20) sont des renvois de contexte, non des protocoles cités pour refaire la préparation.
- `comparisons` vide : aucune valeur de la littérature chiffrée dans l'article.
