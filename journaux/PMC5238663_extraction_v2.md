# Journal d'extraction v2 — PMC5238663

- Découpage : cinq voies de base indépendantes, aucune branche. Les Méthodes décrivent cinq préparations séparées (GO, ZnO NR, CdS NP, CdS–ZnO, CdS–ZnO–RGO) et l'article ne balaie aucun paramètre de synthèse. Les deux conditions d'éclairement (simulateur filtré, soleil) et la présence de RGO sont des conditions de test ou des matériaux distincts, rangés en mesures `catalytic_test` (`cat_vis_*`, `cat_sun_*`) et en résultats, pas en branches.
- GO est une voie `intermediate` (réutilisée dans le ternaire). CdS–ZnO est gardée `material` car testée seule ; le ternaire la cite comme réactif de rôle `intermediate`.
- CdS–ZnO : protocole « one-pot » (ZnCl2, acétate de Cd, acide thioglycolique) qui ne réutilise ni ZnO NR ni CdS NP, bien que l'introduction parle de couplage. Lecture littérale des Méthodes, doute écrit. Le rôle de l'acide thioglycolique n'est pas dit : `precursor`.
- Ternaire : « hydrothermal treatment » dans l'article, mais la suspension est dans l'éthanol, donc `solvothermal_treatment` et méthode `solvothermal` selon les définitions du vocabulaire. Pas d'ajout au vocabulaire : tous les noms nécessaires existaient.
- GO étape 12 : « vacuum drying overnight at same temperature » → `value_text: same temperature` (pas de 40 °C déduit), doute écrit.
- Graphite : pics XRD (26,5° et 54,3°) donnés pour le réactif commercial ; rangés sur la voie GO avec des propriétés `…_graphite_precursor_…` pour ne pas les confondre avec ceux de GO.
- Tableau de pics ZnO (« respectively ») : ordre des 9 positions et des 9 plans identique dans la phrase, un résultat par pic.
- Bande interdite de CdS : 2,12 eV dans le texte (DRS), 2,20 eV sur la Fig. 3b. Les deux sont extraites sous deux propriétés distinctes, la seconde avec `from_figure`.
- Fig. 10 contre texte et Fig. 11 : les courbes C/C0 donnent environ 93–94 % dégradés pour le ternaire contre 98 % dans le texte ; texte conservé comme valeur d'article, lectures de la Fig. 10 gardées à part (30, 60, 90 min, ±2 %). Fig. 11 consultée seulement (barres à 98 / 70 et 97,5 / 69), non extraite pour ne pas doubler le texte.
- Fig. 1 : positions de pics ZnO/CdS lisibles sur l'axe décalées de 3–4° par rapport au texte ; aucune valeur lue sur cette figure.
- Mesures : chaque voie porte ses propres entrées (les voies n'ont pas de parent), avec les réglages de la section « Characterizations » répétés. EDS rattaché à la même colonne que le MET, tension d'accélération déclarée non citée car seulement implicite (« same HRTEM instrument »).
- Réglages de catalyse : intensité solaire en deux réglages `light_source` (luxmètre LX-101A puis 9,5 × 10^4 lux, exposant aplati dans le texte). Le temps de réaction vient des phrases de résultats (90 et 60 min). La phase d'obscurité de 30 min est rangée en `pretreatment`.
- Comparaisons : 8 rangées du Tableau 1 (temps de fin de dégradation) et 9 valeurs de littérature citées dans le texte. Les deux rangées « this work » du tableau sont des résultats de la voie ternaire, pas des comparaisons.
- Annexes : l'article n'en cite aucune ; dossier de figures présent et utilisé.
