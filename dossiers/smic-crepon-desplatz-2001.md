# Fiche d’audit — Crépon & Desplatz (2001), allègements de cotisations sur les bas salaires

- **Référence :** Bruno Crépon et Rozenn Desplatz, « Une nouvelle évaluation des effets des allégements de charges sociales sur les bas salaires », *Économie et Statistique*, n° 348, 2001-8, p. 3–34 (numéro paru en mars 2002).
- **Texte intégral :** [PDF de l'article et des commentaires](https://www.bnsp.insee.fr/ark:/12148/bc6p070n3zr.pdf) ; [notice INSEE](https://www.insee.fr/fr/statistiques/1376044?sommaire=1376054).
- **Commentaires publiés dans le même numéro :** Yannick L'Horty, « Baisse des cotisations sociales sur les bas salaires : une réévaluation » ; Guy Lacroix, « Baisse de charges sur les bas salaires et créations d'emplois ».
- **Critique complémentaire :** Henri Sterdyniak, « Une arme miracle contre le chômage ? », *Revue de l'OFCE*, n° 81, avril 2002.
- **Statut :** texte intégral, encadrés méthodologiques, tableaux 3 et 4, conclusion et commentaires consultés.
- **Avertissement :** cette étude porte sur les extensions d'allègements de cotisations patronales de 1995 et 1996, et non sur l'effet d'une hausse du SMIC.

## 1. Question et politique évaluée

Les auteurs cherchent à évaluer ex post les effets des extensions des allègements de cotisations patronales sur les bas salaires, principalement celles de septembre 1995 et octobre 1996. Le dispositif réduit les cotisations patronales au voisinage du SMIC et de façon dégressive jusqu'à 1,33 SMIC.

Au niveau du SMIC, l'allègement passe de 5,4 points de salaire brut en juillet 1993 à 18,2 points en octobre 1996. La dépense budgétaire indiquée par les auteurs atteint près de 38 milliards de francs en 1996 (environ 5,8 milliards d'euros).

Le traitement n'est donc pas une hausse du SMIC : c'est une réduction de coût employeur, dont l'intensité varie d'une entreprise à l'autre selon la structure des salaires qu'elle versait avant l'extension.

## 2. Données, période et population

### Sources et période

- Résultats d'entreprise observés entre 1994 et 1997.
- Déclarations annuelles de données sociales (DADS) pour la distribution des rémunérations et l'emploi salarié.
- Déclarations de bénéfices réels normaux (BRN) pour les comptes et performances des entreprises.
- Le traitement ex ante est calculé en appliquant à la structure des rémunérations de 1994 la législation d'allègement de 1997, puis en la comparant à celle de 1994. Il mesure ainsi l'exposition mécanique aux extensions de 1995–1996, sans utiliser les salaires postérieurs à la réforme pour définir le traitement.

### Échantillon

- 295 118 entreprises sont présentes dans les BRN de 1993 à 1997 au départ de la constitution du fichier.
- Après nettoyage et appariement BRN-DADS, l'échantillon final compte **87 720 entreprises**, soit environ 30 % du fichier initial.
- Il comprend 34 371 entreprises industrielles et 53 349 entreprises tertiaires, représentant environ **3,77 millions de salariés**.
- Les BRN concernent les entreprises dépassant le seuil de chiffre d'affaires de 3,5 millions de francs (seuil 1992) et relevant des bénéfices industriels et commerciaux.
- Les DADS couvrent les employeurs et salariés, hors salariés agricoles et agents de l'État ; leur exploitation statistique est exhaustive à partir de 1993.

Les auteurs indiquent que le panel final reflète assez bien l'évolution globale des effectifs, mais avec des écarts sectoriels : dans l'échantillon, l'emploi industriel recule moins que dans les comptes nationaux (−1,2 % contre −2,6 %) et l'emploi tertiaire progresse moins (+2,5 % contre +5,7 %). Le BTP est mieux représenté.

### Sélection du panel

Les entreprises doivent être présentes aux dates nécessaires, en particulier en 1993 et 1997. Ce panel cylindré exclut les entreprises créées et celles qui disparaissent pendant la période. Le nettoyage élimine près de la moitié des entreprises industrielles et plus de 60 % des entreprises de services à certaines étapes, notamment en raison de problèmes de mesure du coût du capital.

## 3. Traitement, contrefactuel et stratégie d'identification

### Traitement continu

Pour chaque entreprise, les auteurs calculent la réduction ex ante du coût moyen du travail qui résulterait de l'application de la législation de 1997 à sa structure de rémunérations de 1994. L'exposition varie de zéro à environ 9,5 % selon la part de salariés à bas salaire ; la moyenne citée dans le commentaire de Sterdyniak est d'environ 1,68 %.

