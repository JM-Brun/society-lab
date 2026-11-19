# Audit initial des métadonnées et de la structure pédagogique

**Date :** 19 novembre 2026  
**Dépôt :** `JM-Brun/society-lab`  
**Branche de référence :** `main`  
**Commit audité :** `2e760631f931839df53556a7acfadc5901f1a5bc`  
**Méthode :** arbre Git récursif complet (`git/trees/main?recursive=1`), complété par la lecture des scripts, registres, schémas et documents d'architecture.

## 1. Résultat essentiel

L'architecture d'exploitation des métadonnées est désormais documentée dans `docs/metadata-intelligence-architecture.md` (PR #181, fusionnée dans `main`).

L'audit du dépôt montre toutefois une distinction importante :

- Le dépôt contient déjà un système substantiel de connaissances structurées : neuf familles de registres canoniques, taxonomie, tags, types de relations, graphe, synthèses, schémas, validateurs, calculateur de KPIs et outils d'analyse d'impact.
- **Aucune structure dédiée nommée Understand, Build, parcours d'apprentissage, leçon ou flashcard n'est présente dans l'arbre Git audité.**
- Aucun fichier Quarto `.qmd` ni fichier HTML n'est présent dans cet instantané.
- Les 144 fichiers Markdown ne peuvent donc pas être assimilés à 144 pages pédagogiques : ils comprennent documentation, analyses, dossiers, synthèses, protocoles, guides et autres ressources.
- Il n'est pas possible de calculer honnêtement le nombre de parcours, de leçons ou de pages pédagogiques à partir des seules structures actuellement observées.

**Conséquence d'architecture :** la première livraison ne doit pas inventer des parcours ou transformer arbitrairement les dossiers et synthèses en leçons. Il faut d'abord identifier où réside le site/parcours pédagogique attendu, ou constater qu'il reste à construire. Le système de métadonnées peut déjà exploiter les objets documentaires et scientifiques du dépôt, mais les métriques pédagogiques restent « non disponibles / non modélisées », et non égales à zéro.

## 2. Photographie du dépôt

### 2.1 Volume de l'arbre Git

| Mesure | Valeur |
|---|---:|
| Entrées de l'arbre récursif | 305 |
| Fichiers suivis (blobs) | 271 |
| Répertoires (hors racine) | 34 |
| Fichiers Markdown `.md` | 144 |
| Fichiers Quarto `.qmd` | 0 |
| Fichiers HTML | 0 |
| Fichiers Python | 45 |
| Fichiers YAML `.yml` | 57 |
| Fichiers YAML `.yaml` | 1 |
| Schémas / fichiers JSON | 13 |
| Fichiers CSV | 8 |

Ces valeurs décrivent exclusivement l'arbre Git du commit indiqué. Elles ne comptent ni fichiers locaux non suivis, ni contenu externe, ni ressources servies par un autre dépôt.

### 2.2 Répartition par répertoire de premier niveau

| Répertoire | Fichiers |
|---|---:|
| `.claude` | 1 |
| `.github` | 9 |
| Racine | 9 |
| `analysis` | 7 |
| `claims` | 25 |
| `data` | 9 |
| `docs` | 43 |
| `dossiers` | 61 |
| `forecasts` | 2 |
| `governance` | 4 |
| `hypotheses` | 4 |
| `knowledge` | 16 |
| `research` | 5 |
| `schemas` | 11 |
| `scripts` | 22 |
| `sources` | 5 |
| `syntheses` | 13 |
| `templates` | 2 |
| `tests` | 22 |
| `tools` | 1 |

Le nombre de fichiers dans un répertoire ne représente pas nécessairement le nombre d'objets de son registre : il peut inclure le registre lui-même, des README, des modèles ou des notes.

### 2.3 Structure pédagogique : constat et limites

La recherche dans l'arbre n'a identifié :

- aucun répertoire `understand/` ou `build/` à la racine ;
- aucun chemin contenant `learning-path`, `lesson` ou `flashcard` ;
- aucun fichier `.qmd` ou `.html` ;
- aucun manifeste de navigation ou registre de parcours identifiable par ces conventions.

Cela ne prouve pas que le projet global ne possède aucun parcours pédagogique : ils peuvent être hébergés dans un autre dépôt, une branche, une application, une configuration externe ou sous des noms qui ne sont pas détectables par ces conventions. L'audit porte sur le dépôt `society-lab` et sur le commit précisé ci-dessus.

**Décision :** ne publier aucun nombre de pages Understand/Build, de leçons ou de parcours tant que leur source effective n'a pas été localisée et inspectée. La prochaine vérification doit porter sur le dépôt / site qui héberge effectivement ces pages et sur les liens éventuels entre ce corpus et `society-lab`.

## 3. Capacités déjà disponibles à réutiliser

| Besoin | Outil existant | Ce qu'il apporte | Ce qu'il ne faut pas lui faire faire |
|---|---|---|---|
| Calcul de KPIs | `scripts/validate/calculate_project_kpis.py` | Charge les neuf registres, la taxonomie, les territoires, les relations et les correspondances de synthèses ; calcule des mesures documentaires explicables. | Ne pas le dupliquer dans un nouveau calculateur. |
| Couverture des fiches | `scripts/audit/audit_registry_coverage.py` | Compare registres, fichiers, schémas, champs observés et correspondances dossier–synthèse. | Ne pas le transformer en inventaire de pages pédagogiques sans source de parcours. |
| Validation des registres | `scripts/validate/validate_registry.py` | Valide les registres, schémas, identifiants, références et relations selon les contrats existants. | Ne garantit pas la qualité scientifique ni la couverture pédagogique. |
| Traçage d'impact | `scripts/analysis/trace_knowledge_impact.py` | Suit des références typées explicites depuis une source vers études, datasets, claims, hypothèses, mécanismes, prévisions, dossiers et synthèses. | N'infère pas de dépendances à partir de tags, cooccurrences ou proximité du graphe. |
| Liens Markdown | `scripts/validate/validate_markdown_links.py` | Contrôle les liens Markdown internes. | Un lien de navigation n'est pas une relation pédagogique ou scientifique. |
| Ancres Markdown | `scripts/validate/validate_markdown_anchors.py` | Contrôle les références aux ancres. | Ne fournit pas une cartographie sémantique des pages. |
| Synthèses | `scripts/validate/validate_syntheses.py` | Vérifie les correspondances et les contraintes de synthèse existantes. | Ne mesure pas la qualité réelle d'une synthèse. |
| Fraîcheur | `scripts/validate/check_synthesis_freshness.py` | Signale les synthèses susceptibles d'être à revoir. | La date d'un commit ne prouve pas une revue scientifique. |
| KPIs et performance | `scripts/benchmark/benchmark_project_kpis.py`, `scripts/audit/benchmark_validation_scale.py` | Mesures de performance des outils existants. | Ne pas créer un benchmark concurrent sans question de performance nouvelle. |
| Vue du backlog | `scripts/report/generate_backlog_view.py` | Génère une vue des issues et du travail à réaliser. | Les labels GitHub ne remplacent pas la taxonomie scientifique. |

### 3.1 Sources canoniques structurantes

- `knowledge/TAXONOMY.yml` : domaines.
- `knowledge/TAGS.yml` : vocabulaire transversal contrôlé.
- `knowledge/RELATION_TYPES.yml` : relations orientées et types d'endpoints autorisés.
- `knowledge/graph.yml` : arêtes typées et justifiées.
- `knowledge/concepts/registry.yml` : concepts canoniques.
- `knowledge/mechanisms/registry.yml` : mécanismes.
- Les registres des sources, études, datasets, claims, hypothèses, dossiers et prévisions.
- `syntheses/registry.yml` : association dossiers–synthèses.
- Les schémas JSON et les validateurs associés.

Le graphe décrit actuellement des relations entre objets de connaissance et de recherche. Il ne doit pas être étendu avec des relations de parcours, de leçon ou de progression pédagogique tant que le modèle de navigation et les besoins réels ne sont pas identifiés.

## 4. Ce que le système peut mesurer dès maintenant

### 4.1 Mesures documentaires et scientifiques

Les mesures déjà traitées par le calculateur de KPIs doivent rester le point de départ :

- couverture documentaire des sources ;
- répartition des statuts épistémiques des claims ;
- couverture des dossiers par les synthèses ;
- diagnostics de cohérence et de couverture des relations, sans ratio de connectivité global non justifié.

Les valeurs de l'audit de faisabilité daté du 18 novembre 2026 sont un instantané historique ; ne pas les réutiliser comme chiffres courants sans recalcul sur le commit étudié.

### 4.2 Mesures de structure du dépôt

L'arbre Git permet déjà de produire des comptages reproductibles par :

- extension ;
- répertoire ;
- famille de ressources ;
- présence ou absence de registres, schémas, scripts et tests ;
- liens entre fichiers et objets canoniques, à partir des outils de couverture existants.

Ces mesures sont des indicateurs d'inventaire technique, pas des métriques pédagogiques.

### 4.3 Mesures pédagogiques à suspendre

Les métriques suivantes restent indisponibles tant que le corpus pédagogique n'est pas localisé ou modélisé :

- nombre de parcours ;
- nombre de leçons ;
- nombre de pages Understand et Build ;
- nombre de pages par leçon et par parcours ;
- nombre de pages explicitement associées à une notion ;
- nombre de notions enseignées par page ;
- nombre de pages pédagogiques entrantes/sortantes ;
- nombre de fiches de révision, flashcards et résumés associés à chaque page.

Pour chacune, distinguer trois états dans les futurs rapports : `available`, `not_modelled`, `unknown`. Ne pas convertir `not_modelled` en zéro.

## 5. Modèle de liaison entre corpus pédagogique et Society Lab

Le corpus pédagogique a été localisé dans le dépôt public [`JM-Brun/llm-lab`](https://github.com/JM-Brun/llm-lab). Il ne faut pas recopier ses pages dans les registres scientifiques de Society Lab. Construire une couche de liaison minimale, fondée sur les identifiants et chemins canoniques déjà disponibles :

1. une page pédagogique garde son identifiant et son chemin dans son dépôt d'origine ;
2. une notion renvoie vers l'identifiant `CONCEPT-*` du registre de Society Lab ;
3. un dossier, une synthèse, une étude ou une source conserve son identifiant canonique propre ;
4. la relation entre une page pédagogique et un concept est explicite et qualifiée (par exemple : notion enseignée, prérequis, mention contextuelle) ;
5. la provenance de l'association est traçable (métadonnée explicite, décision éditoriale ou extraction à confirmer) ;
6. les liens de navigation, les associations pédagogiques et les relations scientifiques restent trois catégories différentes.

Une éventuelle projection inter-dépôts devra préciser le dépôt source, le commit ou la version, le chemin, l'identifiant stable et la date de collecte. Les données externes indisponibles doivent être signalées comme telles.

## 6. Plan de travail corrigé

### Lot 0A — Localiser le corpus pédagogique

- [ ] Identifier le dépôt et la branche qui hébergent réellement les pages Understand et Build.
- [ ] Vérifier si le site publié est généré depuis un autre dépôt ou une autre configuration.
- [ ] Inventorier les fichiers, les routes, la navigation et les éventuels manifestes de parcours.
- [ ] Identifier la définition concrète d'une page, d'une leçon, d'un parcours et d'une ressource de révision.
- [ ] Vérifier comment les notions sont référencées (IDs, frontmatter, liens, graphes ou autre).
- [ ] Identifier les pages partagées entre parcours, les pages exclues et les ressources dérivées.

**Sortie attendue :** source du corpus identifiée, inventaire exhaustif et dictionnaire des champs réels. Si le corpus n'existe pas encore, acter explicitement cette décision au lieu de simuler un inventaire.

### Lot 0B — Consolider les outils de Society Lab

- [ ] Comparer les sorties de `calculate_project_kpis.py` et `audit_registry_coverage.py` pour éviter les calculs redondants.
- [ ] Documenter les contrats d'entrée/sortie de `trace_knowledge_impact.py`.
- [ ] Vérifier la couverture réelle des liens Markdown et ancres dans la CI.
- [ ] Inventorier les tests associés et les formats de rapport déjà produits.
- [ ] Définir une API commune uniquement si plusieurs outils ont réellement besoin du même index de lecture.

### Lot 1 — Premier catalogue interrogeable

- [ ] Créer un inventaire commun des objets canoniques de Society Lab, sans recopier les données.
- [ ] Ajouter les index inverses des relations explicites.
- [ ] Exposer des requêtes de pages/notions/dossiers/sources à partir des relations et champs réellement existants.
- [ ] Ajouter le corpus pédagogique comme adaptateur séparé, après le lot 0A.
- [ ] Produire des résultats JSON déterministes avec listes d'objets et provenance.

### Lot 2 — Couverture et recommandations

- [ ] Définir les règles d'éligibilité par famille d'objets.
- [ ] Détecter les références orphelines et les écarts fiches–graphe.
- [ ] Mesurer les associations pédagogiques explicites, une fois disponibles.
- [ ] Produire des suggestions de fiches de révision manquantes, uniquement si la règle éditoriale et la population éligible sont explicites.
- [ ] Conserver les recommandations en lecture seule et soumises à validation humaine.

## 7. Critères de validation du lot 0

Le lot 0 sera terminé lorsque :

- le dépôt qui contient effectivement Understand/Build est identifié ou leur absence est explicitement actée ;
- les définitions de page, leçon, parcours et ressource de révision sont tirées des données réelles ;
- les pages sont dédupliquées selon une identité stable et les occurrences dans plusieurs parcours sont conservées ;
- les associations page–notion distinguent enseignement explicite, prérequis et simple mention ;
- les liens de navigation ne sont pas assimilés à des relations sémantiques ;
- les scripts et rapports déjà présents sont réutilisés ;
- les métriques non calculables sont publiées comme non modélisées ou inconnues, jamais comme zéro.

## 8. Traçabilité et suite

- Architecture cible : `docs/metadata-intelligence-architecture.md`.
- KPIs : `docs/project-kpis.md` et audit de faisabilité associé.
- Couverture des registres : `scripts/audit/audit_registry_coverage.py`.
- Calcul des KPIs : `scripts/validate/calculate_project_kpis.py`.
- Impact de connaissance : `scripts/analysis/trace_knowledge_impact.py`.
- Inventaire de fichiers précédent : `docs/repository-file-inventory-2026-11-18.md` (instantané du 18 novembre, à ne pas confondre avec le présent arbre).

**Prochaine action prioritaire :** retrouver le dépôt ou la configuration qui héberge réellement les pages Understand et Build. Tant que cette dépendance n'est pas résolue, le comptage pédagogique serait artificiel.


## 9. Corpus pédagogique retrouvé dans LLM Lab — audit complémentaire

Le dépôt pédagogique distinct est `JM-Brun/llm-lab`, branche `main`, commit audité `07fd29f92a5c96a62c725dc806e284ff6199a82e`. L'arbre contient 924 fichiers et 77 répertoires. Il comprend 233 fichiers Quarto `.qmd` sous `site/` : 110 sous `site/fr/`, 111 sous `site/en/`, 10 fragments générés sous `site/includes/` et 2 pages partagées à la racine de `site/`.

Le manifeste `site/_quarto.yml` comporte **223 entrées explicites dans `project.render`** : 110 françaises, 111 anglaises et 2 pages racine. Ce nombre de pages rendues ne doit pas être confondu avec les 233 fichiers QMD présents dans l'arbre : les fragments inclus sont des ressources de génération, pas des pages autonomes du parcours.

### 9.1 Understand : parcours canonique

Le fichier `data/guided-route.yml` est la source canonique de la route Understand. Son instantané contient :

| Mesure | Français | Anglais |
|---|---:|---:|
| Étapes de parcours | 9 | 9 |
| Occurrences de pages principales dans les étapes | 21 | 21 |
| Pages principales distinctes | 20 | 20 |
| Occurrences de pages optionnelles | 28 | 28 |
| Pages optionnelles distinctes | 27 | 27 |
| Pages distinctes principales + optionnelles | 46 | 46 |

La page `generation` est référencée dans deux étapes principales ; il faut donc distinguer occurrences et pages distinctes. `cross-entropy` apparaît à la fois comme page principale et comme ressource optionnelle, ce qui explique que l'union compte 46 pages et non 47.

Les deux transitions typées entre étapes sont conservées séparément des appartenances aux étapes. Les liens de page `suggested_route` ne doivent pas être substitués aux appartenances canoniques du parcours.

### 9.2 Build : parcours d'implémentation indépendant

Les pages `site/fr/build-path.qmd` et `site/en/build-path.qmd` sont les points d'entrée du parcours Build. Leurs métadonnées hiérarchiques référencent six pages enfants :

- cinq visites guidées : configuration, briques numériques, bloc Transformer, assemblage du modèle et génération ;
- une branche distincte de préparation du corpus.

Le document `docs/learning-path.md` précise que Build suit les dépendances d'implémentation et ne constitue pas la suite obligatoire d'Understand. Il faut conserver cette distinction : les cinq visites guidées ne doivent pas être comptées comme cinq étapes Understand, et la branche de préparation du corpus ne doit pas être transformée en prérequis de l'inférence.

### 9.3 Concepts et associations explicites page–notion

Le registre bilingue `data/concepts.yml` contient, au commit audité :

| Mesure | Valeur |
|---|---:|
| Concepts canoniques distincts | 102 |
| Concepts ayant au moins une association explicite à une page | 99 |
| Concepts sans association de page | 3 |
| Occurrences d'associations concept–page | 290 |
| Identifiants de page distincts référencés | 84 |

Les trois concepts sans association de page sont `multi-head-attention`, `causal-mask` et `softmax`. Cela constitue un diagnostic à examiner, pas une erreur automatique : une notion peut être représentée dans les explications d'une page plus générale, dans le graphe ou dans les ressources sans avoir de page autonome.

Le champ `concepts[].resources` de `data/concepts.yml` contient ici des **identifiants de pages**. Il ne doit pas être confondu avec le registre distinct `data/resources.yml`, qui porte des ressources non-page (notamment des modules d'implémentation). Le système de requêtes devra exposer ces deux associations sous des catégories différentes.

Quatre références de page du registre de concepts ne figurent pas dans la liste `project.render` de `site/_quarto.yml` au commit audité : les pages d'exercices FR/EN de l'apprentissage en contexte et de l'ingénierie du contexte. Les quatre fichiers existent et portent `status:published` dans leur page-map. Ce constat est un **cas de réconciliation à examiner**, pas une preuve suffisante de lien cassé : vérifier si ces pages sont volontairement exclues du rendu explicite, intégrées autrement ou si le manifeste doit être complété.

### 9.4 Outils pédagogiques déjà présents

LLM Lab possède déjà les composants suivants :

| Composant | Source canonique / rôle |
|---|---|
| Identité et métadonnées de page | `site/**/*.qmd`, frontmatter et bloc `LLM-LAB-PAGE-MAP v1` |
| Index de pages publiées | `site/tools/page_index.py` |
| Validation des métadonnées et des relations de page | `site/tools/check_page_metadata.py` |
| Audit topologique et candidats de revue | `site/tools/audit_page_metadata.py` |
| Génération de la carte d'apprentissage | `site/tools/build_learning_map.py` |
| Validation du registre des ressources non-page | `site/tools/check_resource_registry.py` |
| Parcours Understand | `data/guided-route.yml` |
| Parcours Build et preuves de réalisation | `docs/learning-path.md`, pages Build, code et tests |
| Concepts et associations page–concept | `data/concepts.yml` |
| Architecture cible de requêtes et diagnostics | `docs/project-intelligence-layer.md` |
| Découverte inter-graphes et traçabilité | issue [#1233](https://github.com/JM-Brun/llm-lab/issues/1233), ouverte au moment de l'audit |

La *Project Intelligence Layer* est décrite comme une architecture proposée, sans composant runtime unique déjà livré. Les lecteurs, validateurs et générateurs spécialisés existent néanmoins déjà. La prochaine étape n'est donc pas de créer une seconde architecture, mais de faire converger les outils existants vers une API de requêtes testée, selon l'issue #1233 et les priorités déjà ouvertes dans LLM Lab.

### 9.4.1 Implémentations en cours dans LLM Lab

Deux PR ouvertes dans `JM-Brun/llm-lab` matérialisent déjà une partie des besoins décrits ici :

- [PR #1380 — deterministic project metadata query index](https://github.com/JM-Brun/llm-lab/pull/1380) ajoute `site/tools/project_index.py` et ses tests. Le modèle en mémoire indexe les tags, les associations explicites page–concept dans les deux sens, les relations de page par famille et direction, les domaines et les appartenances aux étapes Understand. Il expose des requêtes et des comptages avec des unités distinctes.
- [PR #1379 — generated Understand/Build revision coverage inventory](https://github.com/JM-Brun/llm-lab/pull/1379) ajoute `site/tools/audit_revision_coverage.py`, ses tests et son intégration CI. Il inventorie les pages publiées des destinations Understand/Build, conserve les appartenances Understand core/optional, signale les pages Understand hors parcours, associe les concepts et les ressources d'implémentation et laisse explicitement la couverture des synthèses à `not_assessed`.

Au moment de cet audit, les deux PR sont ouvertes et leurs tests / contrôles qualité sont encore en cours ; aucune réussite n'est revendiquée. Elles sont toutefois les implémentations à suivre et à réutiliser. Ne pas créer dans Society Lab un second index de pages ou un second inventaire de fiches de révision.

La suite logique, après validation et fusion de ces PR, est de recalculer les inventaires sur le HEAD courant de LLM Lab, de traiter les associations de pages publiées absentes du manifeste de rendu et de poursuivre l'issue [#1233](https://github.com/JM-Brun/llm-lab/issues/1233) pour les passerelles inter-graphes et les chemins de preuve.

### 9.4.2 Premier inventaire Understand/Build généré en CI

La PR #1379 a exécuté `site/tools/audit_revision_coverage.py` sur le commit `1b431e2ff2ec2a04a76941756c0523e443394d6a`. Le job de qualité a généré et téléversé un artefact JSON/Markdown (`revision-coverage-inventory`, workflow run `44564321515`). Ces chiffres sont donc issus du code de la PR ouverte, pas encore d'une version fusionnée sur `main`.

| Destination / type | Pages FR+EN | Objets pédagogiques bilingues |
|---|---:|---:|
| Understand — `concept-lesson` | 42 | 21 leçons |
| Understand — `system-overview` | 4 | 2 pages d'orientation système |
| **Understand total** | **46** | **23 sujets bilingues** |
| Build — `guided-build` | 14 | 7 modules |
| Build — `concept-bridge` | 2 | 1 sujet |
| **Build total** | **16** | **8 sujets bilingues** |
| **Understand + Build** | **62** | **31 sujets bilingues** |

Le parcours Understand compte neuf étapes canoniques. Le rapport de couverture distingue les appartenances core et optional (40 et 6 occurrences dans son modèle de projection) ; il ne faut pas confondre ces occurrences, les pages distinctes et les sujets bilingues. Build est inventorié par sa destination et ses preuves ; aucun ordre linéaire n'est déduit de la seule liste des pages.

### 9.4.3 Associations explicites et couverture des ressources de révision

Le même artefact donne les mesures suivantes :

- Understand : 144 associations explicites page–concept ; les 46 pages ont au moins un concept associé.
- Build : 18 associations page–concept sur 6 pages ; 10 pages ont une association explicite vers une ressource d'implémentation.
- Les 62 pages Understand/Build ont toutes `synthesis_status: not_assessed`.

Le dernier point est une limite de modèle, pas un résultat « zéro fiche de révision ». Le dépôt contient des fiches et pages de révision, mais aucune relation typée et suffisamment exhaustive ne permet encore d'affirmer quelle fiche, flashcard ou synthèse couvre quelle page. Avant de créer un champ ou un registre, inventorier les ressources de révision existantes (pages Quarto, `docs/revision-sheets/`, fiches, flashcards, exercices) et vérifier si leur identité peut être portée par les structures existantes. La future mesure devra distinguer `covered`, `not_covered`, `not_expected`, `unknown` et `not_assessed`.

### 9.4.4 État des validations des PR LLM Lab au 19 novembre 2026

- PR [#1379](https://github.com/JM-Brun/llm-lab/pull/1379) : le job Python quality a réussi, le test suite a réussi après relance ; le contrôle Quarto / navigateur était encore en cours lors de la dernière vérification. L'artefact ci-dessus a été généré avec succès.
- PR [#1380](https://github.com/JM-Brun/llm-lab/pull/1380) : une première CI a révélé un problème Ruff d'ordre des imports, puis un problème de formatage dans le test ajouté. Les deux corrections ont été poussées sur la branche ; les nouveaux contrôles doivent encore être vérifiés sur le dernier HEAD.

### 9.5 Frontière inter-dépôts à préserver

- `llm-lab` reste propriétaire des pages, routes, métadonnées pédagogiques, concepts LLM, ressources d'implémentation et graphes associés.
- `society-lab` reste propriétaire des sources, études, datasets, claims, hypothèses, concepts et mécanismes sociétaux, dossiers et synthèses.
- Les identifiants de concepts ne sont pas fusionnés par simple similarité de libellé. Une correspondance entre deux concepts doit être qualifiée (exacte, partielle, analogue, ambiguë ou absente), justifiée et versionnée.
- Les graphes pédagogiques et scientifiques restent séparés. Les passerelles inter-dépôts sont des références ou relations d'interopérabilité explicites, pas une fusion des graphes.
- Les outils de chaque dépôt restent exécutables indépendamment ; aucune page publique de Society Lab ne doit dépendre d'un artefact non publié de LLM Lab.

Références complémentaires : [contrat inter-dépôts de Society Lab](cross-repository-contract.md), [revue de gestion des connaissances LLM Lab / Society Lab](cross-repository-knowledge-management-review.md), [architecture Project Intelligence Layer de LLM Lab](https://github.com/JM-Brun/llm-lab/blob/main/docs/project-intelligence-layer.md) et [schéma des métadonnées de page LLM Lab](https://github.com/JM-Brun/llm-lab/blob/main/docs/page-metadata-schema.md).
