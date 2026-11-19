# Architecture d'un système intelligent d'exploitation des métadonnées

**Statut :** proposition d'architecture et plan d'implémentation incrémental.  
**Date :** 2026-11-19  
**Périmètre :** inventaire, requêtes, métriques, navigation pédagogique, analyse du graphe et aide à la construction du corpus.

## 1. Objectif

Faire de Society Lab un corpus interrogeable et pilotable par ses métadonnées. Le système doit répondre de façon reproductible à des questions telles que :

- Combien de parcours d'apprentissage, de leçons et de pages existent ?
- Combien de pages sont effectivement incluses dans un parcours donné ?
- Quelles pages expliquent une notion, directement ou indirectement ?
- Quelles notions sont expliquées par une page donnée ?
- Quelles pages sont reliées à une page donnée, par quel type de relation et à quelle distance ?
- Quelles notions sont présentes dans les dossiers mais absentes du parcours pédagogique ?
- Quelles pages, notions, sources ou relations sont orphelines, dupliquées, incomplètes ou à réviser ?
- Quelles actions de construction auraient le plus d'utilité pédagogique ou documentaire ?

Le but n'est pas de maximiser les nombres de pages, de notions ou d'arêtes. Il est d'améliorer la couverture, la cohérence, la navigabilité, la traçabilité et la qualité de maintenance.

Society Lab reste un projet de compilation critique des connaissances existantes : les métriques décrivent le corpus et son organisation, elles ne valident pas automatiquement la qualité scientifique des contenus.

## 2. Principes non négociables

1. **Sources de vérité uniques.** Les fiches, registres, schémas et métadonnées canoniques restent la référence. Les index, graphes calculés, rapports et tableaux de bord sont des projections générées.
2. **Pas de registre parallèle par commodité.** Avant tout nouveau champ ou type, inventorier les structures existantes, leurs consommateurs, les schémas, les validateurs et les données historiques.
3. **Séparer structure pédagogique et graphe scientifique.** « Une leçon contient une page » n'a pas le même sens que « une étude étaye une affirmation ».
4. **Relations typées et interprétables.** Une proximité de tags, un titre ressemblant ou une cooccurrence ne créent pas une relation.
5. **Comptages auditables.** Chaque mesure expose définition, périmètre, exclusions, objets comptés et éventuelles ambiguïtés.
6. **Inconnu n'est pas zéro.** Une métadonnée absente, un lien non détecté ou un type inconnu sont signalés comme tels.
7. **Pas de score global opaque.** Présenter des dimensions et diagnostics séparés, avec leurs limites.
8. **Lecture seule par défaut.** Les recommandations ne modifient pas automatiquement les fiches, les relations, les tags ou les parcours.
9. **Calcul local et reproductible.** Commencer par Python et les formats déjà utilisés ; éviter une base externe ou un moteur distribué sans besoin mesuré.
10. **Compatibilité progressive.** Toute évolution de contrat doit être précédée d'un inventaire des usages réels et de tests de compatibilité historique.

## 3. Architecture logique

### 3.1 Sources canoniques

- Taxonomie et tags : `knowledge/TAXONOMY.yml`, `knowledge/TAGS.yml`.
- Relations : `knowledge/RELATION_TYPES.yml` et `knowledge/graph.yml`.
- Fiches et registres : les neuf registres canoniques déjà couverts par le validateur.
- Synthèses : `syntheses/registry.yml`.
- Contrats : schémas JSON et validateurs existants.
- Pages pédagogiques et parcours : structures Understand / Build et métadonnées réellement présentes, à inventorier avant de figer leur modèle.
- Gouvernance : mappings d'issues et labels GitHub, utilisés pour le pilotage du travail et non comme substituts aux métadonnées scientifiques.

### 3.2 Pipeline de lecture

```text
Fichiers et registres canoniques
        |
        v
Inventaire déterministe et validation des références
        |
        v
Modèle de lecture normalisé (en mémoire)
        |
        +--> Index par identifiant, type, domaine, tag et chemin
        |
        +--> Index de relations entrantes / sortantes
        |
        +--> Index de structure pédagogique (après inventaire)
        |
        v
API de requêtes et calculs de métriques
        |
        +--> CLI et sorties JSON
        +--> Rapports Markdown
        +--> Pages / tableaux de bord Quarto
        +--> Diagnostics et recommandations explicables
```

Le modèle de lecture est reconstruit à partir des sources à chaque exécution ou depuis un cache explicitement invalidable. Il ne devient pas une deuxième source de vérité.

