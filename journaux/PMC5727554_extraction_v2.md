# Journal d'extraction v2 — PMC5727554

- Découpage : un seul enchaînement de synthèse, découpé en 5 voies selon les échantillons caractérisés. Na-titanate_nanosheets (2b, voie de base, kind intermediate : étapes 1 à 3), TiO2NT_HCl (2c, lavage acide, étapes propres 1 à 4), puis TiO2NT-400 (recuit, post_treatment) et ses deux branches 600 et 800 °C. Le recuit est une étape ajoutée : sa variation porte `parent_value: "none"`, d'où 2 avertissements « variation sans paramètre hérité », attendus.
- Précurseur Degussa P25 (2a) : sans voie propre (commercial). Ses résultats mesurés (88/12 %, 24 nm DRX, 25 nm MET, σ 2,83 nm, morphologie irrégulière) sont rangés sur la première voie avec le suffixe `_P25_precursor` ; consigné en doute.
- Fig. 2c : texte et légende disent « annealed nanotubes after acid washing », tableau 2 et méthode indiquent un lavage sans recuit ; lecture retenue : (c) non recuit.
- Pureté et fournisseur : puretés numériques dans le tableau 1, fournisseur dans une autre phrase ; une seule citation `supplier_quote` possible, donc pureté « analytical grade » (phrase générale contiguë à celle du fournisseur). Valeurs du tableau 1 non reprises, signalé en doute.
- Conditions d'EDS (15 eV, 75 mA, 1,3 × 10−3 Pa, 25 mm) rattachées à l'EDS car elles suivent la phrase sur l'EDS ; unités probablement fausses, recopiées telles quelles. TEM : tension non citée.
- Figures lues : σ des histogrammes (2,01 ; 2,73 ; 2,02 ; 18,5 nm) écrits sur les figures 8, 10 et 12, avec `from_figure` ; Fig. 6 (EDS) lue qualitativement. Fig. 13 : la tangente coupe l'axe vers 3,2 eV alors que le texte dit 3,28 eV ; valeur du texte gardée.
- Échantillon 800 °C marqué `succeeded: false` (nanotubes détruits), lecture discutable consignée.
- Vocabulaire : 5 réglages ajoutés (profile_fitting, calculation_constant, beam_current, working_distance, chamber_pressure), après recherche.
- `measured_by: not_stated` pour la taille de 30 nm des nanofeuillets (tableau 2 sans technique).
- Comparaisons : bande interdite de l'anatase massif (3,2 eV, bib0195) et recuit de H2Ti3O7 à 700 °C (bib0125, texte).
