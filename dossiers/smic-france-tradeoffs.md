# Augmenter le SMIC en France : pouvoir d'achat, emploi, salaires et finances publiques

- **Identifiant :** DOSSIER-SMIC-FRANCE-TRADEOFFS
- **Statut :** recherche en cours
- **Dernière revue documentaire :** 13 novembre 2026
- **Domaines :** économie, finances publiques, institutions
- **Périmètre :** France hors Mayotte pour les séries nationales citées ; comparaison européenne et OCDE ; déclinaisons territoriales à construire.
- **Période principale :** 1990-2026, avec attention particulière à 2021-2026.

## Prolongement quantitatif

- [Prototype de microsimulation avec OpenFisca-France](../docs/smic-openfisca-prototype.md) — cas-types de ménages, comparaison statique de hausses hypothétiques et protocole de validation. Aucun résultat chiffré n'est publié avant exécution et audit du modèle.

## Question de recherche

Dans quelles conditions une hausse du salaire minimum interprofessionnel de croissance (SMIC), au-delà de son mécanisme légal d'indexation, améliore-t-elle durablement le niveau de vie des travailleurs modestes sans dégrader excessivement l'emploi, la progression salariale, la compétitivité, la productivité et les finances publiques ?

La question ne se réduit pas à « pour ou contre ». Il faut comparer des scénarios précis : indexation seule, coup de pouce ponctuel, hausse graduelle, hausse forte et rapide, réforme de la prime d'activité, réforme des allègements de cotisations et négociation des minima de branche.

## Résumé provisoire

Le SMIC est à la fois un plancher salarial, un instrument de réduction des inégalités de rémunération et un paramètre du coût du travail. Son effet distributif est réel pour les salariés directement concernés, mais il ne se confond pas avec la réduction de la pauvreté : le niveau de vie dépend aussi du temps de travail, de la composition du ménage, des transferts, du logement et de l'emploi des autres membres du foyer.

Les éléments examinés suggèrent que le salaire minimum français est élevé relativement au salaire médian et comprime la distribution des salaires dans le bas de l'échelle. Les effets sur l'emploi ne peuvent cependant pas être déduits mécaniquement de ce seul ratio. Ils dépendent du niveau initial, de l'ampleur et du calendrier de la hausse, de la productivité, des marges, de la demande, des secteurs, du territoire et des politiques d'allègement.

L'enjeu systémique central est le couplage entre SMIC, minima conventionnels, négociation salariale, prime d'activité, cotisations patronales et coût budgétaire des allègements. Les rapports officiels signalent des effets avérés des allègements sur l'emploi, mais aussi leur coût, leur complexité et des risques de trappes à bas salaires. Ces constats ne prouvent pas qu'une hausse donnée du SMIC détruit ou crée un nombre déterminé d'emplois.

**État de preuve :** cadrage documentaire initial. Les sources et études ci-dessous ont été repérées et leurs publications consultées au niveau de la page, du résumé ou des extraits accessibles. Les analyses causales détaillées, tableaux annexes, microdonnées et calculs de réplication restent à effectuer. Les claims demeurent donc « under_review ».

## 1. Définir ce que l'on augmente

Le SMIC est un minimum légal horaire brut. Il faut distinguer :
- le taux horaire brut, qui est le plancher légal ;
- le salaire mensuel brut correspondant à 35 heures, soit 151,67 heures mensuelles ;
- le salaire net, qui dépend des prélèvements applicables et n'est donné qu'à titre indicatif ;
- le coût total employeur, qui dépend des cotisations et allègements ;
- le revenu disponible du ménage, après impôts et prestations.

Une hausse de 5 % du taux horaire brut n'implique donc ni une hausse de 5 % du revenu disponible de tous les ménages modestes, ni une hausse de 5 % du coût employeur dans toutes les entreprises.

### 1.1 Mécanisme français de revalorisation

Le mécanisme légal combine :
1. l'évolution des prix à la consommation des 20 % de ménages ayant les revenus les plus faibles ;
2. la moitié du gain de pouvoir d'achat du salaire horaire de base des ouvriers et employés.

En cours d'année, une hausse automatique intervient si l'indice des prix de référence progresse d'au moins 2 % depuis la dernière revalorisation. Le gouvernement peut aussi décider d'un « coup de pouce » discrétionnaire.

Ces mécanismes doivent être séparés dans les séries historiques : une revalorisation automatique protège le plancher contre l'inflation selon une formule donnée ; un coup de pouce modifie le niveau relatif du plancher.

### 1.2 Repères récents vérifiés

Au 1er janvier 2026, le SMIC horaire brut en France hors Mayotte est de 12,02 €, soit 1 823,03 € brut mensuels pour 151,67 heures. Une hausse automatique de 2,41 % est entrée en vigueur le 1er juin 2026 : 12,31 € brut par heure et 1 867,02 € brut mensuels ; le net mensuel indicatif publié est de 1 477,93 €.

