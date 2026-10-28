# Journal d'extraction v2 — PMC7447784 (BiOCl-GO, photocatalyse du diclofénac)

- **Découpage** : une voie de base BiOCl-GO (synthèse hydrothermale « one pot ») et une branche BiOCl, seule différence « in the absence of GO ». Les tests photocatalytiques (concentration, dose, pH, piégeurs, cycles, sources de lumière) sont des résultats et des mesures `catalytic_test` de la voie de base, pas des branches (règle des tests du matériau fini).
- **BiOCl a ses propres étapes** : la phrase « A similar method » ne dit pas que l'étape de dissolution de GO dans HCl (2 h d'agitation) a eu lieu sans GO. J'ai donc repris les étapes suivantes (agitation 16 h à 25 °C, 140 °C 16 h, lavage, séchage 105 °C 8,0 h) en citant les phrases des Méthodes, et omis la première ; doute posé.
- **GO** : « Hummer’s method » renvoyé à CR23, sans quantités. Pas de voie `intermediate` (aucune étape à écrire sans inventer) : GO est un réactif de rôle `intermediate` de BiOCl-GO, avec `method_sources` CR23 (`protocole_complet`) et une annotation de limite. GO figure dans l'inventaire sans voie.
- **Variation de BiOCl** : paramètre = nom exact du réactif GO du parent, `value_text` « absent ».
- **Fournisseur** : la phrase de la section Chemicals nomme HCl et NaBiO3 (Sigma Aldrich) ; pureté déclarée non citée. Acétone, éthanol et eau de lavage (rôle `wash`) hors grille.
- **Tableau 1 (XPS)** : chaque rangée de l'élément est citée en entier ; la colonne BiOCl ou BiOCl-GO est choisie d'après l'en-tête « Element | BiOCl | BiOCl-GO » et l'ordre BE / Atomic (%). Les atomes de C (28,68 et 38,3 %) sont aussi dans le texte, sans doublon.
- **« respectively » XPS** : « 5.3 eV and 5.31 eV … BiOCl and BiOCl-GO » lu dans l'ordre (BiOCl 5,3 ; BiOCl-GO 5,31).
- **Table 2 (cinétique)** : chaque rangée en citation ; k et R² en `kinetics_fit_*` et `statistic_r2_*`, rattachés à la mesure de la série (concentration, dose, pH). La rangée 1,0 g L−1 est identique à la rangée 25 mg L−1 (même expérience), recopiée dans les deux séries.
- **Valeurs lues sur figure** (2 chiffres significatifs) : Fig. 5 (BiOCl solaire ≈ 27, visible ≈ 19, photolyse solaire ≈ 4), Fig. 9 (pH 7 ≈ 42, pH 9 ≈ 25), Fig. 10b (PBQ ≈ 23, IP ≈ 18), Fig. 10c (cycles 1 à 5). Les autres points des courbes ne sont pas repris.
- **Contradiction texte/figure** : 2 g L−1 = 50,8 % dans le texte, ≈ 60 % sur la Fig. 8 → texte retenu, doute. Autres incohérences gardées telles quelles : résumé 34,4 % vs 34,3 %, k non monotone en concentration, conclusion qui attribue 0,0386 min−1 à la lumière solaire, pH 6 des légendes contre pH 5 optimal.
- **pH par mesure** : chaque mesure `catalytic_test` reprend le pH de sa légende (6 pour Fig. 7 et 8, série 5/7/9 pour Fig. 9) ; le pH de la Fig. 5 reste « non cité ».
- **Photolyse sans catalyseur** : rattachée à BiOCl-GO faute de matériau, avec une mesure `cat_photolysis` (catalyseur « no catalyst »).
- **Piégeurs** : l'identité des piégeurs (PBQ = superoxyde, IP = hydroxyle, TEOA = trous) va dans le réglage `method` de la mesure, sans nom ajouté au vocabulaire ; aucune quantité de piégeur écrite.
- **Littérature** (`comparisons`) : Table 3 en entier (réf. laissée vide pour les quatre rangées sans renvoi), valeurs de l'introduction (3,2 ; 2,9 ; 99 % ; 1,43 ; 2,18 eV), plaques de Sun, adsorption de 14 % (CR27) et 5 % (CR28), 3,33 eV (CR17).
- **Annexes** : seule la figure S1 (titre) est dans le fichier d'annexe ; annotation « Annexe absente du dépôt ».
- **Vocabulaire** : aucun nom ajouté ; `method` utilisé pour les piégeurs, `pretreatment` pour l'équilibre d'adsorption de 30 min et la régénération.
