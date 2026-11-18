# Protocole d'ingestion des sources

## Principe
L'ingestion transforme une ressource repérée en objet documenté, vérifiable et réutilisable. Elle ne vaut ni validation scientifique ni approbation de ses conclusions.

## Pipeline
1. **Découverte** — consigner URL, date de découverte, contexte et raison de sélection.
2. **Déduplication** — comparer DOI, URL canonique, titre, auteurs, organisme et version ; relier les versions sans les confondre.
3. **Identification** — attribuer un SOURCE-* stable ; identifier l'éditeur, auteurs, date, langue, type et périmètre.
4. **Accès et droits** — noter accès, licence, conditions de réutilisation ; ne pas archiver un PDF tiers par défaut.
5. **Qualification initiale** — noter nature primaire/secondaire, méthode annoncée, financement et conflits connus, sans inférer la qualité depuis la réputation.
6. **Extraction** — séparer résumé fidèle, résultats rapportés, affirmations candidates, limites déclarées et questions non résolues. Chaque extraction importante doit pointer vers page, tableau, figure, section ou URL.
7. **Mise en relation** — relier domaines, tags, études, datasets, claims, concepts et dossiers uniquement lorsque le lien est justifié.
8. **Revue** — attribuer un statut explicite ; les points non vérifiés restent non vérifiés.
9. **Publication éventuelle** — une source n'apparaît dans une conclusion publique qu'après examen adapté à l'enjeu.
10. **Maintenance** — surveiller errata, nouvelles versions, rétractations, mises à jour et changements d'URL.

## Statuts recommandés
discovered → metadata_complete → screened → reviewed → used → superseded / retracted. Ces statuts décrivent le traitement interne, pas une note de qualité.

## Fiche d'extraction minimale
- Question à laquelle la source pourrait contribuer
- Référence bibliographique et URL/DOI
- Type de source et provenance
- Méthode, échantillon/unité, période, périmètre
- Résultats exacts et localisation dans le document
- Limites, biais possibles, financement et conflits
- Ce que la source ne permet pas de conclure
- Affirmations candidates et relations proposées
- Niveau de vérification et nom/date de revue

## Règles de prudence
- Ne jamais transformer une corrélation en causalité.
- Ne jamais généraliser au-delà de la population, période ou géographie étudiée.
- Distinguer absence de preuve et preuve d'absence.
- Ne pas compter plusieurs reprises d'une même étude comme confirmations indépendantes.
- Pour les méta-analyses, examiner hétérogénéité, biais de publication et qualité des études incluses.
- Une source institutionnelle peut être primaire sur ses propres données et intéressée sur leur interprétation.
- Toute extraction par IA est une proposition à vérifier sur la source originale.

## Lots d'ingestion
Pour une ingestion en lot, conserver le manifeste du lot : date, requête ou origine, critères d'inclusion/exclusion, nombre examiné, nombre retenu, doublons et motifs de rejet. Ne pas créer artificiellement une fiche complète si les métadonnées sont inconnues.

## Contrat opérationnel des lots

Un lot correspond à une opération de découverte et de sélection bornée : une requête, un catalogue, une campagne de collecte ou un périmètre de recherche. Il ne correspond ni à un sujet de recherche entier ni à une validation scientifique.

Le contrat de données est défini dans [`schemas/ingestion-batch.schema.json`](../schemas/ingestion-batch.schema.json). Copier [le modèle de manifeste](../templates/ingestion-batch.yml) dans `sources/batches/` et le compléter. Les manifestes sont contrôlés par `scripts/validate/validate_registry.py`.

### États du lot et décisions sur les candidates

- `open` : découverte en cours ; des candidates peuvent encore être ajoutées.
- `screening` : les critères d'inclusion/exclusion sont appliqués.
- `review` : les candidates retenues sont en cours d'identification et de qualification.
- `closed` : toutes les candidates ont une décision finale ; aucune ne reste `deferred`.

Chaque candidate reçoit une décision :
- `selected` : elle correspond aux critères et possède un `SOURCE-*` canonique existant ;
- `duplicate` : elle pointe vers une autre candidate du lot ou une source canonique ;
- `excluded` : le motif d'exclusion est consigné ;
- `deferred` : la décision est reportée avec une raison ;
- `inaccessible` : l'accès est impossible ou limité, avec le statut d'accès et le motif.