Il n'existe pas un groupe témoin expérimental unique. L'identification repose sur la comparaison des évolutions 1994–1997 entre entreprises bénéficiant ex ante d'intensités différentes d'allègement.

### Hypothèse centrale

L'hypothèse d'identification est une indépendance conditionnelle : à caractéristiques observables données, la réduction ex ante du coût ne doit pas être corrélée aux évolutions contrefactuelles de l'entreprise en l'absence de réforme.

Les auteurs construisent un score synthétique à partir d'environ cinquante variables initiales (environ quarante retenues), incluant notamment taille, secteur, structure de qualification et de rémunération, croissance passée, caractéristiques financières, exposition à la concurrence internationale et autres variables de performance. Le score explique environ 50 % de la variance du traitement.

Cette stratégie est sophistiquée pour une exposition continue, mais elle ne rend pas aléatoire la structure salariale initiale. Elle ne neutralise que les facteurs observables et les facteurs approchés par les contrôles.

### Estimateurs

Trois familles de spécifications sont comparées :
1. régression paramétrique linéaire avec l'ensemble des contrôles ;
2. régression paramétrique utilisant le score comme résumé des contrôles ;
3. estimateur semi-paramétrique par séries/polynômes, autorisant une relation non linéaire entre le traitement, le score et les résultats.

L'estimateur semi-paramétrique est privilégié par les auteurs parce qu'il autorise une hétérogénéité de l'effet selon l'intensité de l'allègement. Il est toutefois beaucoup moins précis.

## 4. Résultats sur l'emploi et sensibilité au modèle

### Effet marginal d'un point de réduction ex ante (tableau 3)

Pour une hausse d'un point de la réduction ex ante du coût du travail, les coefficients d'évolution des effectifs salariés sont :

| Estimateur | Industrie | Tertiaire |
|---|---:|---:|
| (1) Contrôles complets, linéaire | 1,60 (SE 0,14) | 1,79 (SE 0,10) |
| (2) Score, linéaire | 2,00 (SE 0,16) | 2,36 (SE 0,12) |
| (3) Semi-paramétrique | 3,30 (SE 0,82) | 5,16 (SE 0,68) |

Ces coefficients sont des réponses marginales associées à un point de réduction ex ante, pas directement des élasticités au SMIC.

### Effet total estimé (tableau 4)

Les auteurs calculent la croissance des effectifs imputable à l'extension des dispositifs :
- spécification paramétrique complète : 1,28 % dans l'industrie et 2,35 % dans le tertiaire ;
- spécification paramétrique sur score : 1,60 % et 3,10 % ;
- spécification semi-paramétrique : **2,62 % dans l'industrie et 3,44 % dans le tertiaire**.

La réduction moyenne ex ante du coût du travail dans l'échantillon est estimée à environ 1,7 %.

### Chiffrage macroéconomique

En appliquant les taux semi-paramétriques à l'emploi salarié national retenu par les auteurs, ils obtiennent :
- environ 150 000 emplois créés ou sauvegardés dans l'industrie ;
- environ 310 000 dans le tertiaire ;
- soit **environ 460 000 emplois** entre 1994 et 1997.

Les auteurs précisent que ce chiffrage est imprécis : l'intervalle construit à partir des erreurs-types des taux de croissance est de **255 000 à 670 000**. Les estimations paramétriques donnent un résultat sensiblement inférieur : **290 000 emplois**, dont 75 000 dans l'industrie et 215 000 dans le tertiaire.

Il faut donc éviter de citer « 460 000 » comme un décompte certain ou comme le résultat unique de l'étude : il s'agit du chiffrage macro issu de la spécification semi-paramétrique privilégiée, plus flexible mais moins précise. Le chiffrage linéaire donne 290 000.

### Qualification et substitution

Les auteurs attribuent environ 220 000 des 460 000 emplois aux catégories qu'ils classent comme non qualifiées et 240 000 aux catégories qualifiées. Les non-qualifiés représenteraient ainsi près de la moitié des créations/sauvegardes, alors qu'ils représentent environ un quart de l'emploi total dans leur calcul.

Les auteurs interprètent les résultats comme la combinaison de :
- substitutions entre travailleurs non qualifiés et qualifiés, et dans une moindre mesure entre travail et capital ;
- effets de volume : baisse des coûts unitaires, répercussion supposée dans les prix, hausse de la demande et de la production.

Ils reconnaissent que les prix d'entreprise ne sont pas observés directement ; le mécanisme de prix est inféré à partir des coûts unitaires et du mark-up estimé.

## 5. Tendances préalables et robustesse

