# Fiche d'audit — Benyamina & Stutzmann (2025), trajectoires salariales des salariés au SMIC

- **Référence :** Rania Benyamina et Chloé Stutzmann, *Wage Trajectories of French Minimum Wage Earners*, Trésor-Éco n° 365, Direction générale du Trésor, juin 2025.
- **Source primaire :** [PDF intégral (12 pages)](https://www.tresor.economie.gouv.fr/Articles/06d82898-9d76-4539-8b29-53ba0f35e393/files/9efa8621-fcbc-4720-9e53-5f7d073bc32a) ; [notice officielle](https://www.tresor.economie.gouv.fr/Articles/2025/06/12/wage-trajectories-of-french-minimum-wage-earners).
- **Statut :** lecture du document primaire, des tableaux 1 à 3, de l'encadré méthodologique, des cinq groupes de trajectoires et de l'encadré COVID-19.
- **Question :** les salariés proches du SMIC en 2013 progressent-ils durablement dans la hiérarchie salariale, restent-ils proches du plancher ou connaissent-ils des épisodes de chômage et de non-observation ?
- **Avertissement central :** étude longitudinale descriptive de mobilité salariale ; elle ne mesure pas l'effet causal des revalorisations du SMIC sur les trajectoires.

## 1. Données et champ

L'étude utilise le **Panel Tous salariés de l'INSEE** sur 2013–2021, construit à partir des DADS, des DSN et des fichiers de paie de la fonction publique. Il couvre environ un douzième des salariés, hors salariés agricoles, et inclut :
- secteur privé ;
- entreprises publiques ;
- fonction publique ;
- salariés employés par des particuliers.

Les personnes indemnisées au chômage apparaissent dans le panel lorsqu'elles ont connu au moins une période d'emploi l'année précédente. La base peut perdre de vue une personne en cas de passage à l'inactivité ou à la retraite, de chômage prolongé de plus d'un an, de passage au travail indépendant ou de départ à l'étranger. Les revenus éventuellement perçus hors champ ne sont alors pas observés.

Deux sous-échantillons sont tirés aléatoirement en 2013 :
- **échantillon tous salariés :** environ 30 000 personnes de 15 à 64 ans, représentatives selon l'âge, le sexe et le salaire horaire brut annuel moyen ;
- **échantillon salariés au SMIC :** environ 30 000 personnes tirées parmi les quelque 360 000 salariés du panel dont le salaire horaire brut annuel moyen est inférieur à 1,1 SMIC en 2013.

La définition de « salarié au SMIC » est donc **moins de 1,1 fois le SMIC**, et non exactement le SMIC légal. Le salaire horaire brut annuel moyen est calculé comme la rémunération brute totale annuelle divisée par le nombre d'heures travaillées sur l'année. Cette mesure tient compte des temps partiels et des périodes d'emploi discontinues, mais elle ne décrit pas le taux horaire contractuel à une date donnée.

## 2. Construction des statuts et méthodes

Pour chaque année, chaque individu reçoit un statut :
- **chômage :** indemnisé plus de six mois dans l'année (plus de 910 heures) ;
- **non observé :** totalement absent du panel pendant l'année ;
- sinon, une des cinq catégories de salaire moyen horaire brut :
  1. moins de 1,1 SMIC ;
  2. de 1,1 à moins de 1,6 SMIC ;
  3. de 1,6 à moins de 2,5 SMIC ;
  4. de 2,5 à moins de 3,5 SMIC ;
  5. au moins 3,5 SMIC.

Le document utilise deux méthodes complémentaires :
1. **matrice de transition annuelle** entre catégories de salaire, chômage et non-observation ;
2. **analyse séquentielle** des trajectoires, avec Optimal Matching puis classification hiérarchique ascendante (méthode de Ward), pour identifier cinq profils récurrents.

Une régression logistique multinomiale estime ensuite les caractéristiques associées à l'appartenance à chacun des groupes. Les coefficients du tableau 3 sont des **odds ratios**, pas des effets marginaux en points de probabilité.

## 3. Mobilité salariale 2013–2019 : résultats descriptifs

Dans l'échantillon tous salariés, la part des personnes sous 1,1 SMIC passe de 12 % en 2013 à 6 % en 2019. Plus d'un salarié sur cinq se trouve dans une tranche salariale supérieure à celle de 2013. Mais 22 % de l'échantillon initial ne sont plus observés en 2019.

Pour les personnes initialement sous 1,1 SMIC :
- **52 %** restent dans cette tranche l'année suivante ;
- **27 %** passent dans la tranche 1,1–1,6 SMIC ;
- **3 %** passent dans la tranche 1,6–2,5 SMIC ;
- **1 %** passent dans la tranche 2,5–3,5 SMIC ;
- **8 %** sont classés au chômage ;
- **9 %** ne sont plus observés.

Sur six ans, la moitié des salariés initialement sous 1,1 SMIC ont rejoint une tranche de salaire supérieure en 2019 ; près d'un quart ne sont plus observés et près de 8 % sont au chômage. Un peu plus de 1 % seulement sont restés chaque année dans la catégorie proche du SMIC sur toute la période.

La hausse médiane de rémunération entre 2013 et 2019 est de **36 %** pour les personnes initialement sous 1,1 SMIC, contre **14 %** pour celles initialement entre 2,5 et 3,5 SMIC. Cette comparaison est nominale et descriptive : elle ne mesure pas le gain réel, ne neutralise pas la composition par âge ou ancienneté et ne permet pas d'attribuer l'écart aux revalorisations du SMIC.

## 4. Cinq groupes de trajectoires parmi les salariés initialement proches du SMIC

La classification des trajectoires des quelque 30 000 salariés initialement sous 1,1 SMIC distingue :

| Groupe | Part | Profil |
|---|---:|---|
| Forte progression salariale | 13 % | Plus de 80 % atteignent au moins 1,6 SMIC en 2019 ; jeunes, cadres et temps plein surreprésentés |
| Progression modérée | 28 % | Près de 70 % passent quatre années ou plus entre 1,1 et 1,6 SMIC |
| Épisodes de chômage | 15 % | Plus des trois quarts connaissent au moins une année de chômage ; 11 % sont au chômage quatre ans ou plus entre 2014 et 2019 |
| Non-observation prolongée | 19 % | Sorties du champ diverses, dont retraite, inactivité, chômage prolongé, travail indépendant ou départ à l'étranger |
| Proximité durable du SMIC | 25 % | Plus de 90 % restent proches du minimum au moins quatre années sur la période ; 64 % sont encore dans cette situation en 2019 |

Il faut distinguer **proximité durable** et **présence au SMIC chaque année** : le groupe de 25 % inclut des personnes proches du plancher au moins quatre ans, pas nécessairement pendant les sept années consécutives. La proportion restant sous 1,1 SMIC tous les ans est bien plus faible (un peu plus de 1 %).

## 5. Qui reste durablement proche du SMIC ?

La régression logistique du tableau 3, toutes choses égales par ailleurs selon les variables incluses, associe la trajectoire de proximité durable à plusieurs caractéristiques :
- les femmes ont un odds ratio de **1,17** par rapport aux hommes ;
- les ouvriers et employés sont plus susceptibles de rester proches du SMIC que les catégories « autres », et beaucoup plus que les cadres ;
- les salariés des services ont un odds ratio de **2,2** par rapport à ceux de l'industrie et de **1,6** par rapport au commerce de détail.

L'âge joue aussi : les jeunes sont plus susceptibles de connaître une forte progression salariale, tandis que les 55–64 ans sont davantage exposés à la non-observation prolongée. L'ancienneté et le changement d'employeur sont également associés aux trajectoires.

Ces résultats décrivent une hétérogénéité de mobilité : la hausse médiane plus forte des salariés au SMIC en 2013 est en partie liée à leur composition, notamment la présence de jeunes en début de carrière. Elle ne signifie pas que chaque salarié au SMIC connaît une progression rapide.

## 6. Conjoncture et trajectoires : la crise de 2008 et la pandémie

Le document rappelle les résultats de l'étude DARES–DG Trésor (2018) sur 2005–2013 : pendant la crise de 2008, la probabilité qu'un salarié au SMIC soit au chômage cinq trimestres plus tard augmente de 2,5 points, contre 0,9 point pour l'ensemble des salariés. Pour les salariés au SMIC n'ayant pas connu le chômage, la probabilité de dépasser 1,05 SMIC cinq trimestres plus tard passe de 43 % avant la crise à 39 % après. Ces chiffres proviennent de l'étude 2018 citée, pas d'une identification causale de la présente étude.

### Encadré COVID-19 (2019–2021)

Un troisième échantillon d'environ 30 000 salariés est tiré en 2019. En 2020, 6 % connaissent une activité partielle pendant plus d'un quart de l'année ; 36 % de ces salariés sont encore en activité partielle en 2021.

Les salariés proches du SMIC en 2019 ont environ deux fois plus de risque de connaître l'activité partielle que ceux entre 1,6 et 2,5 SMIC, et trois fois plus que ceux entre 2,5 et 3,5 SMIC. Les auteurs ne détectent pas de différence apparente de progression salariale parmi ceux qui sortent de l'activité partielle, mais observent un risque de chômage supérieur : 12 % pour ceux sortant de l'activité partielle, contre 4 % pour ceux n'y ayant pas été.

Les auteurs qualifient ces résultats de préliminaires : la période est courte et les effets sectoriels de la pandémie sont difficiles à séparer. Il ne s'agit pas d'une estimation causale de l'effet de l'activité partielle ou du SMIC.

## 7. Tendances préalables et limites d'identification

Cette étude est une analyse de trajectoires et non une évaluation causale d'une revalorisation du SMIC :
1. aucun groupe témoin n'est construit pour isoler l'effet des hausses du SMIC ;
2. aucune stratégie de différence-de-différences ou d'étude d'événement ne compare des trajectoires préalables parallèles ;
3. les trajectoires sont influencées par l'âge, l'ancienneté, la qualification, le secteur, le temps partiel, la mobilité et la conjoncture ;
4. le seuil de 1,1 SMIC regroupe des situations différentes et peut être franchi à la suite d'une progression salariale, d'un changement d'heures ou de composition de la rémunération ;
5. le statut « non observé » agrège des sorties du champ hétérogènes et ne peut être assimilé automatiquement à l'inactivité ou au chômage ;
6. les personnes au chômage sont identifiées par l'indemnisation majoritaire, ce qui ne couvre pas tous les épisodes de chômage ;
7. la hausse médiane de 36 % est nominale et ne constitue pas une mesure du gain réel de pouvoir d'achat ;
8. la classification en cinq groupes dépend des choix de distance et de regroupement d'une analyse séquentielle ; elle est utile pour décrire les profils, pas pour identifier leurs causes.

## 8. Synthèse et niveau de preuve

**Constat principal :** la plupart des salariés initialement proches du SMIC ne restent pas durablement dans cette situation. Une part importante progresse, notamment les jeunes en début de carrière, mais une minorité substantielle (25 %) connaît une proximité durable du plancher. Les femmes, employés et salariés des services sont davantage représentés dans ce dernier groupe.

**Ce que l'étude apporte :**
- une mesure longitudinale des transitions entre tranches salariales, chômage et non-observation ;
- une distinction entre progression forte, progression modérée, chômage, sortie du champ et proximité durable du SMIC ;
- une mise en évidence de l'hétérogénéité des trajectoires selon le sexe, l'âge, la catégorie professionnelle et le secteur ;
- un rappel utile de l'importance de la conjoncture, notamment pendant la crise de 2008.

**Ce qu'elle ne permet pas d'affirmer :**
- que les hausses du SMIC ont causé les progressions salariales observées ;
- que le SMIC a provoqué ou empêché les épisodes de chômage ;
- que la progression nominale médiane de 36 % correspond à une hausse réelle équivalente ;
- que les salariés « non observés » sont tous inactifs ou au chômage.

**Niveau de confiance :**
- **élevé** pour les transitions descriptives dans les échantillons représentatifs retenus ;
- **modéré** pour les associations entre caractéristiques et groupes de trajectoires, conditionnelles aux variables du modèle ;
- **nul** pour une interprétation causale des revalorisations du SMIC.

## 9. Référence primaire

Benyamina, Rania & Chloé Stutzmann (2025), *Wage Trajectories of French Minimum Wage Earners*, Trésor-Éco n° 365, Direction générale du Trésor, juin 2025, [PDF intégral](https://www.tresor.economie.gouv.fr/Articles/06d82898-9d76-4539-8b29-53ba0f35e393/files/9efa8621-fcbc-4720-9e53-5f7d073bc32a).
