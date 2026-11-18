# Audit des sources sans relation documentaire — 18 novembre 2026

**Périmètre :** instantané de `main` consulté le 18 novembre 2026. Analyse en lecture seule de `sources/registry.yml` et `knowledge/graph.yml`. Aucun registre, aucune source et aucune relation métier n'ont été modifiés.

## Résultat reproductible

- Sources dans le registre : **220**.
- Relations du graphe : **633**.
- Sources reliées par au moins une relation documentaire retenue : **169/220**.
- Sources sans relation documentaire retenue : **51**.
- Parmi ces dernières, **38** ont au moins une relation `REL-ABOUT` (rattachement thématique uniquement) et **13** n'ont aucune relation incidente dans le graphe.

La définition documentaire reprend celle du KPI `source_to_knowledge_coverage` : `REL-SUPPORTS`, `REL-QUALIFIES`, `REL-INCLUDES`, `REL-USES`, `REL-CITES`, `REL-TRANSCRIBES` et `REL-TRANSCRIBED-FROM`. Les relations doivent être structurellement valides (identifiant unique, justification non vide, endpoints connus et type déclaré). `REL-ABOUT` n'est pas une preuve de contribution documentaire.

## Lecture de l'audit

La catégorie « ABOUT uniquement » ne signifie pas que la source est inutile ou purement contextuelle : elle indique seulement que le graphe ne documente pas encore de contribution précise de cette source à une étude, un claim, un jeu de données ou une synthèse.

La catégorie « sans relation » signale une priorité de revue plus élevée, mais ne justifie pas à elle seule la création d'un lien. Une source peut être une piste, une référence méthodologique, une source de contexte, une source redondante ou une source effectivement mobilisée mais dont le lien manque. Il faut vérifier le contenu du dossier et la contribution réellement effectuée.

### A. Sources déjà rattachées thématiquement (`REL-ABOUT`), sans contribution documentaire

