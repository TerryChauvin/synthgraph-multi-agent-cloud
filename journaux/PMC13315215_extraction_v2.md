# Journal d'extraction v2, PMC13315215

- Une seule voie de base (`Ce(NDC)MOF@Bentonite`), sans branche : l'article ne prépare qu'un matériau. Les balayages de dose (16–100 mg), de concentration de NaBH4 (0,01–0,10 mol/L) et de température (25–45 °C) sont des conditions de test du catalyseur fini, donc des résultats de la voie (une mesure `catalytic_test` par série : `cat_dose`, `cat_conc`, `cat_temp`, `cat_reuse`) et non des branches (règle des tests du matériau fini).
- Bentonite et NDC laissés en `sample_inventory` avec `route: null` (réactifs non synthétisés) ; leurs pics DRX et bandes IR sont gardés comme résultats de la voie du composite, avec le suffixe `raw_bentonite`, `bentonite` ou `NDC` dans le nom de la propriété.
- Méthode `solvothermal` retenue par analogie (DMF/eau, 120 °C) alors que l'article dit seulement « transferred to the oven for one hour at 120 °C » ; action `heat` (pas `solvothermal_treatment`) pour ne pas imposer les cases d'autoclave. Doute écrit.
- « 1 g of bentonite was dissolved in 50 ml distilled water » : action `disperse` (argile insoluble), rôle `substrate` pour la bentonite (support) ; pas de fournisseur (origine géologique seulement), déclaré non cité.
- « All chemicals used are of high grade » : retenu comme pureté du nitrate de cérium et du NDC (réactifs de la phrase précédente) avec cette phrase en `supplier_quote` ; DMF 99,5 % et éthanol 99 % viennent de la phrase « dimethyl formamide (DMF) (99.5% alfa chemicals) … ethanol (99%) ». « alfa chemicals » gardé comme fournisseur du DMF (lecture littérale de « 99.5% alfa chemicals »).
- Durée « one hour » : `value_text` (pas de chiffre dans la citation).
- Tableau 1, dernière rangée « 90100 | 0.251620.2389 » : cellules fusionnées, lues comme 90 → 0,25162 et 100 → 0,2389. Doute écrit.
- Tableau 2 : HGR sans unité écrite dans le tableau ; unité laissée vide (tableau 5 et résumé donnent mL min−1 g−1 pour 116). Trois valeurs pour le meilleur HGR (116,02 / 116,33 / 116) gardées avec leur citation.
- Tableau 4 : toutes les rangées extraites telles quelles (ΔH, ΔS, ΔG par température, K en « sec−1 »), bien que ΔG positif, ΔS ≈ 1 « KJ » et Ea de 217,8 kJ/mol contredisent le texte et la pente de la fig. 11e. Rien corrigé ; doute et annotation `limite_reproductibilite`. ΔE (constante, 217,8) pris une seule fois via `activation_energy` et la citation du texte.
- BET : « 196 ˚C » (Méthodes) contre « 77 K » (Résultats) ; réglage `measurement_temperature` = 77 K avec la citation des Résultats.
- XPS : deux appareils cités ; entrée `xps_1` sur l'Escalab 250Xi (seule avec rayonnement Al-Kα). Attribution des énergies Ce suivant « respectively » du texte.
- Figures lues : fig. 3 (46 cc/g), fig. 4 (pic à ≈ 24 Å), fig. 9c, 10c, 11c (R en mL/min, 2 chiffres significatifs), fig. 12 (valeurs imprimées sur les barres, 47–57 min). Les courbes brutes V(t) et ln Ct ne sont pas transcrites.
- Comparaisons littérature : 8 rangées du tableau 5 (hors la ligne de l'étude, rangée en résultat avec `catalytic_performance_HGR_16mg_30C_0_05M_table5`), `ref_id` issu de `corpus/refs` (CR82, CR83, CR84, CR76).
- `method_sources` vide : les renvois du texte portent sur des assignations de bandes, des équations (BET, Eyring, Arrhenius) ou le contexte, pas sur une préparation ou un protocole.
- Aucune annexe (« Supporting Information ») dans l'article ni dans le fichier texte.
- Ajout au vocabulaire : propriété `thermodynamic_parameter` (ΔH, ΔS, ΔG, ΔE issus d'Arrhenius/Eyring/van't Hoff), absente de la liste et appelée à revenir (adsorption, catalyse) ; mesurée par `catalytic_test`, `adsorption_test`, `electrochemistry`.
- Case `light_source` de `catalytic_test` déclarée non citée (essai non photocatalytique) faute d'autre moyen de satisfaire la grille.
