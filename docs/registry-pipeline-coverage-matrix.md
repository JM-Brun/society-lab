# Matrice de couverture des propriétés — Source, Study, Dataset, Claim

**Statut : proposition de règles par étape, à valider humainement.** Cette matrice ne modifie pas les schémas JSON et n'autorise aucune migration de masse. Les exigences « R » sont des critères de passage proposés, non des obligations actuellement imposées par les validateurs.

## Légende et étapes

- **R** : requis pour franchir l'étape.
- **C** : requis si la condition indiquée s'applique.
- **O** : facultatif, utile selon le contexte.
- **—** : non pertinent.

Étapes : **D** découverte ; **Q** qualification ; **E** extraction ; **A** analyse ; **V** vérification d'un claim ; **P** publication.

## Source

| Propriété | D | Q | E | A | V | P | Règle |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| `id`, `title`, `source_type`, `language` | R | R | R | R | R | R | Identité et nature de la source |
| `url` | C | C | C | C | C | C | Requis si une URL stable existe ; sinon noter l'absence |
| `organization`, `authors` | O | C | C | C | C | C | Émetteur/auteurs lorsqu'ils sont identifiables |
| `publication_date`, `updated_date` | O | C | C | C | C | C | Précision réellement disponible, sans inférence |
| `domains`, `geographic_scope`, `temporal_scope` | O | C | C | C | C | C | Requis si la portée affecte la pertinence |
| `methodology` | — | C | C | C | C | C | Requis pour une source empirique, statistique ou évaluative |
| `limitations` | — | C | C | R | R | R | Limites connues avant interprétation |
| `access_status` | O | R | R | R | R | R | Conditionne la possibilité d'accès |
| `license` | — | C | C | C | C | C | Requis avant réutilisation/redistribution ; inconnue explicitement conservée |
| `doi`, `funding_and_conflicts`, `tags`, `notes` | O | O | O | O | O | O | Selon disponibilité et pertinence |

## Study

| Propriété | D | Q | E | A | V | P | Règle |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| `id`, `title`, `study_type`, `source_ids`, `domains` | R | R | R | R | R | R | Identité, méthode générale, provenance et domaine |
| `review_status` | O | R | R | R | R | R | État du contrôle documentaire/méthodologique |
| `research_question` | — | C | C | R | R | R | Question effectivement étudiée |
| `methods` | — | C | R | R | R | R | Méthodes indispensables à l'interprétation |
| `population_or_unit` | — | C | R | R | R | R | Population et unité d'analyse |
| `geographic_scope`, `temporal_scope` | — | C | R | R | R | R | Champ géographique et période |
| `dataset_ids` | — | C | C | C | C | C | Requis si un dataset canonique est exploité |
| `key_findings` | — | — | C | R | R | R | Résultats rapportés, séparés des interprétations |
| `limitations` | — | C | C | R | R | R | Biais, validité externe, précision et données manquantes |
| `authors`, `organization`, `publication_date`, `funding_and_conflicts`, `review_notes`, `tags` | O | O | O | O | O | O | Selon disponibilité et pertinence |

## Dataset

| Propriété | D | Q | E | A | V | P | Règle |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| `id`, `title`, `provider`, `domains`, `access_status` | R | R | R | R | R | R | Identification, producteur, domaine, accès |
| `source_ids` | O | C | C | C | C | C | Requis si une documentation/source officielle est identifiée |
| `url`, `doi` | O | C | C | C | C | C | Localisateur stable lorsqu'il existe |
| `geographic_scope`, `temporal_coverage` | — | C | R | R | R | R | Champ réel du jeu de données |
| `unit_of_observation` | — | C | R | R | R | R | Individu, établissement, emploi, ménage, agrégat, etc. |
| `variables` | — | C | R | R | R | R | Variables disponibles et utilisées |
| `version_or_vintage` | — | C | R | R | R | R | Millésime/version pour reproductibilité |
| `license` | — | C | C | C | C | C | À qualifier avant réutilisation ou diffusion |
| `retrieved_at` | — | — | C | C | C | C | Requis si une copie a effectivement été récupérée |
| `file_hash` | — | — | C | C | C | C | Requis pour un artefact local figé, pas pour un accès distant sans copie |
| `transformation_notes` | — | — | C | R | R | R | Filtres, recodages, exclusions et calculs réellement appliqués |
| `limitations` | — | C | R | R | R | R | Couverture, pondérations, ruptures, non-réponse, confidentialité |
| `tags` | O | O | O | O | O | O | Navigation |

## Claim