| Identifiant | Type | Domaine(s) |
|---|---|---|
| `SOURCE-PARCOURSUP-BILAN-2026` | institutional_report | DOMAIN-EDUCATION |
| `SOURCE-SIES-PARCOURSUP-2026-ADMISSIONS` | scientific_study | DOMAIN-EDUCATION |
| `SOURCE-DEPP-ETAT-ECOLE-2025` | institutional_report | DOMAIN-EDUCATION |
| `SOURCE-INSEE-INEGALITES-SCOLAIRES-2025` | institutional_report | DOMAIN-EDUCATION |
| `SOURCE-OECD-PISA-2022-FRANCE` | institutional_report | DOMAIN-EDUCATION |
| `SOURCE-OECD-EAG-2025-FRANCE` | institutional_report | DOMAIN-EDUCATION |
| `SOURCE-EU-EDUCATION-MONITOR-2025-FRANCE` | institutional_report | DOMAIN-EDUCATION |
| `SOURCE-DEFENSEUR-DROITS-JEUNESSES-ORIGINE-2026` | institutional_report | DOMAIN-EDUCATION, DOMAIN-MIGRATION, DOMAIN-SECURITY |
| `SOURCE-PARCOURSUP-OPEN-DATA-2025` | primary_data | DOMAIN-EDUCATION |
| `SOURCE-PARCOURSUP-ADMISSION-REVIEW-2026` | other | DOMAIN-EDUCATION |
| `SOURCE-COUR-DES-COMPTES-PEINES-ALTERNATIVES-2025` | institutional_report | DOMAIN-SECURITY, DOMAIN-INSTITUTIONS, DOMAIN-FINANCE |
| `SOURCE-MINISTERE-JUSTICE-TIG-PRONONCE-2024` | institutional_report | DOMAIN-SECURITY |
| `SOURCE-MINISTERE-JUSTICE-TUTEURS-TIG-2024` | institutional_report | DOMAIN-SECURITY, DOMAIN-INSTITUTIONS |
| `SOURCE-SENAT-EXECUTION-PEINES-2025` | institutional_report | DOMAIN-SECURITY, DOMAIN-INSTITUTIONS |
| `SOURCE-INSEE-SMIC-SERIES-2026` | primary_data | DOMAIN-ECONOMY, DOMAIN-FINANCE |
| `SOURCE-SERVICE-PUBLIC-SMIC-RULES-2026` | law_or_policy | DOMAIN-ECONOMY, DOMAIN-INSTITUTIONS |
| `SOURCE-MINTRAVAIL-SMIC-JUNE-2026` | institutional_report | DOMAIN-ECONOMY, DOMAIN-INSTITUTIONS |
| `SOURCE-DARES-SMIC-BENEFICIARIES-2024` | institutional_report | DOMAIN-ECONOMY |
| `SOURCE-EXPERTS-SMIC-2024` | institutional_report | DOMAIN-ECONOMY, DOMAIN-FINANCE |
| `SOURCE-FRANCE-STRATEGIE-EXONERATIONS-2024` | institutional_report | DOMAIN-ECONOMY, DOMAIN-FINANCE |
| `SOURCE-INSEE-SMIC-MEAN-WAGE-2012` | scientific_study | DOMAIN-ECONOMY |
| `SOURCE-INSEE-MINIMUM-WAGE-RIGIDITY-2019` | scientific_study | DOMAIN-ECONOMY |
| `SOURCE-ALBERTINI-POIRIER-TERRIAU-2025` | scientific_study | DOMAIN-ECONOMY, DOMAIN-FINANCE |
| `SOURCE-COTTET-PAYROLL-TAX-2024` | scientific_study | DOMAIN-ECONOMY, DOMAIN-FINANCE |
| `SOURCE-HCREP-EXEMPTIONS-2024` | institutional_report | DOMAIN-ECONOMY, DOMAIN-FINANCE |
| `SOURCE-GROUPE-EXPERTS-SMIC-2020` | institutional_report | DOMAIN-ECONOMY |
| `SOURCE-DARES-SMIC-FORMULA` | institutional_explainer | DOMAIN-ECONOMY |
| `SOURCE-CHATEFP-HISTORY-WAGES-2024` | historical_institutional_publication | DOMAIN-ECONOMY, DOMAIN-INSTITUTIONS |
| `SOURCE-NBER-ABOWD-KRAMARZ-MARGOLIS-1999` | scientific_study | DOMAIN-ECONOMY |
| `SOURCE-CREPON-DESPLATZ-2001` | scientific_study | DOMAIN-ECONOMY |
| `SOURCE-CAHUC-CARCILLO-LE-BARBANCHON-2019-ZERO-CHARGES` | working_paper | DOMAIN-ECONOMY |
| `SOURCE-SHIFT-ABOUT-AND-MISSION` | institutional_explainer | DOMAIN-ENERGY, DOMAIN-ENVIRONMENT, DOMAIN-ECONOMY |
| `SOURCE-SHIFT-INTELLECTUAL-REFERENTIAL` | think_tank_report | DOMAIN-ENERGY, DOMAIN-ENVIRONMENT, DOMAIN-ECONOMY, DOMAIN-SCIENCE |
| `SOURCE-INSEE-LEVEL-BY-AGE-1996-2024` | primary_data | DOMAIN-ECONOMY, DOMAIN-SOCIETY |
| `SOURCE-INSEE-INTERGEN-TRANSMISSIONS-2024` | institutional_research | DOMAIN-ECONOMY, DOMAIN-FINANCE, DOMAIN-SOCIETY |
| `SOURCE-INSEE-PATRIMOINE-NET-ENDETTEMENT-2024` | primary_data | DOMAIN-ECONOMY, DOMAIN-FINANCE, DOMAIN-SOCIETY |
| `SOURCE-INSEE-HVP-ACCESS-2023-2024` | institutional_explainer | DOMAIN-ECONOMY, DOMAIN-SOCIETY |
| `SOURCE-INSEE-HVP-METHODOLOGY-2023-2024` | institutional_explainer | DOMAIN-ECONOMY, DOMAIN-FINANCE, DOMAIN-SOCIETY |

### B. Sources sans aucune relation incidente

