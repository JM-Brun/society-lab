# Gouvernance des issues

**Statut :** convention versionnée, audit mécanique en lecture seule et revue sémantique humaine documentée.  
**Référence canonique des labels :** [governance/issue-labels.json](../governance/issue-labels.json).  
**Issue de suivi :** [#123 — taxonomie et métadonnées de pilotage](https://github.com/JM-Brun/society-lab/issues/123).

## Finalité et axes

Les labels sont des métadonnées de pilotage, pas un substitut au titre, au contenu ou aux relations entre issues. Ils séparent quatre axes indépendants :

- **Portée** : internal indique le travail réalisé dans le dépôt ; il ne signifie pas que les contenus scientifiques sont confidentiels.
- **Gouvernance** : meta signale un chantier transversal de gouvernance, architecture, méthode, qualité, audit ou coordination. Ce label ne signifie pas simplement « important ».
- **Priorité** : exactement un de priority:high, priority:medium, priority:low pour chaque issue ouverte de travail interne.
- **Nature** : research, data, documentation, enhancement, knowledge-graph décrivent le livrable ou le travail. Plusieurs peuvent coexister.

Le JSON canonique contient les descriptions, couleurs, règles et invariants. Les labels historiques ou spécifiques non listés sont conservés tant qu'ils ne sont pas explicitement dépréciés.

## Règles de triage

- Toute issue de travail interne ouverte reçoit internal.
- Une issue ouverte reçoit une et une seule priorité. L'absence de priorité est une anomalie à corriger lors du triage, pas une invitation à la deviner.
- high exige une dépendance, un risque ou une échéance explicite ; il doit rester rare.
- medium correspond au travail important mais non bloquant.
- low correspond à une amélioration utile sans urgence.
- meta requiert une décision humaine et un périmètre réellement transversal.
- Réévaluer les labels quand les dépendances, risques, échéances ou critères d'acceptation évoluent.
- Ne jamais fermer, déprioriser ou reclasser automatiquement une issue par simple heuristique.

## Création et maintenance

Le modèle GitHub .github/ISSUE_TEMPLATE/task.md demande objectif, contexte, périmètre, dépendances, plan, livrables, critères d'acceptation, priorité proposée, nature et état réel. Le label internal est proposé par défaut ; la priorité reste à confirmer humainement.

Lorsqu'un label est créé, modifié ou déprécié :
1. modifier le fichier canonique dans une PR ;
2. expliquer la migration et les éventuels alias ;
3. synchroniser les métadonnées GitHub après revue ;
4. vérifier les issues ouvertes et les workflows ;
5. ne supprimer aucun label historique sans vérifier ses usages.

## Contrôle automatisé

Le workflow issue-governance.yml lance un audit hebdomadaire, à la demande et lors des événements d'issues. Il lit les issues ouvertes et signale :
- l'absence de internal ;
- l'absence de priorité ;
- plusieurs priorités simultanées.

Il publie un rapport dans le résumé GitHub Actions. Il est volontairement non destructif : aucune attribution automatique de meta ou de priorité, aucune fermeture et aucune modification d'issue. Les issues de pull request ne sont pas traitées comme des issues ordinaires.

## Revue sémantique périodique\n\nLa grille, les seuils et le format des comptes rendus sont définis dans [governance/backlog-review.md](../governance/backlog-review.md). La première revue datée est conservée dans [governance/backlog-reviews/2026-11-18.md](../governance/backlog-reviews/2026-11-18.md). La cadence proposée est une revue légère mensuelle et une revue complète trimestrielle. Les alertes ne modifient jamais seules les labels ou l'état des issues. Le champ GitHub `updated_at` n'est pas un indicateur fiable de progrès après un reclassement massif ; les événements substantiels et dates de revue doivent être utilisés.\n\n## Limites connues

L'automatisation ne peut pas déterminer de façon fiable si meta est justifié, si une priorité est proportionnée, si une issue est obsolète ou si deux demandes sont des doublons. Ces points nécessitent une revue humaine contextualisée. Le contrôle actuel ne constitue pas une synchronisation des définitions de labels vers l'API GitHub ; la synchronisation contrôlée reste une étape distincte.


## Feuille de route

Les travaux qui dépassent le premier lot sont suivis séparément :

- [#125 — Synchroniser les labels GitHub depuis le référentiel canonique](https://github.com/JM-Brun/society-lab/issues/125) : inventaire, comparaison API, rapport de dérive, dry-run par défaut et application explicite sans suppression.
- [#126 — Revue sémantique périodique du backlog](https://github.com/JM-Brun/society-lab/issues/126) : justification de meta et des priorités, qualité des objectifs/livrables/critères, fraîcheur, doublons et décisions humaines.
- [#127 — Vue de backlog multidimensionnelle](https://github.com/JM-Brun/society-lab/issues/127) : priorité, nature, domaine et dépendances à partir des sources canoniques et identifiants stables.

## Validation opérationnelle — 20 novembre 2026

La [PR #210](https://github.com/JM-Brun/society-lab/pull/210) a ajouté des déclenchements sur `main` lors des modifications des workflows et de leurs entrées. Les exécutions manuelles et planifiées existantes restent disponibles.

- **Synchronisation des labels (#125)**. Le [dry-run](https://github.com/JM-Brun/society-lab/actions/runs/44761357552) a comparé 10 définitions canoniques à 18 labels GitHub : `priority:low` est absent, neuf labels diffèrent par leur description ou couleur, et neuf labels historiques sont hors référentiel. Le job d'application a été ignoré. Pour appliquer les écarts après approbation explicite, déclencher manuellement le workflow `sync-issue-labels.yml` avec `apply=true`, puis refaire un dry-run pour vérifier la convergence. Le rapport de dérive reste disponible pour cette opération de maintenance. #123 est clôturée sur la vérification de la taxonomie, de la revue périodique et de la vue de backlog.
- **Vue de backlog (#127)**. Le [run sur main](https://github.com/JM-Brun/society-lab/actions/runs/44761357403) a produit le Markdown et l'instantané des 23 issues ouvertes avant la clôture de #125, #127 et #156. Les 23 correspondances et les priorités ont été contrôlées. Le rejeu hors ligne reproduit le rendu octet pour octet.
- **Revue sémantique (#126)**. La méthode et la première revue sont versionnées. Parmi les cinq alertes historiques, #2 est close, #29, #36 et #82 portent une priorité moyenne, et #110 reste élevée tant que l'acquisition et l'harmonisation des exports ADEME prioritaires conditionnent la comparaison quantitative.

Pour les détails des critères vérifiés, voir les issues #125, #126 et #127. Le mapping des issues ouvertes est tenu à jour avec leurs fermetures.
