# Indicateurs de pilotage de Society Lab

**Statut :** spécification proposée — à valider sur les données réelles avant toute intégration automatisée.  
**Périmètre :** pilotage de la production et de la maintenance des connaissances, pas évaluation automatisée de la vérité scientifique.

## 1. Finalité et principes

Society Lab est un projet documentaire de recherche secondaire : il rassemble, confronte et synthétise des travaux et données existants, sans prétendre conduire ses propres expériences. Ses indicateurs doivent donc mesurer la capacité du dépôt à transformer des sources en connaissances traçables, qualifiées, reliées et synthétisées.

Les KPIs doivent respecter les principes suivants :

1. **Mesurer l'utilité, pas le volume.** Le nombre de fichiers, de commits, de sources ou d'arêtes n'est pas un résultat en soi.
2. **Rendre les calculs auditables.** Chaque ratio expose numérateur, dénominateur, exclusions, cas indéterminés et liste des objets concernés.
3. **Ne pas fabriquer de précision.** Un champ absent ou un statut ambigu ne doit pas être interprété comme une validation.
4. **Séparer qualité documentaire et qualité scientifique.** Une CI verte confirme uniquement les propriétés effectivement contrôlées.
5. **Ne pas créer de score global.** Les dimensions sont complémentaires et ne doivent pas se compenser artificiellement.
6. **Réutiliser les sources de vérité existantes.** Registres, fiches, schémas et graphe canoniques ; pas de registre KPI parallèle.
7. **Rester soutenable.** Calculs déterministes, locaux, sans service externe ni dépendance lourde.

## 2. Tableau de bord proposé

La première version doit distinguer quatre indicateurs de pilotage prioritaires et deux diagnostics complémentaires.

| Indicateur | Rôle | Calcul cible | Priorité |
|---|---|---|---|
| Source-to-Knowledge Coverage | Mesurer l'exploitation documentaire des sources | Sources éligibles reliées à au moins un objet de connaissance / sources éligibles | Principal |
| Evidence Verification Coverage | Suivre la vérification documentée des claims | Claims éligibles avec statut de vérification explicite / claims éligibles | Principal |
| Synthesis Coverage | Vérifier que les dossiers principaux disposent d'une synthèse | Dossiers principaux éligibles avec synthèse enregistrée / dossiers principaux éligibles | Principal |
| Cross-domain Integration Coverage | Mesurer les mises en relation réellement transversales | Relations inter-domaines justifiées et éligibles, rapportées au périmètre suivi ; voir définition ci-dessous | Principal, après audit |
| Knowledge Graph Connectivity | Détecter les objets isolés ou insuffisamment reliés | Objets éligibles ayant au moins une relation pertinente et justifiée / objets éligibles | Diagnostic |
| Synthesis Freshness | Repérer les synthèses potentiellement à réviser | Synthèses signalées comme en retard / synthèses suivies | Diagnostic |

Les indicateurs principaux ne constituent pas un classement de performance scientifique. Ils signalent des dimensions de couverture et de maintenance.

## 3. Définitions opérationnelles

### 3.1 Source-to-Knowledge Coverage

**Question :** les sources enregistrées contribuent-elles effectivement aux objets de connaissance ?

- **Numérateur :** sources éligibles reliées, par une référence typée existante, à au moins un objet de connaissance exploitable (étude, dataset, claim ou autre objet explicitement autorisé).
- **Dénominateur :** sources éligibles du registre canonique.
- **Exclusions à définir :** sources de contexte, doublons fusionnés, références non acquises ou sources explicitement écartées ; ne les exclure que si le modèle de données permet de les identifier sans inférence.
- **Garde-fou :** une source simplement présente au registre ne compte pas comme exploitée. Un lien de proximité ou une cooccurrence ne suffit pas ; la relation doit être typée et conforme aux règles du dépôt.

Afficher également le nombre de sources sans lien exploitable et la liste des identifiants concernés.

