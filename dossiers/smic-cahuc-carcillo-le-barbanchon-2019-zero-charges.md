# Audit d'étude — Cahuc, Carcillo & Le Barbanchon (2019), crédit d'embauche « zéro charges » (2009)

- **Référence :** Pierre Cahuc, Stéphane Carcillo et Thomas Le Barbanchon, « The Effectiveness of Hiring Credits », *Review of Economic Studies*, 86(2), 2019, p. 593–626. Version de travail : IZA Discussion Paper n°11248, décembre 2017.
- **Question :** quel est l'effet d'une baisse temporaire et ciblée du coût du travail sur les embauches et l'emploi des petites entreprises françaises ?
- **Attention au périmètre :** cette étude évalue un crédit d'embauche réservé aux nouveaux salariés, et non une hausse du SMIC, ni une baisse générale de cotisations portant sur tous les salariés.

## 1. Dispositif étudié

Le dispositif « zéro charges » est annoncé le 4 décembre 2008 dans le plan de relance. Il s'applique aux embauches (et à certains renouvellements de contrats temporaires) réalisées jusqu'au 31 décembre 2009 dans les entreprises privées de moins de 10 équivalents temps plein, selon leur effectif moyen antérieur à l'annonce. Les postes éligibles sont rémunérés sous 1,6 SMIC et doivent durer au moins un mois ; les emplois déjà couverts par certains dispositifs ciblés sont exclus.

La réduction est maximale au SMIC : elle diminue le coût du travail d'environ 12 %, jusqu'à 2 400 euros sur douze mois. Elle s'ajoute aux allègements généraux déjà existants. La mesure est donc temporaire, non anticipée, limitée aux nouveaux entrants et concentrée sur une fraction des entreprises et des emplois. Elle a ensuite été prolongée pour certaines embauches jusqu'en juin 2010 ; les auteurs concentrent l'identification principale sur 2009, avant les problèmes de sélection liés à la prolongation.

## 2. Données et population

Les auteurs combinent :
- les DADS de l'Insee, qui décrivent les périodes d'emploi, heures et rémunérations par salarié ;
- les fichiers administratifs de Pôle emploi sur les entreprises ayant demandé le crédit et les montants versés.

Les DADS couvrent environ 85 % des salariés, mais excluent notamment les administrations publiques et, à cette date, les salariés des particuliers employeurs. Le champ de l'évaluation est le secteur privé couvert par ces sources. Le traitement porte sur les entreprises et les embauches éligibles ; **les résultats ne sont pas une estimation spécifique aux jeunes**, même si les emplois à bas salaire comprennent des jeunes.

## 3. Identification

Deux stratégies complémentaires sont mobilisées.

1. **Différences de différences au niveau des entreprises :** entreprises de 6 à moins de 10 ETP (traitées) comparées à celles de 10 à moins de 14 ETP (témoins), de novembre 2008 à novembre 2009. La taille est mesurée avant l'annonce, ce qui limite la manipulation opportuniste du seuil. Les auteurs contrôlent notamment les effets année, secteur, région et leurs interactions, l'âge de l'entreprise, sa taille économique, la part de bas salaires et de temps partiel ainsi que la composition professionnelle.
2. **Variable instrumentale sur cellules bassin d'emploi × secteur :** la part des embauches éligibles observée avant la réforme (2006–2008) instrumente la part des embauches subventionnées en 2009. Les contrôles comprennent les tendances antérieures, des caractéristiques des entreprises et de la cellule ainsi que des indicateurs financiers.

La comparaison n'est pas une régression sur la variation du SMIC légal : le choc exogène est l'éligibilité au crédit d'embauche autour du seuil de 10 salariés.

## 4. Résultats principaux

Dans la spécification de référence en différences de différences, le crédit augmente de **0,8 point de pourcentage le taux de croissance de l'emploi** du groupe traité en 2009 (erreur-type rapportée de 0,2 point ; significatif à 1 %). La croissance des heures travaillées augmente d'environ 0,9 point, ce qui ne suggère pas une substitution des heures des salariés déjà présents par celles des nouveaux embauchés.