Ces montants sont des repères datés, pas une prévision de salaire net individuel. La source statistique de référence est la série annuelle de l'INSEE, alimentée par le ministère du Travail.

### 1.3 Qui est concerné ?

La Dares indique que 2,1 millions de salariés du secteur privé non agricole ont bénéficié directement de la revalorisation du 1er janvier 2026, soit 11,8 % du champ Acemo. Il s'agit d'un indicateur de bénéficiaires directs, qui ne signifie pas que tous ces salariés perçoivent une rémunération globale exactement égale au SMIC. À titre de comparaison, 2,2 millions de salariés (12,4 %) avaient été directement concernés en novembre 2024. En 2024, la Dares estimait par ailleurs que les salariés à temps partiel et ceux des TPE étaient davantage exposés aux revalorisations. Les champs et dates doivent rester explicites.

Ce chiffre désigne les bénéficiaires directs de cette revalorisation et de ce champ statistique ; il ne faut pas le présenter comme la part de tous les salariés français rémunérés au SMIC, ni comme un décompte actuel en 2026.

## 2. Arguments favorables à une hausse

### 2.1 Pouvoir d'achat et protection contre les prix

Une hausse nominale supérieure à l'inflation pertinente augmente le salaire réel horaire des salariés conservant le même volume de travail. Elle peut corriger une perte de pouvoir d'achat lorsque les prix essentiels (logement, énergie, alimentation, transport) progressent plus vite que l'indice moyen.

Limites : l'effet dépend des heures rémunérées, du maintien dans l'emploi, des transferts et de la hausse éventuelle des prix. Les ménages modestes ne sont pas tous salariés au SMIC ; certains sont sans emploi, indépendants ou retraités.

### 2.2 Inégalités salariales et reconnaissance du travail

Le plancher relève les rémunérations les plus basses et réduit mécaniquement les écarts salariaux mesurés en bas de distribution. Il peut renforcer le pouvoir de négociation des salariés peu rémunérés et améliorer l'attractivité de métiers difficiles à pourvoir.

Limites : la compression des écarts peut aussi réduire les différentiels entre niveaux de qualification, ancienneté et responsabilité si les grilles ne sont pas révisées. La question devient alors celle de la dynamique des salaires au-dessus du SMIC.

### 2.3 Demande intérieure

Les ménages à bas revenus ont généralement une capacité d'épargne limitée ; une hausse de leur revenu peut donc être davantage consacrée à la consommation courante. Elle peut soutenir les commerces et services locaux.

Limites : une partie de la demande supplémentaire se porte sur des produits importés ; les entreprises peuvent répercuter une partie du coût sur les prix, réduire leurs marges ou adapter l'emploi. L'effet macroéconomique net doit être estimé, pas présumé.

### 2.4 Incitations à la productivité et à la montée en gamme

Un plancher plus élevé peut inciter certaines entreprises à réduire le turnover, investir dans la formation, réorganiser les processus, automatiser des tâches pénibles ou monter en gamme.

Limites : ces adaptations nécessitent du temps, du financement, des compétences et une demande solvable. D'autres entreprises peuvent ne pas disposer de ces marges d'ajustement.

### 2.5 Réduction des inégalités de genre

Les femmes sont surreprésentées parmi les salariés directement concernés par les hausses du SMIC, en lien notamment avec la structure sectorielle des emplois et le temps partiel. Le plancher peut donc réduire certains écarts de rémunération.

Limites : il ne corrige pas à lui seul les écarts de volume de travail, de carrière, de métiers, de responsabilités ou de rémunération au-delà du minimum.

## 3. Arguments défavorables et risques à tester

### 3.1 Coût du travail et demande de travail

Si le coût horaire augmente plus vite que la productivité et que les prix ou marges ne peuvent absorber l'écart, certaines entreprises peuvent ralentir les embauches, réduire les heures, substituer du capital au travail ou quitter le marché.

Le risque n'est pas uniforme : il est potentiellement plus important pour les activités à faible marge, forte intensité de main-d'œuvre et faible possibilité de hausse des prix. L'effet dépend aussi de la concurrence, de la demande et des tensions de recrutement.

Ne pas transformer ce mécanisme théorique en affirmation automatique de destructions d'emplois. Il faut identifier empiriquement l'ampleur, les groupes affectés et l'horizon.

### 3.2 Petites entreprises et territoires

Les TPE, les entreprises rurales, les secteurs saisonniers et les activités de proximité peuvent avoir moins de capacité à absorber un choc de coût que de grandes entreprises disposant de marges, de pouvoir de marché ou de capacités d'investissement.

Mais les TPE ne sont pas homogènes : certaines bénéficient d'une demande locale soutenue ou de gains de productivité, d'autres sont contraintes par des marchés publics, des tarifs administrés ou une concurrence intense.

