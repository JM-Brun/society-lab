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
  - "SOURCE-INSEE-PATRIMOINE-NET-ENDETTEMENT-2024"
  - "SOURCE-INSEE-HVP-ACCESS-2023-2024"
  - "SOURCE-INSEE-HVP-METHODOLOGY-2023-2024"
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


## 3 bis. Ce que révèlent les transmissions (HVP 2023-2024)

L'enquête Histoire de vie et Patrimoine 2023-2024 a recueilli les réponses de 11 940 ménages en France hors Mayotte. Elle couvre les patrimoines financier, immobilier, professionnel et résiduel, l'endettement, les héritages, les donations, les aides financières et des éléments biographiques. Les revenus sont appariés aux données fiscales et sociales de 2022. Les résultats publiés sont fondés sur les déclarations des répondants et ne sont pas calés sur les masses de la comptabilité nationale.

Début 2024 :
- 41 % des ménages ont déjà hérité au moins une fois au cours de leur vie ; 20 % ont déjà reçu une donation déclarée ; 7 % ont versé une donation.
- Le patrimoine brut médian atteint 306 600 € pour les ménages ayant déjà hérité, 435 900 € pour ceux ayant reçu une donation, et 205 100 € pour l'ensemble des ménages.
- Le patrimoine brut moyen est respectivement de 515 400 €, 698 300 € et 374 900 €.
- 60 % des ménages ayant hérité ont une personne de référence âgée d'au moins 60 ans, contre 40 % de l'ensemble des ménages ; seuls 3 % des ménages ayant hérité ont une personne de référence de moins de 30 ans, contre 9 % de l'ensemble.

**Lecture correcte :** ces écarts sont des associations descriptives entre expérience de transmission et patrimoine observé, pas l'effet causal net d'un héritage ou d'une donation. Les ménages ayant hérité sont plus âgés et ont eu davantage de temps pour accumuler ; l'origine sociale, la composition familiale, le niveau de patrimoine des parents et les trajectoires résidentielles jouent aussi. Le patrimoine observé après transmission mêle le transfert reçu, l'épargne ultérieure, les rendements, les dettes et les autres événements du cycle de vie.

La définition statistique doit également être conservée : un ménage est considéré comme concerné si au moins un membre a reçu un héritage ou une donation au cours de sa vie ; les caractéristiques détaillées de la transmission sont recueillies auprès de la personne de référence et de son conjoint. Les montants peuvent être déclarés à la date de transmission ou à la date de l'enquête, le plus souvent à la date de transmission. Les donations prises en compte sont les donations déclarées auprès d'un notaire, d'un avocat ou de l'administration fiscale. Les aides familiales couvrent notamment dons ponctuels ou réguliers, logement gratuit, paiement de loyer et prêts d'argent.

## 3 ter. Patrimoine net, dette et comparaison à âge identique

Début 2024, le patrimoine brut médian de l'ensemble des ménages est de 205 100 €, tandis que le patrimoine net médian, après déduction des emprunts, est de 148 100 €. La différence est substantielle et interdit d'utiliser le patrimoine brut comme équivalent du patrimoine effectivement détenu.

L'Insee publie également une série de patrimoine brut moyen par âge en euros 2024 pour 2015, 2021 et 2024. À titre d'exemple, à 25 ans, le patrimoine brut moyen est estimé à 140 000 € en 2015, 159 000 € en 2021 et 155 500 € en 2024. Cette comparaison à âge identique entre vagues est plus pertinente qu'une comparaison jeunes/seniors à une date donnée, mais elle ne constitue pas encore le test demandé : il s'agit d'une moyenne, non d'une médiane ou d'une distribution nette, les classes d'âge fines sont sensibles aux effectifs, et la série ne comprend que trois vagues. Il faut éviter d'interpréter la variation 2015-2024 comme une trajectoire individuelle ou un effet générationnel pur.

L'Insee indique par ailleurs que le patrimoine immobilier augmente fortement entre 30 et 45 ans, période d'acquisition fréquente de la résidence principale, et que les ménages de 50 à 79 ans détiennent 61 % de la masse patrimoniale pour 50 % des ménages. Ces constats rendent prioritaire une comparaison de l'accès à la propriété, du taux d'effort, de la dette immobilière et du patrimoine net par âge.