La décomposition par type de poste indique un effet concentré sur les emplois éligibles (sous 1,6 SMIC et d'au moins un mois) : environ +1,1 point sur leur croissance d'emploi, contre un effet faible et non significatif sur les emplois non éligibles. Les auteurs ne trouvent pas d'augmentation significative des séparations ni d'effet sur la survie des entreprises. Ils ne détectent pas de hausse salariale attribuable au dispositif.

Les auteurs calculent une élasticité de l'emploi au changement de coût induit par le crédit d'environ **−4**, avec un intervalle de confiance à 95 % de **[−6 ; −2]**. Cette valeur ne doit pas être assimilée à l'élasticité standard d'une hausse du coût salarial de tous les salariés : le crédit ne porte que sur les nouveaux entrants. En réexprimant le choc comme une variation du coût salarial de l'ensemble des salariés, les auteurs obtiennent une élasticité plus conventionnelle d'environ **−1**, avec un intervalle à 95 % de **[−1,5 ; −0,5]**.

## 5. Tendances préalables et robustesses

Les auteurs exploitent les trajectoires mensuelles des entreprises de 2006 à 2011. Les écarts d'évolution de l'emploi entre petites et moyennes entreprises ne divergent pas avant l'annonce ; les placebo de 2007 et 2008 ne détectent pas d'effet différentiel comparable à celui de 2009. Les annexes ajoutent :
- des placebo temporels pour les résultats de la stratégie instrumentale ;
- des seuils placebo de taille d'entreprise ;
- plusieurs bandes de taille autour du seuil (notamment 7–13, 6–14 et 5–15 ETP) ;
- des estimations pondérées par l'emploi ;
- des tests sur la composition des embauches, les heures et les séparations.

Les résultats principaux restent positifs et statistiquement significatifs dans ces variantes. Les auteurs ne trouvent pas d'accumulation anormale d'entreprises juste sous le seuil de 10 ETP, malgré quelques différences réglementaires mineures à ce seuil.

## 6. Limites et validité externe

- Le traitement est une **subvention temporaire aux nouveaux embauchés**, pas une baisse générale du coût de tous les salariés. Il cible la marge d'embauche, pas directement la rétention des salariés en poste.
- Le caractère non anticipé, la durée limitée, la crise de 2008–2009, le chômage élevé et le ciblage des petites entreprises sont des éléments constitutifs du résultat.
- L'évaluation en différences de différences porte sur des entreprises déjà observées dans la bande 6–14 ETP ; les créations d'entreprises nouvelles ne sont pas dans cet échantillon.
- Le seuil de 10 ETP est institutionnellement imparfait, même si les auteurs ne trouvent pas de bunching et utilisent des placebo.
- Les résultats sur les effets d'équilibre et les politiques permanentes reposent en partie sur un modèle structurel et des simulations, pas sur une expérience observée.
- Aucun effet propre aux moins de 25 ans n'est identifié dans les résultats présentés.
- Il serait erroné de convertir l'élasticité −4 en effet d'une hausse du SMIC brut : le traitement ne touche que les nouveaux embauchés. Même l'élasticité standard −1 reste propre au choc et au contexte étudiés.

## 7. Niveau de confiance et conclusion opérationnelle

**Confiance modérée à élevée** pour l'effet local du crédit temporaire sur la croissance de l'emploi des petites entreprises éligibles en 2009 : le seuil de taille, les données administratives, les pré-tendances, les placebo et les stratégies complémentaires renforcent l'identification.

**Confiance faible pour toute extrapolation** à une baisse permanente des cotisations, à une hausse du SMIC, à l'ensemble des entreprises ou à l'emploi des jeunes. Le résultat établit surtout que le ciblage des nouveaux entrants et le caractère temporaire peuvent modifier fortement la réponse de l'emploi au coût.

Conclusion : cette étude doit figurer dans le dossier SMIC comme preuve sur un mécanisme de coût employeur et sur l'efficacité d'un crédit d'embauche ciblé, **jamais comme estimation de l'effet d'une hausse du SMIC**.

## Sources primaires et vérifications

- Cahuc, Carcillo & Le Barbanchon (2017), IZA DP 11248, PDF intégral : https://www.econstor.eu/bitstream/10419/177052/1/dp11248.pdf
- Version publiée, *Review of Economic Studies* (2019) : https://doi.org/10.1093/restud/rdy011
- Notice IZA : https://www.iza.org/publications/dp/11248/the-effectiveness-of-hiring-credits
- CASD, description du projet et du seuil d'éligibilité : https://www.casd.eu/en/project/labor-demand-and-finance/
- Bozio & Wasmer (2024), rapport France Stratégie sur les exonérations, notamment la discussion des élasticités et des allègements récents : https://www.strategie-plan.gouv.fr/files/2024-11/rapport_vffff_241003.pdf
