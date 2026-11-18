# Revue inter-dépôts : gestion des connaissances de LLM Lab et Society Lab

**Date :** 2026-11-18  
**Statut :** revue documentaire et proposition d'adaptation ; aucune migration de données ni adoption automatique de l'architecture LLM Lab.

## 1. Décision

LLM Lab apporte des motifs d'architecture utiles pour renforcer la traçabilité de Society Lab, en particulier la séparation entre identité d'une source, événements d'inspection, extractions atomiques et connaissances canoniques. Il ne faut ni fusionner les dépôts, ni importer les graphes pédagogiques, ni remplacer les registres et schémas existants.

Le dépôt Society Lab reste la source de vérité de ses sources, études, jeux de données, claims, hypothèses, concepts, mécanismes, analyses et synthèses. Cette revue complète le protocole d'audit suivi dans l'issue #114 ; elle ne crée pas un second pipeline.

## 2. Périmètre et prudence

La comparaison porte sur les documents d'architecture et de processus consultés dans les deux dépôts au 18 novembre 2026. Les documents LLM Lab décrivent notamment une architecture cible de lineage et une trajectoire de migration : ils ne prouvent pas que chaque composant est déjà implémenté ou opérationnel. Les propositions ci-dessous sont donc des motifs à évaluer, pas des fonctionnalités réputées disponibles.

