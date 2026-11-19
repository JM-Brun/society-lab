# Audit des KPIs et de la connectivité du graphe — 19 novembre 2026

## Périmètre et traçabilité

- Dépôt : `JM-Brun/society-lab`
- Commit audité : `8e64dbe59b9bf89326089e3ee9455c236b5db2f9`
- Instantané du calcul : **2026-11-19 21:20:47 UTC**
- Calculateur : `scripts/validate/calculate_project_kpis.py`
- Workflow post-fusion : `Validate knowledge base` #1057, réussi ; `Secret scanning` #331, réussi.
- Les diagnostics de connectivité sont descriptifs : aucun seuil de degré, score global ou anomalie automatique n'est déduit de l'isolement.

## Indicateurs

| Indicateur | Numérateur | Dénominateur | Résultat | Interprétation |
|---|---:|---:|---:|---|
| Couverture documentaire des sources | 218 | 220 | 99,1 % | Source reliée par au moins une relation documentaire retenue, valide et justifiée |
| Claims à statut conclusif | 28 | 80 | 35,0 % | Claims actifs ayant un statut conclusif explicite |
| Couverture des synthèses | 25 | 25 | 100,0 % | Dossiers actifs associés chacun à une synthèse valide |

### Sources non couvertes (2)

- `SOURCE-DEFENSEUR-DROITS-JEUNESSES-ORIGINE-2026`
- `SOURCE-EU-EDUCATION-MONITOR-2025-FRANCE`

Ces deux fiches sont utilisées comme sources de contexte et restent reliées uniquement par `REL-ABOUT`. Elles ne sont pas mobilisées comme preuves d'un claim ou d'une étude dans le graphe. Leur absence de couverture documentaire est donc **un choix de qualification explicite**, pas une omission à corriger par un lien artificiel.

Le champ de couverture documentaire ne compte pas `REL-ABOUT` comme preuve de mobilisation : seules les relations documentaires retenues par le calculateur entrent dans son numérateur.

### Statuts des claims

| Statut | Nombre |
|---|---:|
| `partially_supported` | 27 |
| `supported` | 1 |
| `under_review` | 52 |
| `superseded` | 3 |

Les trois claims `superseded` sont exclus du dénominateur. Les 52 claims `under_review` expliquent la majeure partie du taux de 35 %. Ce KPI mesure la présence d'un statut conclusif, pas la vérité des claims ni la qualité de leurs preuves.

### Synthèses

- 25 associations dossier → synthèse valides.
- 11 fichiers de synthèse distincts.
- Aucun dossier actif sans synthèse valide.
- Aucune anomalie de correspondance.

## Graphe de connaissances

- **476 nœuds indexés**
- **699 relations**
- **699 relations valides**, aucune relation exclue par les diagnostics d'intégrité
- Aucune collision d'identifiant de nœud signalée
- Aucun diagnostic d'intégrité de relation signalé

### Connectivité par type de nœud

| Type | Nœuds | Avec relation | Isolés |
|---|---:|---:|---:|
| CLAIM | 83 | 83 | 0 |
| CONCEPT | 15 | 15 | 0 |
| DATASET | 14 | 14 | 0 |
| DOMAIN | 15 | 14 | 1 |
| DOSSIER | 25 | 25 | 0 |
| HYPOTHESIS | 22 | 22 | 0 |
| SOURCE | 220 | 220 | 0 |
| STUDY | 62 | 62 | 0 |
| SYNTHESIS | 11 | 11 | 0 |
| TERRITORY | 9 | 8 | 1 |

### Relations valides par type

| Type | Nombre |
|---|---:|
| `REL-ABOUT` | 178 |
| `REL-CHILD-OF` | 8 |
| `REL-CITES` | 45 |
| `REL-GEOGRAPHICALLY-WITHIN` | 7 |
| `REL-INCLUDES` | 327 |
| `REL-QUALIFIES` | 8 |
| `REL-SUMMARIZED-BY` | 11 |
| `REL-SUMMARIZES` | 1 |
| `REL-SUPPORTS` | 87 |
| `REL-TRANSCRIBES` | 21 |
| `REL-USES` | 6 |
| **Total** | **699** |

### Isolements résiduels qualifiés

- `DOMAIN-HEALTH` : aucune fiche des registres examinés ne déclare ce domaine. Il reste isolé sans que cela constitue une anomalie démontrée. À réexaminer si le corpus s'enrichit sur la santé ou la démographie.
- `TERRITORY-INTERNATIONAL` : le référentiel `knowledge/TERRITORIES.yml` définit explicitement cette échelle comme relationnelle, transversale et non administrative. Elle n'a pas de parent géographique ; son isolement dans les seules relations `REL-GEOGRAPHICALLY-WITHIN` est cohérent avec cette définition.

### Correction de traçabilité intégrée

La PR #188 a ajouté 11 relations à partir des champs canoniques `domains` et `domain_ids` :
- 10 relations `REL-ABOUT` reliant les objets au domaine déclaré ;
- 1 relation `REL-INCLUDES` reliant `DOMAIN-SCIENCE` au concept qui déclare ce domaine.

Les domaines isolés sont ainsi passés de quatre à un. Les relations ajoutées sont thématiques, non probatoires. Aucune relation `REL-SUPPORTS` n'a été ajoutée. Les deux sources de contexte restent des sources de contexte.

## Décisions et limites

1. Ne pas chercher à augmenter artificiellement les 99,1 % de couverture des sources : les deux sources non couvertes sont classées et justifiées.
2. Ne pas traiter le taux de 35 % des claims conclusifs comme une mesure de vérité ou de qualité scientifique. Les 52 claims `under_review` forment un portefeuille de vérification à poursuivre.
3. Ne pas créer de relation pour `DOMAIN-HEALTH` ou `TERRITORY-INTERNATIONAL` sans objet canonique ou justification sémantique supplémentaire.
4. Conserver le benchmark ×1/×10/×100 dans le workflow périodique et manuel séparé. Sur l'exécution post-fusion, le calcul KPI en CI a duré environ une seconde, contre environ 53 secondes pour les tests unitaires ; le calcul KPI n'est pas le poste dominant.
5. L'inventaire de couverture des registres est un artefact distinct : la présence des champs n'atteste ni leur qualité ni la validité scientifique de leurs contenus.

## Conclusion opérationnelle

La connectivité documentaire et structurelle du graphe est désormais cohérente avec les métadonnées explicites examinées. Les seuls isolements résiduels sont qualifiés et ne justifient pas de relations artificielles. Les trois KPIs restent stables ; les deux sources de contexte demeurent volontairement hors du numérateur documentaire. L'issue #156 peut rester ouverte pour la revue qualitative des sources et claims et la stabilisation durable du processus d'audit.
