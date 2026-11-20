# Traçage d’impact des modifications de sources

Le script `scripts/analysis/trace_knowledge_impact.py` aide à identifier les objets du dépôt à revoir lorsqu'une source canonique change (nouvelle version, erratum, retrait, rétractation ou correction).

## Utilisation

Depuis la racine du dépôt :

```bash
python scripts/analysis/trace_knowledge_impact.py --source-id SOURCE-EXAMPLE
python scripts/analysis/trace_knowledge_impact.py --source-id SOURCE-EXAMPLE --format json

# Pilote TIG : rapport Cour des comptes 2025
python scripts/analysis/trace_knowledge_impact.py \
  --source-id SOURCE-COUR-DES-COMPTES-PEINES-ALTERNATIVES-2025

# Pilote Parcoursup : bilan ministériel 2026
python scripts/analysis/trace_knowledge_impact.py \
  --source-id SOURCE-PARCOURSUP-BILAN-2026
```

Le test d'intégration du pilote TIG vérifie dans les registres réels que la source Cour des comptes rejoint notamment le claim `CLAIM-TIG-EXECUTION-DELAY-2025`, le dossier TIG et sa synthèse `syntheses/tig-france.md`. Ce test complète les tests unitaires synthétiques : il vérifie un chemin réellement présent, mais ne démontre pas l'exhaustivité de toutes les dépendances du dépôt.

Le script retourne les études et jeux de données qui référencent directement la source, les claims qui la référencent directement ou via une étude ou un dataset, les hypothèses liées aux études, les mécanismes et prévisions explicitement liés, les dossiers qui référencent ces objets et les synthèses associées dans `syntheses/registry.yml`.

## Comparaison de deux révisions Git

```bash
python scripts/analysis/trace_knowledge_impact.py --base origin/main --revision HEAD
python scripts/analysis/trace_knowledge_impact.py --base origin/main --format json
```

Le mode `--base` compare les fiches de `sources/registry.yml` par identifiant, à partir de deux commits. Il signale les ajouts, retraits et modifications et indique les champs modifiés. L'ordre des fiches, l'ordre des clés YAML et les changements de mise en forme sont ignorés. L'ordre à l'intérieur d'un champ liste est pris en compte, par exemple pour les auteurs.

Le traceur examine les dépendances dans chaque révision où la source existe. Pour un retrait, le rapport conserve les liens de la base. Pour une modification, il présente les liens avant et après afin qu'une référence retirée en même temps reste visible. Le workflow compare le commit de fusion testé de chaque PR à son premier parent, puis publie un résumé indicatif et l'artefact JSON `source-change-impact`.

## Règles de propagation

- Seules les références typées explicites sont suivies : `source_ids`, les `source_verifications[*].source_id`, `study_ids`, `dataset_ids`, `supporting_study_ids`, `challenging_study_ids`, `claim_ids`, `hypothesis_ids` et `concept_ids`.
- Les tags, domaines, cooccurrences et voisinages génériques du graphe ne créent pas de dépendance.
- Les arêtes incidentes au sous-graphe concerné sont affichées comme contexte, mais ne sont pas parcourues transitivement : une relation documentaire ou une proximité ne suffit pas à établir une dépendance épistémique.
- Le registre des synthèses relie les dossiers aux chemins et identifiants de synthèse ; ces liens sont restitués sans modifier les documents.

## Interprétation

Le rapport est une **liste de revue**, pas un verdict automatique. Un changement de source peut ne pas affecter un claim si le passage concerné reste inchangé ; inversement, un effet peut exister même si une référence explicite manque. Le script ne réécrit aucun registre, ne change aucun statut et ne déprécie aucune connaissance.

Pour chaque objet listé, le responsable de recherche doit vérifier le localisateur dans la version de source concernée et consigner une décision : inchangé, à recontrôler, corrigé, ou déprécié. Les corrections doivent ensuite être apportées dans les fiches canoniques et les synthèses concernées, puis leurs relations vérifiées.

## Limites actuelles

- Les références implicites dans le texte libre ne sont pas détectées.
- Les analyses reproductibles, débats et pages éditoriales ne sont pas encore intégrés comme types de dépendances autonomes.
- Les liens dossier → synthèse proviennent du registre de correspondance ; la fraîcheur du contenu est contrôlée séparément par `check_synthesis_freshness.py`.
- Le script est conçu pour un corpus versionné dans Git ; il ne remplace pas un journal d’événements de source ni un système de notification.

Les tests unitaires utilisent un graphe synthétique pour vérifier la propagation explicite, la présence des synthèses et l’absence de propagation via les domaines.