Les identifiants de candidates sont locaux au manifeste. Ils ne remplacent jamais les identifiants canoniques `SOURCE-*`. Les doublons ne sont pas supprimés de l'historique : ils sont conservés comme décisions reliées à la source retenue. Un même `SOURCE-*` ne doit pas être sélectionné deux fois dans un même lot.

### Règles de clôture et de reprise

1. Créer le manifeste avant ou au début de la collecte ; ne pas reconstruire les critères après avoir vu les résultats sans le signaler.
2. Conserver la requête, le catalogue ou l'origine précise, la date et les critères d'inclusion/exclusion.
3. Enregistrer les candidates examinées, pas seulement les sources retenues.
4. Résoudre les doublons vers une candidate ou une source canonique ; éviter les chaînes cycliques de doublons.
5. Une candidate reportée garde son statut tant que l'information manque ; un lot ne peut être clos avec des candidates reportées.
6. Une source sélectionnée doit déjà exister dans le registre canonique. Créer ou mettre à jour sa fiche dans une modification traçable avant de clôturer le lot.
7. Les nombres de retenues, rejets et doublons sont calculés à partir des décisions, pas saisis manuellement.
8. Une correction ultérieure du manifeste passe par Git et explique le changement de décision.

Les manifestes ne doivent pas contenir les documents sources eux-mêmes, de données personnelles inutiles ou de secrets. Les droits et les modalités d'archivage restent régis par la [politique des sources](source-policy.md) et la [politique de licences](licensing.md).

### Ce que le manifeste ne prouve pas

La décision `selected` signifie uniquement que la candidate a été retenue pour traitement. Elle ne signifie ni que la source est fiable, ni que sa méthode est robuste, ni que ses résultats sont vérifiés, ni qu'elle soutient une conclusion. Ces évaluations interviennent dans les fiches Source, Study, Dataset et Claim, puis dans les relations justifiées du graphe.


## Traçabilité fine des extractions associées aux claims

Une vérification de source et une extraction sont deux opérations distinctes :
- `source_verifications[*].status` indique jusqu'où le passage a été contrôlé ;
- `source_verifications[*].locator` localise le passage ou l'objet (page, section, tableau, figure, horodatage, champ de dataset ou fragment d'URL) ;
- `source_verifications[*].extraction` décrit ce qui a été extrait et comment, sans transformer automatiquement l'extraction en conclusion validée.

L'objet `extraction` est facultatif pour préserver la compatibilité avec les claims existants. Lorsqu'il est utilisé, il distingue la nature de l'élément, le contenu ou la valeur rapportée, son unité, son dénominateur, sa population, sa période, sa géographie, sa définition opérationnelle, la méthode d'extraction, sa version éventuelle, les transformations, la date et l'auteur de l'extraction ainsi qu'une empreinte SHA-256 facultative d'un artefact conservé légalement.

### Règles d'interprétation

1. Conserver le localisateur au niveau de la vérification, même si l'extraction structurée est absente.
2. Ne pas confondre `reported_result` (résultat rapporté par l'auteur) et `recalculation` (résultat recalculé par Society Lab). Documenter formule, filtres et dénominateurs pour les recalculs.
3. Un extrait textuel est limité à 500 caractères dans le schéma ; privilégier le localisateur et la paraphrase plutôt que la reproduction d'un contenu protégé.
4. Une empreinte identifie un artefact, elle ne prouve ni son authenticité ni les droits de le conserver.
5. Une extraction `model_assisted` reste une proposition jusqu'au contrôle humain sur la source originale. Le statut de vérification ne doit jamais être déduit automatiquement de la méthode.
6. Les champs de population, période, géographie, unité et dénominateur sont renseignés lorsqu'ils conditionnent l'interprétation ; ne pas inventer une valeur absente.
7. L'interprétation éditoriale, la synthèse et le statut du claim restent distincts de l'extraction brute.

Ce contrat est une extension facultative de `schemas/claim.schema.json`, pas un nouveau registre ni un système de preuve parallèle. Les migrations doivent être faites claim par claim après retour à la source ; ne pas remplir les fiches en bloc à partir de leurs formulations actuelles.
