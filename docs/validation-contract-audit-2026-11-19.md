# Audit ciblé des contrats de validation — 19 novembre 2026

## Portée et méthode

Audit en lecture seule du dépôt `JM-Brun/society-lab` sur la branche `main`, à partir des registres canoniques, du graphe YAML, des schémas JSON et du validateur. Les écarts de rapprochement sont des éléments à arbitrer, pas des erreurs automatiquement corrigibles.

## 1. PR #179 — intégration vérifiée

La PR [#179](https://github.com/JM-Brun/society-lab/pull/179) est **fusionnée** dans `main` par le commit `afe4c8cf15914c7fb8a1b13b1498b6154333aa52`.

Sur le commit de correction `8d91d66db81c18d147b97be4b2143155b23f7694`, les workflows déclenchés par la PR sont terminés avec succès :
- **Validate knowledge base** : succès ; job `validate`, dont tests unitaires et validation JSON Schema ;
- **Secret scanning** : succès.

Le statut combiné du commit de merge ne publie pas de statuts individuels (liste vide), mais les deux exécutions PR sont explicitement terminées avec `conclusion=success`. Les contrôles métier ajoutés détectent auto-parenté/cycles territoriaux et incohérences des inverses déclarés. Les inverses réservés non déclarés restent tolérés.

## 2. Taxonomies : slugs de domaines et groupes de tags

État observé :
- 15 domaines dans `knowledge/TAXONOMY.yml` ;
- 15 slugs présents, valides et uniques sans distinction de casse ;
- 38 tags dans `knowledge/TAGS.yml` ;
- six groupes utilisés : `method` (11), `evidence` (5), `status` (3), `lens` (6), `scale` (11), `horizon` (2).

Le validateur contrôlait déjà l'unicité des identifiants DOMAIN/TAG, mais pas l'unicité/forme des slugs ni l'appartenance des tags à un vocabulaire de groupes. Cette PR ajoute :
- une syntaxe de slug stable `^[a-z0-9]+(?:-[a-z0-9]+)*$` ;
- l'unicité des slugs sans distinction de casse ;
- une liste explicite des six groupes effectivement utilisés, avec rejet des groupes inconnus ou absents ;
- des tests positifs et négatifs.

Toute introduction d'un nouveau groupe doit donc être accompagnée d'une décision taxonomique, de sa documentation et d'un test. Aucun tag existant n'est renommé ni déplacé.

## 3. Références géographiques : inventaire et contrat proposé

### Constat mesuré

Les quatre registres portant actuellement le champ `geographic_scope` contiennent :
- sources : 183 fiches sur 220, 233 valeurs ;
- études : 62 sur 62, 97 valeurs ;
- jeux de données : 14 sur 14, 20 valeurs ;
- dossiers : 25 sur 25, 64 valeurs.

Soit **284 fiches, 414 valeurs et 50 libellés distincts**. Aucun de ces enregistrements ne contient actuellement d'identifiant `TERRITORY-*` dans les registres examinés.

Les valeurs mélangent plusieurs sémantiques :
- territoires administratifs ou lieux : France, Loire-Atlantique, Nantes, Nantes Métropole, Île de Nantes ;
- ensembles géographiques ou politiques : Europe, Union européenne, zone euro, international ;
- échantillons/comparateurs : 17 pays, 27 pays européens, comparateurs OCDE, OCDE ;
- unités administratives ou d'observation : académies, régions, départements, établissements ;
- territoires infranationaux ou systèmes juridiques distincts : Flandre, Wallonie, England and Wales, Scotland, Northern Ireland ;
- valeurs incertaines : « À préciser à partir du texte intégral », « Expérience d'enquête ; contexte à préciser dans le texte intégral ».

Ces valeurs ne sont donc ni toutes des territoires, ni toutes des périmètres administratifs, ni toutes convertibles vers le référentiel territorial.

### Inventaire reproductible par révision Git

Le [script d'inventaire](../scripts/audit/report_geographic_scopes.py) lit les quatre registres et le référentiel des territoires à la même révision. Le JSON donne les occurrences, les identifiants des fiches et les éventuels identifiants territoriaux dont le libellé est exactement identique. Il signale aussi les correspondances multiples. Les libellés d'origine sont conservés avec leur casse, leurs accents et leurs qualifications.

```bash
python scripts/audit/report_geographic_scopes.py --revision HEAD > /tmp/geographic-scopes.json
```

Sur `6c6b982e21ee27aba7d6607c4492786ac82c4cf9`, l'exécution retrouve 284 fiches renseignées, 414 occurrences et 50 libellés distincts. Sept libellés (199 occurrences) ont une correspondance textuelle unique avec le référentiel. Les 43 autres (215 occurrences) restent à interpréter. Cette mesure indique une concordance de libellés et ne valide pas l'équivalence des périmètres.

| Cas observé | Question à résoudre avant tout rattachement |
|---|---|
| `France`, `Europe`, `Nantes Métropole` | Le contexte de la fiche correspond-il au territoire, à la juridiction, à l'institution ou à une aire fonctionnelle ? |
| `France hors Mayotte`, `France métropolitaine` | Le périmètre exact doit rester visible. Une référence générale à la France ferait perdre la qualification. |
| `International`, `OCDE`, `17 pays`, `Établissements` | Examiner le rôle du libellé : échelle relationnelle, comparateur, échantillon ou unité d'observation. |
| `Belgique`, `Wallonie`, `Flandre` | Les lieux n'ont pas de libellé équivalent dans le référentiel actuel. Toute extension nécessite une décision sur leur périmètre et leur rôle. |

L'inventaire traite les champs `geographic_scope` au premier niveau. Les champs imbriqués de géographie des claims et prévisions portent d'autres contrats. Ce rapport est une aide à la revue du modèle et s'exécute à la demande.

### Contrat recommandé — sans migration immédiate

1. **Conserver `geographic_scope`** comme champ textuel historique, lisible et non destructif. Ne pas le remplacer par des identifiants.
2. Réserver les identifiants `TERRITORY-*` aux lieux/territoires explicitement représentés dans `knowledge/TERRITORIES.yml`. Un groupe de pays, une population, une juridiction, un échantillon, un comparateur ou une aire fonctionnelle ne devient pas automatiquement un territoire.
3. À terme, ajouter un champ facultatif distinct (par exemple `geographic_scope_ids`) dans les schémas concernés, en complément du texte. Il ne contiendrait que les correspondances exactes validées humainement ; les valeurs non résolues resteraient dans le champ textuel.
4. Distinguer dans la documentation le territoire étudié, la juridiction compétente, l'aire fonctionnelle, le territoire vécu et le groupe de comparaison. Le lien parent géographique ne doit pas servir à encoder une simple proximité ou une relation institutionnelle.
5. Procéder par lots : inventaire des libellés, proposition de correspondances, revue humaine, ajout des identifiants facultatifs, contrôle des références, puis seulement mesure de couverture. Garder les valeurs d'origine et journaliser toute normalisation.

**Décision :** aucune conversion automatique n'est effectuée dans cette PR. Le contrat doit être approuvé avant toute évolution des schémas ou des fiches.

## 4. Relations des fiches et arêtes du graphe

Le [rapport de rapprochement](../scripts/audit/report_graph_reconciliation.py) recalcule les écarts ci-dessous à partir de révisions Git. Il compare `study_ids`, `claim_ids`, `hypothesis_ids` et `concept_ids` des dossiers avec `REL-INCLUDES`, puis `dataset_ids` des études avec `REL-USES`.

```bash
python scripts/audit/report_graph_reconciliation.py --format json
python scripts/audit/report_graph_reconciliation.py --revision HEAD --base origin/main
```

Le rapport fournit les paires propres à chaque côté et, avec `--base`, les paires apparues ou disparues de chaque catégorie. La disparition d'un écart peut venir d'un alignement des représentations ou du retrait d'une référence. Le workflow de validation affiche le résumé à titre indicatif et publie le JSON complet dans l'artefact `graph-reconciliation`. Sur une PR, il compare le commit de fusion testé avec la révision de base indiquée par GitHub. Les modifications locales doivent être commitées pour figurer dans le rapport.

Les [exceptions documentées](../governance/graph-reconciliation-exceptions.yml) sont lues dans la révision auditée. Chaque entrée précise le champ, le côté, les deux identifiants et la raison. Le résumé et le JSON distinguent les écarts à examiner, les exceptions qui correspondent à un écart et les décisions sans écart correspondant. Les listes brutes et le calcul des écarts apparus ou disparus restent consultables. Si le motif d'une décision évolue, mettre à jour l'entrée dans le même changement. Une révision antérieure au fichier d'exceptions s'audite avec une liste vide.

Le graphe contient **684 arêtes** : ABOUT 168, SUPPORTS 87, INCLUDES 326, USES 6, GEOGRAPHICALLY-WITHIN 7, CHILD-OF 8, SUMMARIZED-BY 8, TRANSCRIBES 21, SUMMARIZES 1, QUALIFIES 8 et CITES 44.

Le rapprochement des références explicites des dossiers avec les arêtes `REL-INCLUDES` donne :

| Références déclarées dans les dossiers | Paires déclarées | Paires présentes dans le graphe | Absentes du graphe | Paires du graphe non déclarées dans les fiches |
|---|---:|---:|---:|---:|
| `study_ids` | 45 | 38 | 7 | 10 |
| `claim_ids` | 49 | 40 | 9 | 22 |
| `hypothesis_ids` | 34 | 22 | 12 | 0 |
| `concept_ids` | 17 | 11 | 6 | 0 |
| **Total** | **145** | **111** | **34** | **32** |

Pour les études, 6 références `dataset_ids` sont déclarées ; 5 correspondent à une arête `REL-USES` étude → dataset. La paire absente est `STUDY-PARCOURSUP-ADMISSIONS-2026 → DATASET-PARCOURSUP-2026-INDICATORS`.

### Paires à arbitrer

**Références de fiches absentes de `REL-INCLUDES` :**

- `study_ids` :
  - `DOSSIER-SMIC-FRANCE-TRADEOFFS → STUDY-CAHUC-CARCILLO-LE-BARBANCHON-2019-HIRING-CREDITS`
  - `DOSSIER-SMIC-INDEXATION-DECOMPOSITION → STUDY-CAHUC-CARCILLO-LE-BARBANCHON-2019-HIRING-CREDITS`
  - `DOSSIER-SMIC-FACTORS-TRANSMISSION-2026 → STUDY-EXPERTS-SMIC-2025`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → STUDY-KRAUSE-COHEN-ABOU-CHADI-2023-ACCOMMODATION`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → STUDY-WAGNER-MEYER-2016-IDEOLOGICAL-LANDSCAPE`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → STUDY-DE-LEEUW-BOURNE-2020-PARTY-BANS-ESS`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → STUDY-BIARD-2021-DIACHRONIC-CORDON`
- `claim_ids` :
  - `DOSSIER-PARCOURSUP-EDUCATION-EQUITY → CLAIM-PARCOURSUP-2026-NEW-BACHELORS-OFFER`
  - `DOSSIER-PARCOURSUP-EDUCATION-EQUITY → CLAIM-PARCOURSUP-2026-LYCEENS-OFFER`
  - `DOSSIER-PARCOURSUP-EDUCATION-EQUITY → CLAIM-INSEE-EARLY-SOCIAL-GAPS`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → CLAIM-EUROPE-ACCOMMODATION-NOT-ELECTORAL-CURE-2023`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → CLAIM-WESTERN-EUROPE-IDEOLOGICAL-SHIFT-1980-2014`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → CLAIM-BELGIUM-CORDON-THREE-DECADES-INSTITUTIONAL-ACCESS`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → CLAIM-EUROPE-PARTY-BANS-SOCIAL-LEGITIMACY-ESS-2002-2010`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → CLAIM-EXPOSURE-UNCHECKED-EXTREME-INTERVIEWS-ATTITUDES-NORMS-2025`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → CLAIM-DUTCH-MEDIA-ACCOMMODATION-NORMALIZATION-2022`
- `hypothesis_ids` :
  - `DOSSIER-SMIC-HISTORICAL-EPISODES → HYPOTHESIS-SMIC-EMPLOYMENT-EFFECT-HETEROGENEOUS`
  - `DOSSIER-SMIC-HISTORICAL-EPISODES → HYPOTHESIS-SMIC-WAGE-COMPRESSION-CAREER`
  - `DOSSIER-SMIC-HISTORICAL-EPISODES → HYPOTHESIS-SMIC-PURCHASING-POWER-POVERTY`
  - `DOSSIER-SMIC-INDEXATION-DECOMPOSITION → HYPOTHESIS-SMIC-EMPLOYMENT-EFFECT-HETEROGENEOUS`
  - `DOSSIER-SMIC-INDEXATION-DECOMPOSITION → HYPOTHESIS-SMIC-WAGE-COMPRESSION-CAREER`
  - `DOSSIER-SMIC-CAUSAL-EVIDENCE-MATRIX → HYPOTHESIS-SMIC-EMPLOYMENT-EFFECT-HETEROGENEOUS`
  - `DOSSIER-SMIC-CAUSAL-EVIDENCE-MATRIX → HYPOTHESIS-SMIC-WAGE-COMPRESSION-CAREER`
  - `DOSSIER-SMIC-QUANTITATIVE-UPDATE-2026 → HYPOTHESIS-SMIC-PURCHASING-POWER-POVERTY`
  - `DOSSIER-SMIC-FACTORS-TRANSMISSION-2026 → HYPOTHESIS-SMIC-WAGE-COMPRESSION-CAREER`
  - `DOSSIER-SMIC-FACTORS-TRANSMISSION-2026 → HYPOTHESIS-SMIC-RELIEF-LOW-WAGE-TRAP`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → HYPOTHESIS-BOUNDARY-NORM-WITHOUT-VOTER-STIGMA`
  - `DOSSIER-SMIC-CAHUC-CARCILLO-LEBARBANCHON-2019-HIRING-CREDIT → HYPOTHESIS-SMIC-EMPLOYMENT-EFFECT-HETEROGENEOUS`
- `concept_ids` :
  - `DOSSIER-PREF-2026-ROBUSTNESS-AUDIT → CONCEPT-ROBUSTNESS-OF-TRANSITION`
  - `DOSSIER-PREF-2026-ROBUSTNESS-AUDIT → CONCEPT-SCENARIO-SENSITIVITY-ANALYSIS`
  - `DOSSIER-ENERGY-SCENARIOS-COMPARISON-2026 → CONCEPT-ROBUSTNESS-OF-TRANSITION`
  - `DOSSIER-ENERGY-SCENARIOS-COMPARISON-2026 → CONCEPT-SCENARIO-SENSITIVITY-ANALYSIS`
  - `DOSSIER-ENERGY-SCENARIOS-QUANTITATIVE-2026 → CONCEPT-ENERGY-ACCOUNTING-PERIMETER`
  - `DOSSIER-ENERGY-SCENARIOS-QUANTITATIVE-2026 → CONCEPT-SCENARIO-SENSITIVITY-ANALYSIS`

**Arêtes `REL-INCLUDES` présentes dans le graphe mais absentes des listes des fiches :**

- `study_ids` :
  - `DOSSIER-SMIC-FRANCE-TRADEOFFS → STUDY-HCREP-EXEMPTIONS-2024`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → STUDY-PORTER-WOOD-2024-FACTUAL-CORRECTIONS`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → STUDY-WOOD-ETAL-2024-DEBRIEFING-MISINFORMATION`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → STUDY-HORTA-RIBEIRO-ETAL-2023-PARLER-DEPLATFORMING`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → STUDY-KLINENBERG-2024-DEPLATFORMING-CREATORS`
  - `DOSSIER-DEBATE-BARRAGE-CORDON-SANITAIRE → STUDY-REACTANCE-META-2026`
  - `DOSSIER-CORDON-SANITAIRE-BELGIQUE-EFFICACITE → STUDY-DE-JONGE-2021-BELGIUM-CORDON`
  - `DOSSIER-CORDON-SANITAIRE-BELGIQUE-EFFICACITE → STUDY-YE-ETAL-2026-ILLUSORY-TRUTH-META`
  - `DOSSIER-CORDON-SANITAIRE-BELGIQUE-EFFICACITE → STUDY-ECKER-ETAL-2020-FAMILIARITY-BACKFIRE`
  - `DOSSIER-SMIC-CAUSAL-EVIDENCE-MATRIX → STUDY-CAHUC-CARCILLO-LE-BARBANCHON-2019-HIRING-CREDITS`
- `claim_ids` :
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-TIG-RECIDIVISM-RAW-5Y-2010`
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-TIG-RECIDIVISM-ADJUSTED-5Y`
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-TIG-RECIDIVISM-PRISON-SENTENCE-10Y`
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-TIG-RECIDIVISM-CONVICTION-COUNT-10Y`
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-TIG-COST-PRISON-COMPARISON-UNIT-2022`
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-TIG-HOST-ORGANISATIONS-COSTS-EXCLUDED-2025`
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-TIG-TUTOR-TIME-100H-2025`
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-TIG-TERRITORIAL-COST-DDSE-2022`
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-TIG-SPIP-ASSIGNMENT-DELAY-2023-2024`
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-TIG-OUTCOME-THREE-YEARS-2025`
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-NETHERLANDS-TAAKSTRAF-EXECUTION-OUTCOMES-2024`
  - `DOSSIER-SMIC-FRANCE-TRADEOFFS → CLAIM-SMIC-EXEMPTIONS-TOTAL-2024-HCREP`
  - `DOSSIER-SMIC-FRANCE-TRADEOFFS → CLAIM-SMIC-EXEMPTIONS-EXPERTS-75BN-2024`
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-TIG-EXECUTED-WITHIN-3Y-2020`
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-TIG-CONVERTED-WITHIN-3Y-2020`
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-TIG-UNEXECUTED-AT-3Y-2020`
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-TIG-FAILURE-ATTRIBUTABLE-3Y-2020`
  - `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE → CLAIM-TIG-COUR-SAMPLE-DELAY-2023-2024`
  - `DOSSIER-SMIC-FRANCE-TRADEOFFS → CLAIM-SMIC-COTTET-MW-JOBS-1995-1999`
  - `DOSSIER-SMIC-FRANCE-TRADEOFFS → CLAIM-SMIC-COTTET-FIRM-GROWTH-1995-1997`
  - `DOSSIER-SMIC-FRANCE-TRADEOFFS → CLAIM-SMIC-ALBERTINI-5PCT-MW-EMPLOYMENT`
  - `DOSSIER-SMIC-FRANCE-TRADEOFFS → CLAIM-SMIC-ALBERTINI-5PCT-MW-FISCAL-SURPLUS`

Ces paires sont des écarts observés entre deux représentations. Elles ne constituent pas une consigne d'ajouter/supprimer les liens : chaque paire doit être examinée au regard du contenu du dossier, du sens de `REL-INCLUDES` et de la provenance de la relation.


Interprétation et garde-fous :
- ces champs de fiche et les arêtes sont deux représentations qui se recouvrent partiellement, pas nécessairement des duplications sémantiquement identiques ;
- `source_ids` sur une étude ou un claim n'implique pas à lui seul une arête `SUPPORTS` : la référence bibliographique ne prouve pas que la source étaye le claim ;
- les liens d'inclusion d'un dossier, l'utilisation d'un dataset et l'appui probatoire sont des relations différentes ;
- les 34 liens présents dans les fiches mais absents du graphe, les 32 liens du graphe absents des listes de fiches et le lien étude→dataset manquant doivent être arbitrés individuellement ;
- ne pas synchroniser automatiquement les deux côtés, ni supprimer les arêtes supplémentaires avant d'avoir identifié la source de vérité et le sens métier de chaque champ.

Le validateur actuel contrôle l'existence et le typage des arêtes, ainsi que plusieurs références croisées des fiches ; il ne garantit pas leur équivalence exhaustive. Le prochain livrable doit être une matrice de correspondance par champ et type de relation, avec exceptions justifiées et décision de source de vérité.

## 5. Contraintes conditionnelles des schémas

L'inspection des schémas montre des conditions métier dans :
- `schemas/mechanism.schema.json` : un mécanisme à statut probant (supported/mixed/challenged/rejected) doit fournir au moins un lien vers études ou claims ;
- `schemas/ingestion-batch.schema.json` : règles conditionnelles pour les décisions selected, duplicate, excluded, inaccessible, et pour la clôture d'un lot ;
- `schemas/forecast.schema.json` : aucune règle `if/then` ou `oneOf/anyOf` conditionnelle repérée ; les contraintes sont actuellement principalement structurelles et bornées.

Cette PR ajoute une suite de tests dédiée qui vérifie les cas valides et invalides des conditions mechanism et ingestion-batch, y compris chaque décision et le statut closed. Elle ne modifie pas les schémas ni les données.

## 6. Scalabilité ×10 / ×100

Le corpus de référence interrogé comprend 441 fiches dans les neuf registres canoniques (220 sources, 62 études, 14 datasets, 83 claims, 22 hypothèses, 25 dossiers, 15 concepts, 0 mécanisme et 0 forecast), plus 684 arêtes. Ces volumes sont le point de départ.

La PR ajoute `scripts/audit/benchmark_validation_scale.py`, exécuté par `tests/test_validation_scale_benchmark.py` sur les facteurs ×1, ×10 et ×100. Le script :
- clone les objets avec des identifiants uniques et remappe leurs références internes ;
- conserve les taxonomies partagées et évite de dupliquer les arêtes territoriales statiques ;
- exécute les validations de schémas, d'identifiants, de références croisées et d'arêtes sur les corpus synthétiques ;
- rapporte le nombre de fiches/arêtes, le temps de construction du corpus synthétique, le temps de validation, le temps total et le pic mémoire Python.

**Limite de mesure :** le benchmark couvre la validation des registres et du graphe en mémoire ; il ne mesure pas la génération du site, les appels externes, ni la qualité scientifique. Les chiffres seront ceux du runner GitHub Actions et doivent être interprétés comme un benchmark comparatif reproductible, non comme une mesure universelle.

Mesures relevées sur GitHub Actions (Python 3.12.16, runner hébergé), commit `6a94213` :

| Échelle | Fiches | Arêtes | Construction du corpus | Validation | Total | Pic mémoire Python |
|---|---:|---:|---:|---:|---:|---:|
| ×1 | 441 | 684 | 22,86 ms | 650,29 ms | 675,27 ms | 0,76 MiB |
| ×10 | 4 410 | 6 777 | 136,39 ms | 3 108,48 ms | 3 262,93 ms | 7,36 MiB |
| ×100 | 44 100 | 67 707 | 1 394,88 ms | 27 703,76 ms | 29 311,15 ms | 75,36 MiB |

Chargement YAML du corpus de base : 772,57 ms. Le temps de validation est environ ×4,78 à ×10 et ×42,60 à ×100 par rapport à ×1 ; le temps total est environ ×4,83 et ×43,41. Le pic mémoire augmente approximativement avec le volume. Sur ce benchmark synthétique, aucun emballement quadratique évident n'apparaît jusqu'à ×100, avec un temps total ×100 d'environ 29,3 secondes. Cette observation ne vaut pas preuve de performance pour des corpus dont les distributions, tailles de champs ou graphes seraient très différentes.

La CI du commit `6a94213` est entièrement verte : 145 tests réussis, validation des schémas réussie, inventaire des registres généré, scan de secrets réussi. Les seuils de régression devront être définis à partir de plusieurs exécutions comparables, en tenant compte de la variabilité des runners.

## 7. Arbitrage du lot Parcoursup et éducation — 20 novembre 2026

Le rapprochement a été recalculé sur `413cce97adbc485f5d2e138e25d1289b759a366e` pour [l'issue #114](https://github.com/JM-Brun/society-lab/issues/114). Le lot confronte les champs de la [fiche dossier](../dossiers/registry.yml), du [registre des claims](../claims/registry.yml) et des [études](../research/studies/registry.yml) au [dossier rédigé](../dossiers/parcoursup-education-equity.md), au [jeu d'indicateurs](../research/datasets/registry.yml) et aux arêtes existantes.

### Règles d'arbitrage appliquées

| Champ et sens de lecture | Relation à examiner | Décision et exception |
|---|---|---|
| `study_ids` et `claim_ids` d'un dossier | `REL-INCLUDES`, du dossier vers l'objet | Retenir la relation lorsque l'étude est mobilisée ou l'affirmation examinée dans le dossier à un emplacement identifiable. L'inclusion d'un claim conserve son statut et son périmètre. |
| `hypothesis_ids` d'un dossier | `REL-INCLUDES`, du dossier vers l'hypothèse | Vérifier que le dossier examine l'hypothèse comme piste de travail. Le statut de l'hypothèse relève de sa fiche. |
| `concept_ids` d'un dossier | `REL-INCLUDES`, `REL-ABOUT` ou `REL-USES` selon le rôle | L'inclusion correspond à un concept traité dans le dossier, `REL-ABOUT` à son sujet et `REL-USES` à un concept mobilisé pour l'analyse. Une arête existante peut donc expliquer un écart avec le seul décompte de `REL-INCLUDES`. |
| `dataset_ids` d'une étude | `REL-USES`, de l'étude vers le dataset | La fiche d'étude identifie le jeu et la revue confirme les données effectivement mobilisées. Une proximité thématique ne suffit pas. |
| Arête du graphe absente de la liste de la fiche | Relire la relation, sa justification et le dossier | Conserver l'arête si le dossier en justifie le sens. Compléter la liste de la fiche lorsque l'objet appartient à son périmètre déclaré. Consigner les cas ambigus pour revue. |

Les fiches canoniques établissent l'identité, le statut et les références déclarées des objets. Le dossier rédigé permet de vérifier la place de l'objet dans l'analyse. Le graphe expose la relation typée avec sa justification. Le rapprochement est un relevé d'écarts et son résultat dépend de la sémantique des champs et des arêtes comparés.

### Décisions par paire

| Objet de départ | Objet cible | Décision et ancrage documentaire |
|---|---|---|
| `DOSSIER-PARCOURSUP-EDUCATION-EQUITY` | `CLAIM-PARCOURSUP-2026-NEW-BACHELORS-OFFER` | Ajouter `REL-INCLUDES`. « Fonctionnement et volumes de Parcoursup 2026 » présente les propositions reçues par les néo-bacheliers inscrits selon le SIES. |
| `DOSSIER-PARCOURSUP-EDUCATION-EQUITY` | `CLAIM-PARCOURSUP-2026-LYCEENS-OFFER` | Ajouter `REL-INCLUDES`. La même section mobilise le bilan ministériel pour les lycéens ayant fait des vœux. La fiche du claim documente la divergence entre le HTML et le PDF pour le pourcentage publié. |
| `DOSSIER-PARCOURSUP-EDUCATION-EQUITY` | `CLAIM-INSEE-EARLY-SOCIAL-GAPS` | Ajouter `REL-INCLUDES`. « Les inégalités se forment en amont » cite l'Insee et situe les écarts d'acquis dans la chaîne éducative. |
| `STUDY-PARCOURSUP-ADMISSIONS-2026` | `DATASET-PARCOURSUP-2026-INDICATORS` | Ajouter `REL-USES`. La référence `dataset_ids` est explicite et les catégories et agrégats de la fiche dataset correspondent à ceux que l'étude reprend du bilan et de la note Flash. |

Après correction, le dossier Parcoursup a zéro divergence pour les quatre champs comparés et les 6 paires étude–dataset déclarées dans le dépôt ont une arête `REL-USES`. À l'échelle des dossiers, 31 paires déclarées restent sans `REL-INCLUDES` et 33 arêtes `REL-INCLUDES` restent hors des listes examinées. Le recomptage avant correction était de 34 et 33. Le décompte historique de la section 4 en comptait 32 dans le second sens, avant l'ajout du lien du dossier SMIC vers `CLAIM-SMIC-DEC-2026-ANNOUNCED-INCREASE`. Les **64 écarts restants** exigent une revue par dossier. Les statuts probatoires, le contrat géographique et les schémas sont hors périmètre de ce lot.

## 8. Arbitrage du lot TIG — 20 novembre 2026

Le rapport de rapprochement sur `4261bb105b0462b56b302560da5ff313e4d28b31` relève 16 arêtes `REL-INCLUDES` du dossier `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE` dont la cible n'apparaît pas dans ses `claim_ids`. La revue compare chaque affirmation du [registre](../claims/registry.yml) au passage correspondant du [dossier TIG](../dossiers/tig-peines-alternatives-incarceration.md). Quinze cibles sont reprises dans la [fiche canonique](../dossiers/registry.yml), avec leur statut `under_review`.

| Passage du dossier | Affirmations ajoutées aux références de la fiche | Justification |
|---|---|---|
| §§3.1–3.2, récidive et biais de sélection | `CLAIM-TIG-RECIDIVISM-RAW-5Y-2010`, `CLAIM-TIG-RECIDIVISM-ADJUSTED-5Y`, `CLAIM-TIG-RECIDIVISM-PRISON-SENTENCE-10Y`, `CLAIM-TIG-RECIDIVISM-CONVICTION-COUNT-10Y` | Le dossier distingue le taux brut à cinq ans, l'écart ajusté à cinq ans, puis la recondamnation à de la prison ferme et le nombre cumulé de condamnations à dix ans. |
| §§5.1–5.4, périmètre des coûts | `CLAIM-TIG-HOST-ORGANISATIONS-COSTS-EXCLUDED-2025`, `CLAIM-TIG-TUTOR-TIME-100H-2025`, `CLAIM-TIG-COST-PRISON-COMPARISON-UNIT-2022`, `CLAIM-TIG-TERRITORIAL-COST-DDSE-2022` | Les passages documentent les coûts d'accueil exclus, le tutorat déclaré, la comparaison entre unités différentes et les deux estimations territoriales de DDSE. |
| §§14.1 et 14.2, exécution en France et aux Pays-Bas | `CLAIM-TIG-SPIP-ASSIGNMENT-DELAY-2023-2024`, `CLAIM-NETHERLANDS-TAAKSTRAF-EXECUTION-OUTCOMES-2024` | Les passages identifient l'étape française saisine–affectation et le périmètre néerlandais des données sur le taakstraf. |
| §§15.2–15.3, enquête de délais et cohorte nationale | `CLAIM-TIG-COUR-SAMPLE-DELAY-2023-2024`, `CLAIM-TIG-EXECUTED-WITHIN-3Y-2020`, `CLAIM-TIG-CONVERTED-WITHIN-3Y-2020`, `CLAIM-TIG-UNEXECUTED-AT-3Y-2020`, `CLAIM-TIG-FAILURE-ATTRIBUTABLE-3Y-2020` | Le dossier distingue la mesure du délai sur neuf territoires et la ventilation en quatre issues à 36 mois de la cohorte nationale. |

L'arête vers `CLAIM-TIG-OUTCOME-THREE-YEARS-2025` reste dans le graphe. Sa justification pointe vers l'ancienne ventilation agrégée citée au §14.1. La fiche dossier référence les quatre affirmations distinctes du §15.3. Le rapport mécanique continue donc de signaler cet unique écart TIG, qualifié ici comme historique. L'audit recense **49 écarts au total** après correction, dont cet écart documenté. Les 48 autres écarts restent à examiner.

## 9. Arbitrage du lot scénarios énergétiques — 20 novembre 2026

Le rapport de rapprochement sur `63f2e78d6ee9f914e9a8ae19d37ba0906a85ed27` relève six références `concept_ids` sans arête `REL-INCLUDES`. Les décisions ci-dessous reposent sur le texte des dossiers et les définitions du [registre des concepts](../knowledge/concepts/registry.yml).

| Dossier | Concept | Décision et passage |
|---|---|---|
| [Audit du PREF](../dossiers/pref-2026-audit-robustesse-scenarios.md) | Robustesse d'une trajectoire | Ajouter `REL-INCLUDES`. Le §3.3 définit la robustesse, la distingue de la résilience et donne les critères d'évaluation. |
| Audit du PREF | Analyse de sensibilité | Ajouter `REL-INCLUDES`. Les §§3.2 et 5.3 décrivent les variantes de réussite et leur interprétation conditionnelle. |
| [Comparaison des trajectoires](../dossiers/comparaison-scenarios-transition-pref-rte-ademe-negawatt-snbc3.md) | Robustesse d'une trajectoire | Ajouter `REL-INCLUDES`. Le §3.1 présente la robustesse du PREF et le §5 en fait un axe de comparaison. |
| Comparaison des trajectoires | Analyse de sensibilité | Ajouter `REL-INCLUDES`. Les §§5–6 proposent de tester les conclusions sous différentes hypothèses de sobriété. Le lien décrit un protocole, avec des tests encore à conduire. |
| [Comparaison quantitative](../dossiers/comparaison-quantitative-scenarios-energie-2026.md) | Périmètre comptable énergétique | Conserver `REL-ABOUT` (`REL-QUANT-DOSSIER-USES-BOUNDARY-CONCEPT`). Les §§1 et 6 font des conventions de bilan un sujet central. Le rapport fondé sur `REL-INCLUDES` continue de signaler cette paire, qualifiée ici comme thématique. |
| Comparaison quantitative | Analyse de sensibilité | Retirer la référence de la fiche. Les §§5–7 rapprochent des chiffres publiés, distinguent leurs périmètres et prévoient l'extraction par variante. Le traitement de la sensibilité elle-même est documenté dans les deux dossiers précédents. |

Le lot traite les six paires. Le rapport mécanique passe de 49 à **44 écarts**, dont deux déjà arbitrés (l'ancienne ventilation TIG et le lien thématique de la comparaison quantitative). **42 paires** restent à examiner. Parmi les cinq écarts retirés du rapport, quatre correspondent à des arêtes ajoutées et un à une référence de fiche retirée.

## 10. Arbitrage SMIC : facteurs de transmission et matrice des preuves — 20 novembre 2026

Le rapport de rapprochement sur `f28ebf4e3cf00991f14cb40c1fd08730f5e6061e` signalait sept paires pour ces deux dossiers. Chaque relation a été vérifiée dans le texte et les registres.

| Dossier | Objet | Décision et ancrage |
|---|---|---|
| [Facteurs de transmission](../dossiers/smic-facteurs-mecanismes-transmission-2026.md) | `STUDY-EXPERTS-SMIC-2025` | Ajouter `REL-INCLUDES`. Le §3 reprend la projection pour janvier 2026 et la recommandation du rapport. |
| Facteurs de transmission | `CLAIM-SMIC-DEC-2026-ANNOUNCED-INCREASE` | Ajouter à `claim_ids`. Le §3 et l'addendum du 19 novembre décrivent le montant, la date et la ventilation annoncés. |
| Facteurs de transmission | `HYPOTHESIS-SMIC-WAGE-COMPRESSION-CAREER` | Ajouter `REL-INCLUDES`. Le §1 décrit le canal des minima conventionnels et de la compression des grilles. |
| Facteurs de transmission | `HYPOTHESIS-SMIC-RELIEF-LOW-WAGE-TRAP` | Ajouter `REL-INCLUDES`. Les §§1 et 3 relient le profil des allègements au risque de trappe à bas salaires. |
| [Matrice des preuves](../dossiers/smic-causal-evidence-matrix.md) | `STUDY-CAHUC-CARCILLO-LE-BARBANCHON-2019-HIRING-CREDITS` | Ajouter à `study_ids`. Le complément sur le crédit d'embauche présente l'évaluation de l'aide temporaire aux nouvelles embauches. |
| Matrice des preuves | `HYPOTHESIS-SMIC-EMPLOYMENT-EFFECT-HETEROGENEOUS` | Ajouter `REL-INCLUDES`. Les §§2 et 10 examinent les variations des résultats d'emploi selon l'exposition et les groupes étudiés. |
| Matrice des preuves | `HYPOTHESIS-SMIC-WAGE-COMPRESSION-CAREER` | Ajouter `REL-INCLUDES`. Le §2 examine la diffusion salariale, la compression possible et la mobilité. |

Le rapport passe de 44 à 37 écarts, avec zéro écart sur ces deux dossiers. Il reste 35 paires à examiner et deux écarts déjà qualifiés dans les lots TIG et énergie. Les liens d'inclusion indiquent les objets traités dans les dossiers. La vérification probatoire relève des fiches d'études, de claims et d'hypothèses.

## 11. Arbitrage du dossier général sur le SMIC — 20 novembre 2026

Le rapport sur `c60ae8c327fc6886e04b2d5b74b05e1b70206788` relevait huit écarts pour `DOSSIER-SMIC-FRANCE-TRADEOFFS`. Les objets ci-dessous ont été rapprochés des passages du [dossier général](../dossiers/smic-france-tradeoffs.md) et des registres.

| Objets | Décision et ancrage |
|---|---|
| `STUDY-HCREP-EXEMPTIONS-2024`, `CLAIM-SMIC-EXEMPTIONS-TOTAL-2024-HCREP`, `CLAIM-SMIC-EXEMPTIONS-EXPERTS-75BN-2024` | Compléter la fiche. Le dossier cite la note HCREP et compare les agrégats en conservant la réserve sur leurs périmètres comptables. |
| `CLAIM-SMIC-COTTET-MW-JOBS-1995-1999`, `CLAIM-SMIC-COTTET-FIRM-GROWTH-1995-1997` | Compléter la fiche. Le §15.1 distingue les deux groupes d'entreprises et les résultats sur les emplois au SMIC et sur la croissance de l'emploi. |
| `CLAIM-SMIC-ALBERTINI-5PCT-MW-EMPLOYMENT`, `CLAIM-SMIC-ALBERTINI-5PCT-MW-FISCAL-SURPLUS` | Compléter la fiche. Le tableau du §15.2 présente les résultats simulés par scénario d'indexation pour les deux grandeurs. |
| `STUDY-CAHUC-CARCILLO-LE-BARBANCHON-2019-HIRING-CREDITS` | Conserver la référence de la fiche, expliciter son rôle au §15.1 et ajouter `REL-INCLUDES`. Le renvoi à l'audit existant compare une aide aux nouvelles embauches à une baisse de cotisations qui agit aussi sur la rétention des emplois. |

Le rapport passe de 37 à 29 écarts, dont deux déjà qualifiés dans les lots TIG et énergie. Le dossier général est réconcilié pour les champs comparés. Les résultats scientifiques gardent leur niveau de preuve et les six claims ajoutés à la fiche restent `under_review`.

## 12. Arbitrage des dossiers historiques et méthodologiques sur le SMIC — 20 novembre 2026

Sur `42d8b6fb6383724fa482ce07e267065efa3b3342`, les huit derniers écarts SMIC sont des références présentes dans les fiches. Le périmètre de chaque dossier a été vérifié avant arbitrage.

| Dossier | Objet | Décision et ancrage |
|---|---|---|
| [Épisodes historiques](../dossiers/smic-historical-episodes.md) | `HYPOTHESIS-SMIC-EMPLOYMENT-EFFECT-HETEROGENEOUS` | Ajouter `REL-INCLUDES`. Les §§3.2–3.3 et 5 discutent les populations, l'exposition et les mécanismes d'emploi à tester. |
| Épisodes historiques | `HYPOTHESIS-SMIC-WAGE-COMPRESSION-CAREER` | Ajouter `REL-INCLUDES`. Les §§3.5 et 5 traitent de la compression des grilles et de la progression salariale. |
| Épisodes historiques | `HYPOTHESIS-SMIC-PURCHASING-POWER-POVERTY` | Ajouter `REL-INCLUDES`. Les §§3.1 et 5 distinguent pouvoir d'achat au plancher et pauvreté en ménage. |
| [Décomposition de l'indexation](../dossiers/smic-indexation-decomposition.md) | `STUDY-CAHUC-CARCILLO-LE-BARBANCHON-2019-HIRING-CREDITS`, `HYPOTHESIS-SMIC-EMPLOYMENT-EFFECT-HETEROGENEOUS`, `HYPOTHESIS-SMIC-WAGE-COMPRESSION-CAREER` | Retirer ces références de la fiche. Les §§1 et 5 cadrent une décomposition réglementaire et arithmétique des revalorisations. L'emploi et les salaires sont mentionnés comme travaux à rapprocher au §7. Les objets restent reliés à la matrice des preuves. |
| [Actualisation quantitative](../dossiers/smic-quantitative-update-2026.md) | `HYPOTHESIS-SMIC-PURCHASING-POWER-POVERTY` | Retirer la référence de la fiche. La reconstruction porte sur le pouvoir d'achat horaire. La pauvreté des ménages est citée parmi les limites du calcul et l'hypothèse est traitée dans le dossier historique. |
| [Audit du crédit d'embauche](../dossiers/smic-cahuc-carcillo-le-barbanchon-2019-credit-embauche-zero-charges.md) | `HYPOTHESIS-SMIC-EMPLOYMENT-EFFECT-HETEROGENEOUS` | Retirer la référence de la fiche. Le §8 circonscrit le résultat à l'aide ciblée aux nouvelles embauches. L'étude reste reliée au dossier d'audit et à la matrice, où l'hypothèse sur les revalorisations du SMIC est examinée. |

Le rapport passe de 29 à 21 écarts et ne signale plus d'écart dans les dossiers SMIC. Les trois hypothèses ajoutées au graphe sont des objets discutés dans le dossier historique. Les cinq références retirées concernent les listes des fiches ; leurs objets canoniques, les textes et les liens de recherche cités restent disponibles. Sur les 21 écarts du dépôt, deux sont déjà qualifiés dans les lots TIG et énergie et 19 restent à examiner.

## 13. Arbitrage des dossiers sur le cordon sanitaire — 20 novembre 2026

Sur `9ad3ff7840e961fca972efec4b0627daa9219344`, les deux dossiers concentrent les 19 paires encore à examiner. Le lot rattache les objets déjà traités, avec 11 arêtes `REL-INCLUDES` et huit références d'étude ajoutées aux fiches.

| Dossier et passages | Discordances traitées | Décision |
|---|---|---|
| [Dossier général](../dossiers/debat-barrage-cordon-sanitaire.md), §§12.1–12.4 | Études de Biard, Wagner et Meyer, Krause et ses coauteurs, de Leeuw et Bourne et les quatre affirmations correspondantes | Huit arêtes d'inclusion pour les études et résultats discutés. Les objets distinguent accès institutionnel, évolution des programmes, accommodation électorale et soutien déclaré à une interdiction. |
| Dossier général, §§17.3–17.4 | Affirmations sur les interviews non contestées et la normalisation discursive dans la presse néerlandaise | Deux arêtes d'inclusion. Le premier objet relève d'expériences de court terme et le second d'une analyse du discours. |
| Dossier général, mise à jour sur les effets affectifs du front commun | Hypothèse de démarcation sans stigmatisation des électeurs | Une arête d'inclusion, justifiée par la discussion du risque de débordement. L'hypothèse reste proposée. |
| Dossier général, §§18.1–18.3 | Porter et Wood, Wood et ses coauteurs, méta-analyse sur la réactance, Horta Ribeiro et ses coauteurs, Klinenberg | Ajouter cinq études à la fiche. Les passages traitent des corrections, de la réactance et de la déplateformisation avec leurs indicateurs propres. |
| [Dossier belge](../dossiers/cordon-sanitaire-belgique-efficacite.md), §§3, 5.1 et 5.3 | De Jonge, Ye et ses coauteurs, Ecker et ses coauteurs | Ajouter trois études à la fiche avec les identifiants des arêtes existantes. La comparaison qualitative belge garde son périmètre et les deux études cognitives restent distinctes d'une évaluation du cordon. |

Le dossier belge reprend l'identifiant `STUDY-DE-JONGE-2021-BELGIUM-CORDON` déjà employé dans ses relations. Le rapprochement des deux fiches De Jonge qui renvoient au même DOI relève de l'audit d'ingestion. Le lot conserve les identifiants existants et les statuts probatoires.

Le rapport passe de 21 à deux écarts. Les deux paires encore signalées correspondent aux choix déjà documentés dans les sections 8 et 9 (ancienne ventilation TIG et lien thématique sur le périmètre énergétique). L'inventaire des écarts fiches–graphe est ainsi entièrement arbitré pour les règles actuelles. Les autres volets de l'issue #114, dont le contrat géographique et l'élargissement des mesures de performance, restent distincts.
