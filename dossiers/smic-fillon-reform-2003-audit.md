# Audit d'études — réforme Fillon de 2003 : allègements, emploi et salaires

- **Périmètre :** réforme du 17 janvier 2003, convergence SMIC-GMR et unification des exonérations patronales (2003–2005).
- **Statut :** audit approfondi de Bunel, Gilles & L’Horty (2009) ; audit bibliographique et méthodologique initial de Simonnet & Terracol (2009). Les deux études ne mesurent pas l'effet d'une hausse isolée du SMIC.
- **Question :** les baisses de cotisations ont-elles compensé la hausse du coût du travail issue de la convergence des minima, et avec quels effets sur l'emploi, les heures et les rémunérations ?

## 1. Contexte institutionnel : un traitement composite

La loi du 17 janvier 2003 organise simultanément :
- la convergence progressive, entre juillet 2003 et juillet 2005, du SMIC horaire et des cinq générations de garanties mensuelles de rémunération (GMR) liées au passage aux 35 heures ;
- l'unification des barèmes d'allègements patronaux entre entreprises passées à 35 heures et entreprises restées à 39 heures ;
- une redistribution des exonérations : les entreprises à 39 heures bénéficient généralement d'une hausse plus importante des allègements, tandis que les entreprises à 35 heures perdent une partie de leurs avantages antérieurs, notamment au-dessus de 1,7 SMIC.

Le SMIC horaire augmente de 20,4 % en euros courants entre 2001 et 2005, contre 8,0 à 12,6 % pour les différentes GMR. Il est donc impossible d'interpréter l'épisode comme une expérience « hausse du SMIC seule » : salaires minimaux, temps de travail et cotisations changent conjointement.

## 2. Bunel, Gilles & L’Horty (2009) — étude principale

