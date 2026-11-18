---
id: "CROSS-DOMAIN-KNOWLEDGE-FRAMEWORK"
title: "Cadre de lecture transversale des connaissances"
status: "working_baseline"
last_reviewed: "2026-11-18"
related_issue: 112
---

# Cadre de lecture transversale des connaissances

## 1. Finalité

Society Lab ne doit pas seulement juxtaposer des dossiers thématiques. Il doit permettre de retrouver les mécanismes communs, de comparer leurs manifestations selon les contextes et d'examiner comment les transformations d'un domaine affectent les autres.

La lecture transversale est une **couche de navigation et d'analyse construite à partir des registres canoniques**. Elle ne constitue ni un second graphe, ni une taxonomie concurrente, ni un nouveau parcours d'apprentissage. Les sources, études, claims, hypothèses, concepts, mécanismes, dossiers et synthèses existants restent les objets de référence.

La transversalité ne consiste pas à relier artificiellement tous les sujets. Un lien n'est conservé que s'il apporte une information utile et si sa nature est explicite.

## 2. Les niveaux de relation à ne pas confondre

| Niveau | Question | Ce que le lien autorise à dire |
|---|---|---|
| Proximité thématique | Les sujets portent-ils sur un même enjeu général ? | Ils peuvent être explorés ensemble ; aucune influence n'est établie. |
| Concept ou mécanisme commun | Mobilisent-ils un concept ou mécanisme comparable ? | Le mécanisme fournit une grille de comparaison ; ses effets peuvent différer. |
| Contexte ou condition | L'un modifie-t-il les conditions dans lesquelles l'autre agit ? | Une condition de validité ou un facteur de contexte est identifié. |
| Association empirique | Les variables évoluent-elles ensemble dans les données ? | Une association est observée dans un périmètre donné ; causalité non établie. |
| Influence causale documentée | Des travaux identifient-ils un effet directionnel ? | Une relation causale peut être discutée dans les limites de la méthode et du contexte. |
| Rétroaction / interdépendance | Les effets se répondent-ils dans le temps ? | Une boucle ou une dépendance réciproque peut être décrite si chaque canal est étayé. |
| Arbitrage / transfert | Un choix déplace-t-il coûts, bénéfices ou risques entre acteurs ? | Les transferts et leurs bénéficiaires sont identifiés ; le jugement normatif reste séparé. |
| Comparaison | Deux dispositifs ou contextes sont-ils comparables ? | Les ressemblances et différences sont discutées après harmonisation des définitions. |

Un tag partagé, une présence dans le même domaine ou une intuition de bon sens ne suffisent jamais à créer une relation d'influence.

## 3. Métadonnées attendues pour une relation transversale

Les relations de connaissance restent enregistrées dans `knowledge/graph.yml`. Lorsqu'une relation dépasse la simple organisation, sa justification doit, selon le cas, rendre explicites :

- **mécanisme** : chaîne explicative proposée, avec étapes intermédiaires ;
- **direction** : origine, destination, ou réciprocité explicitement décomposée ;
- **statut épistémique** : établi dans un périmètre, résultat convergent, résultat hétérogène, association descriptive, hypothèse, controverse ou lien rejeté ;
- **portée** : population, secteur, territoire, institution et période ;
- **temporalité** : délai d'apparition, horizon court/moyen/long et éventuels effets différés ;
- **conditions** : institutions, conjoncture, règles, ressources et hypothèses dont dépend le mécanisme ;
- **preuves** : identifiants des sources, études, jeux de données et claims pertinents ;
- **limites** : identification, qualité des données, validité externe, incertitudes et explications alternatives ;
- **révision** : date de dernière vérification et raison d'une éventuelle révision.

Ne pas ajouter mécaniquement tous ces champs à chaque arête si le schéma actuel ne les accepte pas. Tant que l'ontologie n'est pas étendue et validée, conserver ces informations dans la justification et les fiches concernées. L'évolution du schéma relève de l'issue #112.

Les relations causales réciproques doivent être décomposées en deux canaux directionnels et, si nécessaire, en une boucle temporelle. Une arête symétrique « influence mutuelle » masquerait le sens et la séquence des mécanismes.


### 3.1. Fiches de mécanismes : contrat minimal et garde-fous

