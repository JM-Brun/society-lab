# Métadonnées, nomenclature et organisation

## Source de vérité
Les fiches structurées vivent dans le dépôt. Les pages Quarto, index, graphes et tableaux de bord sont des vues générées. Ne jamais modifier une vue générée à la main.

## Identifiants
Format `TYPE-SUJET-DISTINCTIF`, ASCII majuscule, mots séparés par des tirets. Types : DOMAIN, CONCEPT, MECHANISM, ORG, SOURCE, STUDY, DATASET, CLAIM, HYPOTHESIS, ANALYSIS, METHOD, DOSSIER, TAG et REL. L'identifiant est stable, sémantique mais pas surchargé : pas de date volatile, de jugement, de statut ou de numéro séquentiel sans sens. Ne jamais réattribuer un identifiant supprimé.

## Métadonnées communes
Selon le type, privilégier :
- `id` : identifiant stable obligatoire ;
- `title` / `label` : libellé humain ;
- `description` / `summary` : définition concise ;
- `domains` ou `domain_ids` : rattachement à la taxonomie ;
- `tags` : angles transversaux contrôlés ;
- `created_at`, `updated_at`, `reviewed_at` : dates ISO ;
- `status` / `review_status` : cycle de vie ;
- `source_ids`, `study_ids`, etc. : références typées ;
- `language` : langue BCP 47 lorsque connue ;
- `provenance` : origine et transformations.

Les schémas propres à chaque objet font autorité ; ne pas forcer tous les champs sur tous les types.

## Domaines, tags et mots-clés
- Domaine : sujet principal stable, via TAXONOMY.yml.
- Tag : dimension transversale contrôlée, via TAGS.yml.
- Mot-clé libre : exceptionnel, pour recherche temporaire ; ne remplace ni domaine ni tag.
- Une fiche peut avoir plusieurs domaines si son objet est réellement transversal ; limiter les tags au strict utile.

## Nommage des fichiers
Fichiers en minuscules kebab-case, un objet par fichier dans les répertoires dédiés : `study-id.yml`, `concept-id.yml`. Les registres servent d'index, pas de stockage de fiches volumineuses. Les identifiants dans le contenu restent la référence, pas le nom de fichier.

## Dates et chiffres
Dates calendaires ISO 8601 (`YYYY-MM-DD`), horodatages avec fuseau. Toujours documenter unités, base de prix, année de référence, population, dénominateur et périmètre géographique pour les indicateurs quantitatifs.

## Langues
Contenu éditorial principalement français. Conserver titre original, langue originale et traduction éventuelle ; ne pas faire passer une traduction libre pour le titre source.

## Historique
Toute modification substantielle d'une fiche doit laisser une trace Git et, si elle change une conclusion ou une interprétation, une note de révision.
