# Manifestes d'ingestion

Chaque fichier de ce répertoire décrit un lot borné de découverte et de sélection de sources. Il conserve les décisions prises, y compris les doublons, exclusions, reports et sources inaccessibles.

- Un manifeste correspond à une recherche ou opération d'acquisition cohérente, avec un périmètre et des critères explicites.
- Une candidate est identifiée par un identifiant local au lot ; une source retenue reçoit un `SOURCE-*` canonique dans `sources/registry.yml`.
- Les candidates rejetées ou reportées restent dans le manifeste : ne pas les transformer en fiches sources artificielles.
- Les doublons pointent vers une autre candidate du lot ou vers un `SOURCE-*` existant.
- Les nombres de candidates retenues, rejetées ou dupliquées sont calculables depuis les décisions ; ne pas les recopier manuellement dans un compteur susceptible de diverger.
- Le manifeste ne contient ni copie de document tiers, ni donnée personnelle inutile, ni secret.
- Les corrections passent par Git ; ne pas réécrire l'historique des décisions sans explication.

Le contrat est défini par [`schemas/ingestion-batch.schema.json`](../../schemas/ingestion-batch.schema.json), avec un [modèle à copier](../../templates/ingestion-batch.yml). Les manifestes sont validés par la CI.