L'audit du dépôt au 18 novembre 2026 a confirmé que le type `MECHANISM` est autorisé dans les relations, mais qu'aucun registre canonique de fiches de mécanismes n'est encore présent dans `knowledge/`. Le schéma [`mechanism.schema.json`](../schemas/mechanism.schema.json) propose un contrat minimal pour ces fiches : identifiant stable, description, domaines, étapes, direction, conditions de portée, acteurs, indicateurs, horizon, études/claims favorables ou critiques, explications alternatives, limites, statut et date de revue.

Ce schéma est une **proposition de structure**, pas une validation automatique du contenu ni une preuve de causalité. Les statuts distinguent notamment :
- `candidate` : piste de mécanisme à examiner ;
- `theoretical` : chaîne cohérente sur le plan théorique, sans validation empirique suffisante ;
- `descriptive` : canal observé ou décrit, sans identification causale ;
- `supported_in_scope` : mécanisme soutenu dans un périmètre précis ;
- `mixed_evidence` / `challenged` : résultats hétérogènes ou éléments critiques ;
- `rejected_in_scope` / `retired` : mécanisme rejeté dans le périmètre étudié ou fiche retirée.

**Ne pas créer de registre de mécanismes ni de nœuds `MECHANISM` dans le graphe avant d'avoir ajouté le contrôle de schéma, défini l'emplacement canonique du registre et vérifié les références croisées.** Une fiche de mécanisme ne doit pas être créée pour chaque flèche d'un schéma conceptuel : elle doit décrire un canal explicatif réutilisable, suffisamment distinct et documenté.

## 4. Exemple pilote : l'économie comme système d'interactions

Le domaine économique est un bon terrain pilote parce que plusieurs dossiers existants étudient des parties différentes d'un même système : salaire minimum, formation, transition énergétique, finances publiques, emploi, productivité et trajectoires intergénérationnelles.

### 4.1 Carte des mécanismes à examiner

| Dossiers / domaines mis en relation | Mécanismes communs ou canaux possibles | Ce que la confrontation peut éclairer | Statut initial |
|---|---|---|---|
| SMIC ↔ éducation | Qualification, segmentation du marché du travail, progression salariale, mobilité, rendement privé et collectif de la formation | Dans quelles conditions les compétences protègent-elles de la compression salariale ou facilitent-elles les transitions ? | Questions de recherche ; ne pas présumer d'un effet uniforme du diplôme. |
| SMIC ↔ énergie et transition | Prix de l'énergie, intensité énergétique, marges, prix de vente, coût du travail, investissement et exposition sectorielle | Comment les chocs énergétiques et les hausses salariales interagissent-ils selon les secteurs et la capacité de répercussion des coûts ? | Mécanismes plausibles à documenter par secteur et période. |
| Éducation ↔ transition énergétique | Besoins de compétences, formation initiale et continue, reconversion, géographie des emplois et délais d'ajustement | Les compétences disponibles correspondent-elles aux métiers et territoires où les investissements sont prévus ? | Hypothèse de décalage offre/besoins à tester avec les données existantes. |
| TIG ↔ économie et emploi | Capacité des structures d'accueil, tutorat, insertion, coûts d'opportunité, articulation avec l'activité rémunérée | Dans quelles conditions une mesure en milieu ouvert soutient-elle l'insertion sans se substituer à un emploi ? | Question conditionnelle ; distinguer objectif pénal, activité et résultat d'insertion. |
| Pacte intergénérationnel ↔ économie, énergie et éducation | Transferts entre générations, dette, patrimoine, investissement, capital humain, actifs collectifs et externalités de long terme | Qui finance aujourd'hui les investissements dont les bénéfices ou coûts se matérialisent plus tard ? | Cadre de comparaison ; arbitrages normatifs à rendre explicites. |

Cette matrice ne constitue pas une validation empirique des liens. Elle indique où rechercher les résultats existants, quelles variables harmoniser et quelles explications concurrentes examiner.

### 4.2 Exemple de chaîne causale à documenter : transition énergétique et salaires

Une chaîne possible, à ne pas présenter comme démontrée sans études adaptées :

1. Une variation des prix de l'énergie modifie les coûts des entreprises selon leur intensité énergétique et leurs contrats.
2. Les entreprises ajustent, dans des proportions variables, leurs prix, marges, investissements, organisation, volumes ou emploi.
3. Les effets peuvent modifier les besoins de compétences et la demande de travail selon les secteurs.
4. Les tensions de recrutement, la productivité et la négociation salariale peuvent influencer la diffusion des salaires.
5. Les hausses de rémunération et les politiques de compensation peuvent à leur tour modifier les coûts et le revenu disponible des ménages.
6. Les comportements de consommation, d'investissement et de mobilité peuvent rétroagir sur la demande énergétique.

