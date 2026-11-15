# Cette, Chouard & Verdugo (2011) — effets des hausses du SMIC sur le salaire moyen (1970–2009)

**Référence complète.** Gilbert Cette, Valérie Chouard et Grégory Verdugo (2011), « Les effets des hausses du Smic sur le salaire moyen », *Économie et Statistique*, n° 448–449, pp. 3–28. Version de travail Banque de France, Document de travail n° 366, février 2012.

- Article Insee/PDF : https://www.insee.fr/fr/statistiques/fichier/1377686/ES448A.pdf
- Notice Persée : https://www.persee.fr/doc/estat_0336-1454_2011_num_448_1_9746
- Document de travail Banque de France : https://publications.banque-france.fr/sites/default/files/medias/documents/working-paper_366_2012.pdf

## 1. Question et contribution

L'étude cherche à mesurer comment les revalorisations du SMIC se transmettent à deux indicateurs du salaire moyen :
- le salaire horaire de base des ouvriers (SHBO), à structure constante, brut et hors primes et heures supplémentaires ;
- le salaire moyen par tête (SMPT), agrégat macroéconomique qui comprend primes, heures supplémentaires et effets de structure, pour l'ensemble des salariés.

Sa contribution centrale est de ne pas supposer une transmission immédiate : elle autorise des effets distribués sur le trimestre courant et les trois trimestres précédents. Elle distingue aussi les trois composantes institutionnelles de la hausse du SMIC : indexation sur les prix, indexation sur la moitié des gains de pouvoir d'achat du SHBO, coups de pouce discrétionnaires.

Période : séries trimestrielles françaises de 1970 à 2009 ; les équations sont estimées sur 156 observations trimestrielles pour 1971–2009. Champ géographique : France métropolitaine.

## 2. Données et construction des variables

Les auteurs reconstituent une chronologie mensuelle des revalorisations du SMIC depuis 1970 à partir de sources de la Direction générale du Travail, de la Dares et de la Direction générale du Trésor, puis trimestrialisent les hausses. Chaque hausse est décomposée comptablement en :
1. contribution de l'indexation sur les prix ;
2. contribution de l'indexation sur la moitié des gains de pouvoir d'achat du SHBO ;
3. coups de pouce discrétionnaires.

Les séries de SHBO et de salaire mensuel de base (SMB) viennent de l'enquête Acemo de la Dares. Le SMB n'étant disponible qu'à partir de 1985, il n'est pas utilisé dans l'estimation principale sur longue période. Le SMPT vient des comptes nationaux de l'Insee. Sont également mobilisés : indice des prix, chômage (niveau et variation), productivité horaire, durée du travail et effets saisonniers trimestriels.

Les auteurs testent une variante du modèle 3 qui tient compte des garanties mensuelles de rémunération (GMR) issues des lois Aubry, pondérées par la proportion de salariés concernés. Les résultats sont similaires à ceux du modèle qui utilise le seul SMIC sur toute la période.

**Traitement particulier de 2003–2005 :** les revalorisations liées à la convergence des minima salariaux sont ventilées en trois contributions « fictives » selon les composantes habituelles. Au-delà de l'indexation calculée sur les prix et sur le SHBO, le surplus de convergence est comptabilisé comme coup de pouce. Cette convention est importante : elle ne signifie pas qu'il s'agissait d'un coup de pouce politique ordinaire.

## 3. Stratégie économétrique

Les auteurs estiment des équations de salaire trimestrielles par moindres carrés ordinaires, avec 156 observations. Les spécifications successives :
- contrôlent les variations contemporaines et retardées des prix ;
- intègrent productivité, durée du travail, niveau et variation du chômage ;
- ajoutent les variations du SMIC et leurs retards ;
- décomposent ensuite les variations du SMIC entre les trois motifs institutionnels ;
- autorisent enfin une rupture de l'indexation directe des salaires sur les prix au premier trimestre 1982, date retenue après recherche de rupture statistique.

Le modèle dynamique retient les retards du salaire et du SMIC jusqu'à trois trimestres. Les élasticités de long terme sont calculées à partir de la somme des effets dynamiques, en évaluant les polynômes de retards à fréquence de long terme.