**Référence :** Matthieu Bunel, Fabrice Gilles et Yannick L’Horty, « Les effets des allégements de cotisations sociales sur l’emploi et les salaires : une évaluation de la réforme de 2003 », *Économie et Statistique*, n° 429-430, 2009, p. 77–105. Version de travail : *Les effets des allègements de cotisations sociales sur l’emploi et les salaires : une évaluation de la réforme Fillon de 2003*, EPEE, document 09-12, juillet 2009. [PDF de travail](https://www.univ-evry.fr/fileadmin/mediatheque/ueve-institutionnel/03_Recherche/laboratoires/Epee/wp/09-12.pdf) ; [article INSEE](https://www.insee.fr/fr/statistiques/1377396?sommaire=1377406) ; [article Persée](https://www.persee.fr/doc/estat_0336-1454_2009_num_429_1_8064).

### 2.1 Données, période et champ

- Panel cylindré 2002–2005, environ 92 939 entreprises (le résumé de l'article arrondit à près de 90 000).
- Entreprises du secteur privé non agricole de plus de cinq salariés, présentes dans les sources pendant toute la période et bénéficiaires de manière continue des dispositifs concernés en 2003–2004.
- Appariement de fichiers ACOSS (AROME, ORME, SEQUOIA), DADS et SUSE-INSEE.
- Environ 145 000 établissements et 3,4 millions de salariés dans l'échantillon.
- Les très petites entreprises, les entreprises publiques, holdings, intérim, services domestiques, hôtels-cafés-restaurants et entreprises cumulant les deux catégories d'aides sont exclus.
- Deux groupes : entreprises passées à 35 heures avant 2003 (« Fillon-Aubry 2 ») et entreprises restées à 39 heures (« Fillon-autres employeurs »). Dans l'échantillon, 65,1 % relèvent du groupe 39 heures et 33,9 % du groupe 35 heures.

Les sources administratives permettent d'observer les exonérations effectivement perçues, et non seulement un montant théorique. Les variables de résultat incluent les effectifs bruts, l'emploi en équivalent temps plein, le salaire horaire brut et des indicateurs de structure de main-d'œuvre.

### 2.2 Construction du traitement et identification

Le traitement est la variation du coût du travail imputable aux changements de barèmes d'exonération et aux hausses des minima. Les auteurs la calculent à partir de la structure salariale de 2002, maintenue constante pour isoler le choc mécanique de la réforme des ajustements de composition ultérieurs.

Cette exposition est continue et différenciée selon les entreprises ; il n'existe pas de groupe national totalement non traité. La méthode s'inspire de Crépon & Desplatz (2001), mais intègre les exonérations effectivement perçues et les hausses différenciées du SMIC ou des GMR.

Les auteurs combinent :
- moindres carrés ordinaires (MCO), sous hypothèse d'exogénéité conditionnelle du traitement ;
- régressions quantiles, pour étudier l'hétérogénéité dans la distribution ;
- appariement sur score de propension, avec méthodes du plus proche voisin et du noyau, sur support commun ;
- bootstrap de 50 réplications pour les erreurs-types asymptotiques de l'estimateur à noyau.

**Hypothèse d'identification :** conditionnellement aux caractéristiques observées et au score estimé, les différences d'exposition peuvent être interprétées comme quasi exogènes. Le calcul à structure salariale fixe réduit l'endogénéité mécanique due aux réallocations postérieures, mais ne rend pas l'exposition initiale aléatoire.

**Tendances préalables :** ce n'est pas une différence-de-différences standard avec groupe témoin non traité. Le document ne présente pas de test événementiel moderne de tendances parallèles ; l'absence de divergence préexistante entre entreprises plus ou moins exposées n'est donc pas démontrée par un tel test. Le panel comporte des observations antérieures à la réforme, mais cela ne suffit pas à établir à lui seul l'hypothèse d'identification.

### 2.3 Résultats emploi, heures et salaires

Les résultats doivent être lus séparément selon le régime d'horaires.

**Entreprises restées à 39 heures :**
- La variation moyenne du coût du travail liée à la réforme est d'environ −1,017 % (pondérée par les effectifs).
- L'élasticité MCO de l'emploi brut au coût du travail est −0,2234, IC à 95 % [−0,3414 ; −0,1054].
- L'élasticité de l'emploi en équivalent temps plein est rapportée autour de −0,31 (tableau 5 : −0,3133, IC à 95 % [−0,4252 ; −0,2015]).
- Les auteurs calculent un effet d'environ +0,24 % d'emploi brut, soit 3 000 emplois dans l'échantillon ; extrapolation indicative à l'ensemble du secteur marchand : environ +15 500 emplois. Pour l'équivalent temps plein, environ +4 300 dans l'échantillon et +21 500 par extrapolation.
- L'élasticité du salaire horaire brut au coût du travail est négative (environ −0,4484, IC à 95 % [−0,5082 ; −0,3885]) : la baisse du coût est associée à une hausse des rémunérations.

**Entreprises passées à 35 heures :**
- La variation moyenne du coût du travail est d'environ +1,71 % (pondérée par les effectifs).
- L'élasticité MCO de l'emploi brut est faible et non significative : −0,0585, IC à 95 % [−0,2439 ; 0,12695].
- L'élasticité de l'emploi en équivalent temps plein est −0,2776, IC à 95 % [−0,4601 ; −0,0950].
- Les auteurs estiment environ −0,48 % d'emploi en équivalent temps plein, soit −7 700 emplois dans l'échantillon et, par extrapolation, environ −39 000 emplois.
- Ils relient notamment cette baisse du volume horaire au recours accru aux emplois temporaires courts et au temps partiel. Les effets sur les effectifs bruts sont moins nets que sur les équivalents temps plein.

**Bilan agrégé :** l'effet est jugé très faible, voire légèrement négatif, et sans effet clair statistiquement ou économiquement robuste sur l'emploi total. Les entreprises à 39 heures gagnent relativement, celles à 35 heures perdent relativement. Les rémunérations horaires brutes augmentent dans les deux groupes.

Les intervalles ci-dessus sont ceux des élasticités estimées dans les tableaux, et non des intervalles de confiance complets pour les extrapolations nationales de +15 500 ou −39 000 emplois. Ces dernières sont des ordres de grandeur obtenus par extrapolation, à ne pas traiter comme des comptes d'emplois causaux précisément identifiés.

### 2.4 Robustesses et limites

**Éléments favorables :**
- données administratives appariées, avec mesure des exonérations effectivement perçues ;
- traitement construit à partir de la distribution salariale antérieure à la réforme ;
- résultats qualitativement proches entre MCO et appariement sur score de propension ;
- examen des quantiles et distinction entre effectifs et équivalents temps plein ;
- intervalles de confiance publiés pour les principales élasticités.

**Limites :**
1. L'exposition n'est pas randomisée ; les entreprises à 35 h et 39 h diffèrent par taille, secteur, main-d'œuvre, organisation et trajectoire antérieure.
2. Le maintien d'une structure salariale de 2002 isole un choc calculé, mais ne neutralise pas tous les facteurs non observés corrélés à l'exposition.
3. Le panel cylindré exclut les créations et disparitions d'entreprises ; les résultats ne capturent pas directement la marge extensive de création/destruction d'entreprises.
4. Les entreprises peuvent se concurrencer et se déplacer des parts de marché ; les auteurs précisent que leur exercice ne comporte pas de bouclage macroéconomique ni d'effets de substitution intersectoriels.
5. Les résultats agrégés reposent sur extrapolation à partir de deux groupes d'entreprises ; ils ne constituent pas une évaluation complète de l'équilibre général.
6. L'étude ne donne pas un bilan complet par niveau de qualification et de salaire ; les effets sur la composition de l'emploi restent partiellement ouverts.
7. La période associe convergence SMIC-GMR, RTT, diffusion salariale et réforme des exonérations : attribution au seul SMIC impossible.

### 2.5 Niveau de preuve et interprétation

- **Association entre variation du coût et emploi dans les groupes d'entreprises :** preuve microéconomique relativement riche, confiance modérée.
- **Effet causal net de la réforme Fillon sur l'emploi agrégé :** confiance faible à modérée, compte tenu de l'identification conditionnelle, de la sélection, des sorties d'entreprises et des effets de déplacement absents.
- **Effet d'une hausse isolée du SMIC légal :** non identifié par cette étude.
- **Point substantiel :** le résultat montre surtout qu'une même réforme nationale peut redistribuer les coûts et l'emploi entre entreprises selon leur durée collective de travail. Une moyenne nationale masque cette hétérogénéité.

## 3. Simonnet & Terracol (2009) — transitions chômage vers emploi

**Référence :** Véronique Simonnet et Antoine Terracol, « Coût du travail et flux d’emploi : l’impact de la réforme de 2003 », *Économie et Statistique*, n° 429-430, 2009, p. 107–128, DOI [10.3406/estat.2009.8065](https://doi.org/10.3406/estat.2009.8065). [Notice INSEE](https://www.insee.fr/fr/statistiques/1377398?sommaire=1377406) ; [notice Persée](https://www.persee.fr/doc/estat_0336-1454_2009_num_429_1_8065) ; [version HAL](https://insee.hal.science/hal-05643211).

### 3.1 Données et question

- Appariement de l'Enquête Emploi 2001–2007 et de fichiers CERFA.
- Résultat étudié : transitions du chômage vers l'emploi, selon que la personne entre dans une entreprise signataire ou non d'un accord de réduction du temps de travail à 35 heures avant 2003.
- Le traitement est le changement différencié du coût d'embauche au cours de la transition SMIC-GMR et de l'unification des allègements.

### 3.2 Résultats vérifiés dans le résumé éditeur

Les auteurs mettent en évidence un ralentissement des sorties du chômage vers les entreprises passées à 35 heures. Les baisses de cotisations patronales semblent insuffisantes pour compenser la hausse du coût du travail dans ces entreprises ; elles compensent davantage la hausse chez les entreprises non signataires restées à 39 heures. Les sorties du chômage des personnes les plus diplômées ne sont pas modifiées, tandis que celles des moins diplômées ralentissent.

### 3.3 Statut de vérification

Le texte intégral a depuis été obtenu et dépouillé : les données, le modèle de durée, les hypothèses d'identification, les coefficients et erreurs-types des tableaux 5 à 7, les tests de différences entre types d'entreprises et les principales limites sont documentés dans la section 3 de l'audit quantitatif approfondi ci-dessous. Les résultats sont donc désormais plus précis que le résumé initial ; ils restent conditionnels aux hypothèses du modèle et ne constituent pas un bilan net d'emplois.

## 4. Pourquoi les résultats diffèrent de Crépon & Desplatz (2001)

Les deux évaluations ne sont pas directement comparables.

| Dimension | Crépon & Desplatz (2001) | Bunel, Gilles & L’Horty (2009) |
|---|---|---|
| Réforme | Extensions d'allègements de 1995–1996 | Réforme Fillon et convergence SMIC-GMR 2003–2005 |
| Données | BRN-DADS, entreprises 1994–1997 | ACOSS-DADS-SUSE, entreprises 2002–2005 |
| Traitement | Réduction ex ante du coût moyen issue des extensions | Variation du coût calculée à structure salariale 2002 constante, avec exonérations effectivement perçues |
| Contexte | Allègements généraux ciblés sur bas salaires | Redistribution entre entreprises à 35 h et 39 h, hausse de minima et harmonisation des barèmes |
| Résultat | 290 000 à 460 000 emplois selon estimateur, avec incertitudes et limites macro | Effet agrégé faible ou légèrement négatif, redistribution entre groupes |
| Bouclage macro | Non complet ; effets de déplacement contestés | Explicitement absent ; auteurs signalent l'absence d'effets volume et substitutions intersectorielles |

Bunel et al. rappellent eux-mêmes que les estimations sectorielles intégrant effets volume et substitutions intersectorielles (Jamet, 2005 ; Gafsi, L’Horty & Mihoubi, 2005) donnent des effets plus faibles que l'estimation microéconomique de Crépon & Desplatz. La différence ne prouve donc pas que les allègements de 1995 auraient créé des centaines de milliers d'emplois nets et que ceux de 2003 n'auraient rien créé : elle reflète des réformes, des traitements, des populations, des méthodes et des niveaux d'agrégation distincts.

## 5. Synthèse opérationnelle

1. La réforme de 2003 ne permet pas d'isoler l'effet du SMIC : elle combine convergence des GMR, hausse des minima et redistribution des exonérations.
2. Les entreprises à 39 heures bénéficient relativement de la réforme ; les entreprises à 35 heures subissent davantage la hausse du coût moyen, malgré l'unification des allègements.
3. L'emploi en équivalent temps plein réagit plus nettement que les effectifs bruts dans le groupe 35 heures : raison supplémentaire de suivre les heures, pas seulement les têtes.
4. Les salaires horaires bruts progressent dans les deux groupes, ce qui rappelle que les allègements peuvent être en partie transmis aux rémunérations.
5. Le bilan agrégé de Bunel et al. est faible voire légèrement négatif, mais l'étude ne traite pas les effets de déplacement entre entreprises et secteurs.
6. Simonnet & Terracol apportent un résultat complémentaire sur les sorties du chômage : ralentissement pour les entreprises 35 heures et pour les personnes moins diplômées.
7. Ces résultats sont pertinents pour comprendre l'interaction SMIC–cotisations–RTT, mais ne doivent jamais être convertis en élasticité causale d'une hausse isolée du SMIC.

**Conclusion :** les évaluations de 2003 montrent que les effets des allègements dépendent fortement du régime d'horaires et du profil initial des entreprises. Elles confortent la nécessité d'évaluer conjointement salaire minimum, durée du travail et cotisations, sans confondre leur contribution respective. Le niveau de preuve est modéré pour les associations différentielles observées dans les entreprises, mais faible à modéré pour l'effet net macroéconomique.

## 6. Sources primaires et connexes

- Bunel, Gilles & L’Horty (2009), document de recherche EPEE 09-12 : https://www.univ-evry.fr/fileadmin/mediatheque/ueve-institutionnel/03_Recherche/laboratoires/Epee/wp/09-12.pdf
- Bunel, Gilles & L’Horty, article INSEE : https://www.insee.fr/fr/statistiques/1377396?sommaire=1377406
- Simonnet & Terracol (2009), article INSEE : https://www.insee.fr/fr/statistiques/1377398?sommaire=1377406
- Simonnet & Terracol, version HAL : https://insee.hal.science/hal-05643211
- Crépon & Desplatz (2001/2002), article INSEE : https://www.insee.fr/fr/statistiques/1376044?sommaire=1376054
- Jamet (2005), « Allègements généraux de cotisations sociales et emploi peu qualifié : de l’impact sectoriel à l’effet macro-économique », *Revue française d’économie*, 19(3), p. 57–90.
- Gafsi, L’Horty & Mihoubi (2005), « Vingt ans d’évolution de l’emploi peu qualifié et du coût du travail : des ruptures qui coïncident ? », *Revue française d’économie*, 19(3), p. 91–116.


## 3. Audit quantitatif approfondi — Simonnet & Terracol (2009)

**Référence :** Véronique Simonnet et Antoine Terracol, « Coût du travail et flux d’emploi : l’impact de la réforme de 2003 », *Économie et Statistique*, n°429-430, 2009, p. 107–128, DOI 10.3406/estat.2009.8065. [Article intégral, BnSP/INSEE](https://www.bnsp.insee.fr/ark:/12148/bc6p070n3rp.pdf) ; [notice Persée](https://www.persee.fr/doc/estat_0336-1454_2009_num_429_1_8065).

### 3.1 Données et population

- Enquête Emploi en continu, du premier trimestre 2002 au premier trimestre 2007, appariée aux fichiers CERFA identifiant les entreprises signataires d’accords RTT avant le 1er juillet 2003 ; DADS et données URSSAF servent notamment à construire la démographie des entreprises signataires/non signataires.
- Un épisode de chômage est suivi jusqu’à une sortie vers l’emploi, une autre sortie (censure), ou 36 mois.
- Base finale : **17 706 épisodes de chômage**, dont 6 932 se terminent par un retour à l’emploi ; 3 224 sorties vers des entreprises signataires d’un accord 35 h et 3 708 vers des entreprises non signataires.
- L’échantillon initial comptait 21 816 épisodes ; 1 068 épisodes incohérents et 3 042 épisodes sans SIRET ont été retirés (18,83 % de l’échantillon initial).
- Les auteurs indiquent que les caractéristiques observées des épisodes sans SIRET sont proches de celles de l’échantillon retenu, mais cela ne garantit pas l’absence de sélection sur les caractéristiques non observées.
- « Bas diplômes » signifie jusqu’au baccalauréat inclus : 13 094 épisodes ; « hauts diplômes » : 4 612.

### 3.2 Stratégie économétrique

Les auteurs utilisent un modèle de durée à risques concurrents dépendants (Mixed Proportional Hazard). Les deux risques de sortie du chômage sont : emploi dans une entreprise signataire 35 h avant juillet 2003 ; emploi dans une entreprise non signataire.

Le hasard de base est constant par morceaux selon plusieurs intervalles de durée. Les caractéristiques observées comprennent notamment âge, sexe, diplôme, situation familiale, chômage local, assurance chômage, exigences de recherche d’emploi et proportion locale de l’emploi dans les entreprises signataires.

Un indicateur département-trimestre de part de l’emploi dans les entreprises signataires est construit à partir des DADS et des fichiers URSSAF pour contrôler la baisse mécanique de leur poids dans l’économie due aux créations et destructions d’entreprises. Les auteurs reconnaissent que cette variable démographique pourrait elle-même être endogène si la réforme affecte la survie des entreprises.

**Hypothèse d’identification :** le différentiel de variation des taux de sortie vers les entreprises signataires et non signataires après les étapes de la réforme peut être interprété comme effet causal sous les hypothèses du modèle, notamment la spécification des risques concurrents et le contrôle de la démographie des entreprises.

**Hétérogénéité inobservée :** la corrélation estimée entre les deux composantes d’hétérogénéité non observée atteint la borne de 1. Les auteurs réestiment donc le modèle en imposant une corrélation parfaite afin d’éviter un problème de régularité ; ils indiquent que les résultats sont très similaires. Cette solution constitue une hypothèse forte, à conserver dans l’interprétation.

### 3.3 Résultats des tableaux 5 à 7

Les coefficients sont des effets sur le logarithme du taux instantané de sortie du chômage ; les étoiles signalent les seuils de significativité. Ils ne sont pas des pourcentages de probabilité directement observés.

| Échantillon / période | Toutes sorties | Vers entreprises signataires | Vers non-signataires |
|---|---:|---:|---:|
| Ensemble, 2003–2004 | −0,011 (ns) | −0,070 (ns) | 0,018 (ns) |
| Ensemble, 2004–2005 | −0,113*** | −0,250*** | −0,060 (ns) |
| Ensemble, après juillet 2005 | −0,088** | −0,230*** | −0,030 (ns) |
| Bas diplômes, après juillet 2005 | −0,143*** | −0,293*** | −0,093 (ns) |
| Hauts diplômes, après juillet 2005 | −0,082 (ns) | −0,078 (ns) | 0,137 (ns) |

Les auteurs testent aussi directement la différence entre les coefficients postérieurs à juillet 2005 :
- bas diplômes : différence −0,20 ; p = 0,014 ;
- hauts diplômes : différence −0,215 ; p = 0,130 ;
- ensemble : différence −0,20 ; p = 0,003.

L’effet différentiel est donc statistiquement significatif pour l’ensemble et pour les moins diplômés, mais pas pour les plus diplômés. Les sorties vers les entreprises non signataires ne présentent pas de variation significative ; le ralentissement vient essentiellement des sorties vers les entreprises signataires.

### 3.4 Robustesses, interprétation et limites

- Le contrôle de la démographie des entreprises est une contribution importante : sans lui, le recul mécanique du poids des entreprises signataires (qui ne peuvent plus être créées après la date de signature) aurait pu être attribué à tort à la réforme.
- Les auteurs modélisent l’hétérogénéité inobservée, mais la corrélation estimée atteint la borne et doit être contrainte à la corrélation parfaite.
- Le contrôle démographique repose sur l’hypothèse que l’effet de la réforme sur la création et la destruction d’entreprises est négligeable par rapport à leur évolution naturelle ; cette hypothèse n’est pas directement testée.
- L’appariement exclut 18,83 % des épisodes initiaux, notamment faute de SIRET.
- Les entreprises signataires et non signataires ne sont pas assignées aléatoirement ; leurs secteurs, tailles, trajectoires et pratiques de rémunération peuvent différer.
- Le modèle compare les transitions vers deux catégories d’entreprises pendant une réforme qui affecte les deux groupes différemment ; il ne dispose pas d’un groupe national totalement non traité.
- Le texte n’établit pas de test de pré-tendances au format event-study. Les indicatrices temporelles et la période pré-réforme sont utiles, mais ne démontrent pas à elles seules des tendances parallèles.
- Le résultat concerne la sortie du chômage vers un type d’entreprise, non l’emploi total net, les heures travaillées, la durée des contrats ou les salaires après embauche.
- Les coefficients sont des log-hasards : ils ne doivent pas être convertis en nombre d’emplois détruits sans modèle de projection supplémentaire.

**Conclusion :** sous les hypothèses du modèle, la réforme a réduit relativement les sorties du chômage vers les entreprises signataires 35 h, en particulier pour les moins diplômés. L’étude complète les données d’entreprises de Bunel et al. en observant les flux des demandeurs d’emploi, mais ne mesure pas l’effet d’une hausse isolée du SMIC et ne permet pas de chiffrer un solde d’emplois net national.

## 4. Articulation avec les travaux sectoriels

Les résultats de Simonnet & Terracol (2009) portent sur la réforme 2003–2005 et les transitions individuelles ; ils ne doivent pas être agrégés aux évaluations de Jamet (2005) ou Gafsi, L’Horty & Mihoubi (2004), qui portent sur les allègements de 1993–1997. Pour l’épisode 2003, le résultat de flux est cohérent avec l’asymétrie des coûts d’embauche entre entreprises 35 h et 39 h, mais il ne constitue pas une mesure du bilan macroéconomique net.
