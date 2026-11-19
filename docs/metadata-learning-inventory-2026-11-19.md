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

## 5. Modèle de liaison recommandé entre corpus pédagogique et Society Lab

Si le parcours pédagogique est hébergé ailleurs, ne pas recopier ses pages dans les registres scientifiques. Construire une couche de liaison minimale, fondée sur les identifiants et chemins canoniques déjà disponibles :

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
