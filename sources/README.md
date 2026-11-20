# Sources

- `registry.yml` : registre canonique des métadonnées des sources. Il contient actuellement les fiches structurées ; il ne s'agit donc pas encore d'un simple index léger.
- `records/` : emplacement prévu pour les fiches individuelles lorsque le découpage sera justifié par le volume ou les conflits de contribution. Le registre devra alors devenir un index de référence sans dupliquer les métadonnées.
- `batches/` : manifestes des opérations de découverte, de sélection et de déduplication ; voir [leur contrat](batches/README.md).
- [`lifecycle.yml`](lifecycle.yml) contient les événements et décisions de revue concernant les sources déjà identifiées. Voir le [mode opératoire](../docs/source-impact-tracing.md#journal-des-événements-et-des-décisions).

Une entrée de registre n'est pas une validation scientifique de la source. Voir le [protocole d'ingestion](../docs/ingestion-protocol.md) et la [politique des sources](../docs/source-policy.md).
