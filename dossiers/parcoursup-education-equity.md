# Parcoursup et l'égalité des chances dans le système éducatif français

> **Statut :** recherche en cours — cadrage initial et inventaire documentaire, 13 novembre 2026.

## Question centrale
Dans quelle mesure le système éducatif français permet-il une égalité réelle des chances, de la formation des acquis jusqu'à l'accès à l'enseignement supérieur et à la réussite dans les études ?

Parcoursup est le premier terrain d'observation, mais ne doit pas être confondu avec l'ensemble du système éducatif. Une plateforme d'admission peut être plus ou moins efficace dans l'appariement des candidats et des formations sans corriger les inégalités construites en amont, ni garantir les conditions de réussite après l'admission.

## Cadre d'analyse : la chaîne éducative
1. **Petite enfance et acquis initiaux** — conditions familiales, accès aux modes d'accueil, langage et compétences précoces.
2. **École et collège** — apprentissages, orientation progressive, ségrégation scolaire et disparités territoriales.
3. **Lycée** — voies générale, technologique et professionnelle, spécialités, notes, accompagnement et aspirations.
4. **Information et formulation des vœux** — connaissance de l'offre, autocensure, mobilité, coûts, stratégies familiales et accompagnement.
5. **Sélection et affectation** — critères des formations, commissions d'examen des vœux, algorithmes locaux, listes d'appel, capacités et quotas.
6. **Inscription et conditions matérielles** — logement, transport, ressources, bourses, santé et emploi étudiant.
7. **Réussite et trajectoires** — passage en année supérieure, réorientation, abandon, diplomation et insertion.

## Premiers constats documentés

### Fonctionnement et volumes de Parcoursup 2026
Le bilan ministériel indique 1 046 000 candidats pour la campagne 2026, soit +66 000 en un an. Il rapporte 603 910 lycéens ayant reçu au moins une proposition, soit 91,5 % des lycéens ayant formulé des vœux. La note statistique SIES indique pour sa part que 93,7 % des néo-bacheliers inscrits ont reçu au moins une proposition et 81,0 % en ont accepté une.

Ces taux ne sont pas interchangeables : les populations de référence et dénominateurs diffèrent. Ils mesurent la réception ou l'acceptation d'une proposition, pas l'accès au premier choix, la qualité de l'appariement, l'inscription effective ou la réussite ultérieure.

