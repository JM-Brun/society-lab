# Audit — Abowd, Kramarz & Margolis (1999) : salaire minimum et transitions d'emploi en France

- **Référence :** John M. Abowd, Francis Kramarz et David N. Margolis, *Minimum Wages and Employment in France and the United States*, NBER Working Paper 6996, mars 1999.
- **Texte intégral :** https://www.nber.org/system/files/working_papers/w6996/w6996.pdf
- **Nature :** analyse longitudinale de transitions individuelles, avec groupes définis par la position salariale relative au SMIC ; comparaison pseudo-expérimentale, et non expérience naturelle randomisée.
- **Question :** les hausses du SMIC réel en France modifient-elles la probabilité qu'un salarié reste en emploi ?

## 1. Données, période et population

Les données françaises proviennent des fichiers de recherche de l'Enquête Emploi de l'Insee pour 1981–1989. L'enquête porte sur environ 60 000 ménages, interrogés en mars pendant trois années consécutives, avec renouvellement annuel d'un tiers de l'échantillon. Le suivi longitudinal est lié à l'adresse du domicile : les personnes qui déménagent peuvent sortir du panel. Les auteurs construisent des fichiers appariés d'une année sur l'autre, de 1981–1982 à 1988–1989.

Les variables mobilisées sont le statut d'emploi, le salaire mensuel usuel et les heures hebdomadaires usuelles. Le salaire horaire est reconstruit à partir du salaire mensuel et des heures. Le salaire déclaré est net des cotisations salariales et inclut l'impôt sur le revenu selon la description des auteurs. Les heures déclarées peuvent être bruitées ; l'étude signale des déclarations au-delà de la durée légale, ce qui peut affecter le salaire horaire reconstruit.

L'analyse est conduite séparément par sexe et groupes d'âge. Elle porte sur des individus observés en emploi à la date initiale pour l'analyse des sorties d'emploi ; elle ne mesure donc pas à elle seule l'ensemble du chômage, de la participation ou de la qualité des emplois.

## 2. Traitement et groupe de comparaison

Le SMIC réel augmente pendant la période française étudiée. Les auteurs classent les salariés selon leur salaire réel en année t :
- **sous le minimum** ;
- **entre le SMIC de t et celui de t+1** : salariés « rattrapés » par la hausse réelle ;
- **marginalement au-dessus du nouveau minimum**, jusqu'à 15 % au-dessus : groupe de comparaison ;
- **nettement au-dessus**.

Le groupe « rattrapé » est celui dont le salaire réel, inchangé, serait inférieur au nouveau SMIC réel l'année suivante. Le groupe juste au-dessus sert de comparaison, car il est supposé présenter des trajectoires proches tout en étant moins directement exposé au relèvement.

Les auteurs estiment la probabilité d'être encore en emploi en t+1 selon la position salariale en t et les caractéristiques observées. Ils cherchent à isoler la différence de réaction entre le groupe au minimum et le groupe marginalement supérieur. La variation temporelle du SMIC réel fournit le choc, tandis que la proximité salariale construit le contraste.

## 3. Résultats principaux

Le résumé du NBER rapporte, pour une hausse de 1 % du SMIC réel, une baisse de la probabilité future d'emploi des salariés au minimum relativement au groupe marginalement supérieur de :
- **1,3 % pour les hommes** ;
- **1,0 % pour les femmes**.

Ces chiffres sont des élasticités conditionnelles au groupe de travailleurs déjà employés et au contraste avec les salariés légèrement au-dessus du minimum. Ils ne signifient pas que l'emploi total en France diminue de 1,3 % ou 1,0 %.

Le tableau récapitulatif 5 du document fournit aussi des élasticités dites « inconditionnelles », qui intègrent la part des salariés concernés dans l'ensemble de la population considérée :
- hommes : **−0,015** ;
- femmes : **−0,022**.

La différence d'ordre de grandeur est essentielle : le risque estimé est concentré sur les personnes directement exposées, alors que l'effet moyen rapporté sur la probabilité d'emploi agrégée est beaucoup plus faible dans cette spécification.

L'introduction indique également que les effets sont plus importants chez les jeunes hommes concernés ; les élasticités conditionnelles rapportées pour certains groupes d'âge sont de −3,2 pour les 26–30 ans et −4,3 pour les 31–35 ans. Ces estimations par âge ne doivent pas être généralisées à l'ensemble des jeunes ni interprétées sans leurs erreurs-types et la définition précise des sous-échantillons.