### 3.3 Séparation des espaces de relations

Le système doit maintenir des espaces logiques distincts, même si certains sont projetés dans un graphe commun :

- **Pédagogique / éditorial :** parcours → leçons → pages ; ordre, prérequis, regroupement.
- **Conceptuel :** page → notion ; notion → notion ; notion → domaine.
- **Documentaire :** dossier → synthèse ; page → dossier ; page → source.
- **Épistémique :** étude → claim ; source → étude ; relation qui étaye, contredit ou nuance.
- **Provenance :** objet → source d'origine, localisateur, version ou transformation.

Ne pas réutiliser abusivement `REL-INCLUDES` pour coder toutes ces significations. Les relations pédagogiques ne doivent pas être introduites dans `RELATION_TYPES.yml` avant d'avoir vérifié si le parcours est déjà représenté par des fichiers de navigation, des métadonnées Quarto ou un autre mécanisme dédié.

## 4. Modèle de lecture conceptuel

Les types ci-dessous décrivent le modèle d'interrogation cible ; ils ne constituent pas une décision d'ajout immédiat de nouveaux types canoniques.

| Objet de lecture | Identité | Propriétés utiles |
|---|---|---|
| Page | chemin canonique ou ID existant | titre, langue, statut, type, domaines, tags |
| Parcours | identifiant ou fichier de parcours existant | titre, public, niveau, ordre |
| Leçon | identifiant ou section existante | parcours, ordre, objectifs, prérequis |
| Notion | ID `CONCEPT-*` | libellé, définition, domaines, tags |
| Dossier | ID `DOSSIER-*` | statut, domaines, synthèse |
| Synthèse | ID / chemin du registre | date, statut, dossier(s) associé(s) |
| Relation | identifiant ou clé stable dérivée | type, source, cible, justification, provenance |

Chaque objet doit conserver son identifiant canonique et son chemin d'origine. Si une page n'a pas d'identifiant stable, ne pas en fabriquer en masse : étudier d'abord les conventions existantes et les conséquences sur les liens.

### 4.1 Relations pédagogiques minimales à reconnaître

- parcours **contient** leçon ;
- leçon **ordonne / référence** page ;
- page **explique** notion ;
- page **prérequis de** page, si cette relation est explicitement documentée ;
- page **complète / approfondit** page, si cette relation est explicitement documentée ;
- page **renvoie vers** page, issue d'un lien réel et conservant son contexte.

Ces relations ont des portées différentes. Un lien Markdown est un lien de navigation, pas nécessairement une relation pédagogique. Une notion mentionnée dans un texte n'est pas automatiquement une notion enseignée par cette page.

## 5. Catalogue de requêtes et métriques

Chaque métrique doit avoir une définition versionnée, un périmètre explicite et une sortie permettant de remonter aux objets comptés.

### 5.1 Inventaire global

| Question | Mesure | Définition à appliquer |
|---|---|---|
| Combien de pages ? | `pages.total` | Pages du périmètre retenu, dédupliquées par identité canonique |
| Combien de parcours ? | `learning_paths.total` | Parcours reconnus par le mécanisme réel du dépôt |
| Combien de leçons ? | `lessons.total` | Unités de leçon identifiées, sans compter les titres de section arbitraires |
| Combien de notions ? | `concepts.total` | Concepts canoniques distincts du registre |
| Combien de pages pédagogiques ? | `pages.in_learning_paths` | Pages distinctes référencées par au moins un parcours |
| Combien de pages non intégrées ? | `pages.not_in_learning_paths` | Pages éligibles absentes de tout parcours ; exclure explicitement les pages techniques et administratives |
| Combien de ressources de révision ? | `revision_resources.total` | Fiches, flashcards ou résumés reconnus par une association explicite à une page |\n| Combien de pages avec fiche de révision ? | `pages.with_revision_resource` | Pages éligibles associées à au moins une ressource de révision |\n| Combien de notions enseignées ? | `concepts.taught` | Concepts reliés par une relation pédagogique explicite à au moins une page |
| Combien de notions sans page ? | `concepts.without_teaching_page` | Concepts canoniques sans relation pédagogique reconnue |

Ne jamais présenter le nombre total de fichiers Markdown comme le nombre de pages pédagogiques.

### 5.2 Requêtes ciblées

