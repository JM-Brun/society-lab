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
| Claim Conclusion Coverage | Suivre la vérification documentée des claims | Claims éligibles avec statut de vérification explicite / claims éligibles | Principal |
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

### 3.2 Claim Conclusion Coverage

**Question :** quelle proportion des claims actifs possède une conclusion épistémique explicitement documentée ?

- **Numérateur :** claims dont le champ canonique `status` vaut `supported`, `partially_supported`, `contested`, `not_supported` ou `insufficient_evidence`.
- **Dénominateur :** tous les claims actifs, c'est-à-dire les claims dont le statut n'est pas `superseded`.
- **Ventilation obligatoire :** publier les effectifs par valeur réelle de `status`, notamment `unexamined`, `under_review` et les cinq statuts conclusifs.
- **Garde-fou :** une conclusion négative ou contestée compte comme une conclusion documentée, pas comme un résultat positif. Ce ratio ne mesure ni la vérité des propositions ni une vérification indépendante.

Le champ `source_verifications.status` décrit le contrôle de chaque source associée à un claim ; il ne remplace pas le statut épistémique du claim et n'entre pas dans ce calcul.

### 3.3 Synthesis Coverage

**Question :** les dossiers principaux éligibles disposent-ils d'une synthèse autonome référencée ?

- **Dénominateur :** dossiers actifs du registre canonique `dossiers/registry.yml` ; les statuts `scoping`, `researching`, `draft`, `under_review` et `published` sont actifs, `archived` est exclu.
- **Numérateur :** dossiers actifs associés exactement une fois à une synthèse dont le fichier et le fichier du dossier existent.
- **Source :** `syntheses/registry.yml`, rapproché du registre indépendant `dossiers/registry.yml`.
- **Garde-fou :** plusieurs dossiers peuvent partager une synthèse ; compter chaque dossier une fois et dédupliquer les chemins de synthèse uniquement pour les diagnostics.

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

Le calculateur en lecture seule est prototypé dans `scripts/validate/calculate_project_kpis.py`. Avant toute intégration CI, vérifier ses sorties et mesurer son coût. Les trois premiers indicateurs ont désormais un dénominateur défendable sur l'instantané audité ; le quatrième reste un diagnostic.

| Indicateur | Faisabilité présumée | Vérification requise |
|---|---|---|
| Source-to-Knowledge | Bonne | Références typées, couverture du registre, exclusions et relations réellement exploitables |
| Evidence Verification | Conditionnelle | Schéma Claim, valeurs de statut, distinction entre revue et conclusion épistémique |
| Synthesis Coverage | Bonne | Rapprochement du registre indépendant des dossiers, unicité des associations et existence des deux fichiers |
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

Commandes locales :
```bash
python scripts/validate/calculate_project_kpis.py
python scripts/validate/calculate_project_kpis.py --format json --output /tmp/society-lab-kpis.json
```

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

1. Exécuter le calculateur et les tests sur l'instantané complet du dépôt ; vérifier les trois ratios et les listes d'anomalies.
2. Mesurer le coût du calcul sur le corpus courant, puis sur des charges ×10 et ×100, en séparant parsing et calcul si utile.
3. Examiner les 51 sources sans relation documentaire retenue ; distinguer les sources de contexte des omissions d'intégration, sans ajouter de liens artificiels.
4. Maintenir les définitions des statuts de claims et l'éligibilité des dossiers à partir des schémas canoniques.
5. Définir, si cela apporte une information utile, des règles d'éligibilité par type d'objet pour les diagnostics de connectivité.
6. Ajouter le calcul en CI seulement après validation des sorties et du coût marginal ; ne pas créer de seuil de KPI bloquant.

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

**Décision de méthode :** l'audit de faisabilité est documenté et un calculateur en lecture seule ainsi que ses tests sont ajoutés dans la branche de travail. Ils ne sont pas encore intégrés à la CI : les résultats automatisés et le coût doivent d'abord être vérifiés.


## 12. Résultat de l'audit de faisabilité du 18 novembre 2026

L'audit concret et sa méthode sont consignés dans [`project-kpis-feasibility-audit-2026-11-18.md`](project-kpis-feasibility-audit-2026-11-18.md).

| KPI retenu après audit | Définition opérationnelle | Instantané vérifié |
|---|---|---:|
| Couverture documentaire des sources | Sources avec au moins une relation documentaire typée, justifiée et dont les deux endpoints existent / sources du registre | 169/220 (76,8 %) |
| Claims avec conclusion documentée | Claims actifs avec un statut conclusif / claims actifs non superseded | 28/80 (35 %) |
| Couverture des synthèses | Dossiers actifs ayant une association unique et deux fichiers existants / dossiers actifs | 25/25 (100 %) |
| Connectivité du graphe | Objets éligibles ayant au moins une relation attendue et justifiée / objets éligibles | Diagnostic ; règles d'éligibilité par type manquantes |

**Contrôle du graphe :** 633 relations analysées ; aucune justification vide, aucun identifiant ou triplet de relation dupliqué et aucun endpoint inconnu. Le contrôle des endpoints indexe les sources, claims, dossiers, études, jeux de données, hypothèses, concepts, domaines, territoires et identifiants de synthèse. Les relations `REL-ABOUT` seules restent exclues du KPI de couverture documentaire.

**Couverture des synthèses :** le registre `dossiers/registry.yml` fournit le dénominateur indépendant. Les 25 dossiers actifs sont présents exactement une fois dans `syntheses/registry.yml` ; les 11 fichiers de synthèse distincts existent. Le partage d'une synthèse entre plusieurs dossiers est intentionnel.

**Correction de schéma :** le champ d'état des claims est `status`, pas `review_status`. Les vérifications documentaires par source sont enregistrées séparément dans `source_verifications` et ne doivent pas être confondues avec le statut épistémique du claim.

Le calculateur en lecture seule et ses tests sont maintenant ajoutés. L'intégration CI reste différée jusqu'à l'exécution des tests, la vérification du rapport réel et le benchmark sur corpus courant, ×10 et ×100. Aucun score composite ni objectif arbitraire n'est introduit.
