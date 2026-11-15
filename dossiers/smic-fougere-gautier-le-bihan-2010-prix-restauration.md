# Audit — Fougère, Gautier & Le Bihan (2010) : transmission du SMIC aux prix de la restauration

- **Référence :** Denis Fougère, Erwan Gautier et Hervé Le Bihan, « Restaurant Prices and the Minimum Wage », *Journal of Money, Credit and Banking*, 42(7), 2010, pp. 1199–1234. Versions de travail : Banque de France WP 216 (2008), IZA DP 4070 (mars 2009).
- **Texte intégral audité :** https://docs.iza.org/dp4070.pdf
- **Notice Banque de France :** https://publications.banque-france.fr/en/economic-and-financial-publications-working-papers/restaurant-prices-and-minimum-wage
- **Nature de la preuve :** estimation microéconométrique structurelle de rigidité des prix et simulations de réponse agrégée ; pas d'expérience naturelle avec groupe témoin.
- **Période des prix :** juillet 1994 à février 2003.

## 1. Données et champ

Les auteurs exploitent les relevés individuels de prix collectés par l'Insee pour calculer l'IPC. Chaque observation suit le prix d'un produit précis dans un restaurant donné :
- repas en restaurant traditionnel : 93 816 relevés, 2 948 établissements ;
- repas en restauration rapide : 10 726 relevés, 448 établissements.

Les prix sont TTC. Les prix en francs antérieurs à 2002 sont convertis au taux officiel de 6,55957 francs pour un euro. L'analyse porte sur les repas complets, plus régulièrement renseignés que les plats isolés. Le secteur est pertinent car environ 40 % des salariés de la restauration sont rémunérés au SMIC dans le contexte étudié.

Il s'agit de prix de produits suivis dans des établissements, non de données comptables exhaustives sur les marges, la masse salariale ou les profits de chaque entreprise.

## 2. Traitement, contrefactuel et identification

Le SMIC est national et s'applique à toutes les entreprises : les auteurs indiquent qu'un groupe témoin géographique ou sectoriel non exposé, nécessaire à une différence-de-différences classique, n'est pas disponible.

Ils estiment un modèle microéconométrique de rigidité des prix de type état-dépendant, règle (S,s). Le modèle distingue la probabilité qu'un prix soit révisé, le sens de la révision et l'ampleur de la variation lorsqu'un prix change. Il tient compte du fait que les restaurants ne modifient pas leurs prix chaque mois et exploite la variation temporelle du SMIC et les décisions de prix au niveau des produits et établissements, avec des contrôles de coûts alimentaires, de demande et de facteurs calendaires.

**Point important :** le coût du travail au SMIC est construit en tenant compte des cotisations patronales. Sur la période, le taux de cotisation employeur au niveau du minimum passe d'environ 24,8 % à 12,0 % en septembre 1995, puis à 4,2 % en janvier 2003. Les hausses du salaire minimum et les baisses de cotisations se chevauchent donc. L'étude modélise le coût salarial et son environnement institutionnel ; elle ne doit pas être lue comme l'effet d'un choc de salaire brut isolé à cotisations constantes.

## 3. Résultats chiffrés

### 3.1 Réaction des prix lorsqu'ils sont révisés

Après une hausse de 1 % du SMIC, les prix effectivement modifiés augmentent d'environ :
- 0,08 % dans les restaurants traditionnels ;
- 0,117 % dans la restauration rapide, avec une estimation moins précise en raison d'un échantillon plus petit.

Ces coefficients conditionnels à la révision ne sont pas l'effet total sur le niveau des prix : ils ne portent que sur les prix qui changent.

### 3.2 Effet agrégé simulé à long terme

La simulation microéconomique estime qu'une hausse permanente de 1 % du SMIC conduit, à long terme, à :
- +0,097 % sur le niveau des prix des restaurants traditionnels ;
- +0,130 % sur le niveau des prix de la restauration rapide.

L'élasticité agrégée est donc de l'ordre de 0,10 dans les deux sous-secteurs. Une hausse de 1 % du minimum ne se traduit pas par une hausse de 1 % des prix : la répercussion estimée est partielle. Ces valeurs sont des réponses simulées dans le modèle, et non une hausse observée de l'IPC total.

### 3.3 Délai de transmission

La répercussion est lente :
- dans la restauration traditionnelle, environ la moitié de l'effet de long terme est réalisée après 14 mois ; environ 75 % après deux ans ;
- dans la restauration rapide, la demi-vie du choc est d'environ six mois et 75 % de l'effet est réalisé après douze mois.

Le mécanisme passe à la fois par l'ampleur des révisions et par une augmentation de la probabilité de réviser les prix.

## 4. Robustesse et contre-épreuve agrégée

