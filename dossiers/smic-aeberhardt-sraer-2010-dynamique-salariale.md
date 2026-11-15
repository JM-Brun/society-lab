# Audit — Aeberhardt & Sraer (2010) : allègements et dynamique salariale (1994–1997)

- **Référence :** Romain Aeberhardt et David Sraer, « Allègements de cotisations patronales et dynamique salariale », *Économie et Statistique*, n°429–430, pp. 177–189 (numéro référencé 2009, publié en août 2010), DOI [10.3406/estat.2009.8068](https://doi.org/10.3406/estat.2009.8068).
- **Texte intégral :** [PDF BnSP/INSEE](https://www.bnsp.insee.fr/ark:/12148/bc6p070n3rp.pdf) ; [notice Persée](https://www.persee.fr/doc/estat_0336-1454_2009_num_429_1_8068) ; [version de travail INSEE G2007/01](https://www.insee.fr/fr/statistiques/1380699).
- **Nature de la preuve :** deux stratégies quasi-expérimentales (différence de différences et régression sur discontinuité) appliquées à la progression salariale, et non à l'emploi net. Période étudiée : première vague d'allègements 1994–1997.

## 1. Question et contexte

Les allègements patronaux peuvent créer une « trappe à bas salaires » : une hausse du salaire brut réduit l'exonération et augmente donc le coût marginal pour l'employeur. Les auteurs testent si les salariés éligibles aux allègements ont connu une progression salariale inférieure à celle de salariés proches mais non éligibles.

L'étude se concentre sur la première vague de dispositifs et ne couvre pas les extensions ultérieures ni le régime contemporain.

## 2. Données et échantillon

- **Source :** déclarations annuelles de données sociales (DADS) exhaustives, 1994–1997.
- **Population :** salariés du secteur privé à temps complet ayant travaillé toute l'année dans la même entreprise pendant deux années consécutives.
- **Exclusions :** temps partiel, mobilités entre entreprises dans la fenêtre d'observation ; l'article explique que les variables d'heures et les allègements spécifiques au temps partiel compliqueraient l'identification.
- **Groupes :** salariés dont le salaire initial est compris entre 1,2 et 1,33 SMIC (éligibles aux allègements après leur montée en charge) et salariés entre 1,33 et 1,5 SMIC (non éligibles).
- **Effectif :** 1 822 894 observations individuelles sur les quatre années, dont 215 328 en 1994, 519 075 en 1995, 521 873 en 1996 et 566 618 en 1997. Les auteurs signalent un problème d'échantillonnage en 1994 et une qualité incomplète des heures en 1993.
- **Résultat mesuré :** progression annuelle du salaire brut individuel, non l'emploi, les heures ni le salaire net disponible.

Les individus doivent rester dans le même établissement entre t−1 et t pour être appariés ; les auteurs reconnaissent que les mobilités, souvent associées à des primes salariales, sont exclues.

## 3. Stratégie 1 — différence de différences

Le groupe traité est celui des salariés entre 1,2 et 1,33 SMIC, le groupe témoin celui entre 1,33 et 1,5 SMIC. En 1994, aucun groupe n'est touché par le barème considéré ; entre 1995 et 1997, l'intensité des allègements augmente pour le groupe inférieur.

Les auteurs estiment successivement :
1. une spécification avec effets annuels et indicatrice de groupe ;
2. l'ajout de l'âge, du sexe et des secteurs ;
3. l'ajout d'effets fixes d'entreprise.

La progression salariale moyenne du groupe inférieur dépasse celle du groupe supérieur de 0,3 point en 1994, puis de 0,5 point en 1995 et 1996, et de 0,6 point en 1997. Les différences de différences indiquent un avantage relatif du groupe éligible de 0,2 point entre 1994 et 1995, 0,2 point entre 1994 et 1996 et 0,3 point entre 1994 et 1997. Les résultats restent positifs et significatifs dans les trois spécifications, avec des effets fixes d'entreprise.

**Interprétation des auteurs :** les salariés concernés par les allègements n'ont pas connu de progression salariale inférieure ; le différentiel est même très légèrement en leur faveur.

### Hypothèse d'identification et fragilité

L'hypothèse causale est que, sans les allègements, l'écart de progression entre les deux groupes aurait évolué comme avant la réforme. Cela suppose notamment que les changements macroéconomiques nouveaux affectent les deux groupes de façon comparable.

Les auteurs discutent explicitement la diffusion des hausses du SMIC : les salariés sous 1,33 SMIC peuvent être davantage concernés. Ils estiment que cette diffusion ne suffit pas à expliquer le différentiel observé, mais cette correction repose sur une approximation tirée d'autres travaux. Autre limite : le groupe de contrôle entre 1,33 et 1,5 SMIC peut lui-même subir un effet d'équilibre général si les allègements déplacent la demande relative de travail non qualifié et qualifié. Le différentiel DiD peut alors surestimer l'effet direct favorable au groupe traité.

## 4. Stratégie 2 — régression sur discontinuité au seuil de 1,33 SMIC

Les auteurs exploitent le seuil au-delà duquel les allègements disparaissent. Ils comparent les augmentations de salaire des personnes juste en dessous et juste au-dessus du seuil, année par année.

Trois fenêtres sont utilisées :
- [1,2 ; 1,5] SMIC ;
- [1,28 ; 1,38] SMIC ;
- [1,30 ; 1,36] SMIC.

Trois spécifications sont estimées : sans contrôles, avec caractéristiques individuelles/secteur, puis avec effets fixes d'entreprise.

Le résultat essentiel est que l'effet favorable observé dans la spécification la plus simple diminue avec la réduction de la fenêtre et **n'est plus statistiquement significatif après ajout des contrôles** dans les fenêtres étroites. Les tests de 1994, avant le seuil de 1,33 SMIC, ne révèlent pas de différence significative.

**Interprétation :** au voisinage du seuil, les auteurs ne trouvent pas de preuve d'une pénalité salariale liée aux allègements. Mais le résultat est local et ne peut pas être extrapolé aux salariés plus éloignés du seuil.

## 5. Conclusion des auteurs

Les deux méthodes ne mettent pas en évidence de ralentissement de la progression salariale des salariés concernés par les allègements entre 1994 et 1997. La DiD trouve même un petit différentiel positif en faveur des bénéficiaires ; la RDD, plus locale, conclut à l'absence d'effet négatif significatif après contrôles.

Les auteurs rappellent cependant que l'étude ne porte que sur le court et moyen terme. Ils évoquent un possible effet de long terme sur les rendements de la formation professionnelle, qui n'est pas évalué ici.

## 6. Évaluation critique

**Forces :**
- exploitation de données administratives exhaustives ;
- groupe de comparaison proche en salaire initial ;
- deux stratégies d'identification différentes, dont une approche locale autour d'un seuil explicite ;
- contrôles sectoriels et effets fixes d'entreprise ;
- discussion explicite de la diffusion du SMIC et des effets d'équilibre général.

**Limites :**
1. La DiD dépend de l'hypothèse de tendances parallèles ; l'article ne présente pas de longue série de pré-tendances ou d'étude événementielle permettant de la vérifier finement.
2. Le groupe de contrôle peut subir des effets indirects des allègements (substitution entre qualifications), ce qui contamine le contrefactuel.
3. Le groupe traité reçoit aussi les effets de diffusion des revalorisations du SMIC ; la correction de ce phénomène est approximative.
4. La RDD n'est pas un effet moyen : elle identifie au mieux un effet local autour de 1,33 SMIC. La significativité disparaît avec les contrôles et fenêtres resserrées.
5. Le champ exclut les temps partiels et les mobilités ; il ne renseigne pas les trajectoires des personnes changeant d'entreprise ou sortant de l'emploi.
6. La variable de résultat est le salaire brut individuel, pas le revenu disponible, les heures, l'emploi ou les créations nettes.
7. Les conclusions concernent les dispositifs de 1994–1997 et ne sont pas directement transposables aux barèmes ultérieurs.

**Niveau de preuve :** modéré pour l'absence de forte pénalité salariale à court/moyen terme parmi les salariés à temps complet restant dans le même établissement ; plus limité pour un effet causal moyen généralisable. L'étude ne répond pas à la question de l'effet d'une hausse isolée du SMIC sur l'emploi.

## 7. Synthèse opérationnelle

- **Résultat central :** les allègements de 1994–1997 n'ont pas été associés à une progression salariale plus faible des salariés éligibles ; la DiD trouve même un léger différentiel positif de 0,2–0,3 point par rapport au groupe voisin.
- **Robustesse :** la RDD autour de 1,33 SMIC ne met pas en évidence de pénalité après contrôles ; l'effet simple s'efface quand la fenêtre se resserre et que les caractéristiques sont contrôlées.
- **Portée :** cela tempère l'hypothèse d'une trappe salariale immédiate généralisée sur cette première vague d'allègements.
- **Réserve :** cette conclusion ne réfute pas les effets de long terme, les effets sur les mobilités, la formation, les salaires à l'embauche ou d'autres périodes.
- **Lien avec le dossier SMIC :** les revalorisations du SMIC sont un facteur de diffusion salariale qui doit être séparé des effets des exonérations. Cette étude contrôle et discute ce mécanisme, mais n'est pas une évaluation de la hausse du SMIC elle-même.

## 8. Sources

- Aeberhardt & Sraer (2010), texte intégral dans le numéro *Économie et Statistique* n°429–430 : https://www.bnsp.insee.fr/ark:/12148/bc6p070n3rp.pdf
- Persée, notice : https://www.persee.fr/doc/estat_0336-1454_2009_num_429_1_8068
- INSEE, version de travail G2007/01 : https://www.insee.fr/fr/statistiques/1380699