Références LLM Lab :
- [Architecture de l'information](https://github.com/JM-Brun/llm-lab/blob/main/docs/information-architecture.md)
- [Architecture de provenance des sources](https://github.com/JM-Brun/llm-lab/blob/main/docs/source-lineage-architecture.md)
- [Schéma du catalogue de sources](https://github.com/JM-Brun/llm-lab/blob/main/docs/source-catalogue-schema.md)
- [Schéma des métadonnées de page](https://github.com/JM-Brun/llm-lab/blob/main/docs/page-metadata-schema.md)
- [Standards du graphe de connaissances](https://github.com/JM-Brun/llm-lab/blob/main/docs/knowledge-graph-standards.md)
- [Intégration source vers système de connaissance](https://github.com/JM-Brun/llm-lab/blob/main/docs/workflows/source-to-learning-system-integration.md)
- [Validation source vers connaissance](https://github.com/JM-Brun/llm-lab/blob/main/docs/workflows/source-to-knowledge-validation.md)
- [Audit du processus source](https://github.com/JM-Brun/llm-lab/blob/main/docs/source-process-audit.md)

Références Society Lab à maintenir comme contrats canoniques :
- `docs/architecture.md`
- `docs/ingestion-protocol.md`
- `docs/metadata-and-naming.md`
- `docs/cross-repository-contract.md`
- `knowledge/GRAPH.md`
- `knowledge/RELATION_TYPES.yml`
- `docs/audit-ingestion-knowledge-pipeline-2026-11.md`
- issue [#114](https://github.com/JM-Brun/society-lab/issues/114)

## 3. Correspondance fonctionnelle

| Motif observé dans LLM Lab | État / équivalent Society Lab | Apport potentiel | Décision |
|---|---|---|---|
| Catalogue de sources avec métadonnées typées | Registres et schémas de sources déjà présents | Vérifier la couverture des identifiants externes, versions, langues, licences et dates d'accès | Étendre les schémas existants seulement après audit des fiches réelles |
| Événements d'inspection séparés de la fiche source | Le protocole décrit qualification et maintenance ; l'historique est surtout porté par Git et les fiches | Historique append-only des consultations, contrôles, changements d'accès et révisions | Prototype ciblé, sans dupliquer l'identité bibliographique |
| Extractions atomiques avec localisateurs | Claims et traces de vérification existent ; traçabilité de bout en bout incomplète | Relier une connaissance à une page, section, tableau, figure ou observation précise | Priorité élevée ; commencer par un petit nombre de cas réels |
| Lineage entre source, extraction et connaissance | Relations et références typées déjà présentes dans le graphe | Rendre explicites les dépendances et propager les corrections/rétractations | Ajouter une couche de provenance compatible avec le graphe existant, pas un graphe concurrent |
| Attribution de la voix / du statut du contenu | Distinctions épistémiques déjà prescrites dans la méthodologie | Distinguer auteur, source secondaire, commentaire, extraction automatisée et interprétation éditoriale | Formaliser dans le contrat d'extraction |
| Index générés depuis les fiches canoniques | Principe déjà explicite dans Society Lab | Réduire les divergences entre registres et fiches | Conserver la règle existante et vérifier son application |
| Graphes de sources, concepts, pages et parcours pédagogiques distincts | Society Lab possède plusieurs vues et graphes avec des objets sociétaux propres | Clarifier la fonction de chaque graphe et les passerelles entre eux | Ne pas importer les graphes de parcours d'apprentissage de LLM Lab |

## 4. Ce qui doit rester spécifique à Society Lab

Les métadonnées de recherche sociétale ne doivent pas être réduites à un catalogue documentaire générique. Selon le type de source, d'étude, de dataset, de résultat ou de claim, il faut préserver :
- population, unité d'analyse, échantillonnage et dénominateur ;
- période étudiée, date de publication et période de validité ;
- territoire observé, juridiction, aire fonctionnelle et territoires de comparaison ;
- méthode, variables, définitions opérationnelles et limites ;
- financement, conflits d'intérêts et rôle des producteurs ;
- distinction entre résultat rapporté, recalcul reproductible, interprétation, hypothèse et jugement normatif.

Les concepts, mécanismes théoriques, mécanismes observés, mécanismes causaux étayés et représentations pédagogiques restent des objets distincts. Une proximité de vocabulaire entre dépôts n'autorise ni fusion d'identifiants ni équivalence de relations.

## 5. Contrat de provenance cible

La chaîne à rendre navigable est :

`source et version → événement d'inspection → passage / donnée localisée → extraction → étude ou dataset → résultat / claim → relation justifiée → dossier → passage de synthèse`

Chaque maillon doit conserver son identifiant, son type, sa provenance et son statut. Une relation de lineage signifie qu'un objet dépend d'un autre ; elle ne signifie pas que l'affirmation est vraie ni que deux publications constituent des confirmations indépendantes.

### 5.1 Source

Conserver une fiche canonique par œuvre ou ressource intellectuelle identifiée, avec ses identifiants externes, éditeur/producteur, titre original, langue, date, type, URL canonique et statut d'accès. Les éditions, versions, traductions, corrigenda et rétractations doivent être liées explicitement sans écraser l'historique.

### 5.2 Événement d'inspection

Évaluer un journal append-only séparé de la fiche bibliographique. Un événement devrait au minimum préciser :
- identifiant stable et identifiant de source ;
- date/heure avec fuseau et acteur ou processus ;
- action effectuée (découverte, accès, téléchargement, extraction, vérification, révision) ;
- version ou empreinte consultée, si disponible et légalement conservable ;
- résultat, limites d'accès, erreurs et prochaine action ;
- références aux artefacts produits.

Ne pas archiver automatiquement des contenus protégés ni conserver des données personnelles non nécessaires. Le journal décrit l'opération et ses résultats, pas une copie intégrale de la source.

### 5.3 Extraction atomique

Une extraction doit pouvoir être revue indépendamment et comporter, lorsque pertinent :
- identifiant, source et version ;
- localisateur stable (page, section, tableau, figure, cellule, variable, URL et date de consultation) ;
- type : citation, transcription, paraphrase fidèle, résultat rapporté, donnée, calcul reproduit ou interprétation ;
- contenu ou valeur, unité, dénominateur, population, période et territoire ;
- méthode/outillage et transformations ;
- limites, ambiguïtés et hypothèses ;
- origine humaine, import ou assistance IA ;
- statut de vérification, date et réviseur.

Les champs conditionnels doivent dépendre du type d'extraction : une citation n'a pas nécessairement d'unité statistique ; une valeur quantitative ne peut pas omettre son unité ou son dénominateur lorsqu'ils sont nécessaires à son interprétation.

### 5.4 Lineage et corroboration

Les liens de provenance doivent distinguer au minimum :
- extrait de / localisé dans ;
- dérivé de / transformé depuis ;
- rapporte le résultat de ;
- soutient, contredit ou qualifie ;
- réutilise le même jeu de données ou programme ;
- corroboration indépendante (à justifier).

Plusieurs publications issues d'un même échantillon, registre ou programme ne sont pas des réplications indépendantes. Le graphe doit rendre cette dépendance visible pour éviter le double comptage des preuves.

### 5.5 Synthèse

Chaque passage substantiel d'une synthèse devrait pouvoir être relié à une ou plusieurs claims, extractions ou sources. La synthèse conserve aussi les décisions éditoriales : éléments retenus, écartés ou nuancés, contradictions, limites, degré de confiance argumenté et date de revue. Une synthèse n'est pas une simple concaténation de résumés.

## 6. Plan d'adoption progressif

| Priorité | Étape | Livrable / preuve de réussite |
|---|---|---|
| P0 | Cartographier les champs et références existants des schémas source, étude, dataset, claim et relation | Matrice champ → schéma → registre → fichiers réels ; aucune migration à l'aveugle |
| P0 | Définir le contrat minimal d'extraction et ses statuts de vérification | Schéma compatible, exemples texte et tableau, tests positifs/négatifs |
| P0 | Tester la chaîne de preuve sur deux cas existants contrastés | Un cas documentaire qualitatif et un cas quantitatif avec unité, population, période, territoire et dénominateur |
| P1 | Prototyper les événements d'inspection append-only | Historique de consultation/version sans écraser la fiche source |
| P1 | Formaliser les relations de lineage et de dépendance des publications | Contrôle des dépendances communes et du double comptage |
| P1 | Relier les passages de synthèse aux preuves | Échantillon de synthèse navigable jusqu'aux localisateurs |
| P2 | Mesurer les performances et l'ergonomie à ×10 puis ×100 | Temps, mémoire, couverture, erreurs et limites documentés |
| P2 | Automatiser la propagation des changements | Simulation d'erratum/rétractation et rapport des objets en aval à revoir |

## 7. Garde-fous de migration

1. Ne pas déplacer massivement les fichiers ni renommer les identifiants.
2. Ne pas rendre immédiatement obligatoires des champs qui ne peuvent pas être renseignés pour les objets historiques ; utiliser des migrations versionnées et explicites.
3. Ne jamais convertir une absence d'information en valeur supposée : employer un statut inconnu/non documenté lorsque le schéma le permet.
4. Préserver les champs et références existants ; toute transformation doit être réversible ou accompagnée d'un rapport de pertes nul.
5. Ne pas confondre date de consultation, date de publication, date de l'événement étudié et date de validité.
6. Ne pas faire d'un score agrégé un substitut à l'examen méthodologique.
7. Ne pas introduire de base de données graphe avant d'avoir identifié des requêtes bloquantes et mesuré les limites de l'architecture actuelle.
8. Les validations automatisées contrôlent des propriétés explicites ; elles ne certifient pas la qualité scientifique d'une conclusion.

## 8. Tests pilotes recommandés

Choisir les cas dans le corpus existant, sans créer de données fictives :
- **Texte qualitatif / institutionnel :** une affirmation dont le localisateur est un passage précis, en séparant déclaration de l'acteur et fait vérifié indépendamment.
- **Résultat quantitatif :** un résultat avec tableau ou dataset, unité, population, période, territoire, dénominateur et méthode de calcul.
- **Versions / dépendances :** deux publications ou rapports réutilisant une même source de données, afin de tester le non-double-comptage.
- **Correction :** une version corrigée ou un erratum simulé dans les tests, pour vérifier que les objets en aval sont signalés sans réécriture automatique des conclusions.

Critère de passage : les humains peuvent remonter de la synthèse à l'élément source et comprendre ce qui a été rapporté, transformé, interprété et vérifié.

## 9. Prochaines décisions dans l'issue #114

- Auditer d'abord les schémas et usages réels avant de choisir les nouveaux fichiers ou champs.
- Sélectionner les deux pilotes et établir leur chaîne de preuve complète.
- Décider ensuite si les événements d'inspection et les extractions méritent des registres dédiés, sur la base des pilotes.
- Définir les contrôles de lineage, de dépendance des publications et de propagation des corrections.
- Conserver cette revue comme document de cadrage ; les changements de schémas et de code devront faire l'objet de PR séparées, testées en CI.