## 4. Ce que l'identification permet — et ne permet pas

**Points forts**
- Données individuelles longitudinales plutôt que seules séries macroéconomiques.
- Mesure directe des transitions emploi/non-emploi.
- Groupe de comparaison proche dans la distribution salariale.
- Contrôle de caractéristiques individuelles et analyse séparée par âge et sexe.
- Le contraste vise la population effectivement rattrapée par la hausse réelle, plutôt qu'un effet moyen indistinct sur tous les salariés.

**Limites**
1. **Groupe témoin endogène au salaire.** Les salariés juste au-dessus du SMIC peuvent différer en productivité, ancienneté, secteur ou trajectoire ; la proximité salariale ne garantit pas des tendances parallèles.
2. **Pas d'étude événementielle moderne des pré-tendances.** La stratégie ne fournit pas le type de graphique pré/post et de test des tendances préalables aujourd'hui attendu pour une différence-de-différences.
3. **Variation du SMIC agrégée et nationale.** Les hausses coïncident avec les évolutions macroéconomiques ; le groupe salarial proche atténue certains biais, sans éliminer tous les chocs différentiels.
4. **Mesure du salaire horaire.** Le salaire mensuel est observé par intervalles et les heures usuelles sont bruitées ; le ratio salaire/heures peut classer imparfaitement les individus autour du seuil.
5. **Attrition du panel.** Le suivi à domicile perd les personnes qui déménagent ; si la mobilité est corrélée aux trajectoires professionnelles, le panel apparié peut être sélectionné.
6. **Résultat sur les personnes en emploi.** L'étude des sorties ne mesure pas symétriquement les chances d'embauche des personnes initialement sans emploi.
7. **Contexte institutionnel ancien.** 1981–1989 précède les allègements de cotisations patronales massifs des années 1990 et les réformes ultérieures ; le coût employeur n'est pas identique à celui d'aujourd'hui.
8. **Pas de bilan de bien-être.** L'étude ne mesure ni le revenu disponible des ménages, ni les heures, les prix, les marges ou les trajectoires salariales complètes.

## 5. Interprétation correcte

L'étude apporte un signal défavorable ciblé : les salariés déjà en emploi dont le salaire est directement rattrapé par une hausse du SMIC réel présentent une probabilité ultérieure d'emploi plus faible que des salariés proches mais légèrement au-dessus du nouveau plancher. L'effet est plus marqué pour certains groupes d'âge.

Elle ne démontre pas que toute hausse du SMIC détruit massivement des emplois, ni que le taux de chômage global augmente d'autant. Le chiffre conditionnel (−1,3 %/−1,0 %) doit être distingué de l'effet inconditionnel beaucoup plus faible (−0,015/−0,022).

## 6. Classement probatoire

| Proposition | Conclusion | Niveau de preuve |
|---|---|---|
| Les salariés directement rattrapés présentent davantage de sorties relatives de l'emploi | Résultat négatif estimé dans les données françaises 1981–1989 | Modéré |
| L'effet est uniforme pour tous les salariés | Non : il est concentré autour du minimum et varie selon l'âge/sexe | Rejeté |
| L'emploi total baisse de 1,3 % pour chaque hausse de 1 % du SMIC | Non : confusion entre élasticité conditionnelle et inconditionnelle | Rejeté |
| Le SMIC réduit les embauches des chômeurs | Non estimé par ce résultat principal | Insuffisant |
| Le même effet s'applique aux hausses de 2021–2024 | Non démontré | Insuffisant |

**Conclusion opérationnelle :** cette étude empêche de considérer comme acquis que les hausses n'ont aucun coût d'emploi pour les salariés au voisinage immédiat du plancher. Elle ne suffit toutefois pas à quantifier le bilan agrégé d'une revalorisation actuelle. Elle doit être confrontée à Kramarz & Philippon (2001), qui étudient explicitement le coût total employeur et les allègements de cotisations pendant les années 1990.

## 7. Références

- NBER Working Paper 6996 (1999) : https://www.nber.org/papers/w6996
- Version PDF : https://www.nber.org/system/files/working_papers/w6996/w6996.pdf
- Abowd, Kramarz, Lemieux & Margolis (1997), étude spécifique sur les jeunes : https://www.nber.org/papers/w6111
