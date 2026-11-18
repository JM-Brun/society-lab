# Benchmark de validation des registres JSON Schema

Date : 18 novembre 2026

Commit testé : `cae41318be1855abee69c0a1b3c31145d129661d` (branche de la PR #150).

## Protocole reproductible

Le script `scripts/benchmark/benchmark_registry_schema_validation.py` charge les enregistrements réels des neuf registres déclarés dans `scripts/validate/validate_registry.py`, puis répète les mêmes objets en mémoire à ×1, ×10 et ×100. Il appelle directement la fonction de production `validate_schema_and_records` pour chaque registre et chaque échelle.

- Environnement CI : Ubuntu Linux, Python 3.12.16.
- Référence : 441 enregistrements, répartis sur 9 registres.
- Échelles : 441, 4 410 et 44 100 validations d'enregistrements.
- Une chauffe puis trois répétitions ; médiane des trois temps.
- Les enregistrements sources passent au préalable le validateur complet des registres.
- Aucun fichier de registre n'est modifié ; les copies répétées restent en mémoire.

## Résultats observés dans GitHub Actions

| Échelle | Enregistrements | Temps médian | Mesures |
|---|---:|---:|---|
| ×1 | 441 | 0,107703 s | 0,107742 / 0,107562 / 0,107703 s |
| ×10 | 4 410 | 0,568233 s | 0,568233 / 0,563329 / 0,575176 s |
| ×100 | 44 100 | 5,123938 s | 5,114080 / 5,123938 / 5,157131 s |

La multiplication par 100 du volume augmente le temps mesuré d'environ 47,6 fois. Cette observation indique une montée en charge satisfaisante du chemin de validation JSON Schema sur ce corpus et cet environnement. Elle ne constitue pas une garantie de complexité asymptotique : les tailles et distributions des enregistrements sont celles du dépôt répété, pas celles d'un corpus futur différent.

## Périmètre et limites

Ce benchmark mesure uniquement `validate_schema_and_records` :
- lecture et parsing YAML exclus (les objets sont déjà chargés) ;
- références croisées exclues ;
- validation des extrémités et des relations du graphe exclue ;
- manifestes d'ingestion, audit des issues, validateurs de synthèses et liens Markdown exclus ;
- installation des dépendances et démarrage du runner CI exclus.

Il ne mesure donc pas la durée complète de `validate_registry.py`, ni celle du workflow. Les durées varient selon le runner GitHub et sa charge. Aucun seuil de performance bloquant n'est introduit.

## Décision

Aucune optimisation n'est justifiée à ce stade : 44 100 validations d'enregistrements sont effectuées en environ 5,1 secondes dans l'environnement observé. Éviter parallélisme, cache persistant ou index tant qu'une mesure sur le workflow complet ne révèle pas un coût significatif.

Pour la suite, mesurer séparément les références croisées et les relations du graphe avec des données synthétiques cohérentes, puis relever la durée totale de `validate_registry.py` dans un environnement CI stable.