- Le traitement est construit à partir de la structure salariale de 1994, avant les extensions majeures de 1995–1996 : c'est un point fort qui limite la causalité inverse immédiate des salaires post-réforme.
- Les auteurs contrôlent des évolutions passées et de nombreuses caractéristiques observables, et comparent plusieurs estimateurs.
- Le score a un pouvoir explicatif d'environ 50 % de la variance du traitement.
- Les résultats qualitatifs sont de même signe avec les trois estimateurs, mais les ordres de grandeur sont très sensibles à la forme fonctionnelle.
- L'effet semi-paramétrique est systématiquement plus élevé et moins précis que les estimations linéaires.
- Le commentaire de Guy Lacroix souligne que le résultat est sensible au choix de l'estimateur et que des tests formels supplémentaires entre formes fonctionnelles auraient été utiles.

**Pré-tendances :** l'article ne présente pas un event-study avec coefficients annuels pré-traitement ni un test de tendances parallèles au sens moderne. Le recours aux évolutions passées dans les contrôles n'est pas équivalent à un test direct de pré-tendances entre groupes d'exposition.

## 6. Critiques et controverses

### 6.1 Yannick L'Horty (commentaire dans le même numéro)

L'Horty souligne la contribution méthodologique de l'étude et la richesse des données employeurs-salariés. Il insiste néanmoins sur la difficulté d'interpréter l'effet global lorsque les entreprises bénéficiaires gagnent des parts de marché au détriment d'entreprises moins bénéficiaires.

Il met en évidence plusieurs problèmes :
- le panel cylindré 1993–1997 exclut les créations et destructions d'entreprises, qui constituent pourtant un canal important d'ajustement ;
- l'effet de volume mesuré au niveau des entreprises peut redistribuer l'activité entre entreprises sans créer autant d'emplois nets au niveau agrégé ;
- si la baisse de prix des entreprises fortement exposées déplace la demande depuis les entreprises moins exposées, ces dernières ne sont pas un groupe témoin « non affecté » ;
- l'hypothèse selon laquelle les entreprises à exposition nulle ne sont pas affectées peut donc être violée par les effets de concurrence et de parts de marché.

Il considère néanmoins que l'étude apporte une contribution importante et utile aux approches macroéconomiques prospectives.

### 6.2 Guy Lacroix (commentaire dans le même numéro)

Lacroix reconnaît les qualités de l'appariement employeurs-salariés et l'innovation de l'extension du modèle causal de Rubin aux traitements continus. Il relève toutefois :
- une forte sensibilité des résultats au choix de l'estimateur ;
- un résultat semi-paramétrique plus élevé, mais moins précis ;
- le besoin de tests formels permettant de hiérarchiser les formes fonctionnelles ;
- la nécessité de mieux comprendre les décisions d'embauche et l'arbitrage capital-travail dans les entreprises.

Son commentaire est globalement plus favorable à l'apport empirique, mais ne valide pas le chiffre de 460 000 comme une mesure certaine.

### 6.3 Henri Sterdyniak (OFCE, 2002)

Sterdyniak formule une critique plus radicale :
1. **Temps partiel :** l'étude mesure les effectifs, mais pas les heures travaillées. Entre 1994 et 1997, il relève que l'emploi en effectifs augmente plus vite que l'emploi en équivalent temps plein ; une part de la hausse des effectifs pourrait donc refléter le développement du temps partiel, particulièrement dans les entreprises à bas salaires.
2. **Mesure du coût et de la production :** les coûts unitaires et les volumes sont construits statistiquement et non observés directement au niveau de l'entreprise. Il estime que certaines erreurs de mesure du coût du travail peuvent se répercuter mécaniquement dans la mesure de la production en volume.
3. **Échantillon :** il critique l'exclusion d'environ 70 % des entreprises initiales et la représentativité du panel cylindré, dont les évolutions d'effectifs divergent de celles de l'ensemble de l'économie.
4. **Sensibilité de l'estimateur :** l'estimation semi-paramétrique produit des effets bien plus élevés que les estimations linéaires, mais avec une précision plus faible et une dépendance à la flexibilité fonctionnelle.
5. **Financement :** il rappelle que les allègements de 1995 ont été financés dans le contexte d'une hausse de TVA et reproche à l'évaluation de ne pas intégrer les effets de ce financement sur les entreprises non bénéficiaires et la demande.
6. **Passage micro-macro :** il conteste l'extrapolation du différentiel entre entreprises à un nombre net d'emplois nationaux, notamment si les gains de parts de marché des entreprises aidées se font au détriment d'autres entreprises.
7. **Créations/destructions d'entreprises :** l'exclusion des entrées et sorties peut manquer des déplacements d'activité et d'emploi entre entreprises.