| Requête | Résultat attendu |
|---|---|
| Pages d'un parcours | Pages ordonnées, leçons, chemin, statut des références |
| Notions d'une page | Concepts explicitement enseignés, mentionnés ou liés, catégories distinguées |
| Pages d'une notion | Pages qui l'expliquent ; éventuellement pages qui la mentionnent dans une vue séparée |
| Pages liées à une page | Liens entrants et sortants, type, contexte et profondeur |
| Parcours d'une page | Tous les parcours et leçons où elle apparaît |
| Dossiers liés à une notion | Dossiers reliés directement ou par chemin explicable dans le graphe |
| Notions voisines | Concepts reliés par une relation typée, sans confondre proximité et équivalence |
| Sources d'une page | Sources et études avec provenance et localisateurs disponibles |

Une requête de voisinage doit toujours préciser la profondeur et les types de relations suivis. Les chemins transitifs ne doivent pas être présentés comme des relations directes.

### 5.3 Définitions de comptage importantes

- **Page liée à une notion :** compter une page une seule fois par notion, même si plusieurs liens ou occurrences existent.
- **Page liée à une page :** distinguer liens entrants, sortants et relations sémantiques ; exclure les ancres internes et les liens externes du comptage des pages internes.
- **Nombre de pages d'un parcours :** compter les pages distinctes ; publier séparément le nombre d'occurrences si une page apparaît plusieurs fois.
- **Nombre de leçons :** compter les unités reconnues par le modèle réel, pas chaque titre Markdown.
- **Nombre de notions :** distinguer concepts canoniques, synonymes/libellés et mentions textuelles.
- **Relations directes / indirectes :** ne jamais mélanger les deux dans un même chiffre sans ventilation.
- **Pages éligibles :** publier les règles d'inclusion et les exclusions (README, index, templates, notes techniques, archives, etc.).

### 5.4 Exemple de contrat de sortie

```json
{
  "metric": "pages_for_concept",
  "definition_version": 1,
  "scope": "pedagogical_pages",
  "query": {"concept_id": "CONCEPT-EXAMPLE"},
  "count": 0,
  "items": [],
  "excluded": [],
  "unknown": [],
  "generated_at": "2026-11-19T00:00:00Z",
  "source_revision": "<git-commit-sha>"
}
```

Cet exemple est schématique : l'identifiant est fictif et les valeurs nulles ne constituent pas une mesure du dépôt.

## 6. API Python et interface CLI proposées

Créer une bibliothèque réutilisable, indépendante de Quarto et de GitHub Actions. Les noms ci-dessous sont des propositions à adapter à l'organisation réelle des scripts existants après inventaire.

API conceptuelle :

```python
catalog = ProjectCatalog.load(root=".")

catalog.count_pages(scope="pedagogical")
catalog.count_learning_paths()
catalog.count_lessons()
catalog.count_concepts()

catalog.pages_for_concept("CONCEPT-...")
catalog.concepts_for_page("path/to/page.qmd")
catalog.pages_in_learning_path("PATH-...")
catalog.pages_linked_to_page("path/to/page.qmd", direction="both")
catalog.neighbors("CONCEPT-...", relation_types=[...], max_depth=2)

catalog.coverage_report()
catalog.orphan_report()
catalog.recommendations()
```

CLI conceptuelle :

```bash
python -m scripts.metadata inventory
python -m scripts.metadata metrics
python -m scripts.metadata query pages-for-concept CONCEPT-...
python -m scripts.metadata query concepts-for-page path/to/page.qmd
python -m scripts.metadata query path-pages PATH-...
python -m scripts.metadata query neighbors PAGE-... --depth 2
python -m scripts.metadata report coverage --format markdown
python -m scripts.metadata report coverage --format json
python -m scripts.metadata recommendations --format markdown
```

Les commandes sont des exemples d'interface cible, pas des commandes actuellement disponibles. Avant de les créer, rechercher les scripts, fonctions et commandes existants pour réutiliser ou étendre leurs capacités sans doublon.

## 7. Exploitation combinée des métadonnées

Les sources de classement ont des rôles distincts :

- **Domaine :** sujet principal ou rattachement scientifique stable ; taxonomie canonique.
- **Tag :** angle transversal contrôlé (méthode, niveau, horizon, statut, etc.) ; vocabulaire canonique.
- **Graphe :** relation explicite et typée entre objets ; conserve justification et provenance.
- **Registre :** index canonique des fiches et identifiants.
- **Frontmatter / métadonnées de page :** propriétés éditoriales et pédagogiques réellement supportées par le schéma.
- **Liens Markdown / Quarto :** navigation observée, à distinguer d'une relation sémantique.
- **Labels GitHub :** pilotage des issues et du travail ; ne pas les traiter comme des tags scientifiques.
- **Historique Git :** provenance des changements et date de révision, sans assimiler un commit récent à une revue de fond.

