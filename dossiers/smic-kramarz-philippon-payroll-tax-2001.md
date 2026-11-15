# Fiche d’audit — Kramarz & Philippon (2001), coût du travail minimum et exonérations

- **Référence publiée :** Francis Kramarz et Thomas Philippon, « The Impact of Differential Payroll Tax Subsidies on Minimum Wage Employment », *Journal of Public Economics*, 82(1), octobre 2001, p. 115–146. DOI : [10.1016/S0047-2727(00)00137-7](https://doi.org/10.1016/S0047-2727(00)00137-7).
- **Version de travail consultée :** IZA Discussion Paper 219, novembre 2000, [texte intégral PDF](https://docs.iza.org/dp219.pdf).
- **Statut :** lecture du texte intégral de la version IZA ; données, cadre institutionnel, équations, tableaux 1 à 6 et annexe descriptive vérifiés.
- **Avertissement d'interprétation :** l'étude porte sur le **coût total du travail au voisinage du SMIC**, qui combine salaire minimum et cotisations patronales. Elle ne mesure pas isolément l'effet d'une hausse du taux légal du SMIC.

## 1. Question et contexte institutionnel

L'étude analyse les variations du coût employeur des bas salaires en France entre 1990 et 1998. Le SMIC réel augmente sur la période, tandis que les exonérations de cotisations patronales sont introduites puis fortement amplifiées à partir de 1993–1996.

Au niveau du SMIC, les auteurs rapportent une baisse des cotisations patronales de 36,49 % du salaire en 1993 à 21,77 % en 1996. En septembre 1995, le dispositif est renforcé : la réduction au voisinage du SMIC atteint environ 18 points de cotisations. Les barèmes sont ensuite étendus de façon dégressive jusqu'à environ 1,33 SMIC.

Cette configuration permet d'observer des années de hausse du coût minimum et des années de baisse du coût minimum. C'est la variation du coût employeur, et non la seule hausse du salaire minimum, qui constitue le traitement économique central.

## 2. Données, population et construction du coût

- Source : Enquête Emploi de l'INSEE, 1990–1998 ; appariements annuels 1990–1991 à 1997–1998.
- Plan d'enquête : environ 60 000 ménages interrogés en mars pendant trois années consécutives, un tiers renouvelé chaque année ; le suivi individuel dépend du maintien à la même adresse.
- Échantillon : 169 385 observations dans l'échantillon complet de l'annexe A ; les effectifs des groupes « between » et « marginal » dans cette annexe descriptive sont respectivement 5 815 et 11 828.
- Salaire : rémunération mensuelle habituelle, nette des cotisations salariales mais incluant l'impôt sur le revenu. Les heures hebdomadaires déclarées étant jugées trop bruitées, les auteurs utilisent le salaire mensuel et le statut temps plein/temps partiel pour construire le coût ; pour le temps partiel, ils calculent un équivalent temps plein à partir des heures déclarées.
- Emploi : personne ayant travaillé au moins une heure rémunérée pendant la semaine de référence de mars.
- Exclusions : jeunes de moins de 25 ans dans des programmes publics spéciaux (apprentissage, stages, SIVP, etc.), fonctionnaires et salariés du secteur public, ainsi que les personnes déclarant moins de 95 % du SMIC sans signaler un régime dérogatoire (moins de 5 % du fichier initial).

Les contrôles comprennent notamment année, sexe, âge, éducation, ancienneté, type de contrat, temps partiel, expérience potentielle et salaire.

## 3. Traitement et groupes de comparaison

### 3.1 Hausse du coût minimum

Dans les années de hausse du coût minimum, le groupe « between » est constitué des salariés dont le coût réel en t se situe entre l'ancien et le nouveau coût minimum. Le groupe « marginal » regroupe les salariés juste au-dessus, environ entre le nouveau minimum et 1,10 fois celui-ci.

### 3.2 Baisse du coût minimum

Dans les années de baisse, le groupe « between » est défini dans la partie basse de la distribution (environ 0,98 à 1,05 fois le coût minimum), tandis que le groupe « marginal » se situe approximativement entre 1,05 et 1,15 fois le minimum.

### 3.3 Stratégie économétrique

Les auteurs estiment des logits conditionnels sur les transitions :
- sortie de l'emploi : probabilité d'être non-employé en t+1, conditionnellement à l'emploi en t ;
- entrée dans l'emploi : probabilité d'avoir été employé en t, conditionnellement à l'emploi en t+1.

Ils comparent les différences entre groupes pendant les années de hausse et les années de baisse du coût minimum. Les spécifications en différences-de-différences incluent des indicatrices de groupe et des interactions entre groupe et variation du coût. Une autre spécification autorise des effets asymétriques entre hausses et baisses.

Les auteurs justifient l'emploi du groupe « marginal » comme contrôle par un modèle de demande et d'offre du travail. Leur argument théorique est que la réponse propre du groupe témoin aux variations de coût doit être faible ; ils examinent empiriquement si les écarts observés pour ce groupe changent entre périodes.

## 4. Résultats sur les sorties de l'emploi

### 4.1 Estimations séparées par période

Dans le tableau 1, pour les années 1990–1992 de hausse du coût minimum :
- élasticité estimée pour le groupe « between » : −2,59 ;
- élasticité pour le groupe « marginal » : −0,94 ;
- différence d'élasticité : −1,64 ;
- coefficient différentiel : −8,31, erreur-type 3,11.

Pour l'année de baisse de coût (1995 dans la nomenclature du tableau) :
- différence d'élasticité : +0,05 ;
- coefficient différentiel : 0,73, erreur-type 1,64, non significatif selon les auteurs.

Ces résultats indiquent une asymétrie : la baisse du coût ne produit pas un effet miroir évident de la hausse sur la stabilité de l'emploi.

### 4.2 Différences-de-différences symétriques

Le tableau 2 regroupe les années 1990–1992 et 1997 (hausses), et 1993 et 1995 (baisses). La différence d'élasticité est de −0,38 ; le coefficient différentiel est −2,63, erreur-type 1,37. Les auteurs qualifient le résultat de statistiquement significatif, mais l'effet est plus faible que dans les spécifications séparées.

### 4.3 Différences-de-différences asymétriques

Le tableau 3 autorise des coefficients distincts selon que le coût augmente ou diminue :
- différence d'élasticité dans les années de hausse : −1,56 ;
- différence d'élasticité dans les années de baisse : −0,03 ;
- contraste différentiel final entre les deux régimes : coefficient −8,37, erreur-type 3,14.

Les auteurs retiennent une élasticité d'environ **−1,5** : une hausse de 1 % du coût minimum est associée, pour le groupe directement rattrapé, à une hausse d'environ 1,5 % de la probabilité de transition vers le non-emploi, relativement au groupe de comparaison.

Le groupe directement exposé représente environ 3 à 4 % de la population salariée dans les estimations. Les auteurs en déduisent que l'effet agrégé sur l'ensemble du marché du travail est beaucoup plus limité que l'effet relatif sur ce petit groupe.

**Interprétation à conserver :** −1,5 est une élasticité différentielle de transition vers le non-emploi par rapport au groupe proche du seuil, dans un dispositif portant sur le coût total employeur. Ce n'est ni une élasticité de l'emploi total, ni une estimation de l'effet d'une hausse du SMIC brut isolée des cotisations.

## 5. Résultats sur les entrées dans l'emploi

Les résultats d'entrée sont nettement moins convaincants :
- les estimations par année montrent des différences parfois importantes, mais le même phénomène apparaît pendant des périodes de hausse comme de baisse des coûts, ce qui suggère une hétérogénéité structurelle des travailleurs du bas de la distribution ;
- dans les tableaux 5 et 6, les effets différentiels regroupés sont petits et non significatifs ;
- le coefficient différentiel de la spécification asymétrique pour les années de hausse est de 0,10 (SE 4,70), et le contraste final entre régimes est −1,84 (SE 4,97).

Les auteurs concluent que les exonérations ont un effet faible et statistiquement non significatif sur l'entrée depuis le non-emploi. Ils signalent toutefois des changements de transitions à l'intérieur de la distribution salariale et des indices de substitution entre certains salariés bénéficiaires des exonérations et ceux situés au-dessus de la zone aidée.

## 6. Robustesse et qualité du groupe témoin

Les auteurs soutiennent que le groupe « marginal » est un contrôle raisonnable :
- les variations de ses probabilités de transition entre années de hausse et de baisse sont généralement faibles et non significatives ;
- leur modèle théorique explicite les conditions dans lesquelles les réactions du groupe témoin ne contaminent pas la différence-de-différences ;
- l'analyse des transitions dans la distribution salariale ne révèle pas de substitution manifeste entre « between » et « marginal », mais suggère une substitution possible entre des travailleurs situés dans la zone d'exonération (notamment autour de 1,20–1,33 SMIC) et des travailleurs juste au-dessus.

Cette validation reste partielle. Les auteurs reconnaissent que les effets multiples des changements fiscaux et salariaux rendent l'identification difficile. Ils indiquent qu'une analyse directe des politiques d'embauche des entreprises serait nécessaire, mais hors du périmètre de l'article.

## 7. Limites d'identification et de transposition

1. **Instrument composite :** le traitement combine le salaire minimum légal, les cotisations patronales et les exonérations. Impossible d'attribuer −1,5 à la hausse du SMIC seule.
2. **Asymétrie des ajustements :** hausse et baisse du coût ne sont pas symétriques ; une exonération n'est pas l'inverse mécanique d'une hausse du salaire.
3. **Groupe témoin imparfait :** le groupe marginal peut être affecté par les changements de barème, les effets de diffusion ou des substitutions avec les catégories au-dessus.
4. **Pas d'étude d'événement pré-tendances :** les auteurs mobilisent une différence-de-différences entre périodes de hausse et de baisse et des contrôles de groupe, mais ne présentent pas de test graphique ou statistique de tendances préalables comparable à un event-study moderne.
5. **Chocs concomitants :** les réformes de cotisations, les changements de barèmes, les revalorisations du SMIC et la conjoncture évoluent ensemble ; les auteurs eux-mêmes soulignent la difficulté à isoler les effets.
6. **Données de salaire imparfaites :** les heures déclarées sont bruitées ; les salaires mensuels et le statut temps plein/partiel sont utilisés pour approcher le coût horaire.
7. **Population exclue :** les jeunes de moins de 25 ans en contrats ou programmes dérogatoires et le secteur public sont exclus ; les résultats ne décrivent donc pas ces populations.
8. **Sorties de panel :** le suivi dépend du maintien à la même adresse ; l'attrition peut affecter les transitions observées.
9. **Validité externe :** barèmes d'exonération et institutions des années 1990 différents des dispositifs actuels.

## 8. Synthèse et niveau de preuve

**Constat central :** les hausses du coût minimum employeur sont associées à une augmentation des transitions vers le non-emploi pour les salariés directement rattrapés, relativement à des salariés proches du seuil. Le contraste différentiel est de l'ordre de −1,5 en élasticité dans la spécification asymétrique.

**Résultat sur les exonérations :** les baisses de coût ne produisent pas un effet miroir statistiquement établi sur les entrées dans l'emploi. Les effets sur les embauches sont petits et non significatifs dans les estimations regroupées.

**Niveau de confiance :**
- modéré pour l'existence d'un différentiel de transition dans les années et groupes étudiés ;
- faible à modéré pour l'attribution causale au coût minimum, compte tenu des réformes concomitantes et de l'absence de pré-tendances ;
- faible pour une transposition à une hausse contemporaine du SMIC brut.

**Conséquence pour la synthèse du SMIC :** cette étude est utile pour documenter les réactions au coût employeur et l'interaction entre SMIC et exonérations. Elle ne doit pas être présentée comme une estimation causale pure de l'effet du SMIC. Elle complète les études Abowd et al. sur le salaire minimum, mais ne se confond ni avec elles ni avec Cottet (2024), qui étudie une autre réforme et une autre unité d'analyse.

## 9. Sources

- Kramarz & Philippon (2001), *Journal of Public Economics*, 82(1), 115–146 : https://doi.org/10.1016/S0047-2727(00)00137-7
- Version intégrale IZA DP 219 (novembre 2000) : https://docs.iza.org/dp219.pdf
- Notice éditeur : https://www.sciencedirect.com/science/article/pii/S0047272700001377
