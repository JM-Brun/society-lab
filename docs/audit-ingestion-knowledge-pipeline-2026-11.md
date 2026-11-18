# Audit initial du pipeline d'ingestion et de production des connaissances

**Date :** 18 novembre 2026  
**Périmètre :** dépôt `JM-Brun/society-lab`, branche `main`  
**Commit de référence :** `0363723e9f32217b4eccffe4276db22f83503500`  
**Issue de suivi :** [#114 — Auditer et fiabiliser le pipeline complet](https://github.com/JM-Brun/society-lab/issues/114)

> Ce document est une photographie initiale fondée sur l'inspection des documents d'architecture, des schémas, du validateur principal, des registres et de la CI. Il ne constitue pas encore un audit exhaustif de chaque fiche ni un benchmark de performance. Les constats sont séparés des points restant à tester.

## 1. Conclusion exécutive

Society Lab dispose déjà d'une base sérieuse : source de vérité Git, registres canoniques, schémas JSON, taxonomies contrôlées, graphe typé, protocole d'ingestion, principes de provenance et CI. L'architecture est cohérente avec un corpus documentaire versionné et ne justifie pas, à ce stade, l'introduction d'une base graphe externe.

En revanche, la documentation actuelle décrit mieux les principes que l'exécution opérationnelle. Les contrats d'extraction, la traçabilité fine entre passage source et connaissance, les contrôles sémantiques du graphe, la gestion des versions et les mesures de scalabilité doivent être renforcés et démontrés sur des cas réels.

**Verdict : architecture de départ pertinente ; chaîne de traitement partiellement formalisée et contrôlée ; qualité scientifique non certifiée par la CI.** Ne pas présenter l'ensemble du processus comme entièrement automatisé ou validé.

## 2. Éléments effectivement présents

### 2.1 Architecture et gouvernance documentaire

Documents examinés :
- `docs/architecture.md`
- `docs/ingestion-protocol.md`
- `docs/metadata-and-naming.md`
- `docs/source-policy.md`
- `docs/licensing.md`
- `docs/uncertainty-and-revisions.md`
- `METHODOLOGY.md`
- `knowledge/GRAPH.md`

Points solides :
- Le dépôt Git est désigné comme source de vérité ; les vues éditoriales sont dérivées.
- Les couches Evidence, Knowledge & Research, Graph et Publication sont distinguées.
- Le protocole couvre découverte, déduplication, identification, droits, qualification, extraction, mise en relation, revue, publication et maintenance.
- Les extractions IA sont explicitement des propositions à vérifier dans les sources originales.
- Les limites, désaccords, résultats contradictoires et révisions sont reconnus comme éléments de premier rang.
- Les droits des tiers ne sont pas assimilés à la licence globale du dépôt.

Limite : les étapes ne définissent pas encore systématiquement un contrat d'exécution avec entrées, sorties, états, contrôles, erreurs, reprise et critères de passage.

### 2.2 Schémas et registres

Schémas présents pour :
- sources, études, datasets ;
- claims, hypothèses, prévisions ;
- concepts, mécanismes, territoires ;
- dossiers.

Le validateur principal référence les registres de ces objets et applique les schémas JSON correspondants. Il vérifie aussi les identifiants, les domaines et tags, plusieurs références typées, ainsi que l'existence et la compatibilité des extrémités des relations du graphe.

Les schémas posent des bases utiles :
- source : titre, type, langue, date, URL/DOI, périmètres, méthode, limites, financement/conflits, licence et accès ;
- étude : type d'étude, sources, domaines, méthode, population/unité, résultats et limites ;
- dataset : fournisseur, sources, périmètres, unité d'observation, variables, licence, date de récupération, version, empreinte et transformations ;
- claim : type et statut, périmètre, preuves favorables et contraires, vérifications par source, provenance, révisions ;
- concept : identifiant, définition, domaines, tags et alias ;
- mécanisme : description, direction, étapes, conditions, acteurs, indicateurs, horizon, études favorables/défavorables, claims et limites.

Limites à examiner :
- Les métadonnées de localisation des éléments extraits et la chaîne de transformation ne sont pas encore un contrat partagé de bout en bout entre source, étude, dataset et claim.
- Les informations de version et d'identification persistante ne sont pas uniformément requises, ce qui est normal pour certains types de sources mais nécessite des règles conditionnelles explicites.
- Les objets et fichiers hors des registres actuellement énumérés doivent être inventoriés et leurs règles de validation explicitées.

### 2.3 Graphe et ontologie

`knowledge/GRAPH.md` distingue correctement relations documentaires et relations épistémiques, et exige une justification pour les relations probantes. `knowledge/RELATION_TYPES.yml` définit des relations orientées avec types d'objets autorisés et inverses.

Le validateur vérifie :
- l'existence des nœuds référencés ;
- le type autorisé des extrémités ;
- l'existence du type de relation ;
- l'unicité des identifiants d'arêtes.

Il ne démontre pas, à lui seul, que chaque justification est précise, localisable, fraîche ou scientifiquement suffisante. Les contrôles automatiques de cohérence entre relations embarquées dans les fiches et arêtes du graphe, de synonymie/doublons sémantiques et de qualité des mécanismes restent à examiner.

Le travail transversal de l'issue #112 doit rester articulé à cet audit : ne pas créer de registre ni de graphe parallèle. La distinction entre concept, mécanisme théorique, mécanisme observé, représentation pédagogique et relation causale doit être préservée.

### 2.4 CI et tests

Le workflow `.github/workflows/validate.yml` :
1. installe Python 3.12, PyYAML et jsonschema ;
2. exécute `scripts/validate/validate_registry.py` ;
3. vérifie la correspondance dossiers/synthèses ;
4. signale la fraîcheur des synthèses ;
5. exécute les tests unitaires ;
6. vérifie que les fichiers de schéma sont du JSON valide.

Sur le commit de référence, le workflow **Validate knowledge base** (run 796) et le scan de secrets (run 69) ont réussi. La PR #113 a été intégrée dans `main` avant cette photographie.

Cette réussite atteste uniquement du passage des contrôles implémentés. La validation syntaxique des schémas JSON n'est pas une validation de leur adéquation métier ; les tests unitaires existants ne constituent pas un test de charge du corpus complet.

## 3. Lacunes et risques à instruire

| Domaine | Constat initial | Vérification ou amélioration attendue |
|---|---|---|
| Pipeline | Étapes documentées, contrats opérationnels incomplets | Entrées/sorties, statuts, erreurs, reprise et critères de sortie |
| Lots | Manifeste minimal décrit | Identifiants de lot, critères, décisions, rejets, doublons et journal |
| Provenance | Principes présents, champs dispersés selon les objets | Traçabilité source → localisateur → extraction → objet → publication |
| Extraction | Fiche minimale textuelle | Contrats spécifiques aux textes, tableaux, graphiques et données |
| Vérification | Statuts disponibles pour les claims | Contrôler la cohérence entre statut, localisateur et preuve réellement vérifiée |
| Métadonnées | Schémas utiles mais hétérogènes | Règles conditionnelles, versions, dates, langue, licence, accès et transformations |
| Déduplication | Règles bibliographiques décrites | Cas DOI/URL/versions/traductions/rapports issus d'un même programme |
| Concepts | Schéma minimal utile | Alias, définitions concurrentes, périmètre et détection des doublons |
| Mécanismes | Schéma descriptif présent | Statut épistémique, portée, conditions et preuves contradictoires |
| Relations | Types et extrémités contrôlés | Justification localisable, statut, temporalité, cohérence fiche/graphe |
| Maintenance | Errata et rétractations mentionnés | Propagation contrôlée des changements vers claims, graphes et synthèses |
| Scalabilité | Validation globale en CI | Mesures de temps/mémoire et essais sur corpus ×10/×100 |
| Ergonomie | Plusieurs guides séparés | Parcours opératoire unique avec liens, exemples et décisions de renvoi |

## 4. Points précis à vérifier dans le code

Le validateur `scripts/validate/validate_registry.py` est le centre des contrôles actuels. L'audit détaillé doit notamment vérifier :
- la couverture de tous les types d'objets effectivement présents dans le dépôt ;
- les champs de références imbriqués et les références portées par le graphe ;
- la cohérence des inverses déclarés dans `RELATION_TYPES.yml` ;
- les relations dupliquées, les cycles interdits ou suspects et les arêtes sans justification exploitable ;
- les références territoriales, organisations, méthodes et analyses ;
- la cohérence des métadonnées entre fiches sources, études, datasets et claims ;
- les fichiers qui ne sont pas enregistrés dans les registres canoniques ;
- la validation des dates et formats, notamment les formats de langue et les URI ;
- la qualité des messages d'erreur et la durée d'exécution à différentes tailles de corpus.

Ne pas ajouter de contraintes bloquantes avant d'avoir mesuré les données existantes et prévu une migration explicite.

## 5. Architecture cible — principes à conserver

1. Un seul registre canonique par type d'objet ; les vues et exports sont dérivés.
2. Pas d'automatisation qui transforme une extraction en fait vérifié sans contrôle humain.
3. La provenance est attachée à l'élément de connaissance et pas seulement à la fiche source générale.
4. Les objets source, étude, dataset, résultat, claim, concept et mécanisme restent distincts.
5. Les relations épistémiques ont une justification précise et une portée ; les liens d'organisation ne sont pas des preuves.
6. Les identifiants restent stables ; les corrections et versions sont traçables.
7. Les contrôles techniques détectent des incohérences ; ils ne délivrent pas de certification scientifique.
8. Pas de migration vers une base externe tant que les besoins de requête, de volume ou de collaboration ne le justifient pas.

## 6. Cas pilotes recommandés

- **Parcoursup (#2)** : source administrative, dictionnaire de données, extraction reproductible, unité d'observation, dénominateurs et résultats descriptifs.
- **ADEME Saison 2 (#110)** : API/catalogue, versions, acquisition de données brutes, empreintes, harmonisation et comparabilité.
- **SMIC** : séries historiques, révisions de sources, versions, unités monétaires, calculs reproductibles et controverses.
- **TIG** : sources institutionnelles, cohortes, indicateurs de délai, périmètres et dénominateurs.
- **Relations inter-domaines (#112)** : concepts/mécanismes, direction, portée, temporalité et garde-fous causaux.

Ces cas servent à tester un même pipeline sur des formes de preuve différentes, sans créer de parcours éditoriaux concurrents.

## 7. Séquence de travail proposée

1. Inventorier les objets, registres, schémas, fichiers et champs réellement utilisés.
2. Construire une matrice de traçabilité sur quelques objets complets.
3. Définir le contrat d'extraction et les métadonnées manquantes à partir des cas pilotes.
4. Renforcer les validateurs par petits changements rétrocompatibles et tests négatifs.
5. Mesurer la performance avant toute optimisation ou changement de stockage.
6. Documenter la maintenance et la propagation des révisions.
7. Migrer les fiches existantes par lots contrôlés, avec rapport de couverture et sans perte de contenu.

## 8. Statut

**Audit initial réalisé ; audit opérationnel et exhaustif à poursuivre.**

Aucune conclusion n'est tirée ici sur la qualité de chaque source ou claim individuel. Les écarts à confirmer, les tests à écrire et les migrations sont suivis dans l'issue [#114](https://github.com/JM-Brun/society-lab/issues/114).