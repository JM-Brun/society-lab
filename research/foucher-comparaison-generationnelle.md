---
id: "STUDY-FOUCHER-GENERATIONAL-COMPARISON-2026"
title: "Comparer les générations à âge identique : état des preuves et protocole de mise à jour"
domain_ids: ["DOMAIN-ECONOMY", "DOMAIN-SOCIETY", "DOMAIN-FINANCE"]
status: "in_progress"
last_reviewed: "2026-11-18"
geographic_scope: ["France"]
temporal_scope: "Pseudo-panel 1979-2011 ; données contemporaines 1996-2024 ; patrimoine et transmissions 2023-2024"
source_ids:
  - "SOURCE-INSEE-GENERATIONS-DALBIS-BADJI-2017"
  - "SOURCE-INSEE-LEVEL-BY-AGE-1996-2024"
  - "SOURCE-INSEE-PATRIMOINE-AGE-2024"
  - "SOURCE-INSEE-INTERGEN-TRANSMISSIONS-2024"
concept_ids:
  - "CONCEPT-DECLASSEMENT-ECONOMIQUE-RELATIF"
  - "CONCEPT-PACTE-INTERGENERATIONNEL"
---

# Comparer les générations à âge identique

## Question

Les personnes nées après 1970 disposent-elles, au même âge que leurs parents, de ressources économiques et patrimoniales plus faibles ? La question doit être testée sur plusieurs dimensions et ne peut être tranchée par une comparaison instantanée entre jeunes et retraités.

## 1. Résultat empirique de référence : d’Albis et Badji (2017)

L’étude exploite les éditions de l’enquête Budget de famille de 1979 à 2011 dans un pseudo-panel, avec des modèles âge-période-cohorte inspirés de Deaton et Paxson. Elle examine le revenu disponible et la consommation privée par unité de consommation, avec variantes selon la prise en compte des dépenses de logement et des loyers imputés.

Ses résultats publiés indiquent :
- entre 25 et 64 ans, le niveau de vie mesuré par la consommation augmente fortement avec l’âge ; la consommation des 50-54 ans est supérieure de 35 % à celle des 25-29 ans ;
- la cohorte née en 1946 a une consommation estimée supérieure de 40 % à celle née en 1926, mais inférieure de 20 % à celle née en 1976 ;
- sur les cohortes nées de 1901 à 1979, les auteurs concluent qu’aucune génération n’a été désavantagée par rapport à ses aînées selon les indicateurs et stratégies d’identification retenus.

**Portée :** c’est un résultat directement pertinent contre l’idée générale d’une inversion déjà démontrée du progrès intergénérationnel en matière de consommation et de niveau de vie.

**Limites :** les données s’arrêtent en 2011 ; l’étude ne couvre pas les cohortes nées après 1979 sur leur vie adulte, ne constitue pas une mesure exhaustive du patrimoine net et des transmissions, et ses résultats dépendent des choix d’identification âge-période-cohorte. Ce résultat n’exclut donc pas un retournement plus récent, ni des dégradations sur des dimensions particulières (logement, endettement, stabilité de l’emploi, patrimoine d’entrée dans la vie adulte).

## 2. Ce que les données récentes ajoutent — et n’ajoutent pas

### Niveau de vie selon l’âge, 1996-2024

L’Insee publie une série de niveaux de vie médians par tranche d’âge en euros 2024 constants. En 2024, les médianes sont notamment de 25 860 € pour les 18-29 ans, 27 610 € pour les 30-39 ans, 29 590 € pour les 50-64 ans et 27 340 € pour les 65-74 ans.

Ces valeurs décrivent des groupes d’âge observés en 2024, pas les mêmes cohortes suivies au cours du temps. Elles ne permettent pas d’affirmer que les 18-29 ans de 2024 vivent mieux ou moins bien que les 18-29 ans de 1996 sans reconstituer des cohortes et harmoniser les changements de champ et de production statistique. L’Insee signale notamment une rénovation de la chaîne ERFS à partir de 2020.

### Patrimoine