Une même page peut donc être retrouvée par domaine, tag, notion, parcours, dossier, source ou lien. Les résultats doivent expliquer quel chemin a permis de la retrouver.

## 8. Diagnostics et recommandations intelligentes

Le système doit produire des diagnostics explicables, classés par nature, et non une note opaque.

### 8.1 Qualité de structure

- pages de parcours manquantes ou liens cassés ;
- leçons vides, sans objectif ou sans page, si ces champs sont réellement prévus ;
- pages pédagogiques sans notion associée ;
- notions sans page explicative ;
- pages très redondantes ou quasi-duplicatives à examiner ;
- pages sans lien entrant, à distinguer des pages autonomes légitimes ;
- identifiants absents, dupliqués ou non résolus ;
- références et arêtes orphelines ;
- écarts entre associations explicites des fiches et relations du graphe.

### 8.2 Couverture et progression pédagogique

- notions d'un domaine non couvertes par un parcours ;
- notions couvertes par une seule page ;
- pages de synthèse ou de révision absentes lorsqu'elles sont attendues ;\n- pages pédagogiques sans fiche de révision, résumé ou flashcard associée lorsque cette ressource est prévue ;
- pages avancées sans prérequis explicites, si la progression l'exige ;
- déséquilibre entre domaines, niveaux ou types de ressources ;
- notion centrale dans plusieurs dossiers mais absente des supports pédagogiques.

### 8.3 Recommandations d'action

Exemples de recommandations possibles :

- « Créer une fiche de révision pour la page X » si une règle éditoriale validée l'exige et si aucune fiche associée n'existe.
- « Relier la page X à la notion Y » seulement si le contenu et une revue humaine justifient le lien.
- « Examiner l'intégration de la notion Y au parcours Z » si elle est importante dans le corpus mais non enseignée.
- « Vérifier le lien X → Y » si une référence explicite est cassée ou ambiguë.
- « Fusionner ou différencier X et Y » uniquement comme suggestion de revue, jamais comme modification automatique.
- « Actualiser la synthèse X » si ses sources ou dossiers liés ont changé depuis la dernière revue documentée.

Chaque recommandation comporte : identifiants concernés, règle déclenchée, éléments de preuve, niveau d'ambiguïté, action humaine attendue et éventuelles dépendances. Aucun lien sémantique ou causal ne doit être créé automatiquement.

## 9. Scalabilité et performances

Commencer par un catalogue en mémoire construit en un passage sur les registres et un passage sur les relations.

- Index `id -> objet`, `type -> IDs`, `domain -> IDs`, `tag -> IDs`.
- Index d'adjacence `outgoing[id]` et `incoming[id]`.
- Index `concept_id -> page_ids` et `page_id -> concept_ids` si les associations sont explicites.
- Index `path_id -> ordered page occurrences` et `page_id -> path occurrences` après identification du format réel.
- Déduplication par identité canonique, jamais par titre seul.
- Complexité cible : construction O(V + E + M), requête de voisinage O(V' + E') sur le sous-graphe parcouru, comptages indexés proches de O(1) ou O(k).
- Ne recalculer que les projections nécessaires ; conserver un mode complet pour la reproductibilité.
- Cache uniquement dérivé, invalidé par hash des entrées et version du code.

Le benchmark doit reprendre la méthode existante ×1/×10/×100, distinguer chargement, normalisation, indexation, requêtes et génération des rapports, et rester informatif tant qu'aucune enveloppe de performance n'est justifiée.

Ne pas introduire Neo4j, Elasticsearch, un service externe ou une base persistante avant d'avoir mesuré une limite réelle du modèle local.

## 10. Tests et qualité

### Tests unitaires

- déduplication des pages et concepts ;
- pages présentes plusieurs fois dans un parcours ;
- relation entrante vs sortante ;
- liens Markdown relatifs, ancres et liens externes ;
- relations directes vs transitives ;
- tags partagés sans arête sémantique ;
- identifiants absents, inconnus et dupliqués ;
- références croisées invalides ;
- objets légitimement isolés ;
- résultats déterministes et ordre stable.