### 3.3 Prix et inflation

Les entreprises peuvent répercuter une partie de la hausse salariale dans leurs prix, surtout dans les services intensifs en travail. Les effets de second tour dépendent de la diffusion de la hausse, des marges, de la productivité et des anticipations.

Il faut distinguer un ajustement ponctuel du niveau des prix d'une spirale prix-salaires durable. La seconde ne découle pas automatiquement d'une hausse du SMIC.

### 3.4 Compression salariale et progression des carrières

Lorsque le SMIC progresse rapidement, les minima de branche peuvent devenir inférieurs au plancher légal. Les grilles sont alors rattrapées, les écarts entre niveaux se resserrent et les négociations doivent être rouvertes.

Le risque de « tassement » ou de trappe à bas salaires doit être étudié avec les trajectoires individuelles, les promotions, les mobilités et les salaires conventionnels. La compression descriptive des salaires ne prouve pas à elle seule une stagnation des carrières.

### 3.5 Emploi des jeunes, des peu qualifiés et des personnes éloignées de l'emploi

Un plancher élevé peut relever le prix d'embauche de personnes dont la productivité initiale est faible ou incertaine. Il peut ainsi affecter différemment les primo-entrants et les salariés expérimentés.

Mais les employeurs recrutent aussi en fonction de la formation, de l'expérience, des pénuries, de la rotation, des aides, et de la qualité du management. L'effet doit être examiné par âge, qualification, secteur et situation antérieure.

### 3.6 Dépenses publiques et effets de seuil

Les hausses du SMIC peuvent accroître mécaniquement le coût des allègements de cotisations calculés en référence au salaire minimum et modifier les dépenses de prestations, les recettes fiscales et les rémunérations publiques indexées ou négociées.

Il faut établir un compte consolidé : coût des exonérations, recettes de cotisations et d'impôt, prime d'activité, minima sociaux, dépenses de consommation publique et éventuels effets sur l'emploi. Un coût brut d'allègement n'est pas un coût net de politique publique.

## 4. Le système socio-fiscal : la pièce souvent oubliée

La France a construit des allègements de cotisations patronales concentrés sur les bas salaires pour réduire le coût du travail peu qualifié. Ils atténuent le coût employeur au niveau du SMIC, mais leur dégressivité et leurs seuils peuvent créer des taux marginaux élevés lorsque le salaire progresse.

Le rapport du groupe d'experts SMIC 2024 indique que les allègements ont un effet avéré sur l'emploi et estime que leur suppression totale entraînerait 1,5 à 2 millions de suppressions d'emplois. Le rapport 2025 chiffre les allègements à près de 75 milliards d'euros en 2024 ; le rapport 2024 avançait un ordre de grandeur proche de 80 milliards. Ces montants doivent être réconciliés à partir des périmètres comptables et versions de calcul avant d'être traités comme une série comparable. L'estimation d'emplois est un résultat de scénario sur la suppression des allègements, pas l'effet d'une hausse du SMIC.

Le rapport 2025 recommande de ne pas dépasser la revalorisation automatique au 1er janvier 2026 et critique l'extension des allègements au-delà des bas salaires. Il s'agit d'une recommandation d'experts, non d'une preuve que toute hausse discrétionnaire aurait un effet négatif net.

Le rapport France Stratégie sur les exonérations de cotisations (2024) et les travaux du groupe d'experts doivent être confrontés : coût budgétaire, effets sur l'emploi, effets sur les trajectoires salariales, productivité et options de réforme ne sont pas des objets interchangeables.

## 5. Ce que les sources permettent déjà de dire

### 5.1 Niveau relatif du SMIC

Le rapport du groupe d'experts SMIC 2025 donne un ratio SMIC/salaire médian brut à temps plein de 62,5 % en 2024, le plus élevé parmi les pays européens comparés dans son graphique ; le ratio au salaire moyen brut est de 50,4 %. L'OCDE (2025) décrit également un nombre élevé de salariés proches du minimum et une compression en bas de la distribution. Ces ratios ne sont pas des seuils scientifiques universels d'optimalité ou de danger, et dépendent du champ, de l'année et de la définition retenue. Cette comparaison dépend de la définition du salaire, du champ des salariés et de l'année ; elle ne suffit pas à conclure à un optimum ou à un seuil de danger.

### 5.2 Pouvoir d'achat historique

Les séries INSEE montrent que le pouvoir d'achat horaire net du SMIC a progressé de 0,7 % en moyenne annuelle en 2025, après une progression faible en 2024 (+0,2 %) et en 2023 (+0,5 %), et une stagnation en 2022. Ces variations annuelles doivent être distinguées des évolutions cumulées et du revenu disponible des ménages.

### 5.3 Salariés directement concernés

