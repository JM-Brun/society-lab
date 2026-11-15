# Audit — Hennion & Loisy (2006) : estimation macroéconomique des allègements de cotisations

- **Référence :** Marie Hennion et Christian Loisy, « L’impact des exonérations de cotisations patronales de Sécurité sociale sur l’emploi : une nouvelle évaluation », *Dossiers Solidarité et Santé*, n°2, avril–juin 2006, p. 65–72 (article annoncé p. 43 dans le sommaire du numéro).
- **Source intégrale :** [PDF DREES, numéro complet](https://drees.solidarites-sante.gouv.fr/sites/default/files/2020-10/dss02-2006.pdf).
- **Question :** quel effet global sur l’emploi peut-on associer à la baisse du taux apparent de cotisations patronales entre 1990 et 2003 ?
- **Périmètre :** secteur marchand non agricole, tous salariés, emploi en équivalent temps plein. L'étude ne mesure pas uniquement les exonérations ciblées au niveau du SMIC.

## 1. Données et construction des variables

- Comptes trimestriels INSEE et données de la Direction de la Sécurité sociale, période d’estimation 1985T1–2003T3.
- Champ : secteurs marchands non agricoles (SMNA), hors secteur public.
- Emploi salarié mesuré en équivalent temps plein (ETP), afin de prendre en compte le développement du temps partiel.
- Coût réel du travail par tête : masse salariale brute augmentée des cotisations patronales effectivement versées, déflatée par le prix du PIB et rapportée à l’emploi en ETP.
- Taux apparent de cotisations patronales : cotisations versées divisées par la masse salariale. Il intègre donc les exonérations et les évolutions de l’ensemble des prélèvements patronaux couverts, pas seulement les ristournes bas salaires.

La construction des taux apparents comporte des conventions : 95 % des cotisations CNAMTS et 80 % des cotisations CNAF sont attribuées au champ privé non agricole ; pour les taux légaux, les auteurs supposent notamment que 80 % de l’assiette est sous plafond. Ces conventions doivent être gardées à l’esprit lorsqu’on interprète le niveau et l’évolution du taux apparent.

## 2. Méthode économétrique

Les auteurs estiment une équation agrégée d’emploi par modèle à correction d’erreur (ECM), en deux étapes :
- relation de long terme en logarithmes entre emploi, PIB, coût réel du travail par tête et tendance ;
- dynamique de court terme en variations logarithmiques, avec emploi retardé, PIB, coût du travail et terme de correction d’erreur.

Les séries sont traitées comme intégrées d’ordre 1 après tests ADF ; la stationnarité du résidu de long terme est utilisée pour étayer la cointégration. Les auteurs ajustent les écarts-types de long terme par les MCO dynamiques de Stock et Watson.

La spécification impose l’élasticité de l’emploi au PIB égale à 1 et ajoute une variable muette à partir de 1998T4 pour capter l’augmentation d’emploi associée à la réduction du temps de travail. Les auteurs reconnaissent qu’il est difficile de séparer l’effet de la RTT de celui des baisses de cotisations, car les deux évolutions sont colinéaires. La variable muette est une représentation frustre de la RTT, pas une identification indépendante de son effet.

## 3. Résultats

La relation de long terme estimée est :

`log(emploi_t) = constante - 0,002 × tendance + log(PIB_t) - 0,9 × log(coût réel du travail_t) + 0,03 × indicatrice(RTT à partir de 1998T4)`

- Élasticité de long terme de l’emploi au coût réel du travail : **−0,9** (statistique t = −3,3).
- Élasticité au PIB : imposée à 1.
- Tendance : −0,002 (t = −2,0).
- Variable RTT : +0,03 (t = 2,8).

Dans l’équation de court terme, le coefficient de la variation du coût du travail est −0,04 (t = −1,1), donc non significatif ; le terme de correction d’erreur est −0,05 (t = −2,9). Les auteurs interprètent l’ajustement vers le long terme comme progressif, de l’ordre de 5 % de l’écart par trimestre.

Entre 1990 et 2003, le taux apparent de cotisations patronales passe d’environ 33,7 % à 31,1 %, soit une baisse de 2,6 points. Avec un taux moyen de 33 %, une baisse d’un point de cotisation équivaut selon les auteurs à une baisse d’environ 0,75 % du coût du travail ; compte tenu de l’élasticité de long terme estimée, cela correspond à une hausse de l’emploi d’environ 0,68 %.

En appliquant cette relation à la baisse observée, les auteurs estiment **environ 250 000 emplois salariés en ETP créés ou sauvegardés** entre 1990 et 2003, toutes choses égales par ailleurs.

## 4. Limites d’identification et de portée

1. **Traitement agrégé :** le taux apparent couvre l’ensemble des cotisations patronales et ne permet pas d’isoler la part de masse salariale directement concernée par les exonérations bas salaires. Les auteurs indiquent explicitement que leur approche ne distingue pas l’effet propre des mesures ciblées.
2. **Conjoncture :** l’emploi dépend fortement du PIB. La période 1997–2001 associe baisse des taux apparents et forte croissance ; la corrélation brute entre les deux séries n’est pas une preuve causale.
3. **RTT et exonérations :** la RTT de 1998 est contrôlée par une indicatrice, mais les auteurs ne peuvent distinguer proprement ses effets de ceux des allègements, en raison de leur colinéarité. L’indicatrice est une approximation.
4. **Salaires supposés exogènes :** l’équation suppose implicitement l’exogénéité des salaires, alors que les allègements peuvent modifier les négociations et le salaire net. L’équation salariale agrégée testée ne trouve pas d’effet significatif du taux de cotisation sur le salaire réel par tête, mais les auteurs reconnaissent que les données agrégées sont insuffisantes.
5. **Substitution entre qualifications :** l’étude ne peut identifier la substitution entre emploi qualifié et peu qualifié ; elle estime un effet global et suppose qu’il incorpore cette substitution.
6. **Financement :** le coût macroéconomique du financement des exonérations n’est pas pris en compte. Les auteurs le signalent explicitement.
7. **Horizon et extrapolation :** l’élasticité de long terme est appliquée à une baisse de taux observée sur 1990–2003 ; le chiffre de 250 000 est une simulation « toutes choses égales par ailleurs », pas un décompte direct d’emplois attribuables.

## 5. Comparaison avec les évaluations sectorielles et microéconomiques

L’estimation de 250 000 ETP est intermédiaire dans la littérature présentée par les auteurs :
- Jamet (2005) : environ 78 000 à 190 000 emplois peu qualifiés selon les hypothèses sectorielles ;
- Gafsi, L’Horty & Mihoubi : 118 000 à 140 000 emplois peu qualifiés, mais seulement 60 000 à 80 000 emplois nets après éviction d’emplois qualifiés ;
- Crépon & Desplatz : environ 460 000 emplois selon l’estimateur semi-paramétrique, dont environ 220 000 peu qualifiés et 240 000 qualifiés ;
- Laroque & Salanié : environ 490 000 dans leur évaluation de long terme.

Cette comparaison est indicative : les unités, périodes, champs et modèles diffèrent. Hennion & Loisy mesurent un effet agrégé sur tous les ETP du secteur marchand, alors que Jamet et Gafsi et al. se concentrent sur l’emploi peu qualifié et modélisent plus explicitement les substitutions sectorielles et entre qualifications.

## 6. Niveau de preuve et conclusion

- **Association macroéconomique de long terme entre coût du travail et emploi :** relation estimée négative et statistiquement significative dans la spécification retenue.
- **Effet causal des exonérations bas salaires seules :** faible confiance, car le taux de cotisations est agrégé, la conjoncture et la RTT sont concomitantes, et la composition du traitement n’est pas isolée.
- **Bilan net de l’emploi :** l’étude estime 250 000 ETP sur le champ marchand, mais ne prend pas en compte le financement des exonérations et ne distingue pas les qualifications.
- **Effet d’une hausse isolée du SMIC :** non étudié.

**Conclusion :** Hennion & Loisy apportent un point de comparaison macroéconomique utile, mais leur chiffre de 250 000 ETP ne peut pas être attribué exclusivement aux allègements ciblés sur les bas salaires. Il ne contredit pas directement Gafsi et al. : le premier mesure une relation agrégée entre le taux apparent global et l’emploi total, le second modélise les substitutions entre qualifications et aboutit à un solde net de 60 000 à 80 000 emplois pour la politique de bas salaires.

## 7. Sources

- Hennion & Loisy (2006), *Dossiers Solidarité et Santé* n°2, p. 65–72 : https://drees.solidarites-sante.gouv.fr/sites/default/files/2020-10/dss02-2006.pdf
- Jamet (2005), DARES, Document d’études n°103 : https://dares.travail-emploi.gouv.fr/sites/default/files/pdf/de_103.pdf
- Gafsi, L’Horty & Mihoubi (2004), EPEE 04-03R : https://www.univ-evry.fr/fileadmin/mediatheque/ueve-institutionnel/03_Recherche/laboratoires/Epee/wp/04-03R.pdf
- Crépon & Desplatz (2001/2002), INSEE : https://www.insee.fr/fr/statistiques/1376044?sommaire=1376054