### 3.2 Evidence Verification Coverage

**Question :** quelle proportion des claims examinés possède un état de vérification explicite et exploitable ?

- **Numérateur :** claims éligibles dont le statut documente un examen explicite de la proposition, selon une taxonomie validée.
- **Dénominateur :** claims éligibles, hors seuls cas explicitement exclus par une règle documentée.
- **Ventilation obligatoire :** vérifié, partiellement vérifié, à vérifier, contesté, réfuté, indéterminé — sous réserve que ces états correspondent aux valeurs réelles ou à une taxonomie adoptée.
- **Garde-fou :** « réfuté » et « contesté » témoignent d'un examen et ne doivent pas être confondus avec « non vérifié ». Publier la ventilation brute en plus du ratio.

Ne pas coder la taxonomie dans le calcul avant d'avoir audité le schéma Claim et les valeurs réellement présentes. Si le modèle distingue statut éditorial, statut épistémique et statut de vérification, seul le champ pertinent entre dans le calcul.

### 3.3 Synthesis Coverage

**Question :** les dossiers principaux éligibles disposent-ils d'une synthèse autonome référencée ?

- **Numérateur :** dossiers principaux dont l'association à une synthèse existe dans le registre canonique et dont le fichier cible est présent.
- **Dénominateur :** dossiers principaux déclarés éligibles dans le périmètre du registre.
- **Source initiale :** `syntheses/registry.yml`, à confronter au registre des dossiers et aux fichiers réels.
- **Garde-fou :** ne pas compter deux fois un dossier, ni considérer une simple entrée de registre comme suffisante si le fichier cible est absent.

Un contrôle complémentaire de structure peut vérifier la présence des rubriques attendues dans les synthèses : constats, preuves, controverses, limites, conclusions opérationnelles et travaux restants. Ce contrôle mesure la présence des sections, pas leur qualité rédactionnelle ni leur exhaustivité scientifique.

### 3.4 Cross-domain Integration Coverage

**Question :** les dossiers et objets du projet permettent-ils de relier des domaines distincts par des mécanismes ou des preuves explicitement documentés ?

Ne pas utiliser le nombre brut d'arêtes inter-domaines comme ratio de performance. Pour la première version, publier des mesures descriptives :

- nombre de relations inter-domaines justifiées ;
- nombre de couples de domaines effectivement reliés ;
- nombre de mécanismes transversaux documentés ;
- nombre et proportion de relations inter-domaines dont la justification et la provenance sont exploitables.

Le dénominateur d'une couverture générale n'est pas encore stabilisé : il dépend de la définition des relations inter-domaines attendues et du périmètre des objets éligibles. Tant que cette définition n'est pas validée, afficher les comptes et listes, pas un pourcentage présenté comme un KPI comparable.

**Garde-fou :** aucune cible de densité du graphe. Certaines disciplines et certains sujets n'ont pas de lien direct pertinent. Une relation causale ne peut jamais être déduite d'un tag, d'une cooccurrence ou d'une simple proximité.

### 3.5 Knowledge Graph Connectivity

**Question :** les objets qui devraient être reliés disposent-ils de relations pertinentes et justifiées ?

- **Numérateur :** objets éligibles disposant d'au moins une relation conforme à une liste de relations attendues pour leur type.
- **Dénominateur :** objets pour lesquels une relation est effectivement attendue.
- **Diagnostics :** objets isolés, relations sans justification, références orphelines, types incompatibles et divergences entre fiches et graphe.

Cet indicateur reste secondaire jusqu'à la définition explicite des règles d'éligibilité par type d'objet. Les objets de référence, définitions autonomes ou objets nouvellement créés peuvent légitimement ne pas avoir de relation entrante ou sortante.

### 3.6 Synthesis Freshness

**Question :** quelles synthèses peuvent nécessiter une revue à la suite de changements dans leurs dossiers ou leurs sources ?

