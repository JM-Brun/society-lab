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
