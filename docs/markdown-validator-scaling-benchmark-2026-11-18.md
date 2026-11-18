# Microbenchmark de montée en charge des validateurs Markdown

Date : 18 novembre 2026

Code de référence : `main` après les PR #147 et #148, SHA `00500d72949ec504588d97f3b721ef18d32ee514`.

## Périmètre

Ce test mesure les deux contrôles Markdown locaux :
- résolution des chemins dans `validate_markdown_links.py` ;
- résolution des fragments de titres ATX dans `validate_markdown_anchors.py`.

Il ne mesure pas les validateurs YAML/JSON des registres, les appels GitHub, le temps d'installation des dépendances ni l'ensemble du workflow CI.

## Protocole

- Corpus synthétique créé dans des répertoires temporaires, puis supprimé.
- Référence ×1 : 126 fichiers Markdown et 329 liens locaux, soit le volume observé lors de l'audit précédent.
- ×10 : 1 260 fichiers et 3 290 liens.
- ×100 : 12 600 fichiers et 32 900 liens.
- Trois titres ATX par fichier ; les liens ciblent des fichiers Markdown existants et des fragments présents.
- Une exécution de chauffe, puis trois mesures ; temps médian retenu.
- Environnement de mesure : Python 3.13.5, Linux x86_64. Les fonctions exercées reproduisent les parcours et opérations des validateurs actuels sur les cas synthétiques générés ; ces chiffres ne sont pas des durées de CI GitHub Actions.

## Résultats

| Échelle | Fichiers | Liens | Chemins locaux (médiane) | Fragments (médiane) | Erreurs |
|---|---:|---:|---:|---:|---:|
| ×1 | 126 | 329 | 0,0285 s | 0,0299 s | 0 |
| ×10 | 1 260 | 3 290 | 0,2139 s | 0,2879 s | 0 |
| ×100 | 12 600 | 32 900 | 2,1212 s | 3,2716 s | 0 |

À ×100, le parcours des chemins prend environ 74 fois le temps du cas de base et celui des fragments environ 109 fois. Pour 100 fois plus de fichiers/liens, le comportement reste du même ordre de grandeur qu'une croissance linéaire ; l'écart supplémentaire du contrôle d'ancres vient notamment de la lecture et de l'analyse des titres des cibles Markdown. Ces ratios sont indicatifs et sensibles au système de fichiers, au cache et à la charge de la machine.

## Conclusion opérationnelle

- Les deux validateurs Markdown ne montrent pas de signe de saturation sur le corpus synthétique ×100 : environ 2,1 s pour les chemins et 3,3 s pour les fragments dans cet environnement.
- La complexité pratique reste dominée par le parcours des fichiers, la lecture du contenu et le nombre de liens. Le cache local des ancres évite de recalculer les titres d'une même cible à chaque lien.
- Aucun parallélisme, index persistant ou cache global n'est justifié à ce stade ; ils augmenteraient la complexité pour un gain non démontré.
- Conserver le contrôle des fragments en mode informatif tant que les limites de reproduction du rendu GitHub subsistent.

## Limites et suite

Ce microbenchmark ne constitue pas un benchmark de tous les validateurs. La suite utile est de mesurer séparément `validate_registry.py` sur des jeux de données synthétiques cohérents avec les schémas, sans injecter de doublons ou de références invalides qui feraient mesurer le traitement des erreurs plutôt que la montée en charge nominale. Il faudra également conserver une mesure de référence sur le corpus réel et comparer les durées dans les logs CI, sous un environnement stable.