Réutiliser le contrôle existant `scripts/validate/check_synthesis_freshness.py` et ses règles. Rapporter :

- synthèses signalées comme potentiellement obsolètes ;
- synthèses suivies ;
- dossiers modifiés depuis la dernière révision connue ;
- date de dernière revue lorsque renseignée.

**Garde-fou :** la fraîcheur est un signal de maintenance, pas une preuve d'actualité scientifique. Une date récente ne garantit pas qu'une revue substantielle a été effectuée.

## 4. Indicateurs à ne pas promouvoir en KPIs

| Mesure | Usage acceptable | Pourquoi ce n'est pas un KPI principal |
|---|---|---|
| Nombre de commits | Activité du dépôt | Ne mesure ni l'utilité ni la qualité |
| Nombre de fichiers | Taille du corpus | Encourage la fragmentation et le volume |
| Nombre de sources ingérées | Suivi de flux | N'indique pas si les sources sont exploitées |
| Nombre total de claims | Inventaire | Ne dit rien de leur vérification |
| Nombre total d'arêtes | Inventaire du graphe | Peut augmenter par ajout de liens faibles ou artificiels |
| Nombre de synthèses | Inventaire | La couverture des dossiers est plus informative |
| Taux de réussite CI | Fiabilité technique | Garde-fou nécessaire mais peu spécifique à la mission |
| Score global de qualité scientifique | À écarter | Réducteur, non défendable et non automatisable de façon fiable |

## 5. Faisabilité et audit préalable obligatoire

Aucun indicateur ne doit être implémenté sur la seule base de cette spécification. Avant le calcul, auditer les registres, schémas et valeurs réelles.

| Indicateur | Faisabilité présumée | Vérification requise |
|---|---|---|
| Source-to-Knowledge | Bonne | Références typées, couverture du registre, exclusions et relations réellement exploitables |
| Evidence Verification | Conditionnelle | Schéma Claim, valeurs de statut, distinction entre revue et conclusion épistémique |
| Synthesis Coverage | Très bonne | Exhaustivité du registre, unicité des dossiers, existence des chemins et périmètre éligible |
| Cross-domain Integration | Partielle | Domaines des objets, typologie des relations et justification/provenance |
| Knowledge Graph Connectivity | Partielle | Règles d'éligibilité et relations attendues par type d'objet |
| Synthesis Freshness | Déjà partiellement disponible | Comprendre exactement les règles et limites du script existant |

Pour chaque calcul, le prototype doit établir :
1. les fichiers et champs réellement utilisés ;
2. la règle d'éligibilité et les exclusions ;
3. le traitement des valeurs absentes, inconnues ou contradictoires ;
4. les exemples de cas comptés et non comptés ;
5. la stabilité du résultat face aux doublons et aux changements d'ordre des registres ;
6. le coût de calcul sur le corpus courant.

Si les données ne permettent pas un calcul honnête, marquer l'indicateur « non calculable en l'état » et documenter le manque précis. Ne pas ajouter de champ ou migrer massivement les fiches uniquement pour faire monter un KPI.

## 6. Intégration technique envisagée

### Phase 0 — Spécification et audit

- Auditer les schémas, registres et scripts existants.
- Confirmer les définitions, dénominateurs, statuts et exclusions.
- Produire un exemple de calcul manuel vérifiable pour chaque KPI retenu.
- Identifier les réutilisations possibles, notamment le registre des synthèses et le contrôle de fraîcheur.

### Phase 1 — Prototype en lecture seule

- Ajouter un calculateur déterministe, sans mutation des fiches.
- Lire les registres et le graphe canoniques.
- Produire un rapport JSON structuré et un résumé Markdown.
- Inclure les valeurs brutes, les identifiants concernés et les motifs d'exclusion.
- Ne créer aucun registre KPI parallèle et aucune dépendance réseau.

