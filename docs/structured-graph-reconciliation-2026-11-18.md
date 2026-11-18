# Réconciliation ciblée des relations explicites du graphe

Date : 18 novembre 2026

Référence : audit de couverture documenté dans `docs/structured-knowledge-graph-audit-2026-11-18.md`.

## Principe

L'audit initial avait identifié 31 objets sans relation dans `knowledge/graph.yml` et sans référence structurée entrante. Une revue ciblée des fiches a montré que six objets possédaient déjà une relation documentaire explicite dans leurs champs canoniques, mais que cette relation n'était pas représentée dans le graphe.

Les six arêtes ajoutées ci-dessous transcrivent les références déjà présentes dans les registres ; elles n'ajoutent aucune inférence nouvelle. Les justifications sont limitées à la traçabilité bibliographique, à la transcription des données ou à la source explicitement mobilisée par une claim. Elles ne transforment pas une source en réplication indépendante et ne prétendent pas établir un mécanisme causal.

## Relations ajoutées

| Relation | Source | Cible | Fondement dans les registres |
|---|---|---|---|
| `REL-CITES` | `STUDY-LASELVA-ETAL-2026-CLIMATE-PREBUNKING` | `SOURCE-LASELVA-ETAL-2026-CLIMATE-PREBUNKING` | `study.source_ids` ; la publication est la source bibliographique de la revue systématique |
| `REL-TRANSCRIBES` | `SOURCE-INSEE-TEF-2010-SMIC-POWER` | `DATASET-SMIC-REAL-POWER-2001-2008-TEF2010` | `dataset.source_ids` et notes de transcription du tableau 5.3 |
| `REL-TRANSCRIBES` | `SOURCE-DARES-SMIC-POWER-DECOMPOSITION-1971-2001` | `DATASET-SMIC-POWER-DECOMPOSITION-1971-2001` | `dataset.source_ids` et notes de transcription du tableau V |
| `REL-SUPPORTS` | `SOURCE-EXPERTS-SMIC-2025` | `CLAIM-SMIC-MARGINAL-RATES-1P2-2` | `claim.source_ids` et `supporting_evidence` |
| `REL-SUPPORTS` | `SOURCE-EXPERTS-SMIC-2025` | `CLAIM-SMIC-WAGE-PROGRESSION-1P2-2` | `claim.source_ids` et `supporting_evidence` |
| `REL-SUPPORTS` | `SOURCE-OECD-LOW-WAGE-FRANCE-2025` | `CLAIM-SMIC-LOW-WAGE-CAREER-MOBILITY-OECD-2025` | `claim.source_ids` et `supporting_evidence` |

Les trois claims SMIC restent au statut `under_review`. La relation `REL-SUPPORTS` signifie que la source est mobilisée à l'appui de la proposition ; elle ne signifie ni validation définitive de la claim, ni identification causale.

## Bilan actualisé

- 31 objets sans relation ni référence entrante dans l'instantané initial.
- 6 objets désormais reliés au graphe par des arêtes fondées sur des références déjà explicites.
- 25 sources restent sans relation dans le graphe et sans référence structurée entrante identifiée par l'audit.
- Aucun identifiant de source, étude, dataset ou claim n'a été créé ou supprimé.
- Aucun schéma, registre ou type de relation n'a été ajouté.
- Aucun lien `REL-ABOUT` n'a été ajouté uniquement pour améliorer le taux de connectivité.

Les 25 sources restantes comprennent des positions d'acteurs sociaux et politiques, des sources de contexte institutionnelles, des publications de recherche et des ressources documentaires. Elles ne doivent pas toutes être reliées à une claim : certaines ont une fonction de contexte, de documentation ou de représentation d'une position. La suite est une revue source par source, en recherchant des liens de citation, de transcription ou d'étayage réellement établis.

## Contrôles attendus

Le validateur existant doit vérifier les extrémités et les types de ces six relations, leurs identifiants, justifications et l'absence de triplets dupliqués. Les références structurées d'origine demeurent la source de vérité ; le graphe en fournit la navigation relationnelle explicite.
