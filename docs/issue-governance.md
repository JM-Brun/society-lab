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

État au 18 novembre 2026 : les PR #124 et #128 sont fusionnées. La correction de robustesse du retry est proposée dans la [PR #129](https://github.com/JM-Brun/society-lab/pull/129). La grille et la première revue humaine de #126 sont documentées ; les décisions sur les alertes de priorité restent à confirmer. La vue multidimensionnelle #127 reste à réaliser. Les trois chantiers restent distincts pour rendre leurs critères d'acceptation, risques et validations indépendamment vérifiables.

## État de validation du lot initial

La PR #124 a été fusionnée après validation CI. La PR #128 a également été fusionnée ; la PR #129 ajoute un test du chemin de reprise réseau et reste en attente de revue. Un succès CI ne vaut pas approbation de revue.