La Dares montre qu'au 1er janvier 2026, 11,8 % des salariés du secteur privé non agricole ont bénéficié directement de la revalorisation (2,1 millions). La proportion était de 12,4 % au 1er novembre 2024, 14,6 % au 1er janvier 2024 et 17,3 % au 1er janvier 2023. En janvier 2026, 25,6 % des salariés à temps partiel ont bénéficié de la hausse, contre 8,8 % des salariés à temps complet ; les proportions étaient de 21,9 % dans les entreprises de 1 à 9 salariés et 9,5 % dans les entreprises plus grandes. Les femmes représentaient 59,6 % des bénéficiaires. Les proportions sectorielles atteignaient 62,3 % dans la restauration rapide et 53,8 % dans les services à la personne (entreprises). Ces données décrivent l'exposition directe à la hausse, non des pertes ou créations d'emplois causées par elle.

La Dares précise qu'aucune source statistique ne mesure exactement le nombre de salariés rémunérés au SMIC, car l'assiette légale ne correspond pas à la rémunération brute totale. En 2024, 4,9 % des salariés du privé en équivalent temps plein (0,9 million EQTP) percevaient un salaire brut horaire global inférieur à 1,05 SMIC. Sur le champ Ecmoss des entreprises privées de 10 salariés ou plus, 14,5 % des salariés avaient en 2022 un salaire de base inférieur à 1,05 SMIC ; parmi eux, 40,2 % avaient une rémunération totale inférieure à 1,05 SMIC. Ces indicateurs ne sont pas interchangeables : années, champ et définition diffèrent.

### 5.4 Effets sur le salaire moyen

Une étude INSEE publiée en 2012, portant sur 1970-2009, estime que les revalorisations du SMIC ont un effet important sur le salaire moyen et que les revalorisations liées à l'indexation sur la moitié des gains de pouvoir d'achat du salaire ouvrier peuvent nourrir une circularité entre SMIC et salaire de base. Résultat historique à actualiser avec les transformations du marché du travail et les données récentes.

### 5.5 Effets sur l'emploi : ce qui reste à établir

Les sources consultées ici ne justifient pas une élasticité unique et universelle de l'emploi au SMIC français. Il faut comparer les études selon leur stratégie d'identification, les périodes, les populations, les secteurs, l'ampleur des hausses et les marges d'ajustement observées.

Une étude descriptive des évolutions de l'emploi après une hausse ne suffit pas : la conjoncture, les autres réformes, les allègements, la demande et les changements sectoriels peuvent expliquer simultanément les évolutions.

### 5.6 Ce que montrent les études empiriques et les modèles

Il faut éviter de mettre sur le même plan quatre familles de résultats :

| Étude | Objet effectivement étudié | Ce qu'elle apporte | Ce qu'elle ne démontre pas |
|---|---|---|---|
| Cottet (CESifo, 2024) | Réduction de cotisations patronales ciblant les emplois au SMIC ; données administratives employeurs-salariés | Réponses différentes selon le profil antérieur des entreprises : hausse du nombre d'emplois au SMIC dans les entreprises peu exposées auparavant ; croissance de l'emploi dans les entreprises déjà exposées | L'effet d'une hausse du SMIC ; les effets d'une baisse de cotisations ne sont pas symétriques à ceux d'une hausse salariale |
| Albertini, Poirier et Terriau (TEPP, 2025) | Modèle structurel du marché du travail et du système socio-fiscal français | Les simulations prévoient un risque de baisse de l'emploi et du surplus budgétaire en cas de hausse du SMIC, avec sensibilité à l'indexation des allègements et prestations | Un nombre observé d'emplois détruits ; résultat causal issu d'une expérience réelle |
| Gautier, Roux et Suarez Castillo (INSEE, 2019) | Salaires individuels et minima de branche | Les minima influencent le calendrier et l'ampleur des ajustements salariaux ; diffusion aux salaires supérieurs via les minima de branche | Une mesure contemporaine de l'effet sur l'emploi, les prix ou la pauvreté |
| OCDE (2025) | Comparaison internationale des emplois à bas salaire, des compétences et des trajectoires | Le SMIC français est relativement élevé ; la mobilité salariale ascendante des travailleurs à bas salaire n'est pas plus difficile dans les pays comparés | Une identification causale de l'effet d'un coup de pouce français précis |

La distinction la plus importante est celle entre l'effet du salaire minimum et l'effet du système complet qui l'entoure. Les allègements patronaux modifient le coût employeur ; la prime d'activité et les prélèvements modifient le gain net du salarié ; les minima de branche diffusent les hausses. Un résultat sur l'un de ces leviers ne peut pas être attribué automatiquement à un autre.

