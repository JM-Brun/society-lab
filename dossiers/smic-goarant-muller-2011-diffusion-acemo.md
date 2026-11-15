# Fiche d'audit — Goarant & Muller (2011), diffusion du SMIC dans les salaires mensuels

- **Référence :** Claire Goarant et Lara Muller, « Les effets des hausses du Smic sur les salaires mensuels dans les entreprises de 10 salariés ou plus de 2006 à 2009 », *Emploi et salaires*, INSEE Références, édition 2011, p. 69–81.
- **Source primaire :** [PDF INSEE/DARES](https://www.insee.fr/fr/statistiques/fichier/1373824/empsal11f.pdf).
- **Statut :** lecture complète du dossier, des encadrés méthodologiques, des tableaux et graphiques 1 à 12, ainsi que des résultats par convention collective.
- **Question :** dans quelle mesure une revalorisation du SMIC se diffuse-t-elle aux salaires de base au-dessus du minimum, à court terme et à un an ?
- **Champ principal :** postes représentatifs des entreprises de 10 salariés ou plus en France métropolitaine, 2006–2009 ; données trimestrielles ACEMO.

## 1. Données et population effectivement observée

L'étude utilise l'enquête trimestrielle ACEMO de la DARES. Chaque trimestre, elle interroge environ **33 000 établissements** d'entreprises de 10 salariés ou plus en France métropolitaine. Les établissements de plus de 250 salariés sont présents en permanence dans l'échantillon ; les autres le sont pendant quatre années consécutives.

Chaque établissement déclare, pour douze niveaux de poste représentatifs de sa grille de classification, le salaire mensuel brut de base et l'horaire mensuel de base. L'unité d'observation est donc un **poste dans un établissement à une date donnée**, et non nécessairement le même salarié suivi individuellement.

- Période des données disponibles : T3 1999 à T2 2009.
- Champ de l'analyse : entreprises d'au moins 10 salariés ; secteurs marchand non agricole, avec exclusions détaillées de l'administration, agriculture, activités des ménages, associations d'action sociale et autres secteurs indiqués par les auteurs.
- Les secteurs de l'éducation, de la santé et de l'action sociale sont écartés de l'étude.
- Les postes doivent être présents deux trimestres consécutifs : 18 % des observations sont ainsi écartées.
- Les variations de salaire très fortes liées au remplacement du salarié référent du poste sont filtrées : environ 9 % des observations restantes.
- Les salaires horaires inférieurs à 0,8 SMIC, jugés incohérents, sont supprimés (0,3 %). Les salaires légèrement inférieurs au SMIC sont conservés, car le salaire de base observé n'est pas exactement l'assiette légale de vérification du SMIC.
- Sur 5 636 244 observations disponibles, 4 229 905 sont conservées ; 1 463 719 concernent 2006–2009.

**Limite de couverture importante :** les entreprises de moins de 10 salariés sont absentes. Or elles concentrent 26,5 % des salariés concernés par les revalorisations du SMIC, contre 10,2 % de l'ensemble des salariés au 1er juillet 2009. Les résultats ne sont donc pas directement représentatifs des très petites entreprises, qui sont particulièrement exposées au SMIC.

Le salaire mensuel brut de base ne correspond pas exactement à l'assiette légale de vérification du SMIC, qui inclut notamment certaines primes. Les auteurs le considèrent néanmoins comme une approximation satisfaisante au regard des autres sources disponibles.

## 2. Traitement et contexte institutionnel

Jusqu'en 2009, la revalorisation annuelle intervient généralement au 1er juillet. Une hausse anticipée intervient au deuxième trimestre 2008 lorsque le seuil légal d'inflation est franchi. La date annuelle est avancée au 1er janvier à partir de 2010.

Avant la convergence des minima au 1er juillet 2005, plusieurs GMR coexistent avec le SMIC horaire. Pour construire une variable unique de revalorisation, les auteurs calculent une moyenne pondérée de l'évolution du SMIC et des GMR, pondérée par les effectifs des établissements auxquels chaque minimum s'applique.

Cette convention est importante : **la variable de traitement n'est pas toujours la seule hausse du SMIC horaire légal**. Elle agrège les minima applicables dans les établissements pendant la période de coexistence des GMR.

Entre 2006 et 2009, le SMIC horaire augmente en moyenne de 2,4 % par an, contre 4,4 % entre 2000 et 2005 pendant la convergence des GMR. La période étudiée est donc celle de hausses plus modérées que l'épisode institutionnel précédent.

## 3. Stratégie économétrique

Les auteurs estiment un modèle de croissance trimestrielle du salaire mensuel brut de base d'un poste :

- variable expliquée : variation du logarithme du salaire mensuel de base entre deux trimestres ;
- variable principale : variation du logarithme du SMIC moyen, croisée avec la tranche de rémunération du poste au trimestre précédent ;
- tranches : 1–1,1 SMIC, 1,1–1,2, 1,2–1,3, etc., jusqu'à 3 SMIC ou plus (catégorie de référence) ;
- effets temporels par trimestre, pour absorber les chocs communs, dont la conjoncture, l'inflation et le chômage ;
- contrôles de la réduction du temps de travail et des périodes de modération salariale ;
- contrôles de taille d'établissement, de convention collective et de catégorie socioprofessionnelle du poste.

Une variante remplace les tranches de salaire par des déciles de salaire horaire. Les auteurs estiment également une spécification avec effets fixes d'établissement : les conclusions sur la diffusion sont similaires.

Pour l'horizon d'un an, ils comparent les salaires du deuxième trimestre précédant une hausse à leur valeur quatre trimestres plus tard.

**Nature de l'identification :** le modèle compare la progression des salaires des postes situés à différents niveaux de la hiérarchie, autour des dates de revalorisation, en neutralisant les facteurs observés et les chocs temporels communs. Ce n'est pas une expérience aléatoire ni une différence-de-différences fondée sur un groupe traité et un groupe témoin dont les pré-tendances seraient démontrées. La catégorie supérieure à 3 SMIC sert de référence.

## 4. Résultats immédiats par niveau de salaire

Quand le SMIC augmente de 1 % entre deux trimestres, le salaire mensuel de base des postes rémunérés entre 1 et 1,1 SMIC augmente de **0,38 point de plus** que celui des postes rémunérés au-delà de 3 SMIC, après contrôles.

Effets estimés (graphique 6, coefficients lus dans le document) :

| Tranche de salaire | Effet différentiel immédiat (points) |
|---|---:|
| 1,0–1,1 SMIC | 0,38 |
| 1,1–1,2 SMIC | 0,13 |
| 1,2–1,3 SMIC | 0,09 |
| 1,3–1,4 SMIC | 0,06 |
| 1,4–1,5 SMIC | 0,05 |
| 1,5–1,6 SMIC | 0,03 |
| 1,6–1,8 SMIC | 0,04 |
| 1,8–2,0 SMIC | 0,02 |
| 2,0–2,2 SMIC | 0,01 |
| 2,2–2,4 SMIC | 0,02 |
| au-delà de 2,4 SMIC | généralement non significatif |

L'effet est donc fortement concentré sur les postes immédiatement au-dessus du plancher. Il devient faible à partir de 1,1–1,2 SMIC et quasiment nul au-delà de 2 SMIC dans la spécification moyenne.

Il faut interpréter les coefficients comme des **écarts de progression en points par rapport à la catégorie de référence**, et non comme une hausse de 0,38 % de tous les salaires ni comme une élasticité de l'emploi.

## 5. Diffusion retardée et horizon d'un an

Les auteurs introduisent des termes retardés afin de distinguer l'effet immédiat de la revalorisation et les ajustements des trimestres suivants.

Le résultat est nuancé :
- l'effet immédiat est le plus fort pour les postes entre 1 et 1,1 SMIC ;
- un effet positif subsiste au trimestre suivant pour les postes les plus proches du minimum ;
- au deuxième trimestre suivant, des effets négatifs apparaissent sur plusieurs tranches de salaire ;
- les auteurs interprètent cette dynamique comme une compression initiale du bas de la grille, partiellement compensée ensuite par une progression plus forte des salaires qui avaient été moins touchés lors de la revalorisation.

À l'horizon d'un an, une hausse de 1 % du SMIC a un effet différentiel estimé de **0,16 point** pour les postes initialement rémunérés entre 1 et 1,1 SMIC. Au-delà de 1,1 SMIC, l'effet annuel n'est plus statistiquement significatif dans la spécification présentée.

Les résultats sont proches sur la période 1999–2005, avec un effet annuel légèrement plus marqué pour les postes de 1 à 1,1 SMIC. Le rattrapage salarial observé après deux ou trois trimestres dans la période 2006–2009 n'est toutefois pas retrouvé de la même façon sur 1999–2005.

## 6. Différences selon les branches conventionnelles

Les auteurs estiment le modèle séparément pour treize conventions collectives couvrant chacune plus de 100 000 salariés et suffisamment représentées dans ACEMO. Seuls les coefficients significatifs au seuil de 5 % sont affichés.

La diffusion est plus forte et s'étend plus haut dans la grille lorsque :
- la branche compte une proportion importante de salariés proches du SMIC ;
- les minima conventionnels de branche sont eux-mêmes proches du SMIC.

Quelques effets immédiats approximatifs pour les postes de 1 à 1,1 SMIC :
- entreprises de propreté : 0,61 point ;
- industrie chimique : 0,42 ;
- plasturgie : 0,43 ;
- bâtiment ouvrier : 0,30 ;
- commerce alimentaire : 0,40 ;
- prévention et sécurité : 0,13 ;
- métallurgie région parisienne : 0,22.

Dans les branches du commerce alimentaire et de la prévention-sécurité, où environ 40 % des salariés sont entre 1 et 1,1 SMIC, la diffusion est pourtant plus faible et limitée aux postes entre 1 et 1,2 SMIC. Les auteurs relient prudemment ce résultat aux efforts de revalorisation des minima conventionnels au-dessus du SMIC engagés depuis 2005.

Ces chiffres par branche sont des lectures de graphiques, et ne doivent pas être traités comme des coefficients exacts de tableaux de régression. Les banques et les travaux publics cadres n'apparaissent pas, faute de coefficients significatifs.

## 7. Tendances préalables, robustesse et limites d'identification

**Tendances préalables :** l'article ne présente pas de test de pré-tendances de type event-study entre catégories de salaire. Les indicatrices temporelles absorbent les chocs communs et les contrôles par tranche de salaire absorbent les différences moyennes, mais ils ne démontrent pas que les catégories auraient suivi des trajectoires parallèles en l'absence de revalorisation.

**Robustesse :**
- déciles de salaire horaire à la place des tranches en multiples du SMIC : résultats similaires ;
- effets fixes d'établissement : conclusions similaires ;
- comparaison à un an sur les seuls deuxièmes trimestres : effet persistant uniquement pour les postes initialement entre 1 et 1,1 SMIC.

**Limites principales :**
1. **Pas d'effet sur l'emploi :** l'unité est un poste représentatif. Si le salarié change, l'établissement sélectionne un autre salarié de même coefficient. Les destructions et créations d'emplois liées aux hausses du SMIC ne sont donc pas observées.
2. **TPE exclues :** les établissements de moins de 10 salariés, qui concentrent une part disproportionnée des salariés au SMIC, sont hors champ.
3. **Salaire de base seulement :** les primes et compléments entrant dans l'assiette légale ne sont pas intégralement observés.
4. **Sélection des postes :** les postes doivent être observés deux trimestres consécutifs ; les fortes variations liées au changement de salarié référent sont filtrées.
5. **GMR et SMIC agrégés :** avant juillet 2005, le traitement est une moyenne pondérée des différents minima, pas une hausse unique du SMIC légal.
6. **Contexte de la RTT :** les effets de modération salariale liés aux accords de 35 heures sont contrôlés, mais restent une dimension institutionnelle importante de la période.
7. **Identification non expérimentale :** les résultats sont conditionnels à la spécification et aux contrôles ; l'étude ne démontre pas des pré-tendances parallèles.
8. **Pas de mesure du revenu disponible :** les effets sur les salaires de base ne permettent pas de conclure sur le revenu net, les prestations, la pauvreté ou le niveau de vie.

## 8. Synthèse et niveau de preuve

**Constat principal :** les hausses du SMIC se diffusent rapidement dans les salaires mensuels de base proches du minimum. L'effet immédiat est le plus fort entre 1 et 1,1 SMIC (0,38 point différentiel pour une hausse de 1 % du minimum), décroît rapidement et devient quasiment nul au-delà de 2 SMIC. La diffusion dépend fortement des grilles conventionnelles et de la proximité de leurs minima avec le SMIC.

**Temporalité :** une partie de la diffusion se produit dans les deux trimestres suivant la revalorisation. Elle est ensuite partiellement compensée par une progression moins rapide des bas salaires et un rattrapage des catégories moins touchées. À un an, l'effet différentiel significatif ne subsiste que pour les postes initialement entre 1 et 1,1 SMIC (+0,16 point).

**Niveau de confiance :**
- **modéré** pour la diffusion salariale de court terme dans les entreprises de 10 salariés ou plus couvertes par ACEMO ;
- **modéré à faible** pour la persistance à un an et la transposition à toutes les entreprises ;
- **nul** pour une conclusion sur l'emploi, puisque l'étude ne mesure pas les créations/destructions d'emplois.

**Conclusion opérationnelle :** cette étude documente un effet d'entraînement sur les grilles salariales, mais ne peut être utilisée comme preuve que les hausses du SMIC créent ou détruisent des emplois. Elle montre également que l'effet dépend de la structure des branches : là où les minima conventionnels sont déjà au-dessus du SMIC, la diffusion supplémentaire est plus limitée.

## 9. Référence primaire

Goarant, Claire & Muller, Lara (2011), « Les effets des hausses du Smic sur les salaires mensuels dans les entreprises de 10 salariés ou plus de 2006 à 2009 », *Emploi et salaires*, INSEE Références, p. 69–81, [PDF intégral](https://www.insee.fr/fr/statistiques/fichier/1373824/empsal11f.pdf).