### Tests d'intégration sur le dépôt

- un parcours réel Understand et un parcours réel Build ;
- une page avec plusieurs notions ;
- une notion reliée à plusieurs pages ;
- une page reliée à plusieurs pages ;
- une page présente dans plusieurs leçons ou parcours, si ce cas existe ;
- un chemin positif, un chemin négatif et un chemin ambigu dans le graphe ;
- rapprochement fiches ↔ graphe sans synchronisation automatique.

Les fixtures synthétiques complètent les tests réels mais ne les remplacent pas.

### Contrat de qualité des sorties

Chaque rapport doit inclure : version de définition, commit source, date de génération, périmètre, numérateur/dénominateur lorsque pertinent, exclusions, inconnus, liste des anomalies et avertissements méthodologiques.

## 11. Documentation et livrables

Le système doit être documenté à quatre niveaux :

1. **Architecture :** responsabilités des couches, sources de vérité, limites et décisions.
2. **Référence des métriques :** définition, formule, périmètre, exclusions, interprétation et exemples.
3. **Guide d'utilisation :** installation déjà prévue par le dépôt, commandes réelles, filtres et formats de sortie.
4. **Guide de contribution :** comment ajouter une page, une notion, un lien ou une leçon sans casser les index et projections.

Livrables progressifs :

- inventaire automatique des pages Understand et Build ;
- inventaire des parcours, leçons et notions ;
- matrice page ↔ notion et page ↔ page ;
- API Python de lecture ;
- CLI et sorties JSON/Markdown ;
- rapport de couverture et d'anomalies ;
- intégration CI non bloquante au début ;
- tableau de bord Quarto dérivé des sorties ;
- recommandations explicables, soumises à revue humaine.

## 12. Plan de réalisation par lots

### Lot 0 — Inventorier avant de concevoir les migrations

- [ ] Lister les fichiers et conventions des parcours Understand et Build.
- [ ] Identifier les formats de leçons, navigation, pages et métadonnées.
- [ ] Inventorier les scripts, modules, tests et workflows déjà capables de compter, parser, indexer ou parcourir les graphes.
- [ ] Recenser les champs de métadonnées réellement utilisés et leur couverture.
- [ ] Cartographier les liens page–notion et page–page existants, avec cas ambigus.
- [ ] Identifier les consommateurs et les contraintes de compatibilité.

**Sortie :** inventaire reproductible, matrice fichiers → métadonnées → schémas → scripts → tests → workflows. Aucun nouveau contrat n'est imposé à ce stade.

### Lot 1 — Photographie et métriques de base

- [ ] Produire les comptages pages, parcours, leçons, notions et synthèses selon des périmètres vérifiés.
- [ ] Produire les listes des objets inclus, exclus et non classés.
- [ ] Calculer les pages par parcours et les pages par notion.
- [ ] Calculer les liens entrants/sortants par page.\n- [ ] Inventorier les ressources de révision (fiches, flashcards, résumés) et leur association aux pages.
- [ ] Comparer les résultats aux outils existants et expliquer les écarts.

**Sortie :** rapport JSON et Markdown reproductible, sans modification des sources.

### Lot 2 — Bibliothèque de requêtes

- [ ] Construire ou étendre le catalogue en mémoire.
- [ ] Ajouter les index inverses.
- [ ] Implémenter les requêtes ciblées et les tests réels.
- [ ] Documenter les types de liens et la transitivité.

**Sortie :** API Python stable et CLI minimale.

### Lot 3 — Diagnostics et couverture

- [ ] Définir les règles d'éligibilité par type d'objet.
- [ ] Distinguer anomalies certaines, alertes et cas ambigus.
- [ ] Produire les rapports de couverture pédagogique et documentaire.
- [ ] Articuler les KPIs existants sans créer de second calculateur.

**Sortie :** diagnostics explicables, listes d'objets et définitions auditées.

### Lot 4 — Aide à la construction

- [ ] Définir les règles de recommandations et leur niveau de preuve.
- [ ] Générer les suggestions de pages de synthèse / révision manquantes.
- [ ] Prioriser les lacunes par impact pédagogique, dépendances et coût estimé, sans score unique opaque.
- [ ] Ajouter une boucle de revue humaine et de traçabilité des décisions.

**Sortie :** backlog de recommandations, aucune mutation automatique.

### Lot 5 — Publication et maintenance

