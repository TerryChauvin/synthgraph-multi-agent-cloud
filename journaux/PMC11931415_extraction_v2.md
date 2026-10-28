# Journal d'extraction v2 — PMC11931415 (CaCl2/MOF-303)

- Découpage : 10 voies. Poudre de MOF-303 (`MOF-303_powder`), granulés (`A0`, étapes propres de granulation), imprégnation `A1` (base) avec branches `A2` à `A4` (seule la concentration de la solution de CaCl2 change : 10/20/30/40 % w), mélange physique `A1′` (base) avec `A2′` à `A4′`. Les intermédiaires sont des voies indépendantes reliées par un réactif de rôle `intermediate`, car les granulés et la poudre sont aussi des échantillons testés (Tableaux 1 à 3).
- A1=10 %, A2=20 %… : déduit de « respectively » et de la teneur croissante du Tableau 1 ; signalé en doute.
- Mélange physique : A1′–A4′ ne figurent que dans le Tableau 2. Rapprochement avec les teneurs A1–A4 du Tableau 1 (3,28 à 8,93 wt%) pris pour les quantités de CaCl2 des branches, en citant la rangée du Tableau 1 ; c'est la lecture la plus littérale de « according to the content of CaCl2 in … composites » mais elle repose sur la notation prime (doute).
- Méthode de la poudre : `solution_reflux` choisie au lieu de `hydrothermal` (flacon de verre à 373 K, pas d'autoclave), malgré l'intitulé de la Figure 1. Aucun « reflux » dans le texte : doute.
- « 43.08 mol » : coquille pour mmol ; seule la masse (7,5 g) est extraite.
- Mélange eau/éthanol de la granulation : un seul volume total (4,5 ml) ; quantités eau et éthanol déclarées non citées, rapport 1 : 1 gardé en paramètre `volume_ratio`.
- FTIR / TGA / EDS : « the composite » non nommé ; TGA et EDS rattachées à A1 (base de la série), FTIR à la poudre. Résultats chiffrés de la Fig. 8 lus sur la figure (≈ 20 % de perte à 150 °C, ≈ 24 % de résidu à 600 °C).
- Cyclage (Fig. 13) : légende « CaCl2/MOF-303 (3) » lue comme A3 ; capacités ≈ 980 puis ≈ 940 mg g−1 lues sur la figure (2 chiffres significatifs).
- Colonne « Pore volume » du Tableau 1 : volume total ou microporeux indéterminé ; `pore_volume_total` par lecture littérale.
- Adsorbants commerciaux (tamis 3A/4A/5A/13X, gel de silice) : sans voie, valeurs gardées dans des annotations `tendance_observee` (la liste `comparisons` est réservée à la littérature).
- Valeurs de la littérature : douze rangées du Tableau 2 avec renvois `cit31`–`cit36` pris dans `corpus/refs` (la colonne Ref. est vide dans `corpus/text`).
- Deux renvois pour le protocole du MOF-303 (cit30 dans les Méthodes, cit25 dans les Résultats) : les deux gardés dans `method_sources`.
- Valeurs de CaCl2 = 0 des A0 non reprises (échantillons non chargés, aucune mesure ICP décrite pour eux).
- Vocabulaire ajouté : technique `vapor_adsorption_test`, réglages `pressure_range` et `carrier_gas_flow`, propriété `breakthrough_time`, action `shape_forming`, méthodes `granulation` et `physical_mixing`. `adsorption_capacity` et `retention_stability` ne listent pas encore `vapor_adsorption_test` : 21 avertissements « technique inhabituelle » attendus.
- Aucune annexe (Supporting Information) dans le fichier texte ni citée par l'article.
