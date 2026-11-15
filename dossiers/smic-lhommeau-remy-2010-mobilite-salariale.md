# Audit — Lhommeau & Rémy (2010) : allègements et mobilité salariale des bas salaires

- **Référence :** Bertrand Lhommeau et Véronique Rémy, « Les politiques d’allégements ont-elles un effet sur la mobilité salariale des travailleurs à bas salaires ? », *Économie et Statistique*, n°429–430, pp. 21–49, publié le 20 août 2010 (numéro référencé 2009), DOI [10.3406/estat.2009.8062](https://doi.org/10.3406/estat.2009.8062).
- **Texte intégral :** [PDF INSEE](https://www.insee.fr/fr/statistiques/fichier/1377392/ES429B%20.pdf) ; [notice INSEE](https://www.insee.fr/fr/statistiques/1377392?sommaire=1377406) ; [version Persée](https://www.persee.fr/doc/estat_0336-1454_2009_num_429_1_8062).
- **Nature de la preuve :** modèle théorique d’appariement + estimation de panel à effets individuels (Mundlak) sur données DADS regroupées en cellules. Étude des trajectoires salariales, pas évaluation de l’effet causal d’une hausse isolée du SMIC.

## 1. Question et mécanisme

Les auteurs étudient si les allègements patronaux instaurés à partir de 1993 affectent la progression salariale des travailleurs à bas salaires. Deux effets antagonistes sont attendus :
- **effet de surplus :** les allègements diminuent le coût moyen du travail et dégagent une marge qui peut financer des augmentations ou promotions ;
- **effet de progressivité :** lorsque l’allègement décroît avec le salaire, augmenter le salaire brut fait perdre une partie de l’aide ; le coût marginal d’une augmentation est donc plus élevé, ce qui peut freiner les promotions.

Le modèle théorique montre que le résultat dépend de la forme du barème, du taux d’allègement et de son seuil de sortie. Il s’agit d’un arbitrage de conception du dispositif, pas d’un effet mécanique identique pour tous les salariés.

## 2. Données et champ

- **Source :** panel DADS de l’Insee, années 1984–2003.
- **Champ :** salariés du secteur privé (secteurs EB–EF et EH–EP selon la nomenclature utilisée), hors apprentissage, intérim et contrats aidés.
- **Population d’analyse :** salariés dont la rémunération mensuelle est sous les seuils étudiés (principalement 1,3 SMIC ; variantes à 1,1 et 1,8 SMIC), et qui restent dans la même entreprise entre t et t+2.
- **Unité d’estimation :** les auteurs regroupent les données en cellules d’entreprises proches (secteur, taille et recours à la main-d’œuvre peu qualifiée) afin de réduire un fichier individuel de plusieurs millions d’observations et de construire un panel cylindré.
- **Deux résultats mesurés :** croissance du salaire réel des salariés bas salaire entre t et t+2 ; taux de sortie du bas salaire, c’est-à-dire part de ceux qui dépassent le seuil deux ans plus tard.
- **Variables de politique :** intensité des allègements (montant des exonérations / masse salariale) et progressivité du coût du travail (hausse du coût lorsqu’on augmente de 1 % le salaire brut). Le modèle contrôle aussi l’évolution du SMIC/GMR, la valeur ajoutée sectorielle et la RTT.

Le champ exclut les salariés qui changent d’entreprise ou sortent de l’emploi durant la fenêtre étudiée : l’étude renseigne donc les progressions salariales conditionnelles au maintien dans le même employeur, pas la mobilité professionnelle globale.

## 3. Méthode et résultats quantitatifs

Les auteurs estiment un modèle à effets individuels de type Mundlak, combinant les variations dans le temps au sein des cellules et les différences structurelles entre cellules. Le regroupement facilite l’estimation, mais fait perdre une partie de l’hétérogénéité individuelle.

Pour les salaires mensuels inférieurs à 1,3 SMIC, le tableau 3 rapporte :
- coefficient de l’intensité moyenne des allègements : **+0,502** (écart-type 0,101), significatif à 1 % ; pour les salariés à temps complet : **+0,529** (0,093) ;
- coefficient de la progressivité du coût des bas salaires : **−12,817** (1,443), significatif à 1 % ; temps complet : **−8,674** (1,020) ;
- évolution du SMIC/GMR : **+0,142** (0,069), significatif à 5 % ; temps complet : **+0,107** (0,056), significatif à 5 %.

Ces coefficients portent sur les variables construites et l’échelle de la spécification ; ils ne sont pas des élasticités directement transposables à une hausse de 1 % du SMIC.

L’interprétation des auteurs est la suivante : au sein d’une cellule, une hausse de l’intensité des allègements soutient la croissance des salaires et la sortie du bas salaire, tandis qu’une progressivité accrue du coût freine ces deux mobilités. L’effet négatif de la progressivité domine l’effet positif d’intensité dans le bilan global.

### Ordres de grandeur construits par les auteurs

- En 1996, pour les salaires inférieurs à 1,3 SMIC, la contribution estimée des allègements réduit de **2,7 points** le taux de croissance salarial entre t et t+2 ; en ajoutant l’effet des hausses du SMIC sur la période, la réduction estimée est ramenée à **1,8 point**. Le taux de croissance observé de référence est alors de **13,4 %**.
- Par rapport au barème moyen 2001–2002, le barème Fillon de 2005 contribuerait à réduire la croissance des salaires sous 1,3 SMIC de **2,6 points**, contre **1,7 point** pour le barème antérieur.
- L’effet négatif estimé diminue lorsque la définition des bas salaires est élargie à 1,8 SMIC ; l’intensité des allègements est davantage favorable aux salaires les plus proches du minimum.

Ces chiffres sont des contributions calculées à partir des coefficients du modèle et des barèmes observés, non des différences expérimentales entre salariés identiques assignés à des régimes distincts.

## 4. Ce que l’étude permet de conclure

1. Les allègements ont des effets ambivalents sur les trajectoires : l’intensité de l’aide peut favoriser la progression salariale, tandis que sa dégressivité peut la freiner.
2. Pour le champ et les périodes étudiés, les auteurs concluent que l’effet négatif de la progressivité l’emporte en moyenne sur l’effet positif de l’intensité.
3. Les hausses du SMIC/GMR sont intégrées comme variable explicative et atténuent le frein estimé sur les salaires. Le SMIC peut donc compenser partiellement un ralentissement des hausses salariales lié aux allègements.
4. Les résultats sont plus marqués pour les salaires très proches du minimum et s’atténuent quand on élargit le seuil à 1,8 SMIC.
5. L’étude met en évidence un arbitrage entre ciblage des aides près du SMIC (potentiellement favorable à l’emploi) et progression des rémunérations (potentiellement pénalisée par la dégressivité).

## 5. Limites et niveau de preuve

- **Sélection des salariés qui restent en emploi et dans la même entreprise :** les transitions vers un autre employeur, le chômage, l’inactivité et les destructions d’emploi ne sont pas l’objet de l’estimation salariale. La mobilité observée est conditionnelle à la survie de la relation d’emploi.
- **Cellulage et agrégation :** les cellules regroupent des entreprises proches mais ne sont pas des entreprises fixes ni des individus suivis individuellement dans l’équation finale ; l’hétérogénéité à l’intérieur des cellules subsiste.
- **Endogénéité potentielle :** l’intensité et la progressivité des allègements peuvent évoluer avec la composition salariale, les décisions de gestion, les changements de main-d’œuvre et les politiques d’entreprise. Les effets fixes et contrôles réduisent certains biais mais ne créent pas une assignation exogène.
- **Contexte concomitant :** les années 1998–2005 combinent RTT, GMR, convergence des minima et réforme Fillon. Les auteurs modélisent la RTT et le SMIC/GMR, mais la séparation parfaite de ces changements reste difficile.
- **Mesure mensuelle :** les seuils sont exprimés en salaire mensuel ; les variations de temps de travail et de temps partiel peuvent modifier la position relative au seuil sans correspondre à une progression du salaire horaire. Les auteurs proposent aussi des résultats à temps complet.
- **Pas d’effet emploi net :** le papier ne mesure ni les créations nettes d’emplois, ni les heures, ni les effets macroéconomiques de financement des exonérations.

**Appréciation :** preuve informative et relativement détaillée sur le mécanisme de progression salariale dans les entreprises, mais niveau causal modéré à faible pour l’effet propre des allègements. Elle ne doit pas être citée comme démonstration qu’une hausse du SMIC détruit ou crée des emplois.

## 6. Synthèse opérationnelle

**Résultat principal :** les allègements peuvent à la fois soutenir et freiner les carrières salariales. Dans l’estimation de Lhommeau & Rémy, le coût marginal croissant induit par la dégressivité l’emporte sur le surplus créé par la baisse du coût moyen ; le frein est toutefois partiellement compensé par les revalorisations du SMIC/GMR.

**Implication pour l’étude du SMIC :** une revalorisation du SMIC peut soutenir directement les bas salaires et réduire la stagnation relative des rémunérations, mais ce papier ne permet pas d’isoler son effet causal sur les carrières : il étudie principalement les allègements, avec le SMIC/GMR comme variable de contrôle et de diffusion salariale.

**Conclusion :** il faut distinguer trois questions dans la synthèse générale : (a) effet d’une hausse du SMIC sur le salaire horaire des salariés concernés ; (b) diffusion de cette hausse aux salaires proches et aux grilles ; (c) effet des exonérations dégressives sur les promotions au sein des entreprises. Lhommeau & Rémy éclairent surtout la troisième, et partiellement la deuxième.

## 7. Sources

- Lhommeau & Rémy (2010), texte intégral, *Économie et Statistique* n°429–430 : https://www.insee.fr/fr/statistiques/fichier/1377392/ES429B%20.pdf
- Notice INSEE : https://www.insee.fr/fr/statistiques/1377392?sommaire=1377406
- Persée, notice et résumé : https://www.persee.fr/doc/estat_0336-1454_2009_num_429_1_8062
- Lhommeau & Rémy (2008), document de travail cité pour la description des données et indicateurs ; à retrouver pour vérification complémentaire.
