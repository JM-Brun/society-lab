# Vue multidimensionnelle du backlog

## Sources de vérité

La vue de pilotage ne doit pas recopier les titres, labels, domaines ou dépendances dans un tableau entretenu manuellement.

- **Issues et labels opérationnels** : API GitHub du dépôt.
- **Taxonomie de labels** : `governance/issue-labels.json`.
- **Dossiers et domaines scientifiques** : `dossiers/registry.yml` et `knowledge/TAXONOMY.yml`.
- **Synthèses associées** : `syntheses/registry.yml`.
- **Correspondance issue → dossier** : `governance/issue-domain-map.yml`, maintenue explicitement et revue humainement.
- **Dépendances** : liens explicites dans les issues ; la correspondance versionnée peut déclarer les dépendances de pilotage confirmées.

## Modèle de vue

Une ligne de backlog doit exposer au minimum :
- numéro et titre (liens vers GitHub) ;
- état et labels réels ;
- priorité et nature, lues depuis les labels ;
- type de travail (recherche/meta), issu de la correspondance explicite ;
- dossier(s) associé(s), puis domaines dérivés de leurs `domain_ids` ;
- dépendances explicites, sans inférence par similarité ;
- date de dernière revue humaine, distincte de `updated_at` ;
- alertes de données manquantes (issue non mappée, ID de dossier inconnu, dépendance invalide).

## Principes

1. Une issue peut être reliée à plusieurs dossiers ; une issue transversale peut n'avoir aucun dossier.
2. Les domaines sont dérivés des dossiers canoniques. Une issue qui couvre plusieurs domaines conserve tous ces domaines ; ne pas forcer un domaine principal arbitraire.
3. Les labels décrivent la priorité et la nature, pas le domaine scientifique.
4. Les dépendances sont dirigées et explicites. Une mention de numéro dans le corps ne suffit pas à établir une dépendance.
5. Les issues sans correspondance apparaissent dans une section « à qualifier » ; elles ne sont pas classées par heuristique.
6. La fraîcheur est basée sur une date de revue documentée ou une activité substantielle identifiable. Le seul `updated_at` GitHub est insuffisant après des modifications massives de labels.
7. Le rendu est généré depuis les sources de vérité ; aucun copier-coller de titres ou de labels dans un second backlog.

## Première correspondance explicite

`governance/issue-domain-map.yml` relie les 26 issues ouvertes observées le 18 novembre 2026 à leurs dossiers canoniques. Les issues de gouvernance sont marquées `meta` sans domaine scientifique artificiel. Les dépendances ajoutées sont limitées aux relations de pilotage explicitement établies dans les issues et le plan de gouvernance.

Cette correspondance est une première version éditoriale, pas une inférence automatique. Chaque ajout ou modification doit être relu dans une PR.

## Génération et distribution

Le workflow `backlog-view.yml` génère la vue chaque lundi, à la demande et lors d'une PR qui modifie le générateur, ses tests ou le workflow. Il publie le résumé Markdown et conserve pendant 30 jours les fichiers `backlog-view.md` et `backlog-snapshot.json` dans l'artefact `society-lab-backlog-view`.

L'instantané enregistre les champs effectivement utilisés pour le rendu, l'heure du relevé des issues et le SHA du commit dont proviennent les correspondances et dossiers. Le relevé via l'API peut regrouper plusieurs pages lues successivement. L'heure correspond à la fin de la collecte.

Pour capturer un instantané depuis le commit `HEAD`, utiliser la première commande avec `GITHUB_TOKEN` déjà défini. La seconde rejoue le rapport depuis le seul instantané JSON, sans jeton GitHub ni accès au dépôt Git. Utiliser la même version du générateur pour comparer les fichiers octet pour octet.

```bash
python scripts/report/generate_backlog_view.py --snapshot-output backlog-snapshot.json
BACKLOG_OUTPUT=backlog-rejoue.md python scripts/report/generate_backlog_view.py --snapshot-input backlog-snapshot.json
cmp backlog-view.md backlog-rejoue.md
```

Une exécution sans option d'instantané continue de lire la correspondance et les dossiers depuis la copie de travail locale. Le contrôle `scripts/validate/validate_issue_domain_map.py` vérifie l'unicité des issues mappées, l'existence des dossiers et domaines, le type des issues et les dépendances explicites dans la CI principale.

## Contrôles attendus avant génération

- unicité des numéros d'issues dans la correspondance ;
- existence de chaque dossier référencé dans `dossiers/registry.yml` ;
- existence de chaque domaine dans `knowledge/TAXONOMY.yml` ;
- existence des issues et des dépendances dans le dépôt GitHub ;
- présence d'une priorité unique et des labels de nature valides ;
- signalement, sans correction automatique, des issues non mappées ou références invalides.