Les auteurs comparent leur simulation microéconomique à des modèles linéaires estimés sur les séries agrégées de prix. Ces derniers donnent des résultats moins stables : pour les restaurants traditionnels, l'effet de long terme estimé varie approximativement de 0,015 à 0,148 selon les spécifications ; pour la restauration rapide, l'effet agrégé est très faible et peut devenir négatif selon les spécifications.

Les auteurs expliquent cette divergence par la difficulté à séparer la saisonnalité des hausses du SMIC, historiquement concentrées en juillet, et par la difficulté des modèles linéaires à représenter les ajustements discrets et hétérogènes des prix. Cette comparaison est importante : le résultat microéconomique est informatif, mais la mesure agrégée reste sensible à la spécification.

## 5. Limites déterminantes

1. **Pas de groupe témoin non exposé.** Le SMIC est national ; l'identification repose sur la structure du modèle et les variations temporelles, pas sur une différence-de-différences avec contrôle externe.
2. **Exogénéité conditionnelle.** Les simulations supposent que le SMIC est exogène aux prix de la restauration et que les prix des intrants alimentaires et la demande ne réagissent pas au choc. Les tests de causalité de Granger discutés par les auteurs ne prouvent pas une exogénéité structurelle complète.
3. **Équilibre partiel.** Les autres covariables sont maintenues sur leur trajectoire observée ; les boucles macroéconomiques, la demande, les salaires des autres secteurs et les réponses de politique économique ne sont pas simulés.
4. **Période ancienne.** Les données s'arrêtent en février 2003 ; la structure de la restauration, les coûts, les allègements et les modes de consommation ont changé depuis.
5. **Secteur particulier.** La forte part de salariés au SMIC et les caractéristiques de la restauration limitent la transposition aux autres secteurs.
6. **Pas d'effet sur l'emploi ou les marges.** L'étude mesure les prix, pas les créations/destructions d'emplois, les heures, les profits, les faillites ou l'investissement.
7. **Choc permanent simulé.** Le scénario maintient le SMIC durablement au-dessus de sa trajectoire de référence à partir de juillet 1998 ; il ne reproduit pas un épisode historique précis avec tous ses effets macroéconomiques.

## 6. Conclusion probatoire

- Le coût salarial lié au SMIC peut être transmis, au moins partiellement, aux prix de la restauration.
- La transmission estimée est partielle : environ 0,10 % de hausse du niveau des prix du secteur pour une hausse permanente de 1 % du SMIC, dans les simulations microéconomiques.
- La transmission est retardée et hétérogène selon le type de restaurant.
- Les prix constituent donc une marge d'ajustement réelle ; il serait erroné de supposer que le coût est nécessairement absorbé uniquement par les marges ou l'emploi.

L'étude ne permet pas d'affirmer qu'une hausse de 1 % du SMIC augmente l'IPC général de 0,10 %, que tous les secteurs réagissent de la même façon, que les hausses de 2021–2024 ont produit le même effet, ni que les marges ou l'emploi ont baissé. Il faudrait relier les hausses récentes à des données contemporaines de prix, d'exposition salariale, de coûts intermédiaires, de marges et d'emploi avec un contrefactuel crédible.

| Proposition | Résultat | Niveau de preuve |
|---|---|---|
| Le SMIC influence les prix des restaurants | Effet positif et significatif dans le modèle microéconométrique | Modéré |
| Une hausse de 1 % du SMIC se transmet intégralement aux prix | Non : réponse agrégée simulée proche de 0,10 % | Rejeté dans le champ et le modèle |
| La transmission est immédiate | Non : plus d'un an, jusqu'à deux ans pour une grande partie de l'effet | Modéré |
| Le résultat vaut pour tous les secteurs et toutes les périodes | Non démontré | Insuffisant |
| Le SMIC détruit des emplois ou réduit les marges dans la restauration | Non étudié | Insuffisant |

**Conclusion opérationnelle :** la répercussion sur les prix est un canal d'ajustement empirique à prendre au sérieux. Elle réduit une partie du gain réel pour les consommateurs, mais l'étude ne permet ni de chiffrer l'effet sur l'inflation générale ni de calculer le bilan net pour les salariés. Ce canal doit être évalué à côté de l'emploi, des heures, des marges et des revenus disponibles, sans devenir à lui seul un argument pour ou contre une revalorisation.

## 7. Références

- Fougère, Gautier & Le Bihan (2008), Banque de France WP 216 : https://publications.banque-france.fr/sites/default/files/medias/documents/working-paper_216_2008.pdf
- Fougère, Gautier & Le Bihan (2009), IZA DP 4070 : https://docs.iza.org/dp4070.pdf
- Version publiée (2010), *Journal of Money, Credit and Banking*, 42(7), 1199–1234 : https://doi.org/10.1111/j.1538-4616.2010.00332.x