Sources : [bilan Parcoursup 2026](https://www.enseignementsup-recherche.gouv.fr/fr/parcoursup-2026-des-resultats-stables-dans-un-contexte-de-progression-historique-des-candidatures-104400) ; [note Flash SIES 2026-26](https://www.enseignementsup-recherche.gouv.fr/fr/parcoursup-2026-les-propositions-d-admission-dans-l-enseignement-superieur-104448).

### Les inégalités se forment en amont
L'Insee documente des écarts d'acquis associés à l'origine sociale dès l'entrée en maternelle. PISA 2022 montre un écart de 113 points en mathématiques entre les quartiles socio-économiques supérieur et inférieur en France, contre 93 points en moyenne dans l'OCDE.

Ces résultats justifient d'étudier la chaîne éducative entière. Ils ne démontrent pas, à eux seuls, que Parcoursup reproduit mécaniquement ces écarts, ni que l'origine sociale est l'unique facteur explicatif.

Sources : [Insee — Inégalités sociales dans l'enseignement scolaire](https://www.insee.fr/fr/statistiques/8612522) ; [OCDE — PISA 2022, France](https://www.oecd.org/en/publications/pisa-2022-results-volume-i-and-ii-country-notes_ed6fbcc5-en/france_8008535b-en.html).

### Mise en perspective internationale
L'OCDE estime que 75 % des 25-34 ans en France dont au moins un parent est diplômé du supérieur ont eux-mêmes obtenu un diplôme du supérieur, contre 32 % lorsque les parents n'ont pas achevé le deuxième cycle du secondaire. Cet indicateur intergénérationnel éclaire la persistance des inégalités, mais ne mesure pas l'effet propre de Parcoursup.

Source : [OCDE — Regards sur l'éducation 2025, France](https://www.oecd.org/content/dam/oecd/fr/publications/reports/2025/09/education-at-a-glance-2025-country-notes_9749f4ff/france_0639c7fb/aca6dceb-fr.pdf).

## Données ouvertes et fonctionnement de l'examen des candidatures

Le jeu de données ouvert Parcoursup 2025 constitue une première base exploitable : 115 variables, 14 252 formations et 1 015 200 candidats, avec un sous-ensemble de 652 800 néo-bacheliers. Il contient notamment des agrégats par sexe, série du bac, statut de boursier, origine géographique, capacité, propositions, admissions et rang du dernier appelé. La documentation précise toutefois que certains indicateurs cartographiques ne sont pas recalculables à partir du fichier et que l'unité d'observation est la formation, non l'individu. [Jeu de données et documentation](https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-parcoursup/?flg=fr).

Au 13 novembre 2026, la page officielle indique que les données de synthèse 2026 par formation doivent encore être publiées ; l'analyse détaillée devra donc commencer avec le millésime 2025, puis être actualisée lorsque le millésime 2026 sera disponible. [Page Parcoursup sur les données de formation](https://www.parcoursup.gouv.fr/trouver-une-formation/quelles-formations-sont-accessibles-sur-parcoursup-1318).

Il faut également distinguer la plateforme nationale des décisions des formations : les commissions d'examen des vœux (CEV) définissent et appliquent les critères de classement ; Parcoursup assure la mise en relation et le processus d'appel. Près de 19 000 rapports d'analyse des candidatures 2026 sont annoncés comme accessibles depuis les fiches des formations. Cela ouvre une piste concrète d'analyse des critères réellement déclarés et de leur hétérogénéité, sans confondre transparence documentaire et audit indépendant des pratiques. [Explication officielle des modalités d'examen](https://www.parcoursup.gouv.fr/candidater-sur-parcoursup/comment-les-formations-examinent-les-candidatures-1357).

## Hypothèses de travail — non établies
- Les écarts d'accès et de réussite dans le supérieur résultent en partie de mécanismes cumulatifs qui se forment avant la terminale.
- Des taux élevés de propositions peuvent coexister avec des inégalités d'accès aux formations les plus demandées, de qualité de l'appariement et de trajectoires après admission.
- La réception et l'acceptation d'une proposition ne sont pas des mesures suffisantes de la réussite dans le supérieur.

Ces hypothèses doivent être testées par origine sociale, type de baccalauréat, genre, territoire, handicap, situation de boursier, sélectivité, discipline et trajectoire post-admission, avec des données adaptées.

## Questions à instruire

### Critères locaux et commissions d'examen des vœux
- Quels critères sont effectivement mobilisés par les commissions d'examen des vœux (CEV), avec quelles pondérations et quelles marges d'appréciation ?
- Les rapports d'analyse des candidatures sont-ils suffisamment précis, comparables et accessibles pour permettre un audit externe ?
- Les critères varient-ils selon les filières, les établissements, les territoires et les profils de candidats ?
- Comment distinguer les critères formellement annoncés, les outils d'aide à la décision et les décisions humaines finales ?

### Parcoursup : que mesure-t-on réellement ?
- Quels sont les dénominateurs exacts des taux de proposition et d'acceptation ?
- Quelle part des candidats obtient son premier vœu, un vœu de rang élevé ou une formation choisie par défaut ?
- Comment les résultats varient-ils selon voie du bac, origine sociale, statut de boursier, territoire et formation ?
- Quelle part revient aux critères de classement, aux capacités, aux préférences et aux stratégies de vœux ?
- Quelle transparence réelle sur les critères locaux et les classements ?

### En amont
- Quand les écarts d'acquis apparaissent-ils, s'accumulent-ils ou se réduisent-ils ?
- Quels rôles jouent la ségrégation scolaire, les choix de spécialités, les options, les établissements et l'information ?
- Comment distinguer aspirations, préférences, autocensure et contraintes objectives ?

### En aval
- Quels sont les taux de passage, de réorientation, d'abandon et de diplomation selon les profils ?
- Quel rôle jouent logement, ressources, bourses, travail salarié et éloignement géographique ?
- Les filières et diplômes conduisent-ils à des débouchés comparables ?

### Comparaisons
- Comment la France se situe-t-elle par rapport aux pays de l'UE et de l'OCDE ?
- Quels systèmes réduisent mieux la dépendance des parcours à l'origine sociale, et à quel coût ou avec quels arbitrages ?

## État de l'analyse quantitative Parcoursup 2025

Le protocole descriptif et son script reproductible sont désormais intégrés au dépôt :
- [Protocole d'analyse Parcoursup 2025](../research/analysis/parcoursup-2025-protocol.md)
- [Script Python](../scripts/analysis/analyze_parcoursup_2025.py)
- [Protocole d'audit documentaire des rapports CEV 2026](../research/analysis/parcoursup-cev-2026-protocol.md)

Les tests unitaires couvrent les dénominateurs nuls, les valeurs manquantes, les quantiles, l'agrégation au niveau formation et le rejet d'une session incorrecte. La CI GitHub a d'abord révélé une incohérence entre les noms de colonnes des tests (anciens noms avec majuscules) et ceux du script/API (snake_case minuscules). Les tests ont été corrigés pour utiliser les noms canoniques. Sur le commit `a2de052`, les validations des registres et identifiants, les 11 tests unitaires et les schémas JSON passent. Le CSV complet n'a toutefois pas encore été téléchargé ni exécuté dans l'environnement de recherche ; aucun résultat empirique n'est donc présenté.

## Pistes d'amélioration du dispositif de recherche

1. **Construire un corpus des rapports CEV 2026** : collecter un échantillon stratifié par filière, sélectivité, territoire et statut public/privé ; coder les critères, pondérations explicites, attendus et informations manquantes.
2. **Relier les niveaux de la chaîne éducative** : établir une matrice des données disponibles de la petite enfance à la diplomation, en documentant les ruptures de cohortes et les changements de définition.
3. **Renforcer la mesure de l'équité** : distinguer accès à toute formation, accès aux formations demandées, adéquation des vœux, mobilité, inscription et réussite ; ventiler par origine sociale lorsque les données le permettent.
4. **Ajouter une revue des travaux indépendants** : recherches évaluées par les pairs, travaux de chercheurs et évaluations contradictoires des politiques d'orientation et d'admission.
5. **Séparer descriptif et causal** : réserver les conclusions causales aux dispositifs de données et méthodes adaptés (cohortes, quasi-expériences, discontinuités, appariements), après vérification des hypothèses d'identification.
6. **Documenter les mécanismes de compensation** : quotas boursiers, priorités légales, accompagnement, CAES et aides matérielles ; examiner leur mise en œuvre et leurs effets plutôt que présumer leur efficacité.

Ces pistes sont des améliorations du programme de recherche, pas des recommandations de politique publique déjà démontrées.

## Programme de recherche
1. Audit des données Parcoursup 2026 : télécharger les fichiers ouverts, reconstruire les dénominateurs et identifier les croisements disponibles.
2. Revue des mécanismes d'admission : commissions d'examen des vœux, algorithmes locaux, quotas, transparence et contrôle.
3. Inégalités en amont : exploiter DEPP, Insee, PISA et données territoriales.
4. Trajectoires post-admission : mobiliser SIES et données de suivi des cohortes.
5. Comparaison européenne : indicateurs harmonisés Eurostat, OCDE et Commission européenne.
6. Synthèse contradictoire : effets positifs, limites, coûts, arbitrages et propositions évaluées.

## Garde-fous méthodologiques
- Ne pas attribuer à Parcoursup toutes les inégalités du système éducatif.
- Ne pas prendre un taux de proposition pour une mesure d'égalité des chances.
- Distinguer égalité formelle de procédure, égalité d'accès, égalité de traitement, égalité des chances et égalité des résultats.
- Ne pas confondre corrélation, mécanisme plausible et effet causal.
- Comparer uniquement des populations, périodes, unités et définitions compatibles.
- Conserver les résultats contradictoires et documenter les limites des sources institutionnelles comme des sources privées ou militantes.

## Registre de preuve
Les sources, études, jeux de données, affirmations et hypothèses associés sont indexés dans les registres du dépôt. La page thématique [Éducation](../knowledge/domains/education.md) rassemble la carte des connaissances, les principaux manques et les priorités d’amélioration. Les statuts `screened` et `under_review` indiquent un examen initial, pas une validation méthodologique finale.