Pour chaque étape, il faut identifier les travaux qui mesurent effectivement le canal, la population et l'horizon étudiés. L'existence d'une chaîne théorique cohérente ne prouve ni l'ampleur ni le signe net de l'effet.

## 5. Comment produire une synthèse transversale utile

Une synthèse transversale n'est justifiée que si elle répond à une question qui traverse plusieurs dossiers et apporte un éclairage supplémentaire.

Structure recommandée :

1. **Question commune** — problème précis, domaines et périmètre.
2. **Ce que chaque dossier apporte** — résultats déjà établis, sans les recopier intégralement.
3. **Mécanismes partagés** — définitions communes et différences de contexte.
4. **Relations documentées** — résultats empiriques, méthodes, populations et limites.
5. **Relations incertaines** — hypothèses, controverses, explications alternatives et données manquantes.
6. **Effets distributifs** — acteurs gagnants/perdants, transferts et temporalités.
7. **Bilan intégré** — ce que l'on comprend mieux en croisant les domaines, et ce qui reste indécidable.
8. **Conséquences pour les dossiers sources** — mises à jour ciblées des synthèses thématiques et du graphe.

La synthèse transversale renvoie aux synthèses thématiques canoniques ; elle ne crée pas de seconde version de leurs conclusions.

## 6. Procédure à chaque nouvelle ingestion

Pour chaque nouvelle source, étude ou dossier :

1. Identifier les domaines concernés sans multiplier les rattachements artificiels.
2. Rechercher les concepts, mécanismes, acteurs, indicateurs et relations déjà enregistrés.
3. Réutiliser les identifiants existants ; proposer une nouvelle fiche uniquement si le concept est réellement distinct.
4. Examiner les dossiers d'autres domaines susceptibles d'être éclairés par le nouveau contenu.
5. Distinguer la relation directement documentée de la piste de rapprochement.
6. Mettre à jour le graphe seulement si la relation est justifiée ; conserver les incertitudes.
7. Actualiser les synthèses concernées si le bilan change matériellement.
8. Signaler les relations candidates non retenues ou reportées lorsqu'elles risquent d'être prises à tort pour des résultats.
9. Mettre à jour les dates de revue et les références croisées.

## 7. Contrôles de qualité

Une revue transversale doit vérifier :

- absence de doublons de concepts et d'identifiants ;
- cohérence entre taxonomie, tags, fiches et relations ;
- absence d'arêtes probantes sans source identifiable ;
- distinction entre relation organisationnelle et relation épistémique ;
- présence des dénominateurs, périodes, populations et périmètres pour les comparaisons quantitatives ;
- absence de généralisation abusive d'un secteur, territoire ou horizon à l'ensemble de l'économie ;
- conservation des résultats contradictoires et des explications alternatives ;
- traçabilité des changements de conclusion dans Git ;
- cohérence entre dossier, synthèse, registre et graphe.

## 8. Articulation avec l'architecture existante

- `knowledge/graph.yml` reste le registre des relations.
- `knowledge/RELATION_TYPES.yml` reste l'ontologie des relations autorisées.
- `knowledge/TAXONOMY.yml` reste la taxonomie des domaines.
- `knowledge/TAGS.yml` reste le vocabulaire contrôlé des dimensions transversales.
- `knowledge/concepts/registry.yml` et les registres spécialisés restent les sources de vérité des objets.
- `syntheses/registry.yml` conserve la correspondance entre dossiers principaux et synthèses.
- Les pages de domaine restent les points d'entrée thématiques ; la future vue transversale doit être dérivée de ces registres.

Aucune base externe, aucun graphe universel et aucune synchronisation automatique inter-dépôts ne sont introduits par ce cadre.

## 9. Inventaire du corpus et cas d'étude

L'[inventaire initial des connaissances et des rapprochements inter-domaines](cross-domain-knowledge-inventory.md) documente l'état du graphe, les concepts déjà disponibles, les chaînes candidates et les limites de preuve au 18 novembre 2026. Il complète ce cadre sans créer de registre concurrent.

## 10. Travaux restant à mener

Le programme opérationnel, les cas d'étude, les critères d'acceptation et leur articulation avec les issues existantes sont suivis dans [l'issue #112](https://github.com/JM-Brun/society-lab/issues/112). Les prochaines étapes sont l'inventaire dédoublonné des concepts et mécanismes, l'examen des relations candidates dans les dossiers existants, puis une première cartographie économique sourcée.
