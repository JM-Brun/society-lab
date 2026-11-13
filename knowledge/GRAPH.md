# Graphe de connaissances

## Rôle
Le graphe relie les objets du dépôt sans remplacer leurs fiches descriptives. Les fichiers YAML/JSON restent la source de vérité ; le graphe est une vue dérivée, reconstruisible.

## Nœuds
Chaque nœud possède un identifiant stable et un type : DOMAIN, CONCEPT, MECHANISM, ORG, SOURCE, STUDY, DATASET, CLAIM, HYPOTHESIS, ANALYSIS, METHOD, DOSSIER ou TERRITORY. Un identifiant ne change pas lorsque le titre, le statut ou le chemin évolue.

## Arêtes
Les relations sont orientées, typées et documentées dans [RELATION_TYPES.yml](RELATION_TYPES.yml). Une relation peut porter des métadonnées (date d'observation, justification, portée, confiance, source justificative). Ne pas créer une arête seulement parce que deux objets partagent un tag.

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
