# Décomposer les revalorisations du SMIC : règles, indexation et coups de pouce (1970–2026)

- **Identifiant :** DOSSIER-SMIC-INDEXATION-DECOMPOSITION
- **Statut :** dossier de méthode en construction ; transcription historique disponible pour 1970–1993
- **Date de revue :** 14 novembre 2026
- **Périmètre :** France hors Mayotte ; règles légales et épisodes de revalorisation de 1970 à 2026
- **Question :** quelle part des hausses du SMIC relève de l'indexation automatique, de la participation à la progression salariale, des coups de pouce discrétionnaires et des transitions institutionnelles ?

> **Précaution centrale.** Il faut distinguer le taux de revalorisation observé, les composantes prévues par les règles applicables à la date considérée et la hausse réelle du pouvoir d'achat. Une décomposition comptable ou réglementaire n'est pas, à elle seule, une évaluation des effets sur l'emploi, les revenus disponibles ou les prix.

## 1. Objet et résultats attendus

Ce dossier fournit la base méthodologique pour lire l'historique des revalorisations. Il doit permettre de répondre à quatre questions distinctes :

1. Quelles règles juridiques s'appliquaient à chaque période ?
2. Quelle part de la hausse observée correspondait aux obligations automatiques ?
3. Quelle part résultait de décisions discrétionnaires (« coups de pouce ») ou de changements de calendrier ?
4. Comment comparer ces épisodes sans confondre hausse nominale, hausse réelle et amélioration du revenu disponible ?

Le résultat attendu est une chronologie documentée, un tableau de décomposition reproductible et un registre des divergences entre sources.

## 2. Cadre de lecture

Pour chaque épisode, conserver séparément :

- **Date d'effet** et éventuelles dates multiples au cours de l'année ;
- **Hausse nominale observée** du taux horaire ;
- **Composante prix** calculée selon l'indice et la fenêtre légale de la période ;
- **Composante salariale** prévue par le mécanisme applicable, lorsqu'elle existe ;
- **Obligation légale** totale, en explicitant la formule et les arrondis ;
- **Coup de pouce discrétionnaire**, calculé comme résidu seulement si les composantes sont comparables ;
- **Hausse réelle** après inflation, calculée sur une fenêtre cohérente ;
- **Contexte institutionnel** : GMR, convergence, changement de calendrier, revalorisations multiples.

Ne pas supposer que les composantes sont toujours additives en pourcentage. Lorsque les règles sont multiplicatives ou s'appliquent à des bases successives, expliciter la convention de calcul. Ne pas traiter le résidu comme un coup de pouce certain si les indices, périodes de référence ou conventions diffèrent.

## 3. Repères institutionnels à documenter

### 1970 : passage du SMIG au SMIC

Le SMIC remplace le SMIG en 1970. La reconstitution doit préciser les règles initiales d'indexation sur les prix et de participation à la progression du pouvoir d'achat du salaire horaire de base ouvrier. Les premières années nécessitent une attention particulière aux dates d'effet et aux conventions des séries historiques.

### 1981 et les années suivantes

La période comprend des hausses nominales importantes et des épisodes de coups de pouce. Il faut rapprocher les séries de revalorisation des rapports d'experts, des indices de prix et des salaires de référence. Les conséquences sur l'emploi relèvent d'un autre niveau d'analyse : elles ne se déduisent pas de la décomposition de la hausse.

### 2003–2005 : convergence des garanties mensuelles de rémunération

La réduction progressive de la durée légale du travail a conduit à plusieurs garanties mensuelles de rémunération et à un processus de convergence des minima. Il faut distinguer la revalorisation du taux horaire, la garantie mensuelle et les effets de convergence ; les séries ne sont pas directement comparables sans conversion.

### 2008 : changement du calendrier de revalorisation

Le calendrier légal a été modifié, avec une date de revalorisation de référence au 1er janvier à partir de 2010, et une possibilité de revalorisation en cours d'année en cas d'inflation. La chronologie doit distinguer la date de décision, la date d'effet et la période d'indice utilisée.

### 2021–2026 : inflation et revalorisations infra-annuelles

Les revalorisations automatiques en cours d'année doivent être isolées des éventuels coups de pouce. Il faut comparer l'indice de référence effectivement retenu par la loi, la hausse nominale à date d'effet et l'inflation cumulée sur l'année civile. Une comparaison avec les minima conventionnels doit intégrer les délais de négociation et les dates de mise à jour des branches.

