# Revue sémantique du backlog

**Cadence recommandée :** revue légère mensuelle ; revue complète trimestrielle et à chaque changement majeur de périmètre.  
**Responsabilité :** mainteneur du dépôt, avec validation humaine des reclassements et clôtures.  
**Source de vérité :** issues GitHub et labels canoniques ; ce document décrit la méthode, pas un second backlog.

## Grille de revue

Pour chaque issue ouverte, examiner et consigner :

| Dimension | Conforme si… | Signal d'alerte |
|---|---|---|
| Objectif | question/problème précis, périmètre identifiable | formulation vague ou plusieurs objectifs indépendants |
| Preuves/contexte | état de départ, sources ou liens internes vérifiables | affirmation non sourcée ou contexte obsolète |
| Livrables | artefacts ou résultats attendus explicités | aucun résultat vérifiable à produire |
| Critères d'acceptation | critères observables, testables ou vérifiables | « terminer l'analyse » sans définition de fini |
| Dépendances | issues, PR, données et décisions amont reliées | dépendance implicite, déjà résolue ou bloquante non suivie |
| Priorité | high justifié par échéance, risque, dépendance ou effet de blocage ; medium par importance planifiable ; low par caractère non bloquant | priorité sans justification dans le corps ou priorité devenue disproportionnée |
| Meta | gouvernance, architecture, méthode ou coordination réellement transversale | meta utilisé pour signaler seulement l'importance |
| Fraîcheur | dernier progrès substantiel, blocage ou revue explicitement daté | aucune activité substantielle connue au-delà du seuil de revue |
| Doublon/recouvrement | périmètre distinct et articulation documentée | même livrable demandé ailleurs sans partage de responsabilités |
| Traçabilité | liens issue ↔ PR ↔ fichiers/synthèses/graphes cohérents | PR fusionnée mais issue non actualisée, lien cassé ou état contradictoire |

### Qualification des constats

- **Anomalie certaine** : fait vérifiable (lien cassé, dépendance déjà fusionnée encore déclarée « à fusionner », critère vide, priorité absente/multiple).
- **Alerte** : signal nécessitant vérification (issue ancienne, priorité high sans échéance visible, livrable peu concret).
- **Jugement humain** : décision de priorité, pertinence de meta, fusion de périmètres ou clôture. Elle doit inclure une justification.
- **Non évalué** : données insuffisantes ; ne pas transformer l'absence d'information en anomalie.

Aucun de ces constats ne déclenche seul une modification de label, une repriorisation ou une fermeture.

## Seuils de fraîcheur

- Issue `priority:high` : demander une revue si aucun progrès substantiel n'est consigné depuis 30 jours.
- Autres issues ouvertes : demander une revue si aucun progrès substantiel n'est consigné depuis 90 jours.
- Issue bloquée : réexaminer le blocage à chaque revue mensuelle.
- Une revue peut conclure « toujours pertinente, inchangée » avec date et justification.

Ces seuils sont des déclencheurs de revue, pas des règles de clôture. **Ne pas utiliser le seul champ GitHub `updated_at`** : les opérations de classement par lots peuvent modifier cette date sans progrès scientifique ou technique. Privilégier les commentaires substantiels, changements du corps, commits/PR liés et dates de revue consignées.

## Format du compte rendu

Chaque revue datée doit conserver :
1. périmètre et date de l'instantané ;
2. anomalies certaines, alertes, jugements humains et éléments non évalués séparément ;
3. issues examinées et raisons ;
4. propositions de changements, avec justification et état (proposé, accepté, refusé, différé) ;
5. décisions humaines et personne/fonction ayant validé ;
6. actions de suivi et liens vers issues/PR ;
7. limites de couverture.

## Déroulement

1. Extraire la liste des issues ouvertes et leurs labels.
2. Contrôler mécaniquement les invariants de labels.
3. Lire les corps des issues meta et high, puis les issues sans livrables/critères explicites.
4. Comparer les dépendances et PR aux états réellement fusionnés/fermés.
5. Repérer les recouvrements par question et livrable, pas seulement par mots du titre.
6. Produire un rapport daté ; demander validation avant toute mutation.
7. Mettre à jour les issues et documents dans une PR séparée, avec liens croisés.

## Limites

La revue sémantique ne peut pas être entièrement automatisée par des mots-clés ou des dates. Les rapprochements thématiques ne prouvent pas un doublon ; une priorité élevée n'est pas erronée simplement parce qu'une issue est ancienne ; l'absence de commentaire ne prouve pas l'absence de travail hors GitHub. Toute décision de classement reste révisable et justifiée.