Début 2024, le patrimoine brut médian des ménages est de 26 100 € pour les moins de 30 ans et de 245 000 € pour les 60-69 ans. Cette différence est attendue en partie du fait de l’accumulation au cours du cycle de vie. Elle ne mesure ni le patrimoine net par cohorte au même âge, ni les conditions d’accès à la propriété rencontrées par chaque génération.

L’enquête Histoire de vie et Patrimoine 2023-2024 couvre les actifs immobiliers, financiers et professionnels, les dettes, ainsi que les héritages, donations et aides. Les résultats sur les transmissions publiés en avril 2026 sont une source essentielle pour mesurer les inégalités d’accumulation entre ménages d’une même génération.

## 3. Protocole de comparaison à construire

| Dimension | Indicateur principal | Comparaison requise | Précaution |
|---|---|---|---|
| Ressources courantes | Revenu disponible par UC, médiane et déciles | Même âge, cohortes différentes, euros constants | Composition du ménage et transferts |
| Consommation | Dépenses par UC, avec et sans logement | Même âge et nomenclature stable | Loyers imputés, qualité des biens |
| Logement | Statut d’occupation, taux d’effort, surface, localisation | Même âge et statut familial | Prix locaux, taux d’intérêt, qualité |
| Patrimoine | Patrimoine brut, dettes, patrimoine net | Même âge et cohorte | Héritages, donations, endettement |
| Travail | Taux d’emploi, salaire annuel et horaire, précarité | Même âge, sexe et niveau de diplôme | Durée travaillée, chômage, carrières |
| Transferts privés | Aides, donations et héritages reçus | Âge de réception et origine sociale | Déclaratif, transferts intrafamiliaux |
| Services publics | Santé, éducation, prestations en nature | Cohorte et étape du cycle de vie | Valorisation monétaire conventionnelle |

Le tableau final devra comporter au minimum trois cohortes et deux âges de référence, avec médianes, D1/D9 ou déciles, intervalles d’incertitude lorsque disponibles et résultats ventilés par sexe, origine sociale, statut d’emploi et territoire si les effectifs le permettent.

## 4. Identification : âge, période et cohorte

L’identité année = âge + année de naissance crée une colinéarité exacte. Les effets d’âge, de période et de cohorte ne sont donc pas tous identifiables sans restrictions ou hypothèses supplémentaires. Toute estimation doit :
1. expliciter la restriction d’identification retenue ;
2. présenter des spécifications alternatives (APC, APC avec tendance contrainte, approches fondées sur l’espérance de vie ou autres stratégies justifiées) ;
3. montrer les résultats descriptifs bruts en parallèle des estimations ajustées ;
4. tester la sensibilité aux classes d’âge/cohortes et aux ruptures d’enquête ;
5. ne pas présenter une décomposition statistique comme une preuve causale.

## 5. Conclusion provisoire

À ce stade, **les preuves disponibles ne valident pas une affirmation générale selon laquelle les générations récentes vivraient moins bien que leurs parents au même âge**. L’étude de référence disponible conclut plutôt à une progression intergénérationnelle de la consommation jusqu’aux cohortes étudiées, mais ses données s’arrêtent en 2011. Les données récentes documentent les niveaux de vie par âge, le patrimoine et les transmissions, sans encore constituer une comparaison complète de cohortes à âge identique.

La formulation la plus rigoureuse est donc : le déclassement générationnel global reste une hypothèse à tester ; certaines dimensions et certains groupes peuvent néanmoins connaître une détérioration relative, masquée par les moyennes. La question du logement, du patrimoine net et de la transmission est prioritaire.

## Sources

- d’Albis, H. & Badji, I. (2017), [Les inégalités de niveaux de vie entre les générations en France](https://www.insee.fr/fr/statistiques/2647428), *Économie et Statistique*, 491-492.
- Insee (2026), [Niveau de vie selon l’âge, données annuelles 1996-2024](https://www.insee.fr/fr/statistiques/2416878).
- Insee (2026), [Montants de patrimoine brut des ménages, données 2024](https://www.insee.fr/fr/statistiques/8894780).
- Insee (2026), [Transmissions intergénérationnelles en 2024 : donations, héritages et aides](https://www.insee.fr/fr/statistiques/8960228).