L'étude de Cottet est particulièrement utile parce qu'elle montre que les entreprises ne réagissent pas toutes de la même manière à une variation du coût du travail. Elle porte toutefois sur une baisse de cotisations patronales : elle ne permet pas de conclure qu'une hausse du SMIC aurait des effets opposés ou de même ampleur. Le modèle d'Albertini et ses coauteurs traite directement de hausses du SMIC, mais ses conclusions restent conditionnelles aux hypothèses de modélisation. Les deux résultats doivent être lus ensemble, sans transformer le modèle en fait observé.

### 5.7 Le SMIC et les grilles salariales

L'étude INSEE de 2019 indique que les minima salariaux modifient le calendrier et l'ampleur des hausses individuelles. Dans son modèle, ils amplifient par un facteur 1,7 la réponse agrégée des salaires à l'inflation passée ; une hausse du SMIC se diffuse notamment via les minima conventionnels. Cela renforce la nécessité de suivre les grilles de branche, mais ne signifie pas que chaque salarié au-dessus du SMIC obtient une hausse identique.

L'OCDE (2025) ajoute une nuance importante au débat sur la « trappe à bas salaires » : elle identifie des mécanismes socio-fiscaux susceptibles de limiter les gains de mobilité, mais son analyse des trajectoires ne conclut pas que les travailleurs à bas salaire français ont moins de chances de progresser que ceux des pays comparés. Il faut donc distinguer les taux marginaux élevés à certains niveaux de salaire, le comportement des employeurs, et les mobilités professionnelles effectivement observées.

## 6. Questions de recherche et hypothèses