| Identifiant | Type | Domaine(s) |
|---|---|---|
| `SOURCE-PRI-EU-NONCUSTODIAL-COMPARATIVE-2025` | institutional_report | DOMAIN-SECURITY, DOMAIN-INSTITUTIONS |
| `SOURCE-WERMINK-COMMUNITY-SERVICE-RETRIBUTION-2023` | scientific_study | DOMAIN-SECURITY, DOMAIN-FINANCE |
| `SOURCE-FO-POUVOIR-ACHAT-2026` | opinion | DOMAIN-ECONOMY |
| `SOURCE-UK-DFE-2024-HARASSMENT-CENSORSHIP` | institutional_report | DOMAIN-EDUCATION, DOMAIN-INSTITUTIONS |
| `SOURCE-TADROS-2022-RIGHTS-NOPLATFORMING` | academic_article | DOMAIN-INSTITUTIONS, DOMAIN-SOCIETY |
| `SOURCE-LIBERAL-DEFENSE-NOPLATFORMING-2024` | academic_article | DOMAIN-INSTITUTIONS, DOMAIN-EDUCATION, DOMAIN-SOCIETY |
| `SOURCE-VAN-DER-DOES-JACQUET-2023-SPILLOVER-REVIEW` | academic_article | DOMAIN-POLITICS, DOMAIN-SOCIETY |
| `SOURCE-META-ANALYSIS-DEMOCRATIC-INNOVATIONS-2024` | academic_article | DOMAIN-POLITICS, DOMAIN-SOCIETY |
| `SOURCE-GERMANN-2025-MINIPUBLIC-REPRESENTATIVENESS` | academic_article | DOMAIN-POLITICS, DOMAIN-SOCIETY |
| `SOURCE-CEREQ-GENERATION-2021-BTS-MATCHING-2026` | institutional_research | DOMAIN-EDUCATION, DOMAIN-ECONOMY |
| `SOURCE-DEPP-INSERJEUNES-2026` | institutional_explainer | DOMAIN-EDUCATION, DOMAIN-ECONOMY |
| `SOURCE-OECD-PIAAC-DATA-METHODOLOGY-2023` | primary_data | DOMAIN-EDUCATION, DOMAIN-ECONOMY |
| `SOURCE-INSEE-PANEL-TOUS-SALARIES-METADATA-2026` | institutional_explainer | DOMAIN-ECONOMY |

## Protocole de qualification à appliquer source par source

Pour chaque source, examiner les dossiers et études concernés, les citations et les fichiers de synthèse, puis attribuer une qualification provisoire :

1. **Mobilisée — lien manquant :** la source soutient, qualifie, est citée ou utilisée explicitement dans un objet existant. Ajouter uniquement la relation qui décrit cette contribution, avec une justification factuelle et bornée.
2. **Contexte / cadrage :** la source sert à situer un domaine ou une controverse sans contribuer directement à un résultat. Conserver éventuellement `REL-ABOUT` ; ne pas la forcer dans le KPI documentaire.
3. **Méthode / données :** la source décrit une méthode, un dispositif ou un jeu de données effectivement utilisé. Relier à l'étude ou au dataset correspondant via le type de relation approprié, après vérification.
4. **Redondante / remplacée / obsolète :** vérifier les doublons et l'historique avant toute suppression ou archivage ; ne pas supprimer automatiquement.
5. **Non mobilisée / piste :** conserver comme référence de recherche si elle reste utile, sans relation artificielle.
6. **Ambiguë :** consigner la question à résoudre et laisser la source non couverte tant que la preuve de contribution manque.

Une relation documentaire ne doit jamais être déduite du seul domaine, du titre, du type de source ou de la proximité thématique. Une source ne doit pas être reliée directement à un claim simplement parce qu'elle porte sur le même sujet : il faut confirmer qu'elle documente effectivement ce claim, avec le bon périmètre, la bonne population et les bonnes limites.

## Travail restant — ordre recommandé

1. **Revue des 13 sources sans relation :** commencer par identifier leur dossier éventuel, leur statut (piste, méthode, contexte, source mobilisée) et leur usage vérifiable.
2. **Revue des 38 sources ABOUT-only :** vérifier si certaines contribuent déjà à des études, claims, datasets ou synthèses sans relation explicite.
3. **Qualification traçable :** ajouter un tableau de décision (identifiant, catégorie, objet concerné, preuve localisée, action, relecteur/date) dans le rapport ou dans les dossiers concernés. Ne pas créer un nouveau registre permanent si une documentation d'audit suffit.
4. **Corrections minimales :** proposer les relations documentaires justifiées, chacune avec justification précise ; préserver les relations thématiques existantes.
5. **Recalcul :** exécuter `python scripts/validate/calculate_project_kpis.py --format markdown`, comparer les identifiants couverts/non couverts et contrôler les diagnostics d'intégrité. Toute évolution du numérateur doit être expliquée par des liens vérifiés, jamais par une optimisation du ratio.

## Limites

- Cet audit est une classification structurelle, pas une revue de pertinence scientifique des 51 sources.
- Les champs `notes`, `methodology` et `limitations` aident à prioriser la lecture mais ne prouvent pas une utilisation effective dans un dossier.
- Le nombre de relations incidentes ne mesure ni la qualité de la source ni son poids probant.
- Les résultats sont un instantané ; le rapport doit être recalculé après évolution des registres ou du graphe.


## Revue source par source — 18 novembre 2026

**Méthode :** rapprochement des identifiants du registre des sources avec `research/studies/registry.yml`, `research/datasets/registry.yml`, les dossiers enregistrés et leurs bibliographies. Une relation n'est proposée que lorsque l'usage est explicite. Les liens ci-dessous sont des décisions de revue ; ce document ne modifie pas le graphe.