**Nature de l'identification :** série temporelle macroéconomique, sans groupe traité/témoin ni choc exogène isolé. Les auteurs reconnaissent explicitement un risque d'endogénéité : chômage, prix et salaires peuvent se déterminer mutuellement. Ils indiquent qu'une prise en compte complète de ce risque nécessiterait un modèle simultané beaucoup plus complexe. Il s'agit donc d'estimations conditionnelles de transmission dynamique, pas d'une expérience naturelle permettant d'attribuer sans réserve un effet causal à chaque épisode.

## 4. Résultats

### 4.1. Le SMIC a progressé plus vite que les salaires moyens

Sur les quatre décennies 1971–2010 utilisées pour les moyennes descriptives, le pouvoir d'achat du SMIC progresse de 2,5 % par an en moyenne, contre 1,8 % pour le SHBO et 1,4 % pour le SMPT. Sur la dernière décennie considérée, les rythmes moyens sont respectivement de 1,6 %, 1,2 % et 1,0 % (le SMB progresse de 0,8 % sur son champ disponible).

La contribution annuelle moyenne à la hausse nominale du SMIC est d'environ 4,6 points pour les prix et 2,5 points pour les gains de pouvoir d'achat. À l'intérieur de ces derniers, les coups de pouce représentent environ 1,5 point et l'indexation sur la moitié des gains du SHBO environ 1 point. Les coups de pouce contribuent donc davantage aux gains réels du SMIC que la stricte règle d'indexation sur le SHBO.

### 4.2. Transmission globale des hausses du SMIC

Dans le modèle 3, qui autorise des retards, les élasticités estimées du salaire moyen aux variations du SMIC sont :
- SHBO : 0,14 à court terme et 0,34 à long terme ;
- SMPT : 0,06 à court terme et 0,30 à long terme.

Une élasticité de long terme de 0,34 signifie qu'une hausse durable de 1 % du SMIC est associée, après prise en compte des retards, à une hausse d'environ 0,34 % du SHBO dans cette spécification. Pour le SMPT, l'ordre de grandeur est 0,30 %.

Les auteurs estiment donc que la transmission est progressive et plus importante à long terme qu'au trimestre de la hausse. Ces élasticités sont agrégées : elles ne disent pas quelle part des salariés individuels reçoit une augmentation donnée.

### 4.3. Effets selon l'origine de la revalorisation

Le modèle 5 décompose les trois composantes et distingue l'avant/après 1982 pour l'indexation directe sur les prix. Élasticités estimées de court et long terme :

| Composante de revalorisation | SHBO court terme | SHBO long terme | SMPT court terme | SMPT long terme |
|---|---:|---:|---:|---:|
| Indexation prix (directe), avant 1982 | 0,51 | 0,54 | 0,17 | 0,53 |
| Indexation prix (directe), à partir de 1982 | 0,10 | 0,36 | 0,04 | 0,30 |
| Contribution prix via le SMIC | 0,19 | 0,35 | 0,07 | 0,30 |
| Indexation sur la moitié du pouvoir d'achat du SHBO | 0,00 | 0,65 | 0,01 | 0,14 |
| Coups de pouce | 0,11 | 0,23 | 0,08 | 0,28 |

Les coups de pouce se transmettraient à long terme à hauteur de 23 % au SHBO et 28 % au SMPT. Ils ne sont donc pas sans effet sur le salaire moyen, mais leur transmission estimée est inférieure à celle de la composante d'indexation sur le SHBO pour le SHBO lui-même.

### 4.4. Boucle de rétroaction SMIC–SHBO

Le résultat le plus singulier concerne l'indexation du SMIC sur la moitié des gains de pouvoir d'achat du SHBO : la contribution de cette composante au SMIC se répercute à long terme à hauteur de 65 % sur le SHBO lui-même, contre 14 % sur le SMPT. Les auteurs y voient une circularité potentielle : les gains du SHBO augmentent le SMIC par la formule légale, puis cette hausse du SMIC exerce à son tour une pression sur le SHBO.

### 4.5. Rupture de 1982 et inflation