- [ ] Ajouter une vue Quarto générée.
- [ ] Ajouter un workflow périodique et manuel.
- [ ] Mesurer les performances ×1/×10/×100.
- [ ] Documenter la mise à jour, le cache, la reproductibilité et la reprise sur erreur.

**Sortie :** système documenté, maintenable et intégré à la CI.

## 13. Articulation avec les chantiers existants

- **#156 :** réutiliser le calculateur KPI, ses définitions, ses tests et son benchmark ; étendre les diagnostics sans ratio de connectivité prématuré.
- **#114 :** utiliser l'inventaire pipeline et la cartographie fichiers → registres → schémas → validateurs ; ne pas dupliquer les audits.
- **#112 :** réutiliser le graphe et les conventions de relations inter-domaines ; ne jamais déduire de causalité à partir de tags ou de voisinages.
- **#127 :** conserver la distinction entre domaine, priorité, nature et dépendance pour le backlog.
- **#178 et #177 :** tenir compte de l'extension récente de l'audit aux registres complémentaires et aux neuf registres canoniques.
- **#180 :** préserver les contrôles de vocabulaire, de portée géographique, de cohérence fiches–graphe et les mesures de performance proposés dans cette PR, après validation et intégration.

## 14. Critères de réussite

Le système sera considéré comme utile lorsque :

- un utilisateur peut demander combien de pages, leçons et notions existent sans compter manuellement ;
- chaque résultat peut être expliqué et reproduit à partir d'un commit donné ;
- les pages d'une notion et les notions d'une page sont consultables dans les deux sens ;\n- les pages disposent d'un état vérifiable concernant leur ressource de révision associée ;
- les liens entre pages sont distingués par type, direction et profondeur ;
- les parcours Understand et Build sont inventoriés sans heuristique opaque ;
- les lacunes et anomalies sont accompagnées de listes concrètes ;
- les recommandations expliquent pourquoi elles sont proposées et restent soumises à validation ;
- les outils réutilisent les métadonnées et scripts existants plutôt que de créer des sources concurrentes ;
- les performances restent mesurées et proportionnées au volume ;
- la documentation permet à un contributeur de comprendre, utiliser, tester et faire évoluer le système.

## 15. Décisions encore ouvertes

1. Quel est le format canonique effectif des parcours Understand et Build ?
2. Les notions sont-elles reliées aux pages par frontmatter, liens, registre, graphe ou plusieurs mécanismes ?
3. Qu'est-ce qui définit exactement une page pédagogique éligible, par opposition à une page technique ou éditoriale ?
4. Les leçons sont-elles des fichiers, des sections, des entrées de navigation ou des regroupements calculés ?
5. Quels outils existants peuvent être étendus plutôt que remplacés ?
6. Quelles relations de page à page sont déjà explicites et lesquelles ne sont que des liens de navigation ?

Ces questions doivent être tranchées à partir du dépôt et de tests sur des exemples réels avant toute migration des métadonnées ou modification des validateurs.


## 16. Résultats du premier audit du dépôt (19 novembre 2026)

Le lot 0 a été engagé dans `docs/metadata-learning-inventory-2026-11-19.md`, sur l'arbre Git du commit `2e760631f931839df53556a7acfadc5901f1a5bc`.

Constats vérifiés :

- 271 fichiers suivis et 34 répertoires dans l'arbre audité ;
- 144 fichiers Markdown, aucun fichier Quarto `.qmd` ni HTML ;
- aucune structure dédiée identifiable pour Understand, Build, parcours, leçons ou flashcards dans ce dépôt ;
- des outils existants couvrent déjà les KPIs, la couverture des registres, la validation des schémas et références, les liens Markdown, la fraîcheur des synthèses et le traçage d'impact.

En conséquence, les métriques pédagogiques (nombre de parcours, leçons, pages Understand/Build et associations page–notion) ne sont pas calculables à partir de ce dépôt seul. Leur état doit être `not_modelled` ou `unknown`, jamais assimilé à zéro.

**Ajustement du plan :** avant de développer un adaptateur pédagogique ou un inventaire de pages, identifier le dépôt, la branche ou la configuration qui héberge réellement le corpus Understand/Build. Le modèle pédagogique ne sera figé qu'après inspection de ses données et conventions réelles.

Les métriques documentaires et scientifiques restent, elles, calculables à partir des registres et graphes existants. Leur calcul doit réutiliser les scripts actuels, notamment `calculate_project_kpis.py`, `audit_registry_coverage.py` et `trace_knowledge_impact.py`, sans créer de doublon.
