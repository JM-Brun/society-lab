# Audit des relations de sources et règles de connectivité — 18 novembre 2026

**Périmètre :** registre de 220 sources, graphe de connaissances et registres d'études/datasets de `main` (base `4cf86d22934127e68fc473257929fcf8fd2e113b`). Les relations ajoutées dans cette branche sont limitées aux usages explicitement vérifiables. Les liens bibliographiques ne sont pas présentés comme une validation scientifique indépendante.

## 1. Décisions sur les 13 sources sans relation incidente

| Source | Usage vérifié | Relation ajoutée / décision |
|---|---|---|
| `SOURCE-PRI-EU-NONCUSTODIAL-COMPARATIVE-2025` | `source_ids` de `STUDY-PRI-EU-NONCUSTODIAL-COMPARATIVE-2025` | `REL-CITES` étude → source |
| `SOURCE-WERMINK-COMMUNITY-SERVICE-RETRIBUTION-2023` | `source_ids` de `STUDY-WERMINK-NETHERLANDS-COMMUNITY-SERVICE-IV-2023` | `REL-CITES` étude → source |
| `SOURCE-FO-POUVOIR-ACHAT-2026` | Bibliographie de `dossiers/smic-social-partners-evidence.md`, fichier de travail non enregistré dans `dossiers/registry.yml` | **Aucun lien ajouté** : l'objet documentaire n'existe pas comme nœud du graphe. Décider séparément de l'enregistrer ou de documenter son rattachement |
| `SOURCE-UK-DFE-2024-HARASSMENT-CENSORSHIP` | Dossier `DOSSIER-CORDON-SANITAIRE-BELGIQUE-EFFICACITE`, données descriptives sur les refus de conférenciers et limites de mesure | `REL-INCLUDES` dossier → source |
| `SOURCE-TADROS-2022-RIGHTS-NOPLATFORMING` | Même dossier, analyse normative des droits et conditions de justification | `REL-INCLUDES` dossier → source |
| `SOURCE-LIBERAL-DEFENSE-NOPLATFORMING-2024` | Même dossier, argumentation normative en faveur du no-platforming non violent | `REL-INCLUDES` dossier → source |
| `SOURCE-VAN-DER-DOES-JACQUET-2023-SPILLOVER-REVIEW` | `source_ids` de `STUDY-VAN-DER-DOES-JACQUET-2023-SPILLOVER` | `REL-CITES` étude → source |
| `SOURCE-META-ANALYSIS-DEMOCRATIC-INNOVATIONS-2024` | `source_ids` de `STUDY-DEMOCRATIC-INNOVATIONS-META-ANALYSIS-2024` | `REL-CITES` étude → source |
| `SOURCE-GERMANN-2025-MINIPUBLIC-REPRESENTATIVENESS` | `source_ids` de `STUDY-GERMANN-2025-REPRESENTATIVENESS-LEGITIMACY` | `REL-CITES` étude → source |
| `SOURCE-CEREQ-GENERATION-2021-BTS-MATCHING-2026` | `source_ids` de `STUDY-CEREQ-GENERATION-2021-BTS-MATCHING` et dataset associé | `REL-CITES` étude → source |
| `SOURCE-DEPP-INSERJEUNES-2026` | `source_ids` de `STUDY-INSERJEUNES-INSERTION-2023` et dataset associé | `REL-CITES` étude → source |
| `SOURCE-OECD-PIAAC-DATA-METHODOLOGY-2023` | `source_ids` de `STUDY-PIAAC-2023-FRANCE-COMPETENCES` et dataset associé | `REL-CITES` étude → source |
| `SOURCE-INSEE-PANEL-TOUS-SALARIES-METADATA-2026` | `source_ids` de `STUDY-CEREQ-GENERATION-2021-BTS-MATCHING` et `STUDY-INSEE-PANEL-TOUS-SALARIES-TRAJECTORIES` | Deux relations `REL-CITES`, une par étude |

**Résultat :** 12 des 13 sources acquièrent une relation justifiée. La source FO reste volontairement non reliée jusqu'à résolution de la question du document non enregistré.