L'indexation totale de long terme des salaires sur les prix (effet direct et canal indirect via le SMIC) est estimée presque complète avant 1982 : 89 % pour le SHBO et 83 % pour le SMPT. Après 1982, elle est d'environ 71 % pour le SHBO et 60 % pour le SMPT. Les auteurs interprètent cela comme un effet marqué de la désindexation partielle engagée après le tournant de 1982.

## 5. Robustesse et limites

- Les auteurs examinent la colinéarité entre les variables : les corrélations supérieures à 0,7 concernent surtout les variations des prix et la composante prix du SMIC. Ils indiquent que signes et amplitudes des coefficients restent globalement stables.
- Ils testent l'hypothèse selon laquelle les différences entre composantes refléteraient simplement la saisonnalité (coups de pouce et indexation SHBO concentrés au troisième trimestre). Une spécification distinguant les hausses du troisième trimestre donne des résultats proches.
- Les coefficients du quatrième retard ne sont pas significativement différents de zéro ; l'ajout d'un quatrième retard ne modifie pas les trois premiers.
- Les auteurs signalent eux-mêmes le risque d'endogénéité des prix, du chômage et des salaires, non résolu par une estimation simultanée.
- Les données agrégées ne permettent pas d'observer l'hétérogénéité entre secteurs, entreprises, qualifications, temps partiel et types de ménages.
- L'étude ne mesure ni emploi, ni heures travaillées, ni profits, ni prix de vente, ni productivité causée par une hausse donnée, ni revenu disponible.
- La rupture de 1982 est choisie à partir d'un test de date de rupture ; elle peut résumer plusieurs changements macroéconomiques et institutionnels concomitants.
- Les revalorisations 2003–2005 sont décomposées par convention en composantes fictives ; l'effet estimé des « coups de pouce » n'est donc pas directement celui d'une décision discrétionnaire isolée dans cette période.
- Les estimations sont des élasticités macroéconomiques historiques, non des effets causaux identifiés par un instrument ou une comparaison contrefactuelle.

## 6. Confrontation avec Koubi & Lhommeau (2007)

Les deux études se complètent, mais leurs coefficients ne sont pas directement comparables :
- Koubi & Lhommeau utilisent des grilles de postes d'entreprises sur 2000–2005 et mesurent la diffusion selon le niveau relatif au minimum et le délai ; ils trouvent une forte transmission près du SMIC et une transmission retardée vers 1,4–1,5 SMIC.
- Cette, Chouard & Verdugo utilisent des séries macroéconomiques 1970–2009 ; ils estiment un effet agrégé de long terme d'environ 0,34 sur le SHBO et 0,30 sur le SMPT pour la hausse du SMIC dans le modèle 3.
- Le modèle macro de longue période ne permet pas d'identifier la distribution de l'effet par tranche de salaire ; l'étude micro de grille ne couvre pas les petites entreprises ni les salaires totaux.
- Les auteurs de l'étude macro notent eux-mêmes que la comparaison avec Koubi & Lhommeau est délicate : leurs effets temporels absorbent une partie des effets moyens, et les effets fixes de tranches peuvent absorber la diffusion retardée.

## 7. Synthèse opérationnelle pour l'étude historique

**Ce que l'étude établit avec une confiance raisonnable :** les hausses du SMIC se transmettent aux salaires moyens au-delà des seuls bénéficiaires directs ; la transmission est dynamique, plus forte à long terme et dépend de la composante de revalorisation. Les coups de pouce ont un effet mesurable mais plus limité que la composante de rétroaction indexée sur le SHBO.

**Ce qu'elle suggère sans le démontrer causalement :** le mécanisme français d'indexation peut amplifier les fluctuations inflationnistes via une boucle SMIC–SHBO ; la désindexation partielle après 1982 a réduit le degré de transmission directe des prix aux salaires.

**Ce qu'elle ne permet pas de conclure :** elle ne dit pas si une hausse du SMIC améliore le bien-être net, crée ou détruit des emplois, réduit les heures, est absorbée par les marges ou les prix, ni comment le revenu disponible des ménages évolue.

**Conclusion :** cette étude est centrale pour la chronologie historique des revalorisations et leurs effets de diffusion salariale, mais elle doit être articulée aux études microéconomiques sur emploi, trajectoires et revenus pour établir un bilan global des épisodes.