### Phase 2 — Tests unitaires et négatifs

Prévoir au minimum les cas suivants :

- registre vide ;
- fichier référencé absent ;
- identifiant dupliqué ;
- référence inexistante ou de type incorrect ;
- objet isolé mais légitimement exempté ;
- relation sans justification ;
- claim dont le statut est absent ou inconnu ;
- statut réfuté ou contesté ;
- dossier relié à plusieurs sous-dossiers/synthèses ;
- synthèse dupliquée ou entrée de registre orpheline ;
- domaine absent ou relation intra-domaine ;
- valeurs YAML réordonnées sans changement sémantique.

Les tests doivent vérifier les numérateurs, dénominateurs, exclusions, listes d'anomalies et sorties indéterminées, pas seulement le code de retour.

### Phase 3 — CI non bloquante

- Ajouter le calcul après les validations structurelles existantes, si le coût mesuré le justifie.
- Publier le rapport comme artefact ou sortie de job.
- Ne pas faire échouer la CI sur une cible arbitraire de KPI.
- Faire échouer uniquement les erreurs techniques de calcul ou les incohérences qui relèvent déjà d'une règle bloquante.
- Éviter les appels réseau et les installations supplémentaires.
- Ne pas dupliquer les validateurs déjà exécutés.

### Phase 4 — Historique et visualisation (optionnelle)

N'ajouter un historique que si un besoin de suivi longitudinal est établi. Préférer des artefacts CI ou un historique dérivé et reproductible plutôt qu'un registre manuel à maintenir. Toute comparaison temporelle doit tenir compte des changements de périmètre, de schéma et de définition.

## 7. Performance et scalabilité

Le dépôt possède déjà un benchmark des validations de schémas à différentes tailles. Le prototype KPI doit réutiliser les conventions et mesures existantes plutôt que créer une infrastructure parallèle.

Mesurer le temps et, si disponible sans complexité excessive, la mémoire :
- sur le corpus actuel ;
- sur une charge simulée ×10 ;
- sur une charge simulée ×100.

Les jeux de charge doivent préserver les structures et distributions utiles, et distinguer les coûts de parsing, d'indexation et de calcul. Éviter les parcours répétés de tous les objets pour chaque relation : construire des index en mémoire lorsque cela simplifie et accélère réellement le calcul.

Aucun seuil de performance ne doit être fixé avant une mesure de référence. Le critère est un coût marginal faible et stable par rapport à la CI existante.

## 8. Format du rapport

Chaque exécution doit produire une structure de ce type :

| Champ | Description |
|---|---|
| `metric_id` | Identifiant stable de l'indicateur |
| `status` | `computed`, `not_computable` ou `error` |
| `numerator` | Nombre d'éléments comptés, si applicable |
| `denominator` | Nombre d'éléments éligibles, si applicable |
| `value` | Ratio ou valeur descriptive, sans arrondi destructif |
| `unit` | Pourcentage, nombre ou durée |
| `scope` | Registres, types et périmètre couverts |
| `excluded_count` | Nombre d'éléments exclus |
| `unknown_count` | Nombre d'éléments indéterminés |
| `issues` | Anomalies et identifiants concernés |
| `definition_version` | Version de la définition du KPI |
| `generated_at` | Horodatage de génération |

Un ratio nul ne doit jamais être confondu avec un indicateur non calculable (par exemple dénominateur nul).

## 9. Critères d'acceptation

La spécification ne sera considérée comme implémentée que lorsque :

- chaque KPI retenu a une définition stable et un périmètre explicite ;
- chaque dénominateur et chaque exclusion sont justifiés ;
- les données réelles ont été auditées avant codage ;
- les cas inconnus ne sont pas transformés en résultats positifs ou négatifs ;
- les calculs sont déterministes et testés par des tests positifs et négatifs ;
- le rapport permet de retrouver les objets comptés et exclus ;
- aucun score composite de qualité scientifique n'est produit ;
- aucun registre canonique parallèle n'est introduit ;
- le temps de calcul est mesuré sur corpus courant, ×10 et ×100 ;
- l'intégration CI est non bloquante pour les niveaux de KPI et n'ajoute pas de dépendance réseau ;
- la documentation distingue explicitement qualité documentaire, qualité des contrôles et qualité scientifique.

