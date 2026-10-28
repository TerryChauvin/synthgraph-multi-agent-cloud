# Journal d'extraction v2 : PMC6812203

- Découpage : deux voies de base, sans branche. SBA-15 (voie de base, kind material) et NH2-SBA-15 (kind post_treatment, parent null) : le greffage a ses propres étapes et réactifs, et part de « 1 g of calcined SBA-15 » (réactif de rôle intermediate). Aucune série de synthèse n'est balayée.
- Chargement et libération du chloramphénicol : rangés en mesures `adsorption_test` (ads_time, ads_conc, ads_dose, release_1) et résultats de NH2-SBA-15, pas en voies ni en branches (RUNBOOK : tests du matériau fini). Le solide chargé est dans `sample_inventory` avec `route: null`.
- Mesures dupliquées sur les deux voies (xrd_SBA / xrd_NH2, etc.) : NH2-SBA-15 n'est pas une branche de SBA-15, donc elle ne peut pas hériter des mesures de la voie de base.
- Phrases « mixed with 60 mg of SBA-15 » (essai de concentration) et « SBA-15 was mixed with 20 mg/l » (essai de dose) : attribuées à NH2-SBA-15 d'après le résumé et les légendes des figures 5 à 7 ; doute noté.
- Libération : 41 % (« within 30 minutes », Résultats), « at 1 hour » (résumé), 41,35 % (conclusion) extraits en trois résultats distincts, sans trancher.
- Valeur 124,08 mg/l « loaded » du solide : recopiée comme réglage initial_concentration de la libération ; incohérence de bilan de matière signalée en limite_reproductibilite.
- Fournisseur : phrase unique « that from Sigma Aldrich purchased » appliquée aux réactifs listés (règle 6) ; pureté seulement quand écrite (TEOS 98 %, APTES 99 %). Eau distillée : supplier et pureté déclarés non cités (il serait absurde de la dire achetée chez Sigma).
- Étape de refroidissement du greffage : « then cooled » extrait en `cooling = cooled` après l'avertissement du contrôle ; aucun mode ni température précisés.
- Étape de reflux : température non écrite (celle du toluène serait une déduction) donc déclarée non citée, de même que l'atmosphère et la vitesse d'agitation.
- Bandes FTIR : celles de silanol, Si–O–Si et Si–OH attribuées aux deux voies (« pure and functionalized samples ») ; la bande à 1600 cm−1 (NH2) à NH2-SBA-15 seulement.
- Pertes de masse ATG : 3 % à 643 °C (SBA-15) et 18 % à 642 °C (NH2-SBA-15), température dans le suffixe de la propriété.
- Modèles cinétiques : Weibull (m = 0,0025, ln t0 = 1,3875, R2 = 0,9981) extraits ; Korsmeyer–Peppas et non-Fickian gardés en texte (conditions aux limites non respectées). Équations (1) à (5) absentes du texte.
- Figures : le dossier corpus/fig/PMC6812203 n'existe pas, aucune lecture graphique. Aucune annexe citée.
- Vocabulaire : un ajout, propriété `drug_release` (libération d'un médicament, mesurée par adsorption_test) ; `adsorption_capacity` (charge) et `kinetics_fit` ne convenaient pas. Pas de technique « release_test » ajoutée : le test de libération suit la même grille que l'adsorption (dose, volume, pH, température, durée).
- method_sources : bib28 (Zhao, SBA-15), bib29 (calcination), bib30 (Burke, greffage). Non retenus : Eq. (1) (bib31) et modèles de libération (bib41), qui sont des formules d'analyse.
- Comparaisons : trois valeurs génériques de l'introduction (surface 1000 m2/g, volume poreux 0,5–1,5 cm3/g, pores 2–15 nm) ; le renvoi couvre bib17 à bib19, seul bib17 est noté.
