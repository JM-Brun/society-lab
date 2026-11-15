# Fiche d'audit — Aeberhardt, Givord & Marbot (2012), diffusion du SMIC dans la distribution salariale

- **Référence :** Romain Aeberhardt, Pauline Givord et Claire Marbot, *Spillover Effect of the Minimum Wage in France: An Unconditional Quantile Regression Approach*, INSEE, Document de travail G2012/07, juin 2012.
- **Texte primaire intégral :** [PDF INSEE](https://www.insee.fr/fr/statistiques/fichier/1380948/G2012-07.pdf) ; [notice INSEE](https://www.insee.fr/fr/statistiques/1380948).
- **Statut de l'audit :** lecture du document primaire complet (36 pages), vérification des sections institutionnelles, de la stratégie d'identification, des données DADS, des tableaux 1 à 6, de la figure 3 et des tests de robustesse.
- **Question étudiée :** les hausses différenciées des minima salariaux pendant la convergence des GMR en 2003–2005 se diffusent-elles au-delà des salariés directement payés au minimum ?
- **Avertissement central :** l'étude mesure la distribution des rémunérations annuelles brutes des salariés à temps plein et à l'année. Elle ne mesure pas directement l'emploi net, les heures, le revenu disponible ni la pauvreté.

## 1. Contexte institutionnel et traitement

La loi sur les 35 heures a conduit à la coexistence de plusieurs niveaux de rémunération minimale. Les entreprises ayant signé un accord de réduction du temps de travail à des dates différentes ont reçu des garanties mensuelles de rémunération (GMR) distinctes, destinées à préserver le salaire mensuel malgré le passage à 35 heures.

En 2003, six minima coexistent : le SMIC horaire classique et cinq GMR. Un mécanisme de convergence vers un niveau unique est imposé entre 2003 et 2005. Les GMR initialement les plus faibles connaissent les hausses réelles les plus fortes ; les niveaux les plus élevés progressent moins vite, voire reculent légèrement en termes réels. En 2005, les six niveaux convergent.

Le tableau 1 du document donne, en euros 2007, les niveaux réels annuels :
- en 2002 : de 13 612 € pour FGMR0 à 15 167 € pour FGMR5 ;
- en 2005 : 15 068 € pour les six groupes.

Le groupe FGMR0, composé des entreprises n'ayant pas signé d'accord de réduction du temps de travail avant la date limite de 2002, connaît donc le rattrapage le plus fort. Les auteurs utilisent cette variation différenciée comme expérience naturelle.

**Ce n'est pas une hausse uniforme et isolée du SMIC national.** Le traitement est la convergence de minima d'entreprise issus de la réforme des 35 heures, dans un contexte où les allègements de cotisations patronales sont également importants. Le calendrier de signature des accords et les caractéristiques des entreprises font partie du contexte d'identification.

## 2. Données et population effectivement étudiée

- **Source :** panel DADS, échantillon au 1/25e, période 2003–2005.
- **Couverture annoncée :** plus de 157 000 entreprises, dont environ 77 000 présentes pendant toute la période, et environ 425 000 salariés.
- **Tableau descriptif 2003 :** 114 451 entreprises et 299 488 salariés dans les groupes GMR.
- **Champ :** salariés du secteur privé, âgés de 18 à 65 ans, à temps plein et ayant travaillé toute l'année dans la même entreprise ; travailleurs indépendants exclus ; apprentis et stagiaires exclus.
- **Variable de résultat :** rémunération annuelle brute, exprimée en euros 2007, et non salaire horaire.

La restriction au temps plein et à l'année entière est motivée par la qualité jugée insuffisante des heures DADS pour reconstruire un salaire horaire fiable. Elle permet de comparer des rémunérations annuelles, mais exclut une partie importante des salariés les plus précaires, notamment les temps partiels et les personnes ayant des parcours discontinus.

Répartition des salariés par groupe GMR en 2003 :
| Groupe | Part des salariés |
|---|---:|
| FGMR0 | 37,2 % |
| FGMR1 | 5,8 % |
| FGMR2 | 32,2 % |
| FGMR3 | 15,2 % |
| FGMR4 | 8,5 % |
| FGMR5 | 1,0 % |

Les groupes ne sont pas comparables spontanément. Les entreprises ayant signé tôt un accord de réduction du temps de travail sont plus souvent grandes et industrielles ; les entreprises n'ayant pas signé avant 2002 sont plus souvent petites. Les auteurs contrôlent notamment la taille et le secteur, mais cette sélection demeure centrale pour l'identification.

## 3. Stratégie d'identification

Les auteurs utilisent une régression de quantiles inconditionnels (UQR), selon la méthode de Firpo, Fortin et Lemieux (2009), estimée par RIF-Logit. L'objectif est de mesurer comment une variation marginale du niveau du minimum affecte les quantiles de la distribution salariale globale, en maintenant constants les autres déterminants observés.

La variation identifiante provient de la vitesse différente de convergence des six minima entre 2003 et 2005. Les auteurs considèrent que le calendrier de convergence a été imposé plusieurs années après les accords de réduction du temps de travail et n'était donc pas anticipé par la plupart des entreprises au moment de la signature.

Les spécifications comprennent :
- effets fixes temporels ;
- indicatrices de groupe GMR pour tenir compte des politiques salariales propres aux groupes ;
- âge et position socio-professionnelle ;
- ancienneté ;
- taille de l'entreprise et secteur d'activité.

Le SMIC utilisé est retardé d'un an : les négociations salariales ont généralement lieu en fin d'année et les accords s'appliquent au début de l'année suivante. Le taux de juillet de l'année précédente n'a été le minimum légal de référence que pendant la première moitié de l'année observée. Les auteurs reconnaissent que cette convention peut sous-estimer l'effet au tout bas de la distribution.

**Hypothèse d'identification :** conditionnellement aux caractéristiques observées, aux effets de groupe et aux effets temporels, le rythme de convergence des minima ne doit pas être corrélé aux composantes non observées de la distribution salariale. L'argument d'exogénéité repose sur le caractère tardif et imposé du mécanisme de convergence, pas sur une assignation aléatoire des entreprises aux groupes GMR.

## 4. Résultats sur la diffusion salariale

Le résultat principal est une diffusion statistiquement significative du minimum vers la distribution salariale, pour les hommes et les femmes, jusqu'au septième décile.

Pour les hommes, les coefficients du tableau 5 (RIF-Logit) sont :
| Décile | Coefficient du minimum (log) | Erreur-type |
|---:|---:|---:|
| 1 | 0,190 | 0,036 |
| 2 | 0,188 | 0,037 |
| 3 | 0,230 | 0,040 |
| 4 | 0,231 | 0,040 |
| 5 | 0,223 | 0,042 |
| 6 | 0,164 | 0,044 |
| 7 | 0,157 | 0,052 |
| 8 | 0,005 | 0,064 |
| 9 | −0,026 | 0,103 |

Les coefficients sont significatifs jusqu'au septième décile, puis deviennent non significatifs aux huitième et neuvième déciles. La figure 3 montre un profil comparable pour les femmes : l'effet est également significatif jusqu'au septième décile. Le texte indique que l'effet d'une hausse de 1 % du niveau du minimum sur les déciles de rémunération annuelle reste toujours inférieur à 0,2 %.

Les auteurs situent approximativement le premier décile autour de 1,2 fois le minimum et le septième décile autour de deux fois le minimum. Le résultat suggère donc une diffusion salariale au-delà des seuls salariés directement rattrapés par le minimum, mais d'ampleur décroissante avec le niveau de rémunération.

**Interprétation prudente :** il s'agit d'un effet partiel inconditionnel estimé sur les quantiles de la distribution des rémunérations annuelles des salariés retenus dans l'échantillon. Ce n'est pas une hausse de 0,2 % de tous les salaires, ni une élasticité de l'emploi, ni un effet sur le revenu disponible.

## 5. Résultats sur l'emploi : ce que l'étude observe réellement

Les auteurs examinent les taux de création et de destruction d'emplois par groupe GMR (tableau 4). Ils ne trouvent pas de relation monotone claire entre la vitesse de hausse du minimum et :
- la proportion de salariés qui disparaissent de l'entreprise d'une année à l'autre ;
- la proportion de salariés nouvellement présents ;
- les taux de destruction et de création.

En 2003, le taux de disparition des salariés est relativement homogène, autour de 24 % dans l'ensemble des groupes (de 22,0 % à 29,0 %). Les taux d'entrée sont plus dispersés et ne suivent pas une relation monotone avec le niveau GMR.

**Limite décisive :** il s'agit de statistiques descriptives par groupe, pas d'une estimation causale de l'effet sur l'emploi. L'étude ne permet donc pas de conclure que la convergence n'a pas eu d'effet sur l'emploi. Elle montre seulement que les indicateurs descriptifs présentés ne dessinent pas de gradient simple selon l'intensité de la hausse du minimum.

## 6. Robustesse

Les auteurs présentent trois vérifications :
1. remplacer la spécification logit par une spécification linéaire ;
2. exclure les rémunérations annuelles apparaissant sous le minimum horaire légal, potentiellement en raison d'erreurs de mesure ;
3. restreindre l'échantillon aux salariés présents dans la même entreprise l'année précédente ou encore présents l'année suivante.

Les résultats restent qualitativement similaires : l'effet est toujours significatif jusqu'au septième décile. Dans l'échantillon excluant les rémunérations sous le minimum, le profil est plus décroissant : proche de 0,4 au premier décile et inférieur à 0,1 au septième.

Les auteurs signalent toutefois que 2 % des hommes et 5 % des femmes de l'échantillon apparaissent sous le minimum, ce qui peut résulter d'heures mal mesurées, de composantes de rémunération non observées ou d'erreurs de déclaration. La robustesse réduit cette inquiétude sans l'éliminer.

## 7. Tendances préalables et limites d'identification

Le document ne présente pas de graphique d'étude d'événement permettant de vérifier des pré-tendances parallèles entre groupes GMR avant la convergence. Les effets temporels et les contrôles de caractéristiques ne remplacent pas un test explicite de tendances préalables.

Les auteurs reconnaissent que le calendrier des accords de réduction du temps de travail n'est pas exogène : les grandes entreprises ont signé plus tôt et les petites plus tard. Leur stratégie repose sur l'idée que la convergence imposée en 2003–2005 n'était pas anticipée au moment de ces accords. Cette hypothèse est plausible mais non directement testée par une assignation aléatoire.

Autres limites :
1. **Traitement composite :** convergence des GMR, réforme des 35 heures et allègements de cotisations patronales sont institutionnellement imbriqués.
2. **Population sélectionnée :** temps plein, année complète, salariés du privé, 18–65 ans ; les temps partiels, les entrées/sorties d'emploi et les parcours discontinus sont mal couverts.
3. **Rémunération annuelle, pas horaire :** le résultat mélange potentiellement salaire horaire, durée annuelle travaillée et primes.
4. **Composition de l'emploi :** les régressions inconditionnelles et les tests sur salariés stables limitent le biais de composition, mais ne démontrent pas que toute variation de composition est neutralisée.
5. **Groupes d'entreprises hétérogènes :** taille, secteur et date de signature diffèrent ; les contrôles observés ne garantissent pas l'absence de facteurs non observés corrélés à la dynamique salariale.
6. **Période exceptionnelle :** la convergence 2003–2005 ne ressemble pas à une hausse uniforme contemporaine du SMIC.
7. **Pas de résultat direct sur le bien-être :** aucun revenu disponible, pauvreté, emploi net, heures, prix ou marge d'entreprise n'est estimé.

## 8. Synthèse et niveau de preuve

**Constat principal :** la convergence des minima salariaux de 2003–2005 a été associée à une diffusion salariale mesurable au-delà des salariés directement au minimum. L'effet est statistiquement significatif jusqu'au septième décile pour les hommes comme pour les femmes, mais reste inférieur à 0,2 % sur les déciles de rémunération pour une hausse de 1 % du minimum selon la présentation des auteurs.

**Ce que l'étude apporte :**
- une stratégie d'identification plus crédible qu'une simple corrélation temporelle, grâce à la coexistence de six minima et à leur convergence différenciée ;
- une mesure de la diffusion au-delà du plancher, jusqu'à des rémunérations proches de deux SMIC ;
- des tests de robustesse cohérents avec le résultat principal.

**Ce qu'elle ne permet pas d'affirmer :**
- que l'emploi n'a pas diminué : les indicateurs d'emploi sont descriptifs et ne constituent pas une estimation causale ;
- que toutes les hausses nationales du SMIC produisent le même effet ;
- que les gains de salaire observés se traduisent intégralement en revenu disponible ou en réduction de pauvreté.

**Niveau de confiance :**
- **modéré** pour l'existence d'une diffusion salariale pendant la convergence 2003–2005 dans la population étudiée ;
- **faible à modéré** pour l'interprétation causale, car le traitement repose sur une hypothèse conditionnelle d'exogénéité des rythmes de convergence sans pré-tendances documentées ;
- **faible** pour toute conclusion sur l'emploi, les heures, le bien-être ou la transposition à une hausse isolée du SMIC actuel.

## 9. Références primaires

- Aeberhardt, Givord & Marbot (2012), INSEE DSE G2012/07, [PDF intégral](https://www.insee.fr/fr/statistiques/fichier/1380948/G2012-07.pdf).
- [Notice INSEE](https://www.insee.fr/fr/statistiques/1380948).
- Firpo, Fortin & Lemieux (2009), méthode des régressions de quantiles inconditionnels, citée par les auteurs.
- Pour la diffusion salariale à court terme : Koubi & Lhommeau (2007), ainsi que Goarant & Muller (2011), cités par Aeberhardt et al. ; ces travaux sont distincts et ne doivent pas être confondus avec leur expérience naturelle sur la convergence des GMR.