## 2. Décisions sur les 38 sources `REL-ABOUT` uniquement

### 2.1. 25 sources déclarées dans les registres d'études

Le champ `source_ids` de `research/studies/registry.yml` constitue une preuve de rattachement bibliographique. Les 25 sources ci-dessous sont reliées à l'étude qui les déclare. La source Sénat est déclarée dans deux études, ce qui donne 26 relations.

| Source | Étude |
|---|---|
| `SOURCE-PARCOURSUP-BILAN-2026` | `STUDY-PARCOURSUP-ADMISSIONS-2026` |
| `SOURCE-SIES-PARCOURSUP-2026-ADMISSIONS` | `STUDY-PARCOURSUP-ADMISSIONS-2026` |
| `SOURCE-DEPP-ETAT-ECOLE-2025` | `STUDY-SOCIAL-INEQUALITIES-SCHOOL-2025` |
| `SOURCE-INSEE-INEGALITES-SCOLAIRES-2025` | `STUDY-SOCIAL-INEQUALITIES-SCHOOL-2025` |
| `SOURCE-OECD-PISA-2022-FRANCE` | `STUDY-OECD-PISA-2022-FRANCE` |
| `SOURCE-OECD-EAG-2025-FRANCE` | `STUDY-OECD-INTERGEN-EDUCATION-ATTAINMENT-2025` |
| `SOURCE-PARCOURSUP-OPEN-DATA-2025` | `STUDY-PARCOURSUP-FORMATION-OPEN-DATA-2025` |
| `SOURCE-COUR-DES-COMPTES-PEINES-ALTERNATIVES-2025` | `STUDY-COUR-DES-COMPTES-TIG-DDSE-2025` |
| `SOURCE-MINISTERE-JUSTICE-TIG-PRONONCE-2024` | `STUDY-COUR-DES-COMPTES-TIG-DDSE-2025` |
| `SOURCE-MINISTERE-JUSTICE-TUTEURS-TIG-2024` | `STUDY-COUR-DES-COMPTES-TIG-DDSE-2025` |
| `SOURCE-SENAT-EXECUTION-PEINES-2025` | `STUDY-COUR-DES-COMPTES-TIG-DDSE-2025` et `STUDY-SENAT-EXECUTION-PEINES-2025` |
| `SOURCE-INSEE-SMIC-SERIES-2026` | `STUDY-EXPERTS-SMIC-2025` |
| `SOURCE-EXPERTS-SMIC-2024` | `STUDY-EXPERTS-SMIC-2024-RELIEFS` |
| `SOURCE-FRANCE-STRATEGIE-EXONERATIONS-2024` | `STUDY-FRANCE-STRATEGIE-EXONERATIONS-2024` |
| `SOURCE-INSEE-SMIC-MEAN-WAGE-2012` | `STUDY-INSEE-SMIC-MEAN-WAGE-2012` |
| `SOURCE-INSEE-MINIMUM-WAGE-RIGIDITY-2019` | `STUDY-INSEE-MINIMUM-WAGE-RIGIDITY-2019` |
| `SOURCE-ALBERTINI-POIRIER-TERRIAU-2025` | `STUDY-ALBERTINI-POIRIER-TERRIAU-2025` |
| `SOURCE-COTTET-PAYROLL-TAX-2024` | `STUDY-COTTET-PAYROLL-TAX-2024` |
| `SOURCE-HCREP-EXEMPTIONS-2024` | `STUDY-HCREP-EXEMPTIONS-2024` |
| `SOURCE-CAHUC-CARCILLO-LE-BARBANCHON-2019-ZERO-CHARGES` | `STUDY-CAHUC-CARCILLO-LE-BARBANCHON-2019-HIRING-CREDITS` |
| `SOURCE-INSEE-LEVEL-BY-AGE-1996-2024` | `STUDY-FOUCHER-GENERATIONAL-COMPARISON-2026` |
| `SOURCE-INSEE-INTERGEN-TRANSMISSIONS-2024` | `STUDY-FOUCHER-GENERATIONAL-COMPARISON-2026` |
| `SOURCE-INSEE-PATRIMOINE-NET-ENDETTEMENT-2024` | `STUDY-FOUCHER-GENERATIONAL-COMPARISON-2026` |
| `SOURCE-INSEE-HVP-ACCESS-2023-2024` | `STUDY-FOUCHER-GENERATIONAL-COMPARISON-2026` |
| `SOURCE-INSEE-HVP-METHODOLOGY-2023-2024` | `STUDY-FOUCHER-GENERATIONAL-COMPARISON-2026` |