## 3 quater. Limites d'inférence et prochaines extractions

1. Les tableaux agrégés sur les transmissions ne suffisent pas à estimer l'effet d'une transmission à âge, origine sociale, structure familiale et patrimoine parental comparables.
2. Les transmissions déclarées ne couvrent pas nécessairement les aides informelles non monétaires ou non déclarées ; les aides financières recensées ont un périmètre défini par l'enquête.
3. L'enquête est un panel rotatif depuis 2014, mais la page de résultats agrégés ne fournit pas à elle seule un panel longitudinal exploitable pour suivre chaque cohorte de naissance.
4. Pour une comparaison robuste, il faut exploiter les tableaux détaillés par âge, catégorie socioprofessionnelle, revenu et patrimoine, puis obtenir si possible les microdonnées HVP et leur documentation.
5. Comparer séparément : (a) avoir déjà reçu une transmission, (b) âge au moment de la transmission, (c) montant et nature, (d) patrimoine net actuel, (e) situation de logement et endettement.

La prochaine livraison doit produire une matrice par âge/cohorte, avec indicateurs de patrimoine net, accession à la propriété et transmissions, en distinguant résultats publiés, estimations recalculées et questions encore non identifiables.


## 3 quinquies. Accès aux données : une voie réaliste pour passer aux microdonnées

La documentation Insee indique que les données HVP 2023-2024 sont mises à disposition des chercheurs et institutions sur Quetelet-Progedo et au CASD depuis début 2026. Les fichiers de production et de recherche (FPR) sur Quetelet-Progedo offrent un niveau de détail supérieur aux tableaux grand public ; les données individuelles plus détaillées sont accessibles au CASD après autorisation du Comité du secret statistique. La disponibilité n'équivaut donc pas à un accès libre et immédiat.

Le plan de sondage HVP 2023-2024 combine des ménages réinterrogés issus des vagues précédentes et un échantillon entrant. La collecte s'effectue au niveau du ménage, tandis que le suivi longitudinal est réalisé au niveau des individus. Il faut donc identifier les identifiants longitudinaux et les pondérations adaptées avant de construire des trajectoires ; la simple juxtaposition des ménages de chaque vague ne suffit pas.

**Plan opérationnel :** commencer par vérifier le catalogue Quetelet-Progedo, les fichiers disponibles, dictionnaires, pondérations et règles de chaînage ; établir ensuite une table de correspondance des variables de patrimoine net, âge, cohorte, logement et transferts. Si le niveau de détail des FPR est insuffisant, documenter une demande CASD. En attendant, les tableaux publics permettent de cadrer les hypothèses, mais pas de produire une estimation microéconomique propre.


### Repères complémentaires de patrimoine brut moyen à âge fixe (euros 2024)

La figure Insee 2b publie des moyennes par âge exact en 2015, 2021 et 2024. Quelques âges repères :

| Âge de la personne de référence | 2015 | 2024 | Variation réelle 2015-2024 |
|---:|---:|---:|---:|
| 25 ans | 140 000 € | 155 500 € | +11,1 % |
| 30 ans | 182 600 € | 211 300 € | +15,7 % |
| 35 ans | 244 600 € | 263 700 € | +7,8 % |
| 38 ans | 278 100 € | 294 700 € | +6,0 % |

Ces évolutions sont calculées à âge identique et en euros 2024, mais elles portent sur le **patrimoine brut moyen**. Elles ne prouvent pas que la cohorte née en 1999 possède un patrimoine supérieur à celle née en 1990 dans des conditions comparables : les ménages observés à chaque âge diffèrent par leur composition, leur statut d'activité, leur structure familiale et leur sélection statistique. La moyenne est en outre sensible aux patrimoines très élevés. Le résultat ne remplace donc pas une comparaison des médianes et déciles de patrimoine net, du taux de propriété, du capital restant dû et de l'accès aux transmissions. Il constitue néanmoins un premier test descriptif à âge fixe et invite à ne pas présupposer une baisse générale du patrimoine moyen des jeunes adultes.
