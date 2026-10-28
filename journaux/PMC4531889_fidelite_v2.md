# Journal de la critique de fidélité v2 (format 3), PMC4531889

- Mes échantillons avant ouverture de l'extraction : NRA 25 mM canal 10 μm (référence), 5 mM, 50 mM (canal 10 μm), couche de germination seule, canaux 5, 15, 30 μm, point 20 μm de l'encart Fig. 5a, simulation RCWA. L'inventaire de l'extracteur est identique (10 lignes) : aucun échantillon manquant.
- Point à 20 μm : défini seulement par l'encart de la Fig. 5a et par « Above 20 μm » ; j'ai ouvert la figure, le point existe (≈ 31) ; constat `mineur` sur la citation de la variation, pas sur la valeur.
- Valeurs lues sur figure (9,5 ; 31 ; 27) : écart avec mes lectures inférieur à 1 unité, pas de constat. Fig. 3b : photocourants à 10 V cohérents avec le texte (≈ 1,4 ; 2,0 ; 1,1 × 10−4 A).
- Fig. 5b : pics à 10 V ≈ 3,9 × 10−4 A (cohérent avec 3,93). Les pics à ±5 V et −10 V ne sont pas extraits : `manquant` probable, facultatif car valeurs de figure.
- `drying_mode` déclaré absent alors que le texte dit « dried by flowing DI water » : `non_cite_a_tort` probable (et non `sure`, car l'ambiguïté rinçage/séchage est déjà un doute de l'extracteur).
- HMTA = 25 mM : valeur juste par l'équimolarité mais citation qui ne nomme pas l'HMTA : `deduit` probable, correction = changer la citation.
- Méthode `chemical_bath_deposition` (ajout au vocabulaire) contre « hydrothermal » des auteurs : définition de `hydrothermal` = autoclave > 100 °C, article = étuve à 90 °C sans autoclave ; choix cohérent avec contexte_agents.md, écarté comme non-constat.
- Réglages `not_stated` vérifiés (XRD radiation/plage/pas, MEB tension, active_area, logiciel RCWA) : tous réellement absents du texte. Seul drying_mode est faux (25 cases vérifiées, 1 fausse).
- measured_by : tous les liens sont plausibles (SEM pour tailles, XRD pour phase et pic 002, device_test pour photocourants et on-off, transient_1 pour reset time, calc_1 pour absorptions). Résultats du témoin et des simulations rangés sur les voies correspondantes, pas sur le dispositif mesuré.
- `xrd_peak_position_au_111` : pas de position donnée et pic de l'électrode ; `mineur`.
- Comparisons : ref_id absents alors que corpus/refs donne CR1–CR3 et CR14–CR16 ; `mineur`.
- method_sources vide : correct (seul « according to the standard JCPDS card » n'est pas une méthode ; l'indice 2.1 + i0.5 est une constante d'entrée).
