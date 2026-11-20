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
- `forecasts/` : prévisions probabilistes datées, règles de résolution et historique des résultats.
- `dossiers/` : dossiers détaillés transversaux.
- `syntheses/` : synthèses de référence et registre dossier–synthèse.
- `schemas/` : contrats de données.
- `scripts/` et `tests/` : validation et automatisation.
- `site/` : publication Quarto.

## Objets fondamentaux
Source, Study, Dataset, Claim, Hypothesis, Forecast, Concept, Institution, Mechanism, Debate, Analysis, Method, Dossier et Territory. Chaque objet possède une fiche structurée, un identifiant stable et des métadonnées adaptées à sa nature.

## Identifiants et vocabulaire
Les identifiants sont sémantiques, stables, uniques et indépendants du chemin. Voir [métadonnées et nomenclature](metadata-and-naming.md). Les domaines sont définis dans `knowledge/TAXONOMY.yml`, les tags transversaux dans `knowledge/TAGS.yml`. Les mots-clés libres ne doivent pas remplacer les vocabulaires contrôlés.

## Graphe
Les nœuds sont les objets identifiés. Les arêtes sont des relations orientées et typées, définies dans `knowledge/RELATION_TYPES.yml` et instanciées dans `knowledge/graph.yml`. Les relations probantes doivent être justifiées ; les relations inverses sont calculées. Le graphe est une vue dérivée des fiches, pas une base séparée ni une preuve autonome. Voir [principes du graphe](../knowledge/GRAPH.md).

## Données et reproductibilité
Conserver les données brutes uniquement lorsque leur licence, taille et conditions le permettent. Sinon, préférer métadonnées, scripts de téléchargement et instructions de reproduction. Documenter provenance, date d'extraction, transformations, unités et limites. Aucun secret ni donnée personnelle inutile dans Git.

## Ingestion
Toute source suit un pipeline documenté : découverte, déduplication, identification, vérification des droits, qualification, extraction, mise en relation, revue et maintenance. Voir [protocole d'ingestion](ingestion-protocol.md).

## Publication Quarto
Le projet Quarto est isolé dans `site/`, comme dans LLM Lab et J-DriftX. Le manifeste `site/_quarto.yml` liste explicitement l’accueil et les synthèses à rendre. Le site public est produit dans `site/_site/`. Les dossiers, notes d’investigation, ingestions, analyses, jeux de données et registres se consultent dans le dépôt Git public.

Les versions de lecture dans `site/syntheses/` reprennent les synthèses de référence dans `syntheses/`, avec les mêmes noms de fichiers, un format court, leurs références externes et leurs limites. Lorsqu’un résultat de référence change, vérifier aussi la version de lecture concernée. Les pilotes affichent leur statut provisoire et la portée du niveau de confiance.

Pour publier une nouvelle synthèse, préparer la page de lecture, l’ajouter à `project.render` et à l’accueil, puis vérifier le rendu et ses liens. La CI de publication exécute ces deux commandes et envoie uniquement `site/_site/` à GitHub Pages après validation sur `main`.

```sh
quarto render site
python scripts/validate/validate_public_site.py
```

La vérification Python nécessite PyYAML. Le mode de publication du dépôt se règle dans **Settings → Pages → Build and deployment → Source → GitHub Actions**.

## Intégration avec les autres dépôts

Society Lab conserve la propriété canonique de ses objets de recherche, de ses analyses et de ses conclusions. Les autres projets peuvent apporter des concepts, méthodes ou artefacts, mais aucune proximité thématique ne vaut intégration ni équivalence sémantique. Les graphes et identifiants restent propres à chaque dépôt ; les correspondances utiles sont explicites, qualifiées et révisées.

Les dépôts publics doivent rester autonomes vis-à-vis des espaces privés : aucune dépendance de build, de CI ou de lecture ne doit nécessiter un accès privé. Aucun transfert automatique n'est présumé. Toute publication d'un dossier dans un portfolio exige une revue distincte des preuves, de la reproductibilité, des droits et des limites. Voir le [contrat d'intégration inter-dépôts](cross-repository-contract.md).

## Automatisation
Contrôles prévus : validation YAML/JSON et schémas, unicité des identifiants, références internes, types de relations, tests d'analyse et construction Quarto. Ces contrôles ne certifient pas la qualité scientifique.

## Analyse territoriale multiscalaire

Le périmètre territorial est défini dans [knowledge/TERRITORIES.yml](../knowledge/TERRITORIES.yml) et ses principes d'utilisation dans [multiscalar-analysis.md](multiscalar-analysis.md). Les territoires constituent des objets de connaissance référentiels, distincts des domaines thématiques et des organisations.

Une fiche de recherche peut concerner plusieurs territoires et plusieurs échelles. Il faut distinguer le lieu où un phénomène est observé, le territoire de compétence de l'acteur public, l'aire fonctionnelle affectée et le périmètre des données. Les relations d'influence, de dépendance ou de comparaison ne se déduisent jamais d'une simple proximité géographique.

L'approche doit permettre la contextualisation descendante (global vers local), ascendante (local vers global) et latérale (territoires reliés par des flux, réseaux, coopérations ou comparaisons). Les liens causaux restent des hypothèses à documenter, pas des propriétés automatiques de l'arborescence territoriale.