| Propriété | D | Q | E | A | V | P | Règle |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| `id`, `statement`, `claim_type`, `status` | R | R | R | R | R | R | Proposition atomique, type logique et état épistémique |
| `scope` | — | C | C | R | R | R | Population, géographie, période et conditions de validité |
| `domain_ids` | O | C | C | C | C | C | Classification |
| `source_ids` / `study_ids` | — | C | C | C | R | R | Au moins une référence probante pour un claim factuel publié |
| `supporting_evidence` | — | — | C | C | R | R | Éléments soutenant précisément la proposition et localisateurs |
| `counter_evidence`, `best_counterargument` | — | — | O | C | R | R | Éléments contraires et meilleur contre-argument loyal |
| `assumptions`, `limitations` | — | — | O | R | R | R | Hypothèses et limites d'inférence |
| `source_verifications` | — | — | C | C | R | R | Vérification des sources mobilisées, statut et localisateur |
| `confidence` | — | — | — | C | C | C | Seulement si probabilité calibrée et justification ; pas un score de qualité |
| `provenance` | — | C | C | C | C | R | Distinguer rédaction humaine, extraction, suggestion IA et dérivation |
| `revision_triggers`, `revision_history`, `last_reviewed` | — | — | — | O | C | C | Maintenance et historique |
| `normative_criteria` | — | — | — | C | C | C | Requis si claim ou implications normatives |
| `hypothesis_ids`, `tags` | O | O | O | O | O | O | Selon pertinence |

## Constats issus de l'inventaire automatisé du 19 novembre 2026

Le rapport exécuté par CI porte sur **220 Source, 62 Study, 14 Dataset et 83 Claim**. Les champs requis par les schémas sont présents dans toutes les fiches au niveau de présence de premier niveau ; aucune propriété observée hors schéma n'a été détectée.

| Signal | Source | Study | Dataset | Claim | Lecture prudente |
|---|---:|---:|---:|---:|---|
| Auteurs | 46/220 | 8/62 | — | — | Ne pas exiger si auteurs absents ou institutionnels |
| Date de publication | 154/220 | 44/62 | — | — | Dates manquantes à qualifier, pas à inventer |
| Licence | 1/220 | — | 12/14 | — | Lacune importante pour réutilisation ; distinguer inconnue, non applicable et non vérifiée |
| Méthodologie / méthodes | 220/220 | 62/62 | — | — | Présence élevée, qualité sémantique non évaluée |
| Population/unité d'observation | — | 62/62 | 14/14 | — | Présence, précision et compatibilité non vérifiées |
| Variables | — | — | 14/14 | — | Présence ne garantit pas un dictionnaire opérationnel |
| Source verifications | — | — | — | 28/83 | À examiner selon les sources réellement mobilisées |
| Provenance | — | — | — | 26/83 | À prioriser pour les claims publiables |
| Éléments contraires | — | — | — | 1/83 | À traiter à l'étape de vérification, pas dès la découverte |
| Contre-argument | — | — | — | 15/83 | Pertinent selon le type et la controverse du claim |
| Confidence | — | — | — | 0/83 | Ne pas généraliser l'exigence ; champ facultatif et exigeant |

**Attention au comptage des fichiers :** les répertoires Source et Claim contiennent respectivement 3 et 25 fichiers YAML ; ce total inclut le registre et peut inclure des lots/fichiers auxiliaires. Il ne correspond pas au nombre de fiches canoniques (220 et 83).

## Règles transversales

1. La présence d'un champ ne prouve ni son exactitude ni son adéquation probatoire.
2. Une propriété conditionnelle ne devient pas une obligation globale.
3. Les inconnues (date, licence, accès, population) restent explicitement inconnues ; aucune valeur n'est inventée.
4. Accès et licence sont distincts : accès ouvert ne signifie pas réutilisation libre.
5. Pour une extraction, préserver valeur, unité, dénominateur, population, période, géographie, définition et méthode.
6. Un claim causal exige une stratégie d'identification, ses hypothèses, ses alternatives et ses limites ; un claim normatif explicite ses critères de valeur.
7. Distinguer valeur publiée, valeur extraite et valeur recalculée.
8. Aucune migration en masse avant revue des fiches représentatives et des conditions de passage.

## Décisions à valider avant évolution des validateurs

| Sujet | Proposition | Statut |
|---|---|---|
| Profils de maturité | `discovered`, `qualified`, `extracted`, `analyzed`, `claim_checked`, `publishable` | À valider |
| Règles par étape | Validateur de profil séparé des schémas canoniques au départ | À valider |
| Claim factuel publiable | Référence(s) probante(s) et vérification explicite des sources mobilisées | À valider |
| Claim causal | Méthode d'identification, hypothèses, portée et limites adaptées | À valider |
| Hash dataset | Obligatoire seulement pour artefact récupéré et figé | À valider |
| Licences/dates inconnues | Statut inconnu conservé, jamais complété par inférence | À valider |

## Suite

1. Comparer cette matrice au rapport d'inventaire généré par CI.
2. Examiner des fiches représentatives : une par registre, plus un claim multi-sources.
3. Classer chaque écart : donnée manquante, non pertinent, inconnu/inaccessible, imprécis, règle de validation absente.
4. Valider les exigences conditionnelles avec revue humaine.
5. Seulement ensuite, proposer des validateurs d'étape ou une migration ciblée.