## 10. Ordre de réalisation recommandé

1. Auditer les données et les règles de calcul de Synthesis Coverage et Synthesis Freshness : ce sont les points d'entrée les plus simples.
2. Auditer les schémas Claim et Source pour déterminer si Evidence Verification et Source-to-Knowledge sont calculables sans migration.
3. Construire les diagnostics du graphe et la mesure inter-domaines, sans pourcentage tant que le dénominateur n'est pas défendable.
4. Développer le prototype en lecture seule et ses tests.
5. Mesurer le coût marginal et la scalabilité.
6. Intégrer à la CI seulement après validation des résultats et de la performance.

## 11. Références internes

- `README.md` — finalité et architecture du projet.
- `docs/architecture.md` — couches de connaissance et source de vérité.
- `docs/metadata-and-naming.md` — métadonnées et conventions.
- `docs/ingestion-protocol.md` — étapes du pipeline d'ingestion.
- `syntheses/registry.yml` — correspondance dossiers/synthèses.
- `scripts/validate/check_synthesis_freshness.py` — contrôle de fraîcheur existant.
- `.github/workflows/validate.yml` — workflow de validation actuel.
- Issue #114 — audit du pipeline de production des connaissances.

---

**Décision de méthode :** cette spécification documente les indicateurs candidats et leur méthode d'adoption. Elle n'affirme pas que les KPIs sont déjà calculables, ne crée pas encore de calculateur et ne modifie pas la CI. La première livraison technique doit être un audit de faisabilité reproductible, puis un prototype testé en lecture seule.


## 12. Résultat de l'audit de faisabilité du 18 novembre 2026

L'audit concret est consigné dans [`project-kpis-feasibility-audit-2026-11-18.md`](project-kpis-feasibility-audit-2026-11-18.md). Il conduit à ajuster le tableau de bord initial :

| KPI retenu après audit | Définition opérationnelle | État |
|---|---|---|
| Couverture documentaire des sources | Sources du registre ayant au moins une relation typée de contribution documentaire justifiée / sources du registre | Calculable ; instantané 165/220 (75 %) |
| Claims avec conclusion documentée | Claims actifs dont le statut est `supported`, `partially_supported`, `contested`, `not_supported` ou `insufficient_evidence` / claims actifs non superseded | Calculable ; instantané 28/80 (35 %) |
| Couverture des synthèses | Dossiers actifs éligibles disposant d'une synthèse existante / dossiers actifs éligibles | Non calculable honnêtement en pourcentage sans inventaire indépendant des dossiers éligibles |
| Connectivité du graphe | Objets éligibles ayant au moins une relation attendue et justifiée / objets éligibles | Diagnostic seulement ; règles d'éligibilité par type manquantes |

**Correction de schéma :** le champ d'état des claims est `status`, pas `review_status`. Les vérifications documentaires par source sont enregistrées séparément dans `source_verifications` et ne doivent pas être confondues avec le statut épistémique du claim.

**Règle de comptage des sources :** une relation `REL-ABOUT` seule indique un rattachement thématique et ne suffit pas à compter une source comme exploitée. La mesure de couverture documentaire retient les relations typées de contribution listées dans le rapport d'audit, avec justification et extrémités valides.

En conséquence, le tableau de bord initial ne doit pas présenter les quatre ratios comme déjà tous calculables. Les deux premiers peuvent être prototypés immédiatement ; les deux autres restent conditionnés à la définition d'un dénominateur ou de règles d'éligibilité défendables.