Les hypothèses du registre ne sont pas des conclusions :
- une hausse ciblée peut accroître le revenu disponible des salariés concernés, mais le gain de niveau de vie dépend du ménage, des heures et des transferts ;
- les effets négatifs éventuels sur l'emploi sont hétérogènes et concentrés dans certains secteurs, entreprises ou groupes ;
- les allègements patronaux protègent une partie de l'emploi au bas de l'échelle, mais leur profil peut freiner la progression salariale ;
- le SMIC élevé réduit les très bas salaires, mais contribue à la compression de la distribution salariale ;
- les politiques de complément (prime d'activité, transferts, négociation collective, formation) peuvent être plus ou moins efficaces selon l'objectif recherché.

Pour chaque hypothèse, rechercher des éléments qui pourraient la réfuter et des explications concurrentes.

## 7. Comparaisons européennes et internationales

La comparaison doit porter sur le ratio SMIC/salaire médian, le salaire minimum en pouvoir d'achat, les prélèvements, les prestations, la négociation collective, les conventions de branche, la productivité, la structure sectorielle et le chômage.

Comparateurs à examiner : Allemagne, Belgique, Pays-Bas, Espagne, Royaume-Uni et pays nordiques (en tenant compte du fait que plusieurs n'ont pas de salaire minimum légal national). Ne pas classer les pays sur un montant nominal ou un ratio isolé.

L'OCDE fournit un point d'entrée pour les comparaisons de salaire minimum et d'emploi à bas salaire. Eurostat et les instituts statistiques nationaux devront être mobilisés pour harmoniser les définitions et années.

## 8. Déclinaison territoriale : France, Pays de la Loire et Loire-Atlantique

Les effets du SMIC ne s'arrêtent pas à la frontière nationale, mais les données locales ne permettent pas toujours une identification causale. Une première enquête territoriale doit cartographier :
- la part des salariés proches du SMIC par secteur, taille d'entreprise, sexe, âge et temps partiel ;
- les secteurs exposés : hôtellerie-restauration, commerce, aide à domicile, nettoyage, logistique, agriculture et sous-traitance ;
- les écarts de coût de la vie, notamment logement, transport et énergie, sans supposer que le SMIC national produit un niveau de vie identique partout ;
- les tensions de recrutement, vacances de postes, turnover et évolution des heures ;
- la densité de TPE/PME, la saisonnalité et la dépendance à la commande publique ;
- les minima conventionnels et leur calendrier de négociation.

Échelles à distinguer : France, Pays de la Loire, Loire-Atlantique, Nantes Métropole, Nantes et Île de Nantes. Une comparaison territoriale doit préciser les secteurs, les populations et les années ; ne pas extrapoler des données départementales à l'Île de Nantes.

### Protocole d'enquête territoriale

1. Construire un tableau de bord descriptif à partir de Dares, INSEE, Urssaf et données régionales, avec dénominateurs et dates de référence.
2. Obtenir des données agrégées par secteur et taille d'entreprise ; éviter toute donnée individuelle identifiable.
3. Interroger organisations patronales, syndicats, branches, TPE/PME, associations d'aide aux salariés et acteurs de l'emploi.
4. Séparer les effets déclarés (difficultés ressenties) des effets observés (heures, embauches, salaires, prix, marges).
5. Comparer les trajectoires à celles de secteurs ou territoires moins exposés, sans attribuer automatiquement les écarts au SMIC.
6. Documenter les effets distributifs sur salariés, demandeurs d'emploi, employeurs, consommateurs, contribuables et bénéficiaires de prestations.

## 9. Scénarios à comparer

| Scénario | Question évaluative |
|---|---|
| Indexation légale seule | Protection du pouvoir d'achat selon la formule existante |
| Coup de pouce ponctuel | Gain distributif additionnel et effets de rattrapage |
| Hausse graduelle pluriannuelle | Capacité d'adaptation des entreprises et effets cumulés |
| Hausse forte et rapide | Risques de seuils, d'heures, de prix et d'emploi |
| Prime d'activité renforcée | Ciblage du revenu disponible et coût budgétaire |
| Réforme des allègements | Arbitrage emploi, progression salariale et finances publiques |
| Négociation de branche renforcée | Différenciation des qualifications et grilles salariales |

Le cadre détaillé de comparaison est désormais documenté dans [Comparer les politiques de soutien aux bas salaires : scénarios, ménages et entreprises](smic-policy-scenarios.md). Il définit des scénarios S0-S6, des profils de ménages et d'employeurs, un tableau d'évaluation commun et les conditions méthodologiques nécessaires avant tout chiffrage. Les profils sont des cas-types à simuler, pas des statistiques représentatives ni des résultats déjà calculés.

Chaque scénario doit être évalué à horizon court (0-1 an), moyen (2-3 ans) et long (4-10 ans), avec analyse distributive et sensibilité aux hypothèses.

## 10. Indicateurs de suivi

- SMIC réel horaire et mensuel ; rapport au salaire médian et moyen ;
- part des salariés directement concernés par chaque revalorisation ;
- distribution des salaires autour de 1,0 à 1,5 SMIC et progression des minima conventionnels ;
- emploi, chômage, heures travaillées, temps partiel subi, embauches et séparations ;
- salaires réels, revenu disponible, pauvreté en emploi et niveau de vie par ménage ;
- prix des services intensifs en main-d'œuvre et marges sectorielles ;
- coût budgétaire des allègements, recettes sociales et fiscales, prime d'activité ;
- productivité horaire, investissement, formation, automatisation et mobilité salariale.

Toujours indiquer les unités, champs, dates, dénominateurs, ruptures de série et sources.

## 11. Limites et précautions

- Ne pas assimiler hausse du SMIC, hausse du salaire moyen, hausse du revenu disponible et baisse de la pauvreté.
- Ne pas confondre coût employeur brut, coût net d'allègements et coût budgétaire.
- Ne pas attribuer une évolution de l'emploi à une hausse du SMIC sans stratégie causale crédible.
- Ne pas comparer des ratios internationaux sans harmoniser salaires, temps de travail, médianes, impôts et prestations.
- Ne pas traiter les recommandations du groupe d'experts comme des résultats empiriques.
- Les chiffres 2026 sont des données de contexte datées ; ils devront être actualisés.
- Les extraits et résumés consultés ne remplacent pas la lecture des annexes, méthodes et données sous-jacentes.

## 12. Programme de recherche prioritaire

**Priorité A — Vérification des preuves**
- Extraire les tableaux complets du rapport du groupe d'experts SMIC 2025 et de ses annexes.
- Lire le rapport 2024 sur les allègements de cotisations et distinguer les estimations causales des simulations.
- Examiner les méthodes et données de l'étude INSEE sur la transmission aux salaires moyens.
- Construire une bibliographie de travaux causaux français et internationaux sur l'emploi, les heures, les prix et les marges.

**Priorité B — Quantification**
- Reconstituer les revalorisations et les parts de salariés concernés depuis 1990.
- Décomposer les effets par sexe, âge, temps partiel, taille d'entreprise et secteur.
- Évaluer les effets de seuil des allègements et la dynamique des minima conventionnels.
- Estimer les effets distributifs sur ménages types, en tenant compte des prestations et de la fiscalité.

**Priorité C — Territoires**
- Construire le tableau de bord Pays de la Loire / Loire-Atlantique.
- Organiser une enquête qualitative auprès des partenaires sociaux et des entreprises.
- Identifier les secteurs et territoires où les arbitrages sont les plus sensibles.

**Priorité D — Synthèse contradictoire**
- Présenter les meilleurs arguments en faveur d'une hausse et les objections les plus solides.
- Distinguer résultats robustes, résultats conditionnels, désaccords méthodologiques et inconnues.
- Formuler les recommandations sous forme de scénarios et critères explicites, pas comme une conclusion partisane.

## Sources principales

1. [INSEE — Salaire minimum interprofessionnel de croissance, données annuelles 1980-2026](https://www.insee.fr/fr/statistiques/1375188) — série de référence et pouvoir d'achat.
2. [Service-Public — SMIC, montants et règles de revalorisation](https://www.service-public.gouv.fr/particuliers/vosdroits/F2300) — règles juridiques et montants en vigueur.
3. [Ministère du Travail — Revalorisation du SMIC au 1er juin 2026](https://travail-emploi.gouv.fr/revalorisation-du-smic-au-1er-juin-2026) — montants et mécanisme de revalorisation.
4. [Dares — La revalorisation du SMIC au 1er novembre 2024](https://dares.travail-emploi.gouv.fr/publication/la-revalorisation-du-smic-au-1er-novembre-2024) — bénéficiaires directs, distribution et caractéristiques.
5. [Dares — La revalorisation du SMIC au 1er janvier 2026](https://dares.travail-emploi.gouv.fr/publication/la-revalorisation-du-smic-au-1er-janvier-2026) — bénéficiaires directs, ventilations par temps de travail, taille d'entreprise et branche.
6. [Dares — Combien de salariés sont rémunérés au SMIC ?](https://dares.travail-emploi.gouv.fr/publication/combien-de-salaries-sont-remuneres-au-smic) — structure des salaires en 2024.
7. [OCDE — Low-wage employment in France (2025)](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/01/low-wage-employment-in-france_ac641c84/82539f44-en.pdf) — comparaison internationale, distribution des bas salaires et mobilité.
8. [Groupe d'experts SMIC — Rapport 2025](https://www.strategie-plan.gouv.fr/publications/groupe-dexperts-smic-rapport-2025) — recommandation sur la revalorisation et analyse du système socio-fiscal.
9. [Groupe d'experts SMIC — Rapport 2024](https://www.strategie-plan.gouv.fr/publications/groupe-dexperts-smic-rapport-2024) — effets et coût des allègements.
10. [Mission Bozio-Wasmer — Les politiques d'exonérations de cotisations sociales : une inflexion nécessaire (France Stratégie, 3 octobre 2024)](https://www.strategie-plan.gouv.fr/publications/mission-bozio-wasmer-politiques-dexonerations-de-cotisations-sociales-une-inflexion) — bilan et scénarios de réforme, avec code et données de simulation.
11. [Cour des comptes — Synthèse de l'évaluation des exonérations de cotisations sociales](https://www.ccomptes.fr/fr/plateformes-citoyennes/plateforme-evaluations-politique-publique/explorer-evaluations/les-46) — synthèse critique du rapport France Stratégie.
12. [INSEE — Les effets des hausses du SMIC sur le salaire moyen (2012)](https://www.insee.fr/fr/statistiques/1377686) — étude historique 1970-2009.

13. [INSEE — Les salaires minima rendent-ils les salaires plus rigides ? (2019)](https://www.insee.fr/fr/statistiques/4249066) — effets sur les ajustements salariaux individuels et la diffusion via les minima de branche.
14. [Albertini, Poirier et Terriau — Payroll Tax Reductions on Low Wages and Minimum Wage in France (2025)](https://pmb.cereq.fr/doc_num.php?explnum_id=12532) — modèle structurel des interactions entre SMIC, allègements et emploi.
15. [Sophie Cottet — Payroll Tax Reductions for Minimum Wage Workers (CESifo, 2024)](https://www.ifo.de/en/cesifo/publications/2024/working-paper/payroll-tax-reductions-minimum-wage-workers-relative-labor-cost-or) — étude sur les réactions des entreprises à une baisse des cotisations patronales.

## Conclusion provisoire

Le débat pertinent n'est pas de savoir si le SMIC doit être « haut » ou « bas » dans l'absolu. Il est de déterminer quel niveau et quel rythme permettent d'améliorer le revenu et la dignité du travail, tout en préservant les possibilités d'embauche, de progression professionnelle et d'investissement productif.

Le choix de politique publique doit comparer le SMIC avec les instruments qui l'entourent : prime d'activité, transferts, fiscalité, allègements patronaux, négociation collective, formation et politique de productivité. La conclusion restera conditionnelle tant que les effets causaux, les coûts complets et les effets distributifs ne seront pas établis.


## 13. Audit de preuve complémentaire — effets du SMIC et système socio-fiscal (13 novembre 2026)

### 13.1 Ce que le rapport du groupe d'experts 2025 établit — et ce qu'il n'établit pas

Le rapport 2025 du groupe d'experts documente plusieurs constats descriptifs importants : entre 2021 et 2025, le SMIC a progressé d'environ 17 %, contre environ 15 % pour les salaires de base et négociés en moyenne ; le ratio SMIC/salaire médian brut à temps plein atteint 62,5 % en 2024 selon la comparaison OCDE reprise dans le rapport ; le coût des allègements de cotisations est estimé à près de 75 Md€ en 2024 (environ 2,5 % du PIB). Le rapport identifie également des taux marginaux effectifs souvent compris entre 75 et 80 % entre 1,2 et 2 SMIC, liés à la combinaison du retrait des allègements, de la prime d'activité et de l'impôt, ainsi qu'une moindre progression salariale observée dans cette zone.

Ces éléments ne constituent pas, à eux seuls, une estimation causale de l'effet d'un « coup de pouce » donné sur l'emploi. Le ratio au salaire médian est un indicateur comparatif, non un seuil causal d'alerte. La progression salariale observée selon le salaire initial appelle une analyse de composition, de sélection et de trajectoires avant d'attribuer le ralentissement au seul barème socio-fiscal.

Source : Groupe d'experts SMIC, rapport 2025, publié le 12 décembre 2025 : https://www.strategie-plan.gouv.fr/publications/groupe-dexperts-smic-rapport-2025.

### 13.2 Réconcilier les ordres de grandeur 75 / 78 Md€ sans les fusionner

Le rapport du groupe d'experts SMIC 2025 indique près de 75 Md€ d'allègements en 2024. La note d'orientation du Haut Conseil des rémunérations, de l'emploi et de la productivité (16 décembre 2024) cite 78 Md€ pour l'ensemble des dispositifs d'exonération en 2024 selon le PLFSS, dont 66 Md€ pour les dispositifs généraux. Ces montants ne doivent pas être présentés comme une contradiction résolue ni comme une série homogène tant que ne sont pas rapprochés : périmètre (général / ensemble), traitement des exonérations ciblées, compensation, source comptable (PLFSS ou estimation du rapport), année de référence et éventuels arrondis.

Source HCREP : https://www.strategie.gouv.fr/files/2024-12/hcrep_2024_note_orientation_16_decembre_0.pdf. Source du groupe d'experts : lien ci-dessus. **Action restante :** reconstituer les tableaux et notes méthodologiques correspondants avant de choisir un chiffre de référence.

### 13.3 Trois familles d'études à ne pas confondre

| Travail | Méthode / objet | Résultat utilisable | Limite pour le débat sur une hausse du SMIC |
|---|---|---|---|
| Cottet (2024), CESifo WP 11076 | Données administratives employeurs-salariés ; évalue une baisse de cotisations patronales ciblant les emplois au minimum, en exploitant les variations de coût au niveau emploi et entreprise | Réponses hétérogènes : +13 points de hausse des emplois au minimum dans les entreprises auparavant peu exposées ; +4 % de croissance d'emploi sur deux ans dans les entreprises déjà exposées, tous niveaux de salaire confondus | Étudie une baisse de cotisations, pas une hausse du salaire minimum ; l'asymétrie des mécanismes interdit d'inverser directement le résultat |
| Albertini, Poirier et Terriau (2025), WP 25-01 | Modèle structurel d'appariement sur cycle de vie, hétérogénéité des travailleurs et interactions socio-fiscales | Les simulations du modèle prévoient des effets négatifs sur emploi et surplus budgétaire d'une hausse du SMIC, dépendants de l'indexation du barème d'allègements et des autres dispositifs | Résultat de modèle conditionnel aux hypothèses et à la calibration, non observation expérimentale d'emplois détruits |
| Groupe d'experts SMIC 2025 | Rapport institutionnel mobilisant données descriptives, travaux empiriques et analyses du système socio-fiscal | Documente compression salariale, exposition relative élevée et frictions de progression dans certaines tranches | Recommandation d'experts et diagnostic de politique publique ; ne remplace pas une identification causale d'un scénario précis |

Sources : Cottet, https://www.ifo.de/en/cesifo/publications/2024/working-paper/payroll-tax-reductions-minimum-wage-workers-relative-labor-cost-or ; Albertini, Poirier et Terriau, https://www.gate.cnrs.fr/RePEc/2025/2501.pdf ; Groupe d'experts SMIC 2025, lien ci-dessus.

### 13.4 Conclusion provisoire de cette revue

La preuve disponible invite à prendre au sérieux les coûts d'ajustement et les interactions socio-fiscales, mais elle ne justifie ni une élasticité unique de l'emploi au SMIC, ni l'affirmation que toute hausse détruit un nombre déterminé d'emplois. À l'inverse, les gains de salaire brut des personnes concernées ne suffisent pas à démontrer une hausse équivalente du niveau de vie ni une baisse de la pauvreté. Le bon objet d'évaluation reste un scénario précisément défini (montant, calendrier, indexation des allègements, prestations, horizon), mesuré simultanément sur revenus disponibles, emplois, heures, prix, marges, mobilité salariale et finances publiques.

**Travaux encore ouverts :** extraction des tableaux et annexes des rapports 2024-2025 ; réconciliation comptable 75/78 Md€ ; examen détaillé des stratégies d'identification de Cottet et des hypothèses/calibrations d'Albertini et al. ; mise en regard avec les données Dares sur les salariés directement concernés.