### A. Les 13 sources sans relation incidente

| Source | Usage retrouvé | Décision proposée |
|---|---|---|
| `SOURCE-PRI-EU-NONCUSTODIAL-COMPARATIVE-2025` | `STUDY-PRI-EU-NONCUSTODIAL-COMPARATIVE-2025`, champ `source_ids` | Ajouter `REL-CITES` depuis l'étude |
| `SOURCE-WERMINK-COMMUNITY-SERVICE-RETRIBUTION-2023` | `STUDY-WERMINK-NETHERLANDS-COMMUNITY-SERVICE-IV-2023`, champ `source_ids` | Ajouter `REL-CITES` depuis l'étude |
| `SOURCE-FO-POUVOIR-ACHAT-2026` | Citation bibliographique dans `dossiers/smic-social-partners-evidence.md`, fichier de travail non enregistré dans `dossiers/registry.yml` | Ne pas créer de lien vers un objet absent du graphe ; enregistrer le dossier de travail ou documenter son rattachement avant de relier |
| `SOURCE-UK-DFE-2024-HARASSMENT-CENSORSHIP` | `DOSSIER-CORDON-SANITAIRE-BELGIQUE-EFFICACITE`, données descriptives et limites du no-platforming ; bibliographie § 13 | Ajouter `REL-INCLUDES` depuis le dossier |
| `SOURCE-TADROS-2022-RIGHTS-NOPLATFORMING` | Même dossier, analyse normative des droits et conditions de justification ; bibliographie § 14 | Ajouter `REL-INCLUDES` depuis le dossier |
| `SOURCE-LIBERAL-DEFENSE-NOPLATFORMING-2024` | Même dossier, défense normative du no-platforming non violent ; bibliographie § 15 | Ajouter `REL-INCLUDES` depuis le dossier |
| `SOURCE-VAN-DER-DOES-JACQUET-2023-SPILLOVER-REVIEW` | `STUDY-VAN-DER-DOES-JACQUET-2023-SPILLOVER`, champ `source_ids` ; mobilisée dans le dossier Un commun accord | Ajouter `REL-CITES` depuis l'étude |
| `SOURCE-META-ANALYSIS-DEMOCRATIC-INNOVATIONS-2024` | `STUDY-DEMOCRATIC-INNOVATIONS-META-ANALYSIS-2024`, champ `source_ids` ; mobilisée dans le dossier Un commun accord | Ajouter `REL-CITES` depuis l'étude |
| `SOURCE-GERMANN-2025-MINIPUBLIC-REPRESENTATIVENESS` | `STUDY-GERMANN-2025-REPRESENTATIVENESS-LEGITIMACY`, champ `source_ids` ; mobilisée dans le dossier Un commun accord | Ajouter `REL-CITES` depuis l'étude |
| `SOURCE-CEREQ-GENERATION-2021-BTS-MATCHING-2026` | `STUDY-CEREQ-GENERATION-2021-BTS-MATCHING` et `DATASET-CEREQ-GENERATION-2021-BTS-MATCHED` | Ajouter `REL-CITES` depuis l'étude ; ne pas assimiler la notice de projet à une extraction des microdonnées |
| `SOURCE-DEPP-INSERJEUNES-2026` | `STUDY-INSERJEUNES-INSERTION-2023` et `DATASET-INSERJEUNES-2023` | Ajouter `REL-CITES` depuis l'étude |
| `SOURCE-OECD-PIAAC-DATA-METHODOLOGY-2023` | `STUDY-PIAAC-2023-FRANCE-COMPETENCES` et `DATASET-PIAAC-2023-FRANCE` | Ajouter `REL-CITES` depuis l'étude |
| `SOURCE-INSEE-PANEL-TOUS-SALARIES-METADATA-2026` | `STUDY-CEREQ-GENERATION-2021-BTS-MATCHING`, `STUDY-INSEE-PANEL-TOUS-SALARIES-TRAJECTORIES` et deux fiches dataset | Ajouter un `REL-CITES` depuis chacune des deux études |

**Bilan :** 9 sources disposent d'un rattachement explicite à une étude (10 relations étude→source, car la source Insee Panel est référencée par deux études) ; 3 autres sont explicitement citées par un dossier enregistré ; 1 source est citée dans un fichier de travail non enregistré et reste volontairement sans lien.

### B. Les 38 sources avec `REL-ABOUT` uniquement

#### B1. Sources explicitement déclarées dans `research/studies/registry.yml`

