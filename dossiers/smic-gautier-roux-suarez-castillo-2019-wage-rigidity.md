# Fiche d'audit — Gautier, Roux & Suarez Castillo (2019), rigidité salariale et minima

- **Référence :** Erwan Gautier, Sébastien Roux et Milena Suarez Castillo, *Do Minimum Wages Make Wages more Rigid? Evidence from French Micro Data*, INSEE, Document de travail G2019/09, novembre 2019.
- **Source primaire :** [PDF intégral INSEE](https://www.insee.fr/fr/statistiques/fichier/version-html/4249078/G2019-09.pdf) ; [notice INSEE](https://www.insee.fr/en/statistiques/4249078).
- **Statut :** audit du document primaire (93 pages), données, modèle microéconométrique, hypothèses d'identification, simulations agrégées, hétérogénéité par décile et analyses de robustesse.
- **Question :** comment le SMIC national et les minima conventionnels influencent-ils la fréquence et la taille des augmentations salariales, puis la vitesse de transmission de l'inflation et des hausses de minima aux salaires agrégés ?
- **Avertissement central :** le papier étudie la rigidité et la diffusion salariales. Il ne mesure pas l'effet du SMIC sur l'emploi, les heures, les prix ou la pauvreté.

## 1. Données et population observée

Les auteurs appariement trois sources trimestrielles :

1. **Salaires ACEMO (DARES) :** données de 2005T1 à 2015T4, environ 40 000 entreprises d'au moins 10 salariés interrogées chaque trimestre dans le secteur privé marchand non agricole. Les entreprises déclarent les salaires mensuels bruts de base de postes représentatifs, hors primes, indemnités, rémunérations de performance et heures supplémentaires. Selon les auteurs, le salaire de base représente environ 85 % de la rémunération totale.
2. **Minima conventionnels de branche :** plus de 3 000 accords de branche, couvrant plus de 360 branches et environ 90 % des observations salariales ACEMO. Les grilles définissent des minima pour des postes-types ; les auteurs reconstruisent leurs trajectoires trimestrielles à partir des dates d'entrée en vigueur.
3. **Accords salariaux d'entreprise :** base administrative exhaustive des accords déposés auprès du ministère, utilisée sous forme d'indicatrice signalant la signature d'un accord salarial dans le trimestre depuis la dernière hausse du poste. La base ne renseigne pas le montant ni les catégories de salariés effectivement couvertes.

L'échantillon estimé comprend environ **2 millions d'observations de salaires** dans plus de **45 000 entreprises**. Les données permettent de suivre des postes représentatifs dans les entreprises, pas les trajectoires de tous les salariés individuellement. Les auteurs précisent qu'ils se concentrent sur les salariés qui restent dans leur poste/entreprise et ne capturent pas la mobilité professionnelle.

### Ce que la population exclut ou mesure imparfaitement

- Les entreprises de moins de 10 salariés sont absentes.
- Les salaires de base excluent les primes, compléments, performances et heures supplémentaires ; ils ne sont donc pas la rémunération totale ni l'assiette légale complète du SMIC.
- Les postes représentatifs permettent de suivre une trajectoire de salaire au sein de l'établissement, mais ne couvrent pas les changements de poste ou d'employeur.
- Les accords d'entreprise ne fournissent pas le montant exact des augmentations ni les catégories couvertes.
- Le modèle porte sur le secteur privé marchand non agricole, et non sur l'ensemble des salariés publics et privés.

## 2. Institutions salariales et mécanisme étudié

Le système français combine trois niveaux :
- le SMIC national, applicable à tous les salariés ;
- les minima de branche, définis par métier ou classification et qui ne peuvent être inférieurs au SMIC ;
- les accords salariaux d'entreprise, qui peuvent fixer des augmentations générales ou catégorielles.

Les auteurs soulignent que seulement 10 à 15 % des salariés sont directement concernés par une hausse du SMIC national à une date donnée, mais que les minima de branche peuvent transmettre la hausse à des salaires plus élevés. Les branches doivent ouvrir des négociations annuelles, sans obligation de conclure ; en l'absence d'accord, les minima conventionnels restent inchangés et le SMIC s'applique lorsqu'un minimum de branche lui devient inférieur.

Le mécanisme étudié est donc double :
1. effet direct du SMIC sur la probabilité et la taille d'une hausse du salaire individuel ;
2. effet indirect via la révision des minima conventionnels, puis leur transmission aux salaires individuels.

Le papier ne traite pas le SMIC comme un choc isolé dans une expérience naturelle. Il modélise la manière dont les institutions et les négociations salariales interagissent avec l'inflation, le chômage et les hausses de minima.

## 3. Faits descriptifs sur la rigidité des salaires

Sur l'ensemble de l'échantillon :
- environ 27 % des salaires de base sont modifiés chaque trimestre ;
- la hausse non nulle moyenne est d'environ 1,8 % ;
- la variation trimestrielle moyenne du salaire de base est d'environ 0,47 % ;
- 45 % des salaires sont ajustés au premier trimestre, contre environ 20 % en moyenne dans les autres trimestres ;
- la durée entre deux changements de salaire présente un pic marqué à un an.

Les accords salariaux sont synchronisés avec les changements de salaire. La hausse moyenne du salaire de base est d'environ 0,3 % en l'absence d'accord, 0,7 % lorsqu'un accord de branche ou d'entreprise est signé, et 1,1 % lorsque les deux niveaux d'accord sont présents.

Ces faits sont importants pour l'interprétation : les hausses du SMIC et des minima de branche influencent non seulement le montant des augmentations, mais aussi leur calendrier. Une hausse légale peut accélérer les révisions salariales au moment où les négociations annuelles se déroulent.

## 4. Modèle microéconométrique et identification

Les auteurs estiment un modèle de rigidité salariale de type **Tobit de type II en deux étapes** :
- une équation Probit pour la probabilité qu'un salaire soit ajusté ;
- une équation pour la taille de l'ajustement conditionnellement à l'observation d'une hausse.

Les déterminants comprennent les variations cumulées depuis le dernier ajustement :
- IPC national ;
- SMIC nominal ;
- minimum conventionnel de branche correspondant au poste ;
- indicatrice d'accord salarial d'entreprise depuis la dernière hausse ;
- chômage local.

Le modèle inclut également :
- indicatrices de durée depuis la dernière hausse (pour tenir compte de contrats salariaux de type Taylor) ;
- effets de trimestre pour la saisonnalité ;
- contrôles de taille et de secteur de l'entreprise ;
- position du poste dans la distribution salariale, par décile.

L'estimation utilise une procédure de Heckman en deux étapes et des erreurs-types obtenues par bootstrap en grappes au niveau de l'entreprise.

### Hypothèses d'identification

Les variables macroéconomiques telles que l'IPC et le SMIC ne varient pas entre individus à une date donnée. Les auteurs utilisent les variations cumulées depuis la dernière hausse du salaire pour créer de la variation individuelle : deux postes observés au même trimestre peuvent avoir connu des périodes différentes depuis leur dernier ajustement.

L'identification de la taille des hausses repose surtout sur une restriction d'exclusion : les indicatrices de durée et de trimestre influencent la probabilité de révision, mais pas directement la taille de l'augmentation une fois les variations cumulées des déterminants prises en compte. Les auteurs interprètent ces variables comme des effets de calendrier, de négociation et de saisonnalité.

**Cette restriction est substantielle.** Les calendriers de négociation peuvent également être corrélés à la taille des augmentations, même après contrôle des variables cumulées. La robustesse aux variantes de calendrier réduit le risque sans démontrer que l'exclusion est parfaitement vérifiée.

Ce n'est pas une expérience naturelle ni une différence-de-différences avec pré-tendances parallèles. Les paramètres estimés sont des relations conditionnelles dans un modèle structurel de rigidité salariale, ensuite utilisées pour simuler des trajectoires agrégées.

## 5. Résultats microéconométriques

Lorsque le modèle intègre le SMIC, les minima de branche et les accords d'entreprise :
- une hausse de 1 % du SMIC ou du minimum de branche augmente d'environ **2 points** la probabilité d'une révision salariale ;
- un accord salarial d'entreprise augmente cette probabilité d'environ **11 points** ;
- une hausse de 1 % du SMIC augmente la taille de l'ajustement conditionnel d'environ **0,11 point** ;
- une hausse de 1 % du minimum de branche l'augmente d'environ **0,14 point** ;
- un accord salarial d'entreprise augmente la taille moyenne de l'ajustement d'environ **0,33 point**.

Ces résultats indiquent que le SMIC et les minima conventionnels influencent à la fois le déclenchement et le montant des révisions salariales. Ils ne sont pas des élasticités d'emploi.

Les minima de branche réagissent eux-mêmes aux variations du SMIC, de l'inflation et de la croissance salariale passée. Une hausse de 1 % du SMIC, de l'inflation ou de la croissance salariale passée a un effet positif significatif sur la taille des révisions de minima conventionnels (environ 0,24 à 0,31 selon la variable). La probabilité d'une révision de minimum de branche dépend fortement de la durée depuis la dernière mise à jour.

## 6. Simulations agrégées : effets directs et effets de second tour

Les auteurs simulent les trajectoires salariales à partir des paramètres microéconométriques, puis agrègent les salaires simulés. Ils introduisent un choc de 1 % à une date donnée, en comparant les trajectoires avec et sans choc.

Les simulations distinguent :
- **effet direct :** le choc affecte les salaires individuels, mais pas les minima nationaux ou de branche ;
- **effet indirect :** le choc modifie aussi les minima de branche, qui influencent ensuite les salaires ;
- **boucle de rétroaction :** les hausses salariales agrégées passées peuvent influencer les revalorisations ultérieures du SMIC et des minima de branche.

### Résultats agrégés à cinq ans

| Choc de 1 % | Effet direct sur les salaires de base après 5 ans |
|---|---:|
| Inflation IPC | +0,24 point |
| SMIC national | +0,13 point |
| Minima conventionnels de branche | +0,16 point |

Lorsque les minima de branche et le SMIC réagissent eux-mêmes aux chocs :
- l'effet d'un choc de 1 % sur le SMIC passe de **+0,13 à +0,17 point** sur les salaires de base ;
- l'amplification vient surtout de la réaction des minima de branche (environ +0,03 point) ; la boucle de rétroaction supplémentaire est plus faible (environ +0,01 point) ;
- l'effet d'un choc d'inflation passe de +0,22 à **+0,42 point** lorsque les interactions avec les minima sont prises en compte ;
- l'indexation des salaires à l'inflation passée est ainsi amplifiée d'un facteur **1,7**.

Il faut éviter une lecture erronée du facteur 1,7 : il concerne l'amplification de la réponse des salaires à l'inflation passée par les institutions de salaire minimum. Ce n'est pas une multiplication par 1,7 de l'effet causal d'une hausse du SMIC sur l'emploi ou sur l'ensemble des salaires.

Le délai de transmission est également important :
- environ 4 ans pour qu'un choc soit entièrement transmis aux salaires agrégés par les effets directs ;
- environ 5 ans lorsque les minima de branche et les rétroactions sont autorisés à réagir ;
- environ 75 % de l'effet de long terme est transmis après deux trimestres dans le modèle de base avec ajustements dépendant de l'état, contre 58 % dans le modèle à fréquence exogène.

## 7. Hétérogénéité selon le niveau de salaire

Après cinq ans, une hausse de 1 % du SMIC produit dans les simulations un effet total sur les salaires de base qui décroît avec le niveau de salaire :
- environ +0,4 point pour le premier décile, proche du SMIC ;
- environ +0,2 point pour les deuxième et troisième déciles ;
- environ +0,1 point pour les déciles au-dessus de 1,3 SMIC dans la spécification de référence.

La décomposition montre :
- les effets directs du SMIC dominent près du plancher ;
- les minima conventionnels expliquent une part importante des effets dans les déciles supérieurs, jusqu'à environ la moitié de l'effet total au sommet de la distribution ;
- les boucles de rétroaction jouent davantage pour les salaires inférieurs à 1,6 SMIC.

**Réserve importante sur les hauts salaires :** les auteurs indiquent que lorsque des effets fixes temporels complets sont introduits, l'effet total du SMIC devient proche de zéro au-dessus de la médiane (au-delà de 1,5 SMIC). De plus, les branches métallurgie, bâtiment et travaux publics, notamment pour les cadres, contribuent fortement aux effets estimés au sommet de la distribution. Lorsque ces branches sont exclues, l'effet sur les hauts déciles diminue nettement. La diffusion jusqu'aux hauts salaires est donc plus sensible à la spécification et à la composition sectorielle que l'effet près du plancher.

## 8. Robustesse et limites des simulations

Les auteurs testent plusieurs variantes :
- effets de trimestre, effets de date et interactions avec la période postérieure à 2010, année du déplacement de la revalorisation annuelle de juillet à janvier ;
- variantes avec indicatrices de durée seules ou effets trimestriels seuls ;
- introduction du choc à différents trimestres et différentes années ;
- modèle alternatif de croissance annuelle des salaires pour contrôler la productivité des entreprises.

Les effets agrégés à cinq ans sont décrits comme relativement robustes à ces variantes, mais l'hétérogénéité des hauts déciles dépend davantage des effets temporels et des branches retenues.

### Limites majeures

1. **Pas d'emploi :** les simulations gardent la composition de l'échantillon fixe ; aucune entrée ou sortie n'est simulée. Les effets sur les créations/destructions d'emplois ne sont pas estimés.
2. **Pas de prix ni de marges :** les auteurs ne modélisent pas les rétroactions d'un choc sur les prix ou l'emploi, qu'ils laissent explicitement pour des travaux futurs.
3. **Échantillon de salariés en poste :** la mobilité entre entreprises ou postes n'est pas observée ; les effets sur les trajectoires des personnes qui changent d'emploi sont absents.
4. **Entreprises de moins de 10 salariés exclues :** les résultats ne couvrent pas les TPE.
5. **Salaire de base :** les primes, compléments et heures supplémentaires sont exclus.
6. **Accords d'entreprise incomplets :** la base renseigne la présence d'un accord, mais pas le montant des augmentations ni les salariés couverts.
7. **Identification par restriction d'exclusion :** les effets de durée et de trimestre sont supposés n'affecter que la probabilité d'ajustement et non sa taille conditionnelle ; cette hypothèse est centrale.
8. **Simulation conditionnelle au modèle :** les réponses agrégées sont produites par les paramètres estimés et des trajectoires simulées, non par une comparaison expérimentale d'entreprises exposées et non exposées.
9. **Effets sur les hauts salaires sensibles :** la contribution des branches métallurgie et BTP et le choix des effets temporels modifient sensiblement la diffusion estimée au-dessus de 1,5 SMIC.

## 9. Synthèse et niveau de preuve

**Résultat solide :** le SMIC national et les minima conventionnels influencent la fréquence et la taille des ajustements des salaires de base. Le canal des minima de branche est important : il transmet une partie des hausses du SMIC à des rémunérations plus élevées et amplifie aussi la transmission de l'inflation passée.

**Ordres de grandeur du modèle :** une hausse de 1 % du SMIC produit un effet direct de +0,13 point sur les salaires agrégés après cinq ans ; l'effet total simulé atteint +0,17 point lorsque les minima de branche et les rétroactions sont intégrés. L'effet est plus fort près du plancher et plus fragile dans les hauts déciles.

**Ce que l'étude ne permet pas de conclure :**
- elle ne mesure pas la création ou la destruction d'emplois ;
- elle ne mesure pas le revenu disponible ou la pauvreté ;
- elle n'identifie pas l'effet d'un épisode historique précis de « coup de pouce » ;
- le facteur 1,7 n'est pas un multiplicateur d'effet sur l'emploi : il concerne la transmission de l'inflation aux salaires agrégés ;
- les résultats agrégés dépendent des hypothèses du modèle et des simulations.

**Niveau de confiance :**
- **modéré** pour l'existence de canaux de diffusion du SMIC vers les salaires de base via les minima conventionnels ;
- **modéré à faible** pour les ordres de grandeur agrégés à cinq ans, qui reposent sur les hypothèses de simulation et d'identification du modèle ;
- **faible** pour les effets estimés sur les hauts salaires, sensibles aux effets temporels et à la composition sectorielle ;
- **nul** pour une conclusion sur l'emploi, les prix ou le bien-être, qui ne sont pas estimés.

## 10. Référence primaire

Gautier, Erwan, Sébastien Roux et Milena Suarez Castillo (2019), *Do Minimum Wages Make Wages more Rigid? Evidence from French Micro Data*, INSEE Document de travail G2019/09, novembre 2019, [PDF intégral](https://www.insee.fr/fr/statistiques/fichier/version-html/4249078/G2019-09.pdf).
