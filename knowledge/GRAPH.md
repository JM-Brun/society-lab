# Graphe de connaissances

## Rôle
Le graphe relie les objets du dépôt sans remplacer leurs fiches descriptives. Les fichiers YAML/JSON restent la source de vérité ; le graphe est une vue dérivée, reconstruisible.

## Nœuds
Chaque nœud possède un identifiant stable et un type : DOMAIN, CONCEPT, MECHANISM, ORG, SOURCE, STUDY, DATASET, CLAIM, HYPOTHESIS, ANALYSIS, METHOD, DOSSIER ou TERRITORY. Un identifiant ne change pas lorsque le titre, le statut ou le chemin évolue.

## Arêtes
Les relations sont orientées, typées et documentées dans [RELATION_TYPES.yml](RELATION_TYPES.yml). Une relation peut porter des métadonnées (date d'observation, justification, portée, confiance, source justificative). Ne pas créer une arête seulement parce que deux objets partagent un tag.

## Justification des relations probantes

Pour chaque arête `REL-SUPPORTS`, la justification doit permettre à un lecteur de comprendre le lien sans devoir deviner l'intention de l'auteur. Elle précise au minimum :

1. la source, le tableau, la section ou le résultat exact qui soutient l'affirmation ;
2. la population, la période, le territoire et le dénominateur concernés ;
3. le type de soutien (constat directement rapporté, résultat secondairement repris, ou rapprochement interprétatif) ;
4. la principale limite qui restreint la portée de l'affirmation.

Une relation documentaire n'est pas une validation indépendante. Tant que l'étude ou l'affirmation est au statut `screened` ou `under_review`, la justification doit conserver ce statut et les vérifications restantes. Ne pas employer « prouve », « démontre » ou une formulation causale lorsque la source ne permet qu'un constat descriptif.

Distinguer les relations épistémiques (`REL-SUPPORTS`, `REL-CONTRADICTS`, `REL-QUALIFIES`) des relations d'organisation (`REL-ABOUT`, `REL-INCLUDES`). Une relation d'inclusion indique qu'un dossier ou domaine rassemble un objet ; elle ne constitue pas une preuve en faveur de son contenu.

Éviter les justifications temporaires telles que « relation initiale issue de l'inventaire documentaire ». Si le lien ne peut pas encore être motivé à partir des fiches disponibles, différer l'arête ou la qualifier explicitement comme à revoir plutôt que lui donner une apparence de validation.

## Principes
- Une relation épistémique (étaye, contredit, nuance) doit être justifiée par une référence et une portée.
- « Étaye » ne signifie pas « prouve » ; l'intensité et les limites sont dans la justification.
- Distinguer lien bibliographique, lien thématique, dépendance logique et relation probante.
- Les relations contradictoires sont conservées ; elles ne sont pas écrasées par une synthèse.
- Pas de score de confiance automatique agrégé présenté comme vérité.
- Les relations inverses sont calculables et ne doivent pas être saisies en double.

## Représentation
Les relations seront stockées dans des fichiers de registre dédiés au format YAML, puis exportées vers GraphML/JSON-LD si un besoin de visualisation ou d'interopérabilité le justifie. Ne pas introduire Neo4j ou une base externe avant que le volume et les requêtes ne le nécessitent.

## Exemple conceptuel
```text
SOURCE-EUROSTAT-LABOUR -> REL-PUBLISHED-BY -> ORG-EUROSTAT
STUDY-EMPLOYMENT-POLARISATION -> REL-USES -> DATASET-EU-LFS
STUDY-EMPLOYMENT-POLARISATION -> REL-SUPPORTS -> CLAIM-JOB-POLARISATION
CLAIM-JOB-POLARISATION -> REL-ABOUT -> CONCEPT-LABOUR-MARKET
DOSSIER-FUTURE-OF-WORK -> REL-INCLUDES -> CLAIM-JOB-POLARISATION
```

Les identifiants ci-dessus illustrent une forme, ils ne déclarent pas l'existence de ces objets.


## Territoires et relations entre échelles

Les territoires sont des entités référentielles décrites dans [TERRITORIES.yml](TERRITORIES.yml). Ils ne sont ni des domaines thématiques ni des organisations. Les objets de recherche peuvent concerner plusieurs territoires ; leurs fiches doivent conserver les périmètres exacts plutôt que d'inférer une localisation à partir d'un tag.

La hiérarchie géographique ne suffit pas à représenter les interdépendances. Les relations entre échelles (transmission d'une politique, flux économiques, dépendance énergétique, diffusion d'une innovation, externalité environnementale, comparaison, coopération ou rétroaction) doivent être décrites séparément, avec direction, mécanisme, période, preuve et limites. Une relation contextuelle n'est pas automatiquement une relation causale.