Cette critique est une analyse contradictoire argumentée, pas une réplication économétrique démontrant que l'effet est nul. Elle doit être prise au sérieux sans être traitée comme une estimation alternative causale.

## 7. Ce que l'étude mesure — et ne mesure pas

**Mesuré :**
- variation des effectifs salariés par entreprise ;
- structure de qualification ;
- masse salariale et coût moyen du travail ;
- valeur ajoutée, capital et productivité selon les définitions comptables de l'article ;
- association entre intensité d'allègement ex ante et évolution des performances.

**Non mesuré directement ou incomplet :**
- heures travaillées et emploi en équivalent temps plein ;
- prix de vente et volumes physiques au niveau de chaque entreprise ;
- créations et destructions d'entreprises dans le panel cylindré ;
- effets de financement macroéconomique ;
- effets nets de concurrence et de déplacement entre entreprises ;
- revenu disponible des ménages et bien-être ;
- effet causal d'une hausse du SMIC légal.

## 8. Synthèse et niveau de preuve

**Constat principal :** dans le panel d'entreprises étudié, celles qui étaient mécaniquement plus exposées aux extensions des allègements de 1995–1996 ont connu une progression relative plus forte de leurs effectifs entre 1994 et 1997, après contrôle de nombreuses caractéristiques observables.

**Ordre de grandeur :** le chiffre de 460 000 emplois provient de l'estimateur semi-paramétrique privilégié, avec un intervalle de 255 000 à 670 000. Les estimateurs paramétriques donnent environ 290 000 emplois. L'écart entre ces résultats est substantiel et constitue une incertitude méthodologique centrale.

**Niveau de confiance :**
- modéré pour l'association conditionnelle entre exposition ex ante et évolution de l'emploi dans le panel retenu ;
- faible à modéré pour l'interprétation causale, dépendante de l'indépendance conditionnelle et de l'absence de spillovers non contrôlés ;
- faible pour le chiffre macroéconomique net de 460 000, compte tenu de la sélection du panel, de l'absence de créations/destructions d'entreprises, des effets de concurrence et du financement ;
- nul comme preuve directe de l'effet d'une hausse du SMIC légal, puisque l'instrument étudié est un allègement de cotisations.

**Conclusion opérationnelle :** conserver l'étude comme une preuve importante sur les réactions des entreprises à la baisse du coût du travail au voisinage du SMIC. Présenter ensemble les résultats semi-paramétriques et paramétriques, les intervalles d'incertitude et les critiques. Ne jamais transformer le chiffre de 460 000 en nombre incontestable d'emplois nets créés par la baisse des charges, et encore moins en preuve qu'une hausse du SMIC détruit ou crée un nombre équivalent d'emplois.

## 9. Sources

- Crépon & Desplatz (2001), article intégral et commentaires : https://www.bnsp.insee.fr/ark:/12148/bc6p070n3zr.pdf
- Notice INSEE de l'article : https://www.insee.fr/fr/statistiques/1376044?sommaire=1376054
- L'Horty, commentaire : https://www.insee.fr/fr/statistiques/1376052?sommaire=1376054
- Lacroix, commentaire : https://www.insee.fr/fr/statistiques/1376053?sommaire=1376054
- Sterdyniak (2002), OFCE : https://www.ofce.fr/pdf/revue/7-81.pdf


## 7. Mise en perspective DARES–Trésor (Ourliac & Nouveau, 2012)

La synthèse DARES n°169 reprend l’intervalle à 95 % de Crépon & Desplatz comme 260 000–670 000 emplois (valeurs arrondies), avec une estimation centrale de 460 000 : 220 000 emplois peu qualifiés et 240 000 qualifiés. Elle retient un coût brut par emploi de 10 900–28 000 € de 2009. Cet intervalle correspond à la fourchette déjà décrite dans cette fiche (environ 255 000–670 000) ; il ne s’agit pas d’une réplication.

La synthèse rappelle la principale critique : les entreprises les plus aidées peuvent gagner des parts de marché aux dépens d’entreprises moins aidées, de sorte que les réallocations ne se traduisent pas nécessairement par des créations nettes macroéconomiques. Elle précise toutefois que Crépon & Desplatz ont répondu à cette objection en contrôlant la concurrence intra- et intersectorielle. La question restante porte donc sur les effets de déplacement résiduels, le passage au niveau agrégé et le financement des allègements, et non sur une absence totale de contrôle de la concurrence.

Référence : Ourliac & Nouveau (2012), DARES Document d’études n°169, tableaux D et commentaires, p. 31–32 : https://dares.travail-emploi.gouv.fr/sites/default/files/pdf/DE2012-_no169.pdf.