## 4. Première base quantitative : 1970–1993

Le fichier [data/smic-revaluations-1970-1993.csv](../data/smic-revaluations-1970-1993.csv) transcrit le tableau 3 du rapport du Sénat 1993–1994. Il contient, par période annuelle :

- le taux horaire en francs courants ;
- la variation observée ;
- les composantes prix et salariale ;
- l'obligation légale ;
- le résidu présenté comme coup de pouce discrétionnaire ;
- la source, la méthode, un niveau de confiance et des notes.

La source est référencée comme `SOURCE-SENAT-1994-SMIC-DECOMPOSITION`, et le jeu de données comme `DATASET-SMIC-REVALUATIONS-1970-1993`.

**Limites à respecter :**

- les glissements annuels à date donnée ne sont pas des moyennes annuelles ;
- les francs courants ne mesurent pas le pouvoir d'achat ;
- les composantes doivent être contrôlées avec la définition des indices et la fenêtre de référence ;
- des divergences existent avec des publications ultérieures, notamment sur certains épisodes comme 1973 et 1981 ;
- le résidu ne doit pas être interprété comme une décision discrétionnaire certaine avant réconciliation des conventions.

## 5. Protocole de calcul reproductible

Pour chaque période :

1. relever la valeur du SMIC immédiatement avant et après la date d'effet ;
2. recalculer la hausse nominale à partir des valeurs non arrondies lorsque disponibles ;
3. identifier le texte légal applicable et la formule exacte ;
4. relever l'indice des prix, sa population de référence, sa fenêtre et sa valeur de départ ;
5. relever l'indicateur salarial et son champ, s'il entre dans la formule ;
6. recalculer l'obligation automatique en conservant les unités et conventions ;
7. comparer l'obligation au taux observé et qualifier le résidu ;
8. convertir les valeurs en euros constants pour une série de pouvoir d'achat, avec une année de base explicitée ;
9. comparer les résultats aux rapports d'experts et aux séries INSEE ;
10. consigner les écarts, les arbitrages méthodologiques et le niveau de confiance.

Un second calcul doit être produit en moyenne annuelle afin de ne pas confondre glissements à date donnée et évolution moyenne du salaire minimum sur l'année.

## 6. Sources à mobiliser

- **Sénat, rapport 1993–1994**, tableau 3 : source de la transcription 1970–1993, référencée dans le registre des sources.
- **Groupe d'experts sur le SMIC**, rapports annuels et rapports historiques : contrôle des règles, des séries et des divergences de calcul.
- **INSEE**, séries longues du SMIC, des prix et des salaires : reconstitution en euros constants et contrôle indépendant.
- **Légifrance**, textes successifs : vérification de la règle juridique applicable et des dates d'effet.
- **DARES** : effets de diffusion, minima conventionnels et dynamique salariale, à traiter séparément de la décomposition légale.

Chaque chiffre final devra être relié à une source, une formule, une période et une convention de calcul.

## 7. Questions ouvertes prioritaires

1. Réconcilier les écarts entre le tableau du Sénat et les séries des rapports d'experts, en particulier pour 1973 et 1981.
2. Étendre la décomposition au-delà de 1993, puis jusqu'en 2026.
3. Documenter les textes et les formules applicables à chaque sous-période.
4. Reconstituer séparément les taux horaires, les garanties mensuelles de rémunération et la convergence 2003–2005.
5. Construire les séries en euros constants et en moyenne annuelle.
6. Contrôler les revalorisations infra-annuelles de 2021–2026 et distinguer indexation et décisions discrétionnaires.
7. Relier chaque épisode aux études d'effets sur l'emploi, les salaires et les revenus sans confondre description et causalité.

## 8. Conclusion provisoire

La décomposition historique est une étape nécessaire pour comprendre ce que les gouvernements et la loi ont effectivement ajouté au mécanisme automatique. Elle ne suffit pas à déterminer si une hausse a été bénéfique ou défavorable : cette évaluation doit être conduite par population et par indicateur, à partir des études d'impact et d'un contrefactuel explicite.

**Niveau de confiance :** modéré sur l'existence et l'intérêt de la série 1970–1993 ; limité sur la comparabilité de certaines composantes historiques tant que les divergences de méthode ne sont pas réconciliées ; faible sur toute extrapolation causale tirée de la seule décomposition.