Le champ `source_ids` justifie une relation bibliographique `REL-CITES` de l'étude vers la source. La relation formalise la traçabilité du registre ; elle ne signifie pas que la source valide toutes les conclusions de l'étude.

| Source | Étude déclarant la source |
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

Ces 25 sources correspondent à 26 relations étude→source, la source Sénat étant déclarée dans deux études.

#### B2. Sources citées directement dans des dossiers enregistrés

| Source | Dossier | Usage constaté |
|---|---|---|
| `SOURCE-PARCOURSUP-ADMISSION-REVIEW-2026` | `DOSSIER-PARCOURSUP-EDUCATION-EQUITY` | Critères déclarés par les formations et rapports d'analyse des candidatures |
| `SOURCE-SERVICE-PUBLIC-SMIC-RULES-2026` | `DOSSIER-SMIC-FRANCE-TRADEOFFS` | Règles juridiques et montants en vigueur |
| `SOURCE-MINTRAVAIL-SMIC-JUNE-2026` | `DOSSIER-SMIC-FRANCE-TRADEOFFS` | Montants et mécanisme de revalorisation de juin 2026 |
| `SOURCE-DARES-SMIC-BENEFICIARIES-2024` | `DOSSIER-SMIC-FRANCE-TRADEOFFS` | Bénéficiaires directs et distribution de la revalorisation de novembre 2024 |
| `SOURCE-GROUPE-EXPERTS-SMIC-2020` | `DOSSIER-SMIC-INDEXATION-DECOMPOSITION` | Historique des 50 ans du SMIC et décomposition historique |
| `SOURCE-DARES-SMIC-FORMULA` | `DOSSIER-SMIC-INDEXATION-DECOMPOSITION` | Explication de la formule de revalorisation |
| `SOURCE-CHATEFP-HISTORY-WAGES-2024` | `DOSSIER-SMIC-INDEXATION-DECOMPOSITION` | Histoire de l'intervention publique et des négociations salariales |
| `SOURCE-NBER-ABOWD-KRAMARZ-MARGOLIS-1999` | `DOSSIER-SMIC-HISTORICAL-EPISODES` | Trajectoires d'emploi des salariés directement rémunérés au minimum |
| `SOURCE-CREPON-DESPLATZ-2001` | `DOSSIER-SMIC-CAUSAL-EVIDENCE-MATRIX` | Évaluation des extensions d'allègements de cotisations de 1995–1996, non d'une hausse isolée du SMIC |
| `SOURCE-SHIFT-ABOUT-AND-MISSION` | `DOSSIER-SHIFT-PROJECT-ANALYSIS` | Mission déclarée et positionnement de l'organisation |
| `SOURCE-SHIFT-INTELLECTUAL-REFERENTIAL` | `DOSSIER-SHIFT-PROJECT-ANALYSIS` | Référentiel intellectuel déclaré |

Ces 11 sources justifient `REL-INCLUDES` depuis le dossier concerné.

#### B3. Sources conservées en contexte

- `SOURCE-EU-EDUCATION-MONITOR-2025-FRANCE` : aucun usage précis retrouvé dans les dossiers, études ou synthèses examinés ; conserver le rattachement thématique européen.
- `SOURCE-DEFENSEUR-DROITS-JEUNESSES-ORIGINE-2026` : aucun usage précis retrouvé dans les dossiers, études ou synthèses examinés ; conserver le rattachement thématique, sans déduire une contribution à l'analyse de Parcoursup.

### Synthèse des décisions

- **50 relations candidates justifiées** : 36 relations `REL-CITES` depuis les études et 14 relations `REL-INCLUDES` depuis les dossiers enregistrés.
- **48 sources distinctes** pourraient ainsi acquérir une relation documentaire ; les 3 sources restant sans couverture seraient `SOURCE-FO-POUVOIR-ACHAT-2026`, `SOURCE-EU-EDUCATION-MONITOR-2025-FRANCE` et `SOURCE-DEFENSEUR-DROITS-JEUNESSES-ORIGINE-2026`.
- Projection arithmétique, à confirmer après modification et recalcul : **217/220 (98,6 %)**. Ce n'est pas un résultat observé dans ce commit.
- Le fichier `dossiers/smic-social-partners-evidence.md` doit faire l'objet d'une décision de gouvernance séparée avant toute relation pour la source FO.
- Les liens dataset ne sont pas créés automatiquement à partir de `source_ids` : `REL-TRANSCRIBES` ne doit être utilisé que lorsqu'une source est effectivement transformée ou transcrite dans le dataset, pas lorsqu'elle fournit seulement une notice ou des métadonnées.
- Aucune cible de connectivité globale n'est définie.