Les relations créées sont `REL-CITES` de l'étude vers la source. Elles documentent la provenance bibliographique et n'ajoutent pas une validation indépendante des résultats.

### 2.2. 11 sources citées directement dans des dossiers enregistrés

| Source | Dossier | Motif du lien |
|---|---|---|
| `SOURCE-PARCOURSUP-ADMISSION-REVIEW-2026` | `DOSSIER-PARCOURSUP-EDUCATION-EQUITY` | Rapports d'analyse des candidatures et critères des formations |
| `SOURCE-SERVICE-PUBLIC-SMIC-RULES-2026` | `DOSSIER-SMIC-FRANCE-TRADEOFFS` | Règles juridiques et montants en vigueur |
| `SOURCE-MINTRAVAIL-SMIC-JUNE-2026` | `DOSSIER-SMIC-FRANCE-TRADEOFFS` | Montants et mécanisme de revalorisation de juin 2026 |
| `SOURCE-DARES-SMIC-BENEFICIARIES-2024` | `DOSSIER-SMIC-FRANCE-TRADEOFFS` | Bénéficiaires directs de la revalorisation de novembre 2024 |
| `SOURCE-GROUPE-EXPERTS-SMIC-2020` | `DOSSIER-SMIC-INDEXATION-DECOMPOSITION` | Historique et décomposition des revalorisations |
| `SOURCE-DARES-SMIC-FORMULA` | `DOSSIER-SMIC-INDEXATION-DECOMPOSITION` | Formule légale de revalorisation |
| `SOURCE-CHATEFP-HISTORY-WAGES-2024` | `DOSSIER-SMIC-INDEXATION-DECOMPOSITION` | Histoire des négociations et de l'intervention publique sur les salaires |
| `SOURCE-NBER-ABOWD-KRAMARZ-MARGOLIS-1999` | `DOSSIER-SMIC-HISTORICAL-EPISODES` | Trajectoires d'emploi des salariés directement rémunérés au minimum |
| `SOURCE-CREPON-DESPLATZ-2001` | `DOSSIER-SMIC-CAUSAL-EVIDENCE-MATRIX` | Évaluation des allègements de cotisations de 1995–1996, et non d'une hausse isolée du SMIC |
| `SOURCE-SHIFT-ABOUT-AND-MISSION` | `DOSSIER-SHIFT-PROJECT-ANALYSIS` | Mission et positionnement déclarés |
| `SOURCE-SHIFT-INTELLECTUAL-REFERENTIAL` | `DOSSIER-SHIFT-PROJECT-ANALYSIS` | Référentiel intellectuel déclaré |

Ces sources sont reliées par `REL-INCLUDES` du dossier vers la source.

### 2.3. Deux sources conservées en contexte

- `SOURCE-EU-EDUCATION-MONITOR-2025-FRANCE` : aucun usage précis retrouvé dans les dossiers, études ou synthèses examinés ; conserver `REL-ABOUT`.
- `SOURCE-DEFENSEUR-DROITS-JEUNESSES-ORIGINE-2026` : aucun usage précis retrouvé dans les dossiers, études ou synthèses examinés ; conserver `REL-ABOUT`.

## 3. Bilan des relations et des KPIs

- 36 relations `REL-CITES` ajoutées entre 34 sources distinctes et les études qui les déclarent.
- 14 relations `REL-INCLUDES` ajoutées entre 14 sources et des dossiers enregistrés.
- **50 relations nouvelles**, 48 sources supplémentaires couvertes.
- Le graphe passe de 633 à **683 relations**.
- Les trois sources restant sans couverture documentaire sont : `SOURCE-FO-POUVOIR-ACHAT-2026` (citation dans un fichier non enregistré), `SOURCE-EU-EDUCATION-MONITOR-2025-FRANCE` et `SOURCE-DEFENSEUR-DROITS-JEUNESSES-ORIGINE-2026` (aucune contribution précise retrouvée).

