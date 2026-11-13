# Architecture de Society Lab

## Objectif
Séparer les sources, les objets de connaissance, les travaux d'analyse et les publications. Le dépôt Git est la source de vérité ; le site Quarto est une vue éditoriale construite à partir des contenus sélectionnés.

## Couches logiques
1. **Evidence** : documents, publications, données et métadonnées de provenance.
2. **Knowledge & research** : concepts, institutions, mécanismes, études, affirmations, hypothèses, débats et analyses.
3. **Knowledge graph** : relations typées entre objets, stockées en YAML et exportables vers des formats interopérables.
4. **Publication** : dossiers et pages éditorialisées, compréhensibles indépendamment et reliés aux sources.

## Organisation du dépôt
- `knowledge/` : taxonomie, tags, types de relations, graphe, concepts, institutions et mécanismes.
- `sources/` : registre, fiches et manifestes d'ingestion.
- `research/studies/` et `research/datasets/` : études et jeux de données.
- `claims/`, `hypotheses/`, `debates/` : propositions examinées et controverses.
- `analysis/` : analyses quantitatives, qualitatives et reproductibles.
- `dossiers/` : synthèses éditoriales transversales.
- `schemas/` : contrats de données.
- `scripts/` et `tests/` : validation et automatisation.
- `site/` : publication Quarto.

## Objets fondamentaux
Source, Study, Dataset, Claim, Hypothesis, Concept, Institution, Mechanism, Debate, Analysis, Method et Dossier. Chaque objet possède une fiche structurée, un identifiant stable et des métadonnées adaptées à sa nature.

## Identifiants et vocabulaire
Les identifiants sont sémantiques, stables, uniques et indépendants du chemin. Voir [métadonnées et nomenclature](metadata-and-naming.md). Les domaines sont définis dans `knowledge/TAXONOMY.yml`, les tags transversaux dans `knowledge/TAGS.yml`. Les mots-clés libres ne doivent pas remplacer les vocabulaires contrôlés.

## Graphe
Les nœuds sont les objets identifiés. Les arêtes sont des relations orientées et typées, définies dans `knowledge/RELATION_TYPES.yml` et instanciées dans `knowledge/graph.yml`. Les relations probantes doivent être justifiées ; les relations inverses sont calculées. Le graphe est une vue dérivée des fiches, pas une base séparée ni une preuve autonome. Voir [principes du graphe](../knowledge/GRAPH.md).

## Données et reproductibilité
Conserver les données brutes uniquement lorsque leur licence, taille et conditions le permettent. Sinon, préférer métadonnées, scripts de téléchargement et instructions de reproduction. Documenter provenance, date d'extraction, transformations, unités et limites. Aucun secret ni donnée personnelle inutile dans Git.

## Ingestion
Toute source suit un pipeline documenté : découverte, déduplication, identification, vérification des droits, qualification, extraction, mise en relation, revue et maintenance. Voir [protocole d'ingestion](ingestion-protocol.md).

## Publication Quarto
Le site est une projection éditoriale, pas une seconde source de vérité. La construction et le déploiement doivent échouer si les contrôles bloquants échouent.


## Intégration avec les autres dépôts

Society Lab conserve la propriété canonique de ses objets de recherche, de ses analyses et de ses conclusions. Les autres projets peuvent apporter des concepts, méthodes ou artefacts, mais aucune proximité thématique ne vaut intégration ni équivalence sémantique. Les graphes et identifiants restent propres à chaque dépôt ; les correspondances utiles sont explicites, qualifiées et révisées.

Les dépôts publics doivent rester autonomes vis-à-vis des espaces privés : aucune dépendance de build, de CI ou de lecture ne doit nécessiter un accès privé. Aucun transfert automatique n'est présumé. Toute publication d'un dossier dans un portfolio exige une revue distincte des preuves, de la reproductibilité, des droits et des limites. Voir le [contrat d'intégration inter-dépôts](cross-repository-contract.md).

## Automatisation
Contrôles prévus : validation YAML/JSON et schémas, unicité des identifiants, références internes, types de relations, tests d'analyse et construction Quarto. Ces contrôles ne certifient pas la qualité scientifique.
