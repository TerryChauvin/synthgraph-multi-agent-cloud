# Exposants aplatis par `sections.py`

Genere par `audits/exposants_aplatis.py` (lecture seule ; rien dans `synthese.db`, `extractions/`, `critiques/`).

- XML analyses : 615, extractions : 361
- Candidats « chiffre » (10^5 -> 105) : 638 occurrences dans 227 publications (109 extraites)
- Candidats « unite » (signe conservé : 10^-7 -> 10−7, cm^-3 -> cm−3) : 8303 occurrences dans 532 publications (321 extraites)
- Publications extraites dont le JSON contient la chaîne aplatie : chiffre 45, unité 291

Colonne *cité* : la chaîne aplatie (contexte) apparaît telle quelle dans le JSON d'extraction (citation ou valeur potentiellement affectée). Vide = publication non extraite.

## Synthèse et options (rédigée à la main)

- **Cause** : `sections.py` (`flat()`) concatène `e.text` et `tail` sans traiter `<sup>`/`<sub>`. Les exposants sans signe deviennent des chiffres collés (`10<sup>5</sup>` → `105`) ; les exposants signés gardent leur signe (`10−7`, `cm−3`), donc restent lisibles.
- **Ampleur** : 638 occurrences sans signe précédées d'un chiffre dans 227 publications, dont 109 extraites ; 45 extractions contiennent la chaîne aplatie (citation ou valeur à relire en priorité, colonne *cité* = oui). Beaucoup sont des faux positifs (indices, `1 × 10−3` signé classé en « signé », positions, formules) : le tri se fait en ouvrant le XML.
- **Cas confirmés** : PMC9038048 (`105 μg mL−1`, cité), PMC5302706 (`106 times`, `105 times`, cités), PMC10219592 (`1015 cm−3`, cité).
- **Option sûre A (nouveaux articles seulement)** : dans `flat()`, rendre `sup` en `^x` (et `sub` en `_x` seulement hors formules chimiques, sinon `CO_2` partout) uniquement quand `<sup>` est numérique et précédé d'un chiffre ou de `10`. Ne pas régénérer `corpus/text` des 350+ publications extraites : leurs citations sont des sous-chaînes exactes du texte actuel.
- **Option B (rétroactive)** : pour les 45 extractions concernées, corriger à la main (ou par agent) le texte cité ET le texte de `corpus/text/<PMCID>.txt` de la même manière, puis `reload_all.py`. À faire après relecture de la colonne *cité*, hors du périmètre de cette tâche.
- **Non modifié** : `load.py`, `audit.py`, `synthese.db`, `extractions/`, `critiques/`, `sections.py`.

## Exposant précédé d'un chiffre (risque élevé)

| PMCID | contexte aplati | cité |
|---|---|---|
| PMC10037322 | `ficient of >104 cm–1, com` | non |
| PMC10058279 | `sion (1.5 × 108 CFU/mL), ` |  |
| PMC10059734 | ` and an 8 × 105 Am−1 magn` |  |
| PMC10077552 | ` the Co/MA-80031 nanocatal` | non |
| PMC10077552 | `iCu/C@SiO2-80034 catalysts` | non |
| PMC10095197 | `L and 3.3 × 102 CFU/mL, r` |  |
| PMC10095197 | `e was 2.3 × 103 CFU/mL an` |  |
| PMC10095197 | `en of 1.1 × 104 CFU/mL, a` |  |
| PMC10095197 | `ension (1 × 108 CFU/mL) a` |  |
| PMC10095197 | `ension (1 × 109 CFU/mL) w` |  |
| PMC10095197 | `imately 5 × 106 cells/bot` |  |
| PMC10095197 | `inally, 1 × 109 CFU/mL of` |  |
| PMC10095197 | `lution (1 × 108 CFU/mL) w` |  |
| PMC10095197 | `owed 1.35 × 109 CFU/mL fo` |  |
| PMC10095197 | `owed 2.32 × 109 CFU/mL fo` |  |
| PMC10148794 | `onolayer MoSe212 and quant` |  |
| PMC10152066 | ` cells (2 × 106 cells/mL ` |  |
| PMC10152066 | `eafter, 1 × 106 cells/mL ` |  |
| PMC10152066 | `ed with 1 × 105 infectiou` |  |
| PMC10170720 | ` cells (1 × 106 cells/wel` |  |
| PMC10170720 | ` cells (5 × 103 cells/wel` |  |
| PMC10170720 | ` cells (5 × 103 cells/wel` |  |
| PMC10170720 | `ed with 2 × 106 HCT 116 c` |  |
| PMC10170720 | `ging or 1 × 106 cells/wel` |  |
| PMC10189791 | `ty of 2.5 × 105 in 2 mL o` |  |
| PMC10189791 | `ty of 2.5 × 105 in 2 mL o` |  |
| PMC10219592 | `5 to 3.63 × 1015 cm−3. The` | oui |
| PMC10219592 | `from 4.94 × 1015 to 3.63 ×` | oui |
| PMC10290714 | `37, Zr(H2PO4)238, GO-chito` |  |
| PMC10290714 | `Cu/Cu2O@g-C3N419, N-(pheny` |  |
| PMC10293723 | `ately 1.5 × 108 CFU/mL we` | oui |
| PMC10336645 | `efly, 5.0 × 103 cells (U2` |  |
| PMC10336645 | `lture dish (104 cells per` |  |
| PMC10342722 | ` angle of 0.020. The XRD ` | non |
| PMC10386591 | ` of 1.318 × 103 M−1 and 2` | oui |
| PMC10424190 | `ip = 2.69 × 105 × n3/2A ×` | non |
| PMC10473413 | ` diluted to 108 CFU/mL (T` |  |
| PMC10473413 | `oximately 1×108 CFU/mL) w` |  |
| PMC10473413 | `oximately 4×104 cells/mL ` |  |
| PMC10473413 | `ration of 1×106 CFU/mL wa` |  |
| PMC10556056 | `2 and Zn 2p3/265,72. Zn 2p1/2` | non |
| PMC10556056 | `de at 390 cm−167. Raman sp` | non |
| PMC10556056 | `ith Zn/S = 2.537. Table 4 ` | non |
| PMC10556056 | `ressed by 202522. Water po` | non |
| PMC10573519 | `tion of 1 × 107 CFU/mL, c` |  |
| PMC10574157 | `anning from 104 Hz to 0.1` | oui |
| PMC10574157 | `ip = 2.69 × 105 × n3/2 × ` | non |
| PMC10583617 | ` cells (1 × 105 cells mL−` |  |
| PMC10725426 | `proximately 105 (Fig. 5c)` |  |
| PMC10870029 | ` and 3.97 × 1015 Jones for` | oui |
| PMC10870029 | `0000%, 3.97×1015 Jones, an` | non |
| PMC10870029 | `OPD (1.76 × 107 Hz). This` | oui |
| PMC10870029 | `OPD (2.14 × 107 Hz) was l` | oui |
| PMC10870029 | `detectors (≈1014 Jones),[ ` | non |
| PMC10870029 | `s, and 2.14×107 Hz, respe` | non |
| PMC10870029 | `t of 2.14 × 107 Hz. In ad` | oui |
| PMC10870029 | `were 2.30 × 1015 and 3.97 ` | oui |
| PMC10870029 | `y of 3.97 × 1015 Jones, an` | oui |
| PMC10906077 | `w fluence (≪1015 s–1) usin` | oui |
| PMC10956410 | ` cells (1 × 105/well) wer` |  |
| PMC10956410 | `plates, 1 × 104 cells/wel` |  |
| PMC10956410 | `sity of 1 × 105 cells per` |  |
| PMC10975348 | `ty of 1.5 × 104 cells per` |  |
| PMC11001879 | `1, ZnO22, MnO223, and Co3O` | non |
| PMC11001879 | `223, and Co3O424, are the ` | non |
| PMC11007835 | `d to ∼1.5 × 108 CFU/mL, t` |  |
| PMC11018590 | ` density of 104 cells per` |  |
| PMC11036359 | `ing the DFT-D332 exchange–` | non |
| PMC11099149 | ` of SBA-15–NH244One gram o` | non |
| PMC11099149 | `ain SBA-15–NH243. An impor` | non |
| PMC11099149 | `akin to SBA-1535, affirmin` | non |
| PMC11145745 | `adjusted to 105 CFU mL−1 ` |  |
| PMC11145745 | `adjusted to 105 CFU mL−1 ` |  |
| PMC11145745 | `adjusted to 106 CFU mL−1 ` |  |
| PMC11266555 | `, 7.7, and 9.765. In acidi` | non |
| PMC11266555 | `ate exceeds 1010 K/s27.Cer` | non |
| PMC11266555 | `for CO241, CH442, and phos` | non |
| PMC11266555 | `o that of CeO272), highlig` | non |
| PMC11266555 | `orbent for CO241, CH442, a` | non |
| PMC11266555 | `t of pure CeO272). The dec` | non |
| PMC11266555 | `thiols38, H2O231, and asco` | non |
| PMC11266555 | `tions, n = 0.546. The poin` | non |
| PMC11269599 | `um at pH = 9.071,72. The fact` | non |
| PMC11364895 | `sity of 1 × 105 cells/mL ` |  |
| PMC11364895 | `sity of 2 × 105 cells/mL ` |  |
| PMC11364895 | `sity of 5 × 105 cells/mL ` |  |
| PMC11364895 | `sity of 5 × 105 cells/mL ` |  |
| PMC11364895 | `sity of 5 × 105 cells/mL ` |  |
| PMC11364895 | `sity of 5 × 105 cells/mL ` |  |
| PMC11364895 | `sity of 8 × 103 cells/mL ` |  |
| PMC11393933 | ` SiOH.32,40−4211B MAS NMR ` |  |
| PMC11541765 | `cals like H2O242 or any ot` |  |
| PMC11602897 | ` and 1.87 × 1018 cm−3 afte` | oui |
| PMC11602897 | ` and 3.08 × 1018 cm−3, res` | oui |
| PMC11602897 | `018, 3.22 × 1018, and 3.08` | oui |
| PMC11602897 | `8 to 2.05 × 1018 and 1.87 ` | oui |
| PMC11602897 | `from 2.68 × 1018 to 2.05 ×` | oui |
| PMC11602897 | `o be 3.65 × 1018, 3.22 × 1` | oui |
| PMC11678781 | `IS was 10−2–105 Hz with a` | oui |
| PMC11687324 | ` Briefly, 1×103 MDA-MB-23` |  |
| PMC11687324 | ` total of 5×103 MDA-MB-23` |  |
| PMC11687324 | `ordingly, 2×103 MDA-MB-23` |  |
| PMC11687324 | `sessment, 5×105 4T1 cells` |  |
| PMC11736836 | `2,7 ZnO,8 TiO29 or even c` |  |
| PMC11752507 | `c2) = 3.2 × 104 J/m2, L8 ` | non |
| PMC11818718 | `y of 2–2.5 ×104 cells per` |  |
| PMC11840780 | ` Ksv (3.4 × 104 L mol–1) ` | oui |
| PMC11840780 | `hich is 2 × 1010 L mol–1 s` | non |
| PMC11840780 | `nching (2 × 1010 L mol–1 s` | non |
| PMC11840780 | `to be 1.2 × 104 L mol–1 f` | oui |
| PMC11840780 | `ue of 3.1 × 1012 L mol–1 s` | oui |
| PMC11840780 | `ue of 8.6 × 1012 L mol–1 s` | oui |
| PMC11891312 | ` level of 0.0532. A quadra` | non |
| PMC11891312 | `r at 1220 cm−123. These pe` | non |
| PMC11891312 | `ture of MCM-4122. Small-an` | non |
| PMC11935935 | `ion dose of 1012 ions cm−2` |  |
| PMC12043898 | `l solution (107 CFU mL–1)` |  |
| PMC12043898 | `uspensions (108 CFU mL–1)` |  |
| PMC12199321 | ` 108, 1.6 × 107, and 3.0 ` | oui |
| PMC12199321 | ` 108, 1.6 × 107, and 3.0 ` | oui |
| PMC12199321 | `, and 3.0 × 108, respecti` | oui |
| PMC12199321 | `, and 3.0 × 108, respecti` | oui |
| PMC12199321 | `Fs of 4.3 × 108, 1.6 × 10` | oui |
| PMC12199321 | `−1 is 4.3 × 108, 1.6 × 10` | oui |
| PMC12455581 | ` 54.9 and 70.90, correspo` | oui |
| PMC12455581 | `20.8, and 33.30, related ` | oui |
| PMC12494978 | `4. Using Olex235, the stru` |  |
| PMC12494978 | `O₃@[PBVIm]HSO₄30, Na₃[CrMo` |  |
| PMC12494978 | `₆]0.8 H₂O@ZrO₂31, Fe3O4@GA` |  |
| PMC12917697 | `duction and 105 equilibra` |  |
| PMC12917697 | `ge balance. 106 productio` |  |
| PMC12917697 | `ied between 105 K and 100` |  |
| PMC12917697 | `onsisted of 106 productio` |  |
| PMC12917697 | `pt limit of 105 were used` |  |
| PMC12917697 | `pt limit of 105. To ident` |  |
| PMC13057244 | ` battery life45, . From a` |  |
| PMC13057244 | ` permutations12,.Inside L` |  |
| PMC13057244 | `00 GWh in 203020, the need` |  |
| PMC13057244 | `obally by 20406. Recyclin` |  |
| PMC13269777 | ` The PES-ZIF672 support l` |  |
| PMC13269777 | ` The PES-ZIF672-Water sub` |  |
| PMC13269777 | ` The PES-ZIF673-Water mem` |  |
| PMC13269777 | ` and PES-ZIF672-Water (af` |  |
| PMC13269777 | ` and PES-ZIF672-Water sup` |  |
| PMC13269777 | ` and PES-ZIF672-water sup` |  |
| PMC13269777 | ` the PES-ZIF672 and PES-Z` |  |
| PMC13269777 | ` the PES-ZIF672 membrane ` |  |
| PMC13269777 | ` the PES-ZIF672 sample, d` |  |
| PMC13269777 | ` the PES-ZIF672 support l` |  |
| PMC13269777 | ` the PES-ZIF672 support l` |  |
| PMC13269777 | ` the PES-ZIF672 support l` |  |
| PMC13269777 | ` the PES-ZIF672 support l` |  |
| PMC13269777 | ` the PES-ZIF672-Water mem` |  |
| PMC13269777 | ` the PES-ZIF672-Water mem` |  |
| PMC13269777 | ` the PES-ZIF672-Water sam` |  |
| PMC13269777 | ` the PES-ZIF672-Water sam` |  |
| PMC13269777 | ` the PES-ZIF672-Water sam` |  |
| PMC13269777 | ` the PES-ZIF673 membrane ` |  |
| PMC13269777 | ` the PES-ZIF673-Water mem` |  |
| PMC13269777 | ` the PES-ZIF673-Water sam` |  |
| PMC13269777 | ` the PES-ZIF673-Water sup` |  |
| PMC13269777 | ` the PES-ZIF673-Water sup` |  |
| PMC13269777 | `672, PES-ZIF672-water, an` |  |
| PMC13269777 | `PES, PES-ZIF672 (before Z` |  |
| PMC13269777 | `PES, PES-ZIF672, PES-ZIF6` |  |
| PMC13269777 | `PES, PES-ZIF672, and PES-` |  |
| PMC13315215 | `ction of NaBH475,76. These wi` | non |
| PMC13315215 | `ion from NaBH₄8.Hydrogen ` | non |
| PMC13315215 | `lysis of NaBH444,45. The mate` | non |
| PMC13315215 | `lysis of NaBH468. The obta` | non |
| PMC13315215 | `pecies in SiO264. Converse` | non |
| PMC13333848 | `103 atm and 104 K, respec` | non |
| PMC13333848 | `ak at 211 cm−153.Figure 5 ` | non |
| PMC13333848 | `f magnitude 103 atm and 1` | non |
| PMC13424319 | `ation of BCL-26, with cas` |  |
| PMC13424319 | `nsions (1 × 106 cells) we` |  |
| PMC13424319 | `nsions (1 × 106 cells) we` |  |
| PMC13424319 | `of free C4H4N282. In the 1` |  |
| PMC13424319 | `otal of 3 × 106 A549 cell` |  |
| PMC13424319 | `otal of 3 × 106 cells wer` |  |
| PMC13424319 | `tion of 5 × 106 cells/mL.` |  |
| PMC13580062 | ` cells (3 × 106) were sus` |  |
| PMC13580062 | `plates (2 × 105 cells/wel` |  |
| PMC13580062 | `plates (5 × 105 cells/wel` |  |
| PMC2893540 | ` (1.1–1.5 × 109 wires cm−` |  |
| PMC2893540 | ` 1.6, 1.2 × 109 wires cm−` |  |
| PMC2893540 | `2 and 2.0 × 109 wires cm−` |  |
| PMC2893540 | `e 1.4–1.6 × 109 wires cm−` |  |
| PMC3407523 | `t of 8.94 × 107 g/mol [,,` | non |
| PMC3414225 | `hereas only 101 Gl-1 cell` |  |
| PMC3414225 | `owed nearly 104 cells wit` |  |
| PMC3833323 | `MDA-MB-231 (106 cells/mL)` | non |
| PMC3833323 | `sity of 1 × 106 cells per` | non |
| PMC3833323 | `sity of 5 × 104 cells per` | non |
| PMC3913497 | ` cells (ca. 109 CFU (colo` |  |
| PMC3998862 | `and 1.147 × 104 μg · mL−1` | oui |
| PMC3998862 | `sity of 5 × 103 cells per` | non |
| PMC3999824 | `ping of 1.8·1013 cm−2 lead` |  |
| PMC4043712 | `spension (2×104 cells) we` | non |
| PMC4102124 | `, about 5 × 106 4T1 cells` | non |
| PMC4102124 | `ity was 1 × 105 cells per` | non |
| PMC4214824 | ` n-GaN (3 × 1017 cm−3 dopa` | oui |
| PMC4403701 | `al titer of 104. 50% egg ` |  |
| PMC4403701 | `ration of 2×106 cells/mL,` |  |
| PMC4451754 | `once with 2x106 cells of ` |  |
| PMC4451754 | `or cells (2x106 viable tu` |  |
| PMC4456781 | ` and MesoMOF-116 or caviti` | non |
| PMC4456781 | `-96,31 MIL-10032 and MIL-1` | non |
| PMC4456781 | `IF-95, ZIF-10020 and NU-10` | non |
| PMC4456781 | `ch as IRMOF-164 and MesoM` | non |
| PMC4611849 | ` cells (1 × 104 cells/mL)` |  |
| PMC4611849 | ` cells (2 × 105 cells/wel` |  |
| PMC4611849 | `, USA). 1 × 105 cells/wel` |  |
| PMC4611849 | `seeding 3 × 103 HT-29 cel` |  |
| PMC4611849 | `sity of 2 × 105 cells/wel` |  |
| PMC4611849 | `sity of 2 × 105 cells/wel` |  |
| PMC4639843 | ` mixed with 108 cfu mL−1 ` |  |
| PMC4639843 | `tration of ~108 colony fo` |  |
| PMC4725629 | `arland (1.5×109 cfu/mL) w` |  |
| PMC4725629 | `ration of 5×105 colony-fo` |  |
| PMC4973716 | ` mg/mL, and 101 mg/mL) wa` | oui |
| PMC4973716 | `10−1 mg/mL, 100 mg/mL, an` | oui |
| PMC4973716 | `ne serum (5×104 cells/wel` | non |
| PMC4976354 | `nge of 0.01–105 Hz at an ` |  |
| PMC5075710 | ` density of 105 cells/wel` |  |
| PMC5075710 | `2 h against 108 CFU/ml P.` |  |
| PMC5075710 | `2 h against 108 CFU/ml S.` |  |
| PMC5075710 | `cultures (1×108 CFU/ml). ` |  |
| PMC5075710 | `ension of 1×108 CFU/ml of` |  |
| PMC5075710 | `ntration at 108 CFU/ml wa` |  |
| PMC5099674 | `ty of 1.3 × 105 cells/mL ` |  |
| PMC5101912 | ` (J(λ)=2.04X1020 M–1 cm–1 ` | oui |
| PMC5238663 | `ty of 9.5 × 104 lux. Subs` | non |
| PMC5302706 | `d more than 106 times gre` | oui |
| PMC5302706 | `nm for nB = 1016 cm−3.The ` | non |
| PMC5302706 | `nm for nB = 1017 cm−3; λD ` | non |
| PMC5302706 | `nm for nB = 1018 cm−3; λD ` | non |
| PMC5302706 | `rcent (1% ≡ 104 ppm). The` | non |
| PMC5302706 | `s more than 105 times gre` | oui |
| PMC5304159 | `s and 1.2 × 1015 cm−3, res` |  |
| PMC5304631 | `, Germany). 105 PEG molec` | non |
| PMC5304631 | `, and 2.5 × 104 amine-PEG` | oui |
| PMC5304631 | `Au NP 7.5 × 106 EDC molec` | oui |
| PMC5304631 | `antibodies, 103 TAMRA mol` | oui |
| PMC5304631 | `nm) = 5.41× 108·M−1·cm−1 ` | non |
| PMC5309769 | `d 0.21–15 × 1018 cm−3. The` | oui |
| PMC5309769 | `es of 6.5 × 1018 cm−3.Intr` | oui |
| PMC5309769 | `ity of 15 × 1018 cm−3. In ` | oui |
| PMC5309769 | `round 1.5 × 1019 cm-3). Fo` | non |
| PMC5309769 | `round 3.5 × 1018 cm−3). Th` | oui |
| PMC5309769 | `round 5.5 × 1018 cm−3 and ` | oui |
| PMC5309769 | `round 6.0 × 1018 cm−3 and ` | non |
| PMC5369406 | `u is 1.47 × 1019 atoms/m2.` |  |
| PMC5376314 | `g rates of >1010 K/s . Thi` | non |
| PMC5465224 | ` of 10−2 to 105 Hz and it` | oui |
| PMC5466127 | `ension (5 × 106 cells/mL)` |  |
| PMC5466127 | `otal of 1 × 106 cells was` |  |
| PMC5466127 | `sity of 5 × 103 cells/wel` |  |
| PMC5466191 | `about (∼8 × 106 spores/ml` | non |
| PMC5466191 | `nsion (∼8 × 106 spores/ml` | non |
| PMC5551800 | `f apatitic CO32 type B is` |  |
| PMC5551800 | `noculum 3 × 105 cells) mu` |  |
| PMC5551800 | `ty of 5.0 × 103 cells/wel` |  |
| PMC5567205 | ` J = 2.02 × 107 A/m2) res` | oui |
| PMC5567205 | `(J = 2.02 × 107 A/m2). Th` | oui |
| PMC5591228 | ` cells (2 × 105 cells/mL)` |  |
| PMC5591228 | `he range of 103. To ident` |  |
| PMC5591228 | `imately 1 × 106 IU/g). In` |  |
| PMC5680254 | ` from 4.3 × 1016 to 2 × 10` |  |
| PMC5680254 | ` from 4.3 × 1016 to 2 × 10` |  |
| PMC5680254 | `1016 to 2 × 1017 cm−3 whil` |  |
| PMC5680254 | `1016 to 2 × 1017 cm−3 whil` |  |
| PMC5756267 | `ell was 5 × 105 c.f.u. ml` |  |
| PMC5756267 | `ell was 5 × 105 c.f.u. ml` |  |
| PMC5756267 | `oculum (5 × 105 c.f.u. ml` |  |
| PMC5756267 | `oculum (5 × 105 c.f.u. ml` |  |
| PMC5756267 | `on as 2.7 × 107 particles` |  |
| PMC5756267 | `plates (3 × 103 cells per` |  |
| PMC5756267 | `sity of 5 × 105 c.f.u. ml` |  |
| PMC5756267 | `tration 5 × 105 c.f.u. ml` |  |
| PMC5793535 | ` as high as 1021 cm−3 for ` |  |
| PMC5793535 | ` in UZRs to 1021 in 5% GZR` |  |
| PMC5793535 | `ration from 1016 in UZRs t` |  |
| PMC5824763 | ` density of 105 cells/wel` |  |
| PMC5824763 | `sponding to 108 colony-fo` |  |
| PMC5834413 | ` rate about 1010 Ks − 1, w` | non |
| PMC5877699 | ` 105 to 1 × 106 cells/mL.` |  |
| PMC5877699 | `rder of 2 × 105 to 1 × 10` |  |
| PMC5887100 | `sity of 1 × 104 cells per` |  |
| PMC5896389 | `tion of 1 × 105 cells/mL.` | non |
| PMC5896389 | `ty of 5.0 × 105 cells/wel` | non |
| PMC6058695 | ` 0.009 μmol/106 cells und` | oui |
| PMC6058695 | ` 0.009 μmol/106 cells, re` | oui |
| PMC6058695 | ` 0.078 μmol/106 cells aft` | oui |
| PMC6058695 | ` cells (1 × 105 cell/mL) ` | non |
| PMC6058695 | ` cells (2 × 106) were inj` | non |
| PMC6058695 | `0.0059 μmol/106 cells aft` | oui |
| PMC6058695 | `MSNsOf, 8 × 104 cells/mL ` | non |
| PMC6058695 | `SNsOf, 20 × 104 cells/mL ` | non |
| PMC6058695 | `ity of 20 × 105 cells/mL ` | non |
| PMC6058695 | `neration2 × 105 cells/mL ` | non |
| PMC6058695 | `nitoring6 × 104 cells/mL ` | non |
| PMC6058695 | `riefly, 2 × 104 cells/mL ` | non |
| PMC6058695 | `sity of 2 × 104 cells/mL ` | non |
| PMC6083653 | `sity of 2 × 104 cells per` |  |
| PMC6116234 | `f ratio of ~103 with a sm` | oui |
| PMC6116234 | `f ratio of ~103, and a sm` | non |
| PMC6214041 | `ating 5.0 × 106 HeLa cell` |  |
| PMC6214041 | `ells (3.0 × 105 cells/wel` |  |
| PMC6214041 | `sity of 1 × 105 cells per` |  |
| PMC6214041 | `sity of 2 × 105 cells per` |  |
| PMC6214041 | `sity of 2 × 105 per well ` |  |
| PMC6214041 | `sity of 4 × 103 cells per` |  |
| PMC6214041 | `sity of 4 × 103 cells/wel` |  |
| PMC6214041 | `ty of 6.0 × 103 cells/wel` |  |
| PMC6222835 | ` test of L9 (34) was used` | non |
| PMC6273739 | `, about 1 × 106 cells/mL ` |  |
| PMC6273739 | `ated at 1 × 106 cells/wel` |  |
| PMC6273739 | `imately 5 × 104 cells wer` |  |
| PMC6274424 | ` organisms (105 colony-fo` | non |
| PMC6369825 | `dity of 1 × 105 CFU/ml we` | oui |
| PMC6369825 | `tion of 1 × 106 CFU/ml. A` | oui |
| PMC6403542 | ` films (2 × 102–2 × 103 Ω` | non |
| PMC6403542 | `2 × 102–2 × 103 Ω/sq) [,]` | non |
| PMC6403542 | `ce of about 1012 Ω/sq or h` | non |
| PMC6403739 | ` (1.5–30) × 105 cfu/mL. I` |  |
| PMC6409692 | ` as high as 1014–1015 [,,]` |  |
| PMC6409692 | `EF of 2.7 × 107 at 633 nm` |  |
| PMC6409692 | `EF of 2.7 × 107 since the` |  |
| PMC6409692 | `ed as 2.7 × 107. Although` |  |
| PMC6409692 | `high as 2 × 108. Therefor` |  |
| PMC6409692 | `igh as 1014–1015 [,,]. In ` |  |
| PMC6409692 | `rder of 8 × 105. However,` |  |
| PMC6443225 | `ntration of 106 CFU/mL pr` |  |
| PMC6443225 | `ntration of 106 colony-fo` |  |
| PMC6443225 | `ration of 5×104 cells/mL ` |  |
| PMC6474109 | `sity of 1 × 104 cells per` |  |
| PMC6554519 | `ensity of 5×104 cells/wel` |  |
| PMC6554519 | `ensity of 5×104 cells/wel` |  |
| PMC6614408 | `idation of NH338. In contr` | non |
| PMC6628063 | ` with a 1 × 105 molar exc` |  |
| PMC6628063 | ` with a 1 × 105 molar exc` |  |
| PMC6628063 | `103 and 3 × 103 cells/wel` |  |
| PMC6628063 | `12 = 1.42 × 105 M−1 cm−1 ` |  |
| PMC6628063 | `50 = 9.92 × 109 M−1 cm−1 ` |  |
| PMC6628063 | `80 = 2.25 × 105 M−1 cm−1 ` |  |
| PMC6628063 | `eded at 3 × 104 cells/wel` |  |
| PMC6628063 | `eded at 5 × 103 and 3 × 1` |  |
| PMC6628063 | `on of a 1 × 105 molar exc` |  |
| PMC6628063 | `sity of 1 × 105 cells/wel` |  |
| PMC6628063 | `sity of 1 × 105 cells/wel` |  |
| PMC6631201 | `c = (2.69 × 105) n3/2 D1/` | non |
| PMC6678425 | `ion of Zn(OH)42− cannot b` | oui |
| PMC6678425 | `m to form SeO32− ions [].` | oui |
| PMC6688992 | `aqueous Na2SO4119,120, and the ` | non |
| PMC6694146 | `n that of TiO219. In the p` | non |
| PMC6722438 | `S. Cells (2×104) were add` |  |
| PMC6722438 | `ensity of 2×104 cells/wel` |  |
| PMC6722438 | `n (50 μL; 1×107/mL) was a` |  |
| PMC6722438 | `plates at 2×104 cells/wel` |  |
| PMC6928214 | `eact with H2O227, the amou` |  |
| PMC6928996 | `ed with 5 × 104 hMSCs in ` | non |
| PMC6985175 | `index of 1.46214. As the d` |  |
| PMC6994313 | ` 0.5 (1.5 × 108 cfu/ml) i` | non |
| PMC6994313 | ` 0.5 (1.5 × 108 cfu/ml) w` | non |
| PMC6994313 | `sion (1.5 × 108 cfu/ml) w` | non |
| PMC7022538 | ` (α1τ12 + α2τ22)/(α1τ1 + ` | non |
| PMC7022538 | `ely. τ = (α1τ12 + α2τ22)/` | non |
| PMC7024153 | `sity of 5 × 103 cells/wel` |  |
| PMC7033158 | ` a factorial 23, with 8 t` | oui |
| PMC7039937 | `h is 6.42 × 105 S·s·cm−3,` |  |
| PMC7039937 | `rom 10−1 to 106 Hz. The m` |  |
| PMC7039937 | `y of 6.42 × 105 S·s·cm−3,` |  |
| PMC7075133 | ` of 10−1 to 105 Hz and th` |  |
| PMC7075133 | `nge of 10−1–106 Hz with I` |  |
| PMC7075151 | ` (α1τ12 + α2τ22)/(α1τ1 + ` | non |
| PMC7075151 | `) τave = (α1τ12 + α2τ22)/` | non |
| PMC7116022 | `ic of Cs4PbBr67 and the a` |  |
| PMC7182996 | ` Cells (5 × 105 cells/wel` |  |
| PMC7182996 | `0 µl of 5 × 108 CFU/mL ba` |  |
| PMC7182996 | `d and 1.5 × 108 CFU/mL (0` |  |
| PMC7182996 | `l cell (5 × 108 CFU/ml) w` |  |
| PMC7182996 | `ount of 5 × 105 cells hav` |  |
| PMC7184584 | `esized in 200318,19. Chiral o` | non |
| PMC7192947 | ` PEN4 and PEN562,63. Of these` |  |
| PMC7192947 | `NaCl. WSSV (106 copies) w` |  |
| PMC7192947 | `Taiwan in 19926 and subse` |  |
| PMC7192947 | `ocytes (5 × 105 cell per ` |  |
| PMC7192947 | `plates (5 × 105 cell/well` |  |
| PMC7212993 | ` of ca. 5 × 106) and 1 µL` |  |
| PMC7279382 | `rom 10−2 to 105 Hz with a` | oui |
| PMC7352182 | `rom 10−2 to 105 Hz with a` | oui |
| PMC7436023 | ` diluted at 108 bacteria/` |  |
| PMC7447784 | `shown in Eq. 240.2lnCC∘=-k` | non |
| PMC7485164 | `cale (1.3 × 106 CFU/mL), ` |  |
| PMC7503881 | `sity of 1 × 104 cells/mL ` |  |
| PMC7583944 | `sion (1.5 × 105 cells) wa` | oui |
| PMC7583944 | `sion (1.5 × 105 cells) wa` | oui |
| PMC7583944 | `taining 3 × 106 cells. In` | non |
| PMC7596963 | `d standard (108 cfu/ml) o` |  |
| PMC7596963 | `ty of 0.5 × 104 cells per` |  |
| PMC7645746 | ` UiO-66, ZIF-818. While th` | non |
| PMC7645746 | `he CuGA 90–2.232.The FTIR,` | non |
| PMC7645746 | `lly, over 7∙105 tons of s` | non |
| PMC7664687 | ` to achieve 104 cells/wel` | non |
| PMC7712560 | ` BMSCs (1 × 104 cells/cm2` |  |
| PMC7712560 | `s (with 3 × 107 cells/mL ` |  |
| PMC7747735 | ` of 5 °C min−130. The XPS ` | non |
| PMC7747735 | `O2–ZrO2/SBA-1510, MnO2–ZrO` | non |
| PMC7747735 | `ies of γ-Al2O336. In the c` | non |
| PMC7747735 | `kel-based CeO28, and Al2O` | non |
| PMC7747735 | `resence of CO215. Likewise` | non |
| PMC7747735 | `rted TiO2-ZrO25, and V2O5` | non |
| PMC7760056 | `r = 6.023 × 1023 mol−1). T` | non |
| PMC7760056 | `ro (6.023 = 1023). The fol` | non |
| PMC7786535 | `f more than 1010 K s−1 and` | non |
| PMC7824182 | ` density of 103 cells/wel` |  |
| PMC7824182 | `omycin (1 × 104 units per` |  |
| PMC7824182 | `otal of 1 × 106 SkBr3 exp` |  |
| PMC7824182 | `sity of 5 × 104 cells per` |  |
| PMC7847977 | `O (MW = 4 × 105 g, Sigma)` |  |
| PMC7860036 | ` plate (8 × 103 cells/wel` |  |
| PMC7860036 | `6-well, 8 × 103 cells/wel` |  |
| PMC7860036 | `taining 1 × 107 HT29 cell` |  |
| PMC7910993 | `eded at 1 × 104 cells/wel` |  |
| PMC7910993 | `eded at 1 × 105 cells/wel` |  |
| PMC7910993 | `ount of 1 × 104 cells.3. ` |  |
| PMC7912860 | `adjusted to 107 by taking` |  |
| PMC7912860 | `rial cells (107) in LB wa` |  |
| PMC7931434 | ` as low as 2.018,37 and, here` |  |
| PMC7932996 | `ltures (1 × 106 CFU/mL) i` |  |
| PMC7932996 | `tion of 1 × 106 CFU/mL. F` |  |
| PMC7932996 | `tion of 1 × 106 CFU/mL. M` |  |
| PMC8132056 | ` and 3.82 × 1014 (50%‐F‐Ti` | oui |
| PMC8132056 | ` and 5.71 × 1014 cm−3 with` | oui |
| PMC8132056 | ` and 6.67 × 1015 cm−3, res` | non |
| PMC8132056 | `) to 6.69 × 1014 (4%‐F‐TiO` | oui |
| PMC8132056 | `014, 2.20 × 1014, 6.30 × 1` | oui |
| PMC8132056 | `014, 6.30 × 1014, and 5.71` | oui |
| PMC8132056 | `015, 3.59 × 1015, 9.49 × 1` | non |
| PMC8132056 | `015, 9.49 × 1015, and 6.67` | non |
| PMC8132056 | `5 to 9.49 × 1015 cm−3. To ` | oui |
| PMC8132056 | `O2), 4.75 × 1014 (12%‐F‐Ti` | oui |
| PMC8132056 | `from 6.67 × 1015 to 9.49 ×` | oui |
| PMC8132056 | `from 9.72 × 1014 (the pris` | oui |
| PMC8132056 | `o be 4.01 × 1014, 2.20 × 1` | oui |
| PMC8132056 | `o be 5.90 × 1015, 3.59 × 1` | non |
| PMC8132056 | `se width of 104 ps was us` | non |
| PMC8140147 | `nm for CsPbBr322, they lie` |  |
| PMC8149873 | `sion of Li3VO430. This ene` | non |
| PMC8149873 | `y of 2.47 × 103 g m−3. It` | non |
| PMC8159122 | ` + b4X4 + b5X12 + b6X22 +` | non |
| PMC8159122 | `+ b5X12 + b6X22 + b7X32 +` | non |
| PMC8159122 | `+ b6X22 + b7X32 + b8X42 +` | non |
| PMC8159122 | `+ b7X32 + b8X42 + b9X1X2 ` | non |
| PMC8159122 | `/(100) X3 > X32 > X2. As ` | non |
| PMC8159122 | `05X12 + 8.94X22 + 0.00011` | non |
| PMC8159122 | `18X12 − 1232X22 − 0.00558` | non |
| PMC8159122 | `2 + 0.000117X32 − 0.00214` | non |
| PMC8159122 | `22 − 0.00558X32 − 0.5951X` | non |
| PMC8159122 | `32 − 0.00214X42 − 0.01471` | non |
| PMC8159122 | `4 + 0.000005X12 + 8.94X22` | non |
| PMC8159122 | `4 − 0.006818X12 − 1232X22` | non |
| PMC8159122 | `X32 − 0.5951X42 − 1.007X1` | non |
| PMC8159122 | `or PDE X3 > X12 > X2X3 an` | non |
| PMC8159122 | `rial design (34). This de` | non |
| PMC8184743 | ` = 0.047–0.16334.ZnO nanop` | non |
| PMC8184743 | `CdO1, CdO–SiO22 and CdO–Z` | non |
| PMC8184743 | `iO6, and Bi2O37 have been` | non |
| PMC8245356 | `104 and 2 × 104 cells/ml ` |  |
| PMC8245356 | `ties of 3 × 104 and 2 × 1` |  |
| PMC8255795 | ` dilutions (100–105) and ` | non |
| PMC8255795 | ` showed 1 × 106 CFU/mL, w` | oui |
| PMC8255795 | `d wounds, a 104 log of re` | non |
| PMC8255795 | `eduction of 104 log CFU/m` | oui |
| PMC8255795 | `he order of 102 CFU/mL, r` | oui |
| PMC8255795 | `nitude (1 × 107 CFU/mL). ` | non |
| PMC8255795 | `nitude (1 × 108 CFU/mL) f` | non |
| PMC8255795 | `rm biofilm (108 cells/mL)` | non |
| PMC8255795 | `uivalent to 108 cells/mL.` | non |
| PMC8255795 | `utions (100–105) and plat` | non |
| PMC8257353 | ` with a 105-106 CFU/mL co` |  |
| PMC8257353 | `p-G2 cells (104) were loc` |  |
| PMC8257353 | `tock with a 105-106 CFU/m` |  |
| PMC8292365 | `ence of g-C3N427,28, (3) form` | non |
| PMC8292365 | `esence of MoS229,30. However,` | non |
| PMC8292365 | `f MoS2 to MoO326. This is ` | non |
| PMC8292365 | `nal of Mo3p3/245. It is ob` | non |
| PMC8292365 | `oS2 and g-C3N425,62. Accordin` | non |
| PMC8292365 | `of pure g-C3N426. The redu` | non |
| PMC8292365 | `ported in 20095, carbon n` | non |
| PMC8292365 | `ristic of MoS250. The XPS ` | non |
| PMC8292365 | `ture of g-C3N434,44. The peak` | non |
| PMC8325005 | ` cells (1 × 104/ well) we` |  |
| PMC8325005 | ` cells (1 × 106/ well) we` |  |
| PMC8325005 | ` cells (1 × 106/ well) we` |  |
| PMC8325005 | ` cells (1 × 106/well) wer` |  |
| PMC8325005 | ` obtain 1 × 106 CFU (colo` |  |
| PMC8325005 | `ding to 1 × 109 CFU/ml an` |  |
| PMC8325005 | `ty of 3–5 × 104 cells per` |  |
| PMC8347431 | ` plate (1 × 104 cells/mL)` |  |
| PMC8347431 | ` plate (1 × 104 cells/mL)` |  |
| PMC8347431 | `imately 2 × 106 SW480 cel` |  |
| PMC8401075 | ` lines (1 × 104 cells/wel` |  |
| PMC8401075 | `otal of 1 × 104 cells wer` |  |
| PMC8401075 | `sity of 2 × 104 cells wer` |  |
| PMC8434467 | `tion of 1 × 104 was obtai` |  |
| PMC8465261 | `ging, 1.5 × 105 MCF-7 cel` |  |
| PMC8495851 | `represent SiO219 and a new` | non |
| PMC8621457 | `cteria (5 × 105 CFU/mL) w` |  |
| PMC8621457 | `imately 105–106 colony fo` |  |
| PMC8621457 | `ined to 1 × 107 colony fo` |  |
| PMC8621457 | `ium was 1 × 105 CFU/mL. A` |  |
| PMC8621457 | `luency (5 × 108 cells/wel` |  |
| PMC8621457 | `osa) at 1 × 107 CFU/mL wi` |  |
| PMC8621457 | `proximately 105–106 colon` |  |
| PMC8693586 | `sity of 1 × 104 cells per` |  |
| PMC8703864 | `e of 1.72 × 106 Pa and po` | oui |
| PMC8830207 | `nduced by TiO275 together ` |  |
| PMC8838941 | `ance of 8 × 104 LUX. Such` | oui |
| PMC8866530 | `g V2O344, MoO345, LiMn2O44` | non |
| PMC8866530 | `including V2O344, MoO345, ` | non |
| PMC8866530 | `oO345, LiMn2O446, and Fe2O` | non |
| PMC8930993 | `des of NiCo2S443,44.X-ray pho` | non |
| PMC8930993 | `ons of NiCo2S440. The peak` | non |
| PMC8982036 | ` (A1τ12 + A2τ22)/(A1τ1 + ` | non |
| PMC8982036 | `g, 〈τ〉 = (A1τ12 + A2τ22)/` | non |
| PMC8986218 | `BS to 4.0 × 106 cells/mL,` |  |
| PMC8986218 | `ed to 1.0 × 105 cells/mL ` |  |
| PMC8986218 | `on of 1.0 × 104 cells/wel` |  |
| PMC8986218 | `on of 1.0 × 104 cells/wel` |  |
| PMC9025656 | `of 1 to 2 × 105 CFU/mL fo` |  |
| PMC9025656 | `sity of 1 × 104 cells/wel` |  |
| PMC9034142 | `EF was ∼2 × 1010. The rela` | oui |
| PMC9034142 | `F to ∼7.4 × 105 when the ` | non |
| PMC9034142 | `ate (∼6.4 × 105). The lar` | non |
| PMC9034142 | `h up to 2 × 1010 toward th` | non |
| PMC9034142 | `ith EF over 1010. We can a` | non |
| PMC9034142 | `o be ∼6.8 × 105, which is` | non |
| PMC9034142 | `or of 8.5 × 105 was highe` | oui |
| PMC9034142 | `s more than 1010 for rhoda` | non |
| PMC9036545 | ` (EIS) from 105 Hz to 10−` | non |
| PMC9036545 | `als (3.37 × 104 mol m3). ` | non |
| PMC9038048 | `af extract (105 μg mL−1 i` | oui |
| PMC9038048 | `ely 4 mL of 105 μg mL−1 s` | oui |
| PMC9046778 | `ty of 2.3 × 106 mW m2) ov` | oui |
| PMC9048980 | ` S. aureus (105 CFU mL−1)` |  |
| PMC9048980 | `nd E. coli (105 CFU mL−1)` |  |
| PMC9054805 | `k at 2346 cm−128. The peak` | non |
| PMC9054805 | `n onto GO/SiO261. The func` | non |
| PMC9054805 | `rption on FGS256.Adsorptio` | non |
| PMC9060541 | `the rate of 109 K s−1.20 ` | non |
| PMC9063653 | ` retention (104 s) were o` | non |
| PMC9063653 | `table up to 104 s. The st` | oui |
| PMC9064236 | `cient (>4 × 104 cm−1, at ` |  |
| PMC9064236 | `on (3–5.7 × 1015 cm−3) in ` |  |
| PMC9078281 | `adjusted to 105 cells per` |  |
| PMC9078598 | `7 to 9.06 × 1016 cm−3 as t` | oui |
| PMC9078598 | `7 to 9.06 × 1016 cm−3 with` | oui |
| PMC9078598 | `from 1.32 × 1017 to 9.06 ×` | non |
| PMC9078598 | `from 5.47 × 1017 to 9.06 ×` | oui |
| PMC9078598 | `n of 9.06 × 1016 cm−3 also` | oui |
| PMC9078598 | `n of 9.46 × 1013 cm−3, a m` | oui |
| PMC9078598 | `y of 8.99 × 102 Ω cm, whi` | oui |
| PMC9083121 | `e order of ∼104 in 2 wt% ` | non |
| PMC9083121 | `he order of 104 between u` | oui |
| PMC9088863 | `ion (in the 1020 cm−3 rang` |  |
| PMC9088863 | `s about 1 × 1019 cm−3 if ` |  |
| PMC9089436 | ` cells (1 × 104) were inc` |  |
| PMC9089436 | `ups and 5 × 104 HepG2 cel` |  |
| PMC9091964 | `ntration of 106 colony fo` |  |
| PMC9143007 | `A = 6.022 × 1023, CLi+ is ` | non |
| PMC9165520 | `.4O4(2.24 × 1025 cm–3), in` | oui |
| PMC9165520 | `4O4 (2.80 × 1026 cm–3) is ` | oui |
| PMC9182795 | ` set to 5 × 105 CFU/mL). ` |  |
| PMC9182795 | `ension (5 × 103 cells) we` |  |
| PMC9182795 | `sity of 3 × 105/well onto` |  |
| PMC9182795 | `sted to 5 × 105 CFU/mL), ` |  |
| PMC9182795 | `suspension (107 spores/ m` |  |
| PMC9215008 | ` cells, 2 × 104 per well ` |  |
| PMC9215008 | `lls was 6 × 102 µM. The c` |  |
| PMC9215008 | `planted 2 × 104 cells per` |  |
| PMC9227472 | ` A total of 106 CFU/mL (0` |  |
| PMC9227472 | `e swab, and 106 CFU/mL fu` |  |
| PMC9300655 | `r 480–580 cm−145. In the F` | non |
| PMC9307632 | `ation of AgNO325. Furtherm` | non |
| PMC9307632 | `f Ag(I) to Ag059. In its c` | non |
| PMC9307632 | `with 5.64 × 1018 cm−3, and` | oui |
| PMC9323265 | `DQM), 1.0 × 1010 M−1·s−1. ` | non |
| PMC9323265 | `d as 7.72 × 1011 M−1·s−1. ` | oui |
| PMC9323265 | `o be 4.14 × 1012 M−1·s−1. ` | oui |
| PMC9366981 | `f MPS with a 32 factorial` | non |
| PMC9366981 | `rial design (32) using th` | non |
| PMC9374656 | `of 372 mAh g–13.As new an` | non |
| PMC9418562 | `2 of 1.85 × 1012 cm−2 was ` |  |
| PMC9419006 | ` K = 2.34 × 1010 at pH 4.0` | non |
| PMC9464223 | ` Pluronic F1276. In addit` | non |
| PMC9475401 | `ranges from 105 to 10−1 H` | oui |
| PMC9542428 | ` cells (1 × 105 cells per` |  |
| PMC9542428 | ` cells (1 × 105 cells per` |  |
| PMC9542428 | ` cells (1 × 105 cells per` |  |
| PMC9542428 | ` cells (1 × 105) were see` |  |
| PMC9542428 | ` cells (1 × 107) was subc` |  |
| PMC9565927 | `ension (2 × 1010 cells/mL)` |  |
| PMC9565927 | `sity of 1 × 104 cells/wel` |  |
| PMC9565927 | `sity of 1 × 106 cells per` |  |
| PMC9565927 | `sity of 1 × 106 cells per` |  |
| PMC9565927 | `sity of 2 × 104 cells/wel` |  |
| PMC9565927 | `tion of 1 × 104 cells/wel` |  |
| PMC9565927 | `tion of 5 × 103 cells/mL ` |  |
| PMC9605960 | `lue in Table 560. The valu` | non |
| PMC9609168 | ` (2.5–3.6 × 106 CFU/mL) w` | oui |
| PMC9609168 | `sity of 5 × 104 cells/wel` | oui |
| PMC9631917 | `nt (6.022 × 1023 mol–1).CO` | non |
| PMC9667963 | ` studies.45–4829Si MAS NMR` | non |
| PMC9685500 | `be 1.0133 × 105 M−1, and ` | oui |
| PMC9695608 | `f H0f ≤ 5 × 109 A m−1 s−1` |  |
| PMC9696917 | `uspension (~108 CFU/mL) o` |  |
| PMC9774398 | `a factor of 100–105. The ` |  |
| PMC9774398 | `ctor of 100–105. The CFU/` |  |
| PMC9774398 | `of E. coli (105 colony fo` |  |
| PMC9824576 | ` CFU/mL and 104 CFU/mL. I` |  |
| PMC9824576 | `1 mg/mL) of 103 CFU/mL an` |  |
| PMC9824576 | `ntration is 103 CFU/mL (F` |  |
| PMC9824576 | `ntration is 104 CFU/mL, t` |  |
| PMC9844074 | ` lux to 9 × 104 lux. SMAR` | oui |
| PMC9844074 | `ng from 8 × 104 lux to 9 ` | oui |
| PMC9862409 | `sity of 2 × 105/well on a` |  |
| PMC9862409 | `uivalent to 106 CFU/mL []` |  |
| PMC9865864 | `ductivity (~107 S m−1) an` | non |
| PMC9878544 | `Then, 1.0 × 104 of Hela a` |  |
| PMC9878544 | `s and 1.5 × 104 cells/wel` |  |
| PMC9908928 | `ification × 4034.Ethical d` | non |
| PMC9908928 | `sion 3.10.0.2839. The resu` | non |
| PMC9908928 | `{document}0.9424.Field emi` | non |
| PMC9972853 | ` data of ZIF-824,32 and pure ` |  |
| PMC9972853 | `4) and His (106.60) show tha` |  |
| PMC9972853 | `limidazole (102.44) and His ` |  |

## Exposant signé conservé (10−7, cm−3 : risque faible, lisible)

| PMCID | contexte aplati | cité |
|---|---|---|
| PMC10021013 | ` mmol gcat–1 h–1 (Figure 3` |  |
| PMC10021013 | ` mmol gcat–1 h–1 (Figure 3` |  |
| PMC10021013 | ` mmol gcat–1 h–1) with a H` |  |
| PMC10021013 | ` mmol gcat–1 h–1), which w` |  |
| PMC10021013 | ` mmol gcat–1 h–1).34 We al` |  |
| PMC10021013 | ` mmol gcat–1 h–1, outperfo` |  |
| PMC10021013 | ` mmol gcat−1 h−1 at 50 °C,` |  |
| PMC10021013 | `(mmol gcat–1 h–1) (Figure ` |  |
| PMC10021013 | `09.4 mmol gcat–1 h–1 (Figu` |  |
| PMC10021013 | `09.4 mmol gcat–1 h–1) with` |  |
| PMC10021013 | `09.4 mmol gcat–1 h–1, outp` |  |
| PMC10021013 | `19.9 mmol gcat–1 h–1).34 W` |  |
| PMC10021013 | `20 and 1741 cm–1 were obse` |  |
| PMC10021013 | `20.2 mmol gcat–1 h–1 (Figu` |  |
| PMC10021013 | `4.0 and ∼8.0 Å–1 correspon` |  |
| PMC10021013 | `59.3 mmol gcat–1 h–1), whi` |  |
| PMC10021013 | `7, and 1624 cm–1, which co` |  |
| PMC10021013 | `9, and 518.8 h–1, respecti` |  |
| PMC10021013 | `>200 mmol gcat−1 h−1 at 50` |  |
| PMC10021013 | `our (mmol gcat–1 h–1) (Fig` |  |
| PMC10021013 | `tered at 7.0 Å–1. Consider` |  |
| PMC10021013 | `ximum at 4.0 Å–1, which co` |  |
| PMC10037322 | `ent of >104 cm–1, comparab` | non |
| PMC10058279 | ` of 200 nm min−1, in the d` |  |
| PMC10058279 | ` of 200 nm min−1, in the d` |  |
| PMC10058279 | ` under 3000 cm−1 are assig` |  |
| PMC10058279 | `), and 1568 cm−1 to the sy` |  |
| PMC10058279 | `00 and 4000 cm−1.The UV-Vi` |  |
| PMC10058279 | `400 to 1600 cm−1 interval ` |  |
| PMC10058279 | `400 to 3500 cm−1 with weak` |  |
| PMC10058279 | `457 and 410 cm−1 []. The p` |  |
| PMC10058279 | `614 and 685 cm−1 attribute` |  |
| PMC10058279 | `air (50 mL∙min−1). An empt` |  |
| PMC10058279 | `d from 1033 cm−1 can be at` |  |
| PMC10058279 | `d from 1340 cm−1 can be at` |  |
| PMC10058279 | `d under 500 cm−1, with pea` |  |
| PMC10058279 | `group, 1435 cm−1 to the as` |  |
| PMC10058279 | `lution of 4 cm−1, in the i` |  |
| PMC10058279 | `nd from 900 cm−1 is due to` |  |
| PMC10058279 | `th a 10 °C∙min−1 rate, und` |  |
| PMC10058279 | `the 100–200 cm−1 interval.` |  |
| PMC10059734 | ` above1200 L s−1 mmol−1 ar` |  |
| PMC10059734 | ` an 8 × 105 Am−1 magnetic ` |  |
| PMC10059734 | ` of 0.6 mmol L−1 (160 μg/m` |  |
| PMC10059734 | `) and 1 mmol L−1 (240 μg m` |  |
| PMC10059734 | `0.078 Am2kg−1K−1. We note ` |  |
| PMC10059734 | `200 L s−1 mmol−1 are much ` |  |
| PMC10059734 | `400 to 4000 cm−1 (12 to 12` |  |
| PMC10059734 | `482 L s−1 mmol−1 reported)` |  |
| PMC10059734 | `50 and 1400 cm−1 are attri` |  |
| PMC10059734 | `L−1 (240 μg mL−1) was dete` |  |
| PMC10059734 | `ake 1.0 mmol L−1 and 0.6 m` |  |
| PMC10059734 | `and 0.6 mmol L−1 suspensio` |  |
| PMC10059734 | `and 1.0 mmol L−1 of mixed ` |  |
| PMC10059734 | `as 0.078 Am2kg−1K−1. We no` |  |
| PMC10059734 | `cles, (482 L s−1 mmol−1 re` |  |
| PMC10059734 | `e a 2.0 mmol L−1 (by formu` |  |
| PMC10059734 | `eak at 1007 cm−1 is chemic` |  |
| PMC10059734 | `er limit of 10−12 m2s−1 in ` |  |
| PMC10059734 | `fted to 795 cm−1, likely d` |  |
| PMC10059734 | `ing at 2850 cm−1. It is ca` |  |
| PMC10059734 | `ith 0.6 mmol L−1 and 1.0 m` |  |
| PMC10059734 | `k circa 400 cm−1, but this` |  |
| PMC10059734 | `mg (0.4 mmol L−1) of Mn(ac` |  |
| PMC10059734 | `mg (0.4 mmol L−1) of Zn(ac` |  |
| PMC10059734 | `mg (1.2 mmol L−1) of Fe(ac` |  |
| PMC10059734 | `nce at 2961 cm−1 is due to` |  |
| PMC10059734 | `peak at 540 cm−1 (see Figu` |  |
| PMC10059734 | `peak at 786 cm−1 is shifte` |  |
| PMC10059734 | `t of 10−12 m2s−1 in the MR` |  |
| PMC10059734 | `ted to 1015 cm−1 and the S` |  |
| PMC10059734 | `the 1.0 mmol L−1 sample (s` |  |
| PMC10077337 | `568–56.8 μg mL−1). The hig` | non |
| PMC10077337 | `and at 3332 cm−1 is corres` | oui |
| PMC10077337 | `ands at 674 cm−1 and 561 c` | non |
| PMC10077337 | `bout 1.6 μg mL−1, which li` | non |
| PMC10077337 | `e (4000–400 cm−1) and KBr ` | non |
| PMC10077337 | `lution of 4 cm−1 in the mi` | non |
| PMC10077337 | `m−1 and 561 cm−1 correspon` | non |
| PMC10077337 | `nds at 1641 cm−1 and 1033 ` | non |
| PMC10077337 | `−1 and 1033 cm−1 are corre` | non |
| PMC10095197 | ` around 714 cm−1 and 1390 ` |  |
| PMC10095197 | `aks at 1050 cm−1 and 1570 ` |  |
| PMC10095197 | `aks at 1342 cm−1 (D-band) ` |  |
| PMC10095197 | `d) and 1589 cm−1 (G-band),` |  |
| PMC10095197 | `eak at 3320 cm−1 is due to` |  |
| PMC10095197 | `−1 and 1390 cm−1 are due t` |  |
| PMC10095197 | `−1 and 1570 cm−1 are due t` |  |
| PMC10099130 | ` (∼10–11 cm2 S–1) and low ` | non |
| PMC10099130 | ` below 1000 cm–1 are assig` | non |
| PMC10099130 | ` of 11.4 mA cm–2 and a tem` | oui |
| PMC10099130 | ` to 85.5 mAh g–1. This nor` | non |
| PMC10099130 | `.1 to 2.0 mV s–1. The pote` | non |
| PMC10099130 | `.2C (0.034 A g–1) rate. Tw` | non |
| PMC10099130 | `1 and 99 mAh g–1 coupled w` | oui |
| PMC10099130 | `69 and 3269 cm–1 were obse` | oui |
| PMC10099130 | `8 × 10–4 cm2 S–1) at room ` | non |
| PMC10099130 | `and 1.240 g·cm−3 for LFP-I` | oui |
| PMC10099130 | `and 47.7 mAh g–1 were obta` | oui |
| PMC10099130 | `and 47.7 mAh·g–1 at discha` | non |
| PMC10099130 | `band at 807 cm–1 is ascrib` | non |
| PMC10099130 | `cs (0–1.8 × 10–4 cm2 S–1) ` | non |
| PMC10099130 | `d near 1043 cm–1 is assign` | non |
| PMC10099130 | `d to 144 mAh g–1 for LFP/C` | oui |
| PMC10099130 | `ductivity (∼10–11 cm2 S–1) ` | non |
| PMC10099130 | `ectrode (cm2 g–1), and C i` | non |
| PMC10099130 | `ely 1.211 g·cm−3 for LFP-I` | oui |
| PMC10099130 | `ficient (cm2 s–1).Based on` | non |
| PMC10099130 | `ity (153 mAh g–1 at 1C) an` | non |
| PMC10099130 | `of 1–1.2 mg cm–2), acetyle` | oui |
| PMC10099130 | `rystal (mol cm–3), which i` | non |
| PMC10099130 | `s near 1630 cm–1, indicati` | non |
| PMC10099130 | `te of 0.1 mV s–1 over a po` | non |
| PMC10099130 | `y of 152 mAh g–1 at 0.1C.3` | non |
| PMC10099130 | `y of 155 mAh g–1 at 0.1C.2` | non |
| PMC10099130 | `y of 162 mAh g–1 compared ` | oui |
| PMC10131834 | `32 and 3184 cm−1.[ ] Mean` | non |
| PMC10131834 | `and at 1262 cm−1 and a G b` | oui |
| PMC10131834 | `and at 1423 cm−1 from the ` | oui |
| PMC10131834 | `and at 1549 cm−1, demonstr` | non |
| PMC10131834 | `and at 1607 cm−1 that corr` | non |
| PMC10131834 | `and at 1641 cm−1 and –NH b` | oui |
| PMC10131834 | `and at 1724 cm−1 from C=O ` | oui |
| PMC10131834 | `and at 3440 cm−1, implying` | non |
| PMC10131834 | `ars at 2922 cm−1, which im` | non |
| PMC10131834 | `e of 10 °C min−1 in a nitr` | oui |
| PMC10131834 | `ion (0.25 g mL−1, 120 µL) ` | oui |
| PMC10131834 | `ion (0.25 g mL−1, 120 µL) ` | oui |
| PMC10131834 | `is 0.625 mg mL−1, the CIE ` | oui |
| PMC10131834 | `is 50 110 cd m−2 (Figure S` | non |
| PMC10131834 | `ons at 1282 cm−1 relativel` | non |
| PMC10169762 | `5, and 2518 cm−1 were rela` | oui |
| PMC10169762 | `a was 2.5 m2 g−1. The BJH ` | non |
| PMC10169762 | `nd 0.061 mol.g−1 respectiv` | oui |
| PMC10169762 | `re 0.065 mol.g−1 and 0.061` | oui |
| PMC10169762 | `umber (1652 cm−1) which re` | non |
| PMC10170720 | ` and 150 μg mL−1) were res` |  |
| PMC10170720 | ` laser (1 W cm−2) for 6 mi` |  |
| PMC10170720 | ` laser (1 W cm−2) for 6 mi` |  |
| PMC10170720 | ` laser (1 W cm−2). The det` |  |
| PMC10170720 | `, C-N (1342 cm−1), C=C (15` |  |
| PMC10170720 | `, C=C (1514 cm−1), C=O/C=N` |  |
| PMC10170720 | `0 to 100 μg mL−1 were adde` |  |
| PMC10170720 | `H/N–H (3321 cm−1) were fou` |  |
| PMC10170720 | `NDs (100 μg mL−1) + 1064 n` |  |
| PMC10170720 | `NDs (100 μg mL−1) and (4) ` |  |
| PMC10170720 | `O/C=N (1661 cm−1), O–H/N–H` |  |
| PMC10170720 | `aser (1.0 W cm−2) for 6 mi` |  |
| PMC10170720 | `ensity (3 W cm−2) is not s` |  |
| PMC10170720 | `ion (150 µg mL−1) could ra` |  |
| PMC10170720 | `ion (150 μg mL−1) was cove` |  |
| PMC10170720 | `ity was 1 W cm−2 for 15 mi` |  |
| PMC10170720 | `ning 100 μg mL−1 AuNDs for` |  |
| PMC10170720 | `ning 100 μg mL−1 AuNDs, an` |  |
| PMC10170720 | `s C-O (1230 cm−1), C-N (13` |  |
| PMC10170720 | `sure is 1 W cm−2 at 1064 n` |  |
| PMC10170720 | `tion (1.0 W cm−2) for 5 mi` |  |
| PMC10170720 | `tion (1.0 W cm−2, 6 min), ` |  |
| PMC10170720 | `tion (1.0 W cm−2, 6 min), ` |  |
| PMC10170720 | `tion (1.0 W cm−2, 6 min). ` |  |
| PMC10170720 | `were 100 μg mL−1 for 1064 ` |  |
| PMC10200858 | `062 and 557 cm−1. Due to t` |  |
| PMC10200858 | `and at 1541 cm−1, correspo` |  |
| PMC10200858 | `e and qt (g mg−1) are the ` |  |
| PMC10200858 | `e k (g g−1 min−1) is the r` |  |
| PMC10200858 | `eak at 1632 cm−1 is caused` |  |
| PMC10200858 | `eaks at 798 cm−1 due to th` |  |
| PMC10200858 | `qewhere k (g g−1 min−1) is` |  |
| PMC10219592 | `3.63 × 1015 cm−3. Therefor` | non |
| PMC10219592 | `al is 2.770 mm−1 at this w` | non |
| PMC10219592 | `at q = 1.004 Å−1 with incr` | non |
| PMC10219592 | `be 20.30 mA cm−2, well mat` | non |
| PMC10219592 | `ion (100 mW cm−2, AM1.5G, ` | oui |
| PMC10219592 | `n of 100 mW cm−2 at 25°C, ` | non |
| PMC10219592 | `nd q = 0.708 Å−1 and 0.922` | non |
| PMC10219592 | `of 20.91 mA cm−2, a VOC of` | oui |
| PMC10219592 | `−1 and 0.922 Å−1 were obse` | non |
| PMC10224134 | ` GA at 1545 cm−1 indicate ` |  |
| PMC10224134 | ` peak (1085 cm−1), and the` |  |
| PMC10224134 | `and at 1445 cm−1 and the C` |  |
| PMC10224134 | `n peak (800 cm−1), the Si-` |  |
| PMC10224134 | `n peak (960 cm−1). The inf` |  |
| PMC10224134 | `ted at 2922 cm−1 and 2855 ` |  |
| PMC10224134 | `−1 and 2855 cm−1, which ar` |  |
| PMC10249076 | ` 400 to 800 cm–1. The FTIR` |  |
| PMC10249076 | ` and 655.80 cm–1 represent` |  |
| PMC10249076 | ` of 400–800 cm–1. A higher` |  |
| PMC10249076 | ` of 500–700 cm–1. The abso` |  |
| PMC10249076 | `and a 35.2 kAm–1 field str` |  |
| PMC10249076 | `d under 300 cm–1, which ar` |  |
| PMC10249076 | `e at 268.47 cm–1 is attrib` |  |
| PMC10249076 | `ode at ∼730 cm–1 represent` |  |
| PMC10249076 | `of 400–4000 cm–1. Figure 2` |  |
| PMC10249076 | `s above 300 cm–1 correspon` |  |
| PMC10262014 | `400 to 4000 cm−1. Small am` | non |
| PMC10262014 | `C = 0.055 μS m−1; BOECO pu` | oui |
| PMC10262684 | ` 0.05 el Å–2 s–1) to minim` |  |
| PMC10262684 | `ound 0.05 el Å–2 s–1) to m` |  |
| PMC10290714 | `mol), TOF (min-1) = Yield/` |  |
| PMC10293723 | ` cm−1, 1041 cm−1, 825 cm−1` | oui |
| PMC10293723 | ` cm−1, 1247 cm−1, 1041 cm−` | oui |
| PMC10293723 | ` cm−1, 1369 cm−1, 1247 cm−` | oui |
| PMC10293723 | ` cm−1, 1600 cm−1, 1369 cm−` | oui |
| PMC10293723 | ` cm−1, 1714 cm−1, 1600 cm−` | oui |
| PMC10293723 | ` cm−1, 2842 cm−1, 1714 cm−` | oui |
| PMC10293723 | ` cm−1, 2919 cm−1, 2842 cm−` | oui |
| PMC10293723 | `08, and 531 cm−1 indicate ` | oui |
| PMC10293723 | `1 cm−1, 825 cm−1, 608, and` | oui |
| PMC10293723 | `4 cm−1,1600 cm−1 and 1369 ` | non |
| PMC10293723 | `4000 to 400 cm−1 with 4 cm` | non |
| PMC10293723 | `4000 to 400 cm−1 with 4 cm` | non |
| PMC10293723 | `aks at 1600 cm−1 and 1369 ` | non |
| PMC10293723 | `aks at 1714 cm−1,1600 cm−1` | non |
| PMC10293723 | `are at 2842 cm−1 and 1714 ` | non |
| PMC10293723 | `cm−1 with 4 cm−1 resolutio` | non |
| PMC10293723 | `cm−1 with 4 cm−1 resolutio` | non |
| PMC10293723 | `ing at 1268 cm−1 and 1076 ` | non |
| PMC10293723 | `m−1and 2842 cm−1 are regio` | non |
| PMC10293723 | `nds at 3390 cm−1 and CH3 a` | oui |
| PMC10293723 | `nds at 3390 cm−1, 2919 cm−` | oui |
| PMC10293723 | `t peak 2932 cm−1. The CC a` | non |
| PMC10293723 | `ted at 2919 cm−1and 2842 c` | non |
| PMC10293723 | `ved at 1600 cm−1 and 1389 ` | non |
| PMC10293723 | `ved at 3335 cm−1 is due to` | non |
| PMC10293723 | `−1 and 1076 cm−1 respectiv` | non |
| PMC10293723 | `−1 and 1369 cm−1 can be as` | non |
| PMC10293723 | `−1 and 1369 cm−1 that may ` | non |
| PMC10293723 | `−1 and 1389 cm−1 respectiv` | non |
| PMC10293723 | `−1 and 1714 cm−1, which ar` | non |
| PMC10324055 | ` 10 to 50 mg L–1 keeping t` | non |
| PMC10324055 | ` and 0.94 mg g–1 for phosp` | oui |
| PMC10324055 | ` and 0.99 mg g–1 for phosp` | oui |
| PMC10324055 | `.05 to 0.5 g L–1 using the` | non |
| PMC10324055 | `0 rpm) 0.1 g L–1 Ce(III)-B` | oui |
| PMC10324055 | `0, and 50 mg L–1). 0.2 g o` | non |
| PMC10324055 | `10 and 15 mg L–1 each prep` | oui |
| PMC10324055 | `23, and 753 cm–1 correspon` | oui |
| PMC10324055 | `38 and 1397 cm–1 represent` | oui |
| PMC10324055 | `MOF (1.34 m2 g–1).483.5SEM` | non |
| PMC10324055 | `OFs (5.28 m2 g–1)36 and Ce` | non |
| PMC10324055 | `adsorbed (mg g–1) at equil` | non |
| PMC10324055 | `and ΔS (KJ mol–1 K–1) repr` | non |
| PMC10324055 | `e and qt (mg g–1) are the ` | non |
| PMC10324055 | `eak at 3455 cm–1 represent` | non |
| PMC10324055 | `ge 400–4000 cm–1 using the` | non |
| PMC10324055 | `ion of 20 mg L–1 of both i` | non |
| PMC10324055 | `l), ΔH (KJ mol–1), and ΔS ` | non |
| PMC10324055 | `lot ln Kc vs T–1 (Figure S` | non |
| PMC10324055 | `ons (1000 mg L–1) were pre` | non |
| PMC10324055 | `ons of 10 mg L–1 for phosp` | non |
| PMC10324055 | `solution (mg L–1), V is th` | non |
| PMC10324055 | `te and 15 mg L–1 for fluor` | non |
| PMC10324055 | `ution (20 mg L–1) at diffe` | oui |
| PMC10324055 | `ution (20 mg L–1) in separ` | oui |
| PMC10324055 | `ved at 1502 cm–1 is associ` | oui |
| PMC10324055 | `ved at 2918 cm–1 indicates` | non |
| PMC10324055 | `was 15.20 m2 g–1, three-fo` | non |
| PMC10324055 | `xceed 1.5 mg L–1. In fact,` | non |
| PMC10324055 | `ΔS (KJ mol–1 K–1) represen` | non |
| PMC10326808 | ` (∼0.23 mmol g–1 at 0 °C a` | oui |
| PMC10326808 | ` and 0.15 g mL–1 displayed` | oui |
| PMC10326808 | ` and 0.15 g mL–1, respecti` | oui |
| PMC10326808 | ` and 1325 m2 g–1, respecti` | non |
| PMC10326808 | ` from 0.3 g mL–1, the samp` | non |
| PMC10326808 | ` of 0.075 g mL–1 (0.3 g of` | oui |
| PMC10326808 | ` of 0.075 g mL–1 (ZIF-8-Ou` | non |
| PMC10326808 | ` of 0.075 g mL–1 (or 4 mL ` | oui |
| PMC10326808 | ` of 0.075 g mL–1 [Figure S` | non |
| PMC10326808 | ` of 0.075 g mL–1 exhibited` | non |
| PMC10326808 | ` of 0.075 g mL–1 followed ` | oui |
| PMC10326808 | ` of 0.075 g mL–1 proved to` | oui |
| PMC10326808 | ` of 0.075 g mL–1 was appli` | non |
| PMC10326808 | ` of 0.075 g mL–1, includin` | non |
| PMC10326808 | ` to 0.025 g mL–1, or incre` | oui |
| PMC10326808 | `00 and 3650 cm–1, which in` | non |
| PMC10326808 | `02–1.14 mmol g–1 at 25 °C.` | oui |
| PMC10326808 | `12–2.24 mmol g–1 at 0 °C, ` | oui |
| PMC10326808 | `35 and 2928 cm–1, respecti` | non |
| PMC10326808 | `672 and 746 cm–1. A strong` | non |
| PMC10326808 | `C at 10 °C min–1 while mai` | non |
| PMC10326808 | `a of 1079 m2 g–1 obtained ` | oui |
| PMC10326808 | `and 0.025 g mL–1, respecti` | oui |
| PMC10326808 | `ange of 1 × 10–7 bar to 1 ` | oui |
| PMC10326808 | `at influx (W g–1) [Figure ` | non |
| PMC10326808 | `d ∼0.13 mmol g–1 at 25 °C ` | oui |
| PMC10326808 | `d ∼0.13 mmol g–1 at 25 °C,` | oui |
| PMC10326808 | `d ∼0.17 mmol g–1 at 25 °C)` | oui |
| PMC10326808 | `de = 25 mL min–1). A ∼1.5–` | non |
| PMC10326808 | `e (∼0.78 cm3 g–1). Additio` | non |
| PMC10326808 | `e at 25 mL min–1 and held ` | non |
| PMC10326808 | `e of 10 °C min–1 under a n` | oui |
| PMC10326808 | `e of 10 °C min–1 under a n` | oui |
| PMC10326808 | `e of 25 mL min–1 at 25 °C ` | oui |
| PMC10326808 | `e of 25 mL min–1. The samp` | non |
| PMC10326808 | `ea (∼1325 m2 g–1) and pore` | non |
| PMC10326808 | `ea of 685 m2 g–1 was obtai` | non |
| PMC10326808 | `en = 25 mL min–1), and the` | non |
| PMC10326808 | `f 1470.30 m2 g–1 and enhan` | oui |
| PMC10326808 | `i.e., 200 m2 g–1) (Figure ` | non |
| PMC10326808 | `i.e., 685 m2 g–1) and five` | non |
| PMC10326808 | `low 0.075 g mL–1 (or the H` | oui |
| PMC10326808 | `mL = 0.05 g mL–1) when 6 m` | oui |
| PMC10326808 | `me (0.78 cm3 g–1) than ZIF` | non |
| PMC10326808 | `me (0.95 cm3 g–1) for the ` | oui |
| PMC10326808 | `ne (0.38 cm3 g–1) (Table 1` | non |
| PMC10326808 | `o ∼0.21 mmol g–1 at 0 °C a` | oui |
| PMC10326808 | `of 480–4000 cm–1 to determ` | non |
| PMC10326808 | `ond 0.075 g mL–1 (or the H` | oui |
| PMC10326808 | `ound at 420 cm–1, confirmi` | oui |
| PMC10326808 | `ple (1079 m2 g–1), which w` | non |
| PMC10326808 | `s ∼0.19 mmol g–1 at 0 °C a` | oui |
| PMC10326808 | `s ∼2.24 mmol g–1 of CO2 at` | non |
| PMC10326808 | `ut (0.64 cm3 g–1). Interes` | non |
| PMC10336645 | ` and 160 μg mL−1 for U20S ` |  |
| PMC10336645 | `6, and 1 mol L−1. The UV a` |  |
| PMC10336645 | `6, and 1 mol L−1. Then, us` |  |
| PMC10336645 | `60 and 1650 cm−1 typical f` |  |
| PMC10336645 | `and at 1340 cm−1 from blue` |  |
| PMC10336645 | `and at 1590 cm−1 and risin` |  |
| PMC10336645 | `d to 160 μg mL−1, more tha` |  |
| PMC10336645 | `ith 0.08 mg mL−1 of P,N-CD` |  |
| PMC10336645 | `nds at 1017 cm−1, carboxyl` |  |
| PMC10336645 | `nds at 1710 cm−1 were sign` |  |
| PMC10336645 | `p to 1.0 mol L−1, the fluo` |  |
| PMC10336645 | `ure at 1600 cm−1 typical f` |  |
| PMC10336645 | `ution (5 mg mL−1 in PBS) w` |  |
| PMC10336645 | `ution (8 mg mL−1) was adde` |  |
| PMC10342551 | `N/s, a 50 m ns−1 acquisiti` | non |
| PMC10342551 | `ain of 0.011 s−1 with a dw` | non |
| PMC10350639 | `, 1034–1292 cm−1 are chara` | oui |
| PMC10350639 | `00 and 3750 cm−1, which co` | oui |
| PMC10350639 | `3, 4 and 5 A g−1). It is e` | non |
| PMC10350639 | `= 0.0020 mA cm−2). Co/H-AZ` | non |
| PMC10350639 | `= 0.0025 mA cm−2). So we c` | non |
| PMC10350639 | `F g−1 at 1 A g−1 for the C` | oui |
| PMC10350639 | `aks at 1218 cm−1 and 1451 ` | non |
| PMC10350639 | `aks at 2351 cm−1 and 2991 ` | non |
| PMC10350639 | `around 1612 cm−1 is attrib` | oui |
| PMC10350639 | `ate of 10 mV s−1 for all t` | non |
| PMC10350639 | `f 52.83 mA h g−1 at 1 A g−` | oui |
| PMC10350639 | `h g−1 at 1 A g−1 for the C` | oui |
| PMC10350639 | `h g−1 at 1 A g−1 which is ` | oui |
| PMC10350639 | `h g−1 at 1 A g−1 which is ` | oui |
| PMC10350639 | `nd 950–1090 cm−1 is due to` | oui |
| PMC10350639 | `nsity at 5 A g−1. Interest` | oui |
| PMC10350639 | `of 10–100 mV s−1 in a pote` | oui |
| PMC10350639 | `of 72.5 mA h g−1 at 1 A g−` | oui |
| PMC10350639 | `of 72.5 mA h g−1 at 1 A g−` | oui |
| PMC10350639 | `pacitance (F g−1), Qs is t` | non |
| PMC10350639 | `pacity (mA h g−1), I is th` | non |
| PMC10350639 | `rodes at 5 A g−1. Interest` | oui |
| PMC10350639 | `t 52.83 mA h g−1 compared ` | non |
| PMC10350639 | `t of 45.97 F g−1 at 1 A g−` | non |
| PMC10350639 | `urves at 1 A g−1 using eqn` | non |
| PMC10350639 | `ut 72.5 mA h g−1 compared ` | non |
| PMC10350639 | `−1 and 1451 cm−1 can be as` | non |
| PMC10350639 | `−1 and 2991 cm−1 can be as` | non |
| PMC10354497 | ` as 43.16 mg g−1, as per t` |  |
| PMC10354497 | `42 and 1730 cm−1 were assi` |  |
| PMC10354497 | `and at 2940 cm−1 correspon` |  |
| PMC10354497 | `as 500–4000 cm−1, utilizin` |  |
| PMC10354497 | `e of 10 mm min−1 for 20 ti` |  |
| PMC10354497 | `eak at 3338 cm−1, correspo` |  |
| PMC10354497 | `lution of 4 cm−1.2.6Mechan` |  |
| PMC10354497 | `on (0.04 mg mL−1) was prep` |  |
| PMC10354497 | `on of 10 mg mL−1 at 30 °C,` |  |
| PMC10354497 | `peak at 829 cm−1, associat` |  |
| PMC10354497 | `te of 0.5 mL h−1.The PAN/Z` |  |
| PMC10354497 | `thanol (50 g L−1) and ultr` |  |
| PMC10368083 | `14 and 1065 cm−1 are relat` |  |
| PMC10368083 | `766 and 655 cm−1, respecti` |  |
| PMC10368083 | `R (KBr): ν (cm−1) = 3336, ` |  |
| PMC10368083 | `R (KBr): ν (cm−1) = 3360, ` |  |
| PMC10368083 | `R (KBr): ν (cm−1) = 3362, ` |  |
| PMC10368083 | `R (KBr): ν (cm−1) = 3389, ` |  |
| PMC10368083 | `R (KBr): ν (cm−1) = 3403, ` |  |
| PMC10368083 | `R (KBr): ν (cm−1) = 3426, ` |  |
| PMC10368083 | `R (KBr): ν (cm−1) = 3446, ` |  |
| PMC10368083 | `R (KBr): ν (cm−1) = 3446, ` |  |
| PMC10368083 | `R (KBr): ν (cm−1) = 3459, ` |  |
| PMC10368083 | `R (KBr): ν (cm−1) = 3460, ` |  |
| PMC10368083 | `R (KBr): ν (cm−1) = 3465, ` |  |
| PMC10368083 | `R (KBr): ν (cm−1) = 3473, ` |  |
| PMC10368083 | `R (KBr): ν (cm−1) = 3474, ` |  |
| PMC10368083 | `R (KBr): ν (cm−1) = 3503, ` |  |
| PMC10368083 | `R (KBr): ν (cm−1) = 3609, ` |  |
| PMC10368083 | `and at 1104 cm−1 is relate` |  |
| PMC10368083 | `k 2800–3500 cm−1 is relate` |  |
| PMC10372942 | `44 and 1638 cm–1, where th` | non |
| PMC10372942 | `673 and 613 cm–1 ascribed ` | non |
| PMC10372942 | `84, and 748 cm–1 can be at` | non |
| PMC10372942 | `L) and 1538 cm–1 (B). Figu` | non |
| PMC10372942 | `a under 600 cm–1 were assi` | non |
| PMC10372942 | `aks at 1444 cm–1 (L) and 1` | non |
| PMC10372942 | `and at 1444 cm–1 is attrib` | non |
| PMC10372942 | `and at 1638 cm–1 is assign` | non |
| PMC10372942 | `f 1705–1720 cm–1, indicati` | oui |
| PMC10372942 | `ively. K1 (min–1) and K2 (` | non |
| PMC10372942 | `nd at ∼3450 cm–1 assigned ` | non |
| PMC10372942 | `of 1600–700 cm–1 are relat` | non |
| PMC10372942 | `red at 1387 cm–1 related t` | non |
| PMC10372942 | `red at 1662 cm–1 assigned ` | non |
| PMC10372942 | `red at 2930 cm–1 attribute` | non |
| PMC10372942 | `rium [qe (mg.g–1)] was cal` | non |
| PMC10372942 | `trations (mg·L–1) of metal` | non |
| PMC10383321 | ` at 477–447 cm−1 is associ` | oui |
| PMC10383321 | `[] and 3510 cm−1 [], which` | oui |
| PMC10383321 | `aks at 1377 cm−1 and 1262 ` | oui |
| PMC10383321 | `aks at 1538 cm−1 and 1462 ` | oui |
| PMC10383321 | `aks at 3781 cm−1 [] and 35` | oui |
| PMC10383321 | `d 1800–1600 cm−1 are relat` | oui |
| PMC10383321 | `ergy of 5 × 10−5 eV/atom, ` | non |
| PMC10383321 | `ge 4000–400 cm−1 with reso` | oui |
| PMC10383321 | `lution of 4 cm−1. Here, fo` | non |
| PMC10383321 | `ment of 5 × 10−4 Å, and ma` | non |
| PMC10383321 | `of 1000–500 cm−1 indicate ` | oui |
| PMC10383321 | `t 3020–2850 cm−1, whereas ` | non |
| PMC10383321 | `−1 and 1262 cm−1 correspon` | oui |
| PMC10383321 | `−1 and 1462 cm−1 are relat` | oui |
| PMC10386591 | ` 1.318 × 103 M−1 and 2.120` | oui |
| PMC10386591 | ` –C=O (1717 cm−1) and C-O-` | oui |
| PMC10386591 | `.120 × 10−5 Mm−1, respecti` | oui |
| PMC10386591 | `5, and 1118 cm−1 for the r` | oui |
| PMC10386591 | `C-O-C (1034 cm−1). The bro` | non |
| PMC10386591 | `and 2.120 × 10−5 Mm−1, res` | oui |
| PMC10386591 | `and at 1616 cm−1 is caused` | non |
| PMC10386591 | `ion at 3370 cm−1. The char` | non |
| PMC10386591 | `of 500–4000 cm−1. In FT-IR` | non |
| PMC10386591 | `of NBB (2 × 10−4 M) with t` | non |
| PMC10386591 | `of NBB (2 × 10−4 M). At 15` | non |
| PMC10386591 | `om 1 to 4 × 10−4 mol/L. Th` | oui |
| PMC10386591 | `ted at 3246 cm−1 can be at` | oui |
| PMC10405785 | ` cm−1, 1548 cm−1, and 2656` | oui |
| PMC10405785 | `), and 2157 cm−1 (iTOTA). ` | non |
| PMC10405785 | `1, and 2656 cm−1, respecti` | oui |
| PMC10405785 | `10) λ4 (ID/IG)−1where λ is` | non |
| PMC10405785 | `ALO−), 2065 cm−1 (iTALA/LO` | non |
| PMC10405785 | `aks at 1833 cm−1 (iTALO−),` | non |
| PMC10405785 | `and at 2614 cm−1 and the I` | non |
| PMC10405785 | `e from 1700 cm−1 to 2300 c` | non |
| PMC10405785 | `eak at 1014 cm−1 and 1074 ` | oui |
| PMC10405785 | `ed at ∼1750 cm−1 in AB sta` | non |
| PMC10405785 | `hift of ∼45 cm−1. In addit` | non |
| PMC10405785 | `m) = (2.4 × 10−10) λ4 (ID/I` | non |
| PMC10405785 | `m−1 to 2300 cm−1, exhibiti` | non |
| PMC10405785 | `nd at ∼2700 cm−1,23 wherea` | non |
| PMC10405785 | `nds at 1352 cm−1, 1548 cm−` | oui |
| PMC10405785 | `nds at 1683 cm−1,42 confir` | non |
| PMC10405785 | `onds at 716 cm−1 and stret` | oui |
| PMC10405785 | `rs at ∼1730 cm−1.31–33 It ` | non |
| PMC10405785 | `ure of ∼2 × 10−9 Torr. Tra` | oui |
| PMC10405785 | `−1 and 1074 cm−1, respecti` | oui |
| PMC10411504 | ` (1360–1370 cm–1) was abse` | non |
| PMC10411504 | ` value of 30 h–1 (0.5-SZ-6` | oui |
| PMC10411504 | `1.6 mmol h–1 g–1 (mol isos` | oui |
| PMC10411504 | `39, and 996 cm–1 correspon` | oui |
| PMC10411504 | `40 and 1445 cm–1, respecti` | oui |
| PMC10411504 | `7.0 mmol h–1 g–1, respecti` | oui |
| PMC10411504 | `76 and 1039 cm–1) has been` | non |
| PMC10411504 | `and 7.0 mmol h–1 g–1, resp` | oui |
| PMC10411504 | `and at 1075 cm–1, yet abse` | non |
| PMC10411504 | `and at 1630 cm–1 was ascri` | non |
| PMC10411504 | `around 3400 cm–1 attribute` | non |
| PMC10411504 | `at 11.6 mmol h–1 g–1 (mol ` | oui |
| PMC10411504 | `ated to 8 × 10–5 mbar. The` | oui |
| PMC10411504 | `ency (>1400 cm–1)73 was no` | non |
| PMC10411504 | `es (0.5–1.5 nm–2), reaches` | oui |
| PMC10411504 | `nsted sites·nm–2 and there` | non |
| PMC10411504 | `of 1360–880 cm–1 prior to ` | non |
| PMC10411504 | `of 500–4000 cm–1.Scanning ` | non |
| PMC10411504 | `ound 90 kJ mol–1. While th` | non |
| PMC10411504 | `rface (2.04 nm–2) is close` | non |
| PMC10411504 | `rom 13 to 23 h–1. Upon 625` | non |
| PMC10411504 | `ty (1.5–7.2 nm–2) as well ` | non |
| PMC10411504 | `um at ∼2.25 nm–2, and then` | oui |
| PMC10415108 | `-1 and 1440 cm-1 may be du` |  |
| PMC10415108 | `-8 (637.9 m2▪g–1) (Supplem` |  |
| PMC10415108 | `300 to 3000 cm-1 (). The b` |  |
| PMC10415108 | `440 and 421 cm-1 are attri` |  |
| PMC10415108 | `TiO2 at 450 cm-1 is relate` |  |
| PMC10415108 | `he 600-1300 cm-1 region ar` |  |
| PMC10415108 | `nts at 1620 cm-1 and 1440 ` |  |
| PMC10415108 | `quency (443 cm-1) after th` |  |
| PMC10420257 | ` around 330 cm−1, 385 cm−1` |  |
| PMC10420257 | `0 cm−1, 385 cm−1, 439 cm−1` |  |
| PMC10420257 | `5 cm−1, 439 cm−1 and 585 c` |  |
| PMC10420257 | `m−1 and 585 cm−1 and attri` |  |
| PMC10424190 | ` 0.2, 0.1 mV s−1, and the ` | non |
| PMC10424190 | ` and 1.17 × 10−12 (cm2 s−1)` | oui |
| PMC10424190 | ` are 1.92 × 10−13, 1.37 × 1` | oui |
| PMC10424190 | `, 53.43 mA h g−1, 68.35 mA` | oui |
| PMC10424190 | `, 68.35 mA h g−1 and 45.42` | oui |
| PMC10424190 | `3 and 0.5 mV·s−1, scanning` | non |
| PMC10424190 | `d 40.77 mA h g−1, respecti` | oui |
| PMC10424190 | `d 45.42 mA h g−1, respecti` | oui |
| PMC10424190 | `e 33.65 mA h g−1 of LVP-pH` | oui |
| PMC10424190 | `e 41.87 mA h g−1 of LVP-pH` | oui |
| PMC10424190 | `e 42.61 mA h g−1 of LVP-pH` | oui |
| PMC10424190 | `e 52.81 mA h g−1, 53.43 mA` | oui |
| PMC10424190 | `f 2C (200 mA g−1) in a pot` | non |
| PMC10424190 | `ficient (cm2 s−1) of Zn2+,` | non |
| PMC10424190 | `o 52.39 mA h g−1, which wa` | oui |
| PMC10424190 | `× 10−12 (cm2 s−1) for the ` | oui |
| PMC10424190 | `−12, 2.44 × 10−12 and 1.17 ` | oui |
| PMC10424190 | `−13, 1.37 × 10−12, 2.44 × 1` | oui |
| PMC10458794 | ` (325.2 mA h g−1) and MoS2` | oui |
| PMC10458794 | ` and 1596.7 cm−1, which ar` | non |
| PMC10458794 | ` and 500 mAh g−1 at 0.2 A ` | non |
| PMC10458794 | ` ca. 1.5 mg cm−2 on each e` | oui |
| PMC10458794 | ` g−1 at 10 A g−1. By combi` | non |
| PMC10458794 | ` of 366 mA h g−1 at 8.0 A ` | oui |
| PMC10458794 | ` of 605 mA h g−1 after 100` | oui |
| PMC10458794 | ` to 150 mA h g−1 after 400` | oui |
| PMC10458794 | `, 180.1 mA h g−1 after 500` | oui |
| PMC10458794 | `-M, at 0.1 A g−1. The MoS2` | non |
| PMC10458794 | `.0 and 5.0 A g−1, respecti` | oui |
| PMC10458794 | `.2 to 1.2 mV s−1. Figure 5` | non |
| PMC10458794 | `0, to 1.2 mV s−1, the capa` | oui |
| PMC10458794 | `0.1 to 5.0 A g−1. Figure 4` | non |
| PMC10458794 | `1 and 310.8 cm−1, which re` | oui |
| PMC10458794 | `O (363.4 mAh g−1). By cont` | non |
| PMC10458794 | `ar, at 5.0 A g−1, the MoS2` | oui |
| PMC10458794 | `ate at 0.1 A g−1. However,` | non |
| PMC10458794 | `cles at 10 A g−1. All the ` | non |
| PMC10458794 | `d 137.2 mA h g−1 after 600` | oui |
| PMC10458794 | `d 371.0 mA h g−1 at 0.1, 0` | oui |
| PMC10458794 | `d 742.3 mA h g−1, generati` | oui |
| PMC10458794 | `eed is 10° min−1. The SEM ` | non |
| PMC10458794 | `f 304.9 mA h g−1 after 100` | oui |
| PMC10458794 | `f 371.0 mA h g−1 after 100` | oui |
| PMC10458794 | `f 620.3 mA h g−1 after 100` | oui |
| PMC10458794 | `f 627.6 mA h g−1 after 100` | oui |
| PMC10458794 | `f 875.0 mA h g−1 and 742.3` | oui |
| PMC10458794 | `form 0.5 mg mL−1 sol. A mi` | oui |
| PMC10458794 | `gree of 2 × 10−9 Pa; Nitro` | oui |
| PMC10458794 | `g−1 and 10 A g−1, respecti` | non |
| PMC10458794 | `g−1 at 0.2 A g−1 and 10 A ` | non |
| PMC10458794 | `g−1 at 8.0 A g−1. Using a ` | non |
| PMC10458794 | `han 600 mA h g−1 after 80 ` | oui |
| PMC10458794 | `ion 6.73 mg mL−1, was synt` | oui |
| PMC10458794 | `ity at 0.1 A g−1 and long-` | non |
| PMC10458794 | `ity at 5.0 A g−1, exceedin` | non |
| PMC10458794 | `le at 221.0 cm−1 and 310.8` | oui |
| PMC10458794 | `les at 0.1 A g−1 (as shown` | non |
| PMC10458794 | `les at 0.1 A g−1 and rate ` | non |
| PMC10458794 | `les at 0.1 A g−1, and exce` | non |
| PMC10458794 | `les at 0.1 A g−1, which is` | non |
| PMC10458794 | `les at 0.1 A g−1. Note tha` | non |
| PMC10458794 | `les at 0.5 A g−1 and rate ` | non |
| PMC10458794 | `les at 5.0 A g−1; both of ` | non |
| PMC10458794 | `o be 30.3 m2 g−1 according` | oui |
| PMC10458794 | `ode at 0.1 A g−1. Figure 4` | non |
| PMC10458794 | `of 134.9 mAh g−1 at 10 A g` | non |
| PMC10458794 | `of 347.2 mAh g−1 after 230` | non |
| PMC10458794 | `of 409.2 mAh g−1 after 100` | non |
| PMC10458794 | `of 435.3 mAh g−1 after 100` | non |
| PMC10458794 | `on at 1.2 mV s−1 was 76.3%` | non |
| PMC10458794 | `r at 1340.6 cm−1 and 1596.` | non |
| PMC10458794 | `rea (30.3 m2 g−1) and meso` | non |
| PMC10458794 | `rea (30.3 m2 g−1) and meso` | non |
| PMC10458794 | `rea (30.3 m2 g−1), is well` | non |
| PMC10458794 | `s 1000–2000 cm−1.3.4. Elec` | non |
| PMC10458794 | `te of 0.1 mV s−1 between 0` | non |
| PMC10458794 | `te of 0.1 mV s−1 within th` | oui |
| PMC10458794 | `te of 5 °C min−1.For compa` | non |
| PMC10458794 | `y of 368 mAh g−1 after 100` | non |
| PMC10458794 | `y of 463 mAh g−1 and long ` | non |
| PMC10458794 | `ycles at 1 A g−1. From cob` | non |
| PMC10458794 | `ycles at 2 A g−1 and high-` | non |
| PMC10458794 | `ycles at 2 A g−1. Using a ` | non |
| PMC10460902 | ` 5192.2 µmol h−1 g−1. It c` | non |
| PMC10460902 | ` and 0.02 eV Å−1, respecti` | non |
| PMC10460902 | `.12 mmol h−1 g−1, which is` | non |
| PMC10460902 | `.12 mmol h−1 g−1, which is` | non |
| PMC10460902 | `00 and 1200 cm−1 are assoc` | non |
| PMC10460902 | `00 and 3000 cm−1 is the ch` | non |
| PMC10460902 | `1.2 µmol h−1 g−1. Zhang et` | non |
| PMC10460902 | `2.2 µmol h−1 g−1. It can b` | non |
| PMC10460902 | `4000 to 400 cm−1 were perf` | non |
| PMC10460902 | `GCN (0.004 min−1) (Figure ` | non |
| PMC10460902 | `VCN (0.055 min−1) is almos` | oui |
| PMC10460902 | `a of 59.8 m2 g−1, which is` | non |
| PMC10460902 | `ate of 5 K min−1 in nitrog` | oui |
| PMC10460902 | `ate of 5 K min−1. After co` | non |
| PMC10460902 | `d 10.24 mmol g−1 under lig` | oui |
| PMC10460902 | `d with 5 K min−1 to 863 K ` | oui |
| PMC10460902 | `f 561.2 µmol h−1 g−1. Zhan` | non |
| PMC10460902 | `of 5.12 mmol h−1 g−1, whic` | oui |
| PMC10460902 | `of 5.12 mmol h−1 g−1, whic` | oui |
| PMC10460902 | `peak at 810 cm−1 of all th` | non |
| PMC10460902 | `per atom of 10−5 eV and 0.` | non |
| PMC10473413 | `2 cm−1, 2931cm−1 were due ` |  |
| PMC10473413 | `aks at 3132 cm−1, 2931cm−1` |  |
| PMC10473413 | `eak at 3376 cm−1 implied t` |  |
| PMC10473413 | `eaks at 1420cm−1 and 1580 ` |  |
| PMC10473413 | `peak at 767 cm−1 indicated` |  |
| PMC10473413 | `vacuum (5 × 10−3 Pa). The ` |  |
| PMC10473413 | `−1 and 1580 cm−1 were belo` |  |
| PMC10489885 | ` of 1472 mF cm−2 at 1 mA c` | non |
| PMC10489885 | ` of 1572 mF cm−2 is obtain` | oui |
| PMC10489885 | ` of 46.2 Wh kg−1 even at a` | non |
| PMC10489885 | ` of 46.2 Wh kg−1 was achie` | non |
| PMC10489885 | `C g−1 at 1 A g−1). Moreove` | non |
| PMC10489885 | `C g−1 at 1 A g−1. Even at ` | non |
| PMC10489885 | `C g−1 at 1 A g−1. Moreover` | non |
| PMC10489885 | `F g−1 at 1 A g−1 due to it` | non |
| PMC10489885 | `and 26.6 Wh kg−1 at specif` | oui |
| PMC10489885 | `ased to 10 A g−1, the capa` | oui |
| PMC10489885 | `ate of 10 mV s−1 are displ` | non |
| PMC10489885 | `ate of 10 mV s−1, CV curve` | non |
| PMC10489885 | `ce of 1434 F g−1 at 1 A g−` | non |
| PMC10489885 | `eaches 509 C g−1. When the` | non |
| PMC10489885 | `er of 800 W kg−1, demonstr` | non |
| PMC10489885 | `er of 800 W kg−1, thus dem` | non |
| PMC10489885 | `g−1 at 1 mA cm−2) as a bin` | non |
| PMC10489885 | `ice is 208 C g−1 at 1 A g−` | oui |
| PMC10489885 | `m−2 at 1 mA cm−2 []. The e` | non |
| PMC10489885 | `nce (544.6 F g−1 at 1 mA c` | non |
| PMC10489885 | `nce of 120 C g−1 can still` | oui |
| PMC10489885 | `nce of 509 C g−1 at 1 A g−` | oui |
| PMC10489885 | `nd 16,000 W kg−1, respecti` | oui |
| PMC10489885 | `nsity of 1 A g−1, the disc` | oui |
| PMC10489885 | `om 1 to 20 A g−1, as shown` | oui |
| PMC10489885 | `s of 5–50 mV s−1, indicati` | non |
| PMC10489885 | `sity of 10 A g−1, the samp` | oui |
| PMC10489885 | `sity of 20 A g−1, a specif` | oui |
| PMC10489885 | `tance (509 C g−1 at 1 A g−` | oui |
| PMC10489885 | `ting at 10 A g−1 (Figure 5` | oui |
| PMC10489885 | `ucted at 1 A g−1, as shown` | non |
| PMC10489885 | `y of 1.5 mA cm−2. EIS test` | non |
| PMC10489885 | `ycles at 5 A g−1, as shown` | oui |
| PMC10493855 | ` (0–288 μmol L−1) of 2,6-D` | non |
| PMC10493855 | ` L−1 to μmol L−1.12,21 In ` | non |
| PMC10493855 | ` be 1.98 μg mm−2. As shown` | non |
| PMC10493855 | ` μA (μmol cm2)−1, where se` | non |
| PMC10493855 | `) of ∼1 μmol L−1.32,36–38 ` | non |
| PMC10493855 | `.24–288 μmol L−1 (R2 = 0.9` | oui |
| PMC10493855 | `.24–288 μmol L−1, and an i` | non |
| PMC10493855 | `HNPs of nmol L−1 to μmol L` | non |
| PMC10493855 | `as 0.02 μmol L−1 based on ` | oui |
| PMC10493855 | `ion (C, μmol L−1) in Fig. ` | oui |
| PMC10493855 | `of 425.26 m2 g−1 (Fig. S2†` | oui |
| PMC10493855 | `rents (20 mg L−1) chosen w` | oui |
| PMC10493855 | `t of 20 nmol L−1 for detec` | non |
| PMC10493855 | `to ∼0.1 μmol L−1.39 Despit` | non |
| PMC10493855 | `y low (∼nmol L−1) in drink` | non |
| PMC10511489 | ` 575 to 615 cm−1 are attri` |  |
| PMC10511489 | ` about 1440 cm−1 is attrib` |  |
| PMC10511489 | ` about 1490 cm−1 is assign` |  |
| PMC10511489 | `D6R) at 640 cm−1 for zeoli` |  |
| PMC10511489 | `and at 1540 cm−1 is attrib` |  |
| PMC10523092 | ` of 5.55 mg ml−1.2.3.Nanop` | non |
| PMC10529665 | `aks at 1246 cm−1 and 1158 ` | non |
| PMC10529665 | `aks at 1464 cm−1 and 1366 ` | non |
| PMC10529665 | `aks at 2939 cm−1 and 2852 ` | non |
| PMC10529665 | `and at 1636 cm−1 correspon` | non |
| PMC10529665 | `eak at 1108 cm−1 falls wit` | non |
| PMC10529665 | `eak at 1378 cm−1 is due to` | non |
| PMC10529665 | `eak at 1743 cm−1 is attrib` | non |
| PMC10529665 | `group (1420 cm−1) and the ` | oui |
| PMC10529665 | `idge at 669 cm−1, typical ` | non |
| PMC10529665 | `ion at 1104 cm−1 is caused` | oui |
| PMC10529665 | `ion at 1466 cm−1 and 1162 ` | non |
| PMC10529665 | `lution of 4 cm−1, and each` | non |
| PMC10529665 | `of 4000–500 cm−1, with a r` | non |
| PMC10529665 | `roups (1032 cm−1) can be o` | oui |
| PMC10529665 | `y 3400–3200 cm−1 and a ban` | non |
| PMC10529665 | `−1 and 1158 cm−1 are attri` | non |
| PMC10529665 | `−1 and 1162 cm−1 is attrib` | non |
| PMC10529665 | `−1 and 1366 cm−1 are cause` | non |
| PMC10529665 | `−1 and 2852 cm−1, which ar` | non |
| PMC10532637 | `2P (114 mV dec−1) and NPG ` | non |
| PMC10532637 | `PG (196 mV dec−1). A lower` | oui |
| PMC10532637 | `bout 72 mV dec−1, indicati` | oui |
| PMC10532637 | `ope (72 mV dec−1). This st` | oui |
| PMC10532637 | `peed of 5 mV s−1. Electroc` | non |
| PMC10532637 | `rate of 5 mV s−1 in 0.5 M ` | oui |
| PMC10532637 | `te of 100 mV s−1. As shown` | non |
| PMC10532637 | `te of 5 °C min−1 in an Ar ` | oui |
| PMC10532637 | `ted (29 mV dec−1), which i` | non |
| PMC10532637 | `ty of 10 mA cm−2. The obta` | oui |
| PMC10540474 | ` at 1020.34 cm−1, 1076.28 ` |  |
| PMC10540474 | ` at 1031.92 cm−1, 1116.78 ` |  |
| PMC10540474 | `and 2314.58 cm−1. In the s` |  |
| PMC10540474 | `and 2318.44 cm−1. Similarl` |  |
| PMC10540474 | `band at 576 cm−1, which wa` |  |
| PMC10540474 | `nge of 1000 cm−1 and 2350 ` |  |
| PMC10540474 | `of 4000–500 cm−1. The size` |  |
| PMC10540474 | `−1 and 2350 cm−1. Our resu` |  |
| PMC10540474 | `−1, 1076.28 cm−1, 1126.43 ` |  |
| PMC10540474 | `−1, 1116.78 cm−1, 1263.37 ` |  |
| PMC10540474 | `−1, 1126.43 cm−1, 1247.94 ` |  |
| PMC10540474 | `−1, 1247.94 cm−1, 1625.99 ` |  |
| PMC10540474 | `−1, 1263.37 cm−1, 1413.82 ` |  |
| PMC10540474 | `−1, 1413.82 cm−1, 1629.85 ` |  |
| PMC10540474 | `−1, 1625.99 cm−1and 2318.4` |  |
| PMC10540474 | `−1, 1629.85 cm−1, and 2314` |  |
| PMC10556056 | ` around 235 cm−1. The Rama` | non |
| PMC10556056 | ` around 270 cm−1 and LO pe` | oui |
| PMC10556056 | ` around 340 cm−1, supporti` | oui |
| PMC10556056 | ` around 427 cm−1 for all s` | oui |
| PMC10556056 | `0–3, 0.01 × 10–3, -0.25 × ` | oui |
| PMC10556056 | `0–3, 0.35 × 10–3 for ZnS0.` | oui |
| PMC10556056 | `ed as 2.7 × 10–3, − 3.9 × ` | oui |
| PMC10556056 | `ered at 320 cm−1 have a la` | oui |
| PMC10556056 | `mode at 390 cm−167. Raman ` | non |
| PMC10556056 | `–3, -0.25 × 10–3, 0.35 × 1` | oui |
| PMC10556056 | `–3, − 3.9 × 10–3, 0.01 × 1` | oui |
| PMC10573477 | ` (1105.2 mAh·g−1 at 0.1 A·` | oui |
| PMC10573477 | ` (1105.2 mAh·g−1 at 0.5 A·` | oui |
| PMC10573477 | ` V at 0.1 mV·s−1; (c) Cycl` | non |
| PMC10573477 | ` and 116 mAh·g−1), which m` | non |
| PMC10573477 | ` and 252 mAh·g−1 at the cu` | oui |
| PMC10573477 | ` and 345 mAh·g−1) than tha` | oui |
| PMC10573477 | ` and 385 mAh·g−1, respecti` | oui |
| PMC10573477 | ` and 437 mAh·g−1, respecti` | oui |
| PMC10573477 | ` and 5.01 m2·g−1, respecti` | oui |
| PMC10573477 | ` and 530 mAh·g−1 after 500` | oui |
| PMC10573477 | ` from 0.05 A·g−1 to 1 A·g−` | non |
| PMC10573477 | ` only 60 mAh·g−1 at 400 mA` | oui |
| PMC10573477 | `, and 82 mAh·g−1. It can b` | non |
| PMC10573477 | `1 to 252 mAh·g−1 with the ` | non |
| PMC10573477 | `1, and 1.0 A·g−1, respecti` | oui |
| PMC10573477 | `1, and 1.0 A·g−1, respecti` | oui |
| PMC10573477 | `A is 420 mAh·g−1 at 20 mA·` | oui |
| PMC10573477 | `A·g−1 to 1 A·g−1, the capa` | non |
| PMC10573477 | `A·g−1, 0.1 A·g−1, 0.2 A·g−` | oui |
| PMC10573477 | `A·g−1, 0.1 A·g−1, 0.2 A·g−` | oui |
| PMC10573477 | `A·g−1, 0.2 A·g−1, 0.5 A·g−` | oui |
| PMC10573477 | `A·g−1, 0.2 A·g−1, 0.5 A·g−` | oui |
| PMC10573477 | `A·g−1, 0.5 A·g−1, and 1.0 ` | oui |
| PMC10573477 | `A·g−1, 0.5 A·g−1, and 1.0 ` | oui |
| PMC10573477 | `B) (1283 mAh·g−1 at 0.1 A·` | oui |
| PMC10573477 | `C, and 1380 cm−1 can be in` | non |
| PMC10573477 | `Fe (1038 mAh·g−1). As a re` | non |
| PMC10573477 | `Fe at 0.1 mV·s−1. The HA-F` | non |
| PMC10573477 | `about 90 mAh·g−1 and 385 m` | oui |
| PMC10573477 | `aks at 1580 cm−1 can be in` | non |
| PMC10573477 | `are 1038 mAh·g−1 and 437 m` | oui |
| PMC10573477 | `around 3429 cm−1 is due to` | non |
| PMC10573477 | `ates (0.1 mV·s−1, 0.3 mV·s` | non |
| PMC10573477 | `bout 178 mAh·g−1 and 530 m` | oui |
| PMC10573477 | `d from 1380 cm−1 to 1395 c` | oui |
| PMC10573477 | `d from 1580 cm−1 to 1630 c` | oui |
| PMC10573477 | `d from 3429 cm−1 to 3439 c` | oui |
| PMC10573477 | `e of 586 mAh·g−1 after 100` | oui |
| PMC10573477 | `ed to 0.05 A·g−1, which sh` | non |
| PMC10573477 | `en 237.2 mAh·g−1 at 2 A·g−` | oui |
| PMC10573477 | `ers at 2920 cm−1 and 2852 ` | non |
| PMC10573477 | `es of 0.05 A·g−1, 0.1 A·g−` | oui |
| PMC10573477 | `es of 0.05 A·g−1, 0.1 A·g−` | oui |
| PMC10573477 | `from 462 mAh·g−1 to 252 mA` | non |
| PMC10573477 | `g−1 at 0.1 A·g−1) []. Zhu ` | non |
| PMC10573477 | `g−1 at 0.1 A·g−1) and ultr` | non |
| PMC10573477 | `g−1 at 0.1 A·g−1), cycle s` | non |
| PMC10573477 | `g−1 at 0.5 A·g−1 after 400` | non |
| PMC10573477 | `g−1 at 20 mA·g−1, while it` | non |
| PMC10573477 | `g−1, 120 mAh·g−1, and 82 m` | oui |
| PMC10573477 | `g−1, 175 mAh·g−1, 120 mAh·` | non |
| PMC10573477 | `g−1, 210 mAh·g−1, 175 mAh·` | non |
| PMC10573477 | `g−1, 309 mAh·g−1, and 252 ` | oui |
| PMC10573477 | `g−1, 398 mAh·g−1, 309 mAh·` | oui |
| PMC10573477 | `g−1, 447 mAh·g−1, 398 mAh·` | oui |
| PMC10573477 | `hat, 0.1 mol·L−1 NaOH solu` | oui |
| PMC10573477 | `h·g−1 at 2 A·g−1) []. Wu e` | non |
| PMC10573477 | `ies (241 mAh·g−1 and 345 m` | oui |
| PMC10573477 | `is 146.9 mAh·g−1, while af` | non |
| PMC10573477 | `ity (373 mAh·g−1) and poor` | non |
| PMC10573477 | `ity (586 mAh·g−1 at 0.1 A·` | oui |
| PMC10573477 | `ity of 0.1 A·g−1. The init` | non |
| PMC10573477 | `ity of 40 mA·g−1. Inspired` | non |
| PMC10573477 | `les (178 mAh·g−1).To furth` | non |
| PMC10573477 | `lity (10.0 A·g−1 over 16,0` | non |
| PMC10573477 | `m−1 to 1395 cm−1. Similar ` | non |
| PMC10573477 | `m−1 to 1630 cm−1, and the ` | oui |
| PMC10573477 | `m−1 to 3439 cm−1, the arom` | oui |
| PMC10573477 | `nd Fe at 1 A·g−1 are 55.63` | oui |
| PMC10573477 | `ned at 0.1 A·g−1 after 100` | non |
| PMC10573477 | `nt of 100 mA·g−1. Figure 4` | non |
| PMC10573477 | `re 105.42 m2·g−1 and 5.01 ` | oui |
| PMC10573477 | `rial (62 mAh·g−1 and 116 m` | oui |
| PMC10573477 | `s of 252 mAh·g−1, 210 mAh·` | non |
| PMC10573477 | `s of 462 mAh·g−1, 447 mAh·` | oui |
| PMC10573477 | `te of 0.1 mV·s−1, and the ` | oui |
| PMC10573477 | `with 0.1 mol·L−1 HCl solut` | oui |
| PMC10573477 | `y is 530 mAh·g−1, which is` | non |
| PMC10573477 | `y of 586 mAh·g−1 was maint` | non |
| PMC10573477 | `·s−1, 0.3 mV·s−1, 0.5 mV·s` | non |
| PMC10573477 | `·s−1, 0.5 mV·s−1, 0.7 mV·s` | non |
| PMC10573477 | `·s−1, 0.7 mV·s−1, 1.0 mV·s` | non |
| PMC10573477 | `·s−1, 1.0 mV·s−1), as show` | non |
| PMC10573477 | `−1 and 2852 cm−1. The peak` | non |
| PMC10573477 | `−1 at 400 mA·g−1, whose ca` | non |
| PMC10573519 | ` above 1000 cm−1, characte` |  |
| PMC10573519 | ` at 770–760 cm−1, 660 cm−1` |  |
| PMC10573519 | ` of 700–670 cm−1 observed ` |  |
| PMC10573519 | ` to 0.0009 min−1).Apparent` |  |
| PMC10573519 | `), 1200–850 cm−1 (B–O stre` |  |
| PMC10573519 | `0 and ~1200 cm−1 due to th` |  |
| PMC10573519 | `0 cm−1, 660 cm−1 and 630–6` |  |
| PMC10573519 | `00 and 1300 cm−1 could be ` |  |
| PMC10573519 | `1, 1200–900 cm−1 and 900–4` |  |
| PMC10573519 | `20 and 1130 cm−1 []. Accor` |  |
| PMC10573519 | `640 and 450 cm−1 [,,]. The` |  |
| PMC10573519 | `80 and 1040 cm−1) and OH g` |  |
| PMC10573519 | `80 and 1200 cm−1 could be ` |  |
| PMC10573519 | `: 1500–1200 cm−1, 1200–900` |  |
| PMC10573519 | `O2 (0.0065 min−1). Rate co` |  |
| PMC10573519 | `and 630–610 cm−1 can be as` |  |
| PMC10573519 | `and 800–600 cm−1 (bending ` |  |
| PMC10573519 | `and 900–400 cm−1. By analo` |  |
| PMC10573519 | `band at 635 cm−1 and a sho` |  |
| PMC10573519 | `e 1120–1040 cm−1 region (T` |  |
| PMC10573519 | `e 1500–1200 cm−1 (B–O stre` |  |
| PMC10573519 | `e below 700 cm−1 were main` |  |
| PMC10573519 | `f 1130–1040 cm−1 are relat` |  |
| PMC10573519 | `ge (700–600 cm−1), the vib` |  |
| PMC10573519 | `ion 700–400 cm−1 are chara` |  |
| PMC10573519 | `lder at 670 cm−1. On the o` |  |
| PMC10573519 | `m−1 and 880 cm−1 could be ` |  |
| PMC10573519 | `nt (0.0174 min−1) was obta` |  |
| PMC10573519 | `of 1600–400 cm−1 using the` |  |
| PMC10573519 | `of 1600–400 cm−1. Looking ` |  |
| PMC10573519 | `s below 900 cm−1, typical ` |  |
| PMC10573519 | `ut 1100–980 cm−1 and 880 c` |  |
| PMC10573519 | `ution of ±1 cm−1. The UV–V` |  |
| PMC10574157 | ` and 4.62 × 10−5 cm2 s−1 f` | non |
| PMC10574157 | ` of 5–200 mV s−1. The diff` | non |
| PMC10574157 | `% (5 to 17 A g−1) and 62.4` | non |
| PMC10574157 | `% (5 to 17 A g−1) for NiFe` | non |
| PMC10574157 | `(5 to 200 mV s−1) in vario` | non |
| PMC10574157 | `0−6, 1.87 × 10−5, 2.84 × 1` | oui |
| PMC10574157 | `1 × 10−5 cm2 s−1 for 0.1, ` | oui |
| PMC10574157 | `1, and 295 F g−1 for 5, 7,` | oui |
| PMC10574157 | `1, and 730 F g−1 for 5, 7,` | oui |
| PMC10574157 | `15, and 17 A g−1, respecti` | oui |
| PMC10574157 | `15, and 17 A g−1, respecti` | oui |
| PMC10574157 | `2 × 10−5 cm2 s−1 for prist` | oui |
| PMC10574157 | `4 × 10−5 cm2 s−1 for 0.1, ` | oui |
| PMC10574157 | `anges 5–17 A g−1 in ranges` | non |
| PMC10574157 | `kg−1, 330 W kg−1) and (30.` | oui |
| PMC10574157 | `kg−1, 357 W kg−1) for pris` | oui |
| PMC10574157 | `nd (30.2 Wh kg−1, 357 W kg` | oui |
| PMC10574157 | `of 10 A g−1 cm−2. For both` | non |
| PMC10574157 | `of 5 to 17 A g−1 was picke` | non |
| PMC10574157 | `re (11.2 Wh kg−1, 330 W kg` | oui |
| PMC10574157 | `rent of 10 A g−1 cm−2. For` | oui |
| PMC10574157 | `were 2.84 × 10−5 and 4.62 ` | non |
| PMC10583617 | ` and 0.36 × 10−3 to 1.80 ×` |  |
| PMC10583617 | ` and 10 mL min−1 flow rate` |  |
| PMC10583617 | ` and 10 mL min−1) into the` |  |
| PMC10583617 | ` and 10 mL min−1) which wa` |  |
| PMC10583617 | ` and 10 mL min−1, respecti` |  |
| PMC10583617 | ` and 10 mL min−1, the resi` |  |
| PMC10583617 | ` and 400 mg mL−1, and name` |  |
| PMC10583617 | ` as 1000 µg mL−1 as illust` |  |
| PMC10583617 | ` at 6.6 mg min−1 capacity ` |  |
| PMC10583617 | ` at ~690 µg mL−1, ~2650 µg` |  |
| PMC10583617 | ` for 10 mL min−1 flow rate` |  |
| PMC10583617 | ` from 1 mL min−1 to 5 mL m` |  |
| PMC10583617 | ` from 2.2 × 10−3 to 3.64 ×` |  |
| PMC10583617 | ` of 0.5 mL min−1. For inte` |  |
| PMC10583617 | ` of 7.7 mg min−1, however ` |  |
| PMC10583617 | ` only 60 µg mL−1 to mainta` |  |
| PMC10583617 | ` or 400 µmol L−1 was added` |  |
| PMC10583617 | `0 at 100 µg mL−1, S-CDs-20` |  |
| PMC10583617 | `0 to 100 µg mL−1 did not g` |  |
| PMC10583617 | `0/1 at 1 mg mL−1, CP@CDs20` |  |
| PMC10583617 | `1, ~2650 µg mL−1 and ~3080` |  |
| PMC10583617 | `2H at 25 µg mL−1.For MTT a` |  |
| PMC10583617 | `3 to 1.80 × 10−3 mol min−1` |  |
| PMC10583617 | `3 to 3.64 × 10−3 mol min−1` |  |
| PMC10583617 | `400 to 2600 cm−1 were shif` |  |
| PMC10583617 | `90 and 1590 cm−1 for D and` |  |
| PMC10583617 | `9H at 25 µg mL−1, and S-CD` |  |
| PMC10583617 | `aks at 2470 cm−1 (Figure 1` |  |
| PMC10583617 | `and at 1390 cm−1. As demon` |  |
| PMC10583617 | `and at 1590 cm−1 and the a` |  |
| PMC10583617 | `at <0.48 µg mL−1 (Table 3)` |  |
| PMC10583617 | `ate of 5°C min−1) in which` |  |
| PMC10583617 | `e was 1 mL min−1. The over` |  |
| PMC10583617 | `f 10–80 µL min−1, and low ` |  |
| PMC10583617 | `in−1, 5 mL min−1 and 10 mL` |  |
| PMC10583617 | `n PBS (5 mg mL−1) 10 times` |  |
| PMC10583617 | `n at 250 mg mL−1. At high ` |  |
| PMC10583617 | `n for 5 mL min−1 flow rate` |  |
| PMC10583617 | `nd ~3080 µg mL−1 from CP@C` |  |
| PMC10583617 | `on of 60 µg mL−1. An incre` |  |
| PMC10583617 | `s (0.19 mg min−1). The syn` |  |
| PMC10583617 | `te of 1 mL min−1 (CDs-280C` |  |
| PMC10583617 | `te of 1 mL min−1 at 260 an` |  |
| PMC10583617 | `te of 1 mL min−1 at differ` |  |
| PMC10583617 | `te of 1 mL min−1 at variou` |  |
| PMC10583617 | `te of 1 mL min−1 can be us` |  |
| PMC10583617 | `te of 1 mL min−1 decreased` |  |
| PMC10583617 | `te of 1 mL min−1 exhibited` |  |
| PMC10583617 | `te of 1 mL min−1 showed hi` |  |
| PMC10583617 | `te of 1 mL min−1 was appli` |  |
| PMC10583617 | `te of 1 mL min−1 was decre` |  |
| PMC10583617 | `te of 1 mL min−1 which was` |  |
| PMC10583617 | `te of 1 mL min−1 while hig` |  |
| PMC10583617 | `te of 1 mL min−1, 5 mL min` |  |
| PMC10583617 | `te of 1 mL min−1. The UV-v` |  |
| PMC10583617 | `te of 2.5 GS s−1 for ion d` |  |
| PMC10583617 | `til 1000 µg mL−1 while CP@` |  |
| PMC10583617 | `und at 2900 cm−1 [] as sho` |  |
| PMC10583617 | `using 5 mL min−1 and 10 mL` |  |
| PMC10583617 | `ution (2 mg mL−1), and the` |  |
| PMC10583617 | `°C at 1 mL min−1 flow rate` |  |
| PMC10583617 | `× 105 cells mL−1 in MEM α)` |  |
| PMC10583617 | `× 10−3 mol min−1 of citric` |  |
| PMC10583617 | `× 10−3 mol min−1 of urea a` |  |
| PMC10583617 | `−1 to 5 mL min−1 and 10 mL` |  |
| PMC10585300 | `cy at 474.5 cm−1 in the ca` | oui |
| PMC10585300 | `eak at 1000 cm−1 []. The s` | non |
| PMC10585300 | `eak at 1562 cm−1 is attrib` | non |
| PMC10585300 | `eak at 3500 cm−1 is attrib` | non |
| PMC10585300 | `eaks at 830 cm−1 and 678 c` | oui |
| PMC10585300 | `m−1 and 678 cm−1 respectiv` | oui |
| PMC10585300 | `nd at 453.2 cm−1 for ZnO p` | oui |
| PMC10585300 | `of 400–4000 cm−1 on an IR ` | non |
| PMC10585300 | `peak at 460 cm−1 is attrib` | non |
| PMC10585300 | `ved at 1390 cm−1 shows the` | non |
| PMC10625068 | ` of 25.28 mg g−1, proving ` | non |
| PMC10625068 | ` of 28.32 mg g−1 was close` | oui |
| PMC10625068 | ` was 3500 W kg−1.Additiona` | non |
| PMC10625068 | ` was 4.40 mg g−1, 3.53 mg ` | oui |
| PMC10625068 | `00 was 501 F g−1; whereas ` | oui |
| PMC10625068 | `10 to 200 mV s−1, indicati` | non |
| PMC10625068 | `10 to 200 mV s−1. The resu` | non |
| PMC10625068 | `326 to 501 F g−1. The adso` | non |
| PMC10625068 | `9–418.4 kJ mol−1. Comparat` | non |
| PMC10625068 | `F g−1 at 1 A g−1. This wor` | non |
| PMC10625068 | `and 25.28 mg g−1, respecti` | oui |
| PMC10625068 | `ation of 4 g L−1 despite t` | oui |
| PMC10625068 | `ched 111.3 F g−1. Nyquist ` | non |
| PMC10625068 | `d −53.4 KJ mol−1, respecti` | non |
| PMC10625068 | `e of 111.3 F g−1 at 1 A g−` | non |
| PMC10625068 | `g−1 at 0.5 A g−1. Furtherm` | non |
| PMC10625068 | `g−1, 3.53 mg g−1, and 25.2` | oui |
| PMC10625068 | `it was 326 F g−1 at 0.5 A ` | oui |
| PMC10625068 | `m 0.1 to 4 g L−1, cubic γ‐` | oui |
| PMC10625068 | `nds at 1350 cm−1 and 1580 ` | oui |
| PMC10625068 | `nsity of 1 A g−1, the spec` | oui |
| PMC10625068 | `of 10–200 mV s−1. Even at ` | non |
| PMC10625068 | `of 594.61 m2 g−1, and its ` | non |
| PMC10625068 | `pared at 3 g L−1 GO, the C` | non |
| PMC10625068 | `rate (200 mV s−1), the CV ` | non |
| PMC10625068 | `red with 3 g L−1 GO exhibi` | non |
| PMC10625068 | `s 152.8 W h kg−1, and the ` | oui |
| PMC10625068 | `sity of 20 A g−1. The uniq` | non |
| PMC10625068 | `tions of 3 g L−1 revealed ` | non |
| PMC10625068 | `tions of 3 g L−1. This phe` | non |
| PMC10625068 | `−1 and 1580 cm−1. These ba` | non |
| PMC10631235 | ` from 199.9 cm−1 to 196.7 ` |  |
| PMC10631235 | ` from 203.7 cm−1 for pure ` |  |
| PMC10631235 | ` from 298.1 cm−1 to 294.7 ` |  |
| PMC10631235 | ` from 298.8 cm−1 for pure ` |  |
| PMC10631235 | `)LO and 305 cm−1 for ν(CdS` |  |
| PMC10631235 | `98 K) 199.5 cm−1).40 The m` |  |
| PMC10631235 | `Se is 203.7 cm−1, while fo` |  |
| PMC10631235 | `cy is 298.8 cm−1. These pe` |  |
| PMC10631235 | `dS to 292.6 cm−1 for CdS0.` |  |
| PMC10631235 | `e, to 194.9 cm−1 for CdS0.` |  |
| PMC10631235 | `ement is ∼4 cm−1 greater t` |  |
| PMC10631235 | `es are 5–16 cm−1 lower tha` |  |
| PMC10631235 | `h an 1800 g mm−1 grating a` |  |
| PMC10631235 | `ies are 2–5 cm−1 higher th` |  |
| PMC10631235 | `ion at ∼200 cm−1 and two o` |  |
| PMC10631235 | `ion at ∼300 cm−1 (Fig. S10` |  |
| PMC10631235 | `lues of 211 cm−1 for ν(CdS` |  |
| PMC10631235 | `lution is 6 cm−1 as determ` |  |
| PMC10631235 | `ser to ±1.5 cm−1.Conclusio` |  |
| PMC10631235 | `wer than ±1 cm−1, and meas` |  |
| PMC10631235 | `−1 to 196.1 cm−1 as the in` |  |
| PMC10631235 | `−1 to 196.7 cm−1 to 196.1 ` |  |
| PMC10631235 | `−1 to 294.2 cm−1. For both` |  |
| PMC10631235 | `−1 to 294.7 cm−1 to 294.2 ` |  |
| PMC10674298 | ` rarely in mgL−1, EPs are ` | non |
| PMC10674298 | `ant (Kapp, min−1), Co and ` | non |
| PMC10674298 | `ions, from µgL−1 to ngL−1 ` | non |
| PMC10674298 | `m µgL−1 to ngL−1 and rarel` | non |
| PMC10682491 | ` 5 to 100 mV s−1. The dist` |  |
| PMC10682491 | ` density (W kg−1) and t is` |  |
| PMC10682491 | ` g−1 at 10 A g−1. When ope` |  |
| PMC10682491 | ` to be 853 F g−1. The NC-M` |  |
| PMC10682491 | ` using 2 mol L−1 KOH as th` |  |
| PMC10682491 | `(F g−1 or F cm−2), I is th` |  |
| PMC10682491 | `, with 3 mol L−1 KOH servi` |  |
| PMC10682491 | `//AC (25 Wh kg−1 at 447 W ` |  |
| PMC10682491 | `//AC (29 Wh kg−1 at 800 W ` |  |
| PMC10682491 | `10 to 100 mV s−1 within th` |  |
| PMC10682491 | `AC (33.5 Wh kg−1 at 150 W ` |  |
| PMC10682491 | `AC (43.3 Wh kg−1 at 800 W ` |  |
| PMC10682491 | `AC (45.5 Wh kg−1 at 512 W ` |  |
| PMC10682491 | `C-which C (F g−1) is speci` |  |
| PMC10682491 | `CS (42.3 Wh kg−1 at 476 W ` |  |
| PMC10682491 | `F g−1 at 1 A g−1). Ning et` |  |
| PMC10682491 | `F g−1 at 1 A g−1, and stil` |  |
| PMC10682491 | `F g−1 at 1 A g−1. Dai et a` |  |
| PMC10682491 | `F g−1 at 2 A g−1, and exce` |  |
| PMC10682491 | `S (12.035 m2 g−1). As the ` |  |
| PMC10682491 | `ate of 20 mV s−1 in the 3 ` |  |
| PMC10682491 | `ate of 30 mV s−1 from 0.0 ` |  |
| PMC10682491 | `ate of 80 mV s−1. Therefor` |  |
| PMC10682491 | `be 0.036 cm3 g−1 while for` |  |
| PMC10682491 | `be 52.803 m2 g−1, which is` |  |
| PMC10682491 | `ce of 1078 F g−1 at 1 A g−` |  |
| PMC10682491 | `ce of 2115 F g−1 at 2 A g−` |  |
| PMC10682491 | `ce of 2115 F g−1 at a curr` |  |
| PMC10682491 | `density (Wh kg−1), Csp is ` |  |
| PMC10682491 | `des in 3 mol L−1 KOH aqueo` |  |
| PMC10682491 | `e of 222.5 F g−1 at 1 A g−` |  |
| PMC10682491 | `e, and 3 mol L−1 KOH as th` |  |
| PMC10682491 | `hed 1865.2 F g−1 at a curr` |  |
| PMC10682491 | `ient (> 104 cm−1), and its` |  |
| PMC10682491 | `in the 3 mol L−1 KOH elect` |  |
| PMC10682491 | `kHz in 3 mol L−1 KOH elect` |  |
| PMC10682491 | `m 5 to 50 mV s−1) by Eqs. ` |  |
| PMC10682491 | `nce of 169 F g−1 at 10 A g` |  |
| PMC10682491 | `nce of 395 F g−1 at a curr` |  |
| PMC10682491 | `nce of 747 F g−1 at 1 A g−` |  |
| PMC10682491 | `nce of 853 F g−1 at a curr` |  |
| PMC10682491 | `nce of 992 F g−1 at a curr` |  |
| PMC10682491 | `nsity of 1 A g−1. Among th` |  |
| PMC10682491 | `nsity of 1 A g−1. Yang et ` |  |
| PMC10682491 | `nsity of 1 A g−1. Zhao et ` |  |
| PMC10682491 | `nsity of 2 A g−1 and 81% p` |  |
| PMC10682491 | `nsity of 2 A g−1 and 91% p` |  |
| PMC10682491 | `nsity of 2 A g−1 as displa` |  |
| PMC10682491 | `nsity of 8 A g−1. The cycl` |  |
| PMC10682491 | `ode in 3 mol L−1 KOH aqueo` |  |
| PMC10682491 | `of 60.56 Wh kg−1 and a hig` |  |
| PMC10682491 | `of 60.56 Wh kg−1 at a spec` |  |
| PMC10682491 | `of 60.56 Wh kg−1, correspo` |  |
| PMC10682491 | `of 699.89 W kg−1, making i` |  |
| PMC10682491 | `of 699.89 W kg−1, which is` |  |
| PMC10682491 | `of 699.89 W kg−1. Most imp` |  |
| PMC10682491 | `om 1 to 10 A g−1 with a vo` |  |
| PMC10682491 | `om 1 to 10 A g−1. The spec` |  |
| PMC10682491 | `om 2 to 17 A g−1. As the c` |  |
| PMC10682491 | `om 2 to 17 A g−1. More sig` |  |
| PMC10682491 | `om 2 to 17 A g−1. This ser` |  |
| PMC10682491 | `pacitance (F g−1 or F cm−2` |  |
| PMC10682491 | `pacitance (F g−1), ΔV is t` |  |
| PMC10682491 | `s in a 3 mol L−1 KOH aqueo` |  |
| PMC10682491 | `s with 3 mol L−1 HCl solut` |  |
| PMC10682491 | `to 0.025 cm3 g−1.To invest` |  |
| PMC10682491 | `to be 2115 F g−1, while th` |  |
| PMC10682491 | `−1 at 150 W kg−1)52, CoS/g` |  |
| PMC10682491 | `−1 at 447 W kg−1)54.Eventu` |  |
| PMC10682491 | `−1 at 476 W kg−1)26, and N` |  |
| PMC10682491 | `−1 at 512 W kg−1)51, Ni-Co` |  |
| PMC10682491 | `−1 at 800 W kg−1)22, NiCo2` |  |
| PMC10682491 | `−1 at 800 W kg−1)53, NiCo2` |  |
| PMC10698638 | ` and C2 (mg mL−1) refer to` |  |
| PMC10698638 | ` of 0.47 cm3 g−1 was obtai` |  |
| PMC10698638 | ` to 4.343 × 10−3 for CRL@Z` |  |
| PMC10698638 | `.2 ± 1.8 μg mL−1 (0.115 ± ` |  |
| PMC10698638 | `.6 ± 1.3 μg mL−1 (0.1 ± 0.` |  |
| PMC10698638 | `8 and 692.4 cm−1 are ascri` |  |
| PMC10698638 | `; Vmax (mM min−1) and Km (` |  |
| PMC10698638 | `L MTT (5 mg mL−1) was adde` |  |
| PMC10698638 | `a of 1340 m2 g−1 and a tot` |  |
| PMC10698638 | `and at 1420 cm−1. Finally,` |  |
| PMC10698638 | `and at 1574 cm−1 is associ` |  |
| PMC10698638 | `and at 2930 cm−1 is due to` |  |
| PMC10698638 | `band at 421 cm−1 can be as` |  |
| PMC10698638 | `cid at 1710 cm−1 exists in` |  |
| PMC10698638 | `ea of 572 m2 g−1 and a tot` |  |
| PMC10698638 | `eak at 1657 cm−1 correspon` |  |
| PMC10698638 | `ity ≫ 700 U mg−1), para-ni` |  |
| PMC10698638 | `n of 200 μg mL−1. The calc` |  |
| PMC10698638 | `of 0.638 cm3 g−1. Compared` |  |
| PMC10698638 | `of 4000–400 cm−1. A Hitach` |  |
| PMC10698638 | `rom 3.796 × 10−3 for free ` |  |
| PMC10698638 | `t 1350–1500 cm−1 belong to` |  |
| PMC10698638 | `t 3300–3400 cm−1 is observ` |  |
| PMC10698638 | `te of 1 mL min−1.The conve` |  |
| PMC10698638 | `th 1–200 μg mL−1 of the co` |  |
| PMC10698638 | `× 100C1 (mg mL−1) and C2 (` |  |
| PMC10708100 | ` (1836.352 m2g−1) and much` |  |
| PMC10708100 | `nS (12.662 m2g−1). It may ` |  |
| PMC10708100 | `s 1151.684 m2g−1, which is` |  |
| PMC10725426 | `H2 (at 3345 cm−1) of M1 di` |  |
| PMC10725426 | `M2) to 1692 cm−1 (imide 2D` |  |
| PMC10725426 | `de at 385.5 cm–1, associat` |  |
| PMC10725426 | `e at 405.07 cm–1, related ` |  |
| PMC10725426 | `g from 1763 cm−1 (anhydrid` |  |
| PMC10725426 | `ift of 1.22 cm–1 was obser` |  |
| PMC10725426 | `pot at 0.33 nm–1 aligns pe` |  |
| PMC10725426 | `red at 1403 cm−1 (Figure S` |  |
| PMC10725426 | `t Qxy = 0.48 Å-1 was retai` |  |
| PMC10725426 | `t Qxy = 0.48 Å-1, d100 = 1` |  |
| PMC10754887 | ` and 1.38 × 10−5 S/cm). Th` | oui |
| PMC10754887 | ` and 1.67 × 10−5 S/cm) and` | oui |
| PMC10754887 | ` and 2.09 × 10−14). This co` | non |
| PMC10754887 | ` and 2.49 × 10−13 cm2/s) ar` | non |
| PMC10754887 | ` and 4.16 × 10−13 cm2/s, re` | non |
| PMC10754887 | `00 and 3600 cm−1 correspon` | oui |
| PMC10754887 | `C-3, 2.45 × 10−5 S/cm). Mo` | oui |
| PMC10754887 | `C-5 (7.38 × 10−15, 8.00 × 1` | oui |
| PMC10754887 | `C/C, 1.46 × 10−4 S/cm). Du` | oui |
| PMC10754887 | `are at 1695 cm−1 and 1573 ` | oui |
| PMC10754887 | `cted at 448 cm−1 []. Meanw` | non |
| PMC10754887 | `ion (4.37 × 10−3 mol/cm3),` | oui |
| PMC10754887 | `ity (2.45 × 10−5 S/cm), hi` | oui |
| PMC10754887 | `m−1 and 800 cm−1, respecti` | oui |
| PMC10754887 | `nd 1.7546 × 10−4 S/cm, res` | oui |
| PMC10754887 | `ple (1.73 × 10−4 S/cm and ` | oui |
| PMC10754887 | `t of 1.46 × 10−4 S/cm and ` | oui |
| PMC10754887 | `t of 3.49 × 10−13 for 2% Sn` | non |
| PMC10754887 | `und at 1076 cm−1 and 800 c` | oui |
| PMC10754887 | `−1 and 1573 cm−1, respecti` | oui |
| PMC10754887 | `−15, 8.00 × 10−15, and 2.09` | oui |
| PMC10780621 | ` 61 to 39 m2 g−1 as the HF` | non |
| PMC10780621 | ` to 0.08 cm3 g−1 and from ` | non |
| PMC10815866 | ` (≈178.3 mAh g−1) capaciti` | oui |
| PMC10815866 | ` (≈180.7 mAh g−1) and disc` | oui |
| PMC10815866 | ` and 134 mAh g−1 at the 80` | oui |
| PMC10815866 | ` and 190 mAh g−1, respecti` | oui |
| PMC10815866 | `, and 600 mA g−1, respecti` | oui |
| PMC10815866 | `, and 68 mAh g−1 at 40, 10` | oui |
| PMC10815866 | `0 to 200 mAh g−1). This ra` | non |
| PMC10815866 | `1 to 162 mAh g−1 at the 30` | oui |
| PMC10815866 | `acity of mAh g−1 after 80 ` | oui |
| PMC10815866 | `and ≈183 mAh g−1 of discha` | oui |
| PMC10815866 | `and ≈196 mAh g−1 of discha` | oui |
| PMC10815866 | `ate of 12 mA g−1 (after 30` | non |
| PMC10815866 | `ately 151 mAhg−1 []. In Na` | non |
| PMC10815866 | `city (90 mAh g−1) is less ` | non |
| PMC10815866 | `d ≈112.5 mAh g−1 of initia` | oui |
| PMC10815866 | `d ≈152.5 mAh g−1 of initia` | oui |
| PMC10815866 | `ding 117 mAh g−1 of revers` | oui |
| PMC10815866 | `ity (242 mAh g−1) []. P2-N` | non |
| PMC10815866 | `les at 20 mA g−1 was margi` | non |
| PMC10815866 | `ode at 20 mA g−1. The NFM-` | non |
| PMC10815866 | `only ≈45 mAh g−1. This mea` | non |
| PMC10815866 | `tial 196 mAh g−1 to 162 mA` | oui |
| PMC10815866 | `ty of 193 mAhg−1 []. Never` | non |
| PMC10815866 | `ty of 200 mA g−1. Synchrot` | non |
| PMC10815866 | `y of 170 mAh g−1, which is` | non |
| PMC10815866 | `y of 190 mAh g−1, higher t` | non |
| PMC10815866 | `y of 196 mAh g−1 and maint` | non |
| PMC10818925 | ` (8.3145 J·mol−1·K−1), and` | non |
| PMC10818925 | ` and BT (J·mol−1) is a con` | non |
| PMC10818925 | ` and a 1 mg·mL−1 adsorbent` | non |
| PMC10818925 | ` of 82.64 mg·g−1 at 45 °C,` | non |
| PMC10818925 | ` to 1.93 µg·kg−1; however,` | non |
| PMC10818925 | `(0.02–100 mg·L−1) and a 1 ` | non |
| PMC10818925 | `(0.02–100 mg·L−1). Thereaf` | non |
| PMC10818925 | `) and Ce (mg·L−1) represen` | non |
| PMC10818925 | `) and Qt (mg·g−1) are the ` | non |
| PMC10818925 | `0, and 60 mg·L−1) and vari` | non |
| PMC10818925 | `0−CemVC0 (mg·L−1) and Ce (` | non |
| PMC10818925 | `1–59.49 kJ·mol−1) and nega` | non |
| PMC10818925 | `25 ± 0.71 mg·g−1 at an ini` | non |
| PMC10818925 | `3145 J·mol−1·K−1), and T i` | non |
| PMC10818925 | `78 ± 0.17 mg·g−1 at 25 °C,` | oui |
| PMC10818925 | `; and k2 (g·mg−1·min−1) is` | non |
| PMC10818925 | `L−1); Qe (mg·g−1) is the a` | non |
| PMC10818925 | `O=C–O (1380 cm−1), and alk` | oui |
| PMC10818925 | `and 82.86 mg·g−1 at 25, 35` | non |
| PMC10818925 | `be 87.094 m2·g−1 following` | oui |
| PMC10818925 | `capacity (mg·g−1) of AFB1 ` | oui |
| PMC10818925 | `capacity (mg·g−1) of the p` | oui |
| PMC10818925 | `capacity (mg·g−1) was assa` | non |
| PMC10818925 | `city (Qe, mg·g−1) as a fun` | non |
| PMC10818925 | `constant (L·mg−1), which i` | non |
| PMC10818925 | `e; and Q (mg·g−1) is the a` | non |
| PMC10818925 | `ely; AT (L·mol−1) is the e` | non |
| PMC10818925 | `ergy; KF (mg·g−1) and n ar` | non |
| PMC10818925 | `etween 1750 cm−1 and 1500 ` | oui |
| PMC10818925 | `ilibrium (mg·L−1); Qe (mg·` | non |
| PMC10818925 | `ion of 60 mg·L−1, and adso` | oui |
| PMC10818925 | `ion of 60 mg·L−1, the adso` | oui |
| PMC10818925 | `ion of 60 mg·L−1.2.2. Char` | non |
| PMC10818925 | `k2 (g·mg−1·min−1) is the P` | non |
| PMC10818925 | `l C=O (1725 cm−1), carboxy` | oui |
| PMC10818925 | `lution of 1 cm−1. The crys` | non |
| PMC10818925 | `mately 1580 cm−1 and 547 c` | oui |
| PMC10818925 | `m−1 and 547 cm−1. The form` | non |
| PMC10818925 | `n [,]. k1 (min−1) is the P` | non |
| PMC10818925 | `nd 0.483 cm3·g−1, respecti` | oui |
| PMC10818925 | `o −7.49 kJ·mol−1) indicate` | non |
| PMC10818925 | `of 4000–500 cm−1 with a re` | non |
| PMC10818925 | `om 8.621 µg·kg−1 to 1.93 µ` | non |
| PMC10818925 | `rom 5–50 mg·mL−1 []. Anima` | non |
| PMC10818925 | `se and 40 mg·L−1 AFB1 at d` | non |
| PMC10818925 | `tant; Qe (mg·g−1) and Qt (` | non |
| PMC10818925 | `than 20 kJ·mol−1 [,]. Thes` | non |
| PMC10818925 | `than 40 kJ·mol−1, while ΔH` | non |
| PMC10818925 | `ty; Qmax (mg·g−1) is the m` | non |
| PMC10818925 | `with a 1 mg·mL−1 adsorbent` | non |
| PMC10818925 | `y C–O (1062 cm−1) [].The n` | non |
| PMC10818925 | `−1 and 1500 cm−1 could be ` | oui |
| PMC10835253 | ` such as AlPO4−8 and VPI−5` |  |
| PMC10835253 | `081 and 804 cm−1) correspo` |  |
| PMC10835253 | `band at 963 cm−1 attributa` |  |
| PMC10835253 | `band at 963 cm−1, accompan` |  |
| PMC10835253 | `e band (456 cm−1) exhibits` |  |
| PMC10835253 | `e material UTD−1 was synth` |  |
| PMC10835253 | `en at (3450 cm−1) suggests` |  |
| PMC10835253 | `lPO4−8 and VPI−5, were syn` |  |
| PMC10835253 | `nd at (1635 cm−1) reflects` |  |
| PMC10835253 | `of 4000-400 cm−1 for consi` |  |
| PMC10835264 | ` CuS at 50 mVs−1 in cyclic` |  |
| PMC10835264 | ` band (1423 cm−1), G band ` |  |
| PMC10835264 | ` band (1559 cm−1), and 2D ` |  |
| PMC10835264 | `.71 μA mM−1 cm−2 and 1.52 ` |  |
| PMC10835264 | `.71 μA mM−1 cm−2, a linear` |  |
| PMC10835264 | `e 252.71 μA mM−1 cm−2 and ` |  |
| PMC10835264 | `eaks at 470 cm−1 and 912 c` |  |
| PMC10835264 | `es (10-100 mVs−1) demonstr` |  |
| PMC10835264 | `f 252.71 μA mM−1 cm−2, a l` |  |
| PMC10835264 | `m−1 and 912 cm−1 correspon` |  |
| PMC10835264 | `nd 2D (2840 cm−1) band hig` |  |
| PMC10856232 | `4000 to 400 cm−1. The meas` |  |
| PMC10856232 | `97, and 461 cm−1 were ascr` |  |
| PMC10856232 | `97, and 461 cm−1, caused b` |  |
| PMC10856232 | `ing at 1514 cm−1, also obs` |  |
| PMC10856232 | `nds at 1514 cm−1, attribut` |  |
| PMC10856232 | `ons at 1514 cm−1 further s` |  |
| PMC10870029 | ` and 1.15 × 10−3 A cm−2 fo` | oui |
| PMC10870029 | ` and 1.24 × 10−5 W cm−2 fo` | oui |
| PMC10870029 | ` and 1.24 × 10−5 W cm−2, r` | oui |
| PMC10870029 | ` and 1.24 × 10−5 W cm−2, r` | oui |
| PMC10870029 | ` and 3.80 × 10−6 A cm−2 fo` | oui |
| PMC10870029 | ` and 7.56 × 10−17 W Hz−0.5 ` | oui |
| PMC10870029 | ` and 8.40 × 10−16 W cm−2 fo` | oui |
| PMC10870029 | ` nm, 4.89 × 10−7 W cm−2) f` | oui |
| PMC10870029 | ` −2) versus T −1 plots are` | non |
| PMC10870029 | `0 × 10−16 W cm−2 for the C` | oui |
| PMC10870029 | `0−3, 1.51 × 10−3, and 1.15` | oui |
| PMC10870029 | `0−3, 1.76 × 10−3, 1.94 × 1` | oui |
| PMC10870029 | `0−3, 1.94 × 10−3, 2.23 × 1` | oui |
| PMC10870029 | `0−3, 2.23 × 10−3, 1.51 × 1` | oui |
| PMC10870029 | `0−6, 3.48 × 10−6, 4.45 × 1` | oui |
| PMC10870029 | `0−6, 4.12 × 10−6, 4.77 × 1` | oui |
| PMC10870029 | `0−6, 4.45 × 10−6, and 3.80` | oui |
| PMC10870029 | `0−6, 4.77 × 10−6, 3.48 × 1` | oui |
| PMC10870029 | `15 × 10−3 A cm−2 for P3HT:` | oui |
| PMC10870029 | `24 × 10−5 W cm−2 for the C` | oui |
| PMC10870029 | `24 × 10−5 W cm−2, respecti` | non |
| PMC10870029 | `24 × 10−5 W cm−2, respecti` | non |
| PMC10870029 | `24 × 10−5 W cm−2. Contrary` | non |
| PMC10870029 | `29 × 10−6 A cm−2. The Scho` | non |
| PMC10870029 | `6 × 10−17 W cm−2 and LDR o` | non |
| PMC10870029 | `80 × 10−6 A cm−2 for P3HT:` | oui |
| PMC10870029 | `89 × 10−7 W cm−2) for 25 h` | oui |
| PMC10870029 | `P of 7.56 × 10−17 W cm−2 an` | oui |
| PMC10870029 | `acuum (≈5 × 10−6 torr). Th` | oui |
| PMC10870029 | `al of 40 mg mL−1 was used ` | oui |
| PMC10870029 | `ding ln(J s T −2) versus T` | non |
| PMC10870029 | `e of 4.29 × 10−6 A cm−2. T` | oui |
| PMC10870029 | `e of ≈84 µC cm−2, implying` | non |
| PMC10870029 | `n of 0.4 mg mL−1 at room t` | oui |
| PMC10870029 | `over 1.24 × 10−4 and 1.24 ` | oui |
| PMC10870029 | `rates (10 Ω sq−1) were pur` | oui |
| PMC10870029 | `ues (1.24 × 10−4 and 1.24 ` | oui |
| PMC10870029 | `ues (1.30 × 10−16 and 7.56 ` | oui |
| PMC10870029 | `ues (1.45 × 10−15 and 8.40 ` | oui |
| PMC10870029 | `were 1.61 × 10−3, 1.76 × 1` | oui |
| PMC10870029 | `were 5.09 × 10−6, 4.12 × 1` | oui |
| PMC10870029 | `y of 1.24 × 10−5 W cm−2. C` | oui |
| PMC10870712 | ` around 600 cm–1 originate` | oui |
| PMC10870712 | `00 and 1601 cm–1 correspon` | non |
| PMC10870712 | `4000 to 400 cm–1. Thermogr` | non |
| PMC10870712 | `acuated to ∼10–6 Torr.13 L` | non |
| PMC10870712 | `ered at 848 cm–1 is visibl` | non |
| PMC10870712 | `ion of 0.25 cm–1 over a sp` | oui |
| PMC10870712 | `re was <1 × 10–10 mbar. The` | non |
| PMC10883016 | ` 0.25 to 3 g L–1 led to an` | oui |
| PMC10883016 | `, and 4 mL min–1 were used` | oui |
| PMC10883016 | `, and 4 mL min–1, OG dye i` | oui |
| PMC10883016 | `0.25 and 3 g L–1. To exami` | oui |
| PMC10883016 | `014 to 1041 cm–1, possibly` | oui |
| PMC10883016 | `1 to 9.49 mg g–1. This can` | non |
| PMC10883016 | `162.435 kJ mol–1 K–1) indi` | oui |
| PMC10883016 | `20 to 220 mg L–1.The typic` | non |
| PMC10883016 | `435 kJ mol–1 K–1) indicate` | non |
| PMC10883016 | `47 and 3435 cm–1 were ascr` | non |
| PMC10883016 | `500 to 1700 cm–1, correspo` | non |
| PMC10883016 | `595 to 1556 cm–1 due to th` | oui |
| PMC10883016 | `605 and 567 cm–1, respecti` | non |
| PMC10883016 | `62 and 1423 cm–1.29 The Cs` | non |
| PMC10883016 | `62 and 1556 cm–1 were obse` | oui |
| PMC10883016 | `80 and 1029 cm–1 were attr` | non |
| PMC10883016 | `and at 3340 cm–1 (associat` | oui |
| PMC10883016 | `and at 3469 cm–1, indicati` | oui |
| PMC10883016 | `ation (20 mg L–1), with du` | oui |
| PMC10883016 | `cm and 20 mg L–1 at pH = 6` | oui |
| PMC10883016 | `e 2920–2875 cm–1 region sh` | non |
| PMC10883016 | `eak at 1660 cm–1 was assig` | non |
| PMC10883016 | `eak at 2931 cm–1, represen` | oui |
| PMC10883016 | `ion of 20 mg L–1.41 The fi` | non |
| PMC10883016 | `ions at 875 cm–1 and 1100–` | oui |
| PMC10883016 | `le the 1595 cm–1 band corr` | non |
| PMC10883016 | `m 5 to 80 mg L–1 .46 Howev` | non |
| PMC10883016 | `m 5 to 80 mg L–1, and colu` | oui |
| PMC10883016 | `mount Qe (mg g–1) and perc` | non |
| PMC10883016 | `nd 1100–962 cm–1 were attr` | oui |
| PMC10883016 | `red at 1230 cm–1, attribut` | oui |
| PMC10883016 | `te of 3 mL min–1 and an in` | oui |
| PMC10883016 | `−61.572 kJ mol–1) suggests` | non |
| PMC10888240 | ` = 0.06–3.1 nm−1. The scat` |  |
| PMC10888240 | ` at 960–970 cm−1 refers to` |  |
| PMC10888240 | `0, and 1640 cm−1 [,]. Peak` |  |
| PMC10888240 | `00, and 460 cm–1 correspon` |  |
| PMC10888240 | `250 and 900 cm–1 is, in al` |  |
| PMC10888240 | `d 1085–1073 cm−1.The appea` |  |
| PMC10888240 | `e 1630–1640 cm–1 band, sin` |  |
| PMC10888240 | `ge 4000–400 cm−1 and at a ` |  |
| PMC10888240 | `lution of 4 cm−1, using ta` |  |
| PMC10888240 | `n at q = 0.2 Å−1 correspon` |  |
| PMC10888240 | `of 4000–400 cm−1, are show` |  |
| PMC10888240 | `ons at 3750 cm−1 testifies` |  |
| PMC10888240 | `out 960–970 cm−1 confirms ` |  |
| PMC10888240 | `re of 1.3 × 10−1 Pa for 2 ` |  |
| PMC10888240 | `t 1630–1640 cm−1 correspon` |  |
| PMC10888240 | `t 3340–3400 cm–1 correspon` |  |
| PMC10888240 | `the 960–970 cm−1 band corr` |  |
| PMC10906077 | ` (2850–3000 cm–1), ν(C=C–H` | non |
| PMC10906077 | ` from 2.8 × 10–2 to 6.8 × ` | oui |
| PMC10906077 | ` glum < 7 × 10–3.33 Organi` | non |
| PMC10906077 | ` of ±1.18 × 10–2. This pos` | non |
| PMC10906077 | `C=O) = 1720 cm–1 and νs(CO` | non |
| PMC10906077 | `C–H) = 3005 cm–1, and ν(C–` | non |
| PMC10906077 | `OO–) = 1412 cm–1, and both` | non |
| PMC10906077 | `eak at 1371 cm–1 and an N–` | oui |
| PMC10906077 | `eak at 1371 cm–1 and of th` | oui |
| PMC10906077 | `ines at 800 cm–1, confirmi` | oui |
| PMC10906077 | `lution of 4 cm–1. Backgrou` | non |
| PMC10906077 | `m = ±1.18 × 10–2 at 510 ≤ ` | oui |
| PMC10906077 | `m = ±1.18 × 10–2 from the ` | non |
| PMC10906077 | `mine at 800 cm–1 (Figure S` | non |
| PMC10906077 | `oment (<3 × 10–3).9,10 Org` | non |
| PMC10906077 | `t 2850–3000 cm–1 and disap` | oui |
| PMC10906077 | `t 2850–3000 cm–1, which ty` | non |
| PMC10906077 | `uence (≪1015 s–1) using a ` | non |
| PMC10906077 | `um of 6.8 × 10–2. To the b` | non |
| PMC10906077 | `um of 6.8 × 10–2. To the b` | non |
| PMC10906077 | `–2 to 6.8 × 10–2, measured` | oui |
| PMC10906077 | `–H2) = 1466 cm–1 where ν i` | non |
| PMC10956410 | ` 0.02 at 2 min–1 steps, op` |  |
| PMC10956410 | ` at 772–568 cm–1 in PEI N-` |  |
| PMC10956410 | `3, and 1388 cm–1, respecti` |  |
| PMC10956410 | `4, and 1397 cm–1, respecti` |  |
| PMC10956410 | `51 and 3391 cm–1, while C–` |  |
| PMC10956410 | `816–785–616 cm–1 in PdNPs/` |  |
| PMC10956410 | `recorded in cm–1 units, we` |  |
| PMC10956410 | `ved at 1302 cm–1. In the s` |  |
| PMC10964133 | ` (57.58 kJ mol−1) is lower` | oui |
| PMC10964133 | ` and 0.69 mL g−1 for ZIF-8` | oui |
| PMC10964133 | `(391.67 kJ mol−1), implyin` | non |
| PMC10964133 | `d 1337.87 m2 g−1 respectiv` | oui |
| PMC10964133 | `f 1425.94 m2 g−1 and 1337.` | oui |
| PMC10964133 | `g near 1423 cm−1, all kept` | non |
| PMC10964133 | `ring at 421 cm−1 and 1586 ` | non |
| PMC10964133 | `−1 and 1586 cm−1, the plan` | non |
| PMC10967699 | ` 10 to 30 mg L−1, as depic` | non |
| PMC10967699 | ` 10 to 30 mg L−1. Degradat` | non |
| PMC10967699 | ` 72 to 36 mg g−1 when the ` | oui |
| PMC10967699 | ` about 1000 cm−1 was due t` | non |
| PMC10967699 | ` about 1400 cm−1 was due t` | non |
| PMC10967699 | ` and 0.12 g mg−1 min−1, re` | oui |
| PMC10967699 | ` be 79.80 m2 g−1 for PCN-6` | oui |
| PMC10967699 | ` the MNZ (mg L−1), and KF ` | non |
| PMC10967699 | ` to −20 kJ mol−1 suggest m` | non |
| PMC10967699 | ` units of L mg−1. A plot o` | non |
| PMC10967699 | ` units of mg g−1, at vario` | non |
| PMC10967699 | `.12 g mg−1 min−1, respecti` | oui |
| PMC10967699 | `.314 J mol−1 K−1; T denote` | non |
| PMC10967699 | `0, and 1500 cm−1 represent` | oui |
| PMC10967699 | `0, and 30 mg L−1, respecti` | oui |
| PMC10967699 | `0, and 40 mg L−1, respecti` | oui |
| PMC10967699 | `00–129.1 J mol−1) and as p` | non |
| PMC10967699 | `10 and 30 mg L−1. The infl` | non |
| PMC10967699 | `25.2 J mol−1 K−1 indicates` | oui |
| PMC10967699 | `57 and 58 mg g−1, respecti` | oui |
| PMC10967699 | `9 to 74.4 mg g−1 with incr` | non |
| PMC10967699 | `adsorbed (mg g−1) and the ` | non |
| PMC10967699 | `and 0.0054 min−1 for PCN-6` | oui |
| PMC10967699 | `and 25.85 m2 g−1 for PCN-6` | oui |
| PMC10967699 | `and −80 kJ mol−1 indicate ` | non |
| PMC10967699 | `asured in mg L−1; qm is th` | non |
| PMC10967699 | `asured in mg g−1; the vari` | non |
| PMC10967699 | `ately 0.02 g L−1, was imme` | oui |
| PMC10967699 | `d −4.05 kJ mol−1, which si` | oui |
| PMC10967699 | `e of 5–40 mg L−1. The outc` | non |
| PMC10967699 | `ely 25.2 J mol−1 K−1 indic` | oui |
| PMC10967699 | `ion of 30 mg L−1. This was` | non |
| PMC10967699 | `ity of 24 mg g−1 at adsorp` | oui |
| PMC10967699 | `l (<4.2 kJ mol−1), and the` | non |
| PMC10967699 | `ly 2.99 kJ mol−1 for the a` | non |
| PMC10967699 | `m 5 to 40 mg L−1. The high` | non |
| PMC10967699 | `nd 2.99 kJ mol−1 based on ` | oui |
| PMC10967699 | `nge of 1700 cm−1, which wa` | oui |
| PMC10967699 | `ntration (mg L−1); (qe) is` | non |
| PMC10967699 | `of 8.314 J mol−1 K−1; T de` | oui |
| PMC10967699 | `on of 100 mg L−1. The expe` | non |
| PMC10967699 | `solution (mg L−1) at the p` | non |
| PMC10967699 | `sorbed in mg g−1, Ce is th` | non |
| PMC10967699 | `sorbed in mg g−1; the vari` | non |
| PMC10967699 | `terial in mg L−1; and KL i` | non |
| PMC10975348 | ` were 57 emu g−1 and 12 em` |  |
| PMC10975348 | `1 and 12 emu g−1 for start` |  |
| PMC10975348 | `e of 10 °C min−1 under air` |  |
| PMC10975348 | `e of 10 °C min−1, from roo` |  |
| PMC10975348 | `ed to 467 m2 g−1, and the ` |  |
| PMC10975348 | `is 74–80 emu g−1, while fo` |  |
| PMC10975348 | `it is 84 emu g−1 []. Never` |  |
| PMC10975348 | `n of 200 μg mL−1 []. Folic` |  |
| PMC10975348 | `nol (47 mmol L−1) was slow` |  |
| PMC10975348 | `s at 200 μg mL−1 [].Notabl` |  |
| PMC10975348 | `te of 3 °C min−1. After 6 ` |  |
| PMC10975348 | `tion (12 emu g−1), enablin` |  |
| PMC10975348 | `to be 630 m2 g−1 and 2.7 n` |  |
| PMC10975348 | `w of 50 mL min−1.2.4. Diss` |  |
| PMC11001879 | ` equal 3.0 A g−1 is presen` | oui |
| PMC11001879 | ` of 119.04 F g-1 at a curr` | non |
| PMC11001879 | ` to 20.0 mA cm-2. To calcu` | non |
| PMC11001879 | `0 to 50.0 mV s-1 as shown ` | non |
| PMC11001879 | `0 to 50.0 mV s-1. While, G` | non |
| PMC11001879 | `00 and 2950 cm−1 in the IR` | non |
| PMC11001879 | `1.0 to 3.0 A g-1 at the sa` | non |
| PMC11001879 | `1.0 to 3.0 A·g-1) and disp` | non |
| PMC11001879 | `16 and 2044 cm-1 are assig` | non |
| PMC11001879 | `25-AC, 870 F·g-1 for MF45-` | oui |
| PMC11001879 | `5 to 1223 m2.g–1 for MF25-` | non |
| PMC11001879 | `5, and 276 F·g-1, respecti` | oui |
| PMC11001879 | `5, and 3.0 A·g-1 using Eq.` | oui |
| PMC11001879 | `5, and 3.0 A·g−1, respecti` | oui |
| PMC11001879 | `5, and 396 F·g−1 at curren` | oui |
| PMC11001879 | `576 and 427 cm−1. The wave` | non |
| PMC11001879 | `98 and 870 F g-1 at a curr` | oui |
| PMC11001879 | `C, and 800 F·g-1 for MF65-` | oui |
| PMC11001879 | `a of 178 m2 g –1, which is` | non |
| PMC11001879 | `and 826.5 F. g–1 in case o` | oui |
| PMC11001879 | `around 3000 cm−1 correspon` | non |
| PMC11001879 | `at ca. 3398 cm-1 that asso` | oui |
| PMC11001879 | `ched 2134 m2 g–1, while pu` | non |
| PMC11001879 | `d to 1423 m2 g–1 at MF65-A` | oui |
| PMC11001879 | `d to be 96 F·g-1 for AC, 4` | oui |
| PMC11001879 | `e of 870.0 F g-1 at curren` | oui |
| PMC11001879 | `eak at 1437 cm-1 was relat` | non |
| PMC11001879 | `een at 1036 cm-1, that was` | non |
| PMC11001879 | `ity of 1.0 A g-1 and the e` | non |
| PMC11001879 | `ity of 1.0 A g-1 in KOH, H` | oui |
| PMC11001879 | `k near 2950 cm−1 is associ` | non |
| PMC11001879 | `nce of 758 F g-1 at molar ` | non |
| PMC11001879 | `nsity 250 W kg-1. Increasi` | non |
| PMC11001879 | `nsity of 1 A g-1. Arun Kum` | non |
| PMC11001879 | `o 15.56 W h kg-1 at power ` | non |
| PMC11001879 | `o be 2134 m2 g–1 and decre` | non |
| PMC11001879 | `or AC, 402 F·g-1 for MF, 5` | oui |
| PMC11001879 | `or MF, 516 F·g-1 for MF25-` | oui |
| PMC11001879 | `t 15.56 W·h·kg−1 with a co` | oui |
| PMC11001879 | `ty of 250 W·kg−1. This ene` | non |
| PMC11001879 | `ual to 448 F g–1 at curren` | non |
| PMC11001879 | `ved at 1631 cm-1 may be as` | non |
| PMC11002299 | ` 1320.15 µM. L-1 and depic` | non |
| PMC11002299 | ` as 2.352 µAµM-1cm−2. The ` | non |
| PMC11002299 | `2.352 µAµM-1cm−2. The prac` | non |
| PMC11002299 | `352 µA µM−1 cm−2. The LOD ` | non |
| PMC11002299 | `of 2.352 µA µM−1 cm−2. The` | oui |
| PMC11007835 | ` one at 529 cm–1 correspon` |  |
| PMC11007835 | `100 to 3500 cm–1. Fourier-` |  |
| PMC11007835 | `152 and 643 cm–1 correspon` |  |
| PMC11007835 | `24 and 1400 cm–1 became mo` |  |
| PMC11007835 | `400 to 1000 cm–1 correspon` |  |
| PMC11007835 | `400 to 4000 cm–1. Thermogr` |  |
| PMC11007835 | `around 1200 cm–1 correspon` |  |
| PMC11007835 | `around 1400 cm–1 indicates` |  |
| PMC11007835 | `around 1624 cm–1 is attrib` |  |
| PMC11007835 | `peak at 400 cm–1 correspon` |  |
| PMC11007835 | `t 3050–3600 cm–1 that corr` |  |
| PMC11036359 | ` than 1.0 × 10–6 eV.3Resul` | non |
| PMC11036359 | ` than 5.0 × 10–3 eV. The e` | non |
| PMC11098855 | ` (1080-1063 cm−1), [(973 c` | oui |
| PMC11098855 | ` about 20 emug−1. These MN` | non |
| PMC11098855 | ` at 602-630 cm−1 can prove` | oui |
| PMC11098855 | `), (801-808 cm−1)], and (4` | oui |
| PMC11098855 | `1d) to 1645 cm−1 (Fig. 1e)` | oui |
| PMC11098855 | `41 and 1388 cm−1, respecti` | non |
| PMC11098855 | `57 and 2931 cm−1 confirm t` | oui |
| PMC11098855 | `BT@ZnCl2) emug−1. This dem` | non |
| PMC11098855 | `KBr) (vmax, cm−1): 3373, 3` | non |
| PMC11098855 | `KBr) (vmax, cm−1): 3398, 3` | non |
| PMC11098855 | `KBr) (νmax, cm−1): 3458, 3` | non |
| PMC11098855 | `KBr) (νmax, cm−1): 3464, 3` | non |
| PMC11098855 | `KBr) (νmax, cm−1): 3468, 3` | non |
| PMC11098855 | `KBr) (ῡmax, cm−1): 3358, 3` | non |
| PMC11098855 | `KBr) (ῡmax, cm−1): 3385, 3` | non |
| PMC11098855 | `KBr) (ῡmax, cm−1): 3391, 3` | non |
| PMC11098855 | `and at 1653 cm−1 in Fig. 1` | oui |
| PMC11098855 | `d 1627-1645 cm−1 are due t` | non |
| PMC11098855 | `he 400-4000 cm−1 using KBr` | non |
| PMC11098855 | `m−1), [(973 cm−1), (801-80` | oui |
| PMC11098855 | `nd (461-467 cm−1), respect` | oui |
| PMC11098855 | `s from 1653 cm−1 (Fig. 1d)` | oui |
| PMC11098855 | `t 3412-3423 cm−1 and 1627-` | non |
| PMC11099149 | ` about 1092 cm−1 (asymmetr` | oui |
| PMC11099149 | ` about 3440 cm−1 (stretchi` | oui |
| PMC11099149 | `, 1679–1460 cm−1 are due t` | non |
| PMC11099149 | `15 (686.9 m2 g−1) is more ` | non |
| PMC11099149 | `and at 1680 cm−1 is attrib` | oui |
| PMC11099149 | `band at 751 cm−1 is assign` | non |
| PMC11099149 | `eak at 1575 cm−1 proves th` | oui |
| PMC11099149 | `eak at 3171 cm−1 indicates` | non |
| PMC11099149 | `eak of 2930 cm−1 indicates` | oui |
| PMC11099149 | `ion of 1092 cm−1 Si–O–Si b` | non |
| PMC11099149 | `of 400–4000 cm–1 using the` | non |
| PMC11099149 | `out 792–970 cm−1 (stretchi` | oui |
| PMC11099149 | `t about 472 cm−1 (bending ` | oui |
| PMC11145745 | ` 3440, 3389 cm−1 correspon` |  |
| PMC11145745 | ` and 512 μg mL−1. The cult` |  |
| PMC11145745 | ` cm−1, 1640 cm−1 and 1030–` |  |
| PMC11145745 | ` mL−1, 4 μg mL−1, 16 μg mL` |  |
| PMC11145745 | ` of 19.8 μg mL−1. Combined` |  |
| PMC11145745 | ` to 105 CFU mL−1 in RPMI 1` |  |
| PMC11145745 | ` to 105 CFU mL−1 in RPMI 1` |  |
| PMC11145745 | ` to 106 CFU mL−1 in LB med` |  |
| PMC11145745 | `, and 64 μg mL−1 ZnO/r-LNT` |  |
| PMC11145745 | `aks at 2930 cm−1, 1640 cm−` |  |
| PMC11145745 | `d 1030–1300 cm−1 are commo` |  |
| PMC11145745 | `d with 0 μg mL−1, 4 μg mL−` |  |
| PMC11145745 | `ge from 400 cm−1 to 4000 c` |  |
| PMC11145745 | `ion of 2 mg mL−1 and the s` |  |
| PMC11145745 | `ion of 2 mg mL−1 in RPMI 1` |  |
| PMC11145745 | `lue of 8 μg mL−1. The anti` |  |
| PMC11145745 | `mL−1, 16 μg mL−1, and 64 μ` |  |
| PMC11145745 | `m−1 to 4000 cm−1. X-ray ph` |  |
| PMC11145745 | `ons of 2 mg mL−1 were prep` |  |
| PMC11145745 | `peak at 468 cm−1 which att` |  |
| PMC11145745 | `rison, 5 mg mL−1 LNT or 5 ` |  |
| PMC11145745 | `up of 64 μg mL−1 ZnO/r-LNT` |  |
| PMC11197016 | ` and 1350 W kg−1, respecti` | oui |
| PMC11197016 | ` and 1350 W kg−1, respecti` | oui |
| PMC11197016 | ` and 203.7 C g−1, respecti` | oui |
| PMC11197016 | ` and 452.3 F g−1 for nativ` | oui |
| PMC11197016 | `, 12.73 W h kg−1 and power` | oui |
| PMC11197016 | `, and 200 mV s−1) as shown` | oui |
| PMC11197016 | `3.6, 452.3 F g−1, energy d` | non |
| PMC11197016 | `4, 5 and 6 A g−1). In corr` | oui |
| PMC11197016 | `7.1, 203.7 C g−1, specific` | non |
| PMC11197016 | `ak (600–500 cm−1) is evide` | non |
| PMC11197016 | `d 1000–1400 cm−1 for the s` | oui |
| PMC11197016 | `d 12.73 W h kg−1 and power` | oui |
| PMC11197016 | `e of 204.9 F g−1 at the cu` | non |
| PMC11197016 | `eaks at 850 cm−1 and 1000–` | oui |
| PMC11197016 | `n 3200–3600 cm−1 indicates` | non |
| PMC11197016 | `nce of 120 F g−1.7 Kumar e` | non |
| PMC11197016 | `nce of 207 F g−1 in 1 M Na` | non |
| PMC11197016 | `nce of 277 F g−1 retained ` | non |
| PMC11197016 | `nsity of 1 A g−1.10 Furthe` | non |
| PMC11197016 | `nsity of 2 A g−1, which de` | non |
| PMC11197016 | `nsity of 2 A g−1, which de` | non |
| PMC11197016 | `nsity of 2 A g−1. A compar` | non |
| PMC11197016 | `of 4000–500 cm−1. The FTIR` | non |
| PMC11197016 | `peak at 508 cm−1 signifies` | oui |
| PMC11197484 | `at q = 0.717 Å−1, correspo` |  |
| PMC11197484 | `at q = 0.822 Å−1 (n = 3, (` |  |
| PMC11197484 | `below 2.0 × 10−4 Pa.2.2.5.` |  |
| PMC11231976 | `524 and 536 cm–1, indicati` | oui |
| PMC11231976 | `and 590–595 cm–1, unequivo` | oui |
| PMC11231976 | `ands at 484 cm–1 and 590–5` | oui |
| PMC11231976 | `band at 691 cm–1 (A1g) ind` | oui |
| PMC11231976 | `ucture (595 cm–1 correspon` | oui |
| PMC11243152 | ` and 1.19 × 10−9 cm2/s, re` | oui |
| PMC11243152 | `2/s, 7.95 × 10−10 cm2/s, an` | oui |
| PMC11243152 | `o be 1.03 × 10−9 cm2/s, 7.` | oui |
| PMC11266555 | ` at 730–770 cm-1 region in` | non |
| PMC11266555 | ` ν-OH: 3100 cm-1) vanish i` | non |
| PMC11266555 | `(νC=O: 1690 cm-1; δC=O: 52` | non |
| PMC11266555 | `; δC=O: 528 cm-1; ν-OH: 31` | non |
| PMC11266555 | `around 3465 cm-1 confirms ` | non |
| PMC11266555 | `ched 114 μA cm−2 (approxim` | non |
| PMC11266555 | `d 100–500 mg L–1, respecti` | non |
| PMC11266555 | `d 3400–3500 cm-1 correspon` | non |
| PMC11266555 | `e 1000–1200 cm−1 range cor` | non |
| PMC11266555 | `gion of 511 cm-1 of Ce-MOF` | oui |
| PMC11266555 | `ns of TC (mg L-1), respect` | non |
| PMC11266555 | `of 400–4000 cm-1. X-ray di` | non |
| PMC11266555 | `r are 100 ng L-1 to severa` | non |
| PMC11266555 | `t 1400–1540 cm-1 indicate ` | non |
| PMC11266555 | `t 1550–1600 cm-1. C=C stre` | non |
| PMC11266555 | `t 1600–1700 cm-1. The peak` | non |
| PMC11266555 | `te of 0.02°min-1 at 2θ = 1` | non |
| PMC11266555 | `to several g L-1 and 100–5` | non |
| PMC11269599 | ` After 15 × 10−3 g/mL conc` | oui |
| PMC11269599 | ` and Kobs (min−1) is the o` | non |
| PMC11269599 | ` from 1.6 × 10−2 M to 8.08` | oui |
| PMC11269599 | ` of (1.42 × 10−4 M) of AO7` | oui |
| PMC11269599 | ` up to 15 × 10–3 g/mL79–82` | oui |
| PMC11269599 | ` up to 15 × 10−3 g/mL subs` | oui |
| PMC11269599 | `, H2O2 (8 × 10−2 M) as wel` | oui |
| PMC11269599 | `/mL to 15 × 10−3 g/mL with` | oui |
| PMC11269599 | `0, and 1627 cm−1, respecti` | oui |
| PMC11269599 | `1 nm.IR (ν, cm−1): 3423 ν(` | oui |
| PMC11269599 | `1555 and 724cm−1 for C=C s` | non |
| PMC11269599 | `20 and 1661 cm−1, and the ` | non |
| PMC11269599 | `20,1661,717 cm−1 correspon` | non |
| PMC11269599 | `28 and 1169 cm−1 were attr` | non |
| PMC11269599 | `40 °C. (8 × 10−2M) H2O2 wa` | non |
| PMC11269599 | `438 to 1431 cm−1. indicate` | non |
| PMC11269599 | `5 g).IR (ν, cm−1): 3432 ν(` | oui |
| PMC11269599 | `59 and 1715 cm−1 was shift` | non |
| PMC11269599 | `651 to 1632 cm−1, and NH2 ` | non |
| PMC11269599 | `87 and 1074 cm−1, respecti` | non |
| PMC11269599 | `9 nm.IR (ν, cm−1): 3423 ν(` | oui |
| PMC11269599 | `99 and 1469 cm−1 were assi` | non |
| PMC11269599 | `AO7 (1.42 × 10−4 M) with H` | oui |
| PMC11269599 | `M to 2.85 × 10−4 M. (Fig. ` | non |
| PMC11269599 | `M to 8.08 × 10−2 M increas` | oui |
| PMC11269599 | `ak at ν 717 cm−1 confirmed` | non |
| PMC11269599 | `ak at ν 717 cm−1 which is ` | non |
| PMC11269599 | `ak at ν 808 cm−1 was refer` | non |
| PMC11269599 | `an49.IR (ν, cm−1): 3424 ν(` | oui |
| PMC11269599 | `and 12.94 × 10−2 M at 40 °` | non |
| PMC11269599 | `and at 3442 cm−1 for O–H g` | oui |
| PMC11269599 | `ation, 15 × 10−3 g/mL of c` | oui |
| PMC11269599 | `d at ν 1069 cm−1 correspon` | non |
| PMC11269599 | `d at ν 1656 cm−1 this evid` | non |
| PMC11269599 | `d at ν 3423 cm−1. Addition` | non |
| PMC11269599 | `d at ν 3424 cm−1, which is` | non |
| PMC11269599 | `d at ν 3486 cm−1 was sligh` | non |
| PMC11269599 | `d to ν 3432 cm−1, and the ` | non |
| PMC11269599 | `dosage, 8 × 10−2 M H2O2 co` | oui |
| PMC11269599 | `dye (1.42 × 10–4 M), H2O2 ` | non |
| PMC11269599 | `from 6.65 × 10−5 M to 2.85` | oui |
| PMC11269599 | `ge 400–4000 cm−1 utilizing` | non |
| PMC11269599 | `h H2O2 (8 × 10−2 M) in the` | oui |
| PMC11269599 | `hod51.IR(ν, cm−1): 3398 ν(` | oui |
| PMC11269599 | `k at ν 1001 cm−1 has appea` | non |
| PMC11269599 | `k at ν 3423 cm−1 became br` | non |
| PMC11269599 | `lows: (15 × 10−3 g/ml) of ` | oui |
| PMC11269599 | `od46.IR (ν, cm−1): 3422 ν(` | oui |
| PMC11269599 | `od47.IR (ν, cm−1): 3477 ν(` | oui |
| PMC11269599 | `on from 4 × 10−3 g/mL to 1` | non |
| PMC11269599 | `osite (15 × 10–3 g/mL) at ` | oui |
| PMC11269599 | `osite (15 × 10−3 g/mL) and` | oui |
| PMC11269599 | `ound ν 2958 cm−1 (methylen` | non |
| PMC11269599 | `ound ν 3424 cm−1 (hydroxyl` | non |
| PMC11269599 | `s at ν 1634 cm−1 and 1389 ` | non |
| PMC11269599 | `ted to 3420 cm−1. The new ` | non |
| PMC11269599 | `tial 1.42 × 10−4 M dye con` | oui |
| PMC11269599 | `tween 1.6 × 10−2 M and 12.` | oui |
| PMC11269599 | `−1 and 1389 cm−1 correspon` | non |
| PMC11280918 | ` cm−1, 1229 cm−1, 1423 cm−` |  |
| PMC11280918 | ` cm−1, 1423 cm−1, 1470 cm−` |  |
| PMC11280918 | ` cm−1, 1470 cm−1, 1573 cm−` |  |
| PMC11280918 | ` cm−1, 1573 cm−1, and 1669` |  |
| PMC11280918 | ` diluted to 10−12 M, almost` |  |
| PMC11280918 | ` reduced to 10−11 M, a weak` |  |
| PMC11280918 | `1, and 1669 cm−1 correspon` |  |
| PMC11280918 | `aks at 1029 cm−1, 1229 cm−` |  |
| PMC11280918 | `e as low as 10−11 M. This d` |  |
| PMC11280918 | `eak at 1573 cm−1 can be us` |  |
| PMC11280918 | `ng the 1573 cm−1 Raman pea` |  |
| PMC11280918 | `one down to 10−11 M, which ` |  |
| PMC11280918 | `red at 1573 cm−1 in the SE` |  |
| PMC11297172 | ` 0 and 4 kV mm−1 at room t` | oui |
| PMC11297172 | ` fields (kV mm−1) at low f` | non |
| PMC11297172 | ` up to 4 kV mm−1 through t` | non |
| PMC11297172 | `age (0–2 kV mm−1) to be ap` | non |
| PMC11297172 | `eld of 2 kV mm−1, BTS12 an` | non |
| PMC11297172 | `eld of 2 kV mm−1, respecti` | oui |
| PMC11297172 | `eld of 4 kV mm−1, respecti` | oui |
| PMC11297172 | `ing, a 2 kV mm−1 bias is c` | non |
| PMC11297172 | `m 0 to 2 kV mm−1 using an ` | non |
| PMC11297172 | `with a 4 kV mm−1 bias. Com` | non |
| PMC11329678 | ` was 0.026 min−1, whereas ` | oui |
| PMC11329678 | `27 and 1632 cm−1, indicati` | oui |
| PMC11329678 | `400 to 1000 cm−1, Fe3O4 ex` | non |
| PMC11329678 | `eak at 3437 cm−1, suggesti` | oui |
| PMC11329678 | `f 1376–1478 cm−1, Fe3O4 ex` | non |
| PMC11329678 | `from 0.026 min−1 to 0.1 mi` | oui |
| PMC11329678 | `ies.At 1000 cm−1, Ag/CuS/F` | oui |
| PMC11329678 | `n−1 to 0.1 min−1 for catal` | oui |
| PMC11329678 | `sed to 0.1 min−1.This resu` | non |
| PMC11329678 | `ved at 3165 cm−1, indicati` | non |
| PMC11345764 | ` at ∼22 mmol g–1 h–1, show` | oui |
| PMC11345764 | ` is 4.2 mmol g–1 h–1 at 40` | oui |
| PMC11345764 | `.28 mmol g–1 h–1, which is` | oui |
| PMC11345764 | `0 000 mL g–1 h–1. Given th` | non |
| PMC11345764 | `0.7 mmol g–1 h–1 (Figure 2` | oui |
| PMC11345764 | `1.1 mmol g–1 h–1) in perfo` | oui |
| PMC11345764 | `1.5 mmol g–1 h–1 at 400 °C` | oui |
| PMC11345764 | `1.5 mmol g–1 h–1). To high` | non |
| PMC11345764 | `143 and 251 cm–1 are attri` | oui |
| PMC11345764 | `2.4 mmol g–1 h–1 at 400 °C` | oui |
| PMC11345764 | `2C (1.5 mmol g–1 h–1). To ` | oui |
| PMC11345764 | `3.0 mmol g–1 h–1 at 475 °C` | oui |
| PMC11345764 | `3N (6.3 mmol g–1 h–1) and ` | oui |
| PMC11345764 | `4.2 mmol g–1 h–1 at 400 °C` | oui |
| PMC11345764 | `489 and 680 cm–1 are ascri` | oui |
| PMC11345764 | `5.5 mmol g–1 h–1 over Ni/L` | oui |
| PMC11345764 | `500 eV, 1 × 10–5 eV, and −` | non |
| PMC11345764 | `6 000 mL g–1 h–1, which is` | oui |
| PMC11345764 | `6.3 mmol g–1 h–1 at 400 °C` | oui |
| PMC11345764 | `6.3 mmol g–1 h–1) and nobl` | oui |
| PMC11345764 | `9 mmol gMo2CTx–1) is obvio` | oui |
| PMC11345764 | `O (11.1 mmol g–1 h–1) in p` | oui |
| PMC11345764 | `OH and 1 mol L–1 NH3·H2O, ` | oui |
| PMC11345764 | `d 2.6 Å, 9.5 Å–1, as displ` | non |
| PMC11345764 | `is 16.3 mmol g–1 h–1 at 40` | oui |
| PMC11345764 | `ly 0.28 mmol g–1 h–1, whic` | oui |
| PMC11345764 | `nd 0.33 mmol g–1 (Figure 4` | oui |
| PMC11345764 | `nd 21.5 mmol g–1 h–1 at 40` | oui |
| PMC11345764 | `nd 22.4 mmol g–1 h–1 at 40` | oui |
| PMC11345764 | `ning 0.2 mol L–1 NaOH and ` | oui |
| PMC11345764 | `o 57–74 kJ mol–1. Such low` | non |
| PMC11345764 | `o2C (96 kJ mol–1). After t` | non |
| PMC11345764 | `o2CTx (16 m2 g–1) and β-Mo` | oui |
| PMC11345764 | `of 15.5 mmol g–1 h–1 over ` | oui |
| PMC11345764 | `of 2π × 0.03 Å–1. The cuto` | non |
| PMC11345764 | `of 2π × 0.03 Å–1.The plane` | non |
| PMC11345764 | `of 33.0 mmol g–1 h–1 at 47` | oui |
| PMC11345764 | `of 36 000 mL g–1 h–1, whic` | oui |
| PMC11345764 | `of 60 000 mL g–1 h–1. Give` | oui |
| PMC11345764 | `sion of 1 × 10–5 eV. All o` | non |
| PMC11345764 | `t 1.5 Å, 5.1 Å–1 and 2.6 Å` | non |
| PMC11345764 | `te of 2 °C min–1 to 500 °C` | oui |
| PMC11345764 | `to 30.7 mmol g–1 h–1 (Figu` | oui |
| PMC11345764 | `x is 83 kJ mol–1 (Figure 2` | non |
| PMC11345764 | `β-Mo2C (7 m2 g–1) are diff` | oui |
| PMC11345764 | `∼22 mmol g–1 h–1, showing ` | oui |
| PMC11364895 | ` at 2137.68 cm−1, which fu` |  |
| PMC11382057 | ` and 1.04 × 10−3 S cm−1, r` | oui |
| PMC11382057 | ` are 1.91 × 10−4, 3.84 × 1` | oui |
| PMC11382057 | `04 × 10−3 S cm−1 at 25 °C)` | non |
| PMC11382057 | `04 × 10−3 S cm−1) and a lo` | non |
| PMC11382057 | `04 × 10−3 S cm−1, respecti` | non |
| PMC11382057 | `0−4, 3.84 × 10−4, and 1.04` | non |
| PMC11382057 | `13 × 10−4 S cm−1), and thu` | non |
| PMC11382057 | `LZO (∼5.1 g cm−3) []. Next` | oui |
| PMC11382057 | `Li (3860 mAh g−1) can be u` | non |
| PMC11382057 | `ductivity (>10−4 S cm−1 at` | non |
| PMC11382057 | `g at 0.4 mA cm−2, suggesti` | non |
| PMC11382057 | `ity (1.04 × 10−3 S cm−1 at` | oui |
| PMC11382057 | `ity (1.04 × 10−3 S cm−1) a` | oui |
| PMC11382057 | `only 1.13 × 10−4 S cm−1), ` | oui |
| PMC11382057 | `t at 0.4 mA cm−2 for 1 h p` | oui |
| PMC11382057 | `ty (>10−4 S cm−1 at room t` | non |
| PMC11382057 | `y of 0.4 mA cm−2. The Li/M` | non |
| PMC11382057 | `y of 0.4 mA cm−2. This stu` | non |
| PMC11382057 | `y of 0.4 mA cm−2; the corr` | non |
| PMC11393933 | `igh vacuum (10–6 Torr). No` |  |
| PMC11393933 | `m manifold (10–3 Torr). Th` |  |
| PMC11425712 | ` and 70 mA h g–1, respecti` | oui |
| PMC11425712 | ` of 132 mA h g–1 at 0.1 C,` | oui |
| PMC11425712 | ` of 167 mA h g–1), the pot` | non |
| PMC11425712 | ` to 132 mA h g–1, from 103` | non |
| PMC11425712 | `.0 ± 0.1 mg cm–2.Cyclic vo` | non |
| PMC11425712 | `00 and 1000 cm–1 in the FT` | oui |
| PMC11425712 | `1 C = 167 mA g–1). Current` | non |
| PMC11425712 | `CP (103 mA h g–1). This su` | non |
| PMC11425712 | `CP (123 mA h g–1) and bare` | oui |
| PMC11425712 | `and 123 mA h g–1 with citr` | non |
| PMC11425712 | `ate of 10° min–1.The speci` | non |
| PMC11425712 | `ate of 2 L min–1, as repor` | oui |
| PMC11425712 | `ing 141 mA h g–1 at 0.1 C,` | oui |
| PMC11425712 | `of ∼167 mA h g–1.5,6 Howev` | non |
| PMC11425712 | `out 100 mA h g–1, respecti` | oui |
| PMC11425712 | `rate of 5° min–1 ranging f` | non |
| PMC11425712 | `rom 103 mA h g–1 without a` | non |
| PMC11425712 | `te of 0.1 mV s–1, and elec` | non |
| PMC11425712 | `y of 75 mA h g–1 even at a` | oui |
| PMC11556383 | ` = 80.07 emu g−1) are achi` | non |
| PMC11556383 | `of 80.07 emu g−1, with uni` | non |
| PMC11556383 | `tion of 5 × 10−6, and a te` | oui |
| PMC11559627 | ` about 3 mA cm−2 was obser` |  |
| PMC11559627 | ` of 2.42 mA cm−2 and 22.87` |  |
| PMC11559627 | ` of 29.1 mA cm−2 at 50 mV ` |  |
| PMC11559627 | ` s−1, 100 mV s−1, 150 mV s` |  |
| PMC11559627 | ` s−1, 150 mV s−1, 200 mV s` |  |
| PMC11559627 | ` s−1, 200 mV s−1, 250 mV s` |  |
| PMC11559627 | ` s−1, 250 mV s−1 and 300 m` |  |
| PMC11559627 | `1 and 300 mV s−1. The resu` |  |
| PMC11559627 | `ate of 50 mV s−1. The resu` |  |
| PMC11559627 | `ately 33 mA cm−2 but after` |  |
| PMC11559627 | `m−2 at 50 mV s−1 was obtai` |  |
| PMC11559627 | `nd 22.87 mA cm−2 were obta` |  |
| PMC11559627 | `tes of 50 mV s−1, 100 mV s` |  |
| PMC11602897 | ` (at 1580 cd m−2), respect` | oui |
| PMC11602897 | ` and 6.94 × 10–6 (3-F-PEA ` | oui |
| PMC11602897 | ` and 9.35 × 10–6 (3-F-PEA ` | oui |
| PMC11602897 | ` are 4.08 × 10–7 (pristine` | oui |
| PMC11602897 | `% (at 875 cd m−2) and 21.9` | oui |
| PMC11602897 | `(DDAB (4 mg mL−1) and OAmB` | oui |
| PMC11602897 | `1.87 × 1018 cm−3 after the` | oui |
| PMC11602897 | `3.08 × 1018 cm−3, respecti` | oui |
| PMC11602897 | `Cs), 3.85 × 10–6 (PEA NCs)` | oui |
| PMC11602897 | `Cs), 7.21 × 10–6 (PEA NCs)` | oui |
| PMC11602897 | `NCs) cm2 V−1 s−1, and the ` | non |
| PMC11602897 | `NCs) cm2 V−1 s−1. These re` | non |
| PMC11602897 | `OAmBr (8 mg mL−1) dissolve` | oui |
| PMC11602897 | `PEA NCs) cm2 V−1 s−1, and ` | oui |
| PMC11602897 | `PEA NCs) cm2 V−1 s−1. Thes` | oui |
| PMC11602897 | `ding 1000 cd m−2. In this ` | non |
| PMC11602897 | `e of 1000 cd m−2, the life` | oui |
| PMC11602897 | `o be 6.54 × 10–7 (pristine` | oui |
| PMC11602897 | `ss than 4 × 10–4 Pa. The a` | oui |
| PMC11602897 | `y-TPD (8 mg mL−1 in chloro` | oui |
| PMC11635076 | ` cm−1, 3014 cm−1, and 2825` |  |
| PMC11635076 | ` is at 1843 cm–1. The spec` |  |
| PMC11635076 | `00 and 1400 cm−1 could be ` |  |
| PMC11635076 | `00 and 3300 cm–1. The N–H ` |  |
| PMC11635076 | `1, and 2825 cm−1 match the` |  |
| PMC11635076 | `1. The 1605 cm−1 and 1485 ` |  |
| PMC11635076 | `30 and 3440 cm–1 [].N2 ads` |  |
| PMC11635076 | `74 and 1546 cm–1. The C–N ` |  |
| PMC11635076 | `74, and 682 cm–1, which we` |  |
| PMC11635076 | `94 and 1140 cm–1, and the ` |  |
| PMC11635076 | `e 2900–3200 cm−1 range. Tr` |  |
| PMC11635076 | `ed of 1.0° min−1 in the 5–` |  |
| PMC11635076 | `hing at 806 cm−1. Bands at` |  |
| PMC11635076 | `nds at 3053 cm−1, 3014 cm−` |  |
| PMC11635076 | `on 900–1380 cm−1. The 1605` |  |
| PMC11635076 | `ons at 1628 cm−1 arise fro` |  |
| PMC11635076 | `red at 1420 cm−1 and bands` |  |
| PMC11635076 | `−1 and 1485 cm−1 bands are` |  |
| PMC11648698 | `n of 100 mg mL−1. Shown in` |  |
| PMC11678781 | ` A g−1–1.8 A g−1. The freq` | non |
| PMC11678781 | ` ASC at 10 A g−1. After 80` | non |
| PMC11678781 | ` cm−1, 1320 cm−1, and 1185` | non |
| PMC11678781 | ` cm−1, 1700 cm−1, 1320 cm−` | non |
| PMC11678781 | ` cm−1, 1773 cm−1, 1700 cm−` | non |
| PMC11678781 | ` of EIS was 10−2–105 Hz wi` | oui |
| PMC11678781 | `1, and 1185 cm−1 correspon` | non |
| PMC11678781 | `F g−1 at 1 A g−1 and a cap` | non |
| PMC11678781 | `aks at 1367 cm−1 and 1578 ` | oui |
| PMC11678781 | `aks at 3093 cm−1 and 1400 ` | non |
| PMC11678781 | `aks at 3430 cm−1, 1773 cm−` | non |
| PMC11678781 | `ce was 150 F g−1 and the v` | oui |
| PMC11678781 | `e is 65.41 F g−1, and it m` | oui |
| PMC11678781 | `eak at 1367 cm−1 is relate` | non |
| PMC11678781 | `eak at 1578 cm−1 is relate` | non |
| PMC11678781 | `eak at 1650 cm−1 correspon` | oui |
| PMC11678781 | `eed is 50 mv s−1, the cont` | oui |
| PMC11678781 | `eed of 10 mv s−1–100 mv s−` | oui |
| PMC11678781 | `f 1000–2000 cm−1. Fourier-` | non |
| PMC11678781 | `nce of 102 F g−1 at 1 A g−` | oui |
| PMC11678781 | `nce of 102 F g−1 at a curr` | oui |
| PMC11678781 | `nsity is 1 A g−1, the spec` | oui |
| PMC11678781 | `nsity of 1 A g−1. The asse` | non |
| PMC11678781 | `ntials, v (V s−1) is the s` | non |
| PMC11678781 | `s set to 1 A g−1–1.8 A g−1` | oui |
| PMC11678781 | `s-2 is 102 F g−1 and it ha` | non |
| PMC11678781 | `tely 0.2 mg mL−1. The colo` | non |
| PMC11678781 | `v s−1–100 mv s−1. The curr` | non |
| PMC11678781 | `−1 and 1400 cm−1 correspon` | non |
| PMC11678781 | `−1 and 1578 cm−1, respecti` | oui |
| PMC11739850 | ` and 1408 m2 g−1, respecti` |  |
| PMC11739850 | `and 0.82 cm3 g−1. The pore` |  |
| PMC11739850 | `ately 60 mA cm−2 is obtain` |  |
| PMC11739850 | `bout 1.6 mg cm−2.Physicoch` |  |
| PMC11739850 | `d a 1.0 mL min−1 flow rate` |  |
| PMC11739850 | `e was 4 mL min−1.Electroch` |  |
| PMC11739850 | `ing (1.6 mg cm−2), and the` |  |
| PMC11739850 | `ing (1.6 mg cm−2). The ano` |  |
| PMC11739850 | `of 0.55 mmol g−1 for the s` |  |
| PMC11739850 | `stant 9 mL min−1 flow. A c` |  |
| PMC11739850 | `te of 5 °C min−1. The spec` |  |
| PMC11739850 | `to 0.88 mmol g−1 of CO2, w` |  |
| PMC11739850 | `ts at 4 mL min−1 during th` |  |
| PMC11739850 | `w of 25 mL min−1 was injec` |  |
| PMC11739850 | `y of −60 mA cm−2.Gas‐phase` |  |
| PMC11752507 | `kBT = 4.1 × 10–21 J at T = ` | non |
| PMC11752637 | ` The “K2 (g mg−1 min−1)” w` | non |
| PMC11752637 | ` cm−1, 2950 cm−1, and 2870` | oui |
| PMC11752637 | ` of 0.2 mL min−1. The mobi` | oui |
| PMC11752637 | `, and Ki (mg g−1 min−1) fo` | non |
| PMC11752637 | `, and qt (mg g−1) is the a` | non |
| PMC11752637 | `0, 15, 20 mg L−1) of funct` | oui |
| PMC11752637 | `1, and 2870 cm−1 represent` | oui |
| PMC11752637 | `K2 (g mg−1 min−1) is the c` | non |
| PMC11752637 | `K2 (g mg−1 min−1)” was det` | non |
| PMC11752637 | `Ki (mg g−1 min−1) for the ` | non |
| PMC11752637 | `adsorbed (mg g−1) at a spe` | non |
| PMC11752637 | `adsorbed (mg g−1) at equil` | non |
| PMC11752637 | `aks at 3410 cm−1 and 1060 ` | oui |
| PMC11752637 | `and 1.74 cm3 g−1, respecti` | oui |
| PMC11752637 | `cept, Kp (mg g−1 min0.5) r` | non |
| PMC11752637 | `e are 143 m2 g−1 and 1.74 ` | oui |
| PMC11752637 | `eak at 3470 cm−1 represent` | oui |
| PMC11752637 | `es of qe (mg g−1), R2, K1,` | non |
| PMC11752637 | `ion (0.5 mg mL−1) was pass` | oui |
| PMC11752637 | `ion (Ct, mg mL−1) in the s` | oui |
| PMC11752637 | `ion of k1 (min−1). The com` | non |
| PMC11752637 | `is 435.45 mg g−1, and the ` | non |
| PMC11752637 | `ities (q, mg g−1) of MA on` | non |
| PMC11752637 | `nds at 1690 cm−1 and 1440 ` | oui |
| PMC11752637 | `nds at 1710 cm−1 and 1440 ` | oui |
| PMC11752637 | `nds at 3310 cm−1, 2950 cm−` | oui |
| PMC11752637 | `ons (0.5 mg mL−1) in conic` | oui |
| PMC11752637 | `ose at 10 mg L−1. The resu` | non |
| PMC11752637 | `pg L−1 to ng L−1).4 Indust` | non |
| PMC11752637 | `r (435.45 mg g−1) owing to` | non |
| PMC11752637 | `rate of 3 BV h−1. To const` | oui |
| PMC11752637 | `t dose 10 mg L−1. It was n` | non |
| PMC11752637 | `te of 0.5 BV h−1 was calcu` | non |
| PMC11752637 | `te of 0.5 BV h−1. The elut` | non |
| PMC11752637 | `trations (pg L−1 to ng L−1` | non |
| PMC11752637 | `where K2 (g mg−1 min−1) is` | non |
| PMC11752637 | `−1 and 1060 cm−1, which co` | oui |
| PMC11752637 | `−1 and 1440 cm−1 represent` | oui |
| PMC11752637 | `−1 and 1440 cm−1 represent` | oui |
| PMC11818718 | ` and 0.1 mg ml−1 streptomy` |  |
| PMC11818718 | ` and 0.1 μg ml−1) of each ` |  |
| PMC11818718 | ` and 0.1 μg ml−1. Prelimin` |  |
| PMC11818718 | ` of 4.12 μg ml−1. Cytotoxi` |  |
| PMC11818718 | ` of 8.46 μg ml−1, compared` |  |
| PMC11818718 | ` salt (5 mg ml−1; Sigma). ` |  |
| PMC11818718 | `doses in μg mL−1 that resu` |  |
| PMC11818718 | `ure (100 IU ml−1 penicilli` |  |
| PMC11840780 | ` at 0.75 mg/mL–1 (Figure 1` | non |
| PMC11840780 | ` be 0.26 mg/mL–1 and the E` | oui |
| PMC11840780 | ` of 0.75 mg/mL–1 CDs, the ` | non |
| PMC11840780 | `.2 × 104 L mol–1 from the ` | oui |
| PMC11840780 | `.4 × 104 L mol–1) was dete` | oui |
| PMC11840780 | `0.1 to 1 mg/mL–1, the abso` | non |
| PMC11840780 | `03 ± 7.78 × 10–4) and y = ` | oui |
| PMC11840780 | `080 and 685 cm–1 were ascr` | non |
| PMC11840780 | `1 × 1012 L mol–1 s–1. This` | oui |
| PMC11840780 | `1010 L mol–1 s–1). Therefo` | non |
| PMC11840780 | `1010 L mol–1 s–1. Therefor` | non |
| PMC11840780 | `1012 L mol–1 s–1. This cal` | non |
| PMC11840780 | `1012 L mol–1 s–1. This obs` | non |
| PMC11840780 | `15 ± 5.08 × 10–5) × x + (1` | oui |
| PMC11840780 | `2 × 1010 L mol–1 s–1). The` | oui |
| PMC11840780 | `2 × 1010 L mol–1 s–1. Ther` | oui |
| PMC11840780 | `21 ± 4.97 × 10–4) × x + (0` | oui |
| PMC11840780 | `26 ± 1.82 × 10–4) × x + (1` | oui |
| PMC11840780 | `4, and 1413 cm–1 suggested` | oui |
| PMC11840780 | `6 × 1012 L mol–1 s–1. This` | oui |
| PMC11840780 | `62 ± 5.88 × 10–4) × x + (1` | oui |
| PMC11840780 | `93 ± 1.72 × 10–4) and y = ` | oui |
| PMC11840780 | `S-CDs (2 μg mL–1). After 1` | non |
| PMC11840780 | `as 0.002 mg/mL–1.Conclusio` | non |
| PMC11840780 | `t 2900–3250 cm–1 correspon` | non |
| PMC11883551 | ` 161.8486 m2 g−1 and 0.146` | oui |
| PMC11883551 | ` = −394 kJ mol−1 and a sta` | non |
| PMC11883551 | ` = −395 kJ mol−1) percenta` | non |
| PMC11883551 | `0.146227 cm3 g−1, respecti` | oui |
| PMC11883551 | `35 and 1074 cm−1 can be at` | oui |
| PMC11883551 | `f 1596–1643 cm−1 for adeni` | oui |
| PMC11883551 | `hing (3.9 × 10−4 mmol) at ` | oui |
| PMC11883551 | `is 15.1 kJ mol−1) (Fig. 2)` | non |
| PMC11883551 | `n 3201–3465 cm−1 are attri` | oui |
| PMC11883551 | `peak at 658 cm−1.38,39 The` | non |
| PMC11883551 | `te of 5 °C min−1 under an ` | non |
| PMC11891312 | `500 and 800 cm−1 and a wea` | oui |
| PMC11891312 | `and at 3382 cm−1 correspon` | non |
| PMC11891312 | `der at 1220 cm−123. These ` | non |
| PMC11891312 | `imately 810 cm−1 and 1100 ` | oui |
| PMC11891312 | `k at ~ 1633 cm−1 was assig` | non |
| PMC11891312 | `−1 and 1100 cm−1, along wi` | oui |
| PMC11904774 | ` V at 0.02 V s−1. The phot` | non |
| PMC11904774 | ` of 100 mL min−1 at a heat` | non |
| PMC11904774 | ` to 6.41 mA cm−2 under ill` | non |
| PMC11904774 | ` to 7.05 mA cm−2, and the ` | non |
| PMC11904774 | `4000 to 400 cm−1. The phas` | non |
| PMC11904774 | `520, 100 mW cm−2). Linear ` | oui |
| PMC11904774 | `ak at ∼2932 cm−1 is attrib` | non |
| PMC11904774 | `aks at 1736 cm−1 and 1610 ` | non |
| PMC11904774 | `ately ∼3400 cm−1 correspon` | non |
| PMC11904774 | `ction, 1 L min−1 N2 was pu` | oui |
| PMC11904774 | `density (mA cm−2), I is th` | non |
| PMC11904774 | `density (mA cm−2), Voc is ` | non |
| PMC11904774 | `e of 10 °C min−1. This ana` | non |
| PMC11904774 | `eak at 1624 cm−1 suggests ` | non |
| PMC11904774 | `etween 1300 cm−1 and 1000 ` | non |
| PMC11904774 | `f 2600–3000 cm−1 correspon` | oui |
| PMC11904774 | `he DSSC (mW cm−2), V is th` | non |
| PMC11904774 | `round ∼1040 cm−1, which is` | non |
| PMC11904774 | `tensity (mW cm−2), Jsc is ` | non |
| PMC11904774 | `tensity (mW cm−2). Finally` | non |
| PMC11904774 | `ution of 16 cm−1, within a` | non |
| PMC11904774 | `−1 and 1000 cm−1 are linke` | non |
| PMC11904774 | `−1 and 1610 cm−1 are attri` | non |
| PMC11931415 | ` 731–1077 mg g−1, which wa` | non |
| PMC11931415 | ` 731–1077 mg g−1, which wa` | non |
| PMC11931415 | ` cm−1, 1478 cm−1, and 1529` | non |
| PMC11931415 | ` was 1276 m2 g−1, which wa` | oui |
| PMC11931415 | ` was 1375 m2 g−1, which wa` | non |
| PMC11931415 | ` was 20 ml min−1, the heat` | non |
| PMC11931415 | `) was 410 mg g−1.33 The wa` | non |
| PMC11931415 | `1, and 1529 cm−1 correspon` | non |
| PMC11931415 | `5 and 596 m2 g−1.The morph` | non |
| PMC11931415 | `7.2–300.6 mg g−1, among wh` | non |
| PMC11931415 | `aks at 1001 cm−1, 1478 cm−` | non |
| PMC11931415 | `aks at 1386 cm−1 and 1604 ` | oui |
| PMC11931415 | `and 207.0 mg g−1, respecti` | non |
| PMC11931415 | `e 272–606 mg g−1.34 While ` | non |
| PMC11931415 | `e 360–640 mg g−1,31 MIL-12` | non |
| PMC11931415 | `e 420–590 mg g−1,31,32 and` | non |
| PMC11931415 | `e 568–683 m2 g−1, which wa` | oui |
| PMC11931415 | `e 600–680 mg g−1.35,36 The` | non |
| PMC11931415 | `e of 20 ml min−1 under the` | oui |
| PMC11931415 | `e was 10 K min−1, and the ` | non |
| PMC11931415 | `ere 248.6 mg g−1, 151.2 mg` | non |
| PMC11931415 | `f 232–269 mg g−1. The adso` | oui |
| PMC11931415 | `he 400–4000 cm−1 range in ` | non |
| PMC11931415 | `hest, 269 mg g−1. The adso` | oui |
| PMC11931415 | `ity (1077 mg g−1).The CaCl` | non |
| PMC11931415 | `r was 295 mg g−1. The wate` | non |
| PMC11931415 | `s was 416 mg g−1, which re` | oui |
| PMC11931415 | `s was 445 mg g−1, and the ` | non |
| PMC11931415 | `te of 10 K min−1 and a flo` | oui |
| PMC11931415 | `ty (300.6 mg g−1) and the ` | non |
| PMC11931415 | `−1 and 1604 cm−1 were attr` | oui |
| PMC11931415 | `−1, 151.2 mg g−1 and 207.0` | non |
| PMC11935935 | ` 124 mAh gCAM −1 (≈62% of ` |  |
| PMC11935935 | ` 124 mAh gCAM −1 after 30 ` |  |
| PMC11935935 | ` 124 mAh gCAM −1 at ≈0.2 a` |  |
| PMC11935935 | ` 164 mAh gCAM −1) and show` |  |
| PMC11935935 | ` 199 mAh gCAM −1 for Z400,` |  |
| PMC11935935 | ` 274 mAh gCAM −1) on eithe` |  |
| PMC11935935 | ` ion ≈ 2 mS cm−1 at room t` |  |
| PMC11935935 | ` × 10−16 cm2 s−1 from the ` |  |
| PMC11935935 | `, ρ = 6.1 g cm−3, should b` |  |
| PMC11935935 | `.71 m2 gNCM85 −1, and the ` |  |
| PMC11935935 | `2 and ≈2 mA cm−2, respecti` |  |
| PMC11935935 | `2 and ≈2 mA cm−2, respecti` |  |
| PMC11935935 | `6–35 mAh gCAM −1 in the 50` |  |
| PMC11935935 | `= 190 mA gCAM −1), with tw` |  |
| PMC11935935 | `e (≈2.9 mAh cm−2 for q th ` |  |
| PMC11935935 | `es at ≈1 mA cm−2 were achi` |  |
| PMC11935935 | `et to 5 °C min−1). For the` |  |
| PMC11935935 | `f 1012 ions cm−2 was reach` |  |
| PMC11935935 | `ing at 15 N mm−1. The cath` |  |
| PMC11935935 | `o 78 mAh gCAM −1 (≈43%) fo` |  |
| PMC11935935 | `of ≈8 mgCAM cm−2 were punc` |  |
| PMC11935935 | `t D ≈ 3.8 × 10−16 cm2 s−1 f` |  |
| PMC11935935 | `t to 10 °C min−1).Elementa` |  |
| PMC11935935 | `to ≈2.1 mAh cm−2. The reas` |  |
| PMC11935935 | `y 18 mAh gCAM −1 (≈11%) fo` |  |
| PMC11944978 | `aks at 1640 cm−1 and 1083 ` | non |
| PMC11944978 | `around 2921 cm−1 and 2853 ` | oui |
| PMC11944978 | `eak at 3446 cm−1 correspon` | oui |
| PMC11944978 | `nd) at 1371 cm−1 and the s` | oui |
| PMC11944978 | `nd) at 1557 cm−1, which we` | oui |
| PMC11944978 | `re (18.2 MΩ·cm−1, Mili-Q, ` | oui |
| PMC11944978 | `−1 and 1083 cm−1 suggested` | non |
| PMC11944978 | `−1 and 2853 cm−1 correspon` | oui |
| PMC11967815 | ` 50 µg ×100 mL−1 (2.4 µm) ` |  |
| PMC11989644 | ` N2 (50 mL min−1) at a hea` | non |
| PMC11989644 | ` and 3.0 mol L−1), liquid/` | oui |
| PMC11989644 | ` around 650 cm−1 to 500 cm` | non |
| PMC11989644 | `(1608.34 m2 cm−3), and an ` | non |
| PMC11989644 | `(for 3.0 mol L−1 and 20 mL` | non |
| PMC11989644 | `2–3 mol NaOH L−1. If the f` | non |
| PMC11989644 | `400 to 4000 cm−1, accumula` | non |
| PMC11989644 | `ange between λ−1 = 400 to ` | non |
| PMC11989644 | `at ca. 1462 cm−1 can be at` | non |
| PMC11989644 | `at ca. 1462 cm−1 for carbo` | oui |
| PMC11989644 | `band at 462 cm−1 is relati` | non |
| PMC11989644 | `between 800 cm−1 to 400 cm` | oui |
| PMC11989644 | `cm−1 to 400 cm−1 contains ` | non |
| PMC11989644 | `cm−1 to 400 cm−1.The therm` | non |
| PMC11989644 | `cm−1 to 500 cm−1 is relate` | non |
| PMC11989644 | `e of 10 °C min−1 from room` | non |
| PMC11989644 | `etween 1210 cm−1 and 1084 ` | oui |
| PMC11989644 | `etween 1300 cm−1 to 400 cm` | non |
| PMC11989644 | `io (20 mL (2g)−1) for the ` | non |
| PMC11989644 | `m−1 and 678 cm−1, respecti` | oui |
| PMC11989644 | `nds at 3479 cm−1 and 1642 ` | non |
| PMC11989644 | `odes at 983 cm−1 and 678 c` | oui |
| PMC11989644 | `peak at 565 cm−1 is assign` | non |
| PMC11989644 | `rum at 1047 cm−1 (νasy) an` | non |
| PMC11989644 | `scans and 4 cm−1 of resolu` | non |
| PMC11989644 | `sy) and 755 cm−1 (νsy). Th` | non |
| PMC11989644 | `ution (2 mol L−1), stirrin` | oui |
| PMC11989644 | `with 3.0 mol L−1 and 240 m` | non |
| PMC11989644 | `−1 and 1084 cm−1 can be ch` | oui |
| PMC11989644 | `−1 and 1642 cm−1 are chara` | non |
| PMC11990281 | `00, and 450 cm−1. The band` | non |
| PMC11990281 | `450 and 800 cm−1 are attri` | non |
| PMC11990281 | `80 and 3650 cm−1 are attri` | non |
| PMC11990281 | `d is at 960 cm−1, which is` | oui |
| PMC11990281 | `f 1000–1300 cm−1 is attrib` | non |
| PMC11990281 | `in the 1640 cm−1 and 1400 ` | non |
| PMC11990281 | `−1 and 1400 cm−1 range are` | non |
| PMC12002332 | ` cm−1, 1636 cm−1, 1508, 14` |  |
| PMC12002332 | ` cm−1, 2940 cm−1, 1600–170` |  |
| PMC12002332 | `, 1350–1450 cm−1, and 1000` |  |
| PMC12002332 | `, 1600–1700 cm−1, 1350–145` |  |
| PMC12002332 | `.15±0.03 μg.mL−1. Metallic` |  |
| PMC12002332 | `0, and 1992 cm−1, indicati` |  |
| PMC12002332 | `108 to 1990 cm−1, 1636 cm−` |  |
| PMC12002332 | `3, and 3735 cm−1, correspo` |  |
| PMC12002332 | `419 to 1339 cm−1 (Figure 5` |  |
| PMC12002332 | `57 and 1419 cm−1. The peak` |  |
| PMC12002332 | `58 and 1508 cm−1 indicate ` |  |
| PMC12002332 | `8 ± 0.07 µg.mL−1 showed (F` |  |
| PMC12002332 | `802 to 3339 cm−1, 2322, 22` |  |
| PMC12002332 | `and 12.5 μg.mL−1, on the c` |  |
| PMC12002332 | `between 800 cm−1 and 4000 ` |  |
| PMC12002332 | `d 1000–1100 cm−1 are assoc` |  |
| PMC12002332 | `eak at 1270 cm−1 correspon` |  |
| PMC12002332 | `eak at 1362 cm−1 suggests ` |  |
| PMC12002332 | `eak at 1636 cm−1 can be at` |  |
| PMC12002332 | `t 3300–3900 cm−1, 2940 cm−` |  |
| PMC12002332 | `ved at 3317 cm−1, which ca` |  |
| PMC12002332 | `−1 and 4000 cm−1.The Evalu` |  |
| PMC12043898 | ` and 100 mA cm−2, respecti` |  |
| PMC12043898 | ` and 200 mA cm−2) were bot` |  |
| PMC12043898 | ` at 600-700 cm−1 in the Ra` |  |
| PMC12043898 | ` of 100 mL min−1 through a` |  |
| PMC12043898 | ` of 13.5 mol g−1 h−1. It i` |  |
| PMC12043898 | ` of −0.1 mA cm−2) in 0.1 M` |  |
| PMC12043898 | ` to 13.5 mol g−1 h−1 in a ` |  |
| PMC12043898 | `0 or 100 mA cm−2 current d` |  |
| PMC12043898 | `1 and ~1480 cm−1 can be as` |  |
| PMC12043898 | `13.5 mol g−1 h−1 in a neut` |  |
| PMC12043898 | `13.5 mol g−1 h−1), and lon` |  |
| PMC12043898 | `13.5 mol g−1 h−1. It is wo` |  |
| PMC12043898 | `23.4 mol g–1 h–1 at –0.6 V` |  |
| PMC12043898 | `27.0 mol g−1 h−1 in an alk` |  |
| PMC12043898 | `27.0 mol g−1 h−1, neutral:` |  |
| PMC12043898 | `aks at 3240 cm−1 could be ` |  |
| PMC12043898 | `al:>13.5 mol g−1 h−1), and` |  |
| PMC12043898 | `and 23.4 mol g–1 h–1 at –0` |  |
| PMC12043898 | `around 2900 cm−1), indicat` |  |
| PMC12043898 | `around 3300 cm−1 could be ` |  |
| PMC12043898 | `ate of 10 mV s−1 and a rot` |  |
| PMC12043898 | `be 79.9 mV dec−1, which is` |  |
| PMC12043898 | `d at 100 mA cm-2 in the fl` |  |
| PMC12043898 | `ding ~80 μg cm-2. LSV curv` |  |
| PMC12043898 | `e at 100 mA cm−2 could be ` |  |
| PMC12043898 | `ed over 11 g L−1 before th` |  |
| PMC12043898 | `g of 0.1 mg cm–2. Either t` |  |
| PMC12043898 | `h 34 mol g–1 h–1 at –0.4 V` |  |
| PMC12043898 | `ing at 3300 cm−1 for Ni-BT` |  |
| PMC12043898 | `is at 50 mA cm−2 in the 0.` |  |
| PMC12043898 | `ks at ~1210 cm−1 and ~1480` |  |
| PMC12043898 | `ks at ~1340 cm−1 should be` |  |
| PMC12043898 | `ne:>27.0 mol g−1 h−1, neut` |  |
| PMC12043898 | `ns (108 CFU mL–1) to obtai` |  |
| PMC12043898 | `of the 5 mg mL–1 catalyst ` |  |
| PMC12043898 | `on (107 CFU mL–1), then th` |  |
| PMC12043898 | `on of 26.8 g L−1 with a hi` |  |
| PMC12043898 | `over 200 mA cm–2, either i` |  |
| PMC12043898 | `r energy is 10-6 eV.The 2e` |  |
| PMC12043898 | `reach 34 mol g–1 h–1 at –0` |  |
| PMC12043898 | `reached 1.56 s−1 and 2.27 ` |  |
| PMC12043898 | `s−1 and 2.27 s−1 in 1 M Na` |  |
| PMC12043898 | `t 1500-1700 cm−1 in the FT` |  |
| PMC12043898 | `t 3300-3500 cm−1 associate` |  |
| PMC12043898 | `tants (~30 g L−1). In addi` |  |
| PMC12043898 | `te of 1.0 mV s–1 in the H2` |  |
| PMC12043898 | `te of 100 mV s-1 for 5-cyc` |  |
| PMC12043898 | `te of 6 mL min-1, using pu` |  |
| PMC12043898 | `ty of 50 mA cm–2 in the fl` |  |
| PMC12043898 | `ver 27.0 mol g−1 h−1 in an` |  |
| PMC12043898 | `y of 100 mA cm−2 and in a ` |  |
| PMC12043898 | `y of 100 mA cm−2 for 24 h ` |  |
| PMC12043898 | `y of 200 mA cm−2 in 30 mL ` |  |
| PMC12043898 | `yes is 60 mg L–1) is adopt` |  |
| PMC12079599 | `0.5, and 1 A g–1, respecti` | oui |
| PMC12079599 | `0.5, and 1 A g–1, respecti` | oui |
| PMC12079599 | `as 933.9 mAh g–1. The acti` | non |
| PMC12079599 | `d 422.46 mAh g–1, respecti` | oui |
| PMC12079599 | `d 747.98 mAh g–1, respecti` | oui |
| PMC12079599 | `ea (32.17 m2 g–1) than tha` | non |
| PMC12079599 | `f 411.60 mAh g–1 over 200 ` | oui |
| PMC12079599 | `is 588.5 mAh g–1, with a c` | oui |
| PMC12079599 | `ity (670 mAh g–1), large s` | non |
| PMC12079599 | `nd 180.6 mAh g–1 at curren` | oui |
| PMC12079599 | `nd 370.6 mAh g–1 at curren` | oui |
| PMC12079599 | `nd 762.1 mAh g–1, respecti` | oui |
| PMC12079599 | `nsity of 1 A g–1.Doping ce` | non |
| PMC12079599 | `of 450.8 mAh g–1 after 500` | non |
| PMC12079599 | `red to 0.1 A g–1, the spec` | oui |
| PMC12079599 | `rns to 0.1 A g–1, the reve` | oui |
| PMC12079599 | `rns to 0.1 A g–1. The spec` | non |
| PMC12079599 | `rt (29.80 m2 g–1). However` | non |
| PMC12079599 | `s 1373.4 mAh g–1 at a curr` | oui |
| PMC12079599 | `s 747.98 mAh g–1, while th` | oui |
| PMC12079599 | `to 422.1 mAh g–1, indicati` | oui |
| PMC12079599 | `ty of 500 mA g–1 are 673.1` | oui |
| PMC12079599 | `ty of 500 mA g–1 was 747.9` | non |
| PMC12079599 | `ty of 500 mA g–1. The spec` | non |
| PMC12093138 | ` as 39.10 mg g−1, 42.10 mg` | oui |
| PMC12093138 | ` as 48.78 mg g−1. Moreover` | non |
| PMC12093138 | ` as 49.60 mg g−1 within 60` | non |
| PMC12093138 | ` to 40.60 mg g−1, 44.70 mg` | oui |
| PMC12093138 | ` to 49.60 mg g−1. Under vi` | non |
| PMC12093138 | `ak near 800 cm−1 correspon` | oui |
| PMC12093138 | `and 43.60 mg g−1, respecti` | oui |
| PMC12093138 | `and 49.60 mg g−1, respecti` | oui |
| PMC12093138 | `around 1600 cm−1 is the ba` | oui |
| PMC12093138 | `f 1200–1700 cm−1 are due t` | oui |
| PMC12093138 | `k near 1600 cm−1 is caused` | oui |
| PMC12093138 | `k near 1750 cm−1 is the C ` | non |
| PMC12093138 | `k near 3400 cm−1 is the O–` | non |
| PMC12093138 | `nsion (1 mg mL−1) through ` | oui |
| PMC12093138 | `nsion (1 mg mL−1). Similar` | non |
| PMC12093138 | `peak of 806 cm−1 is relate` | oui |
| PMC12093138 | `rom 43.60 mg g−1 to 49.60 ` | non |
| PMC12093138 | `s near 1350 cm−1 and 1600 ` | non |
| PMC12093138 | `t 3000–3500 cm−1 should be` | oui |
| PMC12093138 | `te of 5 °C min−1, keeping ` | oui |
| PMC12093138 | `ution (50 mg L−1) in the d` | oui |
| PMC12093138 | `ution (50 mg L−1) under si` | non |
| PMC12093138 | `ve MB (50 mg L−1) from wat` | non |
| PMC12093138 | `−1 and 1600 cm−1 correspon` | non |
| PMC12093138 | `−1, 42.10 mg g−1, and 43.6` | oui |
| PMC12093138 | `−1, 44.70 mg g−1, and 49.6` | oui |
| PMC12191741 | `y (8.8542 × 10−12 F/m). The` | non |
| PMC12195685 | ` ca. 0.9 mol·L–1 of IP was` | oui |
| PMC12195685 | ` ca. 14 μmol·L–1 of BQ was` | oui |
| PMC12195685 | `1 and 2.7 × 10−3 min−1, re` | non |
| PMC12195685 | `1 and 7.4 × 10−3 min−1 for` | non |
| PMC12195685 | `1.6 × 10−3 min−1 and a con` | non |
| PMC12195685 | `2.7 × 10−3 min−1, respecti` | non |
| PMC12195685 | `3.4 × 10−3 min−1, and a ca` | non |
| PMC12195685 | `4.3 × 10−3 min−1 and 2.7 ×` | non |
| PMC12195685 | `46 and 1596 cm−1 for the M` | oui |
| PMC12195685 | `46 and 1596 cm−1 in the sa` | oui |
| PMC12195685 | `7.4 × 10−3 min−1 for Fe/MC` | non |
| PMC12195685 | `7.5 × 10−3 min−1 and 7.4 ×` | non |
| PMC12195685 | `a. 0.444 (μA·V−1) for the ` | oui |
| PMC12195685 | `a. 11.5 μmol·L−1, 2.875 μm` | non |
| PMC12195685 | `and at 1490 cm−1, which is` | oui |
| PMC12195685 | `and at 3740 cm−1, correspo` | oui |
| PMC12195685 | `ants (k2, μmol−1.min−1) fo` | non |
| PMC12195685 | `at ca. 1580 cm−1, which ca` | non |
| PMC12195685 | `ate of 50 mV·s−1.The surfa` | non |
| PMC12195685 | `d 1445–1455 cm−1. Therefor` | non |
| PMC12195685 | `es at ~1540 cm−1 and 1636 ` | non |
| PMC12195685 | `f ca. 1.6 × 10−3 min−1 and` | non |
| PMC12195685 | `f ca. 3.4 × 10−3 min−1, an` | non |
| PMC12195685 | `f ca. 4.3 × 10−3 min−1 and` | non |
| PMC12195685 | `f ca. 5.5 mg·L−1 (ca. 11.5` | non |
| PMC12195685 | `f ca. 7.5 × 10−3 min−1 and` | non |
| PMC12195685 | `itting 250 W·m−2 at 360 nm` | non |
| PMC12195685 | `k2, μmol−1.min−1) for the ` | non |
| PMC12195685 | `lied (0.05 V·s−1). Compare` | non |
| PMC12195685 | `lower (0.1 g·L−1) compared` | non |
| PMC12195685 | `nts (kapp, min−1) obtained` | non |
| PMC12195685 | `of 400–4000 cm−1. Supporte` | non |
| PMC12195685 | `of ca. 0.1 g·L−1. The RhB ` | non |
| PMC12195685 | `order (k1, min−1) and the ` | non |
| PMC12195685 | `ram area (μA·V−1) and the ` | non |
| PMC12195685 | `ram area (μA·V−1) by the s` | non |
| PMC12195685 | `s less than 10−3 Pa. The b` | non |
| PMC12195685 | `te of 0.05 V·s−1. For the ` | non |
| PMC12195685 | `te of 0.6°·min−1. Inductiv` | non |
| PMC12195685 | `tion (5.5 mg·L−1) for iden` | oui |
| PMC12195685 | `to ca. 0.7 g·L−1, which is` | non |
| PMC12195685 | `vsur, μmol.min−1) was esti` | non |
| PMC12195685 | `−1 and 1636 cm−1 have not ` | non |
| PMC12199321 | ` 10−13, and 10−11 M for MeB` | non |
| PMC12199321 | ` 10−13, and 10−11 M, as wel` | oui |
| PMC12199321 | ` 10−13, and 10−11 M, respec` | oui |
| PMC12199321 | ` and 10.18 m2g−1, respecti` | oui |
| PMC12199321 | ` low LOD of 10−13 M for Rho` | oui |
| PMC12199321 | ` low as 5 × 10−16 M after t` | non |
| PMC12199321 | ` molecules (10−6 M) is fol` | oui |
| PMC12199321 | ` of 10−6 to 10−12 M and 10−` | oui |
| PMC12199321 | ` respect to 10−7 M MeB mol` | oui |
| PMC12199321 | ` spectra of 10−7 M MeB on ` | oui |
| PMC12199321 | ` spectra of 10−7 M MeB, MV` | oui |
| PMC12199321 | `10−12 M and 10−6 to 10−11 ` | oui |
| PMC12199321 | `In terms of 10−7 M MV, R6G` | oui |
| PMC12199321 | `and 10−6 to 10−11 M with th` | oui |
| PMC12199321 | `ated at 312 cm−1, while th` | oui |
| PMC12199321 | `e as low as 10−12, 10−13, a` | oui |
| PMC12199321 | `eak at 1620 cm−1 was selec` | non |
| PMC12199321 | `fts of 1617 cm−1 is 4.3 × ` | oui |
| PMC12199321 | `fts of 1617 cm−1 is as low` | oui |
| PMC12199321 | `he range of 10−6 to 10−12 ` | oui |
| PMC12199321 | `hift to 315 cm−1, which de` | non |
| PMC12199321 | `ion of 10−6–10−13 M, which ` | oui |
| PMC12199321 | `low LODs of 10−12, 10−13, a` | non |
| PMC12199321 | `low LODs of 10−12, 10−13, a` | non |
| PMC12199321 | `nS2 MFs for 10−9 M MeB mol` | oui |
| PMC12199321 | `ntration of 10−6–10−13 M, ` | oui |
| PMC12199321 | `on (LOD) of 10−13 M for met` | oui |
| PMC12199321 | `ons of 10−6–10−13 M were ad` | oui |
| PMC12199321 | `ons of 10−6–10−13 M were in` | oui |
| PMC12199321 | `reatly from 10−6 to 10−14 ` | non |
| PMC12199321 | `rom 10−6 to 10−14 M []. The` | non |
| PMC12199321 | `s of 10−12, 10−13, and 10−1` | oui |
| PMC12199321 | `s of 10−12, 10−13, and 10−1` | oui |
| PMC12199321 | `trations of 10−6–10−13 M w` | oui |
| PMC12199321 | `trations of 10−6–10−13 M w` | oui |
| PMC12199321 | `ttleneck of 10−10 M for pur` | non |
| PMC12199321 | `uctures for 10−8 M MeB mol` | non |
| PMC12199321 | `w as 10−12, 10−13, and 10−1` | oui |
| PMC12306418 | `2 × 10−2 meV K−1). By fitt` |  |
| PMC12306418 | `4+/Te2+/Te0/Te−2) do exist` |  |
| PMC12306418 | `5, and 1710 cm−1 in the FT` |  |
| PMC12306418 | `nt (≈8.62 × 10−2 meV K−1).` |  |
| PMC12311843 | ` to be 0.032 K−1 at 303 K,` | oui |
| PMC12311843 | `10 and 1530 cm−1 in FP(B/I` | non |
| PMC12311843 | `2, and 2921 cm−1 correspon` | non |
| PMC12311843 | `49 and 1074 cm−1 that corr` | non |
| PMC12311843 | `88 and 1723 cm−1 peaks are` | oui |
| PMC12311843 | `90 and 1074 cm−1 appear fr` | non |
| PMC12311843 | `Sa) of 0.032 K−1 and relat` | non |
| PMC12311843 | `Sr) of 12.5% K−1, over a t` | non |
| PMC12311843 | `d 3300–3400 cm−1 is associ` | non |
| PMC12311843 | `ity is 12.5% K−1 at 363 K.` | oui |
| PMC12312155 | `06 and 3554 cm–1 before th` | oui |
| PMC12312155 | `30 and 3138 cm–1 are attri` | non |
| PMC12312155 | `689 and 764 cm–1 are attri` | oui |
| PMC12312155 | `83 and 1665 cm–1 are relat` | oui |
| PMC12312155 | `90 and 1294 cm–1 are assig` | oui |
| PMC12312155 | `and at 3026 cm–1; however,` | non |
| PMC12312155 | `ved at 1483 cm–1 correspon` | oui |
| PMC12423905 | ` to 0.05 cm3 g−1 (1.2 µmol` |  |
| PMC12423905 | ` to 19.75 m2 g−1 (at 1.2 µ` |  |
| PMC12423905 | `om 674.42 m2 g−1 (MSN) to ` |  |
| PMC12423905 | `rom 0.59 cm3 g−1 (MSN) to ` |  |
| PMC12455581 | ` 86% at 2 mV s−1 to 59% at` | oui |
| PMC12455581 | ` about 2 mg cm−2 for each ` | oui |
| PMC12455581 | ` around 428 cm−1 and overl` | oui |
| PMC12455581 | ` kg−1 at 1 A g−1 and a pow` | non |
| PMC12455581 | ` of 2–100 mV s−1 where all` | non |
| PMC12455581 | ` of 416.3 W kg−1 at 0.5 A ` | oui |
| PMC12455581 | ` of 416.3 W kg−1 at a spec` | oui |
| PMC12455581 | `(23.44 W h kg−1 at 350 W ` | non |
| PMC12455581 | `-bond (1678 cm−1) appears ` | oui |
| PMC12455581 | `1 and 457 W kg−1, respecti` | non |
| PMC12455581 | `1, and 1139 cm−1, consiste` | oui |
| PMC12455581 | `2 cm−1, 663 cm−1, and 665 ` | oui |
| PMC12455581 | `400 to 4000 cm−1. The surf` | non |
| PMC12455581 | `59% at 40 mV s−1, as illus` | oui |
| PMC12455581 | `698 and 431 cm−1 belong to` | oui |
| PMC12455581 | `AC (11 W h kg−1 at 200 W ` | non |
| PMC12455581 | `and 143 mA h g−1 at a spec` | oui |
| PMC12455581 | `ate of 40 mV s−1, the capa` | oui |
| PMC12455581 | `band at 477 cm−1 is also d` | oui |
| PMC12455581 | `band at 514 cm−1 in the ZI` | oui |
| PMC12455581 | `cles at 10 A g−1. Thus, th` | non |
| PMC12455581 | `cles at 20 A g−1) in the t` | non |
| PMC12455581 | `cles at 20 A g−1.3.2.2Elec` | non |
| PMC12455581 | `d 3300–3500 cm−1, indicati` | oui |
| PMC12455581 | `d at 124.28 cm−1, 170.87 c` | oui |
| PMC12455581 | `ent of 0.5 A g−1. After 10` | non |
| PMC12455581 | `ents at 10 A g−1 specific ` | non |
| PMC12455581 | `ere, i(V) (A g−1) represen` | non |
| PMC12455581 | `f 16.28 W h kg−1 at 1 A g−` | non |
| PMC12455581 | `f 161.2 mA h g−1 at 1 A g−` | oui |
| PMC12455581 | `f 161.2 mA h g−1 at 1 A g−` | oui |
| PMC12455581 | `f 322.8 mA h g−1 at 10 mV ` | oui |
| PMC12455581 | `f 36.97 W h kg−1 and a pow` | non |
| PMC12455581 | `f 36.97 W h kg−1 and speci` | non |
| PMC12455581 | `f 99.44 mA h g−1 at a curr` | oui |
| PMC12455581 | `g from 10 mV s−1 to 500 mV` | oui |
| PMC12455581 | `g−1 at 0.5 A g−1. The asse` | non |
| PMC12455581 | `g−1 at 10 mV s−1 with 7 wt` | non |
| PMC12455581 | `h g−1 at 1 A g−1 and high ` | non |
| PMC12455581 | `h g−1 at 1 A g−1 as compar` | non |
| PMC12455581 | `ity of 0.5 A g−1. An asymm` | non |
| PMC12455581 | `m−1, 170.87 cm−1, 257.16 c` | oui |
| PMC12455581 | `m−1, 257.16 cm−1, 308.16 c` | oui |
| PMC12455581 | `m−1, 308.16 cm−1, 423.22 c` | oui |
| PMC12455581 | `m−1, 423.22 cm−1, and 1139` | oui |
| PMC12455581 | `om 12.6 mA h g−1 to 14.4 m` | oui |
| PMC12455581 | `pacitance (F g−1), ΔV− is ` | non |
| PMC12455581 | `pacity (mA h g−1) of the p` | non |
| PMC12455581 | `power Ps (W kg−1) was calc` | non |
| PMC12455581 | `rate of 2 mV s−1, and it w` | oui |
| PMC12455581 | `rates (in mV s−1) from 2 t` | non |
| PMC12455581 | `rgy Es (W h kg−1) of the a` | non |
| PMC12455581 | `rrent of 1 A g−1, respecti` | oui |
| PMC12455581 | `rrent, v (mV s−1) is the s` | non |
| PMC12455581 | `rved at 662 cm−1, 663 cm−1` | oui |
| PMC12455581 | `ss and 420 g m−2 areal den` | oui |
| PMC12455581 | `to 14.4 mA h g−1 within th` | oui |
| PMC12455581 | `to 16.7 mA h g−1, which th` | oui |
| PMC12455581 | `ty of 650 W kg−1 and the C` | non |
| PMC12455581 | `ty, Qs (mA h g−1), was cal` | non |
| PMC12455581 | `ure at 20 mV s−1. Fig. 8(c` | non |
| PMC12455581 | `urrent (in A g−1) from 1 t` | non |
| PMC12455581 | `y of 16 W h kg−1 and 457 W` | non |
| PMC12455581 | `−1 at 200 W kg−1),40 and C` | non |
| PMC12455581 | `−1 at 350 W kg−1),55 among` | non |
| PMC12455581 | `−1 to 500 mV s−1. These cu` | non |
| PMC12455581 | `−1, and 665 cm−1 for ZIF-6` | oui |
| PMC12494978 | `54 and 1249 cm−1, indicate` |  |
| PMC12494978 | `e 1000–1100 cm−1 range, wh` |  |
| PMC12494978 | `f 2910–3250 cm−1 correspon` |  |
| PMC12494978 | `n below 900 cm−1, which is` |  |
| PMC12494978 | `nal at 1530 cm−1 indicates` |  |
| PMC12494978 | `nal at 2825 cm−1 indicates` |  |
| PMC12505225 | ` up to 4500 cm−1, with onl` |  |
| PMC12505225 | `400 to 4000 cm−1, confirm ` |  |
| PMC12505225 | `A, 400–4000 cm−1) for the ` |  |
| PMC12505225 | `ably at 579 cm−1), signify` |  |
| PMC12505225 | `ak near 861 cm−1 confirms ` |  |
| PMC12505225 | `around 2340 cm−1 is attrib` |  |
| PMC12505225 | `band at 803 cm−1 and 1064 ` |  |
| PMC12505225 | `e 1070–1100 cm−1 range. On` |  |
| PMC12505225 | `enumber 579 cm−1, a smalle` |  |
| PMC12505225 | `hing at 461 cm−1, which ma` |  |
| PMC12505225 | `imately 803 cm−1 and 1064 ` |  |
| PMC12505225 | `peak at 453 cm−1 attribute` |  |
| PMC12505225 | `peak at 579 cm−1 in the FT` |  |
| PMC12505225 | `rved at 453 cm−1, which is` |  |
| PMC12505225 | `s below 500 cm−1 are indic` |  |
| PMC12505225 | `−1 and 1064 cm−1 are defin` |  |
| PMC12505225 | `−1 and 1064 cm−1 is consis` |  |
| PMC12552603 | ` of 0.04 cm3 g–1. The valu` | non |
| PMC12552603 | `3O4 to 120 m2g−1 after the` | oui |
| PMC12552603 | `6, and 1155 cm−1. Two peak` | non |
| PMC12552603 | `670 and 769 cm−1, associat` | non |
| PMC12552603 | `BET of 610 m2g−1, and pore` | non |
| PMC12552603 | `ET of 1123 m2g–1, and pore` | non |
| PMC12552603 | `acity qe (mg g−1) and perc` | non |
| PMC12552603 | `capacity (mg g−1), KL is L` | non |
| PMC12552603 | `d at 638.12 cm−1, attribut` | oui |
| PMC12552603 | `e of 0,03 cm3g−1 was obtai` | non |
| PMC12552603 | `eak at 1572 cm−1 should be` | non |
| PMC12552603 | `eak at 1622 cm−1 is attrib` | oui |
| PMC12552603 | `eak at 3433 cm−1. The char` | non |
| PMC12552603 | `ntration (mg L−1), KF and ` | non |
| PMC12552603 | `ntration (mg g−1), Qmax re` | non |
| PMC12552603 | `of 400–4000 cm−1. Brunauer` | non |
| PMC12552603 | `sed to 745 m2g–1 by functi` | oui |
| PMC12624334 | ` of 690–900 cm−1 are indic` | oui |
| PMC12624334 | `.20 × 10−2 min−1.18 Furthe` | non |
| PMC12624334 | `.73 × 10−2 min−1. The core` | non |
| PMC12624334 | `.73 × 10−2 min−1. This fin` | non |
| PMC12624334 | `5, and 60 mg L−1, and the ` | non |
| PMC12624334 | `6% for 30 mg L−1 methylene` | non |
| PMC12624334 | `8 (378.14 m2 g−1). The ∼40` | non |
| PMC12624334 | `8 (445.02 m2 g−1) > ZIF-8 ` | oui |
| PMC12624334 | `8 (459.14 m2 g−1) > Fe(5)/` | oui |
| PMC12624334 | `8 (528.08 m2 g−1) > Fe(15)` | oui |
| PMC12624334 | `and at 1143 cm−1 indicates` | oui |
| PMC12624334 | `and at 2928 cm−1 is attrib` | oui |
| PMC12624334 | `around 1400 cm−1. Addition` | oui |
| PMC12624334 | `ation (15 mg L−1), the pho` | oui |
| PMC12624334 | `ation (30 mg L−1), indicat` | non |
| PMC12624334 | `band at 424 cm−1 is assign` | oui |
| PMC12624334 | `ion of 30 mg L−1 offers op` | non |
| PMC12624334 | `ion to 30 mg L−1 resulted ` | oui |
| PMC12624334 | `ion to 45 mg L−1 and 60 mg` | oui |
| PMC12624334 | `of 400–4000 cm−1. The morp` | non |
| PMC12624334 | `t of 2.20 × 10−2 min−1.18 ` | non |
| PMC12624334 | `t of 2.73 × 10−2 min−1. Th` | oui |
| PMC12624334 | `t of 2.73 × 10−2 min−1. Th` | oui |
| PMC12624334 | `ution (30 mg L−1) under vi` | oui |
| PMC12624334 | `ution (30 mg L−1). The cor` | non |
| PMC12624334 | `ution (30 mg L−1, pH ≈ 6.8` | oui |
| PMC12624334 | `−1 and 60 mg L−1 led to a ` | oui |
| PMC12693316 | ` was 0.05 mg L−1 (σ = stan` |  |
| PMC12693316 | `) of 30.2 mg g−1, derived ` |  |
| PMC12693316 | `-MSNs, 20 mg L−1 3-CA, 60 ` |  |
| PMC12693316 | `0.05–15.0 mg L−1 (A = 0.05` |  |
| PMC12693316 | `057 and 798 cm−1 were attr` |  |
| PMC12693316 | `= 0.05929 L mg−1) indicate` |  |
| PMC12693316 | `E = 0.022 mg g−1), with qe` |  |
| PMC12693316 | `and at 1525 cm−1 from asym` |  |
| PMC12693316 | `e to 4.20 mg g−1 in the fi` |  |
| PMC12693316 | `ea (>1000 m2 g−1). These f` |  |
| PMC12693316 | `eak at 1635 cm−1 was assig` |  |
| PMC12693316 | `eaks at 958 cm−1 (Si-OH be` |  |
| PMC12693316 | `from 4.92 mg g−1 in the fi` |  |
| PMC12693316 | `ite (<0.4 mg g−1 at pH 5.0` |  |
| PMC12693316 | `ite (<0.5 mg g−1 at pH 8.8` |  |
| PMC12693316 | `m of 45.8 mg g−1 (pH 7, 25` |  |
| PMC12693316 | `n near 3325 cm−1, attribut` |  |
| PMC12693316 | `ng) and 453 cm−1 (Si-O-Si ` |  |
| PMC12693316 | `ork (>500 m2 g−1).UV–Vis d` |  |
| PMC12693316 | `ration 20 mg L−1), BPA-MSN` |  |
| PMC12693316 | `red at 3040 cm−1, correspo` |  |
| PMC12693316 | `t 0.1–5.0 mg L−1, yielding` |  |
| PMC12693316 | `t 1 and 5 mg L−1 (Table 6)` |  |
| PMC12693316 | `t 3500–3000 cm−1, correspo` |  |
| PMC12693316 | `was 0.016 mg L−1, and the ` |  |
| PMC12805362 | ` and 6.12 × 10−11 cm2 s−1 f` | oui |
| PMC12805362 | ` area (56 m2 g−1), resulti` | non |
| PMC12805362 | ` of 99.8 mAh g−1, correspo` | non |
| PMC12805362 | ` to 48.6 mAh g−1. The LPF-` | oui |
| PMC12805362 | ` × 10−10 cm2 s−1 across th` | oui |
| PMC12805362 | ` × 10−11 cm2 s−1 for the L` | oui |
| PMC12805362 | ` × 10−11 cm2 s−1 when the ` | non |
| PMC12805362 | `, R (J K−1·mol−1) is the g` | non |
| PMC12805362 | `, and 0.8 mV s-1 on a Rads` | oui |
| PMC12805362 | `1 to 11.7 × 10−11 cm2 s−1 w` | non |
| PMC12805362 | `5 and 18 mAh g−1, respecti` | oui |
| PMC12805362 | `about 83 mAh g−1 at 0.1 C ` | oui |
| PMC12805362 | `e of 2.25 × 10−10 cm2 s−1 a` | oui |
| PMC12805362 | `e of 5.38 × 10−11 and 6.12 ` | oui |
| PMC12805362 | `ea, C0 (mol cm−3) is the i` | non |
| PMC12805362 | `from 1.26 × 10−11 to 11.7 ×` | non |
| PMC12805362 | `ing of 2 mg cm-2 on the Al` | oui |
| PMC12805362 | `ity (170 mAh g−1), satisfa` | non |
| PMC12805362 | `m ions, R (J K−1·mol−1) is` | non |
| PMC12805362 | `nd 0.230 cm3 g−1 for the L` | oui |
| PMC12805362 | `nd 110.1 mAh g−1 at 1 C an` | oui |
| PMC12805362 | `nt (21.82 mN m−1 at room t` | non |
| PMC12805362 | `of 154.3 mAh g−1 and 110.1` | non |
| PMC12805362 | `on (22.51 mN m−1 at room t` | non |
| PMC12805362 | `ound 130 mAh g−1 at 0.1 C,` | oui |
| PMC12805362 | `ring 130 mAh g−1 at a curr` | oui |
| PMC12805362 | `round 25 mAh g−1 at 1 C). ` | oui |
| PMC12805362 | `sion (36 mAh g−1 at 10 C, ` | oui |
| PMC12805362 | `t 0.1–0.8 mV s−1 in the LF` | oui |
| PMC12805362 | `te of 0.5 mV s−1. The cont` | non |
| PMC12805362 | `tely 107 mAh g−1 at 1 C, d` | oui |
| PMC12805362 | `ty of 82 mAh g−1 at the sa` | oui |
| PMC12805362 | `y of 130 mAh g−1 at a curr` | oui |
| PMC12917697 | ` cm–1, 1597 cm–1, , 1506 ` |  |
| PMC12917697 | ` set to 1 × 10–5, with a m` |  |
| PMC12917697 | `, and 1261 cm–1 were obs` |  |
| PMC12917697 | `0 cm–1 at 4 cm–1 resolutio` |  |
| PMC12917697 | `00 and 1039 cm–1. On the o` |  |
| PMC12917697 | `00 and 3257 cm–1 in the ca` |  |
| PMC12917697 | `352 to 1312 cm–1 which cor` |  |
| PMC12917697 | `52 and 1153 cm–1, respecti` |  |
| PMC12917697 | `accuracy of 10–3 kcal/mol.` |  |
| PMC12917697 | `accuracy of 10–3 kcal/mol.` |  |
| PMC12917697 | `and at 1018 cm–1 experimen` |  |
| PMC12917697 | `and at 3310 cm–1 in the sy` |  |
| PMC12917697 | `k from 3310 cm–1 in pristi` |  |
| PMC12917697 | `min at 3508 cm–1 was absen` |  |
| PMC12917697 | `nk) to 3302 cm–1 in the Cu` |  |
| PMC12917697 | `of 600–4000 cm–1 at 4 cm–1` |  |
| PMC12917697 | `old was 2 × 10–5 Ha, while` |  |
| PMC12917697 | `olerance of 10–3 kcal/mol,` |  |
| PMC12917697 | `peak at 862 cm–1 was attri` |  |
| PMC12917697 | `red at 1078 cm–1 and at 10` |  |
| PMC12917697 | `red at 1628 cm–1, 1597 cm–` |  |
| PMC12917697 | `ted at 2922 cm–1 arose fro` |  |
| PMC12917697 | `ved at 1641 cm–1 in the sp` |  |
| PMC12917697 | `–1, , 1506 cm–1, , and 1` |  |
| PMC13209189 | ` term Ddip ∝ r−3, which de` |  |
| PMC13209189 | `700 and 950 cm−1 diminishe` |  |
| PMC13209189 | `iC TO (~796 cm−1) and LO (` |  |
| PMC13209189 | `nd LO (~972 cm−1) modes sh` |  |
| PMC13257848 | ` cm−1, 1147 cm−1 and 421 c` | oui |
| PMC13257848 | ` cm−1, 1256 cm−1, 1147 cm−` | oui |
| PMC13257848 | `aks at 1554 cm−1, 1256 cm−` | oui |
| PMC13257848 | `around 1100 cm−1 exhibited` | oui |
| PMC13257848 | `cm−1 to 150 cm−1. These ch` | non |
| PMC13257848 | `d from 3430 cm−1 to 3428 c` | oui |
| PMC13257848 | `eak at 1367 cm−1, tentativ` | oui |
| PMC13257848 | `imately 120 cm−1 to 150 cm` | oui |
| PMC13257848 | `ing at 1685 cm−1 correspon` | oui |
| PMC13257848 | `m−1 and 421 cm−1 were ascr` | oui |
| PMC13257848 | `m−1 to 3428 cm−1, and the ` | oui |
| PMC13257848 | `t 3300–3500 cm−1 and 1638 ` | oui |
| PMC13257848 | `−1 and 1638 cm−1, which co` | oui |
| PMC13269777 | `-1 and 1150 cm-1 peaks cor` |  |
| PMC13269777 | `aks at 2875 cm−1 and 2921 ` |  |
| PMC13269777 | `and at 1660 cm−1 correspon` |  |
| PMC13269777 | `d. The 1246 cm-1 and 1150 ` |  |
| PMC13269777 | `nds at 1482 cm−1 and 1580 ` |  |
| PMC13269777 | `−1 and 1580 cm−1 are attri` |  |
| PMC13269777 | `−1 and 2921 cm-1 are attri` |  |
| PMC13295043 | ` N2 (45 mL·min–1) at 120 °` |  |
| PMC13295043 | ` is 0.55 cm3·g–1, while th` |  |
| PMC13295043 | ` of 0.54 cm3·g–1, and an a` |  |
| PMC13295043 | ` of 0.59 cm3·g–1, with an ` |  |
| PMC13295043 | ` °C (10 °C min–1), using 1` |  |
| PMC13295043 | `2 and 3 mL·min–1 CO2 (10% ` |  |
| PMC13295043 | `IF-8 (9.7% min–1). In cont` |  |
| PMC13295043 | `a of 1001 m2·g–1 and a tot` |  |
| PMC13295043 | `a of 1298 m2·g–1, a total ` |  |
| PMC13295043 | `e of 27 mL·min–1 N2 and 3 ` |  |
| PMC13295043 | `e of 30 mL·min–1), control` |  |
| PMC13295043 | `ea of 111 m2 g–1, accompan` |  |
| PMC13295043 | `ere (70 mL min–1).Nitrogen` |  |
| PMC13295043 | `he 680–1000 cm–1 window (F` |  |
| PMC13295043 | `me (0.48 cm3·g–1), while m` |  |
| PMC13295043 | `n (ε ≈ 30 × 10–3), indicat` |  |
| PMC13295043 | `rea (1038 m2·g–1) and pore` |  |
| PMC13315215 | ` 116.02 ml min-1 g-1 and a` | non |
| PMC13315215 | `.02 ml min-1 g-1 and a low` | non |
| PMC13333848 | `peak at 211 cm−153.Figure ` | non |
| PMC13368945 | ` (1583–1423 cm−1) exhibits` |  |
| PMC13368945 | ` (−28.77 J mol−1 K−1) show` |  |
| PMC13368945 | ` and 1184.8 cm−1 correspon` |  |
| PMC13368945 | ` at 758–693 cm−1 in the lo` |  |
| PMC13368945 | ` at 758–693 cm−1 resemble ` |  |
| PMC13368945 | ` of 0.062 L mg−1. A high c` |  |
| PMC13368945 | `(-17.17 kJ mol−1) indicate` |  |
| PMC13368945 | `(−16.63 kJ mol−1). The neg` |  |
| PMC13368945 | `(−16.99 kJ mol−1) and 318 ` |  |
| PMC13368945 | `(−38.30 kJ mol−1) and ΔS0 ` |  |
| PMC13368945 | `34 and 2928 cm−1 correspon` |  |
| PMC13368945 | `8.77 J mol−1 K−1) show tha` |  |
| PMC13368945 | `83 and 1423 cm−1 arise fro` |  |
| PMC13368945 | `and 1506.67 cm−1 are attri` |  |
| PMC13368945 | `be 0.3625 cm3g−1. The surf` |  |
| PMC13368945 | `k at 683.95 cm−1 correspon` |  |
| PMC13368945 | `nd 1145–994 cm−1 regions c` |  |
| PMC13368945 | `t 3140–2928 cm−1 becomes s` |  |
| PMC13393389 | ` 2 (g mg–1 min–1) are the ` | non |
| PMC13393389 | ` = −28.4 J mol–1K–1) indic` | oui |
| PMC13393389 | ` Al = 0.8 mg L–1, Fe = 0.4` | oui |
| PMC13393389 | ` Fe = 0.4 mg L–1, and Mg =` | oui |
| PMC13393389 | ` Mg = 3.0 mg L–1. All valu` | non |
| PMC13393389 | ` and C e (mg L–1) are the ` | non |
| PMC13393389 | ` and k 2 (g mg–1 min–1) ar` | non |
| PMC13393389 | ` of 11.25 mg g–1. This ini` | oui |
| PMC13393389 | ` of 224.8 mg g–1 and a rem` | non |
| PMC13393389 | ` of 224.8 mg g–1 for the t` | oui |
| PMC13393389 | ` of 224.8 mg g–1, signific` | non |
| PMC13393389 | ` of 621.7 m2 g–1, compared` | oui |
| PMC13393389 | ` q m,cal (mg g–1) represen` | non |
| PMC13393389 | ` to 0.195 mg m–2 (Al/Mg-BD` | non |
| PMC13393389 | ` to 0.200 mg m–2 in the tr` | non |
| PMC13393389 | ` to 215.2 mg g–1. This pos` | non |
| PMC13393389 | ` −34.49 kJ mol–1) further ` | oui |
| PMC13393389 | ` −34.49 kJ mol–1, ΔS° < 0)` | non |
| PMC13393389 | `(C 0 = 10 mg L–1, dose = 2` | non |
| PMC13393389 | `(below 1600 cm–1) across a` | non |
| PMC13393389 | `(mg g–1) (L mg–1)­1/ n ) a` | non |
| PMC13393389 | `, and k 1 (min–1) and k 2 ` | non |
| PMC13393389 | `.5 and 1416 cm–1 to 1589 a` | oui |
| PMC13393389 | `.8 to 7.9 mg g–1, a result` | oui |
| PMC13393389 | `0.2 to 1.2 g L–1 (equivale` | non |
| PMC13393389 | `10 to 300 mg L–1. This dec` | non |
| PMC13393389 | `3% (11.79 mg g–1) observed` | oui |
| PMC13393389 | `8.314 J mol–1K–1) and T is` | non |
| PMC13393389 | `89 and 1411 cm–1, respecti` | oui |
| PMC13393389 | `9% (11.74 mg g–1) at the 2` | oui |
| PMC13393389 | `DC (178.5 mg g–1) and bime` | oui |
| PMC13393389 | `DC (198.9 mg g–1) counterp` | oui |
| PMC13393389 | `F-5 (98.2 mg g–1, 90 h) an` | non |
| PMC13393389 | `L of a 10 mg L–1 CIP solut` | oui |
| PMC13393389 | `a (1122.0 m2 g–1), the mos` | non |
| PMC13393389 | `a of 1122 m2 g–1, and the ` | non |
| PMC13393389 | `al = 9.75 mg g–1). The rel` | non |
| PMC13393389 | `al = 9.86 mg g–1) is in cl` | non |
| PMC13393389 | `and 198.9 mg g–1, respecti` | non |
| PMC13393389 | `and 209.3 mg g–1 in the pr` | oui |
| PMC13393389 | `around 3440 cm–1. This ban` | non |
| PMC13393389 | `band (∼3435 cm–1), confirm` | non |
| PMC13393389 | `beyond 1.0 g L–1 (25 mg), ` | non |
| PMC13393389 | `ime, q e (mg g–1) is the e` | non |
| PMC13393389 | `ion of 10 mg L–1 at pH 7 f` | non |
| PMC13393389 | `ity (q e, mg g–1) were cal` | non |
| PMC13393389 | `ity, K L (L mg–1) is the L` | non |
| PMC13393389 | `ity, qt (mg g–1) is the a` | non |
| PMC13393389 | `mately 1590 cm–1 and 1411 ` | non |
| PMC13393389 | `mately 1685 cm–1, correspo` | non |
| PMC13393389 | `n (10–300 mg L–1) was syst` | non |
| PMC13393389 | `nt, K F ((mg g–1) (L mg–1)` | non |
| PMC13393389 | `o −25.3 kJ mol–1), confirm` | non |
| PMC13393389 | `on (480–600 cm–1) for the ` | non |
| PMC13393389 | `rbon (231 mg g–1, 72 h) an` | non |
| PMC13393389 | `rom 215.2 mg g–1 in the ab` | oui |
| PMC13393389 | `t (8.314 J mol–1K–1) and T` | oui |
| PMC13393389 | `tely 1122 m2 g–1 was succe` | non |
| PMC13393389 | `tion (300 mg L–1) was 0.03` | non |
| PMC13393389 | `to 0.561 cm3 g–1 (Al/Mg/Fe` | non |
| PMC13393389 | `to 1122.0 m2 g–1 (Al/Mg/Fe` | non |
| PMC13393389 | `to 1122.0 m2 g–1 for the f` | oui |
| PMC13393389 | `ty (224.8 mg g–1) and an e` | non |
| PMC13393389 | `u) (190.4 mg g–1, 2.7 h), ` | non |
| PMC13393389 | `xide (379 mg g–1, 48 h). N` | non |
| PMC13393389 | `–1 and 1411 cm–1. These ba` | non |
| PMC13393389 | `−28.4 J mol–1K–1) indicate` | oui |
| PMC13424319 | `(νCH), 1651 cm−1 (νC = N),` |  |
| PMC13424319 | `4, and 1511 cm−1, correspo` |  |
| PMC13424319 | `N) and 1527 cm−1 (νC = C) ` |  |
| PMC13424319 | `ears at 532 cm−1, which is` |  |
| PMC13424319 | `fts to 1157 cm−1, further ` |  |
| PMC13424319 | `nds at 3086 cm−1 (νCH), 16` |  |
| PMC13424319 | `tly to 3093 cm−1, and a pr` |  |
| PMC13446275 | ` (742.9 µmol g−1) of all t` | oui |
| PMC13446275 | ` 1081.9 µmol g−1 and 896.6` | oui |
| PMC13446275 | ` 1345.7 µmol.g−1, which is` | oui |
| PMC13446275 | ` 1587.8 µmol·g−1 and 2125.` | oui |
| PMC13446275 | ` 1713.4 µmol g−1, respecti` | oui |
| PMC13446275 | ` 1816.8 µmol·g−1 and 1713.` | oui |
| PMC13446275 | ` 2125.4 µmol·g−1 for 3 wt%` | oui |
| PMC13446275 | `3 and 1.2 m2 g−1, respecti` | oui |
| PMC13446275 | `a of 55.6 m2 g−1, which ca` | oui |
| PMC13446275 | `d 785.7 µmol g−1, respecti` | oui |
| PMC13446275 | `d 896.6 µmol g−1, respecti` | oui |
| PMC13446275 | `d at 30 mL min−1, where CO` | non |
| PMC13446275 | `e of 50 mL min−1 for 20 mi` | oui |
| PMC13446275 | `f 598.9 µmol g−1. Such rel` | oui |
| PMC13446275 | `f 896.6 µmol g−1 and 785.7` | oui |
| PMC13446275 | `of 1009 µmol g−1 under vis` | oui |
| PMC13446275 | `of 1009 µmol g−1, could be` | non |
| PMC13446275 | `then 20 mL min−1 for the r` | oui |
| PMC13459614 | ` (126.5 kJ mol−1 at pH 5.0` |  |
| PMC13459614 | ` (211.6 kJ mol−1vs. 75.7 k` |  |
| PMC13459614 | ` (3300–3500 cm−1) confirme` |  |
| PMC13459614 | ` CN at 1584 cm−1) were ret` |  |
| PMC13459614 | ` CO at 1644 cm−1, and glyc` |  |
| PMC13459614 | ` at 850–650 cm−1 indicated` |  |
| PMC13459614 | ` band (∼420 cm−1) remained` |  |
| PMC13459614 | ` of 6.25 µg mL−1 for S. au` |  |
| PMC13459614 | ` of 6.25 µg mL−1, confirmi` |  |
| PMC13459614 | ` of 742.0 m2 g−1 (Fig. 5b)` |  |
| PMC13459614 | ` one at 724 cm−1 was assig` |  |
| PMC13459614 | `) and ∼1504 cm−1 (N–H bend` |  |
| PMC13459614 | `, and 50 µg mL−1) and incu` |  |
| PMC13459614 | `. 10.02 kJ mol−1 for ZIF-8` |  |
| PMC13459614 | `.9–28.2 kJ mol−1 (Fig. 10c` |  |
| PMC13459614 | `0, and 1450 cm−1; glycosid` |  |
| PMC13459614 | `0; 81.2 kJ mol−1 at pH 5.5` |  |
| PMC13459614 | `1, and 1042 cm−1, while th` |  |
| PMC13459614 | `31 and 2844 cm−1, and a st` |  |
| PMC13459614 | `4, and 1028 cm−1; the shar` |  |
| PMC13459614 | `5 and 50 µg mL−1 (Fig. 8a)` |  |
| PMC13459614 | `644 and 996 cm−1 were reta` |  |
| PMC13459614 | `8/CS (20 µg mL−1)14 and ou` |  |
| PMC13459614 | `84 and 1028 cm−1.14,36 The` |  |
| PMC13459614 | `8–13.45 kJ mol−1 across ac` |  |
| PMC13459614 | `9, and 2851 cm−1. The stro` |  |
| PMC13459614 | `@CCM (22 µg mL−1).28,58The` |  |
| PMC13459614 | `CS (534.0 m2 g−1 and 0.184` |  |
| PMC13459614 | `Zn–N at 420 cm−1 and CN at` |  |
| PMC13459614 | `and 12.5 µg mL−1 for E. co` |  |
| PMC13459614 | `as 5.26 kJ mol−1) while si` |  |
| PMC13459614 | `ate of 10° min−1. The degr` |  |
| PMC13459614 | `ch at ∼3435 cm−1, a C–H st` |  |
| PMC13459614 | `de I (∼1650 cm−1) and amid` |  |
| PMC13459614 | `de I (∼1656 cm−1) and amid` |  |
| PMC13459614 | `e (0.261 cm3 g−1). The hig` |  |
| PMC13459614 | `e II (∼1590 cm−1) bands ov` |  |
| PMC13459614 | `e II (∼1590 cm−1) bands. P` |  |
| PMC13459614 | `e of 10 °C min−1 with a co` |  |
| PMC13459614 | `e of 50 mL min−1. To condu` |  |
| PMC13459614 | `e: 35.9 kJ mol−1 for the f` |  |
| PMC13459614 | `ea (678.0 m2 g−1) and micr` |  |
| PMC13459614 | `ear 995–920 cm−1 were assi` |  |
| PMC13459614 | `f 211.6 kJ mol−1, compared` |  |
| PMC13459614 | `hen, a 1 mg mL−1 aqueous s` |  |
| PMC13459614 | `ied. 500 µg mL−1 powdered ` |  |
| PMC13459614 | `illin (1 mg mL−1 in dimeth` |  |
| PMC13459614 | `ion at 1584 cm−1 originate` |  |
| PMC13459614 | `ion at 1644 cm−1. Aromatic` |  |
| PMC13459614 | `ion at ∼420 cm−1 was attri` |  |
| PMC13459614 | `ks at ∼1820 cm−1 (C <svg ` |  |
| PMC13459614 | `ly 75.7 kJ mol−1 for PD@ZI` |  |
| PMC13459614 | `n of 0.5 mg mL−1 using mod` |  |
| PMC13459614 | `nd 0.184 cm3 g−1, respecti` |  |
| PMC13459614 | `nd at ∼3365 cm−1, aliphati` |  |
| PMC13459614 | `o 10.02 kJ mol−1 for bare ` |  |
| PMC13459614 | `o 211.6 kJ mol−1). Both th` |  |
| PMC13459614 | `of 0.468 cm3 g−1 (Fig. 5a)` |  |
| PMC13459614 | `of 1221.0 m2 g−1, and a mi` |  |
| PMC13459614 | `of 1289.0 m2 g−1, a microp` |  |
| PMC13459614 | `of 4000–500 cm−1 using a N` |  |
| PMC13459614 | `peak at 996 cm−1 correspon` |  |
| PMC13459614 | `s (5.26 kJ mol−1vs. 10.02 ` |  |
| PMC13459614 | `s. 75.7 kJ mol−1 for ZIF-8` |  |
| PMC13459614 | `t 1147–1028 cm−1 (Fig. S4d` |  |
| PMC13459614 | `t 1450–1380 cm−1.5,13,15,1` |  |
| PMC13459614 | `t 2931/2844 cm−1, CO at 16` |  |
| PMC13459614 | `t 3370–3320 cm−1, C–H at 2` |  |
| PMC13459614 | `t 3435–3300 cm−1, amide I ` |  |
| PMC13459614 | `tch at 2931 cm−1, and amid` |  |
| PMC13459614 | `the 800–650 cm−1 region. T` |  |
| PMC13459614 | `tion at 883 cm−1 was assoc` |  |
| PMC13459614 | `to 5.26 kJ mol−1 at pH 5 c` |  |
| PMC13459614 | `ty (∼0.1 mg mL−1), during ` |  |
| PMC13459614 | `umin (22 µg mL−1) and ZIF-` |  |
| PMC13516552 | ` (0.0958 cm3 g−1) than pri` |  |
| PMC13516552 | ` ~1300–1100 cm−1 correspon` |  |
| PMC13516552 | ` ~1600–1500 cm−1 region ar` |  |
| PMC13516552 | `0.85–1.0 mg cm−2.CR2032-ty` |  |
| PMC13516552 | `CNT at 0.1 A g−1, and the ` |  |
| PMC13516552 | `CNT at 0.1 A g−1. The Poly` |  |
| PMC13516552 | `CV at 0.1 mV s−1 scan rate` |  |
| PMC13516552 | `Pc (19.17 m2 g−1 and 0.062` |  |
| PMC13516552 | `band (~1320 cm−1) and G-ba` |  |
| PMC13516552 | `band (~1565 cm−1) associat` |  |
| PMC13516552 | `d 0.0624 cm3 g−1). This in` |  |
| PMC13516552 | `ea (31.29 m2 g−1) and larg` |  |
| PMC13516552 | `es to 803 mA g−1 after 100` |  |
| PMC13516552 | `g−1 at 0.5 A g−1). These i` |  |
| PMC13516552 | `g−1 at 0.5 A g−1, indicati` |  |
| PMC13516552 | `ite at 0.1 A g−1 are shown` |  |
| PMC13516552 | `ity of 0.5 A g−1. Overall,` |  |
| PMC13516552 | `les at 0.1 A g−1, and stro` |  |
| PMC13516552 | `lity (855 mA g−1 at 0.5 A ` |  |
| PMC13516552 | `n of 1047 mA g−1 after 100` |  |
| PMC13516552 | `of 400–4000 cm−1, along wi` |  |
| PMC13516552 | `ty (~372 mAh g−1) and limi` |  |
| PMC13516552 | `ty of 855 mA g−1 at 0.5 A ` |  |
| PMC13516552 | `y of 1047 mA g−1 after 100` |  |
| PMC13516552 | `y of 1703 mA g−1, which de` |  |
| PMC13516552 | `y of 2016 mA g−1 and retai` |  |
| PMC13516552 | `y of 2016 mA g−1, excellen` |  |
| PMC13516552 | `~600–900 mAh g−1 depending` |  |
| PMC13580062 | ` cm−1, 1578 cm−1, and 1703` |  |
| PMC13580062 | `1, and 1703 cm−1, which we` |  |
| PMC13580062 | `d 3200–3600 cm−1, respecti` |  |
| PMC13580062 | `m−1 and 549 cm−1, which be` |  |
| PMC13580062 | `rred at 748 cm−1 and 549 c` |  |
| PMC13580062 | `ted at 2872 cm−1, correspo` |  |
| PMC13580062 | `ved at 1382 cm−1, 1578 cm−` |  |
| PMC13580062 | `ved at 1612 cm−1 and 3200–` |  |
| PMC2893540 | `.72–4.14 mA cm−2, and Voc ` |  |
| PMC2893540 | `.93–2.25 mA cm−2, and in c` |  |
| PMC2893540 | `r of 100 mW cm−2.Results a` |  |
| PMC2893540 | `× 109 wires cm−2). The dif` |  |
| PMC2893540 | `× 109 wires cm−2).The effe` |  |
| PMC2893540 | `× 109 wires cm−2, respecti` |  |
| PMC2893540 | `× 109 wires cm−2, which ar` |  |
| PMC2897037 | ` (200–1,100 cm−1) of the S` | non |
| PMC2897037 | `752 and 786 cm−1 correspon` | non |
| PMC2897037 | `786 and 946 cm−1 are obser` | oui |
| PMC2897037 | `799 and 968 cm−1[]. The Si` | non |
| PMC2897037 | `ft of ~4–22 cm−1, which co` | oui |
| PMC2897037 | `peak at 260 cm−1 is attrib` | non |
| PMC2897037 | `peak at 946 cm−1 is the ch` | non |
| PMC2964502 | `+ 1.26(Ir/Ia)]−1[], where ` | non |
| PMC2964502 | `m 2 to 7 M, Cl−1 can affec` | non |
| PMC3088885 | `825 and 471 cm-1 correspon` | oui |
| PMC3088885 | `a (500-4000 cm-1) were rec` | non |
| PMC3088885 | `and at 1384 cm-1 is associ` | non |
| PMC3088885 | `and at 1630 cm-1 in the IR` | non |
| PMC3088885 | `band at 605 cm-1 assigned ` | non |
| PMC3088885 | `ion at 1384 cm-1 could be ` | non |
| PMC3088885 | `ork at 1079 cm-1 increases` | non |
| PMC3212207 | ` and ~1,600 cm-1, which co` |  |
| PMC3212207 | `02 to 1,606 cm-1 due to th` |  |
| PMC3212207 | `100 ~ 1,200 cm-1 region of` |  |
| PMC3212207 | `peak at 520 cm-1 was used ` |  |
| PMC3293091 | ` and 168 mAh g-1, respecti` | oui |
| PMC3293091 | `o be 160 mAh g-1 which was` | oui |
| PMC3293091 | `y of 0.1 mA cm-2 in the vo` | oui |
| PMC3293091 | `y of 0.1 mA cm-2 in the vo` | oui |
| PMC3293091 | `y of 170 mAh g-1 and a sui` | non |
| PMC3305512 | ` ZnO (5.6 g cm-3) []. Also` | non |
| PMC3305512 | `0 = 8.854 × 10-12 F/m, know` | non |
| PMC3305512 | `00 to 1,000 cm-1 are shown` | non |
| PMC3305512 | `00 to 1,000 cm-1 with a re` | oui |
| PMC3305512 | `400 and 600 cm-1, respecti` | oui |
| PMC3305512 | `NiO (6.72 g cm-3) is heavi` | non |
| PMC3305512 | `lution of 1 cm-1.The sampl` | non |
| PMC3330020 | `as 161.1 mAh g-1, which wa` | non |
| PMC3330020 | `e of 0.05 mV·s-1 from 2.0 ` | oui |
| PMC3330020 | `ed 161.1 mAh g-1 and was h` | non |
| PMC3330020 | `is 161.1 mAh g-1 which was` | non |
| PMC3330020 | `of 161.1 mAh g-1 at the fi` | oui |
| PMC3330020 | `of 161.1 mAh g-1 at the fi` | oui |
| PMC3330020 | `te of 0.05 mVs-1. Figure 3` | non |
| PMC3330020 | `to 157.5 mAh g-1 after 30 ` | non |
| PMC3330020 | `to 157.5 mAh g-1, and the ` | oui |
| PMC3330020 | `y of 170 mAh g-1. However,` | non |
| PMC3407523 | ` one at 827 cm–1 comes fro` | non |
| PMC3407523 | `0, and 1024 cm−1. In the I` | non |
| PMC3407523 | `311 to 1385 cm−1, suggesti` | non |
| PMC3407523 | `425 to 3431 cm−1 and 1635 ` | non |
| PMC3407523 | `51 and 1523 cm–1 correspon` | non |
| PMC3407523 | `6, and 1234 cm−1 correspon` | non |
| PMC3407523 | `635 to 1632 cm−1, and 1311` | non |
| PMC3407523 | `68 and 1028 cm−1 were due ` | non |
| PMC3407523 | `8, and 1028 cm−1. The broa` | non |
| PMC3407523 | `and at 1728 cm−1 correspon` | non |
| PMC3407523 | `and at 2122 cm−1 only appe` | non |
| PMC3407523 | `band at 240 cm−1, which ca` | non |
| PMC3407523 | `eak at 1123 cm–1; the one ` | non |
| PMC3407523 | `eak at 1728 cm−1 and disap` | oui |
| PMC3407523 | `eak at 2122 cm−1 confirm t` | oui |
| PMC3407523 | `ent at 1311 cm−1. The peak` | non |
| PMC3407523 | `of 150–1700 cm–1. The samp` | non |
| PMC3407523 | `of 400–4000 cm–1. The Rama` | non |
| PMC3407523 | `und at 1635 cm−1 could be ` | non |
| PMC3407523 | `ved at 3425 cm−1 could be ` | non |
| PMC3477086 | `5 and 2,923 cm−1 were due ` | oui |
| PMC3477086 | `ak at 1,300 cm−1 was obser` | oui |
| PMC3477086 | `ed at 1,420 cm−1. Clear Zn` | non |
| PMC3477086 | `rved at 457 cm−1[], and th` | non |
| PMC3497326 | ` at 330–370 cm−1 which is ` | oui |
| PMC3497326 | `027 and 860 cm−1 correspon` | oui |
| PMC3497326 | `er than 500 cm−1. Samaele ` | non |
| PMC3497326 | `he 280–4000 cm−1 range usi` | oui |
| PMC3497326 | `m−1 and 422 cm−1 for SDS-m` | non |
| PMC3497326 | `of 4000–280 cm−1 (Figure 6` | non |
| PMC3497326 | `peak of 470 cm−1 and 422 c` | non |
| PMC3497326 | `tant at 512 cm−1 (blue-shi` | non |
| PMC3503618 | `, and 2,863 cm−1 (symmetri` | non |
| PMC3503618 | `00 to 4,000 cm−1 at a reso` | non |
| PMC3503618 | `8 and 1,351 cm−1 can be at` | non |
| PMC3503618 | `ak at 1,105 cm−1 is the st` | non |
| PMC3503618 | `ak at 1,735 cm−1 is due to` | non |
| PMC3503618 | `ately 1,654 cm−1 should be` | non |
| PMC3503618 | `d the 1,249 cm−1 is from t` | non |
| PMC3503618 | `lution of 4 cm−1. The samp` | non |
| PMC3503618 | `round 1,105 cm−1) assigned` | non |
| PMC3503618 | `round 1,735 cm−1 have been` | non |
| PMC3659320 | `20.3 – 20.7 cm−1, confirmi` | non |
| PMC3659320 | `around 20.4 cm−1, differen` | non |
| PMC3659320 | `ayer is 4.2 cm−1, close to` | oui |
| PMC3659320 | `er (Δk 20.4 cm−1), the one` | oui |
| PMC3659320 | `er (Δk 22.4 cm−1). We can ` | non |
| PMC3659320 | `layer, 19.4 cm−1. This cou` | non |
| PMC3659320 | `olayer, 3.7 cm−1. This sug` | non |
| PMC3700086 | `een at 1639 cm−1. The two ` | non |
| PMC3700086 | `ll near 3280cm−1, were ass` | oui |
| PMC3700086 | `ved at 1370 cm−1 and 1110 ` | non |
| PMC3700086 | `ved at 3411 cm−1, which fa` | oui |
| PMC3700086 | `−1 and 1110 cm−1 represent` | non |
| PMC3833402 | `ccur at 747 cm−1, and the ` |  |
| PMC3833402 | `der at 3430 cm−1 in the sp` |  |
| PMC3833402 | `e 3430–3200 cm−1 experienc` |  |
| PMC3833402 | `ion 552–672 cm−1 can be at` |  |
| PMC3833402 | `n 1554–1562 cm−1. This mig` |  |
| PMC3833402 | `urs at 3275 cm−1 with a sh` |  |
| PMC3833402 | `w (4000–250 cm−1). Thermog` |  |
| PMC3913497 | ` around 870 cm−1. Moreover` |  |
| PMC3913497 | `21 and 1486 cm−1 come from` |  |
| PMC3913497 | `35 and 1100 cm−1 are assig` |  |
| PMC3913497 | `468 and 957 cm−1 are assig` |  |
| PMC3913497 | `568 and 603 cm−1 is an ind` |  |
| PMC3913497 | `603 and 568 cm−1 are assig` |  |
| PMC3913497 | `and of 1056 cm−1 (assigned` |  |
| PMC3913497 | `f 1600–1700 cm−1 ascribed ` |  |
| PMC3913497 | `lution of 4 cm−1.2.3. Anti` |  |
| PMC3913497 | `n 3200–3600 cm−1 correspon` |  |
| PMC3913497 | `nd 950–1100 cm−1 are chara` |  |
| PMC3913497 | `of 4000–400 cm−1 with spec` |  |
| PMC3913497 | `ons 450–650 cm−1 and 950–1` |  |
| PMC3920662 | `), and 1639 cm−1 for carbo` | non |
| PMC3920662 | `38 and 1637 cm−1, indicati` | oui |
| PMC3920662 | `nds at 3304 cm−1 for –OH s` | non |
| PMC3920662 | `roup), 2928 cm−1 for C–H s` | non |
| PMC3998862 | ` × 104 μg · mL−1, respecti` | oui |
| PMC3998862 | `1 and 3,230 cm−1, which we` | oui |
| PMC3998862 | `1, 1,600.81 cm−1, and 1,02` | oui |
| PMC3998862 | `at 2,918.77 cm−1, 1,600.81` | oui |
| PMC3998862 | `ds, 100 U · mL−1 streptomy` | non |
| PMC3998862 | `f 4,000–500 cm−1 at 2° · c` | non |
| PMC3998862 | `ion (5 mg · mL−1) was adde` | oui |
| PMC3998862 | `ks at 1,360 cm−1 and 3,230` | oui |
| PMC3998862 | `m−1 at 2° · cm−1 resolutio` | non |
| PMC3998862 | `nd 1,021.10 cm−1 can be at` | oui |
| PMC3998862 | `nd 100 μg · mL−1 penicilli` | non |
| PMC3998862 | `rude drug · mL−1) revealed` | oui |
| PMC3998862 | `rude drug · mL−1) was foun` | oui |
| PMC3998862 | `s (2.6 mg · mL−1). Accordi` | non |
| PMC3998862 | `to 300 μg · mL−1 of AgNO3 ` | oui |
| PMC3998862 | `to 4.0 mg · mL−1. Likewise` | non |
| PMC3999824 | ` of about 2·10−10 mbar. Non` |  |
| PMC3999824 | `, ν = 386.1 cm−1, and A1g,` |  |
| PMC3999824 | `, ν = 403.0 cm−1, are cons` |  |
| PMC3999824 | `dening of 6 cm−1 and the p` |  |
| PMC3999824 | `f 180 ± 60 N·m−1, which is` |  |
| PMC3999824 | `ith Δ = 1.3 cm−1. As can b` |  |
| PMC3999824 | `ith Δ = 8.2 cm−1, the diff` |  |
| PMC3999824 | `justed to 8·10−3 mbar duri` |  |
| PMC3999824 | `o ν = 385.2 cm−1 and the A` |  |
| PMC3999824 | `o ν = 403.4 cm−1. Shifts o` |  |
| PMC3999824 | `of 1.8·1013 cm−2 leads to ` |  |
| PMC3999824 | `olution ≈ 1 cm−1) has been` |  |
| PMC3999824 | `reases by 4 cm−1. As our d` |  |
| PMC3999824 | `y 4.5 and 1 cm−1/% [–]. Wh` |  |
| PMC4043712 | `ak at 1,741 cm−1of the sym` | non |
| PMC4043712 | `ak at 3,300 cm−1 was not o` | oui |
| PMC4043712 | `ak at 3,300 cm−1, signifyi` | non |
| PMC4043712 | `ed at 3,390 cm−1, indicati` | oui |
| PMC4043712 | `f 500–4,000 cm−1. For appl` | non |
| PMC4102124 | ` 10−3 l s−1 mg−1, respecti` | oui |
| PMC4102124 | ` 10−3 l s−1 mg−1, respecti` | oui |
| PMC4102124 | ` and 0.61 × 10−3 l s−1 mg−` | oui |
| PMC4102124 | ` and 4.27 × 10−3 l s−1 mg−` | oui |
| PMC4102124 | ` with 10 μg ml−1 pentacle ` | non |
| PMC4102124 | ` μl of 1 mg ml−1 PEGylated` | non |
| PMC4102124 | ` μl of 1 mg ml−1 solution ` | non |
| PMC4102124 | `.27 × 10−3 l s−1 mg−1, res` | oui |
| PMC4102124 | `.61 × 10−3 l s−1 mg−1, res` | oui |
| PMC4102124 | `0−3, 1.19 × 10−3 and 0.61 ` | oui |
| PMC4102124 | `3 to 3.67 × 10−3 and 4.27 ` | oui |
| PMC4102124 | `4 and 4.2 × 10−2 M, respec` | oui |
| PMC4102124 | `808 nm, 1 W cm−2) for 5 mi` | non |
| PMC4102124 | `808 nm, 1 W cm−2) for 6 mi` | non |
| PMC4102124 | `808 nm, 1 W cm−2) over tim` | non |
| PMC4102124 | `808 nm, 1 W cm−2), the 70-` | non |
| PMC4102124 | `808 nm, 1 W cm−2). The tem` | oui |
| PMC4102124 | `aBH4 (4.2 × 10−2 M). Becau` | non |
| PMC4102124 | `aline (2 mg ml−1, 20 μl), ` | non |
| PMC4102124 | `density=1 W cm−2). By comp` | oui |
| PMC4102124 | `ed to a 1-W cm−2 808-nm la` | non |
| PMC4102124 | `enol (1.4 × 10−4 M) and Na` | non |
| PMC4102124 | `from 2.30 × 10−3 to 3.67 ×` | oui |
| PMC4102124 | `ining 10 μg ml−1 Au–Cu all` | oui |
| PMC4102124 | `ining 10 μg ml−1 pentacle ` | non |
| PMC4102124 | `ls to 10 μg ml−1 of pentac` | non |
| PMC4102124 | `o be 2.30 × 10−3, 1.19 × 1` | oui |
| PMC4102124 | `pt at 1.4 × 10−4 and 4.2 ×` | oui |
| PMC4102124 | `sity of 1 W cm−2 for 5 min` | non |
| PMC4102124 | `stals (1 mg ml−1, 200 μl) ` | non |
| PMC4102124 | `tion (10 μg ml−1), irradia` | non |
| PMC4214824 | `N (3 × 1017 cm−3 dopant de` | oui |
| PMC4214824 | `proximately 10−4 A with pr` | oui |
| PMC4214824 | `proximately 10−5 A (Figure` | non |
| PMC4214824 | `proximately 10−5 to approx` | oui |
| PMC4362901 | `67, and 731 cm−1 in the 4,` |  |
| PMC4362901 | `e 4,000–400 cm−1 region. T` |  |
| PMC4362901 | `lution of 4 cm−1 in KBr pe` |  |
| PMC4365402 | ` was 4.0 mg mL−1.The prepa` |  |
| PMC4395432 | `ading (3.67×10–8 mol/cm2; ` |  |
| PMC4395432 | `orods (1.93×10–8 mol/cm2),` |  |
| PMC4403701 | ` LDH at 450 cm−1, therefor` |  |
| PMC4403701 | `1 and 1,000 cm−1, attribut` |  |
| PMC4403701 | `1 and 1,380 cm−1 are the c` |  |
| PMC4403701 | `between 400 cm−1 and 1,000` |  |
| PMC4403701 | `k, at 1,640 cm–1, than LDH` |  |
| PMC4403701 | `ks at 1,640 cm−1 and 1,380` |  |
| PMC4403701 | `peak at 460 cm−1 was attri` |  |
| PMC4403701 | `peak at 460 cm−1 was found` |  |
| PMC4451754 | `.0, and 10μgkg−1by i.p., o` |  |
| PMC4456781 | ` was 1360 m2 g–1 which is ` | non |
| PMC4456781 | `1 and 990 m2 g–1, respecti` | non |
| PMC4456781 | `e of 10 °C min–1 up to 850` | oui |
| PMC4456781 | `gh as 625 m2 g–1 together ` | non |
| PMC4456781 | `g–1, 1970 m2 g–1 and 990 m` | non |
| PMC4456781 | `lution of 4 cm–1. Before c` | non |
| PMC4456781 | `rate: 1 °C min–1). BET sur` | non |
| PMC4456781 | `s of 0.2 cm3 g–1.44 In thi` | non |
| PMC4456781 | `w of 60 mL min–1 at a heat` | non |
| PMC4456781 | `was 0.13 cm3 g–1. However,` | non |
| PMC4456781 | `were 1365 m2 g–1, 1970 m2 ` | non |
| PMC4531889 | ` and 1.04 × 10−4 A were ob` | oui |
| PMC4531889 | `0−4, 1.91 × 10−4, and 1.04` | oui |
| PMC4531889 | `ed oxygen to O−2. After UV` | non |
| PMC4531889 | `s of 1.34 × 10−4, 1.91 × 1` | oui |
| PMC4531889 | `t of 1.91 × 10−4 A at 10 V` | oui |
| PMC4531889 | `t of 3.93 × 10−4 A.Conclus` | oui |
| PMC4531889 | `t recover to e−1) of 26.1 ` | oui |
| PMC4585659 | `, 1400/1450 cm−1), C=O str` | oui |
| PMC4585659 | `, 3000–3500 cm−1). In addi` | non |
| PMC4585659 | `5, and 3400 cm−1, respecti` | oui |
| PMC4585659 | `amide, 1600 cm−1), and N-H` | oui |
| PMC4585659 | `vergence of 10−5 Ha was ob` | non |
| PMC4611849 | ` (100 units·mL−1)/streptom` |  |
| PMC4611849 | `54 and 1642 cm−1 are due t` |  |
| PMC4611849 | `56 and 2932 cm−1 attribute` |  |
| PMC4611849 | `and at 1638 cm−1 is presum` |  |
| PMC4611849 | `and at 3450 cm−1 is due to` |  |
| PMC4611849 | `cin (100 mg mL−1). Culture` |  |
| PMC4611849 | `eak at 1037 cm−1 (Figure 1` |  |
| PMC4611849 | `eak at 1382 cm−1 is reduce` |  |
| PMC4611849 | `ions (50 μg·mL−1) in the s` |  |
| PMC4611849 | `peak at 672 cm−1 was attri` |  |
| PMC4611849 | `peed of 3°·min−1. Centrifu` |  |
| PMC4639843 | ` the 0.1 mg mL−1 dispersio` |  |
| PMC4639843 | ` units (cfu mL−1). All gla` |  |
| PMC4639843 | ` was 100 mW cm−2. Before c` |  |
| PMC4639843 | `000 to 3600 cm−1 with peak` |  |
| PMC4639843 | `21 and 1070 cm−1 are ascri` |  |
| PMC4639843 | `21 and 2849 cm−1 in the GO` |  |
| PMC4639843 | `27 and 1373 cm−1 correspon` |  |
| PMC4639843 | `culated k (min−1) constant` |  |
| PMC4639843 | `e of 10 °C min−1. X-ray ph` |  |
| PMC4639843 | `hB or 200 mg L−1 phenol) a` |  |
| PMC4639843 | `ith 108 cfu mL−1 E. coli o` |  |
| PMC4639843 | `mL) of 1 mg mL−1 GO-COOH s` |  |
| PMC4639843 | `red at 3423 cm−1 is attrib` |  |
| PMC4639843 | `talysts (1 g L−1) were sti` |  |
| PMC4639843 | `tants (40 mg L−1 RhB or 20` |  |
| PMC4639899 | ` E2g (1,366 cm−1), G-band ` | oui |
| PMC4639899 | ` for 2 h in 10−6 torr to i` | oui |
| PMC4639899 | ` from 10 cm2 V−1 s−1 on Si` | oui |
| PMC4639899 | ` of ∼10−5 A cm−2 is define` | oui |
| PMC4639899 | ` ∼24,000 cm2 V−1 s−1, high` | oui |
| PMC4639899 | `(near 1,366 cm−1). The Ram` | non |
| PMC4639899 | `(∼13,000 cm2 V−1 s−1) with` | oui |
| PMC4639899 | `) and 1,306 cm−1 (LO phono` | oui |
| PMC4639899 | `,000 cm2 V−1 s−1) with exf` | oui |
| PMC4639899 | `,000 cm2 V−1 s−1, higher t` | oui |
| PMC4639899 | `,000 cm2 V−1 s−1, with a p` | oui |
| PMC4639899 | `09 and 54.6e s−1, respecti` | non |
| PMC4639899 | `40 and 9 cm2 V−1 s−1, resp` | oui |
| PMC4639899 | `40 and∼9 cm2 V−1 s−1 at ro` | oui |
| PMC4639899 | `ast (30 °C min−1) and slow` | oui |
| PMC4639899 | `ast: 30 °C min−1) until 70` | oui |
| PMC4639899 | `band (1,583 cm−1) and 2D b` | oui |
| PMC4639899 | `band (2,672 cm−1) in the R` | oui |
| PMC4639899 | `density of ∼10−5 A cm−2 is` | oui |
| PMC4639899 | `m 10 cm2 V−1 s−1 on SiO2 s` | oui |
| PMC4639899 | `nd 9 cm2 V−1 s−1, respecti` | non |
| PMC4639899 | `nd∼9 cm2 V−1 s−1 at room t` | oui |
| PMC4639899 | `o 42 cm2 V−1 s−1 on h-BN s` | oui |
| PMC4639899 | `r 10,000 cm2 V−1 s−1, with` | oui |
| PMC4639899 | `s of 18,000 Nm−1 correspon` | oui |
| PMC4639899 | `slow (5 °C min−1) cooled u` | oui |
| PMC4639899 | `slow: 5 °C min−1, fast: 30` | oui |
| PMC4639899 | `te to 42 cm2 V−1 s−1 on h-` | oui |
| PMC4639899 | `was ∼2–4 MV cm−1, which is` | oui |
| PMC4645124 | `40 and 1355 cm−1, presenti` | oui |
| PMC4645124 | `500 to 2500 cm−1 on a Reni` | non |
| PMC4645124 | `eaks at 220 cm−1 and 295 c` | non |
| PMC4645124 | `g 28 and 13 cm−1 downshift` | oui |
| PMC4645124 | `m−1 and 295 cm−1 ascribed ` | non |
| PMC4645124 | `ted at 1367 cm−1, which ca` | oui |
| PMC4726031 | ` and 13.15 m2g–1, respecti` | oui |
| PMC4726031 | `1 from 1022 cm−1, providin` | oui |
| PMC4726031 | `471 and 518 cm−1 could be ` | non |
| PMC4726031 | `485 and1384 cm−1 were ascr` | non |
| PMC4726031 | `Si–O at 471 cm−1 and the s` | non |
| PMC4726031 | `and at 3402 cm−1 was attri` | non |
| PMC4726031 | `and at 3453 cm−1 could be ` | non |
| PMC4726031 | `and at 3620 cm−1 assigned ` | non |
| PMC4726031 | `and at 3620 cm−1 was assig` | non |
| PMC4726031 | `etween 4000 cm−1 and 400 c` | non |
| PMC4726031 | `i–O at 1022 cm−1 indicated` | non |
| PMC4726031 | `m−1 and 400 cm−1 on a Nico` | non |
| PMC4726031 | `ted to 1035 cm−1 from 1022` | oui |
| PMC4726031 | `tion at 559 cm−1 appeared ` | oui |
| PMC4726031 | `ved at 1637 cm−1. Meanwhil` | non |
| PMC4726093 | `d from 19 m2·g−1 to 41 m2·` | non |
| PMC4726093 | `g−1 to 41 m2·g−1 with the ` | non |
| PMC4726093 | `ocity of 424 h−1, suggesti` | non |
| PMC4726093 | `rea is 15 m2·g−1 for the L` | non |
| PMC4735866 | ` 22,000 M−1 cm−1. Protein ` | non |
| PMC4735866 | ` and 1547.0 cm−1 in the Am` | non |
| PMC4735866 | `e 1400–2000 cm−1 region af` | non |
| PMC4735866 | `e 1600–1700 cm−1 region (m` | non |
| PMC4735866 | `f 1400–1700 cm−1 (Fig. 5B)` | non |
| PMC4735866 | `m 1500–1600 cm−1 (C–N stre` | non |
| PMC4735866 | `nt of 22,000 M−1 cm−1. Pro` | non |
| PMC4735866 | `of 600–4000 cm−1 using a P` | non |
| PMC4829567 | ` about 1593 cm−1 (G band) ` | oui |
| PMC4829567 | `61 and 1067 cm−1 are assig` | non |
| PMC4829567 | `780 and 546 cm−1, which ar` | oui |
| PMC4829567 | `O–H at 1177 cm−1 covers th` | oui |
| PMC4829567 | `d) and 1357 cm−1 (D band),` | oui |
| PMC4829567 | `ets at 1620 cm−1 due to th` | non |
| PMC4829567 | `ion at 3400 cm−1 is attrib` | non |
| PMC4829567 | `one at 1410 cm−1, is attri` | non |
| PMC4829567 | `oup at 1067 cm−1 in ZHS/GO` | non |
| PMC4923881 | ` below 1000 cm−1), which a` | non |
| PMC4923881 | `400 to 4000 cm−1 in diffus` | non |
| PMC4923881 | `ange of 400 cm−1 to 4000 c` | non |
| PMC4923881 | `between 500 cm−1 to 590 cm` | oui |
| PMC4923881 | `cm−1 to 590 cm−1, which co` | oui |
| PMC4923881 | `e 1610–1630 cm−1 band is d` | non |
| PMC4923881 | `e 3000–3650 cm−1 band is d` | non |
| PMC4923881 | `ear 3492.95 cm−1 correspon` | non |
| PMC4923881 | `lution of 4 cm−1 in the fr` | non |
| PMC4923881 | `m−1 to 4000 cm−1 for thorn` | non |
| PMC4923881 | `peak at 758 cm−1 can be at` | non |
| PMC4951059 | `3,000–3,800 cm−1 is due to` | oui |
| PMC4951059 | `ak at 1,082 cm−1 was shift` | oui |
| PMC4951059 | `ed to 1,073 cm−1, due to t` | oui |
| PMC4951059 | `f 4,000–400 cm−1, using a ` | non |
| PMC4951059 | `lution of 4 cm−1.SEM imagi` | non |
| PMC4951059 | `nd at 1,082 cm−1 show a st` | oui |
| PMC4951059 | `nd at 1,082 cm−1 with a sh` | oui |
| PMC4951059 | `nd at 1,644 cm−1 is relate` | oui |
| PMC4951059 | `nd near 800 cm−1, which ca` | oui |
| PMC4951059 | `peak at 464 cm−1, which is` | oui |
| PMC4951059 | `r at ~1,200 cm−1 is in the` | oui |
| PMC4957122 | `01 and 1440 cm−1) are clea` | oui |
| PMC4957122 | `35 and 1367 cm−1 were assi` | oui |
| PMC4957122 | `35 and 3265 cm−1 related t` | oui |
| PMC4957122 | `42 and 1601 cm−1 are assoc` | oui |
| PMC4957122 | `42 and 1601 cm−1 could be ` | oui |
| PMC4957122 | `45 and 1115 cm−1) and ioni` | oui |
| PMC4957122 | `SV of 64,000 h−1. The comp` | non |
| PMC4957122 | `ecies (1560 cm−1), then pr` | oui |
| PMC4957122 | `ity of 64000 h−1 are shown` | non |
| PMC4957122 | `lution of 4 cm−1. The cont` | non |
| PMC4957122 | `ws: 100 mL min−1 total flo` | oui |
| PMC4961655 | ` around 500 cm−1 indicatin` | oui |
| PMC4961655 | `6 × 10−3 g mol−1 min−1 as ` | oui |
| PMC4961655 | `6 × 10−3 g mol−1 min−1. Th` | oui |
| PMC4961655 | `62 and 1343 cm−1, respecti` | oui |
| PMC4961655 | `7 × 10−2 g mol−1 min−1 and` | oui |
| PMC4961655 | `7 × 10−3 g mol−1 min−1, wh` | oui |
| PMC4961655 | `7 × 10−3 g mol−1 min−1. Ho` | oui |
| PMC4961655 | `e was 1.7 × 10−3 g mol−1 m` | oui |
| PMC4961655 | `eak at 1224 cm−1 indicatin` | oui |
| PMC4961655 | `eak at 3450 cm−1 confirmed` | oui |
| PMC4961655 | `luene 5.6 × 10−3 g mol−1 m` | oui |
| PMC4961655 | `luene 5.6 × 10−3 g mol−1 m` | oui |
| PMC4961655 | `ol is 1.7 × 10−2 and tolue` | non |
| PMC4961655 | `ol is 1.7 × 10−2 g mol−1 m` | oui |
| PMC4961655 | `on is 1.7 × 10−3 g mol−1 m` | oui |
| PMC4961655 | `red at 1739 cm−1 suggestin` | oui |
| PMC4961655 | `−2 g mol−1 min−1 and tolue` | oui |
| PMC4961655 | `−3 g mol−1 min−1 as shown ` | oui |
| PMC4961655 | `−3 g mol−1 min−1, while at` | oui |
| PMC4961655 | `−3 g mol−1 min−1. However,` | non |
| PMC4961655 | `−3 g mol−1 min−1. The rate` | non |
| PMC4973716 | ` dilutions (10−4, 10−5, 10` | non |
| PMC4973716 | `, 10−6, and 10−7) was inje` | non |
| PMC4973716 | `10−2 mg/mL, 10−1 mg/mL, 10` | oui |
| PMC4973716 | `10−3 mg/mL, 10−2 mg/mL, 10` | oui |
| PMC4973716 | `10−4, 10−5, 10−6, and 10−7` | non |
| PMC4973716 | `ions (10−4, 10−5, 10−6, an` | non |
| PMC4973716 | `s of AgNPs (10−3 mg/mL, 10` | oui |
| PMC4976354 | ` (34.00 μmol g−1) compared` |  |
| PMC4976354 | ` BCN (2.29 min−1) and the ` |  |
| PMC4976354 | ` HCN (3.35 min−1) and NCN ` |  |
| PMC4976354 | ` at ca. 880 cm−1 was assig` |  |
| PMC4976354 | `0 mL, 3.2 mg L−1) in a bat` |  |
| PMC4976354 | `BCN (7.46 m2 g−1). This co` |  |
| PMC4976354 | `CN (15.95 m2 g−1), NCN (58` |  |
| PMC4976354 | `CN (32.05 m2 g−1) samples ` |  |
| PMC4976354 | `CN (58.82 m2 g−1), and SCN` |  |
| PMC4976354 | `N (1.26 μmol g−1) and the ` |  |
| PMC4976354 | `N (5.54 μmol g−1) and NCN ` |  |
| PMC4976354 | `N (6.80 μmol g−1) were hig` |  |
| PMC4976354 | `NCN (7. 95 min−1). It was ` |  |
| PMC4976354 | `and at 3500 cm−1 was assig` |  |
| PMC4976354 | `ant (15.61 min−1), which w` |  |
| PMC4976354 | `band at 810 cm−1 correspon` |  |
| PMC4976354 | `der (0.1 mg mL−1) was disp` |  |
| PMC4976354 | `f 1200–1650 cm−1 correspon` |  |
| PMC4976354 | `lution of 1 cm−1 with KBr ` |  |
| PMC4976354 | `r was 73 mW cm−2 at the po` |  |
| PMC4976354 | `s (1.49 μmol g−1, Figure S` |  |
| PMC5028751 | ` and 2.35 × 10−2 min−1 for` | oui |
| PMC5028751 | ` band (1343 cm−1) is corre` | non |
| PMC5028751 | ` band (1586 cm−1) is attri` | non |
| PMC5028751 | `.35 × 10−2 min−1 for Cr(VI` | oui |
| PMC5028751 | `.47 × 10−2 min−1 for Rh B ` | oui |
| PMC5028751 | `00} > 0.44 J m−2 for {101}` | non |
| PMC5028751 | `01} > 0.53 J m−2 for {100}` | non |
| PMC5028751 | `18, and 639 cm−1, which ca` | non |
| PMC5028751 | `O2 is 0.90 J m−2 for {001}` | non |
| PMC5028751 | `around 1343 cm−1 (for D ba` | non |
| PMC5028751 | `d) and 1586 cm−1 (for G ba` | non |
| PMC5028751 | `i.e. 4.47 × 10−2 min−1 for` | oui |
| PMC5075927 | `e 2950–2820 cm−1 peaks are` |  |
| PMC5075927 | `e 3300–3000 cm−1 broad str` |  |
| PMC5075927 | `lution of 2 cm−1 by using ` |  |
| PMC5075927 | `n 3600–3800 cm−1 from Figu` |  |
| PMC5075927 | `t 1440–1360 cm−1 is assign` |  |
| PMC5075927 | `t 1730–1630 cm−1 correspon` |  |
| PMC5080270 | `-3~1.75 ×10-3s−1) than tho` | non |
| PMC5080270 | `10−3~1.73 × 10−3 s−1). The` | oui |
| PMC5080270 | `10−3~2.21 × 10−3 s−1) were` | oui |
| PMC5080270 | `46, and 667 cm−1. The char` | non |
| PMC5080270 | `51, and 669 cm−1, whereas ` | non |
| PMC5080270 | `60 and 1046 cm−1 in AC-AuN` | non |
| PMC5080270 | `NPs (1.07 × 10−3~1.73 × 10` | oui |
| PMC5080270 | `NPs (1.44 × 10−3~2.21 × 10` | oui |
| PMC5080270 | `act at 3268 cm−1 []. This ` | non |
| PMC5080270 | `eak at 1725 cm−1 in the AC` | non |
| PMC5080270 | `red at 2917 cm−1 in the sp` | non |
| PMC5080270 | `ted to 2935 cm−1 after the` | non |
| PMC5080270 | `ted to 3318 cm−1 in AC-AuN` | non |
| PMC5080270 | `ups at 1725 cm−1 in AC-AuN` | non |
| PMC5080270 | `wer (0.038 ×10-3~1.75 ×10-` | non |
| PMC5080270 | `~1.73 × 10−3 s−1). The rat` | non |
| PMC5080270 | `~2.21 × 10−3 s−1) were hig` | oui |
| PMC5080270 | `×10-3~1.75 ×10-3s−1) than ` | non |
| PMC5099674 | ` (0.0844 mol L−1) was adde` |  |
| PMC5099674 | ` and 100 μg mL−1 of strept` |  |
| PMC5099674 | ` at 6.4 mmol L−1), the inc` |  |
| PMC5099674 | `, 0.0844 mol L−1). Fresh N` |  |
| PMC5099674 | `FBS), 100 U mL−1 of penici` |  |
| PMC5099674 | `Se (136 kJ mol−1) is relat` |  |
| PMC5099674 | `Se (136 kJ mol−1) than tha` |  |
| PMC5099674 | `Se (310 kJ mol−1) [], Cd2+` |  |
| PMC5099674 | `Se (310 kJ mol−1) [], we p` |  |
| PMC5099674 | `] = 6.4 mmol L−1, molar ra` |  |
| PMC5099674 | `] = 6.4 mmol L−1, molar ra` |  |
| PMC5099674 | `] = 6.4 mmol L−1, molar ra` |  |
| PMC5099674 | `ate in 1 mol L−1 H2SO4 aqu` |  |
| PMC5099674 | `er (0.05 mol L−1, pH = 10)` |  |
| PMC5099674 | `ion (0.5 mg mL−1, final co` |  |
| PMC5099674 | `l2 (0.05 mol L−1) were inj` |  |
| PMC5099674 | `l2 (6.4 mmol L−1) and a ce` |  |
| PMC5099674 | `n of 1.0 mol L−1 of NaOH. ` |  |
| PMC5099674 | `was 6.4 mmol L−1 in a tota` |  |
| PMC5101912 | `.05 kJ mol–1 K–1) indicate` | oui |
| PMC5101912 | `04X1020 M–1 cm–1 nm4) of t` | oui |
| PMC5101912 | `40 and 1580 cm–1, which ca` | non |
| PMC5101912 | `6, and 1411 cm–1 correspon` | non |
| PMC5101912 | `7 and 5 μmol g–1 respectiv` | oui |
| PMC5101912 | `87 and 1287 cm–1 are attri` | non |
| PMC5101912 | `and at 1725 cm–1 correspon` | oui |
| PMC5101912 | `ate of 0.02° S–1 using a P` | non |
| PMC5101912 | `e (0.05 kJ mol–1 K–1) indi` | oui |
| PMC5101912 | `e (8.72 kJ mol–1) indicate` | oui |
| PMC5101912 | `e 17.45 kJ mol–1. A low ac` | non |
| PMC5101912 | `eak at 1065 cm–1 originate` | non |
| PMC5101912 | `eak at 1228 cm–1 is attrib` | non |
| PMC5101912 | `ed at 1 ml min–1 and each ` | oui |
| PMC5101912 | `ent (0.5 mg ml–1) were add` | oui |
| PMC5101912 | `ge 150–3400 cm–1. Zeta pot` | non |
| PMC5101912 | `he GO (1 mg ml–1) was then` | oui |
| PMC5101912 | `o 20.60 μmol g–1 as the te` | oui |
| PMC5101912 | `ted at 2632 cm–1, indicati` | oui |
| PMC5101912 | `to 17.2 μmol g–1 occurs wi` | oui |
| PMC5101912 | `water (1 mg ml–1). The des` | non |
| PMC5101912 | `y (< 40 kJ mol–1) implies ` | oui |
| PMC5101912 | `y (> 40 kJ mol–1) correspo` | non |
| PMC5101912 | `y, q e (μmol g–1) can be c` | non |
| PMC5101912 | `λ)=2.04X1020 M–1 cm–1 nm4)` | oui |
| PMC5122874 | `ange of 5 × 10−10 Torr. The` | oui |
| PMC5122874 | `stant of 12 nm−1. Powder X` | non |
| PMC5238663 | ` (200000 cm2·V−1·s−1), whi` | non |
| PMC5238663 | ` (5000 W·m−1·K−1) []. Its ` | non |
| PMC5238663 | ` cm−1, 1229 cm−1 and 1725 ` | oui |
| PMC5238663 | `0000 cm2·V−1·s−1), which m` | non |
| PMC5238663 | `1.5, 100 mW·cm−2) having a` | non |
| PMC5238663 | `500 and 600 cm−1. The peak` | oui |
| PMC5238663 | `]. The 1404 cm−1 peak corr` | non |
| PMC5238663 | `aks at 1032 cm−1, 1229 cm−` | oui |
| PMC5238663 | `aks at 3309 cm−1 and 1404 ` | non |
| PMC5238663 | `and at 3454 cm−1 and 1424 ` | oui |
| PMC5238663 | `eak at 1394 cm−1 in the bi` | oui |
| PMC5238663 | `eak at 1550 cm−1 is attrib` | oui |
| PMC5238663 | `eak at 1622 cm−1 could be ` | non |
| PMC5238663 | `ears at 504 cm−1 []. FTIR ` | non |
| PMC5238663 | `f 3000–3500 cm−1 range and` | oui |
| PMC5238663 | `rate of 2°·min−1.Results a` | non |
| PMC5238663 | `rea (2630 m2·g−1) [], chem` | non |
| PMC5238663 | `rly at 1725 cm−1 are weake` | oui |
| PMC5238663 | `tion of MO (10−5 M). Initi` | oui |
| PMC5238663 | `vity (5000 W·m−1·K−1) []. ` | non |
| PMC5238663 | `−1 and 1404 cm−1, which co` | non |
| PMC5238663 | `−1 and 1424 cm−1 could be ` | oui |
| PMC5238663 | `−1 and 1725 cm−1 are the c` | oui |
| PMC5302706 | `540 and 579 cm−1 are denot` | oui |
| PMC5302706 | `ange of 2–5 cm−1) caused b` | non |
| PMC5302706 | `r nB = 1016 cm−3.The condu` | non |
| PMC5302706 | `r nB = 1017 cm−3; λD = 10 ` | non |
| PMC5302706 | `r nB = 1018 cm−3; λD = 3 n` | non |
| PMC5304159 | ` 1.2 × 1015 cm−3, respecti` |  |
| PMC5304159 | `accuracy of 10−12 A, and th` |  |
| PMC5304159 | `accuracy of 10−4 g, and we` |  |
| PMC5304159 | `les (0.026 min−1). Some re` |  |
| PMC5304631 | ` = 5.41× 108·M−1·cm−1 []. ` | non |
| PMC5304631 | `41× 108·M−1·cm−1 []. For t` | non |
| PMC5304631 | `han 18.2 mΩ·cm−1 was used ` | oui |
| PMC5309769 | ` 0.6–0.3 eV ps−1 until Tc ` | non |
| PMC5309769 | ` 1.5 × 1019 cm-3). For bot` | non |
| PMC5309769 | ` 3.5 × 1018 cm−3). This la` | non |
| PMC5309769 | ` 5.5 × 1018 cm−3 and exces` | non |
| PMC5309769 | ` 6.0 × 1018 cm−3 and exces` | non |
| PMC5309769 | ` 6.5 × 1018 cm−3.Intrinsic` | non |
| PMC5309769 | ` around 150 cm−1 (assigned` | oui |
| PMC5309769 | `1–15 × 1018 cm−3. These li` | non |
| PMC5309769 | `d under 1 × 10−9 torr. Al ` | non |
| PMC5309769 | `ds) and 300 cm−1 (which co` | non |
| PMC5309769 | `f 0.1–0.2 nm s−1.CdSe NCsC` | non |
| PMC5309769 | `f 15 × 1018 cm−3. In fact,` | non |
| PMC5309769 | `nd 0.008 eV ps−1 at <N0> a` | non |
| PMC5309769 | `ound 0.3 eV ps−1, whereas ` | non |
| PMC5309769 | `pressure of 10−6 torr. Bph` | oui |
| PMC5309769 | `rder of 150 cm−1 and/or th` | oui |
| PMC5309769 | `uene (10 mg ml−1) was spin` | oui |
| PMC5327880 | `1 and 2,860 cm−1 correspon` | non |
| PMC5327880 | `1,456–1,210 cm−1 are assoc` | non |
| PMC5327880 | `band at 898 cm−1 could be ` | non |
| PMC5327880 | `ds at 2,918 cm−1 and 2,860` | non |
| PMC5327880 | `ed at 1,058 cm−1. The band` | non |
| PMC5327880 | `f 4,000–400 cm−1. Pellets ` | non |
| PMC5327880 | `nd at 1,630 cm−1 is due to` | non |
| PMC5327880 | `on at 3,365 cm−1 with a sh` | non |
| PMC5364236 | ` low as 103 cm−1. Based on` | non |
| PMC5364236 | `(D = 11.4 × 10−10 m2 s−1) w` | oui |
| PMC5364236 | `(D = 17.9 × 10−10 m2 s−1) a` | oui |
| PMC5364236 | `0, and 3303 cm−1 are δ(NH2` | non |
| PMC5364236 | `00 and 2100 cm−1 originate` | non |
| PMC5364236 | `1, and 1386 cm−1, which ar` | non |
| PMC5364236 | `10 and 1407 cm−1, ascribed` | non |
| PMC5364236 | `10, and 937 cm−1 due to C–` | non |
| PMC5364236 | `18 and 2850 cm−1, respecti` | non |
| PMC5364236 | `19 and 1422 cm−1, respecti` | oui |
| PMC5364236 | `2 × 10−10 m2 s−1 and D = 3` | oui |
| PMC5364236 | `299 to 1407 cm−1. Diminish` | non |
| PMC5364236 | `4 × 10−10 m2 s−1) were sig` | oui |
| PMC5364236 | `400 to 2200 cm−1 and origi` | non |
| PMC5364236 | `52 and 2871 cm−1 assigned ` | non |
| PMC5364236 | `6, and 1546 cm−1 character` | non |
| PMC5364236 | `9 × 10−10 m2 s−1) and OctA` | oui |
| PMC5364236 | `9 × 10−10 m2 s−1. Such obs` | non |
| PMC5364236 | `CH2) at 722 cm−1. The spec` | non |
| PMC5364236 | `C═O at 1699 cm−1 and hydro` | non |
| PMC5364236 | `H2) at 1468 cm−1, and meth` | non |
| PMC5364236 | `NH2) = 3253 cm−1) N–H stre` | non |
| PMC5364236 | `NH2) = 3330 cm−1) and symm` | non |
| PMC5364236 | `and at 1397 cm−1. A low-in` | non |
| PMC5364236 | `and at 1528 cm−1 is ascrib` | non |
| PMC5364236 | `and at 1606 cm−1 are also ` | non |
| PMC5364236 | `and at 1642 cm−1 for both ` | non |
| PMC5364236 | `and at 2202 cm−1. Moreover` | non |
| PMC5364236 | `d D = 3.9 × 10−10 m2 s−1. S` | oui |
| PMC5364236 | `e (Δν = 103 cm−1) to chela` | non |
| PMC5364236 | `e (Δν = 135 cm−1) (Nelson ` | non |
| PMC5364236 | `e (Δν = 159 cm−1). This wa` | non |
| PMC5364236 | `e below 110 cm−1 would hav` | non |
| PMC5364236 | `fts to 1510 cm−1 while the` | non |
| PMC5364236 | `lution of 4 cm−1. Extincti` | non |
| PMC5364236 | `ncy at 1696 cm−1 (C═O bond` | non |
| PMC5364236 | `om Δν = 397 cm−1 for LAc t` | non |
| PMC5364236 | `oup at 1299 cm−1. It is wo` | non |
| PMC5364236 | `oup at 1699 cm−1 in the H-` | non |
| PMC5364236 | `to Δν = 103 cm−1 for DDA[L` | non |
| PMC5364236 | `uency (1392 cm−1) shifted ` | non |
| PMC5364236 | `uency (1551 cm−1) and low ` | non |
| PMC5364236 | `y D = 7.2 × 10−10 m2 s−1 an` | oui |
| PMC5369406 | ` 1 or 5 °C min–1) in a flo` |  |
| PMC5369406 | ` 16 to 56 m2 g–1 after cal` |  |
| PMC5369406 | ` and at 836 cm–1 for the ν` |  |
| PMC5369406 | `) kg(CuO/ZnO) –1 as compar` |  |
| PMC5369406 | `) kg(CuO/ZnO) –1 for the b` |  |
| PMC5369406 | `/Ar (30 ml min–1) with hea` |  |
| PMC5369406 | `0 °C, 1 °C min–1, 4 h) and` |  |
| PMC5369406 | `0 °C, 1 °C min–1, 4 h), pe` |  |
| PMC5369406 | `0.5 ≤ Q ≤ 22 Å–1) was proc` |  |
| PMC5369406 | `3.92 molMeOH h–1 kgcat –1 ` |  |
| PMC5369406 | `35 and 27 m2 g–1 respectiv` |  |
| PMC5369406 | `5.43 molMeOH h–1 kgcat –1 ` |  |
| PMC5369406 | `617 and 678 cm–1, assigned` |  |
| PMC5369406 | `75 and 1408 cm–1 for the ν` |  |
| PMC5369406 | `771 and 724 cm–1 correspon` |  |
| PMC5369406 | `934 and 938 cm–1, which ar` |  |
| PMC5369406 | `C (at 5 °C min–1) using ca` |  |
| PMC5369406 | `C at 10 °C min–1, and then` |  |
| PMC5369406 | `C at 10 °C min–1, before h` |  |
| PMC5369406 | `CO2 (50 ml min–1) for 30 m` |  |
| PMC5369406 | `air (50 ml min–1). TGA and` |  |
| PMC5369406 | `eOH h–1 kgcat –1 at 190 °C` |  |
| PMC5369406 | `eOH h–1 kgcat –1 at 205 °C` |  |
| PMC5369406 | `eak at 1049 cm–1 for the ν` |  |
| PMC5369406 | `ge 400–4000 cm–1. Raman sp` |  |
| PMC5369406 | `ied at 1091 cm–1 from the ` |  |
| PMC5369406 | `ium (80 ml min–1).For cata` |  |
| PMC5369406 | `l%) at 3.5 L h–1, 25 bar p` |  |
| PMC5369406 | `m 3 to 21 m2 g–1 (Table 4)` |  |
| PMC5369406 | `m 6 to 16 m2 g–1 due to th` |  |
| PMC5369406 | `red at 3419 cm–1 is associ` |  |
| PMC5369406 | `ure (60 ml min–1). Methano` |  |
| PMC5369406 | `°C at 1 °C min–1 using a 2` |  |
| PMC5369406 | `°C at 1 °C min–1. For Cu s` |  |
| PMC5371968 | `80 and 1620 cm−1; Figure S` |  |
| PMC5371968 | `STP) cm·cm−2·s−1·cm·Hg−1],` |  |
| PMC5371968 | `[1 Barrer = 10−1 cm3(STP) ` |  |
| PMC5371968 | `around 2220 cm−1, which im` |  |
| PMC5371968 | `around 3100 cm−1, assigned` |  |
| PMC5371968 | `cm3(STP) cm·cm−2·s−1·cm·Hg` |  |
| PMC5371968 | `cm−2·s−1·cm·Hg−1], and the` |  |
| PMC5371968 | `ge 4000–500 cm−1.3.2.2. Pu` |  |
| PMC5371968 | `ion of 0.25 cm−1, a sensit` |  |
| PMC5376314 | `00 and 3100 cm−1 can be at` | non |
| PMC5376314 | `8, and 1059 cm−1. The smal` | non |
| PMC5376314 | `ge 380−4000 cm−1.3.Results` | non |
| PMC5376314 | `h) and 1060 cm−1 (asymmetr` | oui |
| PMC5376314 | `peak at 620 cm−1 should co` | non |
| PMC5407272 | ` area: 36 m2 g–1, cat. no.` | oui |
| PMC5407272 | `: 0.026 mmol g–1, Pd: 0.04` | oui |
| PMC5407272 | `: 0.031 mmol g–1, Pd: 0.18` | oui |
| PMC5407272 | `: 0.046 mmol g–1), Au–Pd/T` | oui |
| PMC5407272 | `: 0.048 mmol g–1, d av: 6.` | oui |
| PMC5407272 | `: 0.062 mmol g–1, d av: 5.` | oui |
| PMC5407272 | `: 0.074 mmol g–1, Pd: 0.06` | oui |
| PMC5407272 | `: 0.078 mmol g–1, Pd: 0.14` | oui |
| PMC5407272 | `: 0.086 mmol g–1, d av: 3.` | oui |
| PMC5407272 | `: 0.090 mmol g–1, d av: 3.` | oui |
| PMC5407272 | `: 0.111 mmol g–1, Pd: 0.09` | oui |
| PMC5407272 | `: 0.128 mmol g–1, Pd: 0.08` | oui |
| PMC5407272 | `: 0.144 mmol g–1), Au–Pd/T` | oui |
| PMC5407272 | `: 0.149 mmol g–1, d av: 1.` | oui |
| PMC5407272 | `: 0.150 mmol g–1, Pd: 0.04` | oui |
| PMC5407272 | `: 0.188 mmol g–1), and oth` | oui |
| PMC5407272 | `: 0.250 mmol g–1, d av: 2.` | oui |
| PMC5407272 | `area: 111 m2 g–1, cat. no.` | oui |
| PMC5407272 | `area: 160 m2 g–1, cat. no.` | oui |
| PMC5407272 | `area: 274 m2 g–1, cat. no.` | oui |
| PMC5407272 | `area: 316 m2 g–1, cat. no.` | oui |
| PMC5407272 | `d 0.095 mmol g–1, respecti` | oui |
| PMC5407272 | `e 0.134 mmol g–1 and 0.095` | oui |
| PMC5438438 | `, 1640–1660 cm−1 correspon` | oui |
| PMC5448492 | ` at 2.0 °C min−1 up to 800` | oui |
| PMC5448492 | `300 and 580 cm−1. It is ob` | non |
| PMC5448492 | `76 and 1083 cm−1 at 500 an` | oui |
| PMC5448492 | `and at 1067 cm−1 for the u` | oui |
| PMC5448492 | `and at ~960 cm−1 associate` | non |
| PMC5448492 | `ands at 800 cm−1 and 1076 ` | non |
| PMC5448492 | `around 1080 cm−1, assigned` | non |
| PMC5448492 | `e of 80 mL min−1.4. Conclu` | non |
| PMC5448492 | `gion of 960 cm−1 is assign` | non |
| PMC5448492 | `nds at ~490 cm−1 region as` | oui |
| PMC5448492 | `of 1300–580 cm−1. Thermogr` | non |
| PMC5448492 | `r near 1200 cm−1 correspon` | non |
| PMC5448492 | `rved at 667 cm−1. This ban` | non |
| PMC5448492 | `tes 1.5 °C min−1 to 500 °C` | oui |
| PMC5448492 | `−1 and 1076 cm−1 with a sh` | non |
| PMC5451797 | `00 and 1024 cm−1, respecti` | non |
| PMC5451797 | `446 and 610 cm−1 are assig` | oui |
| PMC5451797 | `5 G (100 mW cm−2). Before ` | non |
| PMC5451797 | `NWs at 1648 cm−1 associate` | oui |
| PMC5451797 | `and at 1355 cm−1 correspon` | non |
| PMC5451797 | `and at 1587 cm−1 attribute` | non |
| PMC5451797 | `ate is 0.5 V s−1 with 3500` | oui |
| PMC5451797 | `eak at 3369 cm−1 was attri` | non |
| PMC5451797 | `r (18 M ohm cm−1, 30 ml) a` | oui |
| PMC5451797 | `rode (25 µA cm−2). From fi` | non |
| PMC5451797 | `y of 160 μA cm−2 at 0 V ve` | oui |
| PMC5451797 | `y, 1.25 ohm cm−1; hardness` | oui |
| PMC5452327 | `4000 to 400 cm−1 at a reso` | oui |
| PMC5452327 | `and at 1400 cm−1, which re` | oui |
| PMC5452327 | `and at 3424 cm−1 and the b` | oui |
| PMC5452327 | `lution of 4 cm−1. The spec` | non |
| PMC5452327 | `nd at ~1600 cm−1, which is` | oui |
| PMC5452327 | `nds at 1055 cm−1 and 1230 ` | oui |
| PMC5452327 | `nds at 1720 cm−1 and 1380 ` | oui |
| PMC5452327 | `peak at 568 cm−1 that prov` | oui |
| PMC5452327 | `−1 and 1230 cm−1 can be at` | oui |
| PMC5452327 | `−1 and 1380 cm−1 as the st` | oui |
| PMC5452520 | ` around 7 m2 g−1. Small BE` | non |
| PMC5452520 | ` to 3.19 cm3 g−1 when the ` | oui |
| PMC5452520 | `% and 0.3 g cm−3 achieved ` | non |
| PMC5452520 | `, and 1.6 × 10−3, respecti` | oui |
| PMC5452520 | `10−4, 1.4 × 10−3, and 1.6 ` | oui |
| PMC5452520 | `10−4, 4.9 × 10−4, 7.2 × 10` | oui |
| PMC5452520 | `10−4, 7.2 × 10−4, 1.4 × 10` | oui |
| PMC5452520 | `5 to 3.5 mol L−1 by solven` | oui |
| PMC5452520 | `and 0.51 cm3 g−1 to 1.31 μ` | oui |
| PMC5452520 | `and 0.71 cm3 g−1 for 5% an` | oui |
| PMC5452520 | `d at 10 °C min−1 under a f` | oui |
| PMC5452520 | `ies (0.28 g cm−3) were obs` | non |
| PMC5452520 | `ity (~0.3 g cm−3) were obs` | non |
| PMC5452520 | `me (0.80 cm3 g−1) was obse` | non |
| PMC5452520 | `me (3.19 cm3 g−1) was obta` | non |
| PMC5452520 | `n (100 cm3 min−1) and the ` | oui |
| PMC5452520 | `n of 2.0 cm3 g−1 (Figure 2` | oui |
| PMC5452520 | `ns of 3.4 × 10−4, 4.9 × 10` | oui |
| PMC5452520 | `of a 1.5 mol L−1 zirconium` | oui |
| PMC5452520 | `to a 1.5 mol L−1 sulfuric ` | oui |
| PMC5452520 | `und 0.70 cm3 g−1 (Figure 2` | oui |
| PMC5456199 | ` about 1008 cm−1 is due to` |  |
| PMC5456199 | ` about 3440 cm−1 and the b` |  |
| PMC5456199 | `around 1650 cm−1 in the as` |  |
| PMC5456199 | `dge at 1163 cm−1 and ring ` |  |
| PMC5456199 | `e of 10 °C min−1. The part` |  |
| PMC5456199 | `eometry at 1 s−1 for the v` |  |
| PMC5456199 | `hing at 896 cm−1. These va` |  |
| PMC5456199 | `ing at 1375 cm−1, C–O stre` |  |
| PMC5456199 | `ing at 1440 cm−1, CH3 symm` |  |
| PMC5456199 | `ing at 3447 cm−1, –CH3 str` |  |
| PMC5456199 | `nit at 1643 cm−1, C–OH in-` |  |
| PMC5456199 | `nit at 2860 cm−1, C–O carb` |  |
| PMC5456199 | `nit at 2962 cm−1, –CH2– st` |  |
| PMC5456199 | `nts (Dc/rc2, s−1, where Dc` |  |
| PMC5456199 | `of 4000–400 cm−1.The zeta ` |  |
| PMC5456199 | `t about 452 cm−1 are due t` |  |
| PMC5456199 | `vacuum (1 × 10−4 Pa) for 1` |  |
| PMC5465224 | ` and 524.6 F g−1 at 1, 2, ` | oui |
| PMC5465224 | ` and 524.6 F g−1 at a lowe` | oui |
| PMC5465224 | ` g−1 to 20 A g−1. Pronounc` | non |
| PMC5465224 | ` of 1173.8 F g−1 and 524.6` | non |
| PMC5465224 | `10, and 20 A g−1, respecti` | oui |
| PMC5465224 | `ate of 10 mV s−1 are shown` | non |
| PMC5465224 | `cy range of 10−2 to 105 Hz` | oui |
| PMC5465224 | `e of 1.33 × 10−6 Pa. Morph` | oui |
| PMC5465224 | `ies from 1 A g−1 to 20 A g` | non |
| PMC5465224 | `nsity of 1 A g−1 and a hig` | non |
| PMC5465224 | `nsity of 5 A g−1, and the ` | non |
| PMC5465224 | `nsity of 5 A g−1. The meth` | non |
| PMC5465224 | `rate of 4° min−1. X-ray ph` | non |
| PMC5465224 | `s from 10 mV s−1 to 50 mV ` | non |
| PMC5465224 | `sity of 20 A g−1, respecti` | oui |
| PMC5465224 | `s−1 to 50 mV s−1 and the r` | non |
| PMC5466191 | `aks at 1637 cm−1 and 1151 ` | non |
| PMC5466191 | `eak at 3016 cm−1 that corr` | oui |
| PMC5466191 | `eak of 1631 cm−1 .Our find` | non |
| PMC5466191 | `eak of 1631 cm−1 correspon` | oui |
| PMC5466191 | `f 3000–3400 cm−1 is the su` | non |
| PMC5466191 | `ine (ϵ = 65 mM−1 cm−1), 50` | non |
| PMC5466191 | `roups, 3016 cm−1 peak corr` | non |
| PMC5466191 | `ϵ = 65 mM−1 cm−1), 50 mM p` | non |
| PMC5466191 | `−1 and 1151 cm−1 arise fro` | non |
| PMC5515720 | ` and 1000 mA g−1, respecti` |  |
| PMC5515720 | ` and 220 mAh g−1 at curren` |  |
| PMC5515720 | ` of 1965 mAh g−1 and a low` |  |
| PMC5515720 | `40 and 1595 cm−1, related ` |  |
| PMC5515720 | `Cl (0.1 mol dm−3) were dis` |  |
| PMC5515720 | `bout 333 mAh g−1 at the 40` |  |
| PMC5515720 | `bout 615 mAh g−1, and this` |  |
| PMC5515720 | `bout 991 mAh g−1 while a c` |  |
| PMC5515720 | `ed to 100 mA g−1, about 95` |  |
| PMC5515720 | `low (30 ml min−1).The work` |  |
| PMC5515720 | `ng of ~4 mg cm−2. The coin` |  |
| PMC5515720 | `only 372 mAh g−1, which ca` |  |
| PMC5515720 | `round 95 mAh g−1 when cycl` |  |
| PMC5515720 | `te of 0.1 mV s−1 and elect` |  |
| PMC5515720 | `ty of 100 mA g−1. It is ob` |  |
| PMC5515720 | `y of 1000 mA g−1, presenti` |  |
| PMC5515720 | `y of 215 mAh g−1 at a high` |  |
| PMC5515720 | `y of 557 mAh g−1 after 40 ` |  |
| PMC5515720 | `y of 744 mAh g−1 at 100 mA` |  |
| PMC5515720 | `−1 at 100 mA g−1 in the se` |  |
| PMC5521283 | `10, and 824 cm−1 that come` | oui |
| PMC5521283 | `15, and 636 cm−1. The inte` | non |
| PMC5521283 | `d to be 1.6 cm−1. The tran` | non |
| PMC5535248 | `039 to 1218 cm−1 was also ` |  |
| PMC5535248 | `400 to 4000 cm−1, and the ` |  |
| PMC5535248 | `400 to 4000 cm−1. The samp` |  |
| PMC5535248 | `and at 1628 cm−1 was attri` |  |
| PMC5535248 | `and at 3442 cm−1, which ex` |  |
| PMC5535248 | `around 1365 cm−1 and the G` |  |
| PMC5535248 | `around 1640 cm−1 in the GO` |  |
| PMC5535248 | `band (~1585 cm−1) of the R` |  |
| PMC5535248 | `eak at 1383 cm−1 was assig` |  |
| PMC5535248 | `lution of 4 cm−1 over the ` |  |
| PMC5535248 | `nds at 1365 cm−1 and 1585 ` |  |
| PMC5535248 | `rate of 4° min−1. The exte` |  |
| PMC5535248 | `ved at 1560 cm−1, which is` |  |
| PMC5535248 | `−1 and 1585 cm−1, respecti` |  |
| PMC5551800 | ` at 600–570 cm−1 and 1090–` |  |
| PMC5551800 | ` at 870–875 cm−1, is due t` |  |
| PMC5551800 | ` cm−1, 1160 cm−1, and 725 ` |  |
| PMC5551800 | ` cm−1, 1455 cm−1, and 1415` |  |
| PMC5551800 | `00 and 1420 cm−1, vibratio` |  |
| PMC5551800 | `1, and 1415 cm−1 are disti` |  |
| PMC5551800 | `2, and 1354 cm−1 [], the s` |  |
| PMC5551800 | `210 and 725 cm−1 are visib` |  |
| PMC5551800 | `570 and 630 cm−1, whereas ` |  |
| PMC5551800 | `573 and 632 cm−1 are assig` |  |
| PMC5551800 | `601 and 570 cm−1 is due to` |  |
| PMC5551800 | `70 and 1100 cm−1 []. Moreo` |  |
| PMC5551800 | `748 and 420 cm−1, and the ` |  |
| PMC5551800 | `90 and 1040 cm−1, as well ` |  |
| PMC5551800 | `99, and 430 cm−1. After 60` |  |
| PMC5551800 | `aks at 1028 cm−1 are assig` |  |
| PMC5551800 | `aks at 1205 cm−1, 1160 cm−` |  |
| PMC5551800 | `aks at 1530 cm−1, 1455 cm−` |  |
| PMC5551800 | `and at 1060 cm−1 (ascribab` |  |
| PMC5551800 | `and at 1435 cm−1 and the w` |  |
| PMC5551800 | `and at 1455 cm−1 and the w` |  |
| PMC5551800 | `and at 1512 cm−1), 0.7ZrO2` |  |
| PMC5551800 | `and at 1543 cm−1 (N–H in-p` |  |
| PMC5551800 | `and at 1543 cm−1 also appe` |  |
| PMC5551800 | `and at 1654 cm−1 is visibl` |  |
| PMC5551800 | `and at 3400 cm−1 is due to` |  |
| PMC5551800 | `ands at 650 cm−1 and 470 c` |  |
| PMC5551800 | `band at 718 cm−1 was repla` |  |
| PMC5551800 | `band at 880 cm−1 [,]. Howe` |  |
| PMC5551800 | `ble at 1455 cm−1 and 1415 ` |  |
| PMC5551800 | `d 1090–1040 cm−1, respecti` |  |
| PMC5551800 | `e 1500–1400 cm−1 and the w` |  |
| PMC5551800 | `eak at 1040 cm−1 [], due t` |  |
| PMC5551800 | `eak at 1040 cm−1, due to P` |  |
| PMC5551800 | `eak at 1060 cm−1 split, an` |  |
| PMC5551800 | `eak at 3640 cm−1, ascribab` |  |
| PMC5551800 | `eak at 3641 cm−1 [,]. Ther` |  |
| PMC5551800 | `gnal at 875 cm−1 can also ` |  |
| PMC5551800 | `he 400–4000 cm−1 region wi` |  |
| PMC5551800 | `in, at 1654 cm−1(stretchin` |  |
| PMC5551800 | `ion 700–400 cm−1 and the s` |  |
| PMC5551800 | `ion 750–400 cm−1 suggest t` |  |
| PMC5551800 | `lder at 510 cm−1, prove th` |  |
| PMC5551800 | `lder at 960 cm−1, are due ` |  |
| PMC5551800 | `lution of 4 cm−1 (45 scans` |  |
| PMC5551800 | `mation of HPO4−2, PO4−3, a` |  |
| PMC5551800 | `min at 1654 cm−1, due to t` |  |
| PMC5551800 | `m−1 and 470 cm−1 are due t` |  |
| PMC5551800 | `n 1450–1410 cm−1, coupled ` |  |
| PMC5551800 | `n 1450–1550 cm−1 vibration` |  |
| PMC5551800 | `n 1500–1300 cm−1, which al` |  |
| PMC5551800 | `n 1500–1300 cm−1. The sign` |  |
| PMC5551800 | `n 1500–1400 cm−1 []. The p` |  |
| PMC5551800 | `n 1700–1300 cm−1, but with` |  |
| PMC5551800 | `nds at 1544 cm−1 and 1350 ` |  |
| PMC5551800 | `ng (at 3400 cm−1 and 1637 ` |  |
| PMC5551800 | `of HPO4−2, PO4−3, and OH− ` |  |
| PMC5551800 | `peak at 420 cm−1 is attrib` |  |
| PMC5551800 | `peak at 738 cm−1, ascribab` |  |
| PMC5551800 | `peak at 748 cm−1, typical ` |  |
| PMC5551800 | `peak at 827 cm−1 []; and (` |  |
| PMC5551800 | `peak at 865 cm−1 [,,]. Mor` |  |
| PMC5551800 | `peak at 865 cm−1 is still ` |  |
| PMC5551800 | `peak at 875 cm−1 are ascri` |  |
| PMC5551800 | `peak at 875 cm−1 are assig` |  |
| PMC5551800 | `peak of 875 cm−1, indeed, ` |  |
| PMC5551800 | `t 1047, 823 cm−1, and the ` |  |
| PMC5551800 | `t about 866 cm−1 []. There` |  |
| PMC5551800 | `ted to 1510 cm−1 and 1420 ` |  |
| PMC5551800 | `ved at 1560 cm−1 and 1446 ` |  |
| PMC5551800 | `−1 and 1350 cm−1 are due t` |  |
| PMC5551800 | `−1 and 1415 cm−1 []. It ca` |  |
| PMC5551800 | `−1 and 1420 cm−1, and the ` |  |
| PMC5551800 | `−1 and 1446 cm−1 are assig` |  |
| PMC5551800 | `−1 and 1637 cm−1 respectiv` |  |
| PMC5551800 | `−1, and 725 cm−1 confirm t` |  |
| PMC5591228 | `as at ~1345 cm−1, correspo` |  |
| PMC5591228 | `nd at ~1593 cm−1 and that ` |  |
| PMC5591228 | `peak (~2681 cm−1) and S3 p` |  |
| PMC5591228 | `peak (~2681 cm−1) and S3 p` |  |
| PMC5591228 | `peak (~2931 cm−1) indicate` |  |
| PMC5591228 | `peak (~2931 cm−1) indicate` |  |
| PMC5593864 | ` peak (2706 cm−1) and a co` |  |
| PMC5593864 | `26 and 1046 cm−1 are due t` |  |
| PMC5593864 | `26 and 1046 cm−1 decrease ` |  |
| PMC5593864 | `40 and 1627 cm−1 can be at` |  |
| PMC5593864 | `at ca. 1356 cm−1 originati` |  |
| PMC5593864 | `at ca. 1599 cm−1 correspon` |  |
| PMC5593864 | `umber (2937 cm−1) can also` |  |
| PMC5680254 | ` at vacuum ≤10−6 mbar. The` |  |
| PMC5680254 | `3 and 437.5 cm−1 are succe` |  |
| PMC5680254 | `ate of 0.01° s−1. Room tem` |  |
| PMC5680254 | `ring at 332 cm−1 is the se` |  |
| PMC5680254 | `to 2 × 1017 cm−3 while fie` |  |
| PMC5680254 | `to 2 × 1017 cm−3 while fie` |  |
| PMC5707940 | ` (near 1350 cm−1). After b` |  |
| PMC5707940 | ` was 8.95 × 10−6 mg/(g·min` |  |
| PMC5707940 | `and at 1590 cm−1. The inte` |  |
| PMC5707940 | `d near 1350 cm−1 and G ban` |  |
| PMC5707940 | `e near 3470 cm−1 was attri` |  |
| PMC5707940 | `ion in 1578 cm−1 (G band) ` |  |
| PMC5707940 | `of 0.00157 min−1, which wa` |  |
| PMC5707940 | `ted to 1582 cm−1, which wa` |  |
| PMC5707940 | `was 0.0053 min−1). The cal` |  |
| PMC5727554 | `sure, 1.3 × 10−3 Pa; and w` |  |
| PMC5746929 | ` at 450–500 cm−1 of Si–O–S` |  |
| PMC5746929 | `0 and ~2850 cm−1, respecti` |  |
| PMC5746929 | `693 and 904 cm−1 are assig` |  |
| PMC5746929 | `694 and 734 cm−1, respecti` |  |
| PMC5746929 | `ak at ~1460 cm−1 is reveal` |  |
| PMC5746929 | `ated at 545 cm−1, correlat` |  |
| PMC5746929 | `d 3390–3350 cm−1 is observ` |  |
| PMC5746929 | `e (400–4000 cm−1), resolut` |  |
| PMC5746929 | `eak at 2931 cm−1 is attrib` |  |
| PMC5746929 | `ed at ~1030 cm−1, which is` |  |
| PMC5746929 | `fied at 786 cm−1 is due to` |  |
| PMC5746929 | `lution of 4 cm−1. X-ray di` |  |
| PMC5746929 | `rsor (1.1 × 10−2 moles GPT` |  |
| PMC5746929 | `ved at 1430 cm−1, assigned` |  |
| PMC5750015 | ` of 650–425 cm−1. There ar` | non |
| PMC5750015 | `207 and 719 cm−1, which co` | non |
| PMC5750015 | `47 and 1076 cm−1, clearly ` | non |
| PMC5750015 | `47 and 1458 cm−1 can be as` | non |
| PMC5750015 | `58 and 1166 cm−1. These sp` | non |
| PMC5750015 | `735 and 962 cm−1 and fairl` | oui |
| PMC5750015 | `ars at 3570 cm−1, which is` | non |
| PMC5750015 | `eak at 1045 cm−1 as indica` | non |
| PMC5750015 | `f 1470–1400 cm−1 as can be` | non |
| PMC5750015 | `gnal at 719 cm−1 as indica` | oui |
| PMC5750015 | `lution of 2 cm−1. X-ray di` | non |
| PMC5750015 | `of 1200–900 cm−1, which ar` | non |
| PMC5750015 | `peak at 962 cm−1 [,]. Samp` | non |
| PMC5750015 | `te of 10°C min−1. After ca` | non |
| PMC5750015 | `tred at 962 cm−1 and three` | oui |
| PMC5750015 | `was at 1045 cm−1, with sma` | oui |
| PMC5750015 | `y 40 drops min−1 through a` | oui |
| PMC5756267 | ` (> 1024 µg ml−1) against ` |  |
| PMC5756267 | ` (> 1024 µg ml−1). The use` |  |
| PMC5756267 | ` 105 c.f.u. ml−1 of bacter` |  |
| PMC5756267 | ` 105 c.f.u. ml−1) was comb` |  |
| PMC5756267 | ` 105 c.f.u. ml−1) was dilu` |  |
| PMC5756267 | ` 105 c.f.u. ml−1. Inoculat` |  |
| PMC5756267 | ` 105 c.f.u. ml−1. The MICs` |  |
| PMC5756267 | ` 105 c.f.u. ml−1. The tryp` |  |
| PMC5756267 | ` 150–600 μg ml−1, while ag` |  |
| PMC5756267 | ` B (0.25 µg ml−1). Similar` |  |
| PMC5756267 | ` about 4 µg ml−1), which w` |  |
| PMC5756267 | ` and 196 µg ml−1, respecti` |  |
| PMC5756267 | ` and 256 µg ml−1, respecti` |  |
| PMC5756267 | ` and 256 µg ml−1, respecti` |  |
| PMC5756267 | ` and 3.8 µg ml−1, respecti` |  |
| PMC5756267 | ` and 384 µg ml−1 for S. au` |  |
| PMC5756267 | ` of 64.5 µg ml−1) against ` |  |
| PMC5756267 | ` oil (2.5 ml l−1) was used` |  |
| PMC5756267 | ` to 1024 µg ml−1) of AgNPs` |  |
| PMC5756267 | ` to be 4 μg ml−1, thus eig` |  |
| PMC5756267 | `.016–256 µg ml−1. Estimati` |  |
| PMC5756267 | `0 and 20 µg ml−1 of AgNPs ` |  |
| PMC5756267 | `0 or 100 µg ml−1 (Manivasa` |  |
| PMC5756267 | `016–1024 µg ml−1. The TSB ` |  |
| PMC5756267 | `4 and 16 µg ml−1) against ` |  |
| PMC5756267 | `6 and 64 µg ml−1, respecti` |  |
| PMC5756267 | `7 particles ml−1 (Fig. 3).` |  |
| PMC5756267 | `85 and 1033 cm−1 (Fig. 4).` |  |
| PMC5756267 | `agent (1 mg ml−1) at 37 °C` |  |
| PMC5756267 | `aks at 3432 cm−1 can be as` |  |
| PMC5756267 | `alis (40 μg ml−1, both). T` |  |
| PMC5756267 | `and at 1033 cm−1 can be as` |  |
| PMC5756267 | `and at 1631 cm−1 can be at` |  |
| PMC5756267 | `ation 20 µg ml−1) as well ` |  |
| PMC5756267 | `cin (512 µg ml−1) against ` |  |
| PMC5756267 | `e (0.001 mol l−1) were als` |  |
| PMC5756267 | `eak at 1385 cm−1 correspon` |  |
| PMC5756267 | `eas at 2925 cm−1 can be as` |  |
| PMC5756267 | `h > 1024 µg ml−1) but not ` |  |
| PMC5756267 | `lis, 256 µg ml−1 for K. pn` |  |
| PMC5756267 | `lution of 4 cm−1 were perf` |  |
| PMC5756267 | `nosa, 48 µg ml−1 for M. fu` |  |
| PMC5756267 | `of 4000–400 cm−1 at a reso` |  |
| PMC5756267 | `on 0.001 mol l−1) and incu` |  |
| PMC5756267 | `rfur (30 μg ml−1) was simi` |  |
| PMC5756267 | `rfur, 64 µg ml−1 for E. co` |  |
| PMC5756267 | `s (1–100 µg ml−1) of AgNPs` |  |
| PMC5756267 | `s > 1000 μg ml−1. Nasrolla` |  |
| PMC5756267 | `to be 32 µg ml−1 for P. ae` |  |
| PMC5756267 | `tudy (32 µl ml−1). However` |  |
| PMC5784500 | ` around 500 cm−1 overlay t` |  |
| PMC5784500 | ` peak (1442 cm−1) was weak` |  |
| PMC5784500 | `08, and 976 cm−1. Among th` |  |
| PMC5784500 | `20, and 610 cm−1, attribut` |  |
| PMC5784500 | `24 and 1310 cm−1 were attr` |  |
| PMC5784500 | `298 and 380 cm−1 were assi` |  |
| PMC5784500 | `42 and 1450 cm−1, due to c` |  |
| PMC5784500 | `50 and 1542 cm–1 can be at` |  |
| PMC5784500 | `band at 606 cm−1 was proba` |  |
| PMC5784500 | `band at 778 cm−1 could be ` |  |
| PMC5784500 | `band at 808 cm−1 could be ` |  |
| PMC5784500 | `band at 976 cm−1 was a res` |  |
| PMC5784500 | `band at 985 cm−1, attribut` |  |
| PMC5784500 | `fted to 514 cm−1, both ind` |  |
| PMC5784500 | `peak at 298 cm−1 and the i` |  |
| PMC5784500 | `peak at 520 cm−1 shifted t` |  |
| PMC5793535 | `igh as 1021 cm−3 for 5% GZ` |  |
| PMC5793645 | ` (20,000 cm2 V−1 s−1) and ` | non |
| PMC5793645 | `,000 cm2 V−1 s−1) and its ` | non |
| PMC5793645 | `1 cm−1, 813 cm−1 and 928 c` | oui |
| PMC5793645 | `50 mL, 10 mg·L−1). The sol` | non |
| PMC5793645 | `7 cm−1, 761 cm−1, 813 cm−1` | oui |
| PMC5793645 | `8 cm−1, 327 cm−1, 761 cm−1` | oui |
| PMC5793645 | `8 cm−1, 761 cm−1 and 813 c` | oui |
| PMC5793645 | `aks at 1331 cm−1 and 1592 ` | oui |
| PMC5793645 | `around 1609 cm−1 is charac` | non |
| PMC5793645 | `ca. 186 µmol·L−1) and mixe` | non |
| PMC5793645 | `ca. 214 µmol·L−1) when use` | non |
| PMC5793645 | `eaks at 248 cm−1, 327 cm−1` | oui |
| PMC5793645 | `ered at 248 cm−1 and 327 c` | oui |
| PMC5793645 | `hose at 668 cm−1, 761 cm−1` | oui |
| PMC5793645 | `mately 1336 cm−1 and 1609 ` | non |
| PMC5793645 | `mately 1336 cm−1 can be at` | non |
| PMC5793645 | `m−1 and 327 cm−1 were attr` | oui |
| PMC5793645 | `m−1 and 813 cm−1 were attr` | oui |
| PMC5793645 | `m−1 and 928 cm−1 were obse` | oui |
| PMC5793645 | `peak at 928 cm−1 arose fro` | oui |
| PMC5793645 | `−1 and 1592 cm−1 were obse` | oui |
| PMC5793645 | `−1 and 1609 cm−1, the D-ba` | non |
| PMC5821621 | ` 1083, 2360 cm−1 are assig` |  |
| PMC5821621 | `, 601, 1029 cm−1 correspon` |  |
| PMC5821621 | `49 and 1037 cm−1 are assig` |  |
| PMC5821621 | `902 and 767 cm−1 are ascri` |  |
| PMC5821621 | `and at 1639 cm−1 is ascrib` |  |
| PMC5821621 | `at 605, 871 cm−1 accounts ` |  |
| PMC5821621 | `eak at 1600 cm−1 where it ` |  |
| PMC5821621 | `eak at 1627 cm−1 is due to` |  |
| PMC5821621 | `eak at 1639 cm−1 is due to` |  |
| PMC5821621 | `f 2500–3000 cm−1 as shown ` |  |
| PMC5821621 | `f 2800–3000 cm−1 correspon` |  |
| PMC5821621 | `f 2850–2980 cm−1 in the tu` |  |
| PMC5821621 | `f 2950–2850 cm−1 while bis` |  |
| PMC5821621 | `f 2980–2850 cm−1 and demet` |  |
| PMC5821621 | `f 3200–3600 cm−1 in neat t` |  |
| PMC5821621 | `ion of 1565 cm−1 is attrib` |  |
| PMC5821621 | `of 400–4000 cm−1. The prep` |  |
| PMC5821621 | `t 3200–3600 cm−1 region ac` |  |
| PMC5821621 | `t 3700–3200 cm−1 is attrib` |  |
| PMC5821621 | `ty = 0.91 g cm−3, purity =` |  |
| PMC5821621 | `ved at 1384 cm−1 accounts ` |  |
| PMC5824763 | ` and ~1,600 cm−1 (associat` |  |
| PMC5824763 | `383 and 737 cm−1 and mediu` |  |
| PMC5824763 | `448 and 502 cm−1) and asym` |  |
| PMC5824763 | `464 and 585 cm−1) have bee` |  |
| PMC5824763 | `7 and 2,915 cm−1) are assi` |  |
| PMC5824763 | `7 and 2,915 cm−1). Other v` |  |
| PMC5824763 | `8 and 1,350 cm−1) both aft` |  |
| PMC5824763 | `e 400–4,000 cm−1 spectral ` |  |
| PMC5824763 | `ed at 1,038 cm−1 (associat` |  |
| PMC5824763 | `hing (1,420 cm−1). The tim` |  |
| PMC5824763 | `hing (1,620 cm−1), C–N–C s` |  |
| PMC5824763 | `ins), 1,471 cm−1 (associat` |  |
| PMC5824763 | `lution of 4 cm−1. Dry plan` |  |
| PMC5824763 | `lution of 5 cm−1. All meas` |  |
| PMC5824763 | `nd at 1,439 cm−1. All thes` |  |
| PMC5824763 | `nd at 1,730 cm−1. This ban` |  |
| PMC5858874 | `68.68 mg KOH g−1 by adding` | oui |
| PMC5858874 | `e of 10 °C min−1 in pure n` | oui |
| PMC5858874 | `e of 50 ml min−1. Each exp` | non |
| PMC5858874 | `n 0.5 mg KOH g−1) (). Comp` | non |
| PMC5858874 | `ue (HHV, MJ kg−1) and ener` | non |
| PMC5869654 | ` band (1348 cm−1) is signi` |  |
| PMC5869654 | ` band (1583 cm−1) compared` |  |
| PMC5869654 | `04 and 1354 cm−1, respecti` |  |
| PMC5869654 | `20, and 838 cm−1 correspon` |  |
| PMC5869654 | `5, and 1055 cm−1 correspon` |  |
| PMC5869654 | `les at 1564 cm−1 during th` |  |
| PMC5877699 | `d 1050–1350 cm−1 respectiv` |  |
| PMC5877699 | `n 1700–2100 cm−1 correspon` |  |
| PMC5882680 | ` at 400–800 cm−1 in pure B` | oui |
| PMC5882680 | ` below 10 m2 g–1 for the b` | non |
| PMC5882680 | `(TBA, 6 mmol l−1) as effec` | oui |
| PMC5882680 | `01 and 1569 cm−1 correspon` | non |
| PMC5882680 | `400 to 1600 cm−1 is shown ` | non |
| PMC5882680 | `BQ, 0.5 mmol l−1) and tert` | oui |
| PMC5882680 | `EDTA, 6 mmol l−1), benzoqu` | oui |
| PMC5882680 | `aks at 3428 cm−1 and 1628 ` | oui |
| PMC5882680 | `band at 808 cm−1 belongs t` | oui |
| PMC5882680 | `e 1200–1600 cm−1 region wi` | non |
| PMC5882680 | `e, the 3155 cm−1 band can ` | non |
| PMC5882680 | `lution (5 mg l−1) and stir` | non |
| PMC5882680 | `nd 0.00313 min−1 for pure ` | oui |
| PMC5882680 | `−1 and 1628 cm−1 in the sp` | oui |
| PMC5887100 | `0 and 50 μg mL–1. After th` |  |
| PMC5887100 | `VC–N, ∼1080 cm–1), was als` |  |
| PMC5887100 | `band (∼1330 cm–1) and a G-` |  |
| PMC5887100 | `band (∼1600 cm–1). In our ` |  |
| PMC5887100 | `between 850 cm–1 and 1700 ` |  |
| PMC5887100 | `n of 100 μg mL–1. Such a p` |  |
| PMC5887100 | `ning 100 μg mL–1 ACDs for ` |  |
| PMC5887100 | `of 400–4000 cm–1.XPSX-ray ` |  |
| PMC5887100 | `p to 500 μg mL–1, the cell` |  |
| PMC5887100 | `–1 and 1700 cm–1 using a g` |  |
| PMC5890287 | `00 and 3430 cm−1 correspon` |  |
| PMC5890287 | `25 and 3430 cm−1 correspon` |  |
| PMC5890287 | `28 and 2865 cm−1 for the C` |  |
| PMC5890287 | `36 and 1044 cm−1 correspon` |  |
| PMC5890287 | `4000 to 450 cm−1 acquired.` |  |
| PMC5890287 | `540 and 309 cm−1 correspon` |  |
| PMC5890287 | `<0.2 cm2·V−1·s−1). Convers` |  |
| PMC5890287 | `and at 1350 cm−1 is assign` |  |
| PMC5890287 | `and at 1580 cm−1 is associ` |  |
| PMC5890287 | `and at 2694 cm−1 is associ` |  |
| PMC5890287 | `eak at 1721 cm−1 was attri` |  |
| PMC5890287 | `n was 1.0 × 10−3 M. It was` |  |
| PMC5890287 | `peak at 466 cm−1 attribute` |  |
| PMC5890287 | `peak at 669 cm−1 can be as` |  |
| PMC5890287 | `red at 3436 cm−1 correspon` |  |
| PMC5890287 | `rs (<0.2 cm2·V−1·s−1). Con` |  |
| PMC5896389 | `00 and 1280 cm-1 indicated` | non |
| PMC5896389 | `ear at 1400 cm-1. Peaks ap` | non |
| PMC5896389 | `mately 1066 cm-1 presented` | non |
| PMC5896389 | `t 2800-2950 cm-1 was assig` | non |
| PMC5896389 | `t 3200-3500 cm-1 belonged ` | oui |
| PMC5923560 | `and at 1040 cm−1 was norma` | non |
| PMC5923560 | `and at 2853 cm−1 and 2923 ` | non |
| PMC5923560 | `nds at 1040 cm−1, characte` | non |
| PMC5923560 | `−1 and 2923 cm−1, which ca` | non |
| PMC5977331 | `ated at 780 cm−1 and 1630 ` | oui |
| PMC5977331 | `hift at 480 cm−1 of ZnO-MC` | oui |
| PMC5977331 | `ing at 2929 cm−1 and 2850 ` | non |
| PMC5977331 | `m−1 and 810 cm−1 belonged ` | non |
| PMC5977331 | `m−1 and 968 cm−1 were the ` | non |
| PMC5977331 | `red at 1080 cm−1 and 810 c` | non |
| PMC5977331 | `ring at 780 cm−1 and 1630 ` | oui |
| PMC5977331 | `ted at 3413 cm−1 and 968 c` | non |
| PMC5977331 | `−1 and 1630 cm−1 of Sal we` | non |
| PMC5977331 | `−1 and 1630 cm−1, respecti` | oui |
| PMC5977331 | `−1 and 2850 cm−1 of Sal-MC` | non |
| PMC5978183 | `.1 ± 0.8) × 10−4 S/cm, whi` | oui |
| PMC5978183 | `.3 ± 1.0) ×·10−3 S/cm, whi` | oui |
| PMC5978183 | `0−5 − 3.2 × 10−6 S/cm) [,,` | non |
| PMC5978183 | `conditions (10−6 mbar). Fo` | non |
| PMC5978183 | `s less than 10-4 eV. To ac` | non |
| PMC5978183 | `ture (1.7 × 10−5 − 3.2 × 1` | non |
| PMC5979620 | `d to 100 mW cm−2. For EIS ` |  |
| PMC5979620 | `e of 10 °C min−1 in air. A` |  |
| PMC5979620 | `e of 10 °C min−1. XRD patt` |  |
| PMC5979620 | `ivity (≈4 S cm−1) and very` |  |
| PMC5979620 | `m at 100 mW cm−2 as measur` |  |
| PMC5979620 | `re (200 mL min−1 flow rate` |  |
| PMC5979620 | `sistance 4Ω sq−1) were pur` |  |
| PMC5979620 | `t of 0.24 × 10−3 m HNO3 (F` |  |
| PMC5979620 | `tion, 20 mg mL−1 in chloro` |  |
| PMC5979620 | `to 19.94 mA cm−2, compared` |  |
| PMC5979620 | `y up to 4 S cm−1 at room t` |  |
| PMC5990742 | `2 × 10−5 mol l−1. The susp` | oui |
| PMC5990742 | `ate of 2°C min−1 to 500°C ` | oui |
| PMC5990742 | `d 1200–1600 cm−1, shown in` | non |
| PMC5990742 | `eaks at 810 cm−1 and 1200–` | non |
| PMC5990742 | `tant of 1.53 h−1, which is` | oui |
| PMC5990742 | `tion of 2 × 10−5 mol l−1. ` | oui |
| PMC6058695 | `31 and 1512 cm−1 could be ` | oui |
| PMC6083653 | `100 to 3700 cm−1 correspon` |  |
| PMC6083653 | `15 and 1588 cm−1 are attri` |  |
| PMC6083653 | `20 and 2850 cm−1 are attri` |  |
| PMC6083653 | `aks at 1630 cm−1, attribut` |  |
| PMC6116234 | ` devices (3 AW−1) but lowe` | non |
| PMC6116234 | `crystal (40 AW−1) based on` | non |
| PMC6116234 | `h up to 8.3 AW−1 under a b` | oui |
| PMC6116234 | `vity of 8.3 AW−1, a high o` | oui |
| PMC6116234 | `vity of 8.3 AW−1, a high o` | oui |
| PMC6154307 | ` flow: 8 L min−1; gas temp` | non |
| PMC6154307 | ` of 0.3 mL/min−1. The inje` | non |
| PMC6154307 | `.5 and 2 mg mL−1. When the` | non |
| PMC6164367 | ` as at 1644 cm−1, which is` |  |
| PMC6164367 | `40 and 1060 cm−1 assigned ` |  |
| PMC6164367 | `40 and 1060 cm−1 character` |  |
| PMC6164367 | `7, and 2876 cm−1 assigned ` |  |
| PMC6164367 | `7, and 2876 cm−1 assigned ` |  |
| PMC6164367 | `7, and 2876 cm−1. These bo` |  |
| PMC6164367 | `88 and 3628 cm−1 associate` |  |
| PMC6164367 | `and at 1644 cm−1 is assign` |  |
| PMC6164367 | `bond at 799 cm−1 proves th` |  |
| PMC6164367 | `e 3700–2600 cm−1, which is` |  |
| PMC6164367 | `e 3700–3200 cm−1, assigned` |  |
| PMC6164367 | `er than 1 × 10−9 mbar. Due` |  |
| PMC6164367 | `ion at 1060 cm−1 for graph` |  |
| PMC6164367 | `ols at 1050 cm−1 is relate` |  |
| PMC6164367 | `peak at 954 cm−1 assigned ` |  |
| PMC6164367 | `t 3700–2600 cm−1, as well ` |  |
| PMC6164367 | `tion at 954 cm−1 belongs t` |  |
| PMC6164367 | `ups at 1730 cm−1 and C–OH ` |  |
| PMC6164367 | `–OH at 1396 cm−1) [,]. Acc` |  |
| PMC6199062 | ` 831/551 mAh g−1, with cou` | non |
| PMC6199062 | ` and 1000 mA g−1, respecti` | non |
| PMC6199062 | ` and 103 mAh g−1 (with cou` | oui |
| PMC6199062 | ` and 179 mAh g−1 for Sb2S3` | oui |
| PMC6199062 | ` and 2000 mA g−1. However,` | non |
| PMC6199062 | ` and 234 mAh g−1 for Sb2S3` | oui |
| PMC6199062 | ` and 239 mAh g−1, respecti` | oui |
| PMC6199062 | ` and 400 mAh g−1 at a curr` | non |
| PMC6199062 | ` and 5000 mA g−1 for five ` | oui |
| PMC6199062 | ` and 5000 mA g−1, Sb2S3-15` | non |
| PMC6199062 | ` and 5000 mA g−1, the Sb2S` | non |
| PMC6199062 | ` and 5000 mA g−1, the disc` | non |
| PMC6199062 | ` and 532 mAh g−1 for Sb2S3` | oui |
| PMC6199062 | ` and 541 mAh g−1, respecti` | oui |
| PMC6199062 | ` and 960 mAh g−1 after 50 ` | non |
| PMC6199062 | `0 and 100 mA g−1, respecti` | non |
| PMC6199062 | `0 to 5000 mA g−1 in the vo` | oui |
| PMC6199062 | `1058/767 mAh g−1 correspon` | oui |
| PMC6199062 | `1058/767 mAh g−1) may be r` | oui |
| PMC6199062 | `7 to 419 mAh g−1. However,` | non |
| PMC6199062 | `around 1 mg cm−2. For LIBs` | non |
| PMC6199062 | `bout 506 mAh g−1 (189 mAh ` | oui |
| PMC6199062 | `bout 674 mAh g−1 (643 mAh ` | oui |
| PMC6199062 | `ced to 50 mA g−1, indicati` | non |
| PMC6199062 | `cles (90 mAh g−1 for Sb2S3` | oui |
| PMC6199062 | `e of 656 mAh g−1 at a curr` | non |
| PMC6199062 | `ed to 500 mA g−1, there wa` | non |
| PMC6199062 | `g−1 (189 mAh g−1 for Sb2S3` | oui |
| PMC6199062 | `g−1 (643 mAh g−1 for Sb2S3` | oui |
| PMC6199062 | `ity (947 mAh g−1) and supe` | non |
| PMC6199062 | `ity of 50 mA g−1 in NIBs. ` | oui |
| PMC6199062 | `ity of 50 mA g−1. Neverthe` | non |
| PMC6199062 | `ity of 50 mA g−1. When the` | non |
| PMC6199062 | `nd 300.5 mAh g−1 are achie` | non |
| PMC6199062 | `r to 629 mAh g−1, indicati` | non |
| PMC6199062 | `s at 201 mAh g−1.Over the ` | non |
| PMC6199062 | `ses to 50 mA g−1, the reve` | non |
| PMC6199062 | `te of 0.1 mV s−1 in the vo` | oui |
| PMC6199062 | `te of 0.1 mV s−1 in the vo` | oui |
| PMC6199062 | `than 200 mAh g−1, which is` | non |
| PMC6199062 | `ty of 100 mA g−1 after 100` | oui |
| PMC6199062 | `ty of 100 mA g−1 after 30 ` | oui |
| PMC6199062 | `ty of 100 mA g−1 and a wid` | non |
| PMC6199062 | `ty of 100 mA g−1 in NIBs, ` | oui |
| PMC6199062 | `ty of 100 mA g−1. Sb2S3-gr` | non |
| PMC6199062 | `ty of 200 mA g−1 after 50 ` | oui |
| PMC6199062 | `ty of 200 mA g−1 after 50 ` | oui |
| PMC6199062 | `ty of 200 mA g−1 are shown` | non |
| PMC6199062 | `ty of 200 mA g−1 in the vo` | oui |
| PMC6199062 | `ty of 200 mA g−1, and the ` | oui |
| PMC6199062 | `ty of 500 mA g−1 after 50 ` | oui |
| PMC6199062 | `ty of 500 mA g−1 in LIBs. ` | oui |
| PMC6199062 | `ty of 500 mA g−1 in the vo` | oui |
| PMC6199062 | `ty of 90 mAh g−1 with a co` | oui |
| PMC6199062 | `y of 1000 mA g−1 after 100` | oui |
| PMC6199062 | `y of 1000 mA g−1 after 100` | oui |
| PMC6199062 | `y of 1000 mA g−1 in the vo` | oui |
| PMC6199062 | `y of 1000 mA g−1 were not ` | non |
| PMC6199062 | `y of 384 mAh g−1 at a curr` | non |
| PMC6199062 | `y of 384 mAh g−1 with a co` | oui |
| PMC6199062 | `y of 400 mAh g−1 at a curr` | non |
| PMC6199062 | `y of 458 mAh g−1 at a curr` | non |
| PMC6199062 | `y of 469 mAh g−1 with a co` | oui |
| PMC6199062 | `y of 548 mAh g−1 after 100` | non |
| PMC6199062 | `y of 548 mAh g−1 at a curr` | non |
| PMC6199062 | `y of 600 mAh g−1 after 100` | non |
| PMC6199062 | `y of 614 mAh g−1 at a curr` | non |
| PMC6199062 | `y of 990 mAh g−1 at a curr` | non |
| PMC6214041 | `5 and ~1520 cm−1 appeared ` |  |
| PMC6214041 | `5 and ~1615 cm−1, which ar` |  |
| PMC6222835 | `at ca. 1275 cm−1 in patter` | non |
| PMC6222835 | `at ca. 1655 cm−1 and 626 c` | non |
| PMC6222835 | `eak at 1066 cm−1 correspon` | oui |
| PMC6222835 | `eak at 1720 cm−1 with low ` | oui |
| PMC6222835 | `eak at 3386 cm−1 of patter` | oui |
| PMC6222835 | `eak at 3396 cm−1 in patter` | oui |
| PMC6222835 | `m−1 and 626 cm−1, which ar` | non |
| PMC6266651 | `09, and 693 cm−1 [,] vanis` | non |
| PMC6266651 | `115 and 138 cm−1 cannot cu` | non |
| PMC6266651 | `57, and 361 cm−1 and weake` | non |
| PMC6266651 | `60 and ~410 cm−1 appeared ` | non |
| PMC6266651 | `85, and 560 cm−1. Accordin` | non |
| PMC6266651 | `n was <0.35 cm−1.The therm` | non |
| PMC6266651 | `peak at 195 cm−1 correspon` | non |
| PMC6266651 | `peak at 262 cm−1 correspon` | non |
| PMC6266651 | `peak at 485 cm−1 correspon` | non |
| PMC6270268 | `, and 1,452 cm−1. The char` | non |
| PMC6270268 | `000 and 400 cm−1 with a re` | non |
| PMC6270268 | `1 and 1,033 cm−1; the char` | oui |
| PMC6270268 | `ared at 874 cm−1 and 1,033` | oui |
| PMC6270268 | `ds at 1,416 cm−1 were ascr` | non |
| PMC6270268 | `e of 10 °C min−1 under a n` | non |
| PMC6270268 | `ed at 1,637 cm−1; and the ` | oui |
| PMC6270268 | `ed at 3,420 cm−1. The band` | non |
| PMC6270268 | `ed at 3,450 cm−1. This sho` | non |
| PMC6270268 | `ed to 3,385 cm−1. Hence, t` | non |
| PMC6270268 | `lution of 4 cm−1, and each` | non |
| PMC6273739 | ` around 539 cm−1 is attrib` |  |
| PMC6273739 | ` below 1000 cm−1. The peak` |  |
| PMC6273739 | `00 and 4000 cm−1.A broad b` |  |
| PMC6273739 | `and at 1382 cm−1 is relate` |  |
| PMC6273739 | `g below 700 cm−1 are due t` |  |
| PMC6273739 | `red at 3412 cm−1 and a hig` |  |
| PMC6273739 | `ted at 1718 cm−1, confirmi` |  |
| PMC6273754 | `vacuum (ca. 10−4 mbar) at ` | oui |
| PMC6274424 | ` OH), ~2933 cm−1 (C–H, asy` | oui |
| PMC6274424 | `cm−1, ~1074 cm−1. Therefor` | non |
| PMC6274424 | `cm−1, ~1663 cm−1, ~1074 cm` | non |
| PMC6274424 | `cm−1, ~2959 cm−1, ~1663 cm` | non |
| PMC6274424 | `ed at ~3504 cm−1, ~2959 cm` | non |
| PMC6274424 | `etch) ~1000 cm−1 (C–O) whi` | oui |
| PMC6274424 | `etch) ~1698 cm−1 (C=O stre` | oui |
| PMC6274424 | `ng at, 3627 cm−1 (hydrogen` | oui |
| PMC6274424 | `retch) 1398 cm−1 (C–O stre` | oui |
| PMC6274424 | `tch), ~2132 cm−1 (C≡C stre` | oui |
| PMC6278251 | ` was p ~3 × 10−9 torr. X-r` |  |
| PMC6297187 | `25 and 3430 cm−1 which cor` | oui |
| PMC6297187 | `aks at 3430 cm-1, belongs ` | non |
| PMC6297875 | ` of 77.9 mAh g−1 at 10 C.A` | oui |
| PMC6297875 | `.5 and 5°C min−1. Obviousl` | non |
| PMC6297875 | `1C = 118 mAh g−1) between ` | non |
| PMC6297875 | `3 is 117 mAh g−1 (de-inter` | non |
| PMC6297875 | `ate of 1°C min−1, the fila` | oui |
| PMC6297875 | `ate of 5°C min−1 is only 1` | oui |
| PMC6297875 | `bout 2.5 mg cm−2. The butt` | non |
| PMC6297875 | `e of 1–5°C min−1. And a se` | non |
| PMC6297875 | `e of 2.5°C min−1 at 800°C ` | oui |
| PMC6297875 | `e of 2.5°C min−1, the obta` | oui |
| PMC6297875 | `e of 2.5°C min−1. For the ` | non |
| PMC6297875 | `ern of 5°C min−1 sample, t` | oui |
| PMC6297875 | `is 0.05 mL min−1. Then the` | non |
| PMC6297875 | `ly 108.8 mAh g−1 at 0.05 C` | oui |
| PMC6297875 | `nly 13.0 mAh g−1 at 10 C. ` | oui |
| PMC6297875 | `of 113.4 mAh g−1 at 0.05 C` | oui |
| PMC6297875 | `of 114.0 mAh g−1 at 0.05 C` | oui |
| PMC6297875 | `of 116.2 mAh g−1 at 0.05 C` | oui |
| PMC6297875 | `ted at 1°C min−1 is even w` | oui |
| PMC6297875 | `ture, 1.5 g mL−1 PVP solut` | oui |
| PMC6301278 | `024 and 742 cm−1 could be ` |  |
| PMC6301278 | `024 and 742 cm−1), respect` |  |
| PMC6301278 | `1 and 3,374 cm−1. A peak a` |  |
| PMC6301278 | `1 and 3,374 cm−1. These pe` |  |
| PMC6301278 | `ak at 1,687 cm−1 correspon` |  |
| PMC6301278 | `ak at 3,374 cm−1 indicated` |  |
| PMC6301278 | `ak at 3,374 cm−1 indicated` |  |
| PMC6301278 | `eins (1,687 cm−1), –C–H– s` |  |
| PMC6301278 | `ks at 2,921 cm−1 could be ` |  |
| PMC6301278 | `mL xylitol (10−2 M). Then ` |  |
| PMC6301278 | `mine (1,455 cm−1) and –O– ` |  |
| PMC6301278 | `mine (2,921 cm−1), C–N str` |  |
| PMC6316361 | `00 and 3200 cm−1, which su` | oui |
| PMC6316361 | `around 1710 cm−1 (which is` | non |
| PMC6316361 | `of 400–4000 cm−1 on a Perk` | non |
| PMC6333247 | ` and 100 mW cm−2 light int` |  |
| PMC6333247 | ` at 21.1 mA cm−2, FF of 72` |  |
| PMC6333247 | ` under 8 mW cm−2 LED light` |  |
| PMC6333247 | `nder 100 mW cm−2 illuminat` |  |
| PMC6333247 | `of 20.94 mA cm−2, as displ` |  |
| PMC6333247 | `rates (15 Ω cm−2), lead io` |  |
| PMC6333247 | `with 100 mW cm−2 intensity` |  |
| PMC6369825 | ` (1,500–400 cm−1). The int` | non |
| PMC6369825 | ` PVP (8.4 × 10−5 M) were p` | oui |
| PMC6369825 | `, and (690) cm−1 correspon` | non |
| PMC6369825 | `, and 1,384 cm−1 at the fu` | oui |
| PMC6369825 | `, and 1,456 cm−1 were pres` | oui |
| PMC6369825 | `0 and 4,000 cm−1. Fourier ` | non |
| PMC6369825 | `4,000–1,500 cm−1) and the ` | non |
| PMC6369825 | `ak at 1,687 cm−1 also coul` | non |
| PMC6369825 | `ak at 2,966 cm−1 is due to` | non |
| PMC6369825 | `ide (1.25 × 10−2 M), and P` | oui |
| PMC6369825 | `ore than 10 cm−1). sugges` | non |
| PMC6369825 | `s of AgNO3 (10−3 M), sodiu` | oui |
| PMC6403542 | `and at 1345 cm−1 that show` | non |
| PMC6403542 | `ing at 1280 cm−1, the sing` | non |
| PMC6403542 | `ing at 1356 cm−1, the C=C ` | non |
| PMC6403542 | `ing at 1427 cm−1, and the ` | non |
| PMC6403542 | `ing at 1550 cm−1. On the o` | non |
| PMC6403542 | `nd at ~1595 cm−1 arising f` | non |
| PMC6403542 | `o 13 and 17 cm−1 in the C=` | oui |
| PMC6403739 | ` at 1642.67 cm−1 could be ` |  |
| PMC6403739 | ` at 3400.21 cm−1 (red-dash` |  |
| PMC6403739 | `7 and 722.5 cm−1 are attri` |  |
| PMC6403739 | `and 2842.47 cm−1 was more ` |  |
| PMC6403739 | `and 2842.47 cm−1, indicati` |  |
| PMC6409692 | `0 µL of R6G 10−3 M. After ` |  |
| PMC6409692 | `35 and 1322 cm−1. These vi` |  |
| PMC6409692 | `50 and 1650 cm−1 can be as` |  |
| PMC6409692 | `e peak 1545 cm−1; calculat` |  |
| PMC6409692 | `ed with a 3 cm−1 resolutio` |  |
| PMC6409692 | `ened by a 5 cm−1 convoluti` |  |
| PMC6409692 | `nal at 1360 cm−1, for both` |  |
| PMC6409692 | `ntration of 10−3 M (data n` |  |
| PMC6409692 | `to be 9.8 × 10−7 M (4.1 × ` |  |
| PMC6409692 | `−7 M (4.1 × 10−10mol R6G/mg` |  |
| PMC6409917 | `0, and 1560 cm-1 might be ` |  |
| PMC6409917 | `aks at 1637 cm−1 and 1243 ` |  |
| PMC6409917 | `and 0.1862 min−1 for ZnO a` |  |
| PMC6409917 | `ely 0.12 mA∙cm−2.The nanoc` |  |
| PMC6409917 | `peak at 807 cm−1 correspon` |  |
| PMC6409917 | `ue (MB, 1 × 10−5 mol/L) ph` |  |
| PMC6409917 | `−1 and 1243 cm−1 are attri` |  |
| PMC6410306 | ` ZnO (6.8 × 10−17), ZnSe (3` |  |
| PMC6410306 | ` ZnO (6.8 × 10−17), ZnSe (3` |  |
| PMC6410306 | ` of 8.79 mA·cm−2, Voc of 0` |  |
| PMC6410306 | `CdSe (6.1 × 10−36) [,] make` |  |
| PMC6410306 | `ZnSe (3.6 × 10−26), and CdS` |  |
| PMC6410306 | `ZnSe (3.6 × 10−26), and CdS` |  |
| PMC6410306 | `dSe (6.31 × 10−36) [], impl` |  |
| PMC6410306 | `of 11.30 mA·cm−2, a Voc of` |  |
| PMC6410306 | `of 11.61 mA·cm−2, a Voc of` |  |
| PMC6410306 | `of 13.46 mA·cm−2, a Voc of` |  |
| PMC6410306 | `sc = 6.7 mA·cm−2, Voc = 0.` |  |
| PMC6410306 | `te of 2 °C·min−1, with hol` |  |
| PMC6410306 | `to 20.77 mA·cm−2, leading ` |  |
| PMC6410306 | `y of 100 mW·cm−2. The inci` |  |
| PMC6443225 | `(Ag+ and AuCl −4 ) using w` |  |
| PMC6443225 | `nd at 1,023 cm−1, which is` |  |
| PMC6443225 | `nd at 3,403 cm−1 due to th` |  |
| PMC6443225 | `tio (Ag+:AuCl −4 =1.00).an` |  |
| PMC6447565 | `543 and 470 cm−1 were assi` |  |
| PMC6447565 | `90 and 3620 cm−1 are attri` |  |
| PMC6447565 | `Fe-O at 540 cm−1 are overl` |  |
| PMC6447565 | `IR (KBr,: ῡ/cm−1): 3365, 3` |  |
| PMC6447565 | `IR (KBr: ῡ /cm−1): 3528, 3` |  |
| PMC6447565 | `and at 1114 cm−1 is ascrib` |  |
| PMC6447565 | `band at 910 cm−1 is relate` |  |
| PMC6447565 | `e to 51.13 m2g−1. This res` |  |
| PMC6447565 | `er gram (emu g−1)33. As di` |  |
| PMC6447565 | `red at 1029 cm−1. Other ch` |  |
| PMC6447565 | `round 30 emu g−1. The load` |  |
| PMC6447565 | `round 47.8 m2g−1, while, C` |  |
| PMC6474109 | ` [] at 1595 cm−1. Stretchi` |  |
| PMC6474109 | ` [] at 3277 cm−1 and 3367 ` |  |
| PMC6474109 | `4 × 10−5 mol·L−1) was diss` |  |
| PMC6474109 | `9 × 10−2 mol·L−1), reactio` |  |
| PMC6474109 | `MO = 8.29 × 10−2 mol·L−1),` |  |
| PMC6474109 | `ate (9.24 × 10−5 mol·L−1) ` |  |
| PMC6474109 | `d 1130–1010 cm−1 []. These` |  |
| PMC6474109 | `eak at 1663 cm−1 as is the` |  |
| PMC6474109 | `nds at 2935 cm−1 and 1462 ` |  |
| PMC6474109 | `–Si at 1310 cm−1 and 1130–` |  |
| PMC6474109 | `−1 and 1462 cm−1, the asym` |  |
| PMC6474109 | `−1 and 3367 cm−1, and the ` |  |
| PMC6492630 | `of 0.004 dB μm–1 can be ob` |  |
| PMC6492630 | `t (0.004 dB μm–1). Therefo` |  |
| PMC6548969 | ` and 100 mW cm−2 illuminat` | oui |
| PMC6548969 | ` and 2.36 × 10−3 S m−1 for` | oui |
| PMC6548969 | ` are 3.07 × 10−4 and 2.36 ` | oui |
| PMC6548969 | ` to 24.6 mA cm−2, as the o` | oui |
| PMC6548969 | `.36 × 10−3 S m−1 for the m` | oui |
| PMC6548969 | `0.1 to 7.5 V s−1), as show` | non |
| PMC6548969 | `SI) (520 mg mL−1 in aceton` | oui |
| PMC6548969 | `and 23.0 mA cm−2 (Figure S` | oui |
| PMC6548969 | `ate of 18° min−1. The elec` | non |
| PMC6548969 | `below ≈2000 cm−1 in Fourie` | non |
| PMC6548969 | `ce of ≈3000 cm−1 and below` | non |
| PMC6548969 | `e (22.49 mA cm−2 and 61.0%` | oui |
| PMC6548969 | `o be ≈6.4 × 10−4 Pa. The f` | oui |
| PMC6548969 | `of 22.60 mA cm−2, close to` | non |
| PMC6548969 | `of 23.31 mA cm−2 and fill ` | oui |
| PMC6548969 | `te of 0.24 A s−1, and CH3N` | oui |
| PMC6548969 | `te of 0.31 A s−1. The cham` | non |
| PMC6548969 | `to be ≈1 mA cm−2, consiste` | non |
| PMC6554519 | `, and 1,124 cm−1, and the ` |  |
| PMC6554519 | `1,300–1,450 cm–1. The broa` |  |
| PMC6554519 | `2PO4 and 8 g L−1 NaCl), th` |  |
| PMC6554519 | `4 2_ at 970 cm−1 correspon` |  |
| PMC6554519 | `4 2_ at 980 cm−1 shows pho` |  |
| PMC6554519 | `82, and 535 cm–1 are assig` |  |
| PMC6554519 | `CM (0.01 mg mL−1) was deve` |  |
| PMC6554519 | `HPO4, 0.19 g L−1 KH2PO4 an` |  |
| PMC6554519 | `ately 1,636 cm−1 is associ` |  |
| PMC6554519 | `ch at 3,550 cm−1 and HOP4 ` |  |
| PMC6554519 | `f 4,000–400 cm−1 at a reso` |  |
| PMC6554519 | `ion of the PO4−3 group at ` |  |
| PMC6554519 | `lution of 4 cm−1. KBr pres` |  |
| PMC6554519 | `n band of HPO4−2 was obtai` |  |
| PMC6554519 | `nd at 2,800 cm−1 for the O` |  |
| PMC6554519 | `oeia (2.38 g L−1 Na2HPO4, ` |  |
| PMC6554519 | `y 535–1,124 cm−1, the P-O ` |  |
| PMC6562340 | `, and 1,425 cm−1 were obse` | non |
| PMC6562340 | `0 and 3,500 cm−1 was notic` | non |
| PMC6562340 | `2 and 1,632 cm−1 (Li et al` | non |
| PMC6562340 | `2 × 10−3 mol L−1), ν is th` | non |
| PMC6562340 | `9 × 10−5 cm2 s−1), C0 is t` | non |
| PMC6562340 | `= 96,485 C mol−1), D0 is t` | non |
| PMC6562340 | `e potentials J−1 vs. ω−1/2` | non |
| PMC6562340 | `eaks at 808 cm−1 correspon` | oui |
| PMC6562340 | `f O2 (1.2 × 10−3 mol L−1),` | oui |
| PMC6562340 | `ient (1.9 × 10−5 cm2 s−1),` | oui |
| PMC6562340 | `yte (0.01 m2 s−1) (Soren e` | non |
| PMC6566378 | `2 ± 0.02 eV ps–1 for this ` |  |
| PMC6600758 | ` 0.9–1.0 mg·cm−2, the elec` | oui |
| PMC6600758 | ` and 1000 mA·g−1 for the n` | oui |
| PMC6600758 | ` to 326 mA·h·g−1 for MS. T` | oui |
| PMC6600758 | `.314 J·mol−1·K−1); T is th` | non |
| PMC6600758 | `/20 (C = 1 A·g−1) for the ` | oui |
| PMC6600758 | `e from 1250 cm−1 to 1632 c` | oui |
| PMC6600758 | `e of 10 °C·min−1. X-ray ph` | non |
| PMC6600758 | `eak at 1524 cm−1 is probab` | oui |
| PMC6600758 | `f about 809 cm−1, and in t` | oui |
| PMC6600758 | `hift by 283 cm−1, suggesti` | oui |
| PMC6600758 | `ity of 50 mA·g−1 for the f` | oui |
| PMC6600758 | `m−1 to 1632 cm−1, are attr` | oui |
| PMC6600758 | `nd 2467 mA·h·g−1 for MS an` | oui |
| PMC6600758 | `o ~1204 mA·h·g−1 at the 17` | oui |
| PMC6600758 | `of 1204 mA·h·g−1 for 200 c` | oui |
| PMC6600758 | `of 1278 mA·h·g−1 and 2467 ` | oui |
| PMC6600758 | `of ~650 mA·h·g−1 was maint` | oui |
| PMC6600758 | `of ~900 mA·h·g−1 at the 10` | oui |
| PMC6600758 | `om ~650 mA·h·g−1 at the 50` | oui |
| PMC6600758 | `rates; ν (mV·s−1) and a, b` | non |
| PMC6600758 | `red at 3456 cm−1 are ascri` | non |
| PMC6600758 | `t (8.314 J·mol−1·K−1); T i` | non |
| PMC6600758 | `t (96485 C·mol−1); C is th` | non |
| PMC6600758 | `te (372 mA·h·g−1) and capa` | non |
| PMC6600758 | `te of 0.5 mV·s−1 in the ra` | oui |
| PMC6600758 | `te of 0.5 mV·s−1), is illu` | non |
| PMC6600758 | `to ~326 mA·h·g−1 at the 20` | oui |
| PMC6600758 | `ty (670 mA·h·g−1) compared` | non |
| PMC6628063 | `/mL (6.87 × 10−5 M). The e` |  |
| PMC6628063 | `1 × 108 M−1 cm−1 and ε450 ` |  |
| PMC6628063 | `2 × 105 M−1 cm−1 for the T` |  |
| PMC6628063 | `2 × 109 M−1 cm−1 for 20 nm` |  |
| PMC6628063 | `5 × 105 M−1 cm−1 was used ` |  |
| PMC6628063 | `= 1.42 × 105 M−1 cm−1 for ` |  |
| PMC6628063 | `= 2.25 × 105 M−1 cm−1 was ` |  |
| PMC6628063 | `= 5.41 × 108 M−1 cm−1 and ` |  |
| PMC6628063 | `= 9.92 × 109 M−1 cm−1 for ` |  |
| PMC6631201 | ` (S/N), 0.1 Vs−1 was recom` | oui |
| PMC6631201 | `6 × 10−6 cm2 s−1 []), v de` | non |
| PMC6631201 | `8 V at 100 mVs−1 for both ` | non |
| PMC6631201 | `8.6 μA mM−1 cm−2). Chen et` | non |
| PMC6631201 | `N)6] (7.6 × 10−6 cm2 s−1 [` | non |
| PMC6631201 | `ning rate (V s−1), A denot` | non |
| PMC6631201 | `ration (mol cm−3). The eff` | non |
| PMC6631201 | `rsion (1 mg mL−1) and disp` | oui |
| PMC6631201 | `te of 1 mL min−1, and agit` | oui |
| PMC6631201 | `y (418.6 μA mM−1 cm−2). Ch` | non |
| PMC6678425 | ` and ~499.7 cm−1 are index` | non |
| PMC6678425 | `and ~1592.6 cm−1 (G band o` | non |
| PMC6678425 | `and ~1592.6 cm−1, which si` | oui |
| PMC6678425 | `m−1, ~244.5 cm−1, ~499.7 c` | oui |
| PMC6678425 | `m−1, ~499.7 cm−1, ~1351.2 ` | oui |
| PMC6678425 | `s of ~115.4 cm−1, ~244.5 c` | oui |
| PMC6678425 | `−1, ~1351.2 cm−1 and ~1592` | oui |
| PMC6688992 | ` of 99.3 mW cm−2, the samp` | non |
| PMC6688992 | `.077 ± (5 × 10−3) μA for I` | oui |
| PMC6688992 | `.3 ± 0.6 mW cm−2 to the sa` | oui |
| PMC6688992 | `.827 ± (5 × 10−3) μA and 2` | oui |
| PMC6688992 | `18 ± (1.7 × 10−3) μA and 1` | oui |
| PMC6688992 | `3637 ± (5 × 10−4) and 0.63` | oui |
| PMC6688992 | `56 ± (1.0 × 10−3) μA, resp` | oui |
| PMC6688992 | `6363 ± (5 × 10−4), respect` | oui |
| PMC6688992 | `e 1–10 cm2 V s−1, similar ` | non |
| PMC6688992 | `e of 10 °C min−1 in the 12` | oui |
| PMC6688992 | `e of 10 °C min−1 to 180 °C` | oui |
| PMC6688992 | `e of 10 °C min−1, and was ` | oui |
| PMC6688992 | `ity 99.3 mW cm−2; the form` | non |
| PMC6688992 | `round 10 µA cm−2. Addition` | non |
| PMC6694146 | ` constant (min−1)19.Photoc` | non |
| PMC6694146 | ` of 0.0039 min−1; MgAC-Fe3` | non |
| PMC6694146 | `of ~0.1175 min−1; this was` | non |
| PMC6694146 | `se to 0.036 (h−1) (Fig. 2b` | oui |
| PMC6694146 | `te of 0.032 (h−1) (Fig. 2a` | oui |
| PMC6702676 | ` (701.7 mA h g−1 after 600` | oui |
| PMC6702676 | ` 1, 1.5, 2 A g−1, respecti` | non |
| PMC6702676 | ` 71% at 2 mV·s−1.The capac` | non |
| PMC6702676 | ` around 500 cm−1 in ZnSe@N` | oui |
| PMC6702676 | ` is 530 mA h g−1 at 0.5 A ` | oui |
| PMC6702676 | ` of 0.2–2 mV s−1 in LIBs a` | non |
| PMC6702676 | ` of 382 mA h g−1 at 0.5 A ` | oui |
| PMC6702676 | ` than 8.1 m2 g−1 of ZnSe@N` | oui |
| PMC6702676 | `0 and 1,586 cm−1, which ar` | non |
| PMC6702676 | `1,214.0 mA h g−1 and 447.5` | oui |
| PMC6702676 | `1,226.1 mA h g−1 after 200` | oui |
| PMC6702676 | `5, 2, 3, 5 A g−1, and reco` | oui |
| PMC6702676 | `5A at 0.2 mV s−1. The obvi` | non |
| PMC6702676 | `72.9% at 2 A g−1. And ther` | non |
| PMC6702676 | `Bs at 0.5 mV·s−1 are calcu` | oui |
| PMC6702676 | `Fs with 0.1 Ag−1 for the f` | non |
| PMC6702676 | `N-CNFs at 2 Ag−1 with volt` | oui |
| PMC6702676 | `ack to 0.1 A g−1, the capa` | oui |
| PMC6702676 | `ack to 0.2 A g−1, respecti` | oui |
| PMC6702676 | `ack to 0.2 A g−1. Because ` | non |
| PMC6702676 | `ased to 2 mV·s−1, the capa` | oui |
| PMC6702676 | `d 228.9 mA h g−1 when the ` | oui |
| PMC6702676 | `d 323.3 mA h g−1 at curren` | oui |
| PMC6702676 | `d 362.3 mA h g−1, respecti` | oui |
| PMC6702676 | `d 365.6 mA h g−1 after 200` | oui |
| PMC6702676 | `d 368.9 mA h g−1 after 200` | oui |
| PMC6702676 | `d 447.5 mA h g−1 in LIBs a` | non |
| PMC6702676 | `d 455.0 mA h g−1 in LIBs a` | non |
| PMC6702676 | `d 570.9 mA h g−1 at 0.1, 0` | oui |
| PMC6702676 | `e 984.7 mA h g−1 and 81.3%` | oui |
| PMC6702676 | `e of 0.1–2 A g−1, and the ` | non |
| PMC6702676 | `ed at 0.2 mV s−1. As shown` | non |
| PMC6702676 | `f 1,134 mA·h·g−1 at 0.6 A·` | non |
| PMC6702676 | `f 446.2 mA h g−1 with init` | oui |
| PMC6702676 | `f 701.7 mA h g−1 after 600` | oui |
| PMC6702676 | `g−1 at 0.1 A g−1 after 50 ` | non |
| PMC6702676 | `g−1 at 0.5 A g−1 after 100` | non |
| PMC6702676 | `g−1 at 0.5 A g−1 after 180` | non |
| PMC6702676 | `g−1 at 0.6 A·g−1 after 500` | non |
| PMC6702676 | `h g−1 at 5 A g−1, and reco` | oui |
| PMC6702676 | `m 0.1 to 5 A g−1. The ZnSe` | non |
| PMC6702676 | `nd 26.4 mA h g−1 at 5 A g−` | oui |
| PMC6702676 | `nd 99.4 mA h g−1 at the sa` | oui |
| PMC6702676 | `nged to 0.1A g−1, the capa` | non |
| PMC6702676 | `nsity of 2 A g−1. It is ex` | non |
| PMC6702676 | `o 455.0 mA h g−1. Moreover` | non |
| PMC6702676 | `o 822.7 mA h g−1 when the ` | oui |
| PMC6702676 | `ode at 0.1 A g−1 at first ` | non |
| PMC6702676 | `s 259.5 mA h g−1 at 0.1 A ` | oui |
| PMC6702676 | `s 365.6 mA h g−1 after 200` | oui |
| PMC6702676 | `s is 30.2 m2 g−1, higher t` | oui |
| PMC6702676 | `s set to 2 A g−1, the ZnSe` | non |
| PMC6702676 | `t 701.7 mA h g−1 after 600` | oui |
| PMC6702676 | `te of 10°C min−1) in a tub` | oui |
| PMC6702676 | `te of 10°C min−1. The Rama` | non |
| PMC6702676 | `ty (372 mA h g−1) of the c` | non |
| PMC6702676 | `ycles at 2 A g−1, and the ` | non |
| PMC6720160 | ` cm−1, 1474 cm−1 and 1443 ` | oui |
| PMC6720160 | `1 from 3435 cm−1 of TPPS4.` | non |
| PMC6720160 | `18 and 1026 cm−1 are attri` | oui |
| PMC6720160 | `PH2 at 3315 cm−1, 1474 cm−` | oui |
| PMC6720160 | `and at 1595 cm−1 are assig` | non |
| PMC6720160 | `eak at 1419 cm−1 and a med` | non |
| PMC6720160 | `eak at 2519 cm−1 in the Cu` | oui |
| PMC6720160 | `eak at 3436 cm−1 was forme` | non |
| PMC6720160 | `ift to 1577 cm−1 of the –C` | oui |
| PMC6720160 | `nds at 1584 cm−1 in the co` | non |
| PMC6720160 | `nds at 3127 cm−1 and 1595 ` | non |
| PMC6720160 | `str at 1401 cm−1 band in t` | non |
| PMC6720160 | `ted to 3376 cm−1 from 3435` | non |
| PMC6720160 | `ved at 1570 cm−1 in the GS` | non |
| PMC6720160 | `−1 and 1443 cm−1 assigned ` | oui |
| PMC6720160 | `−1 and 1595 cm−1 on the GS` | non |
| PMC6722878 | ` of 300 mm min−1 at room t` | oui |
| PMC6722878 | ` was 50 mm·min−1. The cros` | non |
| PMC6722878 | `a of 1466 m2 g−1 with a po` | oui |
| PMC6769153 | `, 1023, 859 cm−1 can be as` | non |
| PMC6769153 | `21 and 2851 cm−1 gradually` | oui |
| PMC6769153 | `21 and 2851 cm−1 in FTIR s` | non |
| PMC6769153 | `21 and 2851 cm−1, respecti` | oui |
| PMC6769153 | `97 and 1027 cm−1 can be as` | non |
| PMC6769153 | `d) and 1582 cm−1 (G-band),` | oui |
| PMC6779780 | `50 ml, 10 mg L−1) by conti` | oui |
| PMC6779780 | `ate of 5°C min−1. The prod` | non |
| PMC6779780 | `of 0.02751 min−1, being 1.` | oui |
| PMC6804187 | ` around 6 × 10−8 mbar. An ` |  |
| PMC6804187 | `ce, a 600 g mm−1 grating a` |  |
| PMC6804187 | `r vacuum of 10−6 Torr two ` |  |
| PMC6804187 | `t 2596−2573 cm−1, correspo` |  |
| PMC6812203 | ` around 400 cm−1, which ma` | non |
| PMC6812203 | ` around 800 cm−1 exists be` | non |
| PMC6812203 | ` around 950 cm−1 may be ca` | non |
| PMC6812203 | `around 1600 cm−1, which co` | oui |
| PMC6812203 | `e 3740–3500 cm−1, as shown` | oui |
| PMC6812203 | `t 3380–3310 cm−1, and beca` | non |
| PMC6814701 | `00 and 1300 cm−1 to C–O st` | non |
| PMC6814701 | `1600 to 500 cm−1 are ident` | non |
| PMC6814701 | `35 and 1160 cm−1 are relat` | non |
| PMC6814701 | `4500 to 500 cm−1.X-ray Pho` | non |
| PMC6814701 | `aks at 1594 cm−1 correspon` | non |
| PMC6814701 | `and at 1020 cm−1 to alipha` | non |
| PMC6814701 | `and at 1235 cm−1 are speci` | non |
| PMC6814701 | `around 3250 cm−1 are assoc` | non |
| PMC6814701 | `e of 3.54 × 10−3/s, Fig. 1` | oui |
| PMC6814701 | `enols; 1723 cm−1 is shifte` | non |
| PMC6814701 | `n of 3.33 × 10−5 M, was an` | oui |
| PMC6814701 | `nge of 1331 cm−1 in the wi` | non |
| PMC6814701 | `on, at 1705 cm−1 to ketone` | non |
| PMC6814701 | `s is 8.24 × 10−3s to AuMt1` | oui |
| PMC6837232 | ` exceeds 3 g l−1. These re` | non |
| PMC6837232 | ` ml of 1 mol l−1 HCl was m` | oui |
| PMC6837232 | ` ml of 2 mol l−1 ammonia w` | oui |
| PMC6837232 | ` of 0.69 kGy h−1 and the c` | oui |
| PMC6837232 | ` of 0.69 kGy h−1 for 1 h. ` | non |
| PMC6837232 | ` of 0.69 kGy h−1. The prep` | non |
| PMC6837232 | `.04–13.83 m2 g−1 and 23.1–` | oui |
| PMC6837232 | `ained at 1 g l−1 and the s` | non |
| PMC6837232 | `alyst is 1 g l−1, the deco` | oui |
| PMC6837232 | `ate of 2 kGy r−1. The ultr` | non |
| PMC6837232 | `ation (2 kGy r−1). The abs` | non |
| PMC6837232 | `ation of 1 g l−1; further ` | non |
| PMC6837232 | `epared 20 mg l−1 methyl or` | oui |
| PMC6837232 | `ion to 50 mg l−1. Although` | non |
| PMC6837232 | `lyst was 1 g l−1. The UV–v` | non |
| PMC6837232 | `n was 1.35 g l−1 and the T` | non |
| PMC6837232 | `on was 50 mg l−1, and the ` | oui |
| PMC6837232 | `r, the 20 mg l−1 methyl or` | oui |
| PMC6837232 | `sing a 20 mg l−1 methyl or` | oui |
| PMC6837232 | `site was 3 g l−1. At this ` | non |
| PMC6837232 | `tion was 1 g l−1, the 0.35` | oui |
| PMC6837232 | `tion was 1 g l−1, the meth` | oui |
| PMC6837232 | `tion was 1 g l−1, which is` | oui |
| PMC6837232 | `value of 3 g l−1, there ar` | oui |
| PMC6837232 | `values (μmol J−1) of each ` | non |
| PMC6837232 | `were 59.3 m2 g−1 and 19.3 ` | oui |
| PMC6837232 | `with a 20 mg l−1 methyl or` | oui |
| PMC6864515 | `2 and 0.6 mL h−1, respecti` | oui |
| PMC6864515 | `38 and 1535 cm−1, a distin` | oui |
| PMC6864515 | `50 and 2996 cm−1, and an e` | oui |
| PMC6864515 | `O−C at 1078 cm−1. FT‐IR sp` | oui |
| PMC6864515 | `eak at 1726 cm−1. Also at ` | oui |
| PMC6864515 | `eak at 1733 cm−1, and a de` | oui |
| PMC6864515 | `ile at 1148 cm−1 an ester‐` | oui |
| PMC6864515 | `lso at 1614 cm−1 is the ab` | oui |
| PMC6864515 | `peed of 5° min−1. The morp` | non |
| PMC6899919 | ` of 0.05 mol L−1) added to` |  |
| PMC6913939 | ` 1020, 1144 cm−1 and prima` | oui |
| PMC6913939 | `500 to 3800 cm−1. All samp` | non |
| PMC6913939 | `ence at 520 cm−1. The spec` | non |
| PMC6913939 | `ety at 1141 cm−1. Detailed` | non |
| PMC6913939 | `rate γ = 100 s−1 was appli` | non |
| PMC6915586 | `/mL (6.12 × 10−5 M), while` |  |
| PMC6915586 | `3, and 2878 cm−1 in Y-CDs’` |  |
| PMC6915586 | `32 and 2767 cm−1 represent` |  |
| PMC6915586 | `63 and 1551 cm−1 correspon` |  |
| PMC6915586 | `8, and 1233 cm−1 (C–O). Th` |  |
| PMC6915586 | `841 and 672 cm−1 of both C` |  |
| PMC6915586 | `eak at 3046 cm−1 in R-CDs’` |  |
| PMC6926885 | ` X of 720 m2·g−1 [], but m` |  |
| PMC6926885 | ` at 1639.94 cm−1 ascribed ` |  |
| PMC6926885 | ` at 3470.94 cm−1 is attrib` |  |
| PMC6926885 | ` of 12.12 m2·g−1.3.3. Effe` |  |
| PMC6926885 | `D6R, 561.21 cm−1) and a be` |  |
| PMC6926885 | `be 486.46 m2·g−1, lower th` |  |
| PMC6926885 | `e of 350 r·min−1 for 10 h.` |  |
| PMC6926885 | `e of 350 r·min−1 for 4 h, ` |  |
| PMC6926885 | `m−1 to 4000 cm−1. In addit` |  |
| PMC6926885 | `ng from 400 cm−1 to 4000 c` |  |
| PMC6926885 | `ode (666.08 cm−1), double ` |  |
| PMC6926885 | `ode (973.24 cm−1), symmetr` |  |
| PMC6926885 | `of 11.5 °C·min−1 for 3 h. ` |  |
| PMC6926885 | `ond (460.11 cm−1), are obs` |  |
| PMC6926885 | `out 12.12 m2·g−1, as shown` |  |
| PMC6928214 | `t 1200–1300 cm−1 is the ab` |  |
| PMC6928214 | `t 2500–2600 cm−1 indicated` |  |
| PMC6928214 | `t about 750 cm−1 confirms ` |  |
| PMC6928996 | `), and 3420 cm−1 (N-H stre` | non |
| PMC6928996 | `450 to 4000 cm−1. The char` | non |
| PMC6928996 | `he 600–1100 cm−1 region. T` | non |
| PMC6928996 | `hing), 1652 cm−1 (C=O grou` | non |
| PMC6928996 | `t 2800-2950 cm−1 (C-H stre` | non |
| PMC6928996 | `und at 1063 cm−1. In addit` | non |
| PMC6955683 | `e of 14,104 cm−1 (circa 70` | non |
| PMC6955683 | `rs at 14535 cm−1 (c.a. 688` | non |
| PMC6960519 | ` area 425 m2 g−1, SAR = 50` |  |
| PMC6960519 | ` at 200 mL min−1 for 4 h. ` |  |
| PMC6960519 | `SA of 294 m2 g−1 and an al` |  |
| PMC6960519 | `and 0.46 cm3 g−1 in sample` |  |
| PMC6960519 | `and 50 cm3 min−1 synthetic` |  |
| PMC6960519 | `e of 10 °C min−1 under hel` |  |
| PMC6960519 | `e of 30 mL min−1, and then` |  |
| PMC6960519 | `e of 40 °C min−1.3. Result` |  |
| PMC6960519 | `nd 3131 μmol g−1 in the al` |  |
| PMC6960519 | `ned at 0.02° s−1. 2.3.2. N` |  |
| PMC6960519 | `of 2 µm Hg min−1.2.3.3. Te` |  |
| PMC6960519 | `rom 0.14 cm3 g−1 in zeo1 (` |  |
| PMC6960519 | `rom 502 μmol g−1 in the un` |  |
| PMC6960519 | `with 40 °C min−1 heating r` |  |
| PMC6994313 | ` (1730–1700 cm−1) are not ` | non |
| PMC6994313 | ` and 1471.5 cm−1 which can` | non |
| PMC6994313 | `26.1–2851.7 cm−1 is attrib` | non |
| PMC6994313 | `e of 10 °C min−1 under an ` | oui |
| PMC6994313 | `rom 830–725 cm−1. The char` | non |
| PMC7014116 | ` around 960 cm−1 which cor` | oui |
| PMC7014116 | ` bond; 1447 cm−1, which ca` | non |
| PMC7014116 | ` cm−1, 2990 cm−1, and 2878` | oui |
| PMC7014116 | `1, and 1041 cm−1 respectiv` | oui |
| PMC7014116 | `1, and 2878 cm−1, which ca` | non |
| PMC7014116 | `3 cm−1, 957 cm−1, and 1041` | oui |
| PMC7014116 | `and at 1045 cm−1 (δC–CH3),` | non |
| PMC7014116 | `and at 1088 cm−1 (νC–O–C),` | non |
| PMC7014116 | `and at 1457 cm−1 can be at` | non |
| PMC7014116 | `and at 1755 cm−1 can be at` | non |
| PMC7014116 | `ands at 585 cm−1 and 428 c` | oui |
| PMC7014116 | `asCH3); 887 cm−1, which ca` | non |
| PMC7014116 | `band at 871 cm−1 correspon` | non |
| PMC7014116 | `chain; 1762 cm−1, which ca` | non |
| PMC7014116 | `he 4000–600 cm−1 region. T` | oui |
| PMC7014116 | `lution of 4 cm−1 in the 40` | oui |
| PMC7014116 | `m−1 and 428 cm−1 which can` | oui |
| PMC7014116 | `nds at 1184 cm−1 and 1089 ` | non |
| PMC7014116 | `nds at 2998 cm−1 and 2947 ` | oui |
| PMC7014116 | `of 600–1100 cm−1 with the ` | non |
| PMC7014116 | `rved at 603 cm−1, 957 cm−1` | oui |
| PMC7014116 | `ved at 2995 cm−1, 2990 cm−` | oui |
| PMC7014116 | `−1 and 1089 cm−1, respecti` | non |
| PMC7014116 | `−1 and 2947 cm−1 can be at` | oui |
| PMC7022538 | `H. The 1560 cm−1 peak was ` | non |
| PMC7022538 | `eak at 1221 cm−1 was attri` | non |
| PMC7022538 | `eak at 1338 cm−1 was attri` | non |
| PMC7022538 | `eak at 1483 cm−1 was attri` | non |
| PMC7022538 | `eak at 2884 cm−1 was attri` | non |
| PMC7022538 | `eak at 3069 cm−1 was attri` | non |
| PMC7022538 | `eak at 3278 cm−1 can be at` | non |
| PMC7024153 | `07 and 2851 cm−1, separate` |  |
| PMC7024153 | `20 and 3300 cm−1, which wa` |  |
| PMC7024153 | `eak at 1363 cm−1 was due t` |  |
| PMC7024153 | `eak at 1640 cm−1 could be ` |  |
| PMC7033158 | ` = 0.0039 min−1), 48.36% ` | oui |
| PMC7033158 | ` = 0.0055 min−1) and 58.3` | oui |
| PMC7033158 | ` = 0.0070 min−1) of RhB w` | oui |
| PMC7033158 | ` = 0.0124 min−1), 88.03% ` | oui |
| PMC7033158 | ` = 0.0173 min−1) and 94.1` | oui |
| PMC7033158 | ` Methods (P Po−1 = 0.05–0.` | oui |
| PMC7033158 | ` and 202 W m−2 for visib` | oui |
| PMC7033158 | ` and 505 m² g−1 - AgNPs-F` | non |
| PMC7033158 | `(0.001 mol L−1, Synth, P` | oui |
| PMC7033158 | `(0.002 mol L−1, Neon, PA` | oui |
| PMC7033158 | `, 0.05 mol L−1, Synth, P` | oui |
| PMC7033158 | `, 24.25 mg L−1 RhB conce` | oui |
| PMC7033158 | `1 to 304 m² g−1 - TiNPs-F` | non |
| PMC7033158 | `25) (56 m2 g−1) nanocata` | non |
| PMC7033158 | `3] = 0.7 g L−1 and [RhB]` | oui |
| PMC7033158 | `4, 0.2 mol L−1, Neon, PA` | oui |
| PMC7033158 | `BET (505 m² g−1), while T` | non |
| PMC7033158 | `B] = 20 mg L−1) in dark ` | oui |
| PMC7033158 | `O3 (158 m2 g−1) and TiO2` | non |
| PMC7033158 | `O3, (304 m² g−1), while F` | non |
| PMC7033158 | `ed at 3394 cm−1 strip, is` | oui |
| PMC7033158 | `ere 1.41 g L−1 to Fe2O3 ` | oui |
| PMC7033158 | `ion (20 mg L−1, 61.8 W ` | oui |
| PMC7033158 | `k = 0.022 min−1) of RhB w` | oui |
| PMC7033158 | `le the 1620 cm−1 strip is ` | oui |
| PMC7033158 | `me (1.6 cm³ g−1). In addi` | non |
| PMC7033158 | `rate 10 °C min−1) for 4 h` | oui |
| PMC7033158 | `rea (158 m² g−1 to 304 m` | non |
| PMC7033158 | `te of 1 drop s−1), forming` | non |
| PMC7033158 | `ved at 611 cm−1 correspon` | oui |
| PMC7033158 | `wed at 590 cm−1 due to th` | oui |
| PMC7033158 | `−1, 61.8 W m−2 for UV ir` | oui |
| PMC7039937 | ` 1,253.97 m2·g−1. The larg` |  |
| PMC7039937 | ` from 3.2 × 10−7S·cm2·s−1 ` |  |
| PMC7039937 | ` is 13.51 × 10−2 S·cm−1 at` |  |
| PMC7039937 | ` × 10−7S·cm2·s−1 to 0.85 ×` |  |
| PMC7039937 | `, and 1,600 cm−1 can be at` |  |
| PMC7039937 | `. DK (in cm2 s−1) denotes ` |  |
| PMC7039937 | `000 and 400 cm−1 in air. T` |  |
| PMC7039937 | `1 to 0.85 × 10−7 S·cm2·s−1` |  |
| PMC7039937 | `10−2−10−1 S·cm−1) and exce` |  |
| PMC7039937 | `12 × 10−2 S·cm−1 (at room ` |  |
| PMC7039937 | `2 × 105 S·s·cm−3, 14.3-tim` |  |
| PMC7039937 | `2 × 105 S·s·cm−3, 14.3-tim` |  |
| PMC7039937 | `26 × 10−2 S·cm−1 at 20°C, ` |  |
| PMC7039937 | `51 × 10−2 S·cm−1 at 80°C. ` |  |
| PMC7039937 | `8 and 1,080 cm−1 correspon` |  |
| PMC7039937 | `d to 4.12 × 10−2 S·cm−1 (a` |  |
| PMC7039937 | `e is 7.26 × 10−2 S·cm−1 at` |  |
| PMC7039937 | `ed at 5 mm min−1. At least` |  |
| PMC7039937 | `ivity (10−2−10−1 S·cm−1) a` |  |
| PMC7039937 | `ly at 1,680 cm−1 which bel` |  |
| PMC7039937 | `nd at 1,712 cm−1 for pure ` |  |
| PMC7039937 | `nd at 2,230 cm−1 in all th` |  |
| PMC7039937 | `nductivity (10−2−10−1 S·cm` |  |
| PMC7039937 | `on at 1,243 cm−1 in the co` |  |
| PMC7039937 | `te of 20°C min−1. The tens` |  |
| PMC7039937 | `tested from 10−1 to 106 Hz` |  |
| PMC7039937 | `× 10−7 S·cm2·s−1, and the ` |  |
| PMC7075133 | `cy range of 10−1–106 Hz wi` |  |
| PMC7075133 | `he range of 10−1 to 105 Hz` |  |
| PMC7075151 | `and at 1749 cm−1 is corres` | oui |
| PMC7075151 | `and at 3202 cm−1 is assign` | oui |
| PMC7075151 | `t 1605–1307 cm−1, they are` | non |
| PMC7078890 | ` to 2.00 mg mL−1) of BNS3 ` | non |
| PMC7078890 | ` to 2.00 mg mL−1), dimethy` | oui |
| PMC7078890 | `0 cm−1, 906 cm−1, and 1033` | non |
| PMC7078890 | `00 to 1100, cm−1 were attr` | non |
| PMC7078890 | `1, and 1033 cm−1 attribute` | non |
| PMC7078890 | `30 and 1450 cm−1 are the r` | non |
| PMC7078890 | `400 to 4000 cm−1, and 16 s` | non |
| PMC7078890 | `600 to 3100 cm−1 (Figure 2` | non |
| PMC7078890 | `603 and 569 cm−1 describes` | non |
| PMC7078890 | `O4−3 at 630 cm−1 into BNS ` | non |
| PMC7078890 | `aks at 1093 cm−1 are descr` | non |
| PMC7078890 | `and at 1740 cm−1 correspon` | non |
| PMC7078890 | `eak at 1220 cm−1, 906 cm−1` | non |
| PMC7078890 | `lution of 4 cm−1 and a fre` | non |
| PMC7078890 | `nfirmed by PO4−3 at 630 cm` | non |
| PMC7078890 | `oltage, 7 × 10−2 bar press` | oui |
| PMC7078890 | `peak at 947 cm−1 is due to` | non |
| PMC7078890 | `t 2950–2850 cm−1 expresses` | non |
| PMC7078890 | `tion at 412 cm−1 is the ch` | non |
| PMC7116022 | `0–50 000 g mol–1, which ro` |  |
| PMC7116022 | `1 × 10–4 mg ml–1, without ` |  |
| PMC7116022 | `from ∼26 mg ml–1 to ∼1 × 1` |  |
| PMC7116022 | `l–1 to ∼1 × 10–4 mg ml–1, ` |  |
| PMC7178313 | `3 eV = 1855 cm−1) is relat` | non |
| PMC7181732 | ` band (2685 cm−1), D + D′ ` | oui |
| PMC7181732 | ` band (2935 cm−1) and 2D′ ` | oui |
| PMC7181732 | ` band (3202 cm−1). The app` | non |
| PMC7181732 | ` cm−1, 1170 cm−1, 1565 cm−` | oui |
| PMC7181732 | ` cm−1, 1220 cm−1 and 980 c` | non |
| PMC7181732 | ` cm−1, 1260 cm−1 and 795 c` | oui |
| PMC7181732 | ` cm−1, 1365 cm−1, 1220 cm−` | non |
| PMC7181732 | ` cm−1, 1565 cm−1, 1660 cm−` | oui |
| PMC7181732 | ` cm−1, 1660 cm−1 and 3220 ` | oui |
| PMC7181732 | `4 cm−1 2920 cm−1 attribute` | non |
| PMC7181732 | `aks at 1560 cm−1, 1260 cm−` | oui |
| PMC7181732 | `aks at 1580 cm−1 and 1605 ` | oui |
| PMC7181732 | `and at 1345 cm−1 caused by` | oui |
| PMC7181732 | `and at 1580 cm−1 originati` | non |
| PMC7181732 | `ands at 740 cm−1, 1170 cm−` | oui |
| PMC7181732 | `d from 1580 cm−1 to 1605 c` | oui |
| PMC7181732 | `let at 3422 cm−1 and 3306 ` | oui |
| PMC7181732 | `m−1 and 795 cm−1 correspon` | oui |
| PMC7181732 | `m−1 and 980 cm−1 related t` | non |
| PMC7181732 | `m−1 to 1605 cm−1 due to ox` | oui |
| PMC7181732 | `nds at 1404 cm−1 2920 cm−1` | non |
| PMC7181732 | `t 2970–3700 cm−1, 1365 cm−` | non |
| PMC7181732 | `to be ~265 m2g−1. This val` | non |
| PMC7181732 | `−1 and 1605 cm−1 are simul` | oui |
| PMC7181732 | `−1 and 3220 cm−1 related t` | oui |
| PMC7181732 | `−1 and 3306 cm−1 along wit` | oui |
| PMC7182996 | `34 and 1641 cm−1 were reco` |  |
| PMC7182996 | `35 and 1390 cm−1 were prev` |  |
| PMC7182996 | `41 and 1435 cm−1 peaks are` |  |
| PMC7182996 | `43 and 1044 cm−1 were only` |  |
| PMC7182996 | `67 and 3281 cm−1, 1634 and` |  |
| PMC7182996 | `and 3249.83 cm−1 were reco` |  |
| PMC7182996 | `around 1635 cm−1 could be ` |  |
| PMC7182996 | `ly and 3279 cm−1, 3297 and` |  |
| PMC7182996 | `t 3550–3200 cm−1 might be ` |  |
| PMC7184584 | `C), C (mmol ml−1)] was des` | non |
| PMC7184584 | `C, 0.4 mmol ml−1]. The X-r` | non |
| PMC7184584 | `C, 0.8 mmol ml−1]) was cha` | non |
| PMC7184584 | `an 1.2 mmol ml−1.Identify ` | non |
| PMC7184584 | `ter C (mmol ml−1), which r` | oui |
| PMC7184584 | `to 1.0 mmol ml−1. The high` | non |
| PMC7254238 | ` of 600–400 cm−1 [,]. No o` |  |
| PMC7254238 | ` νH2O), 794 cm−1 (lattice ` |  |
| PMC7254238 | `(HOH), 1308 cm−1 (νsym (O=` |  |
| PMC7254238 | `(OCO)), 915 cm−1 (δ(OCO))]` |  |
| PMC7254238 | `=C–O), 1051 cm−1 (ν(C–O))]` |  |
| PMC7254238 | `e of 10 °C min−1 for time ` |  |
| PMC7254238 | `es [600–400 cm−1: ν(La–O) ` |  |
| PMC7254238 | `igand: 1445 cm−1 (νsym (OC` |  |
| PMC7254238 | `igand: 1642 cm−1 (νasym (O` |  |
| PMC7254238 | `ion in 5 mg mL−1 LaFeO3 su` |  |
| PMC7254238 | `of 4000–400 cm−1. Thermal ` |  |
| PMC7254238 | `te of 10 K min−1 using a N` |  |
| PMC7254238 | `tion of 3 ng L−1 was repor` |  |
| PMC7254238 | `w of 20 mL min−1 and heati` |  |
| PMC7254238 | `water [3410 cm−1 (νOH, νH2` |  |
| PMC7254336 | ` (0.249 mmol·g−1) estimate` | non |
| PMC7254336 | ` (2.847 mmol·g−1, 11.94 g,` | oui |
| PMC7254336 | ` (6.075 mmol·g−1, 4.94 g, ` | oui |
| PMC7254336 | ` (7.914 mmol·g−1, 0.38 g, ` | oui |
| PMC7254336 | ` (9.048 mmol·g−1, 3.32 g, ` | oui |
| PMC7254336 | ` mL (g-sample)−1) in a 200` | oui |
| PMC7254336 | `(11.980 mmol·g−1, 0.26 g, ` | oui |
| PMC7254336 | `, 2.691 mmol·g−1, 1.26 g, ` | oui |
| PMC7254336 | `.224 mmol-Al g−1) determin` | non |
| PMC7254336 | `0 cm3(NTP) min−1 and then ` | non |
| PMC7254336 | `0 cm3(NTP) min−1, acting a` | non |
| PMC7254336 | `0.1–13.4 mol·L−1 HNO3 solu` | oui |
| PMC7254336 | `20 g-cat h mol−1 in these ` | non |
| PMC7254336 | `d with 2 mol·L−1 HNO3 in a` | oui |
| PMC7254336 | `e of 10 °C·min−1 under air` | oui |
| PMC7254336 | `h a 13.4 mol·L−1 HNO3 solu` | oui |
| PMC7254336 | `ow (30 cm3·min−1). The wei` | oui |
| PMC7254336 | `th a 2.0 mol·L−1 HNO3 solu` | oui |
| PMC7279382 | `ate of 50 mV s−1, and EIS ` | non |
| PMC7279382 | `hanged from 10−2 to 105 Hz` | oui |
| PMC7279382 | `ient (7.6 × 10−6 cm2/s); t` | non |
| PMC7285084 | `C = 7400 g mol−1, Ð = 1.49` | oui |
| PMC7285084 | `e of 10 °C min−1 under a n` | oui |
| PMC7285084 | `e of 10 °C min−1 under a n` | oui |
| PMC7285084 | `ion of 2 mg mL−1, then wat` | oui |
| PMC7285084 | `on of 10 mg mL−1. The mixe` | non |
| PMC7285084 | `on of 10 mg mL−1. The solu` | non |
| PMC7285084 | `on of 20 mg mL−1 and used ` | non |
| PMC7285084 | `se in 0.2 mL h−1 and the m` | oui |
| PMC7285084 | `th 0.35 mL min−1 at 40 °C.` | oui |
| PMC7285084 | `w of 20 mL min−1. The CD s` | non |
| PMC7285084 | `was 7400 g mol−1 (Ð = 1.49` | oui |
| PMC7285084 | `was 8100 g mol−1 (Ð = 1.44` | oui |
| PMC7289851 | ` glass (27 m2g−1, 0.2 μm):` |  |
| PMC7289851 | `-alumina is 10−3 S cm−1 at` |  |
| PMC7289851 | `a is 10−3 S cm−1 at room t` |  |
| PMC7289851 | `area of 5 m2 g−1 (average ` |  |
| PMC7289851 | `lumina (45 m2g−1, 0.1 μm):` |  |
| PMC7289851 | `ty of 10−5 Scm−1 at room t` |  |
| PMC7289851 | `uctivity of 10−5 Scm−1 at ` |  |
| PMC7321157 | `nts (p/p0 = 10−9–10−7). Th` |  |
| PMC7321157 | `p/p0 = 10−9–10−7). The rat` |  |
| PMC7321157 | `speed 0.1° min−1.4.3. Meas` |  |
| PMC7344730 | ` 977 to 983 cm−1 correspon` |  |
| PMC7344730 | ` about 1575 cm−1 for C = N` |  |
| PMC7344730 | ` and 100 mAh g−1 at 2 C, a` |  |
| PMC7344730 | ` and 100 mAh g−1 for LiFeP` |  |
| PMC7344730 | `0 and ~1590 cm−1 in Figure` |  |
| PMC7344730 | `0) and 1299 cm−1 for C-N s` |  |
| PMC7344730 | `058 and 977 cm−1 correspon` |  |
| PMC7344730 | `1 C, 120 mAh g−1 at 1C and` |  |
| PMC7344730 | `144 and 708 cm−1 are assig` |  |
| PMC7344730 | `299 to 1307 cm−1 for the C` |  |
| PMC7344730 | `4 and 95 mAh g−1 for pure ` |  |
| PMC7344730 | `4 is 120 mAh g−1 and that ` |  |
| PMC7344730 | `4 is 120 mAh g−1. The theo` |  |
| PMC7344730 | `4 is 170 mAh g−1. The coul` |  |
| PMC7344730 | `486 to 1505 cm−1 for the C` |  |
| PMC7344730 | `575 to 1592 cm−1 for the C` |  |
| PMC7344730 | `647 and 632 cm−1 correspon` |  |
| PMC7344730 | `C is 145 mAh g−1, and the ` |  |
| PMC7344730 | `I is 145 mAh g−1 at 0.1 C.` |  |
| PMC7344730 | `NI is 95 mAh g−1, that of ` |  |
| PMC7344730 | `and at 3229 cm−1 assigned ` |  |
| PMC7344730 | `around 1050 cm−1, which is` |  |
| PMC7344730 | `d to 120 mAh g−1 for pure ` |  |
| PMC7344730 | `e 11), 1486 cm−1 for C = C` |  |
| PMC7344730 | `eak at 3229 cm−1 is assign` |  |
| PMC7344730 | `eaks at 796 cm−1 assigned ` |  |
| PMC7344730 | `ears at 610 cm−1, attribut` |  |
| PMC7344730 | `ions at 632 cm−1 and the b` |  |
| PMC7344730 | `lution of 1 cm−1. Thermogr` |  |
| PMC7344730 | `ode at 1136 cm−1 associate` |  |
| PMC7344730 | `of 4000–400 cm−1, with a r` |  |
| PMC7344730 | `peak at 796 cm−1 is assign` |  |
| PMC7344730 | `s of 145 mAh g−1 at 0.1 C ` |  |
| PMC7344730 | `ty is 70 mAh g−1 for LiFeP` |  |
| PMC7344730 | `y of 145 mAh g−1 at 0.1 C,` |  |
| PMC7344730 | `y of 145 mAh g−1, compared` |  |
| PMC7352182 | ` and 237.00 Fg−1 at discha` | oui |
| PMC7352182 | ` at 3432.65 cm−1 can be at` | non |
| PMC7352182 | ` range from 10−2 to 105 Hz` | oui |
| PMC7352182 | ` rate of 10 mV−1 and diffe` | non |
| PMC7352182 | ` rate of 10 mV−1. Figure 9` | non |
| PMC7352182 | ` rate of 10 mV−1. The capa` | non |
| PMC7352182 | `, and 79.16 Fg−1 at a scan` | oui |
| PMC7352182 | `, and 86.22 Fg−1 at temper` | oui |
| PMC7352182 | `.0, and 5.0 Ag−1, respecti` | oui |
| PMC7352182 | `/cm2 at 10 mVs−1 []. The c` | non |
| PMC7352182 | `0 Fg−1 at 1 Ag−1. Wang et ` | non |
| PMC7352182 | `0.6 V at 10 mV−1 for 20 cy` | oui |
| PMC7352182 | `3 Fg−1 at 1 Ag−1 in 3 M KC` | non |
| PMC7352182 | `342.5, 1585 cm−1 and 1585 ` | oui |
| PMC7352182 | `Fg−1 at 0.5 Ag−1, which is` | non |
| PMC7352182 | `and 1111.87 cm−1 are shown` | non |
| PMC7352182 | `and 2345.81 cm−1 can be at` | non |
| PMC7352182 | `and 3432.65 cm−1. The abso` | non |
| PMC7352182 | `ate of 5–70 mV−1 are shown` | non |
| PMC7352182 | `can rate 10 mV−1 for over ` | oui |
| PMC7352182 | `dow, and v (mV−1) is the s` | non |
| PMC7352182 | `e of 231.32 Fg−1 at 0.5 Ag` | non |
| PMC7352182 | `e of 425.53 Fg−1 at 1 Ag−1` | non |
| PMC7352182 | `ensity of 1 Ag−1. Jafari e` | non |
| PMC7352182 | `gh as 340.7 Fg−1 at a curr` | non |
| PMC7352182 | `h to be 270 Fg−1 at 1 Ag−1` | non |
| PMC7352182 | `om 0.5 to 5 Ag−1. Based on` | non |
| PMC7352182 | `sity of 0.5 Ag−1. All thre` | oui |
| PMC7352182 | `y (30–200 S cm−1) compared` | non |
| PMC7352182 | `−1 and 1585 cm−1, which ca` | non |
| PMC7352254 | ` liquid (mg·mL−1) phases, ` |  |
| PMC7352254 | ` t (qt), in mg−1, was calc` |  |
| PMC7352254 | ` than 8 kJ·mol−1, leading ` |  |
| PMC7352254 | ` than 8 kJ·mol−1, the adso` |  |
| PMC7352254 | `(8314 JK−1·mol−1) and T is` |  |
| PMC7352254 | `000 to 3000 cm−1 were scan` |  |
| PMC7352254 | `0−7 ohm−1 · cm−1, Lab Mana` |  |
| PMC7352254 | `2 and 100 mg L−1. The cont` |  |
| PMC7352254 | `3.0 × 10−7 ohm−1 · cm−1, L` |  |
| PMC7352254 | `70 and 2740 cm−1, respecti` |  |
| PMC7352254 | `F (mg1−n Ln g −1) and n ar` |  |
| PMC7352254 | `adsorbed (mg·g−1) and liqu` |  |
| PMC7352254 | `ant (J·mol−1·K−1) and T is` |  |
| PMC7352254 | `around 1675 cm−1.The resul` |  |
| PMC7352254 | `ater (3.0 × 10−7 ohm−1 · c` |  |
| PMC7352254 | `d 313.43 mg·g −1, respecti` |  |
| PMC7352254 | `dsorbent (mg·g−1) (GO), Co` |  |
| PMC7352254 | `e range 2 × 10−6 ≤ P/P° ≤ ` |  |
| PMC7352254 | `ed at ~1640 cm−1 (band C=C` |  |
| PMC7352254 | `here, Co (mg L−1) is the i` |  |
| PMC7352254 | `in ca. 3440 cm−1 [,,,,], w` |  |
| PMC7352254 | `ion of 60 mg L−1. After a ` |  |
| PMC7352254 | `n and Ct (mg L−1) is the c` |  |
| PMC7352254 | `nd 0–20 kJ mol−1, respecti` |  |
| PMC7352254 | `nd 313.43 mg g−1 respectiv` |  |
| PMC7352254 | `nergy (mol2·KJ−2) and Qm i` |  |
| PMC7352254 | `nstant k1 (min−1) can be c` |  |
| PMC7352254 | `onstant (J·mol−1·K−1) and ` |  |
| PMC7352254 | `onstant (L·mol−1) correspo` |  |
| PMC7352254 | `owards 1695 cm−1, due to v` |  |
| PMC7352254 | `r Zn(II) (mg·L−1), Ce is t` |  |
| PMC7352254 | `r vacuum of 10−5 mbar for ` |  |
| PMC7352254 | `re (150 mL min−1) with a h` |  |
| PMC7352254 | `rgy, E (kJ·mol−1), can be ` |  |
| PMC7352254 | `stant (8314 JK−1·mol−1) an` |  |
| PMC7352254 | `stant DR (mg·g−1). ε is th` |  |
| PMC7352254 | `te of 5 °C·min−1. The chem` |  |
| PMC7352254 | `the ions (mg·L−1) after th` |  |
| PMC7352254 | `to ca. 3470 cm−1, is assig` |  |
| PMC7352254 | `to −400 kJ mol−1 and 0–20 ` |  |
| PMC7352254 | `wards ~1075 cm−1, which is` |  |
| PMC7352254 | `wards ~1390 cm−1 that corr` |  |
| PMC7436023 | `l tension (N·m−1), and θ t` |  |
| PMC7436023 | `mber (2.6 × 10−6–0.2 MPa).` |  |
| PMC7436023 | `tween 2.6 × 10−6 and 400 M` |  |
| PMC7436023 | `uced: 1.6 × 10−3 cm3/g (se` |  |
| PMC7436023 | `y σ = 485 mN·m−1 and θ = 1` |  |
| PMC7447784 | ` 1.5 and 2 g L−1 BiOCl–GO ` | oui |
| PMC7447784 | ` added 1.0 g L−1 of the ca` | oui |
| PMC7447784 | ` of 0.0037 min−1. These re` | non |
| PMC7447784 | ` to 0.0042 min-1, respecti` | non |
| PMC7447784 | ` ≈ 17.38 mW cm−2). The sus` | oui |
| PMC7447784 | `15 and 25 mg L−1 and the r` | non |
| PMC7447784 | `15 and 25 mg L−1 concentra` | oui |
| PMC7447784 | `15 and 25 mg L−1) were tak` | oui |
| PMC7447784 | `DCF and k (min-1) is appar` | non |
| PMC7447784 | `ce 17.45 mW cm−2; λ = 390–` | oui |
| PMC7447784 | `ht for 25 mg L−1 DCF. Sola` | non |
| PMC7447784 | `lue 0.0386 min−1. The cost` | non |
| PMC7447784 | `m 0.5 to 2 g L−1, the appa` | non |
| PMC7447784 | `ty for 25 mg L−1 Diclofena` | non |
| PMC7481534 | ` Then 20 μL 10−5 uranyl so` |  |
| PMC7481534 | ` about 3300 cm−1 and 1701 ` |  |
| PMC7481534 | ` cm−1, 1600 cm−1 should be` |  |
| PMC7481534 | ` mL 0.05 mg mL−1 aGQDs dis` |  |
| PMC7481534 | ` of 0.05 mg mL−1 aGQD solu` |  |
| PMC7481534 | ` of 1000 g mol−1 to remove` |  |
| PMC7481534 | ` of 10−7 to 10−6 M with th` |  |
| PMC7481534 | ` range from 10−7 M to 10−6` |  |
| PMC7481534 | ` was chosen 10−5 M, 100 ti` |  |
| PMC7481534 | ` was chosen 10−7 M, while ` |  |
| PMC7481534 | `aks at 1381 cm−1 and 1255 ` |  |
| PMC7481534 | `aks at 2300 cm−1, 1600 cm−` |  |
| PMC7481534 | `and at 1605 cm−1 respectiv` |  |
| PMC7481534 | `e of 10 °C min−1 and kept ` |  |
| PMC7481534 | `entration (~10−7 M), which` |  |
| PMC7481534 | `entration (~10−7 M), while` |  |
| PMC7481534 | `he range of 10−7 to 10−6 M` |  |
| PMC7481534 | `lled around 10−3 M, and th` |  |
| PMC7481534 | `m 10−7 M to 10−6 M. Meanwh` |  |
| PMC7481534 | `nds at 1365 cm−1 and at 16` |  |
| PMC7481534 | `ntrolled at 10−5 M.3Result` |  |
| PMC7481534 | `tion around 10−6 M, a sign` |  |
| PMC7481534 | `und 0.05 mg mL−1.2.5Detect` |  |
| PMC7481534 | `−1 and 1255 cm−1 shows the` |  |
| PMC7481534 | `−1 and 1701 cm−1 are assoc` |  |
| PMC7485164 | ` Ca+2 and PO4 −2.15 The el` |  |
| PMC7485164 | `22 and 1090 cm−1 correspon` |  |
| PMC7485164 | `28 and 1090 cm−1 correspon` |  |
| PMC7485164 | `3, 599, 637 cm–1 which are` |  |
| PMC7485164 | `429 and 450 cm−1 cans be a` |  |
| PMC7485164 | `435 and 590 cm−1 can be at` |  |
| PMC7485164 | `45 and 1075 cm−1 are assig` |  |
| PMC7485164 | `49 and 1081 cm−1 bands are` |  |
| PMC7485164 | `49 and 1081 cm−1, the band` |  |
| PMC7485164 | `589 and 606 cm−1, for the ` |  |
| PMC7485164 | `600 and 628 cm–1 correspon` |  |
| PMC7485164 | `band at 875 cm−1 due to th` |  |
| PMC7485164 | `band at 961 cm−1 is a typi` |  |
| PMC7485164 | `band at 964 cm−1 being the` |  |
| PMC7485164 | `ding to a CO3 −2 group. Fo` |  |
| PMC7485164 | `hosphate (PO4 −3) function` |  |
| PMC7485164 | `ncies for PO4 −3 are assoc` |  |
| PMC7485164 | `te group (PO4 −3),13,14,22` |  |
| PMC7485164 | `up, the 964 cm−1 band is a` |  |
| PMC7503313 | ` × 10−3 mol∙kg−1 in the ab` |  |
| PMC7503313 | ` × 10−4–1 × 10−3 mol∙kg−1 ` |  |
| PMC7503313 | `o be of 1 × 10−4–1 × 10−3 ` |  |
| PMC7503662 | ` constant (min−1), shows a` | non |
| PMC7503662 | `N4 (29.936 m2g−1). The por` | non |
| PMC7503662 | `eO2 (9.770 m2g−1) and g-C3` | non |
| PMC7503662 | `ea (77.608 m2g−1) and the ` | non |
| PMC7503662 | `in (12.628 m2g−1), CeO2 (9` | non |
| PMC7503662 | `of 0.01022 min−1, which wa` | oui |
| PMC7503662 | `was 77.608 m2g−1, which wa` | non |
| PMC7503881 | ` around 857 cm−1 was assoc` |  |
| PMC7503881 | `0, and 1375 cm−1 may be al` |  |
| PMC7503881 | `amide (1599 cm−1) in pure ` |  |
| PMC7503881 | `amine (1655 cm−1) and amid` |  |
| PMC7503881 | `and at 1030 cm−1 correspon` |  |
| PMC7503881 | `and at 1565 cm−1 was relat` |  |
| PMC7503881 | `ber at 1571 cm−1 and 1581 ` |  |
| PMC7503881 | `d 1030–1105 cm−1 (stretchi` |  |
| PMC7503881 | `−1 and 1581 cm−1 correspon` |  |
| PMC7518261 | `00 and 2845 cm−1 related t` | oui |
| PMC7518261 | `000 and 912 cm−1 (narrow a` | oui |
| PMC7518261 | `16 and 2857 cm−1, respecti` | oui |
| PMC7518261 | `30 and 2855 cm−1 were attr` | oui |
| PMC7518261 | `990 and 912 cm−1 detected ` | non |
| PMC7518261 | `and 0.26 mol L−1 for PbBr2` | oui |
| PMC7518261 | `f 0.054 mmol L−1 of PbBr2 ` | oui |
| PMC7518261 | `nal at 1595 cm−1 from the ` | non |
| PMC7518261 | `nd 0.27 mmol L−1 in the re` | oui |
| PMC7518261 | `nd 0.27 mmol L−1 of PbBr2 ` | oui |
| PMC7518261 | `number 1579 cm−1 attribute` | non |
| PMC7518261 | `t 3300–2700 cm−1 (broad si` | oui |
| PMC7518261 | `ted at 1670 cm−1 was shift` | oui |
| PMC7518261 | `ted at 1705 cm−1 was assig` | oui |
| PMC7518261 | `umber (1650 cm−1) due to t` | oui |
| PMC7550332 | `400 to 4000 cm−1 by using ` | oui |
| PMC7550332 | `aults (β, 4·10–4), indicat` | oui |
| PMC7550332 | `e of 10 °C min−1 under 40 ` | non |
| PMC7550332 | `ime window (10–7/10–9 s) i` | non |
| PMC7550332 | `indow (10–7/10–9 s) is fas` | non |
| PMC7550332 | `nder 40 mL min−1 O2 flow.R` | oui |
| PMC7550332 | `nsic (α”, 7·10–3) and twin` | oui |
| PMC7563594 | `4000 to 800 cm−1). Accordi` |  |
| PMC7563594 | `51 and 1576 cm−1 indicate ` |  |
| PMC7563594 | `67 and 1714 cm−1, indicati` |  |
| PMC7563594 | `ars at 1714 cm−1, which re` |  |
| PMC7563594 | `ned at 1651 cm−1, indicati` |  |
| PMC7563594 | `of 800–4000 cm−1 to analyz` |  |
| PMC7578857 | `d of 10−2 eV Å−1. For Nd3+` | non |
| PMC7578857 | `hreshold of 10−2 eV Å−1. F` | non |
| PMC7578857 | `n of 150 mg mL−1 and 2 mL ` | non |
| PMC7578857 | `rged within 10−6 eV, with ` | non |
| PMC7578857 | `y of 141 mW cm−2 (see Figu` | non |
| PMC7583944 | `0 and ~1275 cm−1 [,,] were` | non |
| PMC7583944 | `04 and 1397 cm−1, as well ` | non |
| PMC7583944 | `50 and 1750 cm−1, were fou` | non |
| PMC7583944 | `550 and 650 cm−1 [,]. Char` | non |
| PMC7583944 | `for the 904 cm−1 COO− peak` | oui |
| PMC7596963 | ` of 385–540 cm−1 is normal` |  |
| PMC7596963 | `00 and 3000 cm−1 due to th` |  |
| PMC7596963 | `21 and 1576 cm−1, recogniz` |  |
| PMC7596963 | `40 and 1519 cm−1 are relat` |  |
| PMC7596963 | `band at 448 cm−1are assign` |  |
| PMC7596963 | `band at 574 cm−1 and lower` |  |
| PMC7596963 | `ce (140–190 cm−1) was for ` |  |
| PMC7596963 | `ce (200–320 cm−1) was rela` |  |
| PMC7596963 | `ence (< 110 cm−1) was for ` |  |
| PMC7596963 | `k at ~ 3360 cm−1 is attrib` |  |
| PMC7596963 | `ode at 1645 cm−1 and the s` |  |
| PMC7596963 | `ode at 3476 cm−1. Compared` |  |
| PMC7596963 | `of 400–4000 cm−1 regions u` |  |
| PMC7596963 | `the 500–600 cm−1 range is ` |  |
| PMC7596963 | `–1421 = 155 cm−1) was ascr` |  |
| PMC7601971 | ` and 186 mAh g−1, respecti` | non |
| PMC7601971 | `SA = 66.8 m2 g−1) with an ` | oui |
| PMC7601971 | `SA = 97.5 m2 g−1) was impr` | oui |
| PMC7601971 | `bout 120 mAh g−1 at 0.5C. ` | oui |
| PMC7601971 | `f 90–110 mAh g−1) and cycl` | oui |
| PMC7601971 | `land) (2 mol L−1) and NH3∙` | oui |
| PMC7601971 | `nd) (0.2 mol L−1). The sol` | non |
| PMC7601971 | `on was 2 mol L−1) and an a` | oui |
| PMC7601971 | `ow (100 mL min−1) accordin` | oui |
| PMC7601971 | `ressed (6 t cm−2). Electro` | non |
| PMC7601971 | `te of 5 °C min−1 under air` | oui |
| PMC7601971 | `ty of 53 mAh g−1 in the fi` | oui |
| PMC7601971 | `with 148 mAh g−1 at 0.5C. ` | oui |
| PMC7645746 | ` 3338, 3263 cm−1 and the v` | oui |
| PMC7645746 | ` GA to 1416 cm−1 in CuGA 9` | non |
| PMC7645746 | `3, and 1022 cm−1 in GA spe` | non |
| PMC7645746 | `5, and 1050 cm−1, respecti` | non |
| PMC7645746 | `9, and 1575 cm−1, which ar` | oui |
| PMC7645746 | `bent, Ks (L mg−1) is the S` | non |
| PMC7645746 | `d 1363–1591 cm−1 correspon` | oui |
| PMC7645746 | `d from 1421 cm−1 in GA to ` | non |
| PMC7645746 | `of 400–4000 cm−1 wavenumbe` | non |
| PMC7645746 | `oup at 1699 cm−1 disappear` | oui |
| PMC7648642 | ` cm–1, 1055 cm–1 and 1030 ` | non |
| PMC7648642 | ` cm–1, 1448 cm–1 and 1647 ` | oui |
| PMC7648642 | `) and bT (L mg−1) are the ` | non |
| PMC7648642 | `, and ε (J mol−1) is Polan` | non |
| PMC7648642 | `.314 J mol−1 K−1) is the u` | non |
| PMC7648642 | `CF and 10 mg L−1 U(VI), wh` | non |
| PMC7648642 | `KF (mg1−n Ln g−1) are Lang` | non |
| PMC7648642 | `NO3 (0.1 mol L−1) for 24 h` | oui |
| PMC7648642 | `R (8.314 J mol−1 K−1) is t` | non |
| PMC7648642 | `VI); cad (mg L−1) is the c` | non |
| PMC7648642 | `aks at 1368 cm–1 and 1443 ` | oui |
| PMC7648642 | `aks at 1370 cm–1, 1448 cm–` | oui |
| PMC7648642 | `as 241.28 mg g−1 for the a` | oui |
| PMC7648642 | `city; Ce (mg L−1) is the u` | non |
| PMC7648642 | `city; KL (L mg−1) and KF (` | non |
| PMC7648642 | `e β (mol2 (J2)−1) is D–R i` | non |
| PMC7648642 | `ion of 10 mg L−1 at pH 3.0` | non |
| PMC7648642 | `is 241.28 mg g−1.In the pr` | non |
| PMC7648642 | `is 8–16 kJ mol−1, the sorp` | non |
| PMC7648642 | `m–1, ~ 2900 cm–1, 1055 cm–` | non |
| PMC7648642 | `of 0.56 kJ mol−1 in this s` | oui |
| PMC7648642 | `of 241.28 mg g−1 at pH 3.0` | non |
| PMC7648642 | `or CF (q (mg g−1)) of U(VI` | non |
| PMC7648642 | `rium; Qm (mg g−1) is the m` | non |
| PMC7648642 | `rium; ce (mg L−1) is the e` | non |
| PMC7648642 | `s 13.47 kJ mol−1, which re` | oui |
| PMC7648642 | `s E < 8 kJ mol−1 follows t` | non |
| PMC7648642 | `s at ~ 3330 cm–1, ~ 2900 c` | non |
| PMC7648642 | `tion, ct (mg L−1) is the U` | non |
| PMC7648642 | `was 5–150 mg L−1 (Fig. 5).` | non |
| PMC7648642 | `where Kd (mL g−1) is the d` | non |
| PMC7648642 | `where Qe (mg g−1) is the e` | non |
| PMC7648642 | `where c0 (mg L−1) is the i` | non |
| PMC7648642 | `where qT (mg g−1) and bT (` | non |
| PMC7648642 | `–1 and 1030 cm–1 appeared ` | non |
| PMC7648642 | `–1 and 1443 cm–1 appeared ` | oui |
| PMC7648642 | `–1 and 1647 cm–1 were attr` | oui |
| PMC7660179 | ` of 175–800 cm−1. The resu` | non |
| PMC7660179 | ` rate of 1.2 s−1, and a go` | non |
| PMC7660179 | `), 612(A1g) cm−1) phase []` | oui |
| PMC7660179 | `345 and 706 cm−1 are assig` | non |
| PMC7660179 | `ent of 1 × 10 −6 A and a v` | oui |
| PMC7660179 | `nd 638(B1g) cm−1 from the ` | oui |
| PMC7660179 | `peak at 447 cm−1 (Eg) attr` | oui |
| PMC7664687 | ` 5 to 40 mg mL−1, while th` | oui |
| PMC7664687 | ` and 100 µg mL−1, before b` | non |
| PMC7664687 | ` and 100 µg mL−1. After 24` | non |
| PMC7664687 | `.626 10–34 J s−1), ν is th` | non |
| PMC7664687 | `20 and 40 mg L−1, respecti` | non |
| PMC7664687 | `4+]f, 10 mg mL−1 starch) (` | oui |
| PMC7664687 | `4+]f, 10 mg mL−1 starch, 2` | oui |
| PMC7664687 | `4+]f, 20 mg mL−1 fructose,` | oui |
| PMC7664687 | `4+]f, 20 mg mL−1 fructose,` | oui |
| PMC7664687 | `4+]f, 40 mg mL−1 fructose ` | oui |
| PMC7664687 | `4+]f, 40 mg mL−1 fructose,` | oui |
| PMC7664687 | `arch, 20 mg mL−1 fructose)` | oui |
| PMC7664687 | `ce of 20 mg mL−1 fructose ` | oui |
| PMC7664687 | `e and 10 mg mL−1 starch an` | oui |
| PMC7664687 | `e and 10 mg mL−1 starch. T` | oui |
| PMC7664687 | `n at 0.5 mg mL−1 was added` | non |
| PMC7664687 | `tose, 10 mg mL−1 starch) a` | oui |
| PMC7664687 | `tose, 10 mg mL−1 starch) a` | oui |
| PMC7664687 | `tose, 10 mg mL−1 starch). ` | oui |
| PMC7664687 | `wer, −150 μV K−1) at 300 K` | non |
| PMC7672297 | ` at 1226.82 cm−1, 1079.73 ` |  |
| PMC7672297 | ` at 1402.48 cm−1 was due t` |  |
| PMC7672297 | ` at 1642.89 cm−1 was due t` |  |
| PMC7672297 | ` at 2091.41 cm−1 was attri` |  |
| PMC7672297 | ` at 3381.17 cm−1 belong to` |  |
| PMC7672297 | `and 1045.60 cm−1 can be at` |  |
| PMC7672297 | `d at 619.93 cm−1 belongs t` |  |
| PMC7672297 | `lution of 4 cm−1.2.4.6.X-r` |  |
| PMC7672297 | `of 400–4000 cm−1 at a reso` |  |
| PMC7672297 | `−1, 1079.73 cm−1 and 1045.` |  |
| PMC7692729 | `d was 3.6 cd A−1 and 1.0%,` | oui |
| PMC7692729 | `ely 10–15 Ω∙sq−1 was clean` | oui |
| PMC7692729 | `of 26.1 °C∙min−1. The alka` | non |
| PMC7692729 | `uum of ∼6 × 10−6 torr. The` | oui |
| PMC7702064 | `(COO−)=1626 cm−1, in agree` |  |
| PMC7702064 | `1, resol. 1 cm−1) were rec` |  |
| PMC7702064 | `a (4000‐400 cm−1, resol. 1` |  |
| PMC7702064 | `air (10 mL min−1) and prot` |  |
| PMC7702064 | `and at 1600 cm−1. This ban` |  |
| PMC7702064 | `e 2800–3200 cm−1 (Figure S` |  |
| PMC7702064 | `ea of 264 m2 g−1, more tha` |  |
| PMC7702064 | `gon (10 mL min−1). N2 adso` |  |
| PMC7702064 | `ing at 3216 cm−1 and the C` |  |
| PMC7702064 | `n 1300–1700 cm−1 assigned ` |  |
| PMC7702064 | `nal at 1609 cm−1 correlate` |  |
| PMC7702064 | `te of 4 °C min−1, with the` |  |
| PMC7702064 | `te of 4 °C min−1, with the` |  |
| PMC7702064 | `‐74 (1168 m2 g−1). Zn‐MOF‐` |  |
| PMC7702064 | `–500°, 5 K min−1) and diff` |  |
| PMC7702064 | `–60°, 2.5° min−1) measurem` |  |
| PMC7702064 | `−150.78 kJ mol−1). Three d` |  |
| PMC7702064 | `−202.37 kJ mol−1 was calcu` |  |
| PMC7702064 | `−216.12 kJ mol−1. The ener` |  |
| PMC7702064 | `−341.55 kJ mol−1) and mono` |  |
| PMC7702064 | `−468.46 kJ mol−1) coordina` |  |
| PMC7715020 | `and 1987.95 cm−1 (Fig. 5a)` |  |
| PMC7715020 | `and 1987.95 cm−1. Peak 330` |  |
| PMC7715020 | `and 2047.29 cm−1(Fig. 5b).` |  |
| PMC7715020 | `and 2047.29 cm−1. The peak` |  |
| PMC7715020 | `eak 1972.46 cm-1maycorresp` |  |
| PMC7715020 | `eak 1987.95 cm−1 may corre` |  |
| PMC7715020 | `eak 2047.29 cm-1could corr` |  |
| PMC7715020 | `eak 2198.40 cm-1may corres` |  |
| PMC7715020 | `eak 2223.71 cm−1 could cor` |  |
| PMC7715020 | `eak 3273.24 cm−1 may repre` |  |
| PMC7715020 | `eak 3303.05 cm-1may corres` |  |
| PMC7715020 | `of 500–4000 cm−1.2.3.7.Det` |  |
| PMC7720120 | ` 200,000 cm2 v−1 s−1), hig` | non |
| PMC7720120 | ` and 2800 Wh L−1 [], respe` | non |
| PMC7720120 | ` of 1675 mAh g−1 []. Thus,` | non |
| PMC7720120 | ` of 2500 Wh kg−1 and 2800 ` | non |
| PMC7720120 | `, 1012.5 mAh g−1, 1030.7 m` | oui |
| PMC7720120 | `, 1030.7 mAh g−1 and 1134 ` | oui |
| PMC7720120 | `,000 cm2 v−1 s−1), high me` | non |
| PMC7720120 | `1, 837.1 mAh g−1, 1012.5 m` | oui |
| PMC7720120 | `C = 1675 mAh g−1), respect` | oui |
| PMC7720120 | `and 1134 mAh g−1 at 0.1 C ` | oui |
| PMC7720120 | `as 985.4 mAh g−1, 837.1 mA` | oui |
| PMC7720120 | `e of 10 °C·min−1 from room` | oui |
| PMC7720120 | `p to 2630 m2 g−1), great e` | non |
| PMC7747735 | ` 900 to 500 cm−1 can be at` | non |
| PMC7747735 | `.07 and 4° min−1 scan rate` | non |
| PMC7747735 | `2 → Al3+ and O−2 → Co3+ re` | non |
| PMC7747735 | `4000 to 400 cm−1 and illus` | non |
| PMC7747735 | `4000 to 400 cm−1. UV–Vis d` | non |
| PMC7747735 | `570 and 675 cm−1 which are` | oui |
| PMC7747735 | `and at 3430 cm−1 could be ` | non |
| PMC7747735 | `band at 750 cm−1 assigned ` | oui |
| PMC7747735 | `e of 10 °C min−1 while flo` | non |
| PMC7747735 | `er (CT) from O−2 to Al3+ i` | oui |
| PMC7747735 | `gnal at 700 cm−1 indicates` | oui |
| PMC7747735 | `mp of 5 °C min−130. The XP` | non |
| PMC7747735 | `ng of 5 °C min−1 under O2 ` | non |
| PMC7747735 | `ransition of O−2 → Al3+ an` | non |
| PMC7747735 | `ted at 1630 cm−1 is assign` | oui |
| PMC7759625 | ` 107.94 μmol·g−1; strong, ` | non |
| PMC7759625 | `, 13.85 μmol·g−1; strong, ` | non |
| PMC7759625 | `, 85.54 μmol g−1) but the ` | non |
| PMC7759625 | `0 and 1,540 cm−1, which ca` | non |
| PMC7759625 | `ed samples (10−1 mbar, 573` | oui |
| PMC7759625 | `g, 8.72 μmol·g−1). After t` | non |
| PMC7759625 | `o 104.5 μmol·g−1) and incr` | non |
| PMC7759625 | `o 111.5 μmol·g−1). This re` | non |
| PMC7759625 | `o 76.74 μmol·g−1). On the ` | non |
| PMC7759625 | `o 86.84 μmol·g−1), which c` | non |
| PMC7759625 | `s fixed at 4 h−1. Prior to` | non |
| PMC7760056 | ` C = 6.18 × 10−8 mol/L (Eq` | oui |
| PMC7760056 | `.314 J·mol−1·K−1), A is th` | non |
| PMC7760056 | `023 × 1023 mol−1). Therefo` | non |
| PMC7760056 | `10−5 to 5 × 10−5 mol−1 of ` | non |
| PMC7760056 | `22 and 1095 cm−1 accentuat` | non |
| PMC7760056 | `39 and 1622 cm−1 revealed ` | non |
| PMC7760056 | `5, and 5.0 ×10−5, the rate` | non |
| PMC7760056 | `6 nm = 26 × 10−7 cm, M = a` | non |
| PMC7760056 | `eak at 1015 cm−1 was obser` | non |
| PMC7760056 | `eak at 1452 cm−1 may be as` | non |
| PMC7760056 | `eak at 3400 cm-1 was attai` | oui |
| PMC7760056 | `hieve 1.0 × 10−5 M concent` | oui |
| PMC7760056 | `mL of 1.0 × 10−5 M dyes so` | oui |
| PMC7760056 | `o 5 × 10−5 mol−1 of dye (R` | non |
| PMC7760056 | `of 4000–400 cm−1 using a B` | non |
| PMC7760056 | `on from 1 × 10−5 to 5 × 10` | non |
| PMC7760056 | `ons of 1.0 ×10−5, 2.0 ×10−` | non |
| PMC7760056 | `t (8.314 J·mol−1·K−1), A i` | non |
| PMC7760056 | `×10−5, 2.0 ×10−5, 3.0 ×10−` | non |
| PMC7760056 | `×10−5, 3.0 ×10−5, 4.0 ×10−` | non |
| PMC7760056 | `×10−5, 4.0 ×10−5, and 5.0 ` | non |
| PMC7786535 | ` than 1010 K s−1 and sonoc` | non |
| PMC7824182 | `83, and 634 cm−1) and can ` |  |
| PMC7824182 | `ch at ~3484 cm−1. The amid` |  |
| PMC7824182 | `d at 3455.8 cm−1 was relat` |  |
| PMC7824182 | `of 4000–400 cm−1. A vibrat` |  |
| PMC7824182 | `on at ~1660 cm−1 []. In ad` |  |
| PMC7824182 | `p to 3016.7 cm−1 []. CS FT` |  |
| PMC7824182 | `t 1480–1700 cm−1 correspon` |  |
| PMC7847977 | ` and 0.3 mA cm−2 of curren` |  |
| PMC7847977 | ` and 0.5 mA cm−2 for 50 cy` |  |
| PMC7847977 | ` and 0.5 mA cm−2 with a ch` |  |
| PMC7847977 | ` and 3.02 × 10−5 S cm−1, r` |  |
| PMC7847977 | `, and 100 mA g−1 current d` |  |
| PMC7847977 | `, and 200 mA g−1, respecti` |  |
| PMC7847977 | `.0 × 10−4 S cm−1 for the P` |  |
| PMC7847977 | `0 and 200 mA g−1 current d` |  |
| PMC7847977 | `0 and 200 mA g−1 current d` |  |
| PMC7847977 | `02 × 10−5 S cm−1, respecti` |  |
| PMC7847977 | `1 to 0.5 mA cm−2 at 60°C. ` |  |
| PMC7847977 | `10 to 200 mA g−1 and back ` |  |
| PMC7847977 | `24% at 50 mA g−1 current d` |  |
| PMC7847977 | `4 and 2.0 × 10−4 S cm−1 fo` |  |
| PMC7847977 | `P was ~2 mg cm−2, and the ` |  |
| PMC7847977 | `ack to 10 mA g−1, the disc` |  |
| PMC7847977 | `ack to 10 mA g−1. Charge a` |  |
| PMC7847977 | `al was 2 mg cm−2, under th` |  |
| PMC7847977 | `as 153.3 mAh g−1 and then ` |  |
| PMC7847977 | `ase at 10 mA g−1, the reco` |  |
| PMC7847977 | `ct of 200 mA g−1 current d` |  |
| PMC7847977 | `d as 0.4 mA cm−2, which is` |  |
| PMC7847977 | `d to 0.5 mA cm−2, the cell` |  |
| PMC7847977 | `ed to 1.2 × 10−4 and 2.0 ×` |  |
| PMC7847977 | `ed to 200 mA g−1, the pola` |  |
| PMC7847977 | `ent of 50 mA g−1 and the s` |  |
| PMC7847977 | `ion at 50 mA g−1 current d` |  |
| PMC7847977 | `ion at 50 mA g−1 current d` |  |
| PMC7847977 | `ity of 50 mA g−1. As expec` |  |
| PMC7847977 | `mally low (≤10−6 S cm−1) o` |  |
| PMC7847977 | `nd 100.3 mAh g−1 obtained ` |  |
| PMC7847977 | `nd 100.8 mAh g−1 at 100 an` |  |
| PMC7847977 | `nd 100.8 mAh g−1 at 100 an` |  |
| PMC7847977 | `nd 103.7 mAh g−1, respecti` |  |
| PMC7847977 | `nd 110.9 mAh g−1 for the c` |  |
| PMC7847977 | `nd 135.3 mAh g−1 after 100` |  |
| PMC7847977 | `nd 135.3 mAh g−1 after 100` |  |
| PMC7847977 | `of 137.4 mAh g−1 at the ma` |  |
| PMC7847977 | `of 137.4 mAh g−1 at the ma` |  |
| PMC7847977 | `of 156.6 mAh g−1 at the fo` |  |
| PMC7847977 | `only 0.3 mA cm−2. Even whe` |  |
| PMC7847977 | `ow (≤10−6 S cm−1) owing to` |  |
| PMC7847977 | `rate of 1 mV s−1. It showe` |  |
| PMC7847977 | `than 0.5 mA cm−2. To impro` |  |
| PMC7847977 | `to 155.5 mAh g−1, which de` |  |
| PMC7847977 | `ty of 200 mA g−1, which mi` |  |
| PMC7847977 | `under 200 mA g−1 current d` |  |
| PMC7847977 | `were 2.24 × 10−5 and 3.02 ` |  |
| PMC7847977 | `y (3,860 mAh g−1), low den` |  |
| PMC7847977 | `y of 0.3 mA cm−2, the cell` |  |
| PMC7847977 | `y of 0.5 mA cm−2, a high v` |  |
| PMC7860036 | ` cm−1, 1540 cm−1, and 1640` |  |
| PMC7860036 | `1, and 1640 cm−1 could be ` |  |
| PMC7860036 | `4000 to 500 cm−1 (Nicolet ` |  |
| PMC7860036 | `aks at 3320 cm−1 and 2950 ` |  |
| PMC7860036 | `d I at 1390 cm−1, 1540 cm−` |  |
| PMC7860036 | `−1 and 2950 cm−1 represent` |  |
| PMC7910993 | ` as 833.99 m2g−1.From the ` |  |
| PMC7910993 | ` cm−1, 1448 cm−1, and 432 ` |  |
| PMC7910993 | `ate at 2917 cm−1 and the a` |  |
| PMC7910993 | `he 200–4000 cm−1 range) of` |  |
| PMC7910993 | `tch at 1610 cm−1 and C=N s` |  |
| PMC7910993 | `tretch 1448 cm−1. The FTIR` |  |
| PMC7910993 | `ved at 1063 cm−1, 1448 cm−` |  |
| PMC7910993 | `−1, and 432 cm−1, respecti` |  |
| PMC7912860 | `500 to 4000 cm−1. The surf` |  |
| PMC7912860 | `aks at 1386 cm−1 and 1153 ` |  |
| PMC7912860 | `eak at 1583 cm−1 reflects ` |  |
| PMC7912860 | `eak at 2951 cm−1 is assign` |  |
| PMC7912860 | `ted at 1073 cm−1.The major` |  |
| PMC7912860 | `−1 and 1153 cm−1 represent` |  |
| PMC7913101 | ` and 96.8 S·cm−1 in its ox` |  |
| PMC7913101 | `m of 21.1 S·cm−1 when redu` |  |
| PMC7931434 | ` of 2.5 °C min–1 to remove` |  |
| PMC7932996 | `00 to 1,300 cm–1 disclosed` |  |
| PMC7932996 | `08 to 1,445 cm–1 correspon` |  |
| PMC7932996 | `12 to 1,550 cm–1 correspon` |  |
| PMC7932996 | `254 to 3211 cm–1 correspon` |  |
| PMC7932996 | `52 to 2,048 cm–1 correspon` |  |
| PMC7932996 | `f 4,000–400 cm–1 to identi` |  |
| PMC7932996 | `ld) at 8°C min–1 to 300°C ` |  |
| PMC7962968 | ` constant (mgL−1 min−1), K` | non |
| PMC7962968 | ` constant (min−1). A plot ` | non |
| PMC7962968 | ` reactant (Lmg−1), and [MB` | non |
| PMC7962968 | `and at 1650 cm−1 character` | non |
| PMC7962968 | `ant (mgL−1 min−1), K is th` | non |
| PMC7962968 | `d 2800–2900 cm−1 is identi` | non |
| PMC7962968 | `d 3400–3600 cm−1 due to th` | non |
| PMC7962968 | `ge 400–4000 cm−1 using the` | non |
| PMC7962968 | `ing at 1109 cm−1 and 1020 ` | non |
| PMC7962968 | `ion of a 5 mgL−1 MB dye so` | oui |
| PMC7962968 | `ntration (mg L−1). When [M` | non |
| PMC7962968 | `region, 426 cm−1, correspo` | oui |
| PMC7962968 | `rged within 10−5 eV. The p` | non |
| PMC7962968 | `−1 and 1020 cm−1 are due t` | non |
| PMC7996286 | ` cm−1, 1079 cm−1 (C–O) to ` | non |
| PMC7996286 | ` cm−1, 1413 cm−1 (C–S) to ` | non |
| PMC7996286 | ` cm−1, 1577 cm−1 (N–H) to ` | non |
| PMC7996286 | ` cm−1, 1577 cm−1 and 1066 ` | non |
| PMC7996286 | ` cm−1, 1584 cm−1 (N–H) to ` | non |
| PMC7996286 | ` cm−1, 2342 cm−1 (O=C=O, C` | non |
| PMC7996286 | ` constant (min−1). The lin` | non |
| PMC7996286 | `) from 3366 cm−1 (–OH and ` | non |
| PMC7996286 | `, at 10 °C min−1. A pH-met` | non |
| PMC7996286 | `0, and 1033 cm−1 were foun` | oui |
| PMC7996286 | `13 and 1335 cm−1 on Met-GO` | non |
| PMC7996286 | `15 and 1049 cm−1, for MOX ` | non |
| PMC7996286 | `17 and 3696 cm−1, 2342 cm−` | oui |
| PMC7996286 | `48 and 2330 cm−1, 1584 cm−` | oui |
| PMC7996286 | `83 and 1407 cm−1, 1079 cm−` | oui |
| PMC7996286 | `856 and 660 cm−1 appear to` | non |
| PMC7996286 | `876 and 698 cm−1 were foun` | non |
| PMC7996286 | `NH) to 3347 cm−1, 1577 cm−` | oui |
| PMC7996286 | `Then 0.5 mol/L−1 L-methion` | oui |
| PMC7996286 | `aks at 1616 cm−1, 1577 cm−` | non |
| PMC7996286 | `and at 3366 cm−1 was due t` | oui |
| PMC7996286 | `ands at 692 cm−1 and 1217 ` | non |
| PMC7996286 | `d from 3347 cm−1 (–OH stre` | non |
| PMC7996286 | `eak at 1721 cm−1 refers to` | non |
| PMC7996286 | `eak at 2933 cm−1, was assi` | non |
| PMC7996286 | `of 4000–500 cm−1. The surf` | non |
| PMC7996286 | `peak at 941 cm−1 is attrib` | non |
| PMC7996286 | `to a 0.2 mol L−1 CaCl2 sol` | oui |
| PMC7996286 | `–H) to 1580 cm−1 and 1413 ` | non |
| PMC7996286 | `–H) to 1584 cm−1, 1413 cm−` | oui |
| PMC7996286 | `–O) to 1079 cm−1, showing ` | non |
| PMC7996286 | `–S) to 1407 cm−1 and 1066 ` | non |
| PMC7996286 | `−1 and 1066 cm−1 (C–O) to ` | non |
| PMC7996286 | `−1 and 1066 cm−1, respecti` | non |
| PMC7996286 | `−1 and 1217 cm−1 show vibr` | non |
| PMC7996286 | `−1 and 1413 cm−1 (C–S–, S=` | non |
| PMC8003880 | ` = 400–2000 cm−1), scannin` |  |
| PMC8003880 | `mately 1420 cm−1, which wa` |  |
| PMC8072711 | ` (ν4a), 574 cm−1 (ν4b) and` |  |
| PMC8072711 | ` 428 to 425 cm−1 with an i` |  |
| PMC8072711 | ` HA) to 960 cm−1 (in Sr-Se` |  |
| PMC8072711 | ` constant (N·m−1), and μ i` |  |
| PMC8072711 | `, while 447 cm−1 and 428 c` |  |
| PMC8072711 | `074 to 1068 cm−1. Similarl` |  |
| PMC8072711 | `1) from 956 cm−1 (in HA) t` |  |
| PMC8072711 | `2 h: 100 µg·mL−1, 200 µg·m` |  |
| PMC8072711 | `4000 to 400 cm−1 and the r` |  |
| PMC8072711 | `4b) and 560 cm−1 (ν4b) [].` |  |
| PMC8072711 | `900 to 1200 cm−1 []. The t` |  |
| PMC8072711 | `L−1, 200 µg·mL−1, and 1000` |  |
| PMC8072711 | `aks at 1046 cm−1 and 1054 ` |  |
| PMC8072711 | `and 1000 µg·mL−1.3. Discus` |  |
| PMC8072711 | `and 1000 μg·mL−1) were tak` |  |
| PMC8072711 | `and at 1405 cm−1 was chara` |  |
| PMC8072711 | `d 1046–1032 cm−1 (ν3b asym` |  |
| PMC8072711 | `eak at 1076 cm−1 were char` |  |
| PMC8072711 | `eaks at 580 cm−1 and 594 c` |  |
| PMC8072711 | `les at 1087 cm−1 (ν3a asym` |  |
| PMC8072711 | `m−1 and 428 cm−1 were ascr` |  |
| PMC8072711 | `m−1 and 560 cm−1 [], where` |  |
| PMC8072711 | `m−1 and 594 cm−1 were attr` |  |
| PMC8072711 | `ode, at 601 cm−1 and 560 c` |  |
| PMC8072711 | `of 300–1200 cm−1 at 30 s f` |  |
| PMC8072711 | `peak at 631 cm−1 in HA was` |  |
| PMC8072711 | `peak at 962 cm−1 in HA was` |  |
| PMC8072711 | `rved at 601 cm−1 (ν4a), 57` |  |
| PMC8072711 | `rved at 767 cm−1 were attr` |  |
| PMC8072711 | `rved at 830 cm−1 was attri` |  |
| PMC8072711 | `rved at 960 cm−1 was attri` |  |
| PMC8072711 | `te of 5 °C min−1).Se-Sr-HA` |  |
| PMC8072711 | `tio of 0.1 g·L−1 in partic` |  |
| PMC8072711 | `ution was 4 cm−1.4.2.3. Ra` |  |
| PMC8072711 | `−1 and 1054 cm−1 and one m` |  |
| PMC8101407 | ` of 41.4 mA cm−2. The maxi` |  |
| PMC8101407 | `, of 14.6 cd A−1. The blue` |  |
| PMC8101407 | `e of 18.1 cd m−2. A maximu` |  |
| PMC8101407 | `e of 1861 cd m−2 was reali` |  |
| PMC8101407 | `t J = 20 mA cm−2.We found ` |  |
| PMC8103248 | ` around 800 cm−1 is assign` |  |
| PMC8103248 | `200 to 1000 cm−1 depicts S` |  |
| PMC8103248 | `400 to 4000 cm−1. To reduc` |  |
| PMC8103248 | `55 and 1067 cm−1 can be as` |  |
| PMC8103248 | `lution of 4 cm−1 in Happ-G` |  |
| PMC8103248 | `tio of 0.1 g.L−1 in partic` |  |
| PMC8118497 | ` and 1629.0 cm−1 were disa` |  |
| PMC8118497 | ` and 1697.8 cm−1), suggest` |  |
| PMC8118497 | `) and 465.3 cm−1 (Si–O–Si ` |  |
| PMC8118497 | `H at 1630.4 cm−1 could be ` |  |
| PMC8118497 | `H at 3452.1 cm−1, antisymm` |  |
| PMC8118497 | `Si at 464.0 cm−1 (Figure 1` |  |
| PMC8118497 | `Si at 801.9 cm−1, and the ` |  |
| PMC8118497 | `d 1450–1560 cm−1 (belongin` |  |
| PMC8118497 | `d at 1308.8 cm−1 relative ` |  |
| PMC8118497 | `d at 1523.2 cm−1 refer to ` |  |
| PMC8118497 | `d at 1694.9 cm−1 relative ` |  |
| PMC8118497 | `d at 3300.1 cm−1 correspon` |  |
| PMC8118497 | `i at 1080.3 cm−1, symmetri` |  |
| PMC8118497 | `ion), 801.7 cm−1 (Si–O–Si ` |  |
| PMC8118497 | `m−1, 1524.0 cm−1 and 1697.` |  |
| PMC8118497 | `of 400–4000 cm−1. KBr pell` |  |
| PMC8118497 | `of 400–4000 cm−1. Moreover` |  |
| PMC8118497 | `on), 1084.6 cm−1 (Si–O–Si ` |  |
| PMC8118497 | `ound 3299.4 cm−1, 1524.0 c` |  |
| PMC8118497 | `s at 1629.0 cm−1. After co` |  |
| PMC8118497 | `s at 1630.4 cm−1 and 1629.` |  |
| PMC8118497 | `s at 1734.6 cm−1 and stret` |  |
| PMC8118497 | `s at 3431.1 cm−1 (Si–OH an` |  |
| PMC8118497 | `t 2800–2900 cm−1 and the b` |  |
| PMC8125317 | ` 80 and 115 cm−1. These tw` | non |
| PMC8125317 | ` 98 and 437 cm−1 and are a` | non |
| PMC8125317 | ` and 0.038 min−1, respecti` | oui |
| PMC8125317 | ` and 0.038 min−1, respecti` | oui |
| PMC8125317 | ` and 0.046 min−1, respecti` | oui |
| PMC8125317 | ` and 6.41 m2 g−1, respecti` | oui |
| PMC8125317 | ` around 443 cm−1 that cann` | non |
| PMC8125317 | ` around 535 cm−1 in the Ra` | non |
| PMC8125317 | ` around 580 cm−1 is report` | non |
| PMC8125317 | ` around 580 cm−1 may be at` | non |
| PMC8125317 | ` of 38.51 m2 g−1, while ca` | oui |
| PMC8125317 | ` °C (0.084 min−1) decrease` | oui |
| PMC8125317 | `000 and 500 cm−1 and with ` | non |
| PMC8125317 | `1100 to 700 cm−1 are attri` | non |
| PMC8125317 | `570 to 1390 cm−1 as well a` | non |
| PMC8125317 | `around 3400 cm−1 is attrib` | non |
| PMC8125317 | `ation of 1 g L−1 and a RhB` | non |
| PMC8125317 | `d 80 to 190 cm−1 may be re` | non |
| PMC8125317 | `lution (4 mg L−1) and then` | oui |
| PMC8125317 | `mode at 574 cm−1 and the E` | non |
| PMC8125317 | `mode at 583 cm−1 []. The p` | non |
| PMC8125317 | `nd from 632 cm−1 to lower ` | non |
| PMC8125317 | `nd with a 4 cm−1 resolutio` | non |
| PMC8125317 | `ound 0.091 min−1, whereas ` | oui |
| PMC8125317 | `peak at 380 cm−1 is associ` | non |
| PMC8125317 | `peak at 409 cm−1 is relate` | non |
| PMC8125317 | `round 89 mW cm−2 (0.89 sun` | non |
| PMC8125317 | `te of 250 °C h−1.X-ray dif` | non |
| PMC8125317 | `tem was 0.3 cm−1. The lase` | non |
| PMC8125317 | `tion of 5 mg L−1. Liu et a` | non |
| PMC8125317 | `ty of 35 mW cm−2. The solu` | oui |
| PMC8125317 | `und at 1640 cm−1 is associ` | non |
| PMC8125317 | `ure (0.091 min−1).Under so` | non |
| PMC8125317 | `ution (10 mg L−1).To the b` | non |
| PMC8132056 | ` and 5.29 × 10−4 cm2 V−1 s` | oui |
| PMC8132056 | ` of 2000 rpm s−1. Chlorobe` | non |
| PMC8132056 | `0, and 22.2 nm−1 correspon` | non |
| PMC8132056 | `0−4, 1.21 × 10−4, 1.92 × 1` | oui |
| PMC8132056 | `0−4, 1.92 × 10−4, and 5.29` | oui |
| PMC8132056 | `10−4 cm2 V−1 s−1, respecti` | oui |
| PMC8132056 | `5.71 × 1014 cm−3 within th` | oui |
| PMC8132056 | `6.67 × 1015 cm−3, respecti` | non |
| PMC8132056 | `9 × 10−4 cm2 V−1 s−1, resp` | oui |
| PMC8132056 | `9.49 × 1015 cm−3. To gain ` | non |
| PMC8132056 | `TIPD (15 µL mL−1).Device F` | non |
| PMC8132056 | `around 5 mg mL−1) by the a` | oui |
| PMC8132056 | `ate of 2 K min−1. The capa` | non |
| PMC8132056 | `ch 21.55 mA cm−2 and 22.63` | oui |
| PMC8132056 | `en 5 and 30 nm−1 (Figure S` | non |
| PMC8132056 | `ion (100 mW cm−2) with a s` | non |
| PMC8132056 | `n of 100 mW cm−2 (AM 1.5G)` | non |
| PMC8132056 | `n of 100 mW cm−2 (AM 1.5G)` | non |
| PMC8132056 | `n of 200 rpm s−1. The seco` | non |
| PMC8132056 | `nce of 10 Ω sq−1 was purch` | oui |
| PMC8132056 | `o be 0.77 × 10−4, 1.21 × 1` | oui |
| PMC8132056 | `of 23.23 mA cm−2, and an F` | oui |
| PMC8132056 | `of 23.36 mA cm−2, and an F` | oui |
| PMC8132056 | `to 22.90 mA cm−2, ≈2.5% en` | non |
| PMC8136633 | ` and 598.92 cm-1 are attri` | oui |
| PMC8136633 | ` and 631.70 cm-1 correspon` | non |
| PMC8136633 | ` and at 864 cm-1, which ca` | oui |
| PMC8136633 | `aks at 3570 cm-1 and 631.7` | non |
| PMC8136633 | `and 1088.45 cm-1 are relat` | oui |
| PMC8136633 | `and at 1367 cm-1, showing ` | non |
| PMC8136633 | `carbonate (CO3-2) peak was` | oui |
| PMC8136633 | `n 1420–1450 cm-1 and at 86` | oui |
| PMC8136633 | `n 3300–3450 cm-1 and at 13` | oui |
| PMC8136633 | `of 400–4000 cm-1. The SEM ` | non |
| PMC8136633 | `ons at 1430 cm-1, formed f` | oui |
| PMC8136633 | `oup at 3570 cm-1, phosphat` | non |
| PMC8136633 | `p at 962.18 cm-1) can indi` | non |
| PMC8136633 | `phosphate (PO4-3), and the` | oui |
| PMC8136633 | `s of (OH-, PO4-3) appeared` | non |
| PMC8149873 | ` (−1577 kJ mol−1) as compa` | non |
| PMC8149873 | ` (−1926 kJ mol−1) and lowe` | non |
| PMC8149873 | ` and 4000 mA g−1 (Suppleme` | oui |
| PMC8149873 | ` of 4.484 m2 g−1 (3.2 and ` | oui |
| PMC8149873 | `% (429.1 mAh g−1) after 50` | oui |
| PMC8149873 | `+ (−520 kJ mol−1), the abs` | non |
| PMC8149873 | `.1 to 5.0 mV s−1 are condu` | non |
| PMC8149873 | `1 and 281.4 cm−1 could be ` | non |
| PMC8149873 | `2.47 × 103 g m−3. It is ea` | non |
| PMC8149873 | `3 × 10−10 m2 s−1) due to i` | non |
| PMC8149873 | `3 × 10−10 m2 s−1) is lower` | non |
| PMC8149873 | `4/568.91 mAh g−1 with a CE` | oui |
| PMC8149873 | `58 μm (Ns = 10−15 mol). To ` | non |
| PMC8149873 | `6 × 10−10 m2 s−1). The XRD` | non |
| PMC8149873 | `VO4 (591 mAh g−1), attribu` | oui |
| PMC8149873 | `ak at 403.2 cm−1 could acc` | non |
| PMC8149873 | `ak at 702.5 cm−1. The sign` | non |
| PMC8149873 | `al at 147.6 cm−1 (B1g) cou` | non |
| PMC8149873 | `al at 201.1 cm−1 while the` | non |
| PMC8149873 | `al at 528.3 cm−1 could be ` | non |
| PMC8149873 | `d at 1091.6 cm−1 20 in the` | non |
| PMC8149873 | `eak at 1091 cm−1 in Raman ` | non |
| PMC8149873 | `ed at 951.3 cm−1 is attrib` | non |
| PMC8149873 | `ed at 991.3 cm−1 could be ` | non |
| PMC8149873 | `ft of 482.7 cm−1 while a p` | non |
| PMC8149873 | `ity (591 mAh g−1) than gra` | non |
| PMC8149873 | `ity (7.06 × 10−10 m2 s−1). ` | non |
| PMC8149873 | `ity of 50 mA g−1 was shown` | oui |
| PMC8149873 | `ity of 50 mA g−1, the capa` | oui |
| PMC8149873 | `ks at ⁓1091 cm−1 and the m` | non |
| PMC8149873 | `n as 1.18 × 10−18 moles whi` | non |
| PMC8149873 | `nd 268.7 mAh g−1 (for 0LCV` | oui |
| PMC8149873 | `nd 337.2 mAh g−1 and capac` | oui |
| PMC8149873 | `nd 750–1000 cm−1 correspon` | non |
| PMC8149873 | `of 350.6 mAh g−1 in its fi` | oui |
| PMC8149873 | `of 462.8 mAh g−1 and retai` | oui |
| PMC8149873 | `of 50–800 mA g−1 of Ca-dop` | non |
| PMC8149873 | `ons (10.3 × 10−10 m2 s−1) d` | non |
| PMC8149873 | `ons (7.93 × 10−10 m2 s−1) i` | non |
| PMC8149873 | `p to 2000 m2 g−1)60,64, th` | non |
| PMC8149873 | `s 946.78 mAh g−1 with a ve` | oui |
| PMC8149873 | `solute Ns = 10−18 mol) to 2` | non |
| PMC8149873 | `te of 0.1 mV s−1.Based on ` | non |
| PMC8149873 | `than 600 mAh g−1, which is` | non |
| PMC8149873 | `ty of 100 mA g−1, the cycl` | oui |
| PMC8149873 | `were set to 10−4 eV and 0.` | non |
| PMC8149873 | `y of 100 mAh g−1. The cycl` | non |
| PMC8149873 | `y, 543.1 mAh g−1 (for 3LCV` | oui |
| PMC8153126 | ` cm−1, 1468 cm−1, and 1345` |  |
| PMC8153126 | ` cm−1, 1654 cm−1 and 1561 ` |  |
| PMC8153126 | `(-OH); 1720 cm−1 ascribed ` |  |
| PMC8153126 | `1, and 1345 cm−1 from the ` |  |
| PMC8153126 | `4 cm−1, 964 cm−1 and 843 c` |  |
| PMC8153126 | `ak at ~2900 cm−1, meaning ` |  |
| PMC8153126 | `aks at 1104 cm−1, 964 cm−1` |  |
| PMC8153126 | `aks at 2883 cm−1, 1468 cm−` |  |
| PMC8153126 | `and at 1376 cm−1 correspon` |  |
| PMC8153126 | `around 1648 cm−1.3.3. Rama` |  |
| PMC8153126 | `around 1718 cm−1 in the FT` |  |
| PMC8153126 | `around 2880 cm−1, 1654 cm−` |  |
| PMC8153126 | `eak at 1150 cm−1 was attri` |  |
| PMC8153126 | `eak at 1510 cm−1 was ident` |  |
| PMC8153126 | `ed at: 3384 cm−1 attribute` |  |
| PMC8153126 | `gnal (~2700 cm−1) that cha` |  |
| PMC8153126 | `group; 1585 cm−1 correspon` |  |
| PMC8153126 | `lution of 4 cm−1, and 32 s` |  |
| PMC8153126 | `m−1 and 843 cm−1 were attr` |  |
| PMC8153126 | `n 3400–3200 cm−1 that corr` |  |
| PMC8153126 | `nd G (~1590 cm−1) bands []` |  |
| PMC8153126 | `of 100–3200 cm−1. The wave` |  |
| PMC8153126 | `of 4000–600 cm−1, at a res` |  |
| PMC8153126 | `p; and 1046 cm−1 attribute` |  |
| PMC8153126 | `phene; 1234 cm−1 represent` |  |
| PMC8153126 | `red at 1585 cm−1 from the ` |  |
| PMC8153126 | `se D (~1360 cm−1) and G (~` |  |
| PMC8153126 | `−1 and 1561 cm−1 were attr` |  |
| PMC8155954 | `ed at 0.1 mV s−1 between 2` | oui |
| PMC8155954 | `ity (372 mAh g−1) []. Comm` | non |
| PMC8155954 | `nd 102.5 mAh g−1, respecti` | oui |
| PMC8155954 | `nd 121.9 mAh g−1 in the 10` | oui |
| PMC8155954 | `nd 144.7 mAh g−1 from the ` | oui |
| PMC8155954 | `nd 162.6 mAh g−1, with Cou` | oui |
| PMC8155954 | `of 171.0 mAh g−1 after fin` | oui |
| PMC8155954 | `of 174.5 mAh g−1 at 1 C an` | oui |
| PMC8155954 | `of 175.5 mAh g−1 with a Co` | non |
| PMC8155954 | `y of 183 mAh g−1 at 0.1 C,` | oui |
| PMC8159122 | `ation of 1 g∙L−1, then the` | non |
| PMC8159122 | `te of 5 °C min−1 for a dur` | non |
| PMC8184743 | ` up to 4000 cm−1. The FTIR` | non |
| PMC8184743 | `00 and 1600 cm−1 correspon` | non |
| PMC8184743 | `400 and 467 cm−1 correspon` | oui |
| PMC8184743 | `96 and 3502 cm−1 correspon` | non |
| PMC8184743 | `d near 2900 cm-1 correspon` | non |
| PMC8184743 | `nd near 700 cm−1 which may` | oui |
| PMC8184743 | `nd near 900 cm−1 may corre` | oui |
| PMC8199406 | ` of 4200 mAh g−1 for Li22S` | non |
| PMC8199406 | `aks at 1350 cm−1 and 1578 ` | oui |
| PMC8199406 | `ate (>5 °C min−1) in the o` | oui |
| PMC8199406 | `d 1131.9 mAh g−1, respecti` | oui |
| PMC8199406 | `e 108.024 m2 g−1. The larg` | non |
| PMC8199406 | `es at 500 mA g−1, respecti` | oui |
| PMC8199406 | `es at 500 mA g−1, respecti` | oui |
| PMC8199406 | `f 3084.1 mAh g−1 and 1131.` | oui |
| PMC8199406 | `ity of 50 mA g−1 to activa` | non |
| PMC8199406 | `les at 50 mA g−1 of sCCSi-` | non |
| PMC8199406 | `nd 726.7 mAh g−1 in the fo` | oui |
| PMC8199406 | `o 1173.1 mAh g−1 and 726.7` | oui |
| PMC8199406 | `peak at 506 cm−1 correspon` | non |
| PMC8199406 | `rate (3 °C min−1 to 5 °C m` | oui |
| PMC8199406 | `s only 372 mAh−1 for LiC6)` | non |
| PMC8199406 | `te of 1 °C min−1, and fina` | oui |
| PMC8199406 | `te of 1 °C min−1, the high` | oui |
| PMC8199406 | `te of 5 °C min−1 to obtain` | oui |
| PMC8199406 | `ty of 500 mA g−1. Electroc` | non |
| PMC8199406 | `−1 and 1578 cm−1 correspon` | oui |
| PMC8199406 | `−1 to 5 °C min−1) in the v` | oui |
| PMC8228098 | `Jsc (~26 µA cm−2) is obser` |  |
| PMC8228098 | `ion (100 mW cm−2 AM 1.5 G ` |  |
| PMC8228098 | `vacuum (6 × 10−6 mbar).The` |  |
| PMC8233738 | `30 and 3500 cm−1 were due ` | oui |
| PMC8233738 | `61 and 1550 cm−1, which be` | oui |
| PMC8233738 | `97, and 467 cm−1, caused b` | oui |
| PMC8233738 | `at ca. 1468 cm−1 (or 1490 ` | oui |
| PMC8233738 | `at ca. 2930 cm−1 (or 2940 ` | oui |
| PMC8233738 | `of 4000–400 cm−1 using an ` | non |
| PMC8233738 | `−1 (or 1490 cm−1) was ascr` | oui |
| PMC8233738 | `−1 (or 2940 cm−1) was attr` | oui |
| PMC8238979 | ` and 10 s step−1, a diverg` |  |
| PMC8238979 | `000 and 400 cm−1. Data rep` |  |
| PMC8238979 | `29 and 1091 cm−1 are attri` |  |
| PMC8238979 | `446 and 416 cm−1are charac` |  |
| PMC8238979 | `67 and 1638 cm−1 for O–H s` |  |
| PMC8238979 | `698 and 625 cm−1 are attri` |  |
| PMC8238979 | `and at 1638 cm−1 is assign` |  |
| PMC8238979 | `and at 3467 cm−1 is associ` |  |
| PMC8238979 | `e was 1.5 °C s−1. Once the` |  |
| PMC8246083 | ` (0.010 mmol g−1 for K-SAP` |  |
| PMC8246083 | ` (0.024 mmol g−1 for K-SAP` |  |
| PMC8246083 | ` (0.027 mmol g−1 at 0.98 b` |  |
| PMC8246083 | ` (0.027 mmol g−1 at 0.98 b` |  |
| PMC8246083 | ` (0.070 mmol g−1 at 0.85 b` |  |
| PMC8246083 | `0–0.070 mmol g−1 for N2). ` |  |
| PMC8246083 | `2 (0.01 mmol g−1 at 0.02 b` |  |
| PMC8246083 | `7–0.027 mmol g−1 for CH4 a` |  |
| PMC8246083 | `O (0.45 mmol g−1) (Fig. 4a` |  |
| PMC8246083 | `O (0.87 mmol g−1) > Cs-SAP` |  |
| PMC8246083 | `O (3.53 mmol g−1) > K-SAPO` |  |
| PMC8246083 | `O (4.41 mmol g−1) > Na-SAP` |  |
| PMC8246083 | `d 0.014 mmol g−1 for Cs-SA` |  |
| PMC8246083 | `d 0.017 mmol g−1 for Cs-SA` |  |
| PMC8246083 | `d 0.027 mmol g−1 at 0.98 b` |  |
| PMC8246083 | `d 0.070 mmol g−1 at 0.85 b` |  |
| PMC8246083 | `d 0.070 mmol g−1 at 0.85 b` |  |
| PMC8246083 | `e (1.21 mmol g−1 at 0.02 b` |  |
| PMC8246083 | `y (1.21 mmol g−1 at 0.02 b` |  |
| PMC8255795 | ` (–OH 3,444 cm–1) was obse` | oui |
| PMC8255795 | `H2 at 1,399 cm–1. Addition` | non |
| PMC8255795 | `OH at 1,080 cm–1 (). These` | non |
| PMC8255795 | `p (C=O 1706 cm–1) and the ` | oui |
| PMC8255795 | `–H at 2,986 cm–1 and stret` | non |
| PMC8255795 | `–O at 1,170 cm–1 and C–OH ` | non |
| PMC8257353 | ` C=N+ (1425 cm−1), and ami` |  |
| PMC8257353 | ` at 1637.14 cm−1, which is` |  |
| PMC8257353 | `(−OH) (3423 cm−1). In part` |  |
| PMC8257353 | `, C-H (1429 cm−1), and hyd` |  |
| PMC8257353 | `22 and 1618 cm−1, respecti` |  |
| PMC8257353 | `54 and 1632 cm−1 are attri` |  |
| PMC8257353 | `63 and 3340 cm−1, respecti` |  |
| PMC8257353 | `FeOO− (1637 cm−1), and hyd` |  |
| PMC8257353 | `alkene (845 cm−1), C-O epo` |  |
| PMC8257353 | `ation (1094 cm−1), FeOO− (` |  |
| PMC8257353 | `ation (1201 cm−1), C=O str` |  |
| PMC8257353 | `ation (1707 cm−1), and –OH` |  |
| PMC8257353 | `d 64.54 emu·gr−1 for GO-Fe` |  |
| PMC8257353 | `e Fe-O (546 cm−1), sp2 C-H` |  |
| PMC8257353 | `group (3224 cm−1). Besides` |  |
| PMC8257353 | `mber of 543 cm−1. Moreover` |  |
| PMC8257353 | `mber of 583 cm−1 confirms ` |  |
| PMC8257353 | `of 4000–400 cm−1. The EDX ` |  |
| PMC8257353 | `ons 530–630 cm−1 correspon` |  |
| PMC8257353 | `oxide (1091 cm−1), C-H (14` |  |
| PMC8257353 | `oxide (1098 cm−1), C=N+ (1` |  |
| PMC8257353 | `p2 C-H (829 cm−1), C-O fun` |  |
| PMC8257353 | `p2 C-H (837 cm−1), C-O epo` |  |
| PMC8257353 | `rint at 537 cm−1 related t` |  |
| PMC8257353 | `roups (1111 cm−1), C-O str` |  |
| PMC8257353 | `roups (1548 cm−1) improved` |  |
| PMC8257353 | `roups (3206 cm−1). These o` |  |
| PMC8257353 | `uted-E (908 cm−1), C-H str` |  |
| PMC8263741 | ` 1.2×10−3 S cm−1), was det` | oui |
| PMC8263741 | ` 1.7×10−5 S cm−1, similar ` | oui |
| PMC8263741 | ` 2.3×10−6 S cm−1 (250 °C).` | oui |
| PMC8263741 | ` 2.6×10−3 S cm−1 (175 °C) ` | oui |
| PMC8263741 | ` 3.5×10−3 S cm−1 (200 °C) ` | oui |
| PMC8263741 | ` 4.2×10−6 S cm−1 (175 °C) ` | oui |
| PMC8263741 | ` 6.4×10−5 S cm−1 at 200 an` | oui |
| PMC8263741 | ` 6.6×10−4 S cm−1. This tre` | non |
| PMC8263741 | ` 7.3×10−5 S cm−1 was deter` | oui |
| PMC8263741 | ` and 10–4 S cm–1, regardle` | non |
| PMC8263741 | ` of 8.3 °C min−1 (Figure S` | oui |
| PMC8263741 | ` or 8.3 °C min−1 from 30 t` | non |
| PMC8263741 | ` °C) to 2.3×10−6 S cm−1 (2` | oui |
| PMC8263741 | `.1 × 10−3 S cm−1). We hypo` | non |
| PMC8263741 | `.1 × 10−3 S cm−1. On subse` | non |
| PMC8263741 | `.3 × 10−5 S cm−1 were obta` | oui |
| PMC8263741 | `.5 × 10−3 S cm−1 vs 1.1 × ` | oui |
| PMC8263741 | `0 °C (5 °C min–1 heating r` | oui |
| PMC8263741 | `0.05–0.1 mS cm−1 were achi` | non |
| PMC8263741 | `0−4 and 6.4×10−5 S cm−1 at` | oui |
| PMC8263741 | `3 and 3.5 × 10−3 S cm−1 vs` | oui |
| PMC8263741 | `6 to 3.5 mS cm–1 can be ac` | oui |
| PMC8263741 | `7 to 2.65 g cm−3 with incr` | oui |
| PMC8263741 | `C to 1.53 g cm−3 at 250 °C` | oui |
| PMC8263741 | `alue of 1.7×10−5 S cm−1, s` | oui |
| PMC8263741 | `alue of 7.3×10−5 S cm−1 wa` | oui |
| PMC8263741 | `ased (2.6 × 10−3 and 3.5 ×` | oui |
| PMC8263741 | `d to 3.06 g cm−3 upon incr` | oui |
| PMC8263741 | `ease to 6.6×10−4 S cm−1. T` | oui |
| PMC8263741 | `ed from 4.2×10−6 S cm−1 (1` | oui |
| PMC8263741 | `en 10–5 and 10–4 S cm–1, r` | non |
| PMC8263741 | `from 1.47 g cm−3 at 175 °C` | oui |
| PMC8263741 | `ng to 1.1 × 10−3 S cm−1. O` | oui |
| PMC8263741 | `nge between 10–5 and 10–4 ` | non |
| PMC8263741 | `of ~ 10–1 S cm–1 at room t` | non |
| PMC8263741 | `r to 2.95 g cm−3 at 250 °C` | oui |
| PMC8263741 | `te of 500 °C h−1 and kept ` | oui |
| PMC8263741 | `te of 500 °C h−1. As can b` | non |
| PMC8263741 | `tes (≥ 1 mS cm–1)3–6. Amon` | non |
| PMC8263741 | `th = 2.29 g cm−3) impuriti` | non |
| PMC8263741 | `th = 4.09 g cm−3) and Li6P` | non |
| PMC8263741 | `ties of 1.5×10−4 and 6.4×1` | oui |
| PMC8263741 | `ties of 2.6×10−3 S cm−1 (1` | oui |
| PMC8263741 | `tivity of ~ 10–1 S cm–1 at` | non |
| PMC8263741 | `ty of 7.3 × 10−5 S cm−1 we` | oui |
| PMC8263741 | `ved (2.58 g cm−3 at 200 °C` | oui |
| PMC8263741 | `y of 2.38 g cm−3 was found` | oui |
| PMC8263741 | `y of 2.45 g cm−3 for tetra` | oui |
| PMC8263741 | `y of 4.57 g cm−3 was calcu` | oui |
| PMC8263741 | `°C (~ 2 °C min–1 heating r` | oui |
| PMC8263741 | `°C) and 3.5×10−3 S cm−1 (2` | oui |
| PMC8263741 | `–LiI (~ 1.2×10−3 S cm−1), ` | oui |
| PMC8263741 | `−1 vs 1.1 × 10−3 S cm−1). ` | oui |
| PMC8292365 | ` RhB, Co (mg L−1) is the i` | non |
| PMC8292365 | ` about 17.9 cm−1 may come ` | non |
| PMC8292365 | ` and 0.11450 h−1, respecti` | oui |
| PMC8292365 | ` and ~ 1605 cm−1 (G band) ` | non |
| PMC8292365 | ` is 48.78 m2 g−1, much hig` | oui |
| PMC8292365 | ` of 400–600 cm−1 were pres` | non |
| PMC8292365 | ` where C (mg L−1) is the e` | non |
| PMC8292365 | `) and 402.0 cm−1 (A1g) tha` | non |
| PMC8292365 | `00 (29.35 m2 g−1) compared` | non |
| PMC8292365 | `3 and 636.2 cm−1 via chang` | non |
| PMC8292365 | `N4 (14.44 m2 g−1). The red` | non |
| PMC8292365 | `ak at 636.2 cm−1 could als` | non |
| PMC8292365 | `ak at 726.6 cm−1 correspon` | oui |
| PMC8292365 | `eaks at 809 cm−1, and in t` | non |
| PMC8292365 | `f 1000–1800 cm−1 as shown ` | non |
| PMC8292365 | `f 1250–1632 cm−1 are attri` | non |
| PMC8292365 | `ks at 377.2 cm−1 (E12g) an` | non |
| PMC8292365 | `peak at 419 cm−1 correspon` | non |
| PMC8292365 | `red at 3453 cm−1 are ascri` | non |
| PMC8292365 | `rs at 708.7 cm−1 for CN-50` | oui |
| PMC8292365 | `s at ~ 1354 cm−1 (D band) ` | non |
| PMC8292365 | `sing a 30 mg L−1 solution ` | non |
| PMC8292365 | `time, and k (h−1) is the r` | non |
| PMC8307816 | ` at ca. 220 cm−1 to 320 cm` |  |
| PMC8307816 | `O) and 1120 cm−1 (2 TO), a` |  |
| PMC8307816 | `ca. 570–580 cm−1 [,], it c` |  |
| PMC8307816 | `ca. 720–730 cm−1 was diagn` |  |
| PMC8307816 | `cm−1 to 320 cm−1, triangul` |  |
| PMC8307816 | `mode at 560 cm−1 for TiN. ` |  |
| PMC8307816 | `odes at 560 cm−1 with a we` |  |
| PMC8307816 | `s up to 620 cm−1, and two ` |  |
| PMC8309541 | ` and 1433.8 cm−1 correspon` | non |
| PMC8309541 | ` and 1546.7 cm−1 correspon` | non |
| PMC8309541 | `cm−1 to 510 cm−1 are relat` | non |
| PMC8309541 | `eaks in 400 cm−1 to 510 cm` | non |
| PMC8309541 | `k at 1640.8 cm−1 results i` | non |
| PMC8309541 | `of 900–1300 cm−1 can be at` | non |
| PMC8309541 | `ound 2341.4 cm−1 is caused` | non |
| PMC8309541 | `round 838.6 cm−1 are in-pl` | non |
| PMC8309541 | `t 3200–3600 cm−1 correspon` | oui |
| PMC8347744 | ` 900 to 650 cm−1 [] sugges` | non |
| PMC8347744 | ` and 1631.7 cm−1, correspo` | non |
| PMC8347744 | ` and 2852.6 cm−1, respecti` | non |
| PMC8347744 | ` around 585 cm−1, caused b` | oui |
| PMC8347744 | ` of 10−8 to 10−9 Torr in t` | non |
| PMC8347744 | `340 to 2360 cm−1 are relat` | non |
| PMC8347744 | `a of 7.58 m2 g−1, the surf` | non |
| PMC8347744 | `aks at 1095 cm−1 and 1020 ` | non |
| PMC8347744 | `aks at 2935 cm−1 and 2842.` | non |
| PMC8347744 | `and 2842.9 cm −1, ascribed` | non |
| PMC8347744 | `d at 1261.4 cm−1 could be ` | non |
| PMC8347744 | `eak at 1261 cm−1 specific ` | non |
| PMC8347744 | `eak at 1382 cm−1, which ca` | non |
| PMC8347744 | `en (250 mL min−1) until th` | non |
| PMC8347744 | `lution of 2 cm−1 and 32 sc` | non |
| PMC8347744 | `m−1 and 410 cm−1 were due ` | non |
| PMC8347744 | `of 400–4000 cm−1 with a re` | non |
| PMC8347744 | `pressure of 10−8 to 10−9 T` | non |
| PMC8347744 | `t about 685 cm−1 and 410 c` | non |
| PMC8347744 | `−1 and 1020 cm−1, specific` | non |
| PMC8348040 | ` (1050–1100 cm−1). Importa` |  |
| PMC8348040 | ` (2850–3000 cm−1). This fa` |  |
| PMC8348040 | ` of 0.35 cm3 g−1 (Table 2,` |  |
| PMC8348040 | ` of 0.42 cm3 g−1 (Table 2,` |  |
| PMC8348040 | ` of 0.47 cm3 g−1, and a me` |  |
| PMC8348040 | ` to 0.83 cm3 g−1. The size` |  |
| PMC8348040 | `) with 1 mg mL−1 concentra` |  |
| PMC8348040 | `00 and 4000 cm−1. Finally,` |  |
| PMC8348040 | `4000 to 400 cm−1 with a st` |  |
| PMC8348040 | `5 and 673 m2 g−1, respecti` |  |
| PMC8348040 | `a of 1073 m2 g−1 (Table 2,` |  |
| PMC8348040 | `ds (450–500 cm−1), –Si–O–S` |  |
| PMC8348040 | `ds (760–800 cm−1), and –Si` |  |
| PMC8348040 | `ea of 375 m2 g−1 (Table 2,` |  |
| PMC8348040 | `ea of 383 m2 g−1 and a tot` |  |
| PMC8348040 | `ea of 606 m2 g−1 and a por` |  |
| PMC8348040 | `ea of 673 m2 g−1, a total ` |  |
| PMC8348040 | `ea of 685 m2 g−1 (Table 2,` |  |
| PMC8348040 | `ed (0.04 mg mL−1) in ultra` |  |
| PMC8348040 | `ge (0.80 cm3 g−1) and the ` |  |
| PMC8348040 | `ound 100 μg mL−1 [,]. Othe` |  |
| PMC8348040 | `p size of 2 cm−1 and colle` |  |
| PMC8348040 | `p to 1073 m2 g−1 and total` |  |
| PMC8348040 | `to be 496 m2 g−1 and the p` |  |
| PMC8348040 | `ue of 632 m2 g−1 (Entry 6)` |  |
| PMC8348040 | `was 0.35 cm3 g−1. The samp` |  |
| PMC8348040 | `was 0.83 cm3 g−1 and the p` |  |
| PMC8348040 | `°C at 5 °C min−1 (URJC, Mó` |  |
| PMC8360258 | ` below 2000 cm−1 (C = O/C ` |  |
| PMC8360258 | `around 3000 cm−1 (C–H stre` |  |
| PMC8360258 | `ched 0.3 mg cm−2.CO2 RR Te` |  |
| PMC8360258 | `lity (1243 g L−1 at 25 °C)` |  |
| PMC8360258 | `olerance of 10−6 eV. The v` |  |
| PMC8398574 | `3 = μʺ(μʹ)−2f −1 should be` | non |
| PMC8398574 | `σd2/3 = μʺ(μʹ)−2f −1 shoul` | non |
| PMC8401075 | `00 and 3600 cm−1 were assi` |  |
| PMC8401075 | `000 and 400 cm−1 at a reso` |  |
| PMC8401075 | `11 and 3435 cm−1 was an in` |  |
| PMC8401075 | `382 and 656 cm−1, which ar` |  |
| PMC8401075 | `382 and 671 cm−1 in the sy` |  |
| PMC8401075 | `382 and 671 cm−1 in the sy` |  |
| PMC8401075 | `45 and 1642 cm−1 are attri` |  |
| PMC8401075 | `656 and 671 cm−1 were assi` |  |
| PMC8401075 | `88 and 2078 cm−1, represen` |  |
| PMC8401075 | `d. The 1382 cm−1 peak was ` |  |
| PMC8401075 | `lution of 4 cm−1 in the tr` |  |
| PMC8401075 | `nd 0.61127 min−1, respecti` |  |
| PMC8401075 | `or Δν = 823 cm−1) []. Such` |  |
| PMC8401075 | `or Δν = 938 cm−1) and Rhod` |  |
| PMC8401075 | `ν = 8884.15 cm−1) in compa` |  |
| PMC8424352 | ` at 950–970 cm−1 []. In th` | non |
| PMC8424352 | ` at 960–962 cm−1 and (iv) ` | non |
| PMC8424352 | `01 and 1458 cm−1) and the ` | non |
| PMC8424352 | `01 and 1458 cm−1).A bar di` | non |
| PMC8424352 | `458 and 601 cm−1, respecti` | non |
| PMC8424352 | `565 and 603 cm−1 further e` | non |
| PMC8424352 | `585 and 609 cm−1, (iii) υ1` | non |
| PMC8424352 | `73 and 1458 cm−1 supported` | oui |
| PMC8424352 | `974 and 945 cm−1) [,] with` | non |
| PMC8424352 | `ands at 630 cm−1 and 3400–` | non |
| PMC8424352 | `ature, 3°C min−1 for 1 h. ` | oui |
| PMC8424352 | `d 1041–1088 cm−1 are repre` | non |
| PMC8424352 | `d 3400–3600 cm−1 regions, ` | non |
| PMC8424352 | `ding at 427 cm−1, (ii) υ4 ` | non |
| PMC8424352 | `gion of 630 cm−1 but the o` | non |
| PMC8424352 | `ift at 1065 cm−1 [,]. A co` | non |
| PMC8424352 | `n 1035–1045 cm−1. These ob` | non |
| PMC8424352 | `nd (at 1047 cm−1) []. More` | non |
| PMC8424352 | `pprox. 1050 cm−1) []. But ` | non |
| PMC8424352 | `pprox. 1070 cm−1) with tha` | non |
| PMC8424352 | `t 3400–3600 cm−1) for the ` | non |
| PMC8424352 | `te at 20°C min−1, the TG p` | non |
| PMC8433875 | `(90–100 °C, 10−3 mbar). Af` | oui |
| PMC8433875 | `itions (p < 10−6 bar), equ` | oui |
| PMC8434467 | ` = 12.6 kg mol−1), and zwi` |  |
| PMC8434467 | `1, and 1120 cm−1 were assi` |  |
| PMC8434467 | `33 and 1090 cm−1 were rela` |  |
| PMC8434467 | `565 and 603 cm−1 were attr` |  |
| PMC8434467 | `and at 3571 cm−1 correspon` |  |
| PMC8434467 | `eak at 1460 cm−1 was assig` |  |
| PMC8434467 | `eak at 1550 cm−1 belonged ` |  |
| PMC8434467 | `nd near 875 cm−1 may be du` |  |
| PMC8434467 | `ν3) and 633 cm−1 (νL) were` |  |
| PMC8464746 | `00 and 1720 cm–1 are attri` | non |
| PMC8464746 | `50, and 994 cm–1 indicated` | non |
| PMC8464746 | `]. The 2933 cm–1 was the s` | non |
| PMC8464746 | `ated at 890 cm–1 []. The a` | non |
| PMC8464746 | `eak at 1100 cm–1 was attri` | non |
| PMC8464746 | `red at 1090 cm−1 was attri` | oui |
| PMC8464746 | `und at 2600 cm−1 and 1843 ` | non |
| PMC8464746 | `−1 and 1843 cm–1, indicati` | non |
| PMC8465261 | ` cm−1, 1400 cm−1, and 1380` |  |
| PMC8465261 | ` to 50 µmol dm−3 with a de` |  |
| PMC8465261 | ` to 50 µmol dm−3, with the` |  |
| PMC8465261 | `.5–300 µmol dm−3 using flu` |  |
| PMC8465261 | `1, and 1380 cm−1 could be ` |  |
| PMC8465261 | `= 0–1.0 mol dm−3) was also` |  |
| PMC8465261 | `aks at 1417 cm−1, 1400 cm−` |  |
| PMC8465261 | `between 674 cm−1 and 640 c` |  |
| PMC8465261 | `from 7 µmol dm−3 to 50 µmo` |  |
| PMC8465261 | `from 7 µmol dm−3 to 50 µmo` |  |
| PMC8465261 | `he 4000–400 cm−1 spectral ` |  |
| PMC8465261 | `lution of 4 cm−1. Briefly,` |  |
| PMC8465261 | `m−1 and 640 cm−1 could ind` |  |
| PMC8465261 | `om 0.5 µmol dm−3 to 300 µm` |  |
| PMC8465261 | `red at 1580 cm−1 could ind` |  |
| PMC8465261 | `red at 1680 cm−1 and 1041 ` |  |
| PMC8465261 | `s (100 µmol dm−3) were pre` |  |
| PMC8465261 | `to 300 µmol dm−3, and the ` |  |
| PMC8465261 | `y 3267–3305 cm−1 which ind` |  |
| PMC8465261 | `± 0.27 µmol dm−3 and limit` |  |
| PMC8465261 | `± 0.27 µmol dm−3, and the ` |  |
| PMC8465261 | `± 0.89 µmol dm−3 (Figure 6` |  |
| PMC8465261 | `± 0.89 µmol dm−3. These fi` |  |
| PMC8465261 | `−1 and 1041 cm−1 could be ` |  |
| PMC8474143 | ` C=O (∼1750 cm–1) peak are` | non |
| PMC8474143 | `nd at ∼2100 cm–1 correspon` | non |
| PMC8474143 | `re at ∼1100 cm–1 can be as` | non |
| PMC8495851 | `02 and 1088 cm–1 represent` | oui |
| PMC8495851 | `3, and 1364 cm–1, respecti` | non |
| PMC8495851 | `6, and 1384 cm–1. At 1103 ` | oui |
| PMC8495851 | `86 and 1498 cm–1.Compared ` | non |
| PMC8495851 | `9, and 1478 cm–1 of the sp` | oui |
| PMC8495851 | `ANI at 1578 cm–1, which is` | oui |
| PMC8495851 | `PPy at 1576 cm–1, which is` | oui |
| PMC8495851 | `eak at 3448 cm–1 represent` | oui |
| PMC8495851 | `ears at 615 cm–1, demonstr` | oui |
| PMC8495851 | `ted to 1182 cm–1. Simultan` | oui |
| PMC8495851 | `–1. At 1103 cm–1, the char` | oui |
| PMC8539213 | ` CZEYG, 600 cm−1 for CZLPY` | oui |
| PMC8539213 | ` CZLPG, 605 cm−1 for CZEYG` | oui |
| PMC8539213 | ` at 1.5 mL min−1; injectio` | non |
| PMC8539213 | `C at 15 °C min−1; injectio` | non |
| PMC8539213 | `PY, and 603 cm−1 for CZLEY` | oui |
| PMC8539213 | `band at 464 cm−1 is typica` | non |
| PMC8539213 | `hift of ~15 cm−1, which is` | non |
| PMC8539213 | `ible at 597 cm−1 for CZLPG` | oui |
| PMC8539213 | `te of 10 K·min−1 up to 800` | oui |
| PMC8544586 | `00 and 1700 cm−1, which is` |  |
| PMC8544586 | `4000 to 400 cm−1. The spec` |  |
| PMC8544586 | `603 and 566 cm−1 can be at` |  |
| PMC8544586 | `aks at 2002 cm−1 and 1274 ` |  |
| PMC8544586 | `eak at 1034 cm−1 are attri` |  |
| PMC8544586 | `eak at 3572 cm−1 and a bro` |  |
| PMC8544586 | `f 104 cells⋅cm−2.The sampl` |  |
| PMC8544586 | `g at 631.77 cm−1 belongs t` |  |
| PMC8544586 | `ium (4500 mg⋅L−1) suppleme` |  |
| PMC8544586 | `m and 2 mmol⋅L−1 of L-glut` |  |
| PMC8544586 | `peak at 946 cm−1 can be at` |  |
| PMC8544586 | `te of 1 mL⋅min−1. The mola` |  |
| PMC8544586 | `ution was 4 cm−1 and the t` |  |
| PMC8544586 | `−1 and 1274 cm−1 correspon` |  |
| PMC8587718 | ` and 8.72 × 10−7 M, respec` |  |
| PMC8587718 | ` was 2.71 × 10−7 and 8.72 ` |  |
| PMC8587718 | ` was 8.72 × 10−7 M. The CI` |  |
| PMC8587718 | `d as 2.71 × 10−7 M. Figure` |  |
| PMC8587718 | `of 4000–400 cm−1 to determ` |  |
| PMC8587718 | `red at 1720 cm−1 in the or` |  |
| PMC8587718 | `tion of 1 × 10−4 M. The re` |  |
| PMC8600520 | `(3360–3400) cm–1 assigned ` | non |
| PMC8600520 | `56 and 1623 cm–1 appear as` | non |
| PMC8600520 | `lution of 4 cm–1 and 128 s` | oui |
| PMC8600520 | `of 400–4000 cm–1. XRD patt` | non |
| PMC8621345 | ` 5 to 100 mg·L−1. Single a` | non |
| PMC8621345 | ` CR—182.7 mg·g−1). It was ` | non |
| PMC8621345 | ` values) (mg·L−1), V repre` | non |
| PMC8621345 | `(MO—256.3 mg·g−1, CR—182.7` | non |
| PMC8621345 | `596 and 410 cm−1 in the sp` | oui |
| PMC8621345 | `600 and 417 cm−1 which are` | oui |
| PMC8621345 | `a (4000–400 cm−1) were rec` | non |
| PMC8621345 | `and 13.96 mg·g−1 for MO, r` | oui |
| PMC8621345 | `ct times (mg·g−1), C0 mean` | non |
| PMC8621345 | `desorbed (mg·L−1), V means` | non |
| PMC8621345 | `er, 41.64 mg·g−1. For all ` | non |
| PMC8621345 | `f 1000–1500 cm−1 could be ` | non |
| PMC8621345 | `ilibrium (mg·g−1). (3)QD=C` | non |
| PMC8621345 | `ntration (mg·L−1), Ct defi` | non |
| PMC8621345 | `of 4000–400 cm−1, are show` | non |
| PMC8621345 | `on of 100 mg·L−1 was conta` | oui |
| PMC8621345 | `s of 6.65 mg·g−1, while fo` | oui |
| PMC8621345 | `ted at 3391 cm−1 and 1625 ` | non |
| PMC8621345 | `tion (3) (mg·g−1) and Qe i` | non |
| PMC8621345 | `to 178.07 mg g−1 for CR an` | non |
| PMC8621345 | `to 257.25 mg g−1 for MO wi` | non |
| PMC8621345 | `was 24.17 mg·g−1 for CR an` | oui |
| PMC8621345 | `−1 and 1625 cm−1 are chara` | non |
| PMC8621457 | `(C-H), 1706 cm−1 (C=O), 16` |  |
| PMC8621457 | `(C=O), 1630 cm−1 (aromatic` |  |
| PMC8621457 | `, 2920–2880 cm−1 (C-H), 17` |  |
| PMC8621457 | `aks at 3400 cm−1 (-OH), 29` |  |
| PMC8693586 | ` of 1.56 μg mL−1. It seems` |  |
| PMC8693586 | `.8–100.0 μg mL−1) were add` |  |
| PMC8693586 | `.8–200.0 μg mL−1) of AgNPs` |  |
| PMC8693586 | `0 and 10 μg mL−1 of AgNPs ` |  |
| PMC8693586 | `NPs (5.0 μg mL−1) for indi` |  |
| PMC8693586 | `TT) (5.0 μg mL−1, Solarbio` |  |
| PMC8693586 | `act (400 μg mL−1),21 where` |  |
| PMC8693586 | `and 20.0 μg mL−1 of AgNPs,` |  |
| PMC8693586 | `gNPs (10 μg mL−1) into HCT` |  |
| PMC8693586 | `in 100.0 μg mL−1 of AgNPs,` |  |
| PMC8693586 | `ion (2.5 mg mL−1). After t` |  |
| PMC8693586 | `lora (20 μg mL−1 for MCF-7` |  |
| PMC8693586 | `n in 0.8 μg mL−1 of AgNPs.` |  |
| PMC8693586 | `nd 100.0 μg mL−1 of AgNPs,` |  |
| PMC8693586 | `nd 26.18 μg mL−1, respecti` |  |
| PMC8693586 | `nd 26.18 μg mL−1, respecti` |  |
| PMC8693586 | `nd 27.98 μg mL−1 for HCT11` |  |
| PMC8693586 | `nd 69.72 μg mL−1 for HCT11` |  |
| PMC8693586 | `oth 50.0 μg mL−1 for E. co` |  |
| PMC8693586 | `oth 50.0 μg mL−1. By the u` |  |
| PMC8693586 | `stii (51 μg mL−1 for Hela)` |  |
| PMC8693586 | `ted at 15 V cm−1. Data obt` |  |
| PMC8693586 | `to 100.0 μg mL−1 for 24 h.` |  |
| PMC8693747 | ` be 0.0255 min−1, which is` |  |
| PMC8693747 | `1 cm−1, 610 cm−1, and 620 ` |  |
| PMC8693747 | `5, and 1537 cm−1 are assoc` |  |
| PMC8693747 | `and at 3180 cm−1 correspon` |  |
| PMC8693747 | `around 2357 cm−1, which ma` |  |
| PMC8693747 | `around 3100 cm−1 correspon` |  |
| PMC8693747 | `band at 804 cm−1 correspon` |  |
| PMC8693747 | `d from 3400 cm−1 to 3330 c` |  |
| PMC8693747 | `ea (11.12 m2 g−1), while t` |  |
| PMC8693747 | `ea (60.90 m2 g−1). The gre` |  |
| PMC8693747 | `eak at 1313 cm−1 is associ` |  |
| PMC8693747 | `etween 1650 cm−1 and 1150 ` |  |
| PMC8693747 | `lution of 1 cm−1. The opti` |  |
| PMC8693747 | `m−1 to 1420 cm−1, which ar` |  |
| PMC8693747 | `m−1 to 3330 cm−1 for the s` |  |
| PMC8693747 | `nge of 1380 cm−1 to 1420 c` |  |
| PMC8693747 | `peak at 805 cm−1 matches t` |  |
| PMC8693747 | `peak at 806 cm−1 correspon` |  |
| PMC8693747 | `peak at 858 cm−1 is mostly` |  |
| PMC8693747 | `pear at 601 cm−1, 610 cm−1` |  |
| PMC8693747 | `rved at 722 cm−1 is associ` |  |
| PMC8693747 | `ted at 1400 cm−1 correspon` |  |
| PMC8693747 | `ted at 3400 cm−1 is relate` |  |
| PMC8693747 | `ved at 1033 cm−1. This con` |  |
| PMC8693747 | `ved at 1110 cm−1 due to th` |  |
| PMC8693747 | `ved at 1615 cm−1 due to th` |  |
| PMC8693747 | `ved at 2150 cm−1, which ma` |  |
| PMC8693747 | `−1 and 1150 cm−1, which ar` |  |
| PMC8693747 | `−1, and 620 cm−1 due to th` |  |
| PMC8695884 | ` to 0.5 mmol L−1) were sep` | non |
| PMC8695884 | `L−1 and 1 mg L−1 for drink` | non |
| PMC8695884 | `g below 3 mg L−1 and 1 mg ` | non |
| PMC8695884 | `ns (0.01 mol L−1) are prep` | oui |
| PMC8703864 | ` cm−1, 1125 cm−1, and 1482` | oui |
| PMC8703864 | `1, and 1482 cm−1, respecti` | oui |
| PMC8703864 | `470 and 509 cm−1 are produ` | non |
| PMC8703864 | `and at 1397 cm−1. The band` | non |
| PMC8703864 | `band at 938 cm−1 also repr` | non |
| PMC8703864 | `ced at 1071 cm−1, 1125 cm−` | oui |
| PMC8703864 | `eak at 1643 cm−1 is from t` | oui |
| PMC8703864 | `n 3200–3400 cm−1 as shown ` | non |
| PMC8703864 | `rate of 4° min−1. The morp` | non |
| PMC8708305 | ` and 1804 mA g−1, respecti` | oui |
| PMC8708305 | ` of 1086 mAh g−1 during th` | oui |
| PMC8708305 | ` of 1100 mAh g−1 after 100` | non |
| PMC8708305 | `(10.3 × 10−6 K−1 of NiFe2O` | non |
| PMC8708305 | `1 C = 915 mA g−1) and at a` | oui |
| PMC8708305 | `O4 (~915 mAh g−1), which i` | oui |
| PMC8708305 | `O4 and 16 × 10−6 K−1 of st` | non |
| PMC8708305 | `and 1804 mAh g−1, and the ` | oui |
| PMC8708305 | `down to 3 × 10−6 Torr, and` | oui |
| PMC8708305 | `han 1000 mAh g−1. This ind` | non |
| PMC8708305 | `ite (372 mAh g−1). The tra` | non |
| PMC8708305 | `nd 16 × 10−6 K−1 of stainl` | non |
| PMC8708305 | `nts (10.3 × 10−6 K−1 of Ni` | non |
| PMC8708305 | `out 1100 mAh g−1 was stabl` | oui |
| PMC8708305 | `te of 0.1 mV s−1 in the po` | oui |
| PMC8708305 | `te of 0.5 mV s−1, respecti` | oui |
| PMC8708305 | `te of 0.5 mV s−1. All the ` | non |
| PMC8708305 | `y of 91.5 mA g−1 (0.1C) an` | oui |
| PMC8708305 | `y of 91.5 mA g−1 for 100 c` | oui |
| PMC8708305 | `y of 915 mAh g−1, which ca` | non |
| PMC8717584 | ` 500 to 800 cm–1 can be in` | oui |
| PMC8717584 | `0, and 3410 cm–1 indicate ` | oui |
| PMC8717584 | `0, and 3410 cm–1. A combin` | non |
| PMC8717584 | `0, and 3450 cm–1, correspo` | non |
| PMC8717584 | `50 and 1630 cm–1 are relat` | oui |
| PMC8717584 | `peak at 600 cm–1 is relate` | non |
| PMC8717584 | `–O–C at 600 cm–1 can also ` | non |
| PMC8830207 | ` about 1620 cm–1 due to be` |  |
| PMC8830207 | `0 to 0.3 mol L–1), or a pH` |  |
| PMC8830207 | `20 and 1585 cm–1 may colle` |  |
| PMC8830207 | `20 and 3520 cm–1.47 The T-` |  |
| PMC8830207 | `22 and 1616 cm–1, while th` |  |
| PMC8830207 | `78 and 1625 cm–1 are assoc` |  |
| PMC8830207 | `80 and 1256 cm–1 are ascri` |  |
| PMC8830207 | `88 and 1272 cm–1, again du` |  |
| PMC8830207 | `C=O at 1755 cm–1 and of C=` |  |
| PMC8830207 | `HCl (0.1 mol L–1) in the a` |  |
| PMC8830207 | `HCl (0.1 mol L–1) was intr` |  |
| PMC8830207 | `and at 1428 cm–1 can be as` |  |
| PMC8830207 | `around 1665 cm–1, a concer` |  |
| PMC8830207 | `at a 10 °C min–1 rate.Ultr` |  |
| PMC8830207 | `d 3000–3500 cm–1, indicati` |  |
| PMC8830207 | `g., at 1380 cm–1) resembli` |  |
| PMC8830207 | `i] = 0.3 mol L–1 and HCl (` |  |
| PMC8830207 | `i] = 0.5 mol L–1) and less` |  |
| PMC8830207 | `i] ≥ 0.5 mol L–1, immediat` |  |
| PMC8830207 | `lution of 2 cm–1.Thermogra` |  |
| PMC8830207 | `nds at 1172 cm–1 and lower` |  |
| PMC8830207 | `ode at 1320 cm–1, and the ` |  |
| PMC8830207 | `one at 1208 cm–1 is associ` |  |
| PMC8830207 | `re about 10 cm–1 lower com` |  |
| PMC8830207 | `red at 1400 cm–1, absent i` |  |
| PMC8830207 | `s below 800 cm–1; an inten` |  |
| PMC8830207 | `ted to 1363 cm–1.47 The st` |  |
| PMC8830207 | `yte (0.1 mol L–1 KNO3, pH ` |  |
| PMC8838941 | ` (or 9.36 mg·g−1) for Cr(V` | oui |
| PMC8838941 | ` 0.0583 mmol·g−1 (or 12.08` | oui |
| PMC8838941 | ` about 3424 cm−1. The stre` | non |
| PMC8838941 | ` below 1000 cm−1 had an ob` | non |
| PMC8838941 | ` dosage in g·L−1.The adsor` | non |
| PMC8838941 | `(or 12.08 mg·g−1) for Pb(Ⅱ` | oui |
| PMC8838941 | `660 and 629 cm−1, respecti` | oui |
| PMC8838941 | `84, and 669 cm−1 could be ` | non |
| PMC8838941 | `bent in mmol·g−1, and 1/n ` | non |
| PMC8838941 | `bent in mmol·g−1; C0 is th` | non |
| PMC8838941 | `d 0.180 mmol·g−1 (or 9.36 ` | oui |
| PMC8838941 | `eak at 1709 cm−1, which mi` | oui |
| PMC8838941 | `ion in 25 mg·L−1 heavy met` | oui |
| PMC8838941 | `ion of 4.00 cm−1. The powd` | non |
| PMC8838941 | `l ions in mg·L−1; Ce is th` | non |
| PMC8838941 | `n g mmol−1 min−1.The regre` | non |
| PMC8838941 | `of 1250.4 m2·g−1 and an av` | non |
| PMC8838941 | `of 400–4000 cm−1 on a Nico` | non |
| PMC8838941 | `om 20–100 mg·L−1.The Langm` | non |
| PMC8838941 | `onstant in min−1 used as t` | non |
| PMC8838941 | `orption in min−1. The pseu` | non |
| PMC8838941 | `osage of 7 g·L−1 in a crys` | oui |
| PMC8838941 | `peed of 5° min−1 (2θ). The` | oui |
| PMC8838941 | `rption in mg·L−1; A is the` | non |
| PMC8838941 | `take in mmol·g−1; b is the` | non |
| PMC8838941 | `ted at 1039 cm−1 red shift` | oui |
| PMC8838941 | `ted at 1629 cm−1. The abso` | non |
| PMC8838941 | `ted at 1636 cm−1 (Figure 2` | oui |
| PMC8838941 | `ted at 3441 cm−1 and 1039 ` | oui |
| PMC8838941 | `thalpy in L·mg−1.The Freun` | non |
| PMC8838941 | `tion in g mmol−1 min−1.The` | non |
| PMC8838941 | `ue of 321 mg·g−1 and an io` | non |
| PMC8838941 | `ue of 961 mg·g−1. In addit` | non |
| PMC8838941 | `−1 and 1039 cm−1, respecti` | oui |
| PMC8850480 | ` 5 meV·Å−1 (10–4 hartree/b` |  |
| PMC8850480 | ` was set at 10−6 for all c` |  |
| PMC8850480 | `, and 21.90 nm−1 (see Supp` |  |
| PMC8850480 | `about 0.015 nm−1 (full wid` |  |
| PMC8850480 | `e from 0.05 nm−1 to 0.2 nm` |  |
| PMC8850480 | `nm−1 to 0.2 nm−1 and, as s` |  |
| PMC8850480 | `nm−1, 15.44 nm−1, and 21.9` |  |
| PMC8850480 | `rce of 5 meV·Å−1 (10–4 har` |  |
| PMC8850480 | `t q = 10.93 nm−1, 15.44 nm` |  |
| PMC8850480 | `ty at q < 2 nm−1 is shown ` |  |
| PMC8866530 | ` (< 10–6 cm2-s-1) and elec` | non |
| PMC8866530 | ` 382–395 mAh-g-1 at the sa` | oui |
| PMC8866530 | ` and 0.7 mg-cm-2. After dr` | non |
| PMC8866530 | ` and 1088 mA-g-1 (Fig. 6b)` | oui |
| PMC8866530 | ` and 395 mAh-g-1, respecti` | oui |
| PMC8866530 | ` at 12.5 mg-mL-1) were com` | oui |
| PMC8866530 | ` at ~ 100 mA-g-1 (with 100` | non |
| PMC8866530 | ` at ~ 100 mA-g-1, subseque` | non |
| PMC8866530 | `% to 637 mAh-g-1, which is` | non |
| PMC8866530 | `10–13 Ohm-1-cm-1) that aff` | non |
| PMC8866530 | `5 to 542 mAh-g-1 at ~ 1000` | oui |
| PMC8866530 | `and 1000 mAh-g-1, but with` | non |
| PMC8866530 | `at ~ 1000 mA-g-1 across 50` | non |
| PMC8866530 | `at ~ 1000 mA-g-1.Results a` | non |
| PMC8866530 | `city 745 mAh-g-1) prepared` | non |
| PMC8866530 | `e of 690 mAh-g-1 across ea` | oui |
| PMC8866530 | `e of 733 mAh-g-1 across cy` | oui |
| PMC8866530 | `ficients (< 10–6 cm2-s-1) ` | non |
| PMC8866530 | `g at 445 mAh-g-1, peaking ` | oui |
| PMC8866530 | `g to 542 mAh-g-1 at cycle ` | oui |
| PMC8866530 | `ies (10–13 Ohm-1-cm-1) tha` | non |
| PMC8866530 | `ity (372 mAh-g-1) than LTO` | non |
| PMC8866530 | `n to 435 mAh-g-1 at the en` | oui |
| PMC8866530 | `near 615 mAh-g-1 at ~ 100 ` | oui |
| PMC8866530 | `ported as mA-g-1, for each` | non |
| PMC8866530 | `s (> 600 mAh-g-1) than mos` | non |
| PMC8866530 | `st at 500 mA-g-1, which is` | non |
| PMC8866530 | `t at 621 mAh-g-1. Figure 6` | non |
| PMC8866530 | `ty of 109 mA-g-1 (Fig. 6a)` | oui |
| PMC8866530 | `uctivities (10–13 Ohm-1-cm-` | non |
| PMC8866530 | `y at 175 mAh-g-1, and low ` | non |
| PMC8866530 | `y of 435 mAh-g-1 after an ` | non |
| PMC8866530 | `y of 437 mAh-g-1 at the en` | oui |
| PMC8866530 | `y of 995 mAh-g-1 at a curr` | oui |
| PMC8866530 | `y of 995 mAh-g-1 at ~ 100 ` | oui |
| PMC8866530 | `y of 995 mAh-g-1, a nearly` | non |
| PMC8930993 | ` 1.84 to 6 A g−1 (Fig. 8d)` | oui |
| PMC8930993 | ` be 2554.9 F g−1. The spec` | non |
| PMC8930993 | ` of 2554.88 Fg−1 at 2.54 A` | non |
| PMC8930993 | `.21, 792.85 cm−1 (symmetri` | oui |
| PMC8930993 | `//AC (30 Wh kg−1 at 2285.7` | oui |
| PMC8930993 | `/rGo (26 Wh kg−1 at 1821 W` | oui |
| PMC8930993 | `1 at 1500 W kg−1), NiCo2S4` | non |
| PMC8930993 | `1 at 1600 W kg−1), and Por` | non |
| PMC8930993 | `1 at 1821 W kg−1), MOF-2/N` | non |
| PMC8930993 | `1 at 7900 W kg−1)34,43,55–` | non |
| PMC8930993 | `4 to 11.04 A g−1, in a vol` | oui |
| PMC8930993 | `40 and 1037 cm−1. Addition` | non |
| PMC8930993 | `54 to 9.09 A g−1 in a pote` | oui |
| PMC8930993 | `54 to 9.09 A g−1. Moreover` | non |
| PMC8930993 | `6.3 and 668 cm−1 are the c` | non |
| PMC8930993 | `AC (26.6 Wh kg−1 at 700 W ` | oui |
| PMC8930993 | `AC (31.2 Wh kg−1 at 775 W ` | oui |
| PMC8930993 | `AC (35.6 Wh kg−1 at 1500 W` | oui |
| PMC8930993 | `C (24.78 Wh kg−1 at 1770.1` | oui |
| PMC8930993 | `C (34.62 Wh kg−1 at 120.19` | oui |
| PMC8930993 | `C (34.67 Wh kg−1 at 120.13` | oui |
| PMC8930993 | `GO (41.9 Wh kg−1 at 698 W ` | oui |
| PMC8930993 | `H) (17.4 Wh kg−1 at 7900 W` | oui |
| PMC8930993 | `P-50 (19 Wh kg−1 at 703 W ` | oui |
| PMC8930993 | `aks at 1552 cm−1 and 1340 ` | oui |
| PMC8930993 | `ars at 1037 cm−1 which may` | non |
| PMC8930993 | `at 120.13 W kg−1), NiCo2S4` | non |
| PMC8930993 | `at 120.19 W kg−1), ND-CoMo` | non |
| PMC8930993 | `at 1770.1 W kg−1), GRH-NiC` | non |
| PMC8930993 | `at 2285.7 W kg−1), NCS@MCM` | non |
| PMC8930993 | `ate of 50 mV s−1 within a ` | oui |
| PMC8930993 | `d 1387.57 F cm−3 at a curr` | oui |
| PMC8930993 | `e of 98.92 F g−1 was achie` | oui |
| PMC8930993 | `f 1472.29 W kg−1. When the` | non |
| PMC8930993 | `f 1847.18 F cm−3 at a curr` | oui |
| PMC8930993 | `g) and 1107 cm−1 (asymmetr` | oui |
| PMC8930993 | `ity (10–100 Sm−1), flexibi` | non |
| PMC8930993 | `k at 934.02 cm−1 could be ` | non |
| PMC8930993 | `lmost 98.9 F g−1 at a disc` | oui |
| PMC8930993 | `lmost 98.9 F g−1 with an e` | non |
| PMC8930993 | `nt of 1.84 A g−1 in a pote` | non |
| PMC8930993 | `nt of 2.54 A g−1, and 1387` | oui |
| PMC8930993 | `nt of 9.09 A g−1 were achi` | oui |
| PMC8930993 | `nt of 9.09 A g−1. The volu` | non |
| PMC8930993 | `of 12.26 Wh kg−1. These va` | non |
| PMC8930993 | `of 35.17 Wh kg−1 at a powe` | oui |
| PMC8930993 | `of 35.17 Wh kg−1 at a powe` | oui |
| PMC8930993 | `rbon (36 Wh kg−1 at 1600 W` | oui |
| PMC8930993 | `s (10–100 mV s−1). It is o` | non |
| PMC8930993 | `s to 8832 W kg−1, the ASC ` | oui |
| PMC8930993 | `te of 100 mV s−1, indicati` | non |
| PMC8930993 | `te of 150 mV s−1 for 1500 ` | non |
| PMC8930993 | `ted at 3411 cm−1 can be as` | non |
| PMC8930993 | `ty of 1.84 A g−1 for the N` | oui |
| PMC8930993 | `ty of 2.54 A g−1, the spec` | oui |
| PMC8930993 | `up to 100 mV s−1 within a ` | oui |
| PMC8930993 | `y of 1472 W kg−1. These re` | non |
| PMC8930993 | `−1 and 1340 cm−1. These pe` | non |
| PMC8930993 | `−1 at 2.54 A g−1 discharge` | non |
| PMC8930993 | `−1 at 698 W kg−1), Co3O4//` | non |
| PMC8930993 | `−1 at 700 W kg−1), RGO/PPy` | non |
| PMC8930993 | `−1 at 703 W kg−1), NiCo2S4` | non |
| PMC8930993 | `−1 at 775 W kg−1), NiCo2O4` | non |
| PMC8941405 | `92 and 1225 cm−1, all appe` | oui |
| PMC8941405 | `Lewis (1454 cm−1) increase` | non |
| PMC8941405 | `and at 3610 cm−1 decreased` | oui |
| PMC8941405 | `eak at 1613 cm−1 was cause` | non |
| PMC8941405 | `eak at 3728 cm−1. With the` | non |
| PMC8941405 | `edra at 450 cm−1, the doub` | oui |
| PMC8941405 | `ernal (3728 cm−1) silanol ` | oui |
| PMC8941405 | `ernal (3745 cm−1) and inte` | oui |
| PMC8941405 | `nsted (1545 cm−1) decrease` | non |
| PMC8941405 | `red at 1613 cm−1, which gr` | oui |
| PMC8941405 | `t 3750–3700 cm−1 and 3610 ` | non |
| PMC8941405 | `tion at 550 cm−1 and the s` | oui |
| PMC8941405 | `−1 and 3610 cm−1, which we` | non |
| PMC8949796 | `3 to 0.5286 nm−1 for the (` | non |
| PMC8949796 | `5 to 0.4629 nm−1 for the (` | non |
| PMC8949796 | `ase at 2.76 nm−1 is notice` | non |
| PMC8949796 | `ion at 2.76 nm−1 [] in Fig` | non |
| PMC8949796 | `ion at 2.76 nm−1 only ascr` | non |
| PMC8966659 | `20, and 984 cm−1, which ap` | non |
| PMC8966659 | `peak at 618 cm−1 ascribed ` | oui |
| PMC8975640 | `0, and 1545 cm−1 character` | oui |
| PMC8975640 | `0, and 3200 cm−1. Moreover` | non |
| PMC8975640 | `00 and 1450 cm−1 is associ` | non |
| PMC8975640 | `00 and 1700 cm−1 is relate` | non |
| PMC8975640 | `00 and 1991 cm−1 are assig` | non |
| PMC8975640 | `15, or 2400 cm−1 [].In sev` | non |
| PMC8975640 | `20 and 1460 cm−1 character` | oui |
| PMC8975640 | `46 and 1029 cm−1. The peak` | non |
| PMC8975640 | `5 to 0.2 mol L−1. The calc` | non |
| PMC8975640 | `563 and 534 cm−1 are due t` | non |
| PMC8975640 | `571 and 634 cm−1 are assig` | oui |
| PMC8975640 | `60 and 2341 cm−1 []. The C` | non |
| PMC8975640 | `60 and 2341 cm−1 can be re` | non |
| PMC8975640 | `602 and 562 cm−1 are assig` | non |
| PMC8975640 | `62, and 473 cm−1 are assig` | oui |
| PMC8975640 | `66, and 995 cm−1 related t` | non |
| PMC8975640 | `aks at 2070 cm−1 have been` | non |
| PMC8975640 | `and at 1647 cm−1 was attri` | non |
| PMC8975640 | `band at 889 cm−1 related t` | non |
| PMC8975640 | `e 2840–3000 cm−1. There ar` | non |
| PMC8975640 | `eak at 1094 cm−1 emanates ` | non |
| PMC8975640 | `eak at 3400 cm−1 is assign` | non |
| PMC8975640 | `eaks at 473 cm−1 are compo` | oui |
| PMC8975640 | `ge from 400 cm−1 to 4000 c` | oui |
| PMC8975640 | `ile the 432 cm−1 band is d` | non |
| PMC8975640 | `mately 3440 cm−1 is relate` | non |
| PMC8975640 | `m−1 to 4000 cm−1. The samp` | non |
| PMC8975640 | `peak at 962 cm−1 is assign` | non |
| PMC8975640 | `rved at 874 cm−1 []. It mi` | non |
| PMC8975640 | `te groups (PO4−3) and hydr` | non |
| PMC8981000 | ` (349.937 m2 g−1) than the` | non |
| PMC8981000 | ` (369.791 m2 g−1) as well ` | non |
| PMC8981000 | ` around 442 cm−1, while th` | non |
| PMC8981000 | ` around 547 cm−1 and 1250 ` | non |
| PMC8981000 | ` around 550 cm−1 indicates` | non |
| PMC8981000 | `2, and 1250 cm−1 are attri` | non |
| PMC8981000 | `45 and 1632 cm−1 related t` | non |
| PMC8981000 | `45 and 1642 cm−1 assigned ` | non |
| PMC8981000 | `5, and 1640 cm−1 (Fig. 2e)` | oui |
| PMC8981000 | `5, and 1640 cm−1. The abso` | non |
| PMC8981000 | `and at 1490 cm−1 assigned ` | non |
| PMC8981000 | `at near 550 cm−1 whose pos` | non |
| PMC8981000 | `d 306.311 m2 g−1), and the` | non |
| PMC8981000 | `d 335.595 m2 g−1), respect` | non |
| PMC8981000 | `d 339.950 m2 g−1), and ext` | non |
| PMC8981000 | `peak at 547 cm−1 was incre` | non |
| PMC8981000 | `−1 and 1250 cm−1 indicated` | non |
| PMC8981973 | ` 1586, 1396 cm−1 and 1506,` | non |
| PMC8981973 | ` O and 1315 cm−1 assigned ` | non |
| PMC8981973 | ` and 1134 m2 g−1 with the ` | oui |
| PMC8981973 | ` and 1451 m2 g−1, respecti` | oui |
| PMC8981973 | ` around 680 cm−1 as well a` | oui |
| PMC8981973 | ` from 410 m2 g−1 of the mo` | oui |
| PMC8981973 | ` of 50–7800 cm−1. The elem` | non |
| PMC8981973 | `C at 10 °C min−1. Surface ` | non |
| PMC8981973 | `aks at 1506 cm−1 (vibratio` | non |
| PMC8981973 | `around 1680 cm−1 assigned ` | oui |
| PMC8981973 | `d 1506, 746 cm−1 are chara` | non |
| PMC8981973 | `e to 1647 m2 g−1 of UiO-66` | oui |
| PMC8981973 | `han 0.05 mol L−1.8,17,25–2` | non |
| PMC8981973 | `ion (0.2 mol L−1). Despite` | non |
| PMC8981973 | `ion (0.2 mol L−1, limit of` | oui |
| PMC8981973 | `ng) and 480 cm−1 (vibratio` | non |
| PMC8981973 | `or (30.3 kg kg−1), while t` | non |
| PMC8981973 | `r (108.3 kg kg−1). Such a ` | non |
| PMC8981973 | `rate of 0.2° s−1 from 3° t` | non |
| PMC8981973 | `t 3103–2546 cm−1 are due t` | non |
| PMC8981973 | `t 3103–2546 cm−1. In addit` | non |
| PMC8981973 | `t about 480 cm−1 were othe` | oui |
| PMC8981973 | `with 0.2 mol L−1 ZrCl4 was` | non |
| PMC9000489 | ` a 400–4000 cm−1 spectral ` | non |
| PMC9000489 | `84 and 3006 cm−1 were attr` | oui |
| PMC9000489 | `aks at 1556 cm−1 and 1405 ` | non |
| PMC9000489 | `eak at 1194 cm−1 was found` | non |
| PMC9000489 | `eak at 1650 cm−1 was a res` | non |
| PMC9000489 | `−1 and 1405 cm−1 indicated` | non |
| PMC9025656 | ` 493 to 430 cm−1, inferrin` |  |
| PMC9025656 | ` 575 to 526 cm−1, and from` |  |
| PMC9025656 | ` 970 to 934 cm−1, from 575` |  |
| PMC9025656 | ` about 1500 cm−1. The spec` |  |
| PMC9025656 | ` and 712.66 cm−1, respecti` |  |
| PMC9025656 | ` of 1448.15 cm−1, 860.60 c` |  |
| PMC9025656 | ` of 1448.15 cm−1. Aragonit` |  |
| PMC9025656 | `100 to 1027 cm−1, from 970` |  |
| PMC9025656 | `100 to 1155 cm−1, which is` |  |
| PMC9025656 | `ated at 724 cm−1 and 634 c` |  |
| PMC9025656 | `between 400 cm−1 and about` |  |
| PMC9025656 | `m−1 and 634 cm−1 for HA. I` |  |
| PMC9025656 | `m−1, 860.60 cm−1, and 712.` |  |
| PMC9025656 | `of 400–4000 cm−1 [].2.5.2.` |  |
| PMC9026548 | `0, and 1382 cm−1 belong to` | non |
| PMC9026548 | `655 and 452 cm−1 are assig` | non |
| PMC9026548 | `and at 1358 cm−1 for stret` | non |
| PMC9026548 | `ved at 1790 cm−1 and 1722 ` | non |
| PMC9026548 | `−1 and 1722 cm−1 for asymm` | non |
| PMC9034142 | ` and Cnor = 10−4 M is the ` | non |
| PMC9034142 | ` of RhB was 10−11 M. The hi` | oui |
| PMC9034142 | ` shift 1650 cm−1 that was ` | non |
| PMC9034142 | ` value (5 × 10−9 M) obtain` | non |
| PMC9034142 | `) 29 000 g mol−1) were all` | oui |
| PMC9034142 | `00 and 1650 cm−1, which ar` | non |
| PMC9034142 | `07 and 1528 cm−1 should be` | non |
| PMC9034142 | `28 and 1650 cm−1, which ca` | non |
| PMC9034142 | `41 and 2959 cm−1, respecti` | oui |
| PMC9034142 | `B solution (10−5 M) adsorb` | non |
| PMC9034142 | `and at 1650 cm−1 was calcu` | non |
| PMC9034142 | `and at 3420 cm−1 to 2959 c` | non |
| PMC9034142 | `around 1650 cm−1 was the m` | non |
| PMC9034142 | `at the 1650 cm−1 peak from` | oui |
| PMC9034142 | `ations from 10−5 to 10−11 ` | oui |
| PMC9034142 | `centration (10−11 to 10−5 M` | oui |
| PMC9034142 | `de range of 10−11 to 10−5 M` | non |
| PMC9034142 | `eak of 1650 cm−1 from diff` | oui |
| PMC9034142 | `f peak 1650 cm−1 and logar` | non |
| PMC9034142 | `h as low as 10−11 M with EF` | non |
| PMC9034142 | `hB. For the 10−5 M RhB sol` | oui |
| PMC9034142 | `he range of 10−11 to 10−5 M` | non |
| PMC9034142 | `ift of 1650 cm−1 was chose` | non |
| PMC9034142 | `ion down to 10−11 M, the fa` | oui |
| PMC9034142 | `ity at 1650 cm−1 and the x` | non |
| PMC9034142 | `m−1 to 2959 cm−1 due to th` | non |
| PMC9034142 | `n (10−11 to 10−5 M). Then ` | oui |
| PMC9034142 | `n limit was 10–12 M in the ` | non |
| PMC9034142 | `nds at 1652 cm−1 and 3420 ` | non |
| PMC9034142 | `ntration of 10−11 M. Charac` | non |
| PMC9034142 | `ntration of 10−11 M. Here, ` | non |
| PMC9034142 | `o as low as 10−11 M, much l` | non |
| PMC9034142 | `of 10−11 to 10−5 M. The co` | non |
| PMC9034142 | `of 10−11 to 10−5 M. The si` | non |
| PMC9034142 | `of 500–1800 cm−1. A solid-` | non |
| PMC9034142 | `of the 1650 cm−1 peak slig` | oui |
| PMC9034142 | `of the 1650 cm−1 peak, and` | oui |
| PMC9034142 | `ortions for 10−5 M RhB (Ta` | non |
| PMC9034142 | `rom 10−5 to 10−11 M have be` | oui |
| PMC9034142 | `rum of RhB (10−5 M) with p` | non |
| PMC9034142 | `strong 1650 cm−1 spectral ` | non |
| PMC9034142 | `tration was 10−11 M, and ca` | non |
| PMC9034142 | `−1 and 3420 cm−1 correspon` | non |
| PMC9034275 | ` of 0.20 L min−1. The samp` | non |
| PMC9034275 | ` were 502 m2 g−1 and 0.23 ` | oui |
| PMC9034275 | `and 0.23 cm3 g−1, respecti` | oui |
| PMC9034275 | `ate of 12° min−1 over a ra` | non |
| PMC9034275 | `e of 10 °C min−1, using a ` | oui |
| PMC9034275 | `imately 300 cm−1, attribut` | non |
| PMC9034275 | `imately 550 cm−1, attribut` | non |
| PMC9034275 | `tion of 0.2 cm−1, in which` | non |
| PMC9034275 | `udy was 25.8 Å−1 for zeoli` | non |
| PMC9036545 | ` (96 500 C mol−1), the tot` | non |
| PMC9036545 | ` of 640 mA h g−1 after 100` | oui |
| PMC9036545 | ` of 838 mA h g−1 after 120` | oui |
| PMC9036545 | `.314 J mol−1 K−1), absolut` | non |
| PMC9036545 | `.5 to 3.0 mV s−1. The b-va` | non |
| PMC9036545 | `.9 ± 0.1 mg cm−2. The spec` | non |
| PMC9036545 | `0, and 3335 cm−1, which ag` | oui |
| PMC9036545 | `1C is 375 mA g−1. The acti` | non |
| PMC9036545 | `4 (∼900 mA h g−1) is more ` | non |
| PMC9036545 | `61 and 1317 cm−1 correspon` | non |
| PMC9036545 | `a of 58.6 m2 g−1. This nan` | non |
| PMC9036545 | `and 171 mA h g−1 after 600` | oui |
| PMC9036545 | `and 211 mA h g−1 after 600` | oui |
| PMC9036545 | `and 838 mA h g−1 after 120` | oui |
| PMC9036545 | `and 838 mA h g−1 at 3, 5, ` | oui |
| PMC9036545 | `band at 540 cm−1 originate` | non |
| PMC9036545 | `eak at 1590 cm−1 is attrib` | non |
| PMC9036545 | `eak at 3385 cm−1 indicates` | oui |
| PMC9036545 | `m 105 Hz to 10−3 Hz at 25 ` | oui |
| PMC9036545 | `ode (1.54 × 10−4 m2) and t` | non |
| PMC9036545 | `peak at 805 cm−1 is relate` | non |
| PMC9036545 | `t (8.314 J mol−1 K−1), abs` | non |
| PMC9036545 | `ty (372 mA h g−1) and poor` | non |
| PMC9036545 | `ty (375 mA h g−1), and the` | non |
| PMC9036664 | ` 3 mL 10 mg mL−1 NCDs was ` | oui |
| PMC9036664 | ` to 450 μmol L−1. Both Ste` | non |
| PMC9036664 | `00 and 3300 cm−1 are –OH a` | non |
| PMC9036664 | `5 μL 90 μmol L−1 metal ion` | oui |
| PMC9036664 | `Ds is 10 mg mL−1. The exci` | non |
| PMC9036664 | `aks at 1380 cm−1 and 1331 ` | non |
| PMC9036664 | `aks at 1499 cm−1 are the f` | non |
| PMC9036664 | `aks at 1641 cm−1 are vibra` | non |
| PMC9036664 | `eak at 1037 cm−1 is relate` | oui |
| PMC9036664 | `eak at 2898 cm−1 is vibrat` | oui |
| PMC9036664 | `l ions (μmol L−1) were mea` | non |
| PMC9036664 | `re 0.101 L mol−1 and 0.361` | oui |
| PMC9036664 | `t 1450–1600 cm−1 correspon` | oui |
| PMC9036664 | `−1 and 1331 cm−1 are deriv` | non |
| PMC9036687 | ` mL of 10 mg L−1 MB soluti` | oui |
| PMC9036687 | ` to 13.65 m2 g−1.3.3Photoc` | non |
| PMC9036687 | `ned. 0.3 mol L−1 (NH4)2HPO` | oui |
| PMC9036687 | `om 0.08929 min−1 to 0.0463` | oui |
| PMC9036687 | `to 0.04637 min−1, indicati` | non |
| PMC9036896 | ` N–H (−3100 cm−1) and O–H ` | non |
| PMC9036896 | ` O–H (−3300 cm−1) of adsor` | non |
| PMC9036896 | ` was 0.3 mg mL−1). After b` | non |
| PMC9036896 | `1 × 10 3 L mol−1 at the te` | oui |
| PMC9036896 | `31 and 1032 cm−1 appeared,` | oui |
| PMC9036896 | `ated at 810 cm−1 belonging` | oui |
| PMC9036896 | `e 3000–3500 cm−1 region as` | non |
| PMC9036896 | `e of 10 °C min−1 and kept ` | oui |
| PMC9036896 | `f 1200–1650 cm−1 are also ` | non |
| PMC9036896 | `lution of 4 cm−1. The ultr` | non |
| PMC9037448 | ` current, m (g−1), ΔV (V) ` | non |
| PMC9037448 | ` from 97.5 F g−1 to 142.3 ` | oui |
| PMC9037448 | ` from 97.5 F g−1 to 142.3 ` | oui |
| PMC9037448 | `1 and 402.5 cm−1 correspon` | oui |
| PMC9037448 | `1 and 91.8 F g−1 is achiev` | oui |
| PMC9037448 | `1 to 142.3 F g−1 at a curr` | oui |
| PMC9037448 | `1 to 142.3 F g−1, and 87.1` | non |
| PMC9037448 | `1, and 5.0 A g−1, respecti` | oui |
| PMC9037448 | `1where Cs (F g−1) is the a` | non |
| PMC9037448 | `2.5 to 50 mV s−1 showed a ` | non |
| PMC9037448 | `8% at 100 mV s−1. Manufact` | non |
| PMC9037448 | `A g−1, 1.0 A g−1, 2.0 A g−` | oui |
| PMC9037448 | `A g−1, 1.0 A g−1, 2.0 A g−` | oui |
| PMC9037448 | `A g−1, 2.0 A g−1, 3.0 A g−` | oui |
| PMC9037448 | `A g−1, 2.0 A g−1, 3.0 A g−` | oui |
| PMC9037448 | `A g−1, 3.0 A g−1 and 5.0 A` | non |
| PMC9037448 | `A g−1, 3.0 A g−1, and 5.0 ` | oui |
| PMC9037448 | `e of 0.008 e Å−3 is shown ` | non |
| PMC9037448 | `e of 170.2 F g−1, 142.2 F ` | oui |
| PMC9037448 | `eaks 375.84 cm−1 with the ` | oui |
| PMC9037448 | `g−1, 109.3 F g−1 and 91.8 ` | oui |
| PMC9037448 | `g−1, 121.1 F g−1, 109.3 F ` | oui |
| PMC9037448 | `g−1, 142.2 F g−1, 121.1 F ` | oui |
| PMC9037448 | `ies of 0.5 A g−1, 1.0 A g−` | oui |
| PMC9037448 | `ity of 0.5 A g−1, 1.0 A g−` | oui |
| PMC9037448 | `ity of 1.0 A g−1, and 87.1` | oui |
| PMC9037448 | `ity of 1.0 A g−1, and the ` | oui |
| PMC9037448 | `nce of 310 F g−1 and a rem` | non |
| PMC9037448 | `nce of 382 F g−1 at a curr` | non |
| PMC9037448 | `near 375.84 cm−1 and 402.5` | oui |
| PMC9037448 | `nsity of 1 A g−1. The symm` | non |
| PMC9037448 | `of 16.4 W h kg−1 and a ret` | non |
| PMC9037448 | `of 81.4 W h kg−1 in 1 M Na` | non |
| PMC9037448 | `te of 2.5 mV s−1 is descri` | non |
| PMC9037448 | `than 0.01 eV Å−1.In this w` | non |
| PMC9037448 | `ycles (1.0 A g−1). The gap` | non |
| PMC9037448 | `yte is 1 mol L−1 Na2SO3 so` | oui |
| PMC9037448 | `−1 and 5.0 A g−1 is achiev` | non |
| PMC9038048 | ` (30–270 μg mL−1). The con` | non |
| PMC9038048 | ` and 100 μL mL−1 of AuNP i` | non |
| PMC9038048 | ` and 270 μg mL−1. Control ` | non |
| PMC9038048 | ` and 5.0 μL mL−1) in blood` | non |
| PMC9038048 | ` –C–H (2922 cm−1), –C <sv` | non |
| PMC9038048 | ` –C–H (2928 cm−1), –CO (16` | oui |
| PMC9038048 | ` –O–H (3411 cm−1), –C–H (2` | oui |
| PMC9038048 | ` –O–H (3452 cm−1), –C–H (2` | non |
| PMC9038048 | `, –CO (1660 cm−1) function` | oui |
| PMC9038048 | `0 = 2.33 μg mL−1) is more ` | oui |
| PMC9038048 | `5 to 5.0 μL mL−1) of AuNPs` | non |
| PMC9038048 | `50 = 1.9 μg mL−1). Therefo` | non |
| PMC9038048 | `L of 105 μg mL−1 solution ` | oui |
| PMC9038048 | `act (105 μg mL−1 in 2% DMS` | oui |
| PMC9038048 | `alue (60 μg mL−1) than our` | non |
| PMC9038048 | `and 0.50 μL mL−1) of AuNP ` | non |
| PMC9038048 | `ations (1 × 10−3, 2 × 10−3` | non |
| PMC9038048 | `ations (1 × 10−3, 2 × 10−3` | non |
| PMC9038048 | `d to∼10 CFU mL−1 (correspo` | non |
| PMC9038048 | `e blue (5 × 10−5 M) degrad` | non |
| PMC9038048 | `g 10–100 μg mL−1 ascorbic ` | non |
| PMC9038048 | `g> O (1630 cm−1) function` | non |
| PMC9038048 | `ion (328 μg mL−1 with resp` | oui |
| PMC9038048 | `ion (394 μg mL−1 concentra` | oui |
| PMC9038048 | `n is 328 μg mL−1 with resp` | oui |
| PMC9038048 | `nd 50.00 μg mL−1 showed 44` | non |
| PMC9038048 | `nd 50.00 μg mL−1, respecti` | non |
| PMC9038048 | `ngth 394 μg mL−1 HAuCl4·3H` | oui |
| PMC9038048 | `ons (328 μg mL−1 for both)` | non |
| PMC9038048 | `riefly, 3 × 10−2 M (1%) me` | non |
| PMC9038048 | `utions (3 × 10−2 M or 1%) ` | non |
| PMC9038048 | `× 10−3, 2 × 10−3, 3 × 10−3` | non |
| PMC9038048 | `× 10−3, 2 × 10−3, 3 × 10−3` | non |
| PMC9038048 | `× 10−3, 3 × 10−3, 4 × 10−3` | non |
| PMC9038048 | `× 10−3, 3 × 10−3, 4 × 10−3` | non |
| PMC9038048 | `× 10−3, 4 × 10−3, 5 × 10−3` | non |
| PMC9038048 | `× 10−3, 4 × 10−3, 5 × 10−3` | non |
| PMC9038048 | `× 10−3, 5 × 10−3 M) of gol` | non |
| PMC9038048 | `× 10−3, 5 × 10−3 M) of gol` | non |
| PMC9041118 | ` dependence T1−1(T−1) for ` | non |
| PMC9041118 | ` maximum in T1−1(T−1) occu` | oui |
| PMC9041118 | `(3 × 10−4 S cm−1 at 25 °C)` | non |
| PMC9041118 | `100 to 1100 cm−1. All samp` | non |
| PMC9041118 | `and 0.50 mS cm−1. For the ` | non |
| PMC9041118 | `e Li nuclei (τ−1 ≈ ωL). Fo` | non |
| PMC9041118 | `endence T1−1(T−1) for all ` | non |
| PMC9041118 | `etic field, τ0−1 is a pre-` | non |
| PMC9041118 | `imum in T1−1(T−1) occurs a` | oui |
| PMC9041118 | `n comparing T1−1 measureme` | non |
| PMC9041118 | `nt with the T1−1 NMR resul` | non |
| PMC9041118 | `th Qmax = 20 Å−1. Calculat` | non |
| PMC9041118 | `vities (3 × 10−4 S cm−1 at` | oui |
| PMC9041118 | `xation rate T1−1 can be de` | non |
| PMC9041118 | `xation rate T1−1. This hop` | non |
| PMC9042205 | ` 265.161 cm3 g−1, and pore` |  |
| PMC9042205 | ` NaCl, 1.0 g L−1 of NH4Cl,` |  |
| PMC9042205 | ` and 0.011 g L−1 of CaCl2.` |  |
| PMC9042205 | `0.020407 cm3 g−1, and 14.8` |  |
| PMC9042205 | `0.020407 cm3 g−1, and pore` |  |
| PMC9042205 | `02 and 1456 cm−1 for O–H a` |  |
| PMC9042205 | `02, and 808 cm−1 for the m` |  |
| PMC9042205 | `24 and 2855 cm−1 were assi` |  |
| PMC9042205 | `2HPO4, 3.0 g L−1 of KH2PO4` |  |
| PMC9042205 | `4Cl, 0.493 g L−1 of MgSO4·` |  |
| PMC9042205 | `5, and 1120 cm−1 were obse` |  |
| PMC9042205 | `61 and 2343 cm−1 appeared ` |  |
| PMC9042205 | `8, 966, 960 cm−1 represent` |  |
| PMC9042205 | `: 780–840 m2 g−1, pore vol` |  |
| PMC9042205 | `H2PO4, 0.5 g L−1 of NaCl, ` |  |
| PMC9042205 | `a: 8.2616 m3 g−1; pore vol` |  |
| PMC9042205 | `around 3445 cm−1 for both ` |  |
| PMC9042205 | `band at 870 cm−1 represent` |  |
| PMC9042205 | `be 8.2616 m3 g−1, 0.020407` |  |
| PMC9042205 | `cm−1 to 810 cm−1 were foun` |  |
| PMC9042205 | `e of 10 °C min−1 under a n` |  |
| PMC9042205 | `eaks at 450 cm−1 to 810 cm` |  |
| PMC9042205 | `f 1635–1558 cm−1 were assi` |  |
| PMC9042205 | `is 2500 nm min−1 with accu` |  |
| PMC9042205 | `nd 7.9856 m3 g−1 consecuti` |  |
| PMC9042205 | `nd at ∼1635 cm−1 was obser` |  |
| PMC9042205 | `of 4000–400 cm−1 (Fig. 1c)` |  |
| PMC9042205 | `of 4000–400 cm−1.2.5.3Elem` |  |
| PMC9042205 | `peak at 808 cm−1 was obser` |  |
| PMC9042205 | `sity in CFU mL−1 at 600 nm` |  |
| PMC9042205 | `tion: 6.78 g L−1 of Na2HPO` |  |
| PMC9043336 | ` GO at 1224 cm−1. This pro` | non |
| PMC9043336 | ` X and Y (mg g−1), respect` | non |
| PMC9043336 | ` scale of μg L−1.9,10 Ther` | non |
| PMC9043336 | `.314 J mol−1 K−1). The ΔH ` | non |
| PMC9043336 | `0.5 to 1.5 g L−1, which ca` | non |
| PMC9043336 | `30 and 3310 cm−1 correspon` | oui |
| PMC9043336 | `4, and 1560 cm−1 represent` | non |
| PMC9043336 | `4, and 3446 cm−1 which are` | non |
| PMC9043336 | `400 to 4000 cm−1.The speci` | non |
| PMC9043336 | `732 to 1710 cm−1 in the GO` | non |
| PMC9043336 | `= 318.13 g mol−1), KMnO4 (` | oui |
| PMC9043336 | `age of 1.5 g L−1 which is ` | non |
| PMC9043336 | `age of 1.5 g L−1. At highe` | non |
| PMC9043336 | `ally 2630 m2 g−1), which e` | non |
| PMC9043336 | `capacity (mg g−1) and KL i` | non |
| PMC9043336 | `capacity (mg g−1) at time ` | non |
| PMC9043336 | `clofenac (mg L−1), qe is t` | non |
| PMC9043336 | `clofenac (mg L−1), respect` | non |
| PMC9043336 | `e of 10 °C min−1 under the` | oui |
| PMC9043336 | `eak at 1612 cm−1 represent` | oui |
| PMC9043336 | `f GO (10 mg mL−1). A prede` | non |
| PMC9043336 | `ged at 1080 cm−1 which is ` | non |
| PMC9043336 | `ged at 1640 cm−1 in the GO` | oui |
| PMC9043336 | `ged at 1681 cm−1 in the AG` | non |
| PMC9043336 | `hydrogel (mg g−1), qmax is` | non |
| PMC9043336 | `ion of 1.5 g L−1 and 100 p` | non |
| PMC9043336 | `n energy (L mg−1). Further` | non |
| PMC9043336 | `nd 129.26 mg g−1 for GO2–C` | non |
| PMC9043336 | `o be 7.07 m2 g−1 based on ` | oui |
| PMC9043336 | `s than 1.5 g L−1, the remo` | non |
| PMC9043336 | `t (8.314 J mol−1 K−1). The` | non |
| PMC9043336 | `tion (50 mg mL−1) in a gla` | oui |
| PMC9043841 | ` (J = 10 mA cm−2) for Ni2F` | oui |
| PMC9043841 | ` (j = 10 mA cm−2) and a qu` | oui |
| PMC9043841 | `10 to 150 mV s−1, the oxid` | oui |
| PMC9043841 | `4000 to 400 cm−1 at room t` | non |
| PMC9043841 | `DHs (2.4 mA cm−2) at the o` | oui |
| PMC9043841 | `DHs (3.3 mA cm−2) and Ni1F` | oui |
| PMC9043841 | `DHs (4.4 mA cm−2), Ni9Fe1-` | oui |
| PMC9043841 | `DHs (5.6 mA cm−2) is rough` | oui |
| PMC9043841 | `be 950.4 μF cm−2 and 729.7` | oui |
| PMC9043841 | `et to 1.0 × 10−4 eV.Result` | non |
| PMC9043841 | `m 1 to 10 mV s−1 in a non-` | oui |
| PMC9043841 | `nd 729.7 μF cm−2, larger t` | oui |
| PMC9043841 | `ng 0.285 mg cm−2). Linear ` | non |
| PMC9043841 | `of 349.1 mA cm−2 at a pote` | oui |
| PMC9043841 | `of 349.1 mA cm−2 at a pote` | oui |
| PMC9043841 | `rate of 5 mV s−1. Electroc` | non |
| PMC9043841 | `reach 10 mA cm−2 and large` | oui |
| PMC9043841 | `s (542.8 μF cm−2) and Ni9F` | oui |
| PMC9043841 | `s (703.1 μF cm−2), which i` | non |
| PMC9043841 | `than 0.05 eV Å−1, and the ` | non |
| PMC9043841 | `to 349.1 mA cm−2 at 1.8 V ` | oui |
| PMC9043841 | `ty of 20 mA cm−2, which is` | non |
| PMC9048217 | `e of 0.049 min−1, which is` | non |
| PMC9048217 | `e of 0.236 min−1. Furtherm` | non |
| PMC9048217 | `pp = 0.011 min−1), Ag/AgCl` | non |
| PMC9048217 | `pp = 0.021 min−1), Ag/AgCl` | non |
| PMC9048217 | `pp = 0.030 min−1) and Ag/A` | non |
| PMC9048217 | `pp = 0.032 min−1), respect` | oui |
| PMC9048980 | ` and 8.1 mg mL−1 inhibit E` |  |
| PMC9048980 | `.5 and 7 mg mL−1 inhibit S` |  |
| PMC9048980 | `.5 and 8 mg mL−1 inhibit S` |  |
| PMC9048980 | `1 and 16 mg mL−1 inhibit E` |  |
| PMC9048980 | `285 and 335 cm−1, which is` |  |
| PMC9048980 | `487 and 607 cm−1 appeared ` |  |
| PMC9048980 | `55 and 1382 cm−1 disappear` |  |
| PMC9048980 | `55 and 1382 cm−1 in the sp` |  |
| PMC9048980 | `75 and 1052 cm−1 indicate ` |  |
| PMC9048980 | `802 and 459 cm−1. The stro` |  |
| PMC9048980 | `804 and 972 cm−1 appeared ` |  |
| PMC9048980 | `804 and 972 cm−1. The band` |  |
| PMC9048980 | `88 and 1643 cm−1, attribut` |  |
| PMC9048980 | `and at 1059 cm−1 of SBA/Zn` |  |
| PMC9048980 | `at q = 1.64 nm−1, attribut` |  |
| PMC9048980 | `at q = 1.87 nm−1 due to (1` |  |
| PMC9048980 | `at q = 2.06 nm−1 attributi` |  |
| PMC9048980 | `cuum of 2 × 10−7 Pa, Al Kα` |  |
| PMC9048980 | `d 0.6075 mg mL−1 inhibit S` |  |
| PMC9048980 | `e of 10 °C min−1 under the` |  |
| PMC9048980 | `e of 50 mL min−1.2.3.Prepa` |  |
| PMC9048980 | `ed to 163 m2 g−1, and the ` |  |
| PMC9048980 | `eed was 2° min−1 (angular ` |  |
| PMC9048980 | `iefly, 1 mg mL−1 suspensio` |  |
| PMC9048980 | `ion of 1 mg mL−1 were stir` |  |
| PMC9048980 | `li (105 CFU mL−1) were tra` |  |
| PMC9048980 | `nd 0.049 mg mL−1 for each ` |  |
| PMC9048980 | `nd 1.215 mg mL−1 for SBA/C` |  |
| PMC9048980 | `nd >2.48 mg mL−1 inhibit S` |  |
| PMC9048980 | `nd >2.48 mg mL−1, and 0.31` |  |
| PMC9048980 | `of 4000–400 cm−1 following` |  |
| PMC9048980 | `peak at 968 cm−1 generated` |  |
| PMC9048980 | `tively, cfu mL−1.2.7.Deter` |  |
| PMC9048980 | `to q = 2.01 nm−1. These th` |  |
| PMC9048980 | `us (105 CFU mL−1) and E. c` |  |
| PMC9050136 | ` 2924, 3061 cm−1.2.6.Batch` | non |
| PMC9050136 | ` 7 (134.4 mg g−1), while, ` | non |
| PMC9050136 | ` and 1162 m2 g−1, respecti` | oui |
| PMC9050136 | ` in g (mg min)−1 are respe` | non |
| PMC9050136 | ` peak ∼1390 cm−1 is due to` | oui |
| PMC9050136 | ` time qt (mg g−1) is calcu` | non |
| PMC9050136 | `00 and 1145 cm−1 were attr` | oui |
| PMC9050136 | `1 and 175 mg g−1, respecti` | non |
| PMC9050136 | `1where k1 (min−1) and k2 i` | non |
| PMC9050136 | `760 and 752 cm−1 were ascr` | oui |
| PMC9050136 | `OF and 1665 cm−1 of (1 : 1` | oui |
| PMC9050136 | `ak at ∼3450 cm−1 assigned ` | non |
| PMC9050136 | `and C0 in mg L−1 is the in` | non |
| PMC9050136 | `and KL in L mg−1 is the La` | non |
| PMC9050136 | `and qt in mg g−1 are respe` | non |
| PMC9050136 | `ared at 825 cm−1. These re` | oui |
| PMC9050136 | `capacity (mg g−1).4.Conclu` | non |
| PMC9050136 | `cule; qe (mg g−1) is the a` | non |
| PMC9050136 | `e-MOF, 1646 cm−1 of (0.6 :` | oui |
| PMC9050136 | `each 95.6 mg g−1 at pH = 5` | oui |
| PMC9050136 | `er was 10 μg L−1. Conseque` | non |
| PMC9050136 | `ere KL in L mg−1 is the La` | non |
| PMC9050136 | `from 82.5 mg g−1 at pH = 3` | oui |
| PMC9050136 | `ge 400–4000 cm−1 for a sam` | non |
| PMC9050136 | `m (50–200 mg L−1) at 25 °C` | oui |
| PMC9050136 | `n of (100 mg L−1) and appr` | oui |
| PMC9050136 | `nt; qmax (mg g−1) indicate` | non |
| PMC9050136 | `ntration (mg L−1) of the m` | non |
| PMC9050136 | `om (108.4 mg g−1) at pH = ` | oui |
| PMC9050136 | `rom (44.3 mg g−1) at pH 4 ` | oui |
| PMC9050136 | `t 0.005 mL min−1, which is` | oui |
| PMC9050136 | `um (140.6 mg g−1) at pH 5,` | oui |
| PMC9050136 | `up to 150 mg L−1 due to pl` | non |
| PMC9050136 | `up to 150 mg L−1 then almo` | oui |
| PMC9050136 | `ved at 1598 cm−1 for Mg-MO` | oui |
| PMC9050136 | `where Ce (mg L−1) is the e` | non |
| PMC9054292 | ` only one mg L−1. Fig. S4†` | non |
| PMC9054292 | ` that one mg L−1 of CDs co` | oui |
| PMC9054292 | `5 and 1.5 mg L−1). The abs` | non |
| PMC9054292 | `= 1163.4 L mol−1 and pH = ` | oui |
| PMC9054292 | `aks at 1700 cm−1 and 1650 ` | oui |
| PMC9054292 | `and at 2900 cm−1 appeared ` | non |
| PMC9054292 | `e in 0.1 mol L−1 H2SO4 as ` | oui |
| PMC9054292 | `eak at 1060 cm−1 originate` | non |
| PMC9054292 | `eak at 1400 cm−1 correspon` | non |
| PMC9054292 | `eak at 1560 cm−1 correspon` | oui |
| PMC9054292 | `eak at 3300 cm−1 correspon` | oui |
| PMC9054292 | `em at one mg L−1 CDs for a` | non |
| PMC9054292 | `f 0.5–1.5 mg L−1. In the p` | non |
| PMC9054292 | `f 1000–1400 cm−1 can be at` | oui |
| PMC9054292 | `n a 0.05 mol L−1 phosphate` | oui |
| PMC9054292 | `of CDs (1 mg L−1) in a buf` | oui |
| PMC9054292 | `ract (500 mg L−1) was plac` | oui |
| PMC9054292 | `−1 and 1650 cm−1 signifies` | oui |
| PMC9054543 | ` (334.4 kJ mol−1) is lower` | non |
| PMC9054543 | ` (341.1 kJ mol−1), therefo` | non |
| PMC9054543 | ` (d = 910 kg m−3) and HDPE` | oui |
| PMC9054543 | ` (d = 951 kg m−3) were cyl` | oui |
| PMC9054543 | `C at 10 °C min−1, and hold` | non |
| PMC9054543 | `C at 15 °C min−1, and hold` | non |
| PMC9054543 | `YTGP (412 mL g−1) and SLO ` | non |
| PMC9054543 | `YTGP (468 mL g−1) and the ` | non |
| PMC9054543 | `ands at 796 cm−1, which is` | oui |
| PMC9054543 | `ate: 40 mL min−1). The pla` | non |
| PMC9054543 | `cm−1 to 400 cm−1 using the` | non |
| PMC9054543 | `e from 4000 cm−1 to 400 cm` | non |
| PMC9054543 | `e of 10 °C min−1 in He flo` | oui |
| PMC9054543 | `ely:1TGP (mL g−1) = VTGP/M` | non |
| PMC9054543 | `g mode, 546 cm−1 resulted ` | oui |
| PMC9054543 | `olid = 10 mL g−1) at 80 °C` | oui |
| PMC9054543 | `rate of 8° min−1. The surf` | non |
| PMC9054543 | `re, and 450 cm−1 caused fr` | oui |
| PMC9054543 | `rea (>370 m2 g−1) and an a` | non |
| PMC9054543 | `s with 1 mol L−1 NH4Cl sol` | oui |
| PMC9054805 | `455 to 3442 cm−1, which ca` | non |
| PMC9054805 | `800 and 461 cm−1 reflectin` | non |
| PMC9054805 | `ET = 1255 m2 g−1), associa` | non |
| PMC9054805 | `ET = 1390 m2 g−1) is quite` | oui |
| PMC9054805 | `ET = 1768 m2 g−1) because ` | oui |
| PMC9054805 | `and G (1574 cm−1) bands of` | oui |
| PMC9054805 | `and at 1098 cm−1 attribute` | non |
| PMC9054805 | `and at 1544 cm−1 is assign` | non |
| PMC9054805 | `and at 2667 cm−1 indicates` | non |
| PMC9054805 | `and at 2916 cm−1. The asym` | non |
| PMC9054805 | `around 1615 cm−1 correspon` | non |
| PMC9054805 | `der at 1160 cm−1, especial` | non |
| PMC9054805 | `e 1013–1026 cm−1 range is ` | non |
| PMC9054805 | `eak at 1554 cm−1 is attrib` | non |
| PMC9054805 | `eak at 2346 cm−128. The pe` | non |
| PMC9054805 | `eak at 3446 cm−1 represent` | oui |
| PMC9054805 | `eak at 3446 cm−1, which ca` | non |
| PMC9054805 | `ion of 2349 cm−1, which co` | non |
| PMC9054805 | `man D (1347 cm−1) and G (1` | oui |
| PMC9054805 | `n 3742–3867 cm−1 suggests ` | non |
| PMC9054805 | `nd 400–1750 cm−1 correspon` | non |
| PMC9054805 | `peak at 683 cm−1 correspon` | non |
| PMC9054805 | `t 1013–1026 cm−1 shrank si` | non |
| PMC9054805 | `te of 5 °C min−1. In Fig. ` | non |
| PMC9054805 | `ved at 1450 cm−1, due to t` | non |
| PMC9054805 | `ved at 1633 cm−1 but sharp` | non |
| PMC9056161 | `.1 MPa and 1 h−1, respecti` | oui |
| PMC9056161 | `47 and 1222 cm−1 are assig` | non |
| PMC9056161 | `47 and 1222 cm−1 could be ` | oui |
| PMC9056161 | `96 and 1099 cm−1 are assig` | non |
| PMC9056161 | `99 and 1222 cm−1, which ar` | oui |
| PMC9056161 | `C at 10 °C min−1 for 2 h t` | non |
| PMC9056161 | `C at 10 °C min−1, and the ` | oui |
| PMC9056161 | `C at 10 °C min−1.2.4.Catal` | non |
| PMC9056161 | `Pa, WHSV = 1 h−1. Fig. 6 s` | non |
| PMC9056161 | `cm−1 is ∼20 cm−1 higher (b` | oui |
| PMC9056161 | `e with 1 mol L−1 of NH4NO3` | oui |
| PMC9056161 | `er near 450 cm−1 is ∼20 cm` | oui |
| PMC9056161 | `lution of 4 cm−1 using the` | non |
| PMC9056161 | `w of 40 ml min−1, the appr` | non |
| PMC9057400 | ` (125–200 mg L−1) onto the` | non |
| PMC9057400 | `, and 100 mg L−1), and MB ` | oui |
| PMC9057400 | `, and 200 mg L−1) of MB (F` | non |
| PMC9057400 | `, and 200 mg L−1).70 The v` | non |
| PMC9057400 | `00 and 75 mg L−1 were sele` | oui |
| PMC9057400 | `54 and 1394 cm−1 correspon` | oui |
| PMC9057400 | `91, and 960 cm−1 were attr` | oui |
| PMC9057400 | `912 and 775 cm−1 are linke` | oui |
| PMC9057400 | `acity qe (mg g−1) were cal` | non |
| PMC9057400 | `and 13.7 emu g−1, respecti` | oui |
| PMC9057400 | `d RhB (50 mg L−1) dyes fro` | non |
| PMC9057400 | `d) and 50 mg L−1 RhB solut` | non |
| PMC9057400 | `e and C0 (mg L−1) are the ` | non |
| PMC9057400 | `f MB (100 mg L−1) and RhB ` | non |
| PMC9057400 | `in 25–200 mg L−1. The solu` | non |
| PMC9057400 | `mL of 100 mg L−1 MB soluti` | non |
| PMC9057400 | `m−1 and 583 cm−1 are relat` | non |
| PMC9057400 | `nd 153.84 mg g−1, respecti` | non |
| PMC9057400 | `nd 799.56 m2 g−1, respecti` | oui |
| PMC9057400 | `nds at 3410 cm−1 and 583 c` | non |
| PMC9057400 | `on of 100 mg L−1 and stirr` | non |
| PMC9057400 | `reas (<10 m2 g−1), which h` | non |
| PMC9057918 | ` around 300 cm−1, which is` | non |
| PMC9057918 | `240 and 280 cm−1 peaks, co` | non |
| PMC9057918 | `e of 10 °C min−1; in the m` | oui |
| PMC9057918 | `und 380–400 cm−1, which ca` | non |
| PMC9059895 | ` and 0.168 min−1, respecti` | oui |
| PMC9059895 | ` and 0.245 min−1, respecti` | oui |
| PMC9059895 | `nd RB (30 mg L−1, 15 mL).R` | non |
| PMC9059895 | `n−1, 0.039 min−1, 0.058 mi` | oui |
| PMC9059895 | `n−1, 0.058 min−1, 0.067 mi` | oui |
| PMC9059895 | `n−1, 0.058 min−1, 0.076 mi` | oui |
| PMC9059895 | `n−1, 0.067 min−1, 0.076 mi` | oui |
| PMC9059895 | `n−1, 0.076 min−1, 0.086 mi` | oui |
| PMC9059895 | `n−1, 0.076 min−1, 0.148 mi` | oui |
| PMC9059895 | `n−1, 0.086 min−1 and 0.168` | oui |
| PMC9059895 | `n−1, 0.148 min−1 and 0.245` | oui |
| PMC9059895 | `o be 0.008 min−1, 0.039 mi` | oui |
| PMC9059895 | `o be 0.027 min−1, 0.058 mi` | oui |
| PMC9059895 | `of MB (30 mg L−1, 15 mL) a` | non |
| PMC9059895 | `rate of 0.1° s−1 All XRD m` | non |
| PMC9059895 | `ution (30 mg L−1, 30 mL), ` | oui |
| PMC9060541 | `+ 3.66045 × 10−4 × Te × WP` | non |
| PMC9060541 | `+ 4.01792 × 10−4 × Ti × Tc` | non |
| PMC9060541 | `10 and 1650 cm−1 clearly r` | oui |
| PMC9060541 | `6 + 1.793 × 10−3 × A − 0.0` | non |
| PMC9060541 | `619 and 659 cm−1 due to Cd` | oui |
| PMC9060541 | `91 and 1630 cm−1 indicate ` | oui |
| PMC9060541 | `B − 8.654 × 10−3 × C + 0.0` | non |
| PMC9060541 | `D + 4.393 × 10−3 × A × D +` | non |
| PMC9060541 | `D + 9.040 × 10−3 × B × C −` | non |
| PMC9060541 | `and at 1627 cm−1.30 For Cd` | non |
| PMC9060541 | `ate of 109 K s−1.20 These ` | non |
| PMC9060541 | `eak at 1400 cm−1 can be re` | oui |
| PMC9060541 | `er 500–2500 cm−1. The refe` | non |
| PMC9060541 | `ion 400–600 cm−1 is due to` | oui |
| PMC9060541 | `ion 700–950 cm−1 is due to` | oui |
| PMC9060541 | `the 500–700 cm−1 region in` | oui |
| PMC9060541 | `− 1.21566 × 10−3 × WP2wher` | non |
| PMC9060541 | `− 3.24399 × 10−3 × Ti − 0.` | non |
| PMC9061421 | `.1 and 1 mg mL−1 were calc` | oui |
| PMC9061421 | `01 and 1 mg mL−1 of the N-` | non |
| PMC9061421 | `aks at 1715 cm−1 and 1635 ` | non |
| PMC9061421 | `elow 0.1 mg mL−1, the emis` | non |
| PMC9061421 | `f 2800–3480 cm−1 in the FT` | oui |
| PMC9061421 | `n of 1.0 mg mL−1. Then, th` | non |
| PMC9061421 | `nds at 1440 cm−1 and 1256 ` | non |
| PMC9061421 | `ore, 0.1 mg mL−1 was the o` | oui |
| PMC9061421 | `ted at 1 mg mL−1; this was` | non |
| PMC9061421 | `tion (0.1 g mL−1). After 4` | non |
| PMC9061421 | `under 0.1 mg L−1 (about 1.` | non |
| PMC9061421 | `−1 and 1256 cm−1 were assi` | non |
| PMC9061421 | `−1 and 1635 cm−1 indicated` | non |
| PMC9061730 | ` 11.3 kcal mol−1 more stab` | oui |
| PMC9061730 | ` criterion (10−8 a.u.) was` | non |
| PMC9061730 | `), and 1230 cm−1 (C–O stre` | oui |
| PMC9061730 | `40 and 1040 cm−1 correspon` | non |
| PMC9061730 | `asing 1.2 kJ g−1, 2.75 tim` | non |
| PMC9061730 | `e AP (1.9 kJ g−1). At 5% w` | non |
| PMC9061730 | `eak at 1640 cm−1 was attri` | non |
| PMC9061730 | `er (0.07 mg mL−1). As Fig.` | non |
| PMC9061730 | `ge 500–4000 cm−1. UV-visib` | non |
| PMC9061730 | `ls. At 1615 cm−1 appeared ` | non |
| PMC9061730 | `te of 5 °C min−1 under a n` | oui |
| PMC9063653 | `d 140.5 emu cm−3, respecti` | oui |
| PMC9063653 | `e 7.8 × 10−4 K−1, and simi` | oui |
| PMC9063653 | `form 0.1 mol L−1 Co3O4 pre` | oui |
| PMC9063653 | `to be 7.8 × 10−4 K−1, and ` | oui |
| PMC9063869 | ` and 0.1 mol L−1 of CaCl2·` | oui |
| PMC9063869 | ` and 0.1 mol L−1 of CaCl2·` | oui |
| PMC9063869 | ` and 0.1 mol L−1 of CaCl2·` | oui |
| PMC9063869 | ` and 0.4 mol L−1 disodium ` | oui |
| PMC9063869 | ` and 0.4 mol L−1 of Na2HPO` | oui |
| PMC9063869 | ` and 0.5 mol L−1) by ultra` | non |
| PMC9063869 | ` cm−1, 1032 cm−1, 962 cm−1` | oui |
| PMC9063869 | ` to 0.12 mol L−1, the leng` | oui |
| PMC9063869 | `%) (0.06 mol L−1, 0.12 mol` | oui |
| PMC9063869 | `.025–0.2 mg mL−1 by using ` | non |
| PMC9063869 | `.67, 0.4 mol L−1 of Na2HPO` | oui |
| PMC9063869 | `.67, 0.4 mol L−1 of Na2HPO` | oui |
| PMC9063869 | `1 to 0.4 mol L−1, the size` | oui |
| PMC9063869 | `1, 0.334 mol L−1, 0.668 mo` | oui |
| PMC9063869 | `1, 0.668 mol L−1 and 0.835` | oui |
| PMC9063869 | `2 cm−1, 603 cm−1, 564 cm−1` | oui |
| PMC9063869 | `2 cm−1, 962 cm−1, 603 cm−1` | oui |
| PMC9063869 | `3 cm−1, 564 cm−1 correspon` | oui |
| PMC9063869 | `4 is 0.4 mol L−1. There is` | non |
| PMC9063869 | `5%) (0.1 mol L−1, 0.2 mol ` | oui |
| PMC9063869 | `7) (0.06 mol L−1, 0.12 mol` | oui |
| PMC9063869 | `L−1, 0.2 mol L−1 and 0.4 m` | oui |
| PMC9063869 | `L−1, 0.2 mol L−1, 0.334 mo` | oui |
| PMC9063869 | `L−1, 0.2 mol L−1, 0.4 mol ` | oui |
| PMC9063869 | `L−1, 0.4 mol L−1 and 0.5 m` | oui |
| PMC9063869 | `ach 0.033 kg L−1 when the ` | non |
| PMC9063869 | `aks at 2925 cm−1 and 2856 ` | oui |
| PMC9063869 | `aks at 3443 cm−1 and 1638 ` | oui |
| PMC9063869 | `d 1446–1420 cm−1 correspon` | oui |
| PMC9063869 | `d near 1092 cm−1, 1032 cm−` | oui |
| PMC9063869 | `e is 10 °C min−1 when the ` | oui |
| PMC9063869 | `e is 10 °C min−1.Character` | non |
| PMC9063869 | `ed near 633 cm−1 and 3571 ` | oui |
| PMC9063869 | `elow 0.4 mol L−1. The obta` | non |
| PMC9063869 | `es, 0.06 mol L−1 of Na2HPO` | oui |
| PMC9063869 | `es, 0.06 mol L−1 of Na2HPO` | oui |
| PMC9063869 | `nd 0.835 mol L−1) was adde` | oui |
| PMC9063869 | `nd near 874 cm−1 and 1446–` | oui |
| PMC9063869 | `on 400–4000 cm−1.Scanning ` | non |
| PMC9063869 | `rom 0.12 mol L−1 to 0.4 mo` | oui |
| PMC9063869 | `s to 0.5 mol L−1, the nano` | oui |
| PMC9063869 | `s, 0.668 mol L−1 calcium c` | oui |
| PMC9063869 | `te is 7 °C min−1 when the ` | oui |
| PMC9063869 | `te is 7 °C min−1.In the se` | non |
| PMC9063869 | `te of 7 mL min−1, and main` | oui |
| PMC9063869 | `te of 7 mL min−1. In the t` | non |
| PMC9063869 | `°C, 0.06 mol L−1 of Na2HPO` | oui |
| PMC9063869 | `−1 and 1638 cm−1 indicate ` | oui |
| PMC9063869 | `−1 and 2856 cm−1 may be as` | oui |
| PMC9063869 | `−1 and 3571 cm−1. The peak` | oui |
| PMC9063869 | `−1, 0.12 mol L−1, 0.2 mol ` | oui |
| PMC9063869 | `−1, 0.12 mol L−1, 0.2 mol ` | oui |
| PMC9064236 | ` 70° at 2° min−1. X-rays w` |  |
| PMC9064236 | ` be 21.7 mA cm−2, with a S` |  |
| PMC9064236 | ` peak at 96 cm−1 allows th` |  |
| PMC9064236 | ` s (2000 rpm s−1) then seq` |  |
| PMC9064236 | `(Rsq = 10 Ω sq−1) using a ` |  |
| PMC9064236 | `epts, 4.3 W cm−2, 0.0006 m` |  |
| PMC9064236 | `ing from 20 cm−1.Results a` |  |
| PMC9064236 | `mple to 520 cm−1. The gas ` |  |
| PMC9064236 | `nge 150–250 cm−1 make it d` |  |
| PMC9064236 | `or 2.19 kJ mol−1 () above ` |  |
| PMC9064236 | `peak at 111 cm−1 is attrib` |  |
| PMC9064236 | `range (<120 cm−1), with in` |  |
| PMC9064236 | `sq = 0.16 Ω sq−1) were dep` |  |
| PMC9064236 | `t (>4 × 104 cm−1, at wavel` |  |
| PMC9064236 | `xceed 30 kW cm−2, which ex` |  |
| PMC9064236 | `y of ∼11 mA cm−2 could be ` |  |
| PMC9064236 | `ΔE 1.76 kJ mol−1 (Popov et` |  |
| PMC9064236 | `–5.7 × 1015 cm−3) in addit` |  |
| PMC9064545 | ` 660 to 750 cm−1 is integr` |  |
| PMC9064545 | `220 and 290 cm−1 coincide ` |  |
| PMC9064545 | `90 and 1320 cm−1 appear su` |  |
| PMC9064545 | `mp of 1 °C min−1 (Fig. 1).` |  |
| PMC9064545 | `m−1 to 1340 cm−1 and is co` |  |
| PMC9064545 | `onstant 40 N m−1 and a res` |  |
| PMC9064545 | `s from 1310 cm−1 to 1340 c` |  |
| PMC9065796 | `18 and 1139 cm−1 were attr` | non |
| PMC9065796 | `713 and 787 cm−1 were rela` | non |
| PMC9065796 | `LHSV) of 2.0 h−1. After st` | non |
| PMC9065796 | `ed to 728 m2 g−1, and the ` | oui |
| PMC9065796 | `nd 0.1228 ml g−1, respecti` | oui |
| PMC9065796 | `peak at 578 cm−1 was assig` | non |
| PMC9069485 | ` (96 500 C mol−1), C is th` |  |
| PMC9069485 | ` and 70 mA h g−1 respectiv` |  |
| PMC9069485 | ` from 100 mA g−1 to 2 A g−` |  |
| PMC9069485 | ` g−1 and 2 A g−1, the full` |  |
| PMC9069485 | ` of 124 mA h g−1 at a curr` |  |
| PMC9069485 | ` of 134 mA h g−1 (Fig. S7c` |  |
| PMC9069485 | ` of 134 mA h g−1, whereas ` |  |
| PMC9069485 | ` of 277 mA h g−1 after 200` |  |
| PMC9069485 | ` of 593 mA h g−1 has been ` |  |
| PMC9069485 | ` of 593 mA h g−1 is delive` |  |
| PMC9069485 | ` of 600 mA h g−1, more tha` |  |
| PMC9069485 | ` × 10−13 cm2 s−1) is three` |  |
| PMC9069485 | ` × 10−16 cm2 s−1). Therefo` |  |
| PMC9069485 | `.314 J mol−1 K−1), T is th` |  |
| PMC9069485 | `645–992 mA h g−1) and low ` |  |
| PMC9069485 | `A g−1 to 2 A g−1 to assess` |  |
| PMC9069485 | `SGP (3.64 × 10−13 cm2 s−1) ` |  |
| PMC9069485 | `and 118 mA h g−1, respecti` |  |
| PMC9069485 | `ation (1 mol L−1, in the e` |  |
| PMC9069485 | `de (372 mA h g−1) cannot m` |  |
| PMC9069485 | `ed to 100 mA g−1, the SGP ` |  |
| PMC9069485 | `ed to 100 mA g−1. Fig. 8d ` |  |
| PMC9069485 | `eed of 10° min−1. Raman sp` |  |
| PMC9069485 | `ial 126 mA h g−1 as soon a` |  |
| PMC9069485 | `ion (0.5 mol L−1), and hyd` |  |
| PMC9069485 | `ities of 1 A g−1 and 2 A g` |  |
| PMC9069485 | `nd 1006 mA h g−1, remarkab` |  |
| PMC9069485 | `nd) at 1341 cm−1, attribut` |  |
| PMC9069485 | `nd) at 1584 cm−1 correspon` |  |
| PMC9069485 | `nsity of 2 A g−1, the SGP ` |  |
| PMC9069485 | `ode (1.00 × 10−16 cm2 s−1).` |  |
| PMC9069485 | `only 78 mA h g−1 left. Onc` |  |
| PMC9069485 | `t (8.314 J mol−1 K−1), T i` |  |
| PMC9069485 | `te of 0.1 mV s−1. Fig. 5a ` |  |
| PMC9069485 | `te of 0.1 mV s−1. The elec` |  |
| PMC9069485 | `to a 0.8 mg mL−1 water sus` |  |
| PMC9069485 | `ty of 100 mA g−1 between 0` |  |
| PMC9069485 | `ty of 100 mA g−1 between 2` |  |
| PMC9069485 | `ty of 100 mA g−1, as well ` |  |
| PMC9069485 | `ty of 100 mA g−1. In addit` |  |
| PMC9073369 | ` (42.39 mV dec−1) since th` | oui |
| PMC9073369 | `f 42.39 mV dec−1. In addit` | non |
| PMC9073369 | `f 42.39 mV dec−1. More imp` | non |
| PMC9073369 | `mV at 10 mA cm−2 (Fig. S5a` | oui |
| PMC9073369 | `mV at 10 mA cm−2 and a sma` | oui |
| PMC9073369 | `nt of 10 mA cm−2 was used ` | oui |
| PMC9073369 | `rate of 2 mV s−1. In order` | non |
| PMC9073369 | `ty of 10 mA cm−2, and a sm` | non |
| PMC9077458 | `area (364 m2 g−1 and pore ` |  |
| PMC9077458 | `e of 10 °C min−1 and the T` |  |
| PMC9077458 | `early 300 m2 g−1) on ZSM-5` |  |
| PMC9077458 | `me (0.24 cm3 g−1) and exte` |  |
| PMC9077458 | `o 310–370 m2 g−1. They wer` |  |
| PMC9077458 | `rface (64 m2 g−1) and corr` |  |
| PMC9077458 | `ume 0.38 cm3 g−1), indicat` |  |
| PMC9078232 | ` (50–2000 mg L−1) of CV is` | non |
| PMC9078232 | ` and 1600 mg L−1. It perfo` | non |
| PMC9078232 | ` and 2000 mg L−1 and the d` | non |
| PMC9078232 | ` and at 808 cm−1 of g-C3N4` | non |
| PMC9078232 | ` and k2 (g (mg−1 min−1)) a` | non |
| PMC9078232 | `) and qt (mg g−1) are the ` | non |
| PMC9078232 | `1.25, 1.50 g L−1) of the C` | non |
| PMC9078232 | `2 (g (mg−1 min−1)) are the` | non |
| PMC9078232 | `200, 1600 mg L−1). The pse` | non |
| PMC9078232 | `4where k1 (min−1) and k2 (` | non |
| PMC9078232 | `58 and 1774 cm−1 correspon` | non |
| PMC9078232 | `HCL (0.1 mol L−1) and NaOH` | oui |
| PMC9078232 | `HCl (0.5 mol L−1) and deio` | oui |
| PMC9078232 | `V of 1600 mg L−1 were chos` | oui |
| PMC9078232 | `aOH (0.1 mol L−1). The kin` | non |
| PMC9078232 | `aks at 1070 cm−1 and 1774 ` | non |
| PMC9078232 | `e 1200–1700 cm−1 range and` | non |
| PMC9078232 | `e peak 1458 cm−1 correspon` | oui |
| PMC9078232 | `eak at 1319 cm−1 assigned ` | oui |
| PMC9078232 | `eak at 2112 cm−1 assigned ` | oui |
| PMC9078232 | `eak at 2112 cm−1 correspon` | oui |
| PMC9078232 | `f the CV (mg L−1) at initi` | non |
| PMC9078232 | `fted to 821 cm−1, the peak` | non |
| PMC9078232 | `fted to 858 cm−1, the peak` | non |
| PMC9078232 | `ime t qt (mg g−1) and remo` | non |
| PMC9078232 | `ions was 1 g L−1. The adso` | oui |
| PMC9078232 | `n is 1600 mg L−1, except t` | oui |
| PMC9078232 | `of 4500–400 cm−1, using KB` | oui |
| PMC9078232 | `on was 10 mg L−1, and dosa` | oui |
| PMC9078232 | `p of 1600 mg L−1 reached t` | non |
| PMC9078232 | `p to 1800 mg L−1. This mig` | non |
| PMC9078232 | `peak at 808 cm−1 presented` | non |
| PMC9078232 | `peak at 856 cm−1 presented` | non |
| PMC9078232 | `ps to 1.00 g L−1, the remo` | non |
| PMC9078232 | `rbent 1.00 g L−1 was the s` | oui |
| PMC9078232 | `te of 5 °C min−1 to obtain` | oui |
| PMC9078232 | `tion was 1 g L−1. For all ` | non |
| PMC9078232 | `to the 2107 cm−1 and the p` | oui |
| PMC9078232 | `ution (10 mg L−1), respect` | oui |
| PMC9078232 | `vely; qe (mg g−1) and qt (` | non |
| PMC9078232 | `−1 and 1774 cm−1 were disa` | non |
| PMC9078281 | ` 0 to 3.5 × 10−6 mol L−1 (` |  |
| PMC9078281 | ` 0 to 5.0 × 10−6 mol L−1) ` |  |
| PMC9078281 | ` and 100 mg mL−1 streptomy` |  |
| PMC9078281 | ` ion of 2 × 10−3 mol L−1. ` |  |
| PMC9078281 | ` mL, 0.1 mol L−1) and Mill` |  |
| PMC9078281 | ` mL, 0.1 mol L−1), MnCl2 s` |  |
| PMC9078281 | ` μL of 5 mg mL−1 MTT (3-(4` |  |
| PMC9078281 | `0 to 300 μg mL−1, and ther` |  |
| PMC9078281 | `0 to 300 μg mL−1. After th` |  |
| PMC9078281 | `0 × 10−6 mol L−1) were rec` |  |
| PMC9078281 | `0 × 10−6 mol L−1) were rec` |  |
| PMC9078281 | `2 × 10−3 mol L−1. The high` |  |
| PMC9078281 | `4 × 10−6 mol L−1 Hg2+ in d` |  |
| PMC9078281 | `4 × 10−8 mol L−1 by the 3δ` |  |
| PMC9078281 | `5 × 10−6 mol L−1 (Fig. 6d)` |  |
| PMC9078281 | `5 × 10−6 mol L−1) and 200 ` |  |
| PMC9078281 | `Ds (6.52 mg mL−1) solution` |  |
| PMC9078281 | `Hg2+ (4.0 × 10−6 mol L−1) ` |  |
| PMC9078281 | `QDs at 1449 cm−1 increases` |  |
| PMC9078281 | `aks at 1495 cm−1 and 1449 ` |  |
| PMC9078281 | `and at 1411 cm−1, which co` |  |
| PMC9078281 | `and at 1645 cm−1 and a lar` |  |
| PMC9078281 | `and at 1645 cm−1, which re` |  |
| PMC9078281 | `and at 3406 cm−1 correspon` |  |
| PMC9078281 | `ence of 4 × 10−6 mol L−1 H` |  |
| PMC9078281 | `g from 1500 cm−1 to 1750 c` |  |
| PMC9078281 | `ing at 1495 cm−1 in Mn(ii)` |  |
| PMC9078281 | `ion at 1078 cm−1 and NH3+ ` |  |
| PMC9078281 | `ions (0–5 × 10−6 mol L−1) ` |  |
| PMC9078281 | `m−1 and 830 cm−1 were assi` |  |
| PMC9078281 | `m−1 to 1750 cm−1 with a ce` |  |
| PMC9078281 | `nds at 1258 cm−1 and 1078 ` |  |
| PMC9078281 | `nds at 1407 cm−1 and 830 c` |  |
| PMC9078281 | `on (6.52 mg mL−1, ESI†) wa` |  |
| PMC9078281 | `on of 40 μg mL−1 for 3 h, ` |  |
| PMC9078281 | `ter at 1580 cm−1 correspon` |  |
| PMC9078281 | `to be 3.4 × 10−8 mol L−1 b` |  |
| PMC9078281 | `−1 and 1078 cm−1 were attr` |  |
| PMC9078281 | `−1 and 1449 cm−1 correspon` |  |
| PMC9078598 | ` of 0.91 cm2 V−1 s−1 and a` | oui |
| PMC9078598 | ` of 3.35 cm2 V−1 s−1 and c` | oui |
| PMC9078598 | ` to 3.35 cm2 V−1 s−1, whic` | oui |
| PMC9078598 | `0.91 cm2 V−1 s−1 and a res` | oui |
| PMC9078598 | `3.35 cm2 V−1 s−1 and carri` | oui |
| PMC9078598 | `3.35 cm2 V−1 s−1, which is` | non |
| PMC9078598 | `9.06 × 1016 cm−3 also was ` | oui |
| PMC9078598 | `9.06 × 1016 cm−3 as the su` | oui |
| PMC9078598 | `9.06 × 1016 cm−3 with the ` | non |
| PMC9078598 | `9.46 × 1013 cm−3, a mobili` | oui |
| PMC9078598 | `95 and 1040 cm−1 could be ` | oui |
| PMC9078598 | `ound at 331 cm−1, which co` | non |
| PMC9078598 | `peak at 331 cm−1 can be cl` | non |
| PMC9078598 | `peak at 472 cm−1 correspon` | oui |
| PMC9078598 | `peak of 333 cm−1 assigned ` | non |
| PMC9078598 | `ved at ∼472 cm−1, which is` | oui |
| PMC9079727 | ` was 1.54 × 10−5 S cm−1 fo` | non |
| PMC9079727 | `10 × 10−4 S cm−1 was obser` | oui |
| PMC9079727 | `10 × 10−4 S cm−1 was synth` | oui |
| PMC9079727 | `54 × 10−5 S cm−1 for LLZAL` | non |
| PMC9079727 | `proximately 10−4 S cm−1, a` | non |
| PMC9079727 | `te of 4.2° min−1. Cu-Kα ra` | non |
| PMC9079727 | `tely 10−4 S cm−1, and its ` | oui |
| PMC9079727 | `y of 2.10 × 10−4 S cm−1 wa` | oui |
| PMC9079727 | `y of 2.10 × 10−4 S cm−1 wa` | oui |
| PMC9080395 | `.49–1.51 mW cm−2. The reac` | non |
| PMC9080395 | `O (0.148 cm3 g−1) nanopart` | non |
| PMC9080395 | `ading of 2 g L−1 at pH 10 ` | non |
| PMC9080395 | `and 140.9 m2 g−1, respecti` | non |
| PMC9080395 | `be 0.027 cm3 g−1, which is` | non |
| PMC9080395 | `iency at 2 g L−1 could be ` | non |
| PMC9080395 | `ion are: 2 g L−1 catalyst,` | oui |
| PMC9080395 | `ivity at 3 g L−1 is an inc` | non |
| PMC9080395 | `nger and 2 g L−1 loading c` | oui |
| PMC9080395 | `ped ZnO (2 g L−1), anions ` | oui |
| PMC9080395 | `ped ZnO (4 g L−1). The res` | non |
| PMC9080395 | `rate 10 °C min−1. The spec` | non |
| PMC9080395 | `rom 1 to 2 g L−1 and then ` | oui |
| PMC9080395 | `rom 1 to 3 g L−1 while oth` | non |
| PMC9080687 | `of 22.58 mA cm−2, the Voc ` |  |
| PMC9080747 | `C–H of 1401 cm−1 and C–O/C` |  |
| PMC9080747 | `NH– of 1713 cm−1, C–H of 1` |  |
| PMC9080747 | `O–C of 1215 cm−1), but sig` |  |
| PMC9080747 | `O–H of 3424 cm−1, –CONH– o` |  |
| PMC9082527 | `om 52.33 emu g−1 (x = 0.0)` |  |
| PMC9082527 | `om 71.43 emu g−1 (x = 0.0)` |  |
| PMC9082527 | `to 69.34 emu g−1 (x = 0.1)` |  |
| PMC9082527 | `to 87.63 emu g−1 (x = 0.1)` |  |
| PMC9083121 | ` pressure ∼ 10−6 torr. Thi` | oui |
| PMC9083121 | ` resistance 10−15 ohm cm−2 ` | oui |
| PMC9083121 | ` vacuum at ∼10−5 torr at r` | oui |
| PMC9083121 | ` ℏ = 6.58 × 10−16 eVs is th` | non |
| PMC9083121 | `e 10−15 ohm cm−2 for cross` | oui |
| PMC9083121 | `e = 1.602 × 10−19 C is the ` | non |
| PMC9083121 | `m of order ∼10−5 torr. The` | oui |
| PMC9083121 | `m0 = 9.11 × 10−31 kg is the` | non |
| PMC9083554 | ` (iii) 1382 cm−1 correspon` | oui |
| PMC9083554 | ` 152 to 72 F g−1 when curr` | oui |
| PMC9083554 | ` 17.2 × 10−3 s−1, and the ` | non |
| PMC9083554 | ` Ry (1.36 × 10−3 eV), whil` | non |
| PMC9083554 | ` cm−1, 1231 cm−1 and the d` | non |
| PMC9083554 | ` density (W kg−1), and Δt ` | non |
| PMC9083554 | ` from 2–10 A g−1 (Fig. S18` | oui |
| PMC9083554 | ` from 2–10 A g−1) of the 9` | non |
| PMC9083554 | ` from 83–9 F g−1. This can` | non |
| PMC9083554 | ` material (F g−1), V is th` | non |
| PMC9083554 | ` set to 1 × 10−3 Ry per Bo` | non |
| PMC9083554 | ` showed 83 F g−1 at 2 A g−` | non |
| PMC9083554 | ` up to 313 F g−1 when curr` | oui |
| PMC9083554 | `(up to 797 F g−1 at 2 A g−` | oui |
| PMC9083554 | `, (ii) 1728 cm−1 for the c` | oui |
| PMC9083554 | `, and 12 emu g−1, respecti` | oui |
| PMC9083554 | `0 to 1900 W kg−1. These va` | non |
| PMC9083554 | `1 at 0.3 μA cm−2.78 Hydrot` | non |
| PMC9083554 | `10 to 100 mV s−1. GCD meas` | non |
| PMC9083554 | `16 to 5 W h kg−1 with incr` | oui |
| PMC9083554 | `28 and 1580 cm−1, respecti` | oui |
| PMC9083554 | `3 and 141 m2 g−1, respecti` | oui |
| PMC9083554 | `313 to 174 F g−1 with incr` | oui |
| PMC9083554 | `32 and 1572 cm−1 whereas, ` | oui |
| PMC9083554 | `45 and 1587 cm−1, which ar` | oui |
| PMC9083554 | `797 to 266 F g−1 when curr` | oui |
| PMC9083554 | `F g−1 at 1 A g−1.18 In the` | non |
| PMC9083554 | `F g−1 at 2 A g−1 current d` | non |
| PMC9083554 | `F g−1 at 2 A g−1) compared` | oui |
| PMC9083554 | `F g−1 at 2 A g−1), this tr` | non |
| PMC9083554 | `F g−1 at 2 A g−1). The pre` | non |
| PMC9083554 | `F g−1 at 6 A g−1) when the` | oui |
| PMC9083554 | `GO was 152 F g−1 at the ch` | oui |
| PMC9083554 | `aks at 1728 cm−1, 1231 cm−` | non |
| PMC9083554 | `alyst (0.1 g L−1) was adde` | non |
| PMC9083554 | `ance (>600 F g−1) in aqueo` | non |
| PMC9083554 | `ance = 172 F g−1). After 2` | oui |
| PMC9083554 | `ance of 28 F g−1 at 0.5 A ` | non |
| PMC9083554 | `and 0.04 cm3 g−1, respecti` | oui |
| PMC9083554 | `as ∼0.04 cm3 g−1 (obtained` | non |
| PMC9083554 | `at (i) 1232 cm−1 correspon` | oui |
| PMC9083554 | `band at 594 cm−1 was also ` | oui |
| PMC9083554 | `ck (SA 75 m2 g−1, bulk den` | oui |
| PMC9083554 | `d (iv) 1056 cm−1 for the C` | oui |
| PMC9083554 | `d up to 83 F g−1 when the ` | oui |
| PMC9083554 | `e (10–100 mV s−1) in 3 M K` | non |
| PMC9083554 | `e (10–100 mV s−1), the inc` | non |
| PMC9083554 | `e of ∼81.5 F g−1 at 1 A g−` | non |
| PMC9083554 | `eak at 1382 cm−1 indicated` | non |
| PMC9083554 | `ed was 160 F g−1 at a curr` | oui |
| PMC9083554 | `ensity (W h kg−1), Cs is t` | non |
| PMC9083554 | `f 5.7 × 10−3 s−1 for reduc` | non |
| PMC9083554 | `g−1 at 0.5 A g−1.77 Spray ` | non |
| PMC9083554 | `ins at 1621 cm−1 was also ` | non |
| PMC9083554 | `ity (∼10 kW kg−1) for a sh` | non |
| PMC9083554 | `ity (∼5 W h kg−1) is lower` | non |
| PMC9083554 | `ity 2.4 W h kg−1 at a powe` | oui |
| PMC9083554 | `nce of 313 F g−1, whereas ` | non |
| PMC9083554 | `nce of 5.7 F g−1 at 0.3 μA` | non |
| PMC9083554 | `nce of 797 F g−1 and reten` | non |
| PMC9083554 | `nce was 1 × 10−4 Ry (1.36 ` | non |
| PMC9083554 | `nsity is 2 A g−1. The valu` | non |
| PMC9083554 | `nsity of 2 A g−1, and it w` | oui |
| PMC9083554 | `nsity of 2 A g−1. Though t` | non |
| PMC9083554 | `nsity of 6 A g−1 for more ` | oui |
| PMC9083554 | `olyte (313 F g−1 at 2 A g−` | oui |
| PMC9083554 | `olyte at 2 A g−1 current d` | non |
| PMC9083554 | `om 2 to 10 A g−1 in 3 M KO` | non |
| PMC9083554 | `om 2 to 10 A g−1 like CuFe` | oui |
| PMC9083554 | `om 2 to 10 A g−1. In this ` | non |
| PMC9083554 | `om 2 to 10 A g−1.GCD measu` | non |
| PMC9083554 | `or (3–9 W h kg−1 at 3000 t` | oui |
| PMC9083554 | `peed of 3° min−1. Fourier ` | non |
| PMC9083554 | `pp = 17.2 × 10−3 s−1, and ` | non |
| PMC9083554 | `pp of 5.7 × 10−3 s−1 for r` | non |
| PMC9083554 | `r (0.0257 eV Å−1). It is a` | non |
| PMC9083554 | `r RGO (550 F g−1), this pr` | non |
| PMC9083554 | `re ∼0.02 cm3 g−1 and 0.04 ` | oui |
| PMC9083554 | `sity (2–10 A g−1) its capa` | oui |
| PMC9083554 | `sity was 2 A g−1. For 96Cu` | non |
| PMC9083554 | `tance (343 F g−1 at 6 A g−` | oui |
| PMC9083554 | `to 10 000 W kg−1).24,74 Th` | non |
| PMC9083554 | `ty (895 mA h g−1).18 To ov` | non |
| PMC9083554 | `ty 170–230 g L−1), N-methy` | oui |
| PMC9083554 | `ty of 380 W kg−1. The ener` | non |
| PMC9083554 | `ty of 380 W kg−1.To the be` | non |
| PMC9083554 | `ty of 460 W kg−1). When 3 ` | non |
| PMC9083554 | `ty of 543 W kg−1, which wa` | oui |
| PMC9083554 | `ulation was 10−6 Ry, and t` | non |
| PMC9083554 | `y of 11 W h kg−1 at a powe` | oui |
| PMC9083554 | `y of 16 W h kg−1 at a powe` | oui |
| PMC9083554 | `y of 16 W h kg−1 at a powe` | oui |
| PMC9083554 | `ystem (797 F g−1 at 2 A g−` | oui |
| PMC9085430 | ` 0.2–0.4 mol L−1 reactant ` | oui |
| PMC9085430 | ` 0.2–0.4 mol L−1 reactant ` | oui |
| PMC9085430 | ` and 0.4 mol L−1, respecti` | oui |
| PMC9085430 | ` are 8.09 × 10−3, 12.80 × ` | oui |
| PMC9085430 | ` of 10−8 to 10−11 cm2 s−1 d` | oui |
| PMC9085430 | `0.3, 0.4 mol L−1 were labe` | oui |
| PMC9085430 | `5/122.4 mA h g−1, and the ` | oui |
| PMC9085430 | `6 × 10−3 cm3 g−1 for LNMO-` | oui |
| PMC9085430 | `and 13.96 × 10−3 cm3 g−1 f` | oui |
| PMC9085430 | `and 3.935 m2 g−1, respecti` | oui |
| PMC9085430 | `cm−1)/I(615 cm−1) for LNMO` | oui |
| PMC9085430 | `cm−1)/I(615 cm−1) increase` | non |
| PMC9085430 | `d 124.9 mA h g−1, respecti` | oui |
| PMC9085430 | `d at 0.3 mol L−1 has relat` | non |
| PMC9085430 | `d at 0.3 mol L−1 has the l` | non |
| PMC9085430 | `d at 0.3 mol L−1 reactant ` | oui |
| PMC9085430 | `he range of 10−8 to 10−11 ` | oui |
| PMC9085430 | `io of I(576 cm−1)/I(615 cm` | oui |
| PMC9085430 | `n of 0.3 mol L−1 has the l` | non |
| PMC9085430 | `nd 105.36 mg L−1, respecti` | oui |
| PMC9085430 | `os of I(576 cm−1)/I(615 cm` | oui |
| PMC9085430 | `sp = 1.42 × 10−7, 25 °C) d` | non |
| PMC9085430 | `sp = 2.24 × 10−11, 25 °C) a` | non |
| PMC9085430 | `te of 0.1 mV s−1. For all ` | non |
| PMC9085430 | `te of 0.1 mV s−1.Results a` | non |
| PMC9085430 | `to 10−11 cm2 s−1 during th` | oui |
| PMC9085430 | `ty (650 W h kg−1).3,4 In a` | non |
| PMC9085430 | `−3, 12.80 × 10−3, 14.95 × ` | oui |
| PMC9085430 | `−3, 14.95 × 10−3 and 13.96` | oui |
| PMC9088863 | ` was 100 mW cm−2, calibrat` |  |
| PMC9088863 | `evel of 2 × 10−8 torr) thr` |  |
| PMC9088863 | `in the 1020 cm−3 range) in` |  |
| PMC9088863 | `n of 100 mW cm−2. J–V curv` |  |
| PMC9088863 | `on of 40 mg ml−1. The blen` |  |
| PMC9088863 | `ut 1 × 1019 cm−3 if is as` |  |
| PMC9089436 | ` DAPI (1 μg mL−1) after wa` |  |
| PMC9089436 | ` FA (300 μg mL−1) were res` |  |
| PMC9089436 | ` and 600 μg mL−1) for 24 h` |  |
| PMC9089436 | ` and 600 μg mL−1) were int` |  |
| PMC9089436 | ` laser (2 W cm−2 for 3 min` |  |
| PMC9089436 | ` mL of 1 mg mL−1 PMSNs@DOX` |  |
| PMC9089436 | `0 to 600 μg mL−1 of PMSNs ` |  |
| PMC9089436 | `0 to 600 μg mL−1. The fram` |  |
| PMC9089436 | `PMSNs (1 mg mL−1) ethanol ` |  |
| PMC9089436 | `X@FA 600 μg mL−1 after inc` |  |
| PMC9089436 | `ation (2 mg mL−1) were add` |  |
| PMC9089436 | `e at 10 °C min−1. The zeta` |  |
| PMC9089436 | `ere 539.9 m2 g−1 (Fig. 3a)` |  |
| PMC9089436 | `eved 600 μg mL−1 (Fig. 7b)` |  |
| PMC9089436 | `ion of 1 mg mL−1. Each exp` |  |
| PMC9089436 | `s@DOX (1 mg mL−1) ethanol ` |  |
| PMC9089436 | `tion at 2 W cm−2 for 8 min` |  |
| PMC9089436 | `ution (1 mg mL−1) in a 50 ` |  |
| PMC9091964 | ` and 125 μg mL−1 and the p` |  |
| PMC9091964 | ` and 3.9 μg mL−1). Specifi` |  |
| PMC9091964 | ` and 7.8 μg mL−1, respecti` |  |
| PMC9091964 | ` cm−1, 3420 cm−1, and 1634` |  |
| PMC9091964 | ` of 0.09 mol L−1 Tollens' ` |  |
| PMC9091964 | ` of 15.6 μg mL−1, respecti` |  |
| PMC9091964 | ` than 10 μg mL−1 can be to` |  |
| PMC9091964 | `.9 and 35 m2 g−1, respecti` |  |
| PMC9091964 | `0 cm−1, 604 cm−1 and 469 c` |  |
| PMC9091964 | `0, and 0 μg mL−1) was mixe` |  |
| PMC9091964 | `1, and 1634 cm−1 are cause` |  |
| PMC9091964 | `2O (0.67 mol L−1) and 0.07` |  |
| PMC9091964 | `32− at 1425 cm−1, which ma` |  |
| PMC9091964 | `O5 (0.02 mol L−1) were sep` |  |
| PMC9091964 | `ached 80 μg mL−1. This tes` |  |
| PMC9091964 | `and 62.5 μg mL−1, respecti` |  |
| PMC9091964 | `and at 1051 cm−1 and shoul` |  |
| PMC9091964 | `ands at 570 cm−1, 604 cm−1` |  |
| PMC9091964 | `e was 30 μg mL−1, the grow` |  |
| PMC9091964 | `han 15.6 μg mL−1 and 62.5 ` |  |
| PMC9091964 | `id (0.01 mol L−1, 2 mL) wa` |  |
| PMC9091964 | `ion (100 μg mL−1) for E. c` |  |
| PMC9091964 | `m−1 and 469 cm−1 are ascri` |  |
| PMC9091964 | `nds at 3572 cm−1, 3420 cm−` |  |
| PMC9091964 | `of 1–2.5 μg mL−1.11 Furthe` |  |
| PMC9091964 | `peak at 966 cm−1 are attri` |  |
| PMC9091964 | `red at 1050 cm−1. This may` |  |
| PMC9091964 | `than 125 μg mL−1. Meanwhil` |  |
| PMC9091964 | `than 500 μg mL−1, but the ` |  |
| PMC9091964 | `tly, 100 μg mL−1 HA@Ag nan` |  |
| PMC9091964 | `units (CFU) mL−1, then inc` |  |
| PMC9099495 | ` below 3000 cm−1 in the sp` | non |
| PMC9099495 | `00 and 1620 cm−1 due to th` | oui |
| PMC9099495 | `and at 1390 cm−1 recorded ` | non |
| PMC9099495 | `and at 1620 cm−1 is due to` | non |
| PMC9099495 | `around 2200 cm−1 is due to` | non |
| PMC9099495 | `at ca. 3400 cm−1 is due to` | non |
| PMC9099495 | `ered on 400 cm−1 associate` | oui |
| PMC9099495 | `he 4000–450 cm−1 range in ` | non |
| PMC9121351 | `50 and 3100 cm–1, correspo` |  |
| PMC9121351 | `58 and 1702 cm–1), as well` |  |
| PMC9121351 | `lution of 4 cm–1 using the` |  |
| PMC9136838 | ` = 55.8 mV dec–1 among the` |  |
| PMC9136838 | ` = 55.8 mV dec–1 was estim` |  |
| PMC9136838 | ` = 60.3 mV dec–1, respecti` |  |
| PMC9136838 | ` = 65.8 mV dec–1 and b = 6` |  |
| PMC9136838 | ` and 100 mA cm–2 at overpo` |  |
| PMC9136838 | ` and 100 mA cm–2 reached a` |  |
| PMC9136838 | ` at 0.25 mg cm–2 mass load` |  |
| PMC9136838 | ` b = 94 mV dec–1.8 In anot` |  |
| PMC9136838 | ` of 0.25 mg cm–2 (Figure 2` |  |
| PMC9136838 | `(b = 35 mV dec–1).49 Ce-do` |  |
| PMC9136838 | `(b = 80 mV dec–1), outperf` |  |
| PMC9136838 | `b = 124 mV dec–1) in alkal` |  |
| PMC9136838 | `e of 10 °C min–1 was used.` |  |
| PMC9136838 | `ty of 10 mA cm–2 for 100 h` |  |
| PMC9143007 | ` (96,483 C·mol−1), represe` | non |
| PMC9143007 | ` 1.602176 × 10−19 C, NA = 6` | non |
| PMC9143007 | ` and 165 mAh·g−1 at 0.2 C ` | oui |
| PMC9143007 | ` than 40 mAh·g−1 at 2 C []` | oui |
| PMC9143007 | ` was 120 mAh·g−1 at 0.1 C ` | oui |
| PMC9143007 | ` × 10−16 cm2·s−1 for the g` | non |
| PMC9143007 | ` × 10−16 cm2·s−1, which is` | non |
| PMC9143007 | `.314 J·mol−1·K−1), T is th` | non |
| PMC9143007 | `0 is 2.53 × 10−16 cm2·s−1, ` | oui |
| PMC9143007 | `0–80° (10°⋅min−1) were rec` | non |
| PMC9143007 | `2 to 150 mAh·g−1 after six` | non |
| PMC9143007 | `6 × 10−14 S·cm−1) [] make ` | non |
| PMC9143007 | `7 and 87 mAh·g−1 at 0.2, 0` | oui |
| PMC9143007 | `and 79.3 mAh·g−1, with the` | oui |
| PMC9143007 | `and 93.4 mAh·g−1 at 0.5, 1` | oui |
| PMC9143007 | `and 93.4 mAh·g−1, respecti` | oui |
| PMC9143007 | `and 96.9 mAh·g−1, respecti` | oui |
| PMC9143007 | `as 168.1 mAh·g−1 at 0.1 C,` | oui |
| PMC9143007 | `e to 2.90 × 10−16 cm2·s−1 f` | non |
| PMC9143007 | `elow 150 mAh·g−1 at 0.2 C)` | oui |
| PMC9143007 | `elow 170 mAh·g−1. Therefor` | non |
| PMC9143007 | `g to 165 mAh·g−1) at room ` | non |
| PMC9143007 | `ient (~16 × 10−16 cm2/s) []` | non |
| PMC9143007 | `ity (331 mAh·g−1), environ` | non |
| PMC9143007 | `ivity (~6 × 10−14 S·cm−1) [` | non |
| PMC9143007 | `late 140 mAh·g−1 at 0.2 C ` | oui |
| PMC9143007 | `nd 105.4 mAh·g−1 to 114.2,` | oui |
| PMC9143007 | `om 110.1 mAh·g−1 (1st) to ` | oui |
| PMC9143007 | `om 172.5 mAh·g−1 (41st) to` | oui |
| PMC9143007 | `t (8.314 J·mol−1·K−1), T i` | non |
| PMC9143007 | `te 168.1 mAh·g−1 (0.1 C, 1` | non |
| PMC9143007 | `than 120 mAh·g−1 (0.1 C, 1` | non |
| PMC9143007 | `than 180 mAh·g−1 at 0.1 C ` | oui |
| PMC9143007 | `to 163.4 mAh·g−1 (10th), w` | oui |
| PMC9143007 | `to 185.8 mAh·g−1 (50th), w` | oui |
| PMC9143007 | `y of 192 mAh·g−1 at 0.2 C,` | oui |
| PMC9165520 | ` (6.94 eV atom−1),[ ] ind` | non |
| PMC9165520 | ` and 0.02 eV Å−1, respecti` | non |
| PMC9165520 | ` and 100 mA cm–2 (Figure 3` | oui |
| PMC9165520 | ` and 200 mA cm–2 at 1.62 a` | oui |
| PMC9165520 | ` and 200 mA cm–2, which is` | non |
| PMC9165520 | ` and 200 mA cm–2. By evalu` | non |
| PMC9165520 | ` and 200 mA cm–2. Moreover` | non |
| PMC9165520 | ` and1000 mA cm–2 at only1.` | oui |
| PMC9165520 | `2.24 × 1025 cm–3), indicat` | non |
| PMC9165520 | `2.80 × 1026 cm–3) is about` | non |
| PMC9165520 | `3 to 75 mV dec–1, suggesti` | non |
| PMC9165520 | `4 (29.98 mF cm–2), suggest` | oui |
| PMC9165520 | `4 (76.17 mF cm–2), much hi` | oui |
| PMC9165520 | `96 485.3 C mol–1), I is th` | non |
| PMC9165520 | `96 485.3 C mol–1), and n i` | non |
| PMC9165520 | `O4(53.5 kJ mol–1), which d` | non |
| PMC9165520 | `V at 500 mA cm–2 with a ce` | non |
| PMC9165520 | `and 1000 mA cm–2) in conce` | non |
| PMC9165520 | `e (24.5 kJ mol–1) compared` | non |
| PMC9165520 | `each 500 mA cm–2 with asse` | non |
| PMC9165520 | `each 500 mA cm–2 with asse` | non |
| PMC9165520 | `maximum at 6 Å–1 can be ob` | non |
| PMC9165520 | `ng of ≈4 mg cm–2, and grap` | non |
| PMC9165520 | `ng was ≈4mg cm–2 . Charact` | non |
| PMC9165520 | `te of 5 °C·min–1.[ ] The ` | non |
| PMC9165520 | `tion (50 mg mL–1) was adde` | oui |
| PMC9165520 | `ty (>500 mA cm–2) under se` | non |
| PMC9165520 | `ws (dk = 1.0 Å–1) to separ` | non |
| PMC9165520 | `xations are 10−5 eV and 0.` | non |
| PMC9165520 | `y of 500 mA cm–2 over 50 h` | oui |
| PMC9181868 | `15 and 3473 cm−1 represent` | non |
| PMC9181868 | `aks at 2923 cm−1 and 2853 ` | non |
| PMC9181868 | `around 1218 cm−1 reflects ` | non |
| PMC9181868 | `around 1470 cm−1 indicates` | non |
| PMC9181868 | `eak at 1040 cm−1 shows the` | non |
| PMC9181868 | `een at 1630 cm−1, indicati` | non |
| PMC9181868 | `ent, at 570 cm−1 and 450 c` | oui |
| PMC9181868 | `line at 638 cm−1, which co` | non |
| PMC9181868 | `m−1 and 450 cm−1. The high` | non |
| PMC9181868 | `of 4000–500 cm−1. A scanni` | non |
| PMC9181868 | `peak at 773 cm−1 indicates` | non |
| PMC9181868 | `the 500−850 cm−1 range sho` | non |
| PMC9181868 | `−1 and 2853 cm−1 show the ` | non |
| PMC9181973 | ` 148/134 mAh g−1 to 164.8/` | oui |
| PMC9181973 | ` ≈ 107.9 mAh g−1), 78.76% ` | oui |
| PMC9181973 | ` ≈ 126.8 mAh g−1), 81.94% ` | oui |
| PMC9181973 | ` ≈ 148.1 mAh g−1). Restori` | non |
| PMC9181973 | `.8/167.2 mAh g−1. However,` | non |
| PMC9181973 | `1 and 35 mAh g−1. The samp` | non |
| PMC9181973 | `1, 126.2 mAh g−1 and 20.6 ` | oui |
| PMC9181973 | `1, 138.9 mAh g−1, 126.2 mA` | oui |
| PMC9181973 | `1, 140.1 mAh g−1 and 35 mA` | oui |
| PMC9181973 | `1, 149.8 mAh g−1, 140.1 mA` | oui |
| PMC9181973 | `64.8/161 mAh g−1 and 170.8` | oui |
| PMC9181973 | `8.5/89.1 mAh g−1. In addit` | non |
| PMC9181973 | `and 20.6 mAh g−1, respecti` | oui |
| PMC9181973 | `d to 124 mAh g−1, 149.8 mA` | oui |
| PMC9181973 | `ed 167.2 mAh g−1 and 97.89` | oui |
| PMC9181973 | `h ≈ 42.4 mAh g−1), respect` | oui |
| PMC9181973 | `hod (159 mAh g−1). The cyc` | non |
| PMC9181973 | `re 107.1 mAh g−1, 138.9 mA` | oui |
| PMC9181973 | `te of 10 K min−1. The crys` | non |
| PMC9181973 | `th ≈ 137 mAh g−1) and 47.5` | oui |
| PMC9181973 | `to 149.8 mAh g−1. These re` | non |
| PMC9182795 | `33 and 2864 cm−1 are attri` |  |
| PMC9182795 | `4000 to 400 cm−1, using a ` |  |
| PMC9182795 | `62 and 1367 cm−1 []. The p` |  |
| PMC9182795 | `63, and 967 cm−1, which co` |  |
| PMC9182795 | `aks at 3434 cm−1 matched t` |  |
| PMC9182795 | `cted at a 4 cm−1 resolutio` |  |
| PMC9182795 | `eak at 1163 cm−1. The abso` |  |
| PMC9182795 | `eak at 1255 cm−1 can be at` |  |
| PMC9182795 | `eak at 1725 cm−1. The exis` |  |
| PMC9182795 | `peak at 967 cm−1 conforms ` |  |
| PMC9182795 | `strong 1725 cm−1 band in C` |  |
| PMC9202246 | ` μmol·gcat–1·h–1. Cu3(BTC)` | non |
| PMC9202246 | `(1.8 μmol·gcat–1).19 The h` | non |
| PMC9202246 | `.94 μ mol·gcat–1) was 7 ti` | non |
| PMC9202246 | `2.64 μmol·gcat–1·h–1. Cu3(` | non |
| PMC9202246 | `4000 to 400 cm–1 with 2 cm` | oui |
| PMC9202246 | `52 and 1191 cm–1, respecti` | oui |
| PMC9202246 | `6.26 μmol·gcat–1 over Mg0.` | oui |
| PMC9202246 | `889 and 823 cm–1 of Mg0.2C` | oui |
| PMC9202246 | `89 and 1191 cm–1 in the sp` | oui |
| PMC9202246 | `9.44 μmol·gcat–1 over Mg0.` | oui |
| PMC9202246 | `9.44 μmol·gcat–1 over Mg0.` | oui |
| PMC9202246 | `90, and 823 cm–1, which we` | oui |
| PMC9202246 | `cm–1 with 2 cm–1. Thermogr` | non |
| PMC9202246 | `e below 700 cm–1 regions m` | non |
| PMC9202246 | `e of 20 mL·min–1 for 15 mi` | oui |
| PMC9202246 | `eak at 1240 cm–1 is attrib` | oui |
| PMC9202246 | `ed 7.18 mmol·g–1. However,` | non |
| PMC9202246 | `ely 0.39 cm3·g–1. The surf` | non |
| PMC9202246 | `nd 1.68 mmol·g–1, respecti` | oui |
| PMC9202246 | `ove the 700 cm–1 region ar` | non |
| PMC9202246 | `re 3.52 mmol·g–1 and 23.13` | oui |
| PMC9202246 | `s 1561.96 m2·g–1, which wa` | non |
| PMC9202246 | `to 1.52 mmol·g–1. This phe` | non |
| PMC9202246 | `to 2.09 mmol·g–1. MgxCu1–x` | non |
| PMC9202246 | `to 3.24 mmol·g–1. Thus, th` | non |
| PMC9202246 | `to 3.52 mmol·g–1. The yiel` | non |
| PMC9202246 | `to 4.58 mmol·g–1, and that` | oui |
| PMC9202246 | `to 8.61 mmol·g–1. Mg-MOF-7` | non |
| PMC9202246 | `up to 8 mmol·g–1.15 Bao et` | non |
| PMC9215008 | `00 and 4000 cm−1 and the r` |  |
| PMC9215008 | `60 and 1056 cm−1 are S=O, ` |  |
| PMC9215008 | `aks at 1641 cm−1 and 1420 ` |  |
| PMC9215008 | `aks at 2934 cm−1 and 2877 ` |  |
| PMC9215008 | `eak at 1643 cm−1, and ther` |  |
| PMC9215008 | `eak at 2960 cm−1 indicates` |  |
| PMC9215008 | `eak at 3425 cm−1 shows the` |  |
| PMC9215008 | `gnal at 960 cm−1 []; Ful-F` |  |
| PMC9215008 | `les at 1420 cm−1, which pr` |  |
| PMC9215008 | `lution is 8 cm−1, scanning` |  |
| PMC9215008 | `nal at 1100 cm−1, and Si–O` |  |
| PMC9215008 | `nal at 3443 cm−1, Si–O–Si ` |  |
| PMC9215008 | `peak at 802 cm−1 is C–O–S,` |  |
| PMC9215008 | `−1 and 1420 cm−1 are C=O, ` |  |
| PMC9215008 | `−1 and 2877 cm−1 due to th` |  |
| PMC9227472 | `4, and 3428 cm−1, which co` |  |
| PMC9227472 | `7, and 2723 cm−1 correspon` |  |
| PMC9227472 | `and at 3325 cm−1 were attr` |  |
| PMC9227472 | `around 3431 cm−1 indicates` |  |
| PMC9227472 | `eak at 1634 cm−1 and the i` |  |
| PMC9227472 | `eak at 2925 cm−1 reflects ` |  |
| PMC9227472 | `ge 400–4000 cm−1 at room t` |  |
| PMC9227472 | `lization of 10−3 M of AgNO` |  |
| PMC9227472 | `nd 1630.121 cm−1 were rela` |  |
| PMC9227472 | `red at 1057 cm−1, whereas ` |  |
| PMC9300655 | ` (E < 8 kJ mol-1).The nonl` | non |
| PMC9300655 | ` (E > 8 kJ mol-1). For the` | oui |
| PMC9300655 | ` and B1 (mol J-1) is the q` | non |
| PMC9300655 | ` cm-1, 1100 cm−1, 1565 cm-` | non |
| PMC9300655 | ` cm−1, 1565 cm-1, and 1640` | non |
| PMC9300655 | ` h (mg g-1 min-1) are the ` | non |
| PMC9300655 | `) and qt (mg g-1) are the ` | non |
| PMC9300655 | `), and h (mg g-1 min-1) ar` | oui |
| PMC9300655 | `, and qm (mg g-1) is the a` | non |
| PMC9300655 | `. The KF (L mg-1) constant` | non |
| PMC9300655 | `1, 0.283 cm3 g-1, and 10.6` | oui |
| PMC9300655 | `1, and 1640 cm-1 can be as` | non |
| PMC9300655 | `497 and 998 cm−1, which co` | non |
| PMC9300655 | `HNO3 (15 mol L-1) was prep` | oui |
| PMC9300655 | `OH (0.1 mol L −1)/ethanol ` | oui |
| PMC9300655 | `ands at 610 cm-1, 1100 cm−` | non |
| PMC9300655 | `around 1640 cm-1 were not ` | non |
| PMC9300655 | `bent, qe (mg g-1) is the a` | non |
| PMC9300655 | `ber 480–580 cm−145. In the` | non |
| PMC9300655 | `energy (Kj mol-1) is less ` | non |
| PMC9300655 | `ion of 20 mg L-1 and a bin` | non |
| PMC9300655 | `ion: 30.0 mg L-1, and solu` | oui |
| PMC9300655 | `ions, qe (mg g-1) and qt (` | non |
| PMC9300655 | `ively. k1 (min-1), k2 (g m` | non |
| PMC9300655 | `k2 (g mg-1 min-1), and h (` | non |
| PMC9300655 | `n of 30.0 mg L−1, and solu` | non |
| PMC9300655 | `n-1), k2 (g mg-1 min-1), a` | non |
| PMC9300655 | `re 106.54 m2 g-1, 0.283 cm` | oui |
| PMC9300655 | `s 6.704 kJ mol-1, suggesti` | non |
| PMC9300655 | `s 9.054 kJ mol-1 and shows` | non |
| PMC9300655 | `t, and C (g mg-1) is a con` | non |
| PMC9300655 | `tion, Ce (mg L-1) is the e` | non |
| PMC9300655 | `tion, KL (L mg-1) is the e` | non |
| PMC9300655 | `ty of KT (mg L-1) in the T` | non |
| PMC9300655 | `y. Kdiff (mg g-1 min0.5) i` | oui |
| PMC9300655 | `ye (10–50 mg L-1), sonicat` | non |
| PMC9307632 | ` [Cd+2] and [S−2] precurso` | non |
| PMC9307632 | `5.64 × 1018 cm−3, and 0.83` | oui |
| PMC9316793 | `000 to 3680 cm−1 represent` | non |
| PMC9316793 | `15 and 1033 cm−1 reveal th` | oui |
| PMC9316793 | `97 and 1215 cm−1 are assig` | oui |
| PMC9316793 | `and at 1356 cm−1 and a dis` | oui |
| PMC9316793 | `and at 1572 cm−1, represen` | non |
| PMC9323265 | ` 4.14 × 1012 M−1·s−1. Addi` | oui |
| PMC9323265 | ` 7.72 × 1011 M−1·s−1. Both` | oui |
| PMC9323265 | ` as −0.0039 µM−1 and 4.22 ` | oui |
| PMC9323265 | `, 1.0 × 1010 M−1·s−1. Thus` | non |
| PMC9323265 | `0 × 1010 M−1·s−1. Thus, th` | non |
| PMC9323265 | `2 × 1011 M−1·s−1. Both the` | non |
| PMC9323265 | `4 × 1012 M−1·s−1. Addition` | non |
| PMC9323265 | `6, and 1404 cm−1 were rela` | oui |
| PMC9323265 | `74 and 1175 cm−1 []. Thus,` | non |
| PMC9323265 | `around 3400 cm−1 of the FT` | non |
| PMC9323265 | `d as 0.0318 µM−1, based on` | non |
| PMC9323265 | `f 2850–2950 cm−1 were ascr` | non |
| PMC9323570 | ` (96,486 C·mol−1), C is th` | non |
| PMC9323570 | ` (~10−14 cm2·s−1) and elec` | non |
| PMC9323570 | ` 1.9–2.1 mg·cm−2 and then ` | oui |
| PMC9323570 | ` × 10−3 mol·mL−1), and σ i` | non |
| PMC9323570 | `), 140.3 mAh·g−1 (LFP/C), ` | oui |
| PMC9323570 | `), 147.4 mAh·g−1 (LFP-N), ` | oui |
| PMC9323570 | `.314 J mol−1·K−1), T (K) i` | non |
| PMC9323570 | `Li+ (7.69 × 10−3 mol·mL−1)` | oui |
| PMC9323570 | `LiPF6 (1 mol·L−1) dissolve` | oui |
| PMC9323570 | `aks at 1350 cm−1 and 1590 ` | non |
| PMC9323570 | `ductivity (~10−10 S·cm−1) c` | non |
| PMC9323570 | `e of 10 °C·min−1 were carr` | non |
| PMC9323570 | `eak at 1350 cm−1 correspon` | non |
| PMC9323570 | `eak at 1590 cm−1 correspon` | non |
| PMC9323570 | `eed of 12° min−1. Thermal ` | non |
| PMC9323570 | `efficient (~10−14 cm2·s−1) ` | non |
| PMC9323570 | `en 115.8 mAh·g−1 at 10 C, ` | oui |
| PMC9323570 | `n of 0.3 mol·L−1, was obta` | oui |
| PMC9323570 | `nd 128.4 mAh·g−1 at 0.1 C ` | oui |
| PMC9323570 | `nd 160.7 mAh·g−1 (LFP/C-N)` | oui |
| PMC9323570 | `of 126.2 mAh·g−1 (LFP), 14` | oui |
| PMC9323570 | `of 128.4 mAh·g−1 at 5 C wi` | oui |
| PMC9323570 | `of 160.7 mAh·g−1 and 128.4` | non |
| PMC9323570 | `of 200–3000 cm−1 using a l` | non |
| PMC9323570 | `t (8.314 J mol−1·K−1), T (` | non |
| PMC9323570 | `te of 0.1 mV·s−1. All the ` | non |
| PMC9323570 | `te of 3 °C·min−1 in a tube` | oui |
| PMC9323570 | `where D (cm2·s−1) is the L` | non |
| PMC9323570 | `y (~10−10 S·cm−1) cause se` | non |
| PMC9323570 | `−1 and 1590 cm−1 are the c` | non |
| PMC9370708 | `around 1060 cm−1 belong to` | oui |
| PMC9370708 | `eak at 1545 cm−1 in F-1 fi` | oui |
| PMC9370708 | `eak at 1722 cm−1 is attrib` | oui |
| PMC9370708 | `lution of 4 cm−1. Thermal ` | non |
| PMC9370708 | `s near 3404 cm−1 correspon` | non |
| PMC9370708 | `t 2800–2900 cm−1 can be as` | non |
| PMC9374656 | `00, and 500 cm–1, respecti` | oui |
| PMC9374656 | `below 50 mAh g–1 for x = 0` | oui |
| PMC9374656 | `bove 500 mAh g–1 for x = 0` | oui |
| PMC9374656 | `ed was 1 mol L−1 of lithiu` | oui |
| PMC9374656 | `g., 1625 mAh g–1 for Li4.4` | oui |
| PMC9374656 | `g., 3580 mAh g–1 for Li15S` | oui |
| PMC9374656 | `over 500 mAh g–1 even at 1` | oui |
| PMC9374656 | `sure: 3.0 × 10–4 Pa) with ` | oui |
| PMC9374656 | `ty (1700 mAh g–1). The cou` | non |
| PMC9374656 | `y is 810 mAh g–1 after 100` | oui |
| PMC9374656 | `y of 372 mAh g–13.As new a` | non |
| PMC9407535 | ` cm−1, 1080 cm−1, 1114 cm−` |  |
| PMC9407535 | ` cm−1, 1114 cm−1, 793 cm−1` |  |
| PMC9407535 | `4 cm−1, 793 cm−1, and 467 ` |  |
| PMC9407535 | `43 and 1094 cm−1 are chara` |  |
| PMC9407535 | `800 and 900 cm−1 are chara` |  |
| PMC9407535 | `Band at 937 cm−1 is charac` |  |
| PMC9407535 | `ands at 560 cm−1 or 568 cm` |  |
| PMC9407535 | `bility of 4 cm−1. One mill` |  |
| PMC9407535 | `cm−1 or 568 cm−1 may be at` |  |
| PMC9407535 | `he 400–4000 cm−1 domain wi` |  |
| PMC9407535 | `n 1108–1273 cm−1 domain. S` |  |
| PMC9407535 | `nds at 1273 cm−1, 1080 cm−` |  |
| PMC9407535 | `nds at 1650 cm−1 and 1636 ` |  |
| PMC9407535 | `−1 and 1636 cm−1. In Table` |  |
| PMC9407535 | `−1, and 467 cm−1 are assig` |  |
| PMC9412554 | `08 and 1243 cm−1 occurred ` |  |
| PMC9412554 | `26 and 1648 cm−1, correspo` |  |
| PMC9412554 | `405 and 725 cm−1 correspon` |  |
| PMC9412554 | `426 and 603 cm−1, respecti` |  |
| PMC9412554 | `48 and 1117 cm−1 were also` |  |
| PMC9412554 | `5, and 3426 cm−1. The stro` |  |
| PMC9412554 | `8, and 1498 cm−1 in Figure` |  |
| PMC9412554 | `800 and 400 cm−1 was attri` |  |
| PMC9412554 | `eak at 1648 cm−1 represent` |  |
| PMC9417647 | `eak at 1704 cm−1 could be ` | non |
| PMC9417647 | `g from 2974 cm−1 to 2925 c` | oui |
| PMC9417647 | `g from 3311 cm−1 to 3693 c` | non |
| PMC9417647 | `ion at 2974 cm−1 and 2925 ` | oui |
| PMC9417647 | `m−1 to 2925 cm−1 due to th` | oui |
| PMC9417647 | `m−1 to 3693 cm−1), –C–H (a` | oui |
| PMC9417647 | `nal at 1608 cm−1 belongs t` | non |
| PMC9417647 | `ons (0.4 mg mL−1) are sens` | oui |
| PMC9417647 | `−1 and 2925 cm−1, respecti` | oui |
| PMC9418510 | ` 93% (311 m2 g−1), respect` |  |
| PMC9418510 | ` 95% (324 m2 g−1) and 93% ` |  |
| PMC9418510 | ` = −411 kJ mol−1) and so o` |  |
| PMC9418510 | ` near 300 m2 g−1 directly ` |  |
| PMC9418510 | ` near 300 m2 g−1, both of ` |  |
| PMC9418510 | ` of 0.8 mL min−1. The amou` |  |
| PMC9418510 | `= −1388 kJ mol−1), may sho` |  |
| PMC9418510 | `ea of 198 m2 g−1. These va` |  |
| PMC9418510 | `high ∼300 m2 g−1 surface a` |  |
| PMC9418510 | `t 300–400 m2 g−1, thermal ` |  |
| PMC9418510 | `trate (10 mL g−1 of zeolit` |  |
| PMC9418510 | `ve ∼40–80 m2 g−1 higher su` |  |
| PMC9418562 | ` ≈ 1 cm2 V−1 s−1) was obta` |  |
| PMC9418562 | `/W = 1.12 × 10−9 S μm−1), ` |  |
| PMC9418562 | `1.85 × 1012 cm−2 was estim` |  |
| PMC9418562 | `12 × 10−9 S μm−1), accordi` |  |
| PMC9418562 | `cm−1 and 20 cm−1 with a ta` |  |
| PMC9418562 | `eaked at 18 cm−1 and 20 cm` |  |
| PMC9418562 | `esolution 2 cm−1). All the` |  |
| PMC9418562 | `hey are 3.7 cm−1 and 6.2 c` |  |
| PMC9418562 | `in δ = 19.3 cm−1, as indic` |  |
| PMC9418562 | `le δ = 21.2 cm−1 is obtain` |  |
| PMC9418562 | `m−1 and 5.5 cm−1 for E2G a` |  |
| PMC9418562 | `m−1 and 6.2 cm−1 for the a` |  |
| PMC9418562 | `r in 0.1 mg ml−1 sodium ci` |  |
| PMC9418562 | `ths are 2.9 cm−1 and 5.5 c` |  |
| PMC9418562 | `x = 11.9 nF cm−2 being the` |  |
| PMC9418562 | `y (μ ≈ 1 cm2 V−1 s−1) was ` |  |
| PMC9418607 | ` be 0.23 cm3 g−1 (Fig. S11` |  |
| PMC9418607 | `2 (67.3 mV dec−1) and seve` |  |
| PMC9418607 | `AOIA (703 m2 g−1). Consequ` |  |
| PMC9418607 | `and 117 mV dec−1, respecti` |  |
| PMC9418607 | `e of 10 °C min−1. The resu` |  |
| PMC9418607 | `o be 53 mV dec−1, much low` |  |
| PMC9418607 | `o be 66 mV dec−1 and 117 m` |  |
| PMC9418607 | `of 366.8 μF cm−2, indicati` |  |
| PMC9418607 | `ons at 1342 cm−1 and 1598 ` |  |
| PMC9418607 | `rate of 5 mV s−1, in 1 M N` |  |
| PMC9418607 | `rate of 5 mV s−1, indicate` |  |
| PMC9418607 | `te of 5 °C min−1 with a Pe` |  |
| PMC9418607 | `tem. 0.2 mg cm−2 of the as` |  |
| PMC9418607 | `to be 179 m2 g−1, much low` |  |
| PMC9418607 | `to be 703 m2 g−1, at 77 K ` |  |
| PMC9418607 | `ty of 10 mA cm−2 (Ej = 10)` |  |
| PMC9418607 | `ty of 10 mA cm−2 in a two-` |  |
| PMC9418607 | `ty of 10 mA cm−2, Pt/C req` |  |
| PMC9418607 | `ty of 10 mA cm−2, which is` |  |
| PMC9418607 | `−1 and 1598 cm−1, respecti` |  |
| PMC9419006 | ` wafer (520 cm−1) as a sta` | oui |
| PMC9419006 | `62 and 1150 cm−1 were assi` | oui |
| PMC9419006 | `89 and 2383 cm−1 are ascri` | oui |
| PMC9419006 | `9 and 8.3 × 10−17, respecti` | non |
| PMC9419006 | `I are 4.6 × 10−29 and 8.3 ×` | non |
| PMC9419006 | `aks at 1640 cm−1 and 1596 ` | oui |
| PMC9419006 | `around 3320 cm−1 suggest t` | oui |
| PMC9419006 | `eak at 1420 cm−1 is attrib` | oui |
| PMC9419006 | `nds at 1311 cm−1 and 1531 ` | non |
| PMC9419006 | `that (1.0 × 10−12) of CuI. ` | non |
| PMC9419006 | `−1 and 1531 cm−1, which ar` | non |
| PMC9419006 | `−1 and 1596 cm−1 disappear` | oui |
| PMC9419793 | ` of 0.3 mm min−1. The widt` | non |
| PMC9419793 | ` μL of 5 μg ml−1 and 2 μg ` | oui |
| PMC9419793 | `0.3 ± 0.1 MJ m−3 (Fig. 9b)` | oui |
| PMC9419793 | `000 to 3700 cm−1 which ari` | oui |
| PMC9419793 | `1.1 ± 0.6 MJ m−3. rGO-1 ha` | non |
| PMC9419793 | `1.4 ± 0.9 MJ m−3 respectiv` | oui |
| PMC9419793 | `23 and 1050 cm−1 which cor` | oui |
| PMC9419793 | `3 and 680 S cm−1 respectiv` | oui |
| PMC9419793 | `5.7 ± 1.1 MJ m−3 respectiv` | oui |
| PMC9419793 | `75 MPa, 8 MJ m−3 and 680 S` | oui |
| PMC9419793 | `ately 330 S cm−1, a tensil` | oui |
| PMC9419793 | `ately 470 S cm−1. These va` | non |
| PMC9419793 | `ighed.50 μg ml−1 of each G` | oui |
| PMC9419793 | `imately 74 W L−1 for 10 mi` | oui |
| PMC9419793 | `ion at 1620 cm−1 from the ` | oui |
| PMC9419793 | `ionship C (S m−1) = 1/(R ×` | non |
| PMC9419793 | `lus (∼345 S cm−1, 103 ± 35` | oui |
| PMC9419793 | `m 0.01 to 10 s−1 under 25 ` | oui |
| PMC9419793 | `mately 2 μg ml−1 solutions` | non |
| PMC9419793 | `rate of 0.01 s−1, while it` | oui |
| PMC9419793 | `ss of 5.7 MJ m−3, and a co` | non |
| PMC9419793 | `tion (50 μg ml−1) of GO di` | non |
| PMC9419793 | `ty of 470 S cm−1. The pre-` | non |
| PMC9419793 | `ups at 1730 cm−1, the CC v` | oui |
| PMC9419793 | `−1 and 2 μg ml−1 GO soluti` | oui |
| PMC9425827 | `kW) with a h h−1 goniomete` | oui |
| PMC9464223 | `1 cm−1, 802 cm−1 and 484 c` | oui |
| PMC9464223 | `5 cm−1, 981 cm−1, 802 cm−1` | oui |
| PMC9464223 | `band at 802 cm−1. Meanwhil` | non |
| PMC9464223 | `ge 400–4000 cm−1 by Fourie` | non |
| PMC9464223 | `m−1 and 484 cm−1 which cor` | oui |
| PMC9464223 | `nds at 1075 cm−1, 981 cm−1` | oui |
| PMC9464223 | `ons at 1075 cm−1 showed th` | oui |
| PMC9464223 | `peak at 981 cm−1 showed th` | oui |
| PMC9475401 | ` and 75 mA h g−1 for C-LMF` | oui |
| PMC9475401 | ` at 116 mA h g−1 at 10C an` | oui |
| PMC9475401 | ` of 105 mA h g−1 and a cap` | non |
| PMC9475401 | ` of 122 mA h g−1 at 5C and` | oui |
| PMC9475401 | ` of 122 mA h g−1 than the ` | oui |
| PMC9475401 | ` of 129 mA h g−1 for 400 c` | oui |
| PMC9475401 | ` of 129 mA h g−1 with a ca` | oui |
| PMC9475401 | ` of 136 mA h g−1 at 0.1C, ` | oui |
| PMC9475401 | ` × 10−13 cm2 s−1 after the` | oui |
| PMC9475401 | ` × 10−13 cm2 s−1) and C-LM` | oui |
| PMC9475401 | ` × 10−14 cm2 s−1), which w` | non |
| PMC9475401 | `FP (120 mA h g−1). More st` | non |
| PMC9475401 | `FP (126 mA h g−1) and O-LM` | oui |
| PMC9475401 | `MFP (19.9 m2 g−1), which c` | oui |
| PMC9475401 | `MFP (2.02 × 10−14 cm2 s−1),` | oui |
| PMC9475401 | `MFP (32.3 m2 g−1) and O-LM` | oui |
| PMC9475401 | `MFP (8.29 × 10−13 cm2 s−1) ` | oui |
| PMC9475401 | `a of 55.3 m2 g−1 than that` | oui |
| PMC9475401 | `e of 0.05 mV s−1. The elec` | non |
| PMC9475401 | `e of 9.54 × 10−13 cm2 s−1 a` | oui |
| PMC9475401 | `from 105 to 10−1 Hz with a` | oui |
| PMC9475401 | `ined 54 mA h g−1 with a ca` | oui |
| PMC9475401 | `tely 2.5 mg cm−2. A Celgar` | non |
| PMC9476164 | ` 800 to 900 cm–1. Co atoms` | non |
| PMC9476164 | ` above 1000 cm–1 are ascri` | non |
| PMC9476164 | `200 to 1800 cm–1 of ZnO, Z` | non |
| PMC9476164 | `on 1800–200 cm–1 to interp` | non |
| PMC9476164 | `und 600–900 cm–1, the vari` | non |
| PMC9476164 | `und 600–900 cm–1. Also, th` | non |
| PMC9476164 | `y 0.0048474 nm–2 was exhib` | non |
| PMC9476164 | `y 0.0096687 nm–2 was exhib` | non |
| PMC9542428 | `.17 L g − 1 cm−1 at 808 nm` |  |
| PMC9542428 | `25 and 1579 cm−1 in the IZ` |  |
| PMC9542428 | `aser (0.5 W cm−2) for 10 m` |  |
| PMC9542428 | `aser (0.5 W cm−2, 10 min).` |  |
| PMC9542428 | `aser (0.5 W cm−2, 10 min).` |  |
| PMC9542428 | `aser (0.5 W cm−2, 10 min);` |  |
| PMC9542428 | `aser (0.5 W cm−2, 10 min);` |  |
| PMC9542428 | `aser (1.0 W cm−2) for 10 m` |  |
| PMC9542428 | `aser (1.0 W cm−2, 10 min),` |  |
| PMC9542428 | `aser (1.0 W cm−2, 10 min).` |  |
| PMC9542428 | `aser (1.0 W cm−2, 10 min);` |  |
| PMC9542428 | `aser (1.0 W cm−2, 10 min);` |  |
| PMC9542428 | `eak at 1685 cm−1 indicates` |  |
| PMC9542428 | `er at 0.5 W cm−2 for 10 mi` |  |
| PMC9542428 | `er at 1.0 W cm−2 for 10 mi` |  |
| PMC9542428 | `sure (1.0 W cm−2, 10 min) ` |  |
| PMC9563711 | ` at 0.01 mg kg−1. Therefor` | non |
| PMC9563711 | `, and 1,108 cm−1. Absorpti` | non |
| PMC9563711 | `1 and 1,586 cm−1, correspo` | oui |
| PMC9563711 | `6 and 1,108 cm−1 indicate ` | non |
| PMC9563711 | `ak at 1,402 cm−1 (). The b` | non |
| PMC9563711 | `ak at 1,642 cm−1 may indic` | non |
| PMC9563711 | `ds at 3,418 cm−1 indicated` | non |
| PMC9563711 | `ks at 1,353 cm−1 and 1,586` | oui |
| PMC9563711 | `mately 10 mg L−1 of K+, Ca` | non |
| PMC9563711 | `nd at 2,951 cm−1 (). The p` | non |
| PMC9563711 | `p to 1.8 mol L−1) and long` | oui |
| PMC9563711 | `s is 0.1 mg kg−1, and Chin` | non |
| PMC9565927 | `aks at 1035 cm−1, assigned` |  |
| PMC9565927 | `and at 1618 cm−1, correspo` |  |
| PMC9565927 | `ching; 1372 cm−1, assigned` |  |
| PMC9565927 | `ching; 1413 cm−1, correspo` |  |
| PMC9565927 | `of 450–2000 cm−1 (Nicolet ` |  |
| PMC9607883 | `(100–1200 mg L−1) and stir` |  |
| PMC9607883 | `, Ce, Ct (mg L−1) are the ` |  |
| PMC9607883 | `0 to 1200 mg L−1, the adso` |  |
| PMC9607883 | `04 and 1414 cm−1, respecti` |  |
| PMC9607883 | `1, and 1178 cm−1, respecti` |  |
| PMC9607883 | `2†). FT-IR (cm−1, ATR): 35` |  |
| PMC9607883 | `3†). FT-IR (cm−1, ATR): 16` |  |
| PMC9607883 | `50 to 800 mg L−1. During t` |  |
| PMC9607883 | `54 and 1166 cm−1, respecti` |  |
| PMC9607883 | `6, and 1032 cm−1, correspo` |  |
| PMC9607883 | `be 2532.1 mg g−1 at a neut` |  |
| PMC9607883 | `capacity (mg g−1) at equil` |  |
| PMC9607883 | `e (2533.1 mg g−1). It is s` |  |
| PMC9607883 | `e of 10 °C min−1 under dry` |  |
| PMC9607883 | `eak at 1181 cm−1. In parti` |  |
| PMC9607883 | `ion of 1154 cm−1 compared ` |  |
| PMC9607883 | `ion of 50 mg L−1 to determ` |  |
| PMC9607883 | `is 2604.1 mg g−1, which is` |  |
| PMC9607883 | `of 1685.1 mg g−1 at the MG` |  |
| PMC9607883 | `of 2532.1 mg g−1 at a neut` |  |
| PMC9607883 | `on of 400 mg L−1 (Fig. 3a)` |  |
| PMC9607883 | `s (20–400 mg L−1). As a co` |  |
| PMC9607883 | `tion (100 mg L−1) at pH = ` |  |
| PMC9607883 | `ution (50 mg L−1) at an op` |  |
| PMC9609168 | ` (1500–2000 cm−1), and fin` | non |
| PMC9609168 | ` (2000–2500 cm−1), double ` | non |
| PMC9609168 | ` (2500–4000 cm−1), triple ` | non |
| PMC9609168 | ` and 2861.7 cm−1 were rela` | non |
| PMC9609168 | `, and 564.9 cm−1 correspon` | non |
| PMC9609168 | `, and 564.9 cm−1. The spec` | non |
| PMC9609168 | `, and 755.6 cm−1 correspon` | non |
| PMC9609168 | `, and 755.6 cm−1. The peak` | non |
| PMC9609168 | `17, and 551 cm−1. The auth` | non |
| PMC9609168 | `27 and 2034 cm−1 were -N=C` | non |
| PMC9609168 | `400 to 4000 cm−1.X-ray Dif` | non |
| PMC9609168 | `81, and 724 cm−1, which co` | non |
| PMC9609168 | `a at 2098.1 cm−1 referred ` | non |
| PMC9609168 | `eak at 2161 cm−1 was -S-CΞ` | non |
| PMC9609168 | `k at 1397.7 cm−1 was relat` | non |
| PMC9609168 | `k at 1521.7 cm−1 correspon` | non |
| PMC9609168 | `k at 1645.3 cm−1 correspon` | non |
| PMC9609168 | `k at 3347.4 cm−1 refers to` | non |
| PMC9609168 | `k at 3436.1 cm−1 correspon` | non |
| PMC9609168 | `ng 90 mL of 10−3 M silver ` | oui |
| PMC9609168 | `t (600–1500 cm−1) areas. T` | non |
| PMC9611298 | ` C), 110 mAh g−1 (0.2 C), ` | oui |
| PMC9611298 | ` C), 113 mAh g−1 (0.5 C), ` | oui |
| PMC9611298 | ` C), 130 mAh g−1 (0.2 C), ` | oui |
| PMC9611298 | ` × 10−14 cm2 s−1, whereas ` | non |
| PMC9611298 | ` × 10−16 cm2 s−1. The EIS ` | non |
| PMC9611298 | `, and 66 mAh g−1 (1 C). Th` | oui |
| PMC9611298 | `, and 96 mAh g−1 (1 C); th` | oui |
| PMC9611298 | `2 C), 82 mAh g−1 (0.5 C), ` | oui |
| PMC9611298 | `and 97.6 mAh g−1, with cap` | oui |
| PMC9611298 | `bout 125 mAh g−1 (0.1 C), ` | oui |
| PMC9611298 | `bout 800 Wh kg−1 is a good` | non |
| PMC9611298 | `d to 130 mAh g−1 when the ` | oui |
| PMC9611298 | `e of 0.05 mV s−1, which is` | non |
| PMC9611298 | `fted to 979 cm−1 position ` | oui |
| PMC9611298 | `fted to 984 cm−1 position,` | oui |
| PMC9611298 | `hing at 987 cm−1 position ` | oui |
| PMC9611298 | `ined 7.11 × 10−16 cm2 s−1. ` | non |
| PMC9611298 | `nd 145.8 mAh g−1, respecti` | oui |
| PMC9611298 | `s of 145 mAh g−1 (0.1 C), ` | oui |
| PMC9611298 | `s of 6.16 × 10−14 cm2 s−1, ` | oui |
| PMC9611298 | `ty of 96 mAh g−1 at 1 C. T` | oui |
| PMC9611298 | `with 0.05 mV s−1. EIS curv` | non |
| PMC9611298 | `y of 148 mAh g−1, with a c` | oui |
| PMC9612319 | `, and 111 mg·g−1 for BA, b` |  |
| PMC9612319 | `A, and 54 mg·g−1 for BA (T` |  |
| PMC9612319 | `ater, 1.48 g·L−1 at 25°C [` |  |
| PMC9612319 | `han 0.01 mol·L−1) can inhi` |  |
| PMC9612319 | `ls was 73 mg·g−1 for CA, 1` |  |
| PMC9612319 | `n was 160 m² g−1 (Figure S` |  |
| PMC9612319 | `nd BE, 42 mg·g−1 for CA, a` |  |
| PMC9612319 | `ng was 52 mg·g−1 for RA an` |  |
| PMC9612319 | `p of 10 °C.min−1, in air. ` |  |
| PMC9612319 | `r CA, 135 mg·g−1 for BE, a` |  |
| PMC9612319 | `to be 0.74 g·L−1 under the` |  |
| PMC9612319 | `value (37 mg g−1). When ca` |  |
| PMC9626737 | `and 0.18 mg mL−1 by weighi` | oui |
| PMC9626737 | `on (0.15 mg mL−1) and volu` | oui |
| PMC9626737 | `on (0.18 mg mL−1) and then` | oui |
| PMC9626737 | `on (0.78 mg mL−1) was mixe` | oui |
| PMC9626737 | `on of 20 mg mL−1, and soni` | oui |
| PMC9626737 | `out 0.24 mg mL−1. Besides,` | non |
| PMC9626737 | `out 0.78 mg mL−1 and 0.18 ` | oui |
| PMC9626737 | `w as 0.02 μg L−1 for Cd2+ ` | non |
| PMC9631917 | ` 17 μmol g–1 h–1 of CH4 an` | oui |
| PMC9631917 | ` 48 μmol g–1 h–1 and 0.95%` | oui |
| PMC9631917 | ` 48 μmol g–1 h–1 of CH4 an` | oui |
| PMC9631917 | `.12 μmol g–1 h–1) are rele` | oui |
| PMC9631917 | `0.8 μmol g–1 h–1 of CO are` | oui |
| PMC9631917 | `022 × 1023 mol–1).CO2 conv` | non |
| PMC9631917 | `1.2 μmol g–1 h–1 of CH4 ar` | oui |
| PMC9631917 | `11, and 632 cm–1 can be cl` | oui |
| PMC9631917 | `293 μmol g–1 h–1. From eq ` | non |
| PMC9631917 | `3.1 μmol g–1 h–1 of CH3OH,` | oui |
| PMC9631917 | `39, and 686 cm–1 correspon` | oui |
| PMC9631917 | `6.1 μmol g–1 h–1, respecti` | oui |
| PMC9631917 | `8.5 μmol g–1 h–1 of CO, 3.` | oui |
| PMC9631917 | `CO, 3.1 μmol g–1 h–1 of CH` | oui |
| PMC9631917 | `O (0.12 μmol g–1 h–1) are ` | oui |
| PMC9631917 | `O7, 8.5 μmol g–1 h–1 of CO` | oui |
| PMC9631917 | `TNT, 17 μmol g–1 h–1 of CH` | oui |
| PMC9631917 | `TNT, 48 μmol g–1 h–1 of CH` | oui |
| PMC9631917 | `and 0.8 μmol g–1 h–1 of CO` | oui |
| PMC9631917 | `and 1.2 μmol g–1 h–1 of CH` | oui |
| PMC9631917 | `and 6.1 μmol g–1 h–1, resp` | oui |
| PMC9631917 | `ated at 135 cm–1 attribute` | oui |
| PMC9631917 | `band at 890 cm–1 is accred` | non |
| PMC9631917 | `be 1293 μmol g–1 h–1. From` | oui |
| PMC9631917 | `cies at 195 cm–1, correspo` | oui |
| PMC9631917 | `ered at 600 cm–1 is attrib` | non |
| PMC9631917 | `int at 1640 cm–1 correspon` | non |
| PMC9631917 | `red at 3400 cm–1.29 The fi` | non |
| PMC9631917 | `s 188.4 μmol g–1 for CH4 (` | oui |
| PMC9631917 | `t of 48 μmol g–1 h–1 and 0` | oui |
| PMC9651130 | ` p = 1.47 × 10−27 (blue), p` |  |
| PMC9651130 | ` p = 3.03 × 10−4 (green)].` |  |
| PMC9651130 | ` p = 6.98 × 10−4 (green); ` |  |
| PMC9651130 | ` p = 7.59 × 10−10 (blue), p` |  |
| PMC9651130 | `7-AAD (1 mg mL−1 in dimeth` |  |
| PMC9667963 | `band at 570 cm−1 is observ` | oui |
| PMC9667963 | `ity at 1050 cm−1 correspon` | non |
| PMC9667963 | `peak at 960 cm−1 caused by` | non |
| PMC9667963 | `so = 0.4 cm3 g−1) (Fig. S3` | oui |
| PMC9685500 | ` (1 mL, 1 × 10−2 M) with t` | oui |
| PMC9685500 | ` (1 mL, 1 × 10−3 M), some ` | non |
| PMC9685500 | `1.0133 × 105 M−1, and the ` | oui |
| PMC9685500 | `aks at 1110 cm−1 are cause` | oui |
| PMC9685500 | `aks at 1637 cm−1 and 962 c` | oui |
| PMC9685500 | `aks at 2925 cm−1 and 2854 ` | oui |
| PMC9685500 | `ars at 3438 cm−1 is ascrib` | oui |
| PMC9685500 | `eaks of 465 cm−1 and 800 c` | oui |
| PMC9685500 | `ing at 1448 cm−1 are cause` | oui |
| PMC9685500 | `m−1 and 800 cm−1 are assig` | oui |
| PMC9685500 | `m−1 and 962 cm−1 belong to` | oui |
| PMC9685500 | `of 1.925 mg mL−1.2.6Synthe` | non |
| PMC9685500 | `of 400–4000 cm−1 were obta` | non |
| PMC9685500 | `−1 and 2854 cm−1 are relat` | oui |
| PMC9695608 | ` cm−1, ~450 cm−1, and ~320` |  |
| PMC9695608 | ` × 109 A m−1 s−1 []. The h` |  |
| PMC9695608 | ` ≤ 5 × 109 A m−1 s−1 []. T` |  |
| PMC9695608 | `0 cm−1, 280 cm−1 and 712 c` |  |
| PMC9695608 | `1, and ~320 cm−1, respecti` |  |
| PMC9695608 | `200 grooves mm−1. The exci` |  |
| PMC9695608 | `around ~670 cm−1, ~450 cm−` |  |
| PMC9695608 | `ge 100–1000 cm−1. The aver` |  |
| PMC9695608 | `m−1 and 712 cm−1 [], possi` |  |
| PMC9695608 | `ved at ~150 cm−1, 280 cm−1` |  |
| PMC9696917 | ` 43.6 mg CGA g−1 DW, with ` |  |
| PMC9696917 | ` 43.6 mg CGA g−1 DW, with ` |  |
| PMC9696917 | ` 50.1 mg CGA g−1 DW, with ` |  |
| PMC9696917 | ` MeOH) mg CE g−1 DW, which` |  |
| PMC9696917 | `16.46 mg CGA g−1, respecti` |  |
| PMC9696917 | `Cl3 (20 mmol L−1). The thr` |  |
| PMC9696917 | `d as mg CGA mL−1.3.7.3. AB` |  |
| PMC9696917 | `ed as mg CGA g−1.3.8. Scan` |  |
| PMC9696917 | `erial (mg CE g−1).3.7. Eva` |  |
| PMC9696917 | `fer (0.3 mol L−1; pH 3.6),` |  |
| PMC9696917 | `ivalents per g−1 of Hyssop` |  |
| PMC9696917 | `n in 10 mmol L−1 of HCl, a` |  |
| PMC9696917 | `rial (mg CGA g−1).3.6. Det` |  |
| PMC9696917 | `rial (mg CGA g−1).3.7.2. T` |  |
| PMC9696917 | `to 7.3 mg CE g−1 DW (Figur` |  |
| PMC9713890 | `524 and 676 cm–1 were due ` | non |
| PMC9713890 | `60 and 1134 cm–1 were due ` | non |
| PMC9713890 | `63 and 3550 cm–1 referred ` | oui |
| PMC9740727 | ` DSC (10 K·min−1), and ana` | non |
| PMC9740727 | ` even 1564 J·g−1, which al` | non |
| PMC9740727 | ` from 1173 J·g−1 to even 1` | oui |
| PMC9740727 | ` from 1173 J·g−1 to even a` | oui |
| PMC9740727 | `, 238.6 kJ·mol−1 [] and 20` | oui |
| PMC9740727 | `, 383.6 kJ·mol−1 [], 238.6` | oui |
| PMC9740727 | `1 and 20 K·min−1 are [209.` | oui |
| PMC9740727 | `at 500–1500 cm−1 are the p` | oui |
| PMC9740727 | `d 205.4 kJ·mol−1 [], respe` | oui |
| PMC9740727 | `e of 10 °C·min−1 were test` | oui |
| PMC9740727 | `eak at 1579 cm−1 is the st` | oui |
| PMC9740727 | `eak at 2925 cm−1 is the as` | oui |
| PMC9740727 | `ely 190 kJ·mol−1 lower tha` | oui |
| PMC9740727 | `ely 190 kJ·mol−1 when comp` | non |
| PMC9740727 | `gh as 1564 J·g−1, which al` | non |
| PMC9740727 | `in−1, 10 K·min−1 and 20 K·` | oui |
| PMC9740727 | `low as 5 K·min−1.To invest` | non |
| PMC9740727 | `min−1, 5 K·min−1, 10 K·min` | oui |
| PMC9740727 | `ons (10 °C·min−1), 2 wt% Z` | non |
| PMC9740727 | `peak at 752 cm−1 is the st` | oui |
| PMC9740727 | `rea (1500 m2·g−1) and high` | non |
| PMC9740727 | `s 211.7 kJ·mol−1 [], 383.6` | oui |
| PMC9740727 | `s of 2.5 K·min−1 and 5 K·m` | oui |
| PMC9740727 | `s of 2.5 K·min−1, 5 K·min−` | oui |
| PMC9740727 | `t of 2.39 kJ·g−1 (increase` | non |
| PMC9740727 | `−1 and 5 K·min−1 are the s` | oui |
| PMC9777915 | `029 to 2928 cm−1, ascribed` | non |
| PMC9777915 | `2, and 2878 cm−1, which ar` | non |
| PMC9777915 | `377 to 1378 cm−1 was assig` | non |
| PMC9777915 | `400 to 1600 cm−1 attribute` | non |
| PMC9777915 | `50 and 1580 cm−1 is attrib` | non |
| PMC9777915 | `51 and 1342 cm−1 may be at` | non |
| PMC9777915 | `633 to 3446 cm−1 and 3029 ` | non |
| PMC9777915 | `647 to 1644 cm−1, correspo` | non |
| PMC9777915 | `681 and 983 cm−1 [].3.10. ` | non |
| PMC9777915 | `939 to 1195 cm−1 is corres` | non |
| PMC9777915 | `band at 991 cm−1 (Si-O-Al ` | oui |
| PMC9777915 | `eak at 1567 cm−1 correspon` | non |
| PMC9777915 | `eak at 1780 cm−1 appeared ` | oui |
| PMC9777915 | `of 400–4000 cm−1 (Thermo S` | oui |
| PMC9777915 | `sed to 3374 cm−1 after the` | non |
| PMC9777915 | `tic model (min−1); t: cont` | non |
| PMC9777915 | `was at 3359 cm−1 and decre` | non |
| PMC9778285 | ` MW and 475 cm−1 in SG cor` | oui |
| PMC9778285 | ` ZnO at 780 cm−1 and 650 c` | non |
| PMC9778285 | ` at 450/475 cm−1. Thus, th` | non |
| PMC9778285 | `. Below 677 cm−1, bands co` | non |
| PMC9778285 | `502 and 445 cm−1 were attr` | non |
| PMC9778285 | `7 cm−1, 785 cm−1, and 863 ` | non |
| PMC9778285 | `and at 1123 cm−1 was chara` | non |
| PMC9778285 | `ands at 783 cm−1 and 545 (` | non |
| PMC9778285 | `band at 435 cm−1 attribute` | non |
| PMC9778285 | `band at 450 cm−1 assigned ` | oui |
| PMC9778285 | `band at 578 cm−1 was assig` | non |
| PMC9778285 | `d 545 (552) cm−1 were attr` | non |
| PMC9778285 | `e 3600–2000 cm−1 region co` | non |
| PMC9778285 | `es: at 3428 cm−1 hydroxyl ` | oui |
| PMC9778285 | `gion at 463 cm−1 in MW and` | oui |
| PMC9778285 | `he 400–4000 cm−1 domain. T` | non |
| PMC9778285 | `he 600–1000 cm−1 range. Th` | non |
| PMC9778285 | `lder at 550 cm−1 and as sm` | non |
| PMC9778285 | `lder at 550 cm−1 was chara` | oui |
| PMC9778285 | `m−1 and 650 cm−1 in V:ZnO ` | non |
| PMC9778285 | `nds at 1045 cm−1 and 1070 ` | non |
| PMC9778285 | `nds at 1419 cm−1 and 1570 ` | non |
| PMC9778285 | `nts had a 4 cm−1 sensitivi` | non |
| PMC9778285 | `oup at 3410 cm−1 and the b` | non |
| PMC9778285 | `ps; at 1400 cm−1 and 1614 ` | oui |
| PMC9778285 | `ps; at 2924 cm−1 and 2853 ` | oui |
| PMC9778285 | `ring at 727 cm−1, 785 cm−1` | non |
| PMC9778285 | `rved at 677 cm−1, and the ` | non |
| PMC9778285 | `−1 and 1070 cm−1 were char` | non |
| PMC9778285 | `−1 and 1570 cm−1 were assi` | non |
| PMC9778285 | `−1 and 1614 cm−1, two smal` | oui |
| PMC9778285 | `−1 and 2853 cm−1 CH2 group` | oui |
| PMC9778285 | `−1, and 863 cm−1. Other re` | non |
| PMC9782101 | `-OH at 3417 cm−1 and 1057 ` |  |
| PMC9782101 | `C=O at 1708 cm−1 and 1396 ` |  |
| PMC9782101 | `eak at 1572 cm−1 represent` |  |
| PMC9782101 | `−1 and 1057 cm−1 indicate ` |  |
| PMC9782101 | `−1 and 1396 cm−1 indicate ` |  |
| PMC9795147 | `0.5 – 20 µg mL−1) []. The ` | non |
| PMC9795147 | `5 ± 0.67 µg mL−1, and tmax` | non |
| PMC9795147 | `50 – 700 ng mL−1) and it w` | non |
| PMC9795147 | `50 – 700 ng mL−1). The res` | non |
| PMC9795147 | `56 and 1293 cm−1 refer to ` | oui |
| PMC9795147 | `90 and 1560 cm−1 correspon` | oui |
| PMC9795147 | `Ds (0.15 mg mL−1) was mixe` | non |
| PMC9795147 | `H) and 2900 cm−1–CH groups` | oui |
| PMC9795147 | `MOD (100 µg mL−1) was prep` | non |
| PMC9795147 | `MOD (300 ng mL−1), it was ` | non |
| PMC9795147 | `OQ) 45.0 ng mL−1 as seen i` | non |
| PMC9795147 | `ear at 3410 cm−1 and 2900 ` | oui |
| PMC9795147 | `f 50–700 ng mL−1, with a c` | non |
| PMC9795147 | `hat 0.15 mg mL−1 (1.0 mL) ` | non |
| PMC9795147 | `n of 100 µg mL−1. Then the` | non |
| PMC9795147 | `n of 100 µg mL−1.For conte` | non |
| PMC9795147 | `nd 500.0 ng mL−1). Accordi` | non |
| PMC9795147 | `nd 700.0 ng mL−1) were emp` | non |
| PMC9795147 | `ue 14.85 ng mL−1 and limit` | non |
| PMC9795147 | `± 10.4 µg.h mL−1. The resu` | non |
| PMC9795147 | `−1 and 2900 cm−1 correspon` | oui |
| PMC9824576 | `146 and 994 cm−1 are from ` |  |
| PMC9824576 | `eak at 1564 cm−1 is relate` |  |
| PMC9824576 | `eak at 2923 cm−1 is attrib` |  |
| PMC9824576 | `eak at 3132 cm−1 is derive` |  |
| PMC9824576 | `of 4000–400 cm−1. The tran` |  |
| PMC9824576 | `peak at 423 cm−1 is relate` |  |
| PMC9844074 | ` from 0.25 g L−1 to 1 g L−` | oui |
| PMC9844074 | ` from 0.25 g L−1 to 1 g L−` | oui |
| PMC9844074 | ` mL of 3 mol L−1 nitric ac` | oui |
| PMC9844074 | ` of 0.8 mL min−1. Separati` | non |
| PMC9844074 | ` to 0.0068 min−1 by adding` | non |
| PMC9844074 | ` to 0.0068 min−1. The phot` | non |
| PMC9844074 | ` to 0.0092 min−1, when the` | non |
| PMC9844074 | ` to 26.22 m2 g−1 without a` | oui |
| PMC9844074 | ` using 20 mg L−1 concentra` | oui |
| PMC9844074 | `BFO (8.45 m2 g−1). The obs` | non |
| PMC9844074 | `ation (20 mg L−1) of ibupr` | non |
| PMC9844074 | `be 0.016 cm3 g−1 and 0.032` | oui |
| PMC9844074 | `from 8.45 m2 g−1 to 26.22 ` | oui |
| PMC9844074 | `g L−1 to 1 g L−1. The over` | oui |
| PMC9844074 | `g L−1 to 1 g L−1. The pH o` | oui |
| PMC9844074 | `nd 0.032 cm3 g−1, respecti` | oui |
| PMC9844074 | `rom 0.0015 min−1 to 0.0068` | oui |
| PMC9844074 | `rom 0.0015 min−1 to 0.0068` | oui |
| PMC9844074 | `rom 0.0064 min−1 to 0.0092` | non |
| PMC9844074 | `was 26.22 m2 g−1, which wa` | oui |
| PMC9858013 | `26 and 1433 cm−1 appear in` |  |
| PMC9858013 | `3, and 1021 cm−1, respecti` |  |
| PMC9858013 | `59, and 788 cm−1 that are ` |  |
| PMC9858013 | `CH3 at 2884 cm−1 intensifi` |  |
| PMC9862409 | `47 and 1675 cm−1 for C=O o` |  |
| PMC9862409 | `69 and 2933 cm−1, carbonyl` |  |
| PMC9862409 | `78 and 2853 cm−1 for aliph` |  |
| PMC9862409 | `O–C at 1102 cm−1 []. The a` |  |
| PMC9862409 | `ength (1638 cm−1). Ultimat` |  |
| PMC9862409 | `group, 3057 cm−1 for aroma` |  |
| PMC9862409 | `ing at 1303 cm−1, and symm` |  |
| PMC9862409 | `ing at 1401 cm−1, C–O stre` |  |
| PMC9862409 | `ing at 1463 cm−1, C–N stre` |  |
| PMC9862409 | `ing at 1667 cm−1, C=C stre` |  |
| PMC9862409 | `nds at 3361 cm−1 for –NH g` |  |
| PMC9862409 | `t 3600–3299 cm−1, aliphati` |  |
| PMC9865864 | ` is 2.16 mg cm−2, in order` | oui |
| PMC9865864 | `2 mL (10 mg mL−1) GO dispe` | oui |
| PMC9865864 | `F g−1 at 2 A g−1 and an ex` | oui |
| PMC9865864 | `O-6 at 100 A g−1 are super` | non |
| PMC9865864 | `and at 1120 cm−1 together ` | oui |
| PMC9865864 | `ate of 20° min−1. PL spect` | non |
| PMC9865864 | `bout 0.8 mg cm−2, and that` | oui |
| PMC9865864 | `e with 230 F g−1 at 100 A ` | oui |
| PMC9865864 | `g of 1.0 mg cm−2. Finally,` | non |
| PMC9865864 | `ges from 1 A g−1 to 100 A ` | non |
| PMC9865864 | `g−1 at 100 A g−1 (only ~20` | non |
| PMC9865864 | `g−1 is 271 F g−1, which is` | oui |
| PMC9865864 | `g−1 to 100 A g−1). This pr` | non |
| PMC9865864 | `g−1 to 100 A g−1, the spec` | oui |
| PMC9865864 | `g−1 to 100 A g−1, the spec` | oui |
| PMC9865864 | `g−1 to 230 F g−1 with a ca` | oui |
| PMC9865864 | `lue of 550 F g−1; this maj` | non |
| PMC9865864 | `nce of 271 F g−1 at 2 A g−` | oui |
| PMC9865864 | `nce to 645 F g−1 []. Duan ` | non |
| PMC9865864 | `nds at 1597 cm−1 and 2347 ` | oui |
| PMC9865864 | `nds at 3420 cm−1 and 1520 ` | oui |
| PMC9865864 | `nsity of 2 A g−1 (Figure 3` | non |
| PMC9865864 | `nsity of 2 A g−1 is 271 F ` | oui |
| PMC9865864 | `of 100–200 F g−1, much low` | non |
| PMC9865864 | `rea (2630 m2 g−1), excelle` | non |
| PMC9865864 | `s from 271 F g−1 to 230 F ` | oui |
| PMC9865864 | `sed from 2 A g−1 to 100 A ` | oui |
| PMC9865864 | `ses from 2 A g−1 to 100 A ` | oui |
| PMC9865864 | `trodes (71 F g−1). Moreove` | non |
| PMC9865864 | `vity (~107 S m−1) and good` | non |
| PMC9865864 | `−1 and 1520 cm−1 were assi` | oui |
| PMC9865864 | `−1 and 2347 cm−1 were assi` | oui |
| PMC9866506 | ` HF, PF6, HCO3−1, etc.) de` | oui |
| PMC9866506 | ` HF, PF6, HCO3−1, etc.) de` | oui |
| PMC9866506 | ` HF, PF6, HCO3−1, etc.) de` | oui |
| PMC9866506 | `1 and 175 mAhg−1, justify ` | non |
| PMC9866506 | `11, and 267 cm−1 correspon` | non |
| PMC9866506 | `1179/1125 mAhg−1 at the cu` | non |
| PMC9866506 | `17, and 948 cm−1, respecti` | non |
| PMC9866506 | `21, and 817 cm−1 were asso` | non |
| PMC9866506 | `23/771.69 mAhg−1, 730.70/4` | oui |
| PMC9866506 | `40/488.45 mAhg−1, and 1080` | oui |
| PMC9866506 | `60, and 450 cm−1 determine` | non |
| PMC9866506 | `62/661.84 mAhg−1, 737.40/4` | oui |
| PMC9866506 | `63/945.17 mAhg−1, respecti` | oui |
| PMC9866506 | `70/455.99 mAhg−1, and 686.` | oui |
| PMC9866506 | `85/367.53 mAhg−1, respecti` | oui |
| PMC9866506 | `ate of 0.1 mVs−1, respecti` | non |
| PMC9866506 | `ately 700 mAhg−1 with 100%` | non |
| PMC9866506 | `ce) at 0.1 mVs−1 in a volt` | oui |
| PMC9866506 | `de Fe+3 and VO−3 ions in a` | non |
| PMC9866506 | `es of 378 mAhg−1 and 175 m` | non |
| PMC9866506 | `eving 578 mAhg−1 as an ano` | non |
| PMC9866506 | `f 1378.82 mAhg−1 at the C-` | non |
| PMC9866506 | `f ~1255.5 mAhg−1 and can b` | non |
| PMC9866506 | `ity (>600 mAhg−1), safety,` | oui |
| PMC9866506 | `ity of 100 mAg−1 []. FeVO4` | non |
| PMC9866506 | `ity of 100 mAg−1 after 250` | non |
| PMC9866506 | `ity of 100 mAg−1 for 50 cy` | non |
| PMC9866506 | `ity of 100 mAg−1 for 50 cy` | non |
| PMC9866506 | `ity of 100 mAg−1 up to 50 ` | non |
| PMC9866506 | `ity of 100 mAg−1 within th` | oui |
| PMC9866506 | `of 1046.5 mAhg−1 after 100` | non |
| PMC9866506 | `y of 1200 mAhg−1 for LIBs,` | non |
| PMC9878544 | ` FA at 1693 cm–1 that can ` |  |
| PMC9878544 | `0, and 1585 cm–1 can be re` |  |
| PMC9878544 | `1, 0.653 cm3 g–1, and 19.2` |  |
| PMC9878544 | `e 1353.23 m2 g–1, 0.653 cm` |  |
| PMC9878544 | `eak at 1028 cm–1 can be re` |  |
| PMC9878544 | `eak at 1750 cm–1 indicated` |  |
| PMC9878544 | `f 3200–3600 cm–1 can be re` |  |
| PMC9878544 | `nd 100.0 μg mL–1 of differ` |  |
| PMC9878544 | `ning 0.5 mg mL–1 of MTT so` |  |
| PMC9878544 | `te of 5 °C min–1. BET anal` |  |
| PMC9912144 | `(HL, 100 mW cm−2), simulat` | oui |
| PMC9912144 | `.A), 100 mW cm−2), and sun` | oui |
| PMC9912144 | `7, and 1540 cm−1, which ch` | non |
| PMC9912144 | `NRs (1.4 μA cm−2 at 0.3 V ` | oui |
| PMC9912144 | `around 3460 cm−1 correspon` | non |
| PMC9912144 | `d at 4.9 μA cm−2 at 0.3 V ` | oui |
| PMC9912144 | `e near 1630 cm−1, the loca` | non |
| PMC9912144 | `rom 400–600 cm−1 are typic` | non |
| PMC9929317 | ` and 0.01 min −1 for biosy` | oui |
| PMC9929317 | ` and 1052.6 cm−1 are due t` | non |
| PMC9929317 | ` and 2980.5 cm−1 are relat` | non |
| PMC9929317 | `, and 809.7 cm−1. The band` | non |
| PMC9929317 | `4000 to 400 cm−1. FTIR spe` | non |
| PMC9929317 | `ak at 809.7 cm−1 is assign` | non |
| PMC9929317 | `ed at 452.3 cm−1 are produ` | non |
| PMC9929317 | `hat at 1400 cm−1 correspon` | oui |
| PMC9929317 | `k at 1113.1 cm−1 is attrib` | oui |
| PMC9929317 | `k at 3668.7 cm−1 is due to` | non |
| PMC9929317 | `of 400–4000 cm−1 in order ` | non |
| PMC9929317 | `ound 3505.3 cm−1 correspon` | non |
| PMC9929317 | `reaction (min −1), and t i` | non |
| PMC9929317 | `ues 0.005 min −1 for chem ` | oui |
| PMC9958088 | ` at 500–400 cm−1 was ascri` | oui |
| PMC9958088 | `at 1000–900 cm−1 is the as` | non |
| PMC9958088 | `d 1700–1600 cm−1 are the s` | oui |
| PMC9958088 | `dron at 712 cm−1, which is` | non |
| PMC9958088 | `fted to 996 cm−1, which wa` | non |
| PMC9958088 | `lution of 2 cm−1 with 32 s` | non |
| PMC9958088 | `peak at 874 cm−1, which wa` | oui |
| PMC9958088 | `peak at 984 cm−1 shifted t` | oui |
| PMC9958088 | `t 1500–1400 cm−1 is the C–` | oui |
| PMC9958088 | `t 3500–3400 cm−1 and 1700–` | oui |
| PMC9960931 | ` at 620–400 cm−1 were note` | non |
| PMC9960931 | ` mL of 1 mol L−1 sodium hy` | oui |
| PMC9960931 | ` of 0.24 cm3 g−1, suggesti` | non |
| PMC9960931 | ` of 10–37 m2 g−1 typical o` | non |
| PMC9960931 | ` ~3650–3200 cm−1 range cor` | non |
| PMC9960931 | `0, and 2851 cm−1, bands ar` | non |
| PMC9960931 | `2, and 18 m2 g−1 displayed` | non |
| PMC9960931 | `SBET = 10 m2 g−1, which, d` | oui |
| PMC9960931 | `ZnO7.5–14 m2 g−1, ZnO8.0–1` | non |
| PMC9960931 | `ZnO8.0–10 m2 g−1, ZnO8.5–1` | non |
| PMC9960931 | `ZnO8.5–12 m2 g−1, and ZnO1` | non |
| PMC9960931 | `and at ~570 cm−1 originati` | oui |
| PMC9960931 | `e 1632–1571 cm−1 range cor` | non |
| PMC9960931 | `e of 9–21 m2 g−1, where th` | oui |
| PMC9960931 | `e: 4000–400 cm−1, resoluti` | oui |
| PMC9960931 | `ent to 27 m2 g−1 and 25 m2` | non |
| PMC9960931 | `ext, a 1 mol L−1 sodium hy` | oui |
| PMC9960931 | `he 1042–812 cm−1 range ass` | oui |
| PMC9960931 | `lution: 0.5 cm−1, and the ` | oui |
| PMC9960931 | `m mode (7 × 10−4 Pa; RT), ` | oui |
| PMC9960931 | `mber of 403 cm−1, a band a` | non |
| PMC9960931 | `nO11.0–16 m2 g−1. Samples ` | non |
| PMC9960931 | `rea of 37 m2 g−1 and pore ` | non |
| PMC9960931 | `ted at 1410 cm−1 and 1386 ` | non |
| PMC9960931 | `−1 and 1386 cm−1, suggesti` | non |
| PMC9960931 | `−1 and 25 m2 g−1, for ZnO1` | non |
| PMC9972853 | `, and 20 μg mL−1, respecti` |  |
| PMC9972853 | `HCl. 200 μg mL−1 146S in P` |  |
| PMC9972853 | `L of 200 μg mL−1 146S with` |  |
| PMC9972853 | `The peaks ν/cm−1 1110 (C–N` |  |
| PMC9972853 | `d to 200 μg mL−1 and then ` |  |
| PMC9972853 | `ining 40 μg mL−1 146S) wer` |  |
| PMC9972853 | `m 20–200 μg mL−1. The cell` |  |
| PMC9972853 | `n at 200 μg mL−1 of 146S@Z` |  |
| PMC9972853 | `peak at 420 cm−1 revealed ` |  |
| PMC9972853 | `te of 1 °C min−1 from 25 °` |  |
| PMC9972853 | `tion peak ν/cm−1 1651 (C ` |  |
| PMC9999475 | ` over 3–10.5 Å–1 after app` |  |
| PMC9999475 | `LMOF (68 mAh g–1). In the ` |  |
| PMC9999475 | `MOF (178 mAh g–1). However` |  |
| PMC9999475 | `VOF (188 mAh g–1) than for` |  |
| PMC9999475 | `VOF (213 mAh g–1). LMOF al` |  |
| PMC9999475 | `about 93 mAh g–1, which co` |  |
| PMC9999475 | `les (144 mAh g–1) was sign` |  |
| PMC9999475 | `step of 0.03 Å–1 for the p` |  |
| PMC9999475 | `th R bkg = 1 Å–1 in the k ` |  |
| PMC9999475 | `y of 215 mAh g–1, which is` |  |
