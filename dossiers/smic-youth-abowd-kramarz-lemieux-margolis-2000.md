# Fiche d’audit — Abowd, Kramarz, Lemieux & Margolis (1997/2000)

- **Référence :** John M. Abowd, Francis Kramarz, Thomas Lemieux et David N. Margolis, « Minimum Wages and Youth Employment in France and the United States », chapitre 11 de *Youth Employment and Joblessness in Advanced Countries*, University of Chicago Press / NBER, 2000, p. 427–472.
- **Version de travail :** NBER Working Paper 6111, juillet 1997.
- **Sources primaires :** [chapitre intégral (PDF NBER)](https://www.nber.org/system/files/chapters/c6813/c6813.pdf) ; [notice du WP 6111](https://www.nber.org/papers/w6111).
- **Statut :** lecture du chapitre intégral ; données, modèle, tableaux 11.1 à 11.5 et 11.9, et conclusion vérifiés.
- **Périmètre de cette fiche :** résultats français. Les résultats américains servent à comprendre le dispositif comparatif, pas à inférer un effet français.

## 1. Question, population et période

Les auteurs étudient les transitions d’emploi des jeunes de 30 ans ou moins, en France et aux États-Unis. En France, ils exploitent la hausse du SMIC réel sur 1982–1989 ; aux États-Unis, la stabilité du minimum nominal sur 1981–1987, qui correspond à une baisse de sa valeur réelle avec l’inflation.

La partie française utilise l’Enquête Emploi de l’INSEE :
- environ 60 000 ménages interrogés en mars pendant trois années consécutives, avec renouvellement d’un tiers de l’échantillon chaque année ;
- individus appariés d’une année sur l’autre de 1982–1983 à 1988–1989, sous réserve de rester à la même adresse ;
- rémunération mensuelle habituelle déclarée par tranche, nette des cotisations salariales mais incluant l’impôt sur le revenu, et heures hebdomadaires habituelles ;
- salaire horaire estimé à partir de la tranche de rémunération et des heures ; les auteurs tiennent compte du caractère catégoriel de la mesure ;
- emploi défini selon le critère BIT : au moins une heure rémunérée pendant la semaine de référence de mars.

Les régressions conditionnelles françaises des tableaux 11.3 et 11.4 portent sur 30 804 observations de jeunes hommes et 26 434 de jeunes femmes. Ce sont des observations d’analyse, pas nécessairement autant de personnes distinctes sur toute la période.

## 2. Traitement, groupe de comparaison et méthode

### 2.1 Groupe exposé

Pour la France, les auteurs classent comme « entre les deux minima » les salariés dont le salaire horaire réel en t est au moins égal au SMIC réel de t, mais inférieur au SMIC réel de t+1. Le relèvement réel du SMIC les rattrape donc mécaniquement si leur rémunération ne progresse pas.

Ils distinguent également les personnes rémunérées sous le minimum légal dans des dispositifs dérogatoires, notamment les stages et contrats de promotion de l’emploi, ainsi que les apprentis.

### 2.2 Groupe de comparaison

Le groupe de comparaison central est celui des salariés rémunérés marginalement au-dessus du SMIC, initialement jusqu’à 1,10 fois le SMIC. Les auteurs testent aussi des seuils de 1,15 et 1,20.

Ce groupe n’est pas un groupe « non traité » au sens expérimental : il est proche du plancher, peut subir les effets de diffusion et peut différer des salariés exposés sur des caractéristiques non observées.

### 2.3 Modèles

Deux approches sont mobilisées :
1. un logit multinomial sur les transitions entre emploi, chômage et inactivité, estimé sur la population plus large, pour décrire l’hétérogénéité des transitions selon la position dans la distribution salariale ;
2. un logit conditionnel sur les jeunes, estimant la probabilité d’être encore en emploi en t+1 parmi les personnes en emploi en t, en fonction de la hausse réelle du SMIC, de la position salariale et de l’âge.

Les contrôles incluent notamment l’année, le niveau d’éducation, la région (Île-de-France), l’âge, l’expérience professionnelle (polynôme jusqu’au degré 4), l’ancienneté et le salaire horaire (polynôme jusqu’au degré 3), ainsi que le type de contrat et les dispositifs aidés.

L’identification repose sur l’hypothèse que les salariés juste au-dessus du minimum constituent un contrefactuel pertinent pour ceux qui sont rattrapés par la hausse. Les auteurs supposent qu’ils partagent des caractéristiques non observées affectant les transitions, et que les différences restantes reflètent l’effet plus direct du minimum.

## 3. Résultats français : ne pas confondre les estimands

### 3.1 Résultat conditionnel central

Le tableau 11.9 donne, pour les jeunes hommes français, une élasticité conditionnelle agrégée de **−2,489** ; pour les jeunes femmes, **−1,044**. Il s’agit d’une moyenne pondérée des différences d’élasticité entre le groupe « au minimum » et le groupe « marginalement au-dessus », par classe d’âge.

Interprétation : dans le cadre du modèle, une hausse de 1 % du SMIC réel est associée à une baisse relative de la probabilité de maintien en emploi d’environ 2,49 % pour les jeunes hommes concernés, comparativement au groupe de référence proche du seuil. Ce n’est pas une baisse de 2,49 % de l’emploi de l’ensemble des jeunes.

### 3.2 Élasticité dite inconditionnelle

Le même tableau 11.9 fournit des estimations beaucoup plus faibles : **−0,203** pour les jeunes hommes et **−0,108** pour les jeunes femmes.

Ces valeurs ne sont pas directement estimées de la même façon. Les auteurs utilisent une identité de probabilités et doivent poser une hypothèse sur un terme qu’ils ne peuvent pas identifier en France, car le SMIC réel augmente sur toute la période : ils supposent que la hausse du SMIC ne modifie pas le taux auquel les personnes sans emploi accèdent à l’emploi.

Il faut donc présenter les deux résultats ensemble, en explicitant la différence d’estimand et l’hypothèse supplémentaire de l’estimation inconditionnelle. Le chiffre de −2,5 % ne doit jamais être isolé comme effet agrégé.

### 3.3 Hétérogénéité par âge et sexe

Dans le tableau 11.3, le signal masculin est surtout porté par les 25–30 ans : interaction du groupe « entre les deux minima » de −33,2708, erreur-type 9,9755, p = 0,0009, élasticité rapportée −4,8928. Les coefficients pour les hommes de 16–19 ans et 20–24 ans ne sont pas statistiquement significatifs dans cette spécification agrégée.

Pour les femmes, les coefficients du groupe « entre les deux minima » ne sont pas significatifs dans les trois grandes classes d’âge (p = 0,8667 ; 0,1999 ; 0,1383). Dans la spécification plus détaillée du tableau 11.4, certains coefficients par âge deviennent significatifs, notamment à 23 ans pour les femmes (p = 0,0107), mais les auteurs signalent eux-mêmes la difficulté d’interprétation de ce profil et la faiblesse des effectifs dans les cellules.

### 3.4 Part de la population exposée

Les auteurs indiquent que les groupes « entre les deux minima » sont relativement petits : environ 8 % des jeunes hommes et 10 % des jeunes femmes en France. Ils en déduisent que les élasticités conditionnelles élevées peuvent coexister avec des élasticités inconditionnelles beaucoup plus faibles.

## 4. Contrats aidés et mécanisme institutionnel

Les dispositifs français autorisant temporairement une rémunération sous le SMIC comprennent notamment les contrats/stages d’insertion et les travaux d’utilité collective (TUC), ainsi que l’apprentissage. Plusieurs dispositifs étaient réservés aux jeunes de 25 ans ou moins.

Les auteurs observent une protection relative de certains jeunes éligibles aux dispositifs de promotion de l’emploi face aux hausses du SMIC réel. Ils interprètent le décrochage observé autour de 25 ans, en particulier pour les hommes rattrapés par le nouveau minimum, comme compatible avec la fin de cette protection et des allègements associés.

Ce mécanisme est important pour l’analyse historique, mais ne doit pas être transposé mécaniquement aux contrats aidés contemporains : règles, publics et incitations ont changé.

## 5. Robustesses, incertitude et limites

### Éléments de robustesse

- Les auteurs testent trois définitions du groupe « marginalement au-dessus » : 1,10, 1,15 et 1,20 fois le SMIC.
- Ils décrivent les résultats comme robustes à ces variations. Le tableau 11.5 présente les coefficients et erreurs-types pour les jeunes jusqu’à 25 ans.
- La prise en compte des catégories d’âge permet d’examiner la sortie d’éligibilité aux dispositifs d’emploi et les ruptures de trajectoire autour de 25 ans.

### Limites d’identification

1. **Sélection et hétérogénéité non observée :** les auteurs reconnaissent ne pas pouvoir contrôler complètement l’hétérogénéité individuelle non observée. Ils supposent que le groupe juste au-dessus du SMIC en capte une partie suffisante.
2. **Groupe témoin imparfait :** le groupe de comparaison est proche du SMIC et peut lui-même être affecté par la diffusion salariale, les minima de branche ou les chocs sectoriels.
3. **Pas de véritable événement de réforme avec pré-tendances :** la stratégie exploite les variations annuelles du SMIC réel et la position salariale ; elle ne fournit pas un event-study avec coefficients pré-traitement permettant de vérifier des tendances parallèles.
4. **Petites cellules :** plusieurs différences par âge et sexe ne sont pas significatives. Les auteurs soulignent que les résultats détaillés, notamment féminins, sont parfois difficiles à interpréter.
5. **Robustesse limitée :** varier le seuil du groupe de comparaison ne résout pas les problèmes de sélection non observée ni l’absence de pré-tendances.
6. **Appariement conditionné à l’adresse :** les personnes qui déménagent peuvent sortir du suivi ; attrition et sortie d’emploi doivent être distinguées.
7. **Périmètre de l’échantillon conditionnel :** les logit conditionnels portent sur les personnes employées à un moment de la période. Les auteurs avertissent que les résultats ne représentent pas nécessairement toute la population potentiellement active.
8. **Mesure du salaire :** le salaire horaire est approximé à partir de tranches mensuelles et des heures habituelles, ce qui peut classer imparfaitement les personnes autour du seuil.

### Résultats non étudiés

Les heures ne sont pas un résultat estimé. L’étude ne mesure pas les effets sur les prix, les marges, la productivité, le revenu disponible des ménages ou le bien-être global. Elle étudie des transitions annuelles binaires d’emploi, pas le nombre d’heures, la qualité des emplois ou la durée précise du chômage.

## 6. Synthèse et niveau de preuve

**Constat principal :** dans les données françaises de 1982–1989, les jeunes salariés dont la rémunération réelle est rattrapée par le relèvement du SMIC présentent, dans certaines spécifications et surtout chez les hommes de 25–30 ans, une probabilité de maintien en emploi plus faible que les salariés proches mais juste au-dessus du seuil.

**Résultat à citer avec précaution :** l’élasticité conditionnelle agrégée de −2,489 pour les jeunes hommes ne décrit que le contraste entre groupes proches du minimum. L’élasticité inconditionnelle calculée par les auteurs est de −0,203, avec une hypothèse supplémentaire sur les transitions depuis le non-emploi.

**Contrepoids important :** les dispositifs dérogatoires et contrats de promotion de l’emploi semblent avoir amorti une partie de l’effet pour les jeunes éligibles ; le profil par âge est donc indissociable du contexte institutionnel de l’époque.

**Niveau de confiance :**
- modéré pour le constat de différences de transitions dans cet échantillon historique ;
- faible à modéré pour l’interprétation causale, compte tenu du groupe témoin endogène, de l’hétérogénéité non observée, des petites cellules et de l’absence de pré-tendances ;
- faible pour toute extrapolation à une hausse du SMIC dans la France actuelle.

**Conclusion opérationnelle :** conserver cette étude comme preuve historique ciblée sur les trajectoires de jeunes salariés proches du minimum, mais toujours publier ensemble l’estimation conditionnelle et l’estimation inconditionnelle, avec leurs hypothèses. Ne pas agréger son chiffre à celui du WP 6996 de 1999.

## 7. Sources

- Abowd, Kramarz, Lemieux & Margolis (2000), chapitre 11, notamment sections 11.3 à 11.7, tableaux 11.1 à 11.5 et 11.9 : https://www.nber.org/system/files/chapters/c6813/c6813.pdf
- NBER Working Paper 6111 (juillet 1997) : https://www.nber.org/papers/w6111
- Notice de la version publiée : https://www.nber.org/books-and-chapters/youth-employment-and-joblessness-advanced-countries/minimum-wages-and-youth-employment-france-and-united-states