Calcul attendu à partir du périmètre initial : source coverage **217/220 = 98,6 %**. La CI doit confirmer ce résultat et l'absence d'anomalies. Ce taux n'est pas une cible de qualité scientifique ; il décrit uniquement la traçabilité documentaire du registre.

Les deux autres KPIs ne sont pas modifiés par ces relations :
- claims avec conclusion documentée : **28/80 = 35,0 %** ;
- dossiers actifs avec synthèse valide : **25/25 = 100 %**.

Aucun ratio global de connectivité du graphe n'est introduit.

## 4. Règles de connectivité attendues par type d'objet

| Type d'objet | Relation attendue quand la condition est vérifiée | Ce qui ne doit pas être imposé |
|---|---|---|
| SOURCE | `REL-CITES` depuis une étude qui la déclare dans `source_ids` ; `REL-INCLUDES` depuis un dossier enregistré qui la cite explicitement | Une source de contexte ou une piste n'a pas à recevoir artificiellement un lien documentaire |
| STUDY | `REL-CITES` vers chacune des sources effectivement déclarées ; `REL-SUPPORTS`, `REL-QUALIFIES` ou `REL-CONTRADICTS` vers les claims concernés | Une étude ne doit pas être reliée à un claim sur le seul fondement du thème |
| DATASET | `REL-USES` depuis une étude qui exploite réellement le dataset ; `REL-TRANSCRIBES` / `REL-TRANSCRIBED-FROM` uniquement si une filiation ou transcription de données est établie | Ne pas transformer automatiquement toute métadonnée ou notice en relation de provenance |
| DOSSIER | `REL-INCLUDES` vers les études, sources, claims ou concepts explicitement mobilisés ; `REL-SUMMARIZED-BY` vers sa synthèse | Un fichier de travail non enregistré n'est pas un nœud du graphe |
| CLAIM | Relations d'étayage, de nuance ou de contradiction avec les preuves effectivement pertinentes | Un claim `under_review` n'a pas à être forcé vers une conclusion |
| SYNTHESIS | Association unique avec un dossier actif et relation de synthèse correspondante | Le partage d'un fichier de synthèse par plusieurs dossiers n'est pas automatiquement un doublon |
| CONCEPT / MECHANISM | Relations sémantiques explicites, notamment `REL-EXPLAINS` entre concept et mécanisme | Aucun degré minimal universel |
| DOMAIN / TERRITORY / ORG | Relations thématiques, géographiques ou institutionnelles lorsque le lien est pertinent | Aucun degré minimal universel |

### Invariants applicables à toutes les relations

1. Identifiant de relation unique.
2. Type déclaré dans `knowledge/RELATION_TYPES.yml`.
3. Deux endpoints connus et compatibles avec les types autorisés.
4. Justification non vide, spécifique et proportionnée à la preuve.
5. Pas de triplet dupliqué ni de relation inférée du seul domaine, titre ou type de source.

La connectivité est donc évaluée par invariants et par population d'objets éligibles, jamais par un ratio global arbitraire.

## 5. Décision sur les benchmarks Actions

Les journaux du 18 novembre montrent que les deux benchmarks synthétiques ajoutaient environ **34,2 s** au run de référence et **53,8 s** au run de la PR #157. Le benchmark schémas mesurait 9,06 s à ×100 pour la seule fonction de validation ; le benchmark KPI mesurait 1,265 s au total médian à ×100, dont 0,198 s de calcul effectif.

Décision :
- validations fonctionnelles, tests unitaires et calcul ordinaire des KPIs dans chaque CI ;
- benchmarks synthétiques déplacés vers `.github/workflows/benchmarks.yml`, déclenché chaque semaine et manuellement ;
- résultats conservés dans les journaux et résumés Actions.

Ce découplage réduit le coût des changements ordinaires tout en maintenant une surveillance périodique des performances.
