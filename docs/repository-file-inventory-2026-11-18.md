# Inventaire exhaustif du dépôt — 18 novembre 2026

## Instantané et méthode

- Dépôt : `JM-Brun/society-lab`.
- Branche : `main`.
- Commit inventorié : `5379509b641fa3bdc782b034afa9101ba1809f1c`.
- Source : arbre GitHub récursif (`git/trees/main?recursive=1`), réponse non tronquée.
- Résultat : **237 fichiers**, **32 répertoires** (hors racine), **269 entrées** au total.
- Portée : tous les blobs suivis dans l'arbre Git de cet instantané, y compris les fichiers cachés et les fichiers de configuration ; les répertoires vides et les fichiers ignorés/non suivis ne sont pas représentés.
- Cet inventaire est un instantané daté, pas un nouveau registre vivant. Il doit être régénéré par le contrôle de couverture plutôt que maintenu manuellement.

## Répartition
| Répertoire de premier niveau | Fichiers |
|---|---:|
| `.claude` | 1 |
| `.github` | 8 |
| `[racine]` | 9 |
| `analysis` | 6 |
| `claims` | 25 |
| `data` | 9 |
| `docs` | 25 |
| `dossiers` | 61 |
| `forecasts` | 2 |
| `governance` | 4 |
| `hypotheses` | 4 |
| `knowledge` | 16 |
| `research` | 5 |
| `schemas` | 11 |
| `scripts` | 15 |
| `sources` | 5 |
| `syntheses` | 13 |
| `templates` | 2 |
| `tests` | 15 |
| `tools` | 1 |

| Extension | Fichiers |
|---|---:|
| `.md` | 125 |
| `.yml` | 56 |
| `.py` | 31 |
| `.json` | 13 |
| `.csv` | 8 |
| `.gitignore` | 1 |
| `.yaml` | 1 |
| `[sans extension]` | 1 |
| `.txt` | 1 |

## Cartographie de la couverture et des contrôles existants

| Famille de fichiers / données | Source de vérité et contrôle observé | Limite à traiter |
|---|---|---|
| `sources/registry.yml` et `schemas/source.schema.json` | Registre parcouru par `scripts/validate/validate_registry.py`, validation JSON Schema et références croisées. | Les fiches sources autonomes sous `sources/*.yml` doivent être rapprochées explicitement du registre ; ne pas supposer que le contrôle du registre les couvre. |
| `research/studies/registry.yml`, `research/datasets/registry.yml` | Schémas Study/Dataset et références croisées via le validateur central. | Registres canoniques présents ; aucun fichier d'objet individuel dans ces répertoires à cet instant. |
| `claims/registry.yml`, `hypotheses/registry.yml` | Schémas, identifiants, références et vocabulaire via le validateur central. | Le contrôle de structure ne juge pas la qualité probante ni l'indépendance des sources. |
| `knowledge/concepts/registry.yml`, `knowledge/mechanisms/registry.yml` | Schémas, identifiants et liens du graphe ; mécanismes actuellement registre vide. | Vérifier explicitement la cohérence entre fiches, registres et nœuds/arêtes ; ne pas confondre mécanisme déclaré et causalité établie. |
| `dossiers/registry.yml` et `dossiers/*.md` | Schéma du registre ; `validate_syntheses.py` vérifie la présence des dossiers associés aux synthèses. | Le Markdown des dossiers n'a pas de schéma de contenu propre ; la couverture des fichiers Markdown doit être comparée au registre. |
| `syntheses/registry.yml` et `syntheses/*.md` | Contrôle dédié des correspondances, frontmatter, statuts, confiance et sections obligatoires ; contrôle de fraîcheur indicatif. | Le contrôle de fraîcheur utilise les dates de commit locales comme signal, non comme preuve de mise à jour scientifique. |
| `forecasts/registry.yml` et `schemas/forecast.schema.json` | Le registre Forecast figure dans `REGISTRIES` et est validé par schéma. | Registre actuellement vide ; aucun objet Forecast individuel inventorié. |
| `sources/batches/*.yml` et `schemas/ingestion-batch.schema.json` | Contrôle dédié des manifestes, candidats, doublons et cycles `duplicate_of`. | Aucun manifeste de lot YAML présent dans l'instantané ; le dossier contient uniquement son README. |
| `knowledge/TAXONOMY.yml`, `TAGS.yml`, `RELATION_TYPES.yml`, `TERRITORIES.yml`, `knowledge/graph.yml` | Vocabulaire contrôlé, schéma Territory, identifiants, types de nœuds/arêtes, références et justifications. | Les contrôles de justification vérifient la présence, pas la qualité ou l'étayage scientifique du raisonnement. |
| `scripts/analysis/*.py`, `analysis/*.md`, `research/analysis/*.md`, `data/*` | Tests unitaires ciblés pour les scripts d'analyse ; fichiers de données et protocoles versionnés. | Inventaire ne signifie pas validation systématique de chaque jeu de données, transformation ou résultat ; documenter les tests propres à chaque pipeline. |
| `docs/*.md`, `templates/*`, configuration et workflows | Documentation et CI ; schémas JSON syntaxiquement vérifiés dans le workflow. | La présence d'une documentation ou d'un workflow ne garantit pas l'alignement entre tous les contrats et toutes les implémentations. |

## Écarts de couverture observés à qualifier

Sur le même instantané, la comparaison des chemins de fichiers avec le registre de synthèses donne :

- `dossiers/` : **60 fichiers Markdown**, dont **25 chemins** explicitement associés à une entrée de `syntheses/registry.yml` ; **35 fichiers** restent hors de cette correspondance.
- `syntheses/` : **12 fichiers Markdown**, dont **11 chemins distincts** référencés par le registre ; **1 fichier** n'est pas référencé.
- Les 25 chemins de dossiers déclarés existent tous. Les 11 chemins de synthèses déclarés existent tous.
- Ces écarts ne sont **pas encore des erreurs** : plusieurs fichiers de `dossiers/` peuvent être des notes d'étude, matrices de preuves ou audits intermédiaires plutôt que des dossiers principaux ; le fichier de synthèse non référencé peut être historique ou en attente de rattachement. Il faut qualifier leur rôle avant de rendre la couverture bloquante.
- `sources/` contient deux fiches YAML autonomes : `SOURCE-SENAT-1994-SMIC-DECOMPOSITION` est également présent dans le registre canonique ; `SOURCE-SHIFT-PROJECT-CORPUS` est une fiche de regroupement documentaire explicitement décrite comme point d'entrée, pas une source détaillée ordinaire.
## Décisions de renforcement — sans nouveau registre ni schéma

1. Ajouter un **contrôle de couverture des fichiers** calculé à partir de l'arbre du dépôt : fichiers de fiches attendus ↔ chemins déclarés dans les registres existants ; signaler les fichiers orphelins et les entrées qui pointent vers des chemins absents.
2. Faire échouer la CI uniquement sur les écarts de couverture non ambigus (fichier de fiche canonique non référencé, chemin référencé absent, doublon de chemin ou identifiant), avec exceptions explicites pour README, modèles, protocoles, données et vues dérivées.
3. Garder les contrôles de qualité scientifique en avertissements/revue humaine : la validation structurelle ne doit pas inventer la complétude des métadonnées, la licence, la vérification ou la force probante.
4. Réutiliser les registres et schémas actuels. Les registres vides (`mechanisms`, `forecasts`) sont des états valides ; ne pas les remplir artificiellement et ne pas créer de registres parallèles.
5. Distinguer le périmètre des objets canoniques des fichiers de travail : scripts, tests, notes d'analyse, données brutes, documentation et modèles ne sont pas des fiches d'objets et ne doivent pas être forcés dans les registres.
6. Ajouter des tests négatifs pour fichier non référencé, chemin absent, double déclaration, exceptions documentées et répertoire de lots vide ; conserver les tests d'intégrité des références et du graphe.
7. Mesurer le coût du contrôle sur l'arbre complet et garder une complexité linéaire en nombre de fichiers/entrées (index de chemins et d'identifiants construits une fois).

## Liste exhaustive des fichiers suivis

La liste ci-dessous correspond exactement à l'instantané Git indiqué en tête. Les regroupements sont purement organisationnels ; ils ne constituent pas une taxonomie de données.

### .claude

- `.claude/settings.json`

### .github

- `.github/ISSUE_TEMPLATE/task.md`
- `.github/workflows/backlog-view.yml`
- `.github/workflows/issue-governance.yml`
- `.github/workflows/secret-scan.yml`
- `.github/workflows/smic-monthly-reconstruction.yml`
- `.github/workflows/smic-openfisca.yml`
- `.github/workflows/sync-issue-labels.yml`
- `.github/workflows/validate.yml`

### [racine]

- `.gitignore`
- `.pre-commit-config.yaml`
- `AGENTS.md`
- `CHARTER.md`
- `CONTRIBUTING.md`
- `LICENSE`
- `METHODOLOGY.md`
- `README.md`
- `requirements-openfisca.txt`

### analysis

- `analysis/claim-review-pilot-tig-parcoursup-2026-11-13.md`
- `analysis/parcoursup-claim-extraction-pilot-2026-11-18.md`
- `analysis/tig-execution-delay-extraction-pilot-2026-11-18.md`
- `analysis/tig-research-next-steps.md`
- `analysis/tig-territorial-data-specification.md`
- `analysis/tig-territorial-inquiry-protocol.md`

### claims

- `claims/claim-academic-speech-restriction-motives-2025.yml`
- `claims/claim-belgium-cordon-contribution-not-isolated-2021.yml`
- `claims/claim-belgium-cordon-three-decades-institutional-access.yml`
- `claims/claim-belgium-wallonia-flanders-cordon-2021.yml`
- `claims/claim-bypassing-can-outperform-simple-negation-2025.yml`
- `claims/claim-causal-alternative-improves-correction.yml`
- `claims/claim-coalition-signals-cordon-not-systematic-context-2025.yml`
- `claims/claim-coalition-signals-shift-affect-2025.yml`
- `claims/claim-common-front-rhetoric-increases-affective-polarization-2026.yml`
- `claims/claim-cordon-formal-noncollaboration-insufficient-with-discursive-accommodation.yml`
- `claims/claim-correction-novel-misinformation-no-general-familiarity-backfire-2020.yml`
- `claims/claim-corrections-rarely-backfire-2024.yml`
- `claims/claim-deplatforming-displacement-and-net-reach-2023-2024.yml`
- `claims/claim-dutch-media-accommodation-normalization-2022.yml`
- `claims/claim-exposure-unchecked-extreme-interviews-attitudes-norms-2025.yml`
- `claims/claim-false-balance-distorts-consensus-perception-2016.yml`
- `claims/claim-france-2024-withdrawals-reconfigure-runoffs.yml`
- `claims/claim-germany-brandmauer-no-detected-short-term-effect-2025.yml`
- `claims/claim-inoculation-can-produce-durable-transfer.yml`
- `claims/claim-inoculation-improves-discernment-2026.yml`
- `claims/claim-reactance-freedom-threatening-language-2026.yml`
- `claims/claim-repetition-illusory-truth-effect-2026.yml`
- `claims/claim-shift-project-streaming-energy-estimates.yml`
- `claims/claim-unchallenged-platforming-normalizes-extreme-views.yml`
- `claims/registry.yml`

### data

- `data/smic-annual-averages-1994-2026.csv`
- `data/smic-monthly-source-manifest-1970-2025.yml`
- `data/smic-real-power-decomposition-1971-2001.csv`
- `data/smic-real-purchasing-power-1970-2025.csv`
- `data/smic-real-purchasing-power-2001-2008-tef2010.csv`
- `data/smic-real-purchasing-power-2014-2025.csv`
- `data/smic-revaluations-1970-1993.csv`
- `data/smic-revaluations-1994-2026.csv`
- `data/smic-revaluations-1996-2008.csv`

### docs

- `docs/architecture.md`
- `docs/audit-ingestion-knowledge-pipeline-2026-11.md`
- `docs/audit-transversal-etat-des-connaissances.md`
- `docs/backlog-view.md`
- `docs/cross-domain-education-employment-evidence.md`
- `docs/cross-domain-knowledge-framework.md`
- `docs/cross-domain-knowledge-inventory.md`
- `docs/cross-repository-contract.md`
- `docs/cross-repository-knowledge-management-review.md`
- `docs/editorial-charter.md`
- `docs/forecasting.md`
- `docs/ingestion-protocol.md`
- `docs/issue-governance.md`
- `docs/licensing.md`
- `docs/metadata-and-naming.md`
- `docs/multiscalar-analysis.md`
- `docs/pilot-traceability-assessment-2026-11.md`
- `docs/roadmap.md`
- `docs/session-handoff-traceability-smic-2026-11-18.md`
- `docs/smic-1970-1993-arithmetic-audit-2026-11.md`
- `docs/smic-historical-revaluations-brief.md`
- `docs/smic-openfisca-prototype.md`
- `docs/source-impact-tracing.md`
- `docs/source-policy.md`
- `docs/uncertainty-and-revisions.md`

### dossiers

- `dossiers/antoine-foucher-pacte-intergenerationnel.md`
- `dossiers/comparaison-quantitative-scenarios-energie-2026.md`
- `dossiers/comparaison-scenarios-transition-pref-rte-ademe-negawatt-snbc3.md`
- `dossiers/cordon-sanitaire-belgique-efficacite.md`
- `dossiers/debat-barrage-cordon-sanitaire.md`
- `dossiers/journal-recherche-cordon-sanitaire-medias.md`
- `dossiers/matrice-preuves-cordon-sanitaire.md`
- `dossiers/matrice-preuves-strategies-reponse.md`
- `dossiers/parcoursup-education-equity.md`
- `dossiers/pref-2026-audit-robustesse-scenarios.md`
- `dossiers/protocole-comparatif-strategies-reponse-idees-antidemocratiques.md`
- `dossiers/protocole-revue-systematique-cordon-sanitaire.md`
- `dossiers/registry.yml`
- `dossiers/smic-abowd-kramarz-lemieux-margolis-1997-emploi-jeunes.md`
- `dossiers/smic-abowd-kramarz-margolis-1999-transitions-emploi.md`
- `dossiers/smic-aeberhardt-givord-marbot-2012-spillovers.md`
- `dossiers/smic-aeberhardt-sraer-2010-dynamique-salariale.md`
- `dossiers/smic-arguments-fallacieux-poncifs-debat.md`
- `dossiers/smic-audenis-laib-roux-2002-source-access-audit.md`
- `dossiers/smic-barlet-blanchet-le-barbanchon-2010-microsimulation.md`
- `dossiers/smic-bazen-skourias-1997-audit-etudes-recentes.md`
- `dossiers/smic-cahuc-carcillo-le-barbanchon-2019-credit-embauche-zero-charges.md`
- `dossiers/smic-causal-evidence-matrix.md`
- `dossiers/smic-cette-chouard-verdugo-2011-diffusion-salaire-moyen.md`
- `dossiers/smic-contre-productivite-mesure-episodes.md`
- `dossiers/smic-cottet-2020-2024-allegements-emploi.md`
- `dossiers/smic-crepon-desplatz-2001.md`
- `dossiers/smic-dares-beneficiaires-inflation-2021-2024-audit.md`
- `dossiers/smic-economists-literature-review.md`
- `dossiers/smic-emploi-jeunes-bazen-etudes-recentes-etat-preuve.md`
- `dossiers/smic-episodes-historiques-bilan-positif-negatif.md`
- `dossiers/smic-facteurs-mecanismes-transmission-2026.md`
- `dossiers/smic-fillon-reform-2003-audit.md`
- `dossiers/smic-fougere-gautier-le-bihan-2010-prix-restauration.md`
- `dossiers/smic-france-tradeoffs.md`
- `dossiers/smic-gautier-roux-suarez-castillo-2019-wage-rigidity.md`
- `dossiers/smic-goarant-muller-2011-diffusion-acemo.md`
- `dossiers/smic-grecsta-fillon-2009-source-access-note.md`
- `dossiers/smic-hennion-loisy-2006-macro-audit.md`
- `dossiers/smic-historical-episodes.md`
- `dossiers/smic-indexation-and-boosts-1970-2026.md`
- `dossiers/smic-indexation-decomposition.md`
- `dossiers/smic-koubi-lhommeau-2007-diffusion-grilles-salariales.md`
- `dossiers/smic-kramarz-philippon-2001-cout-travail-emploi.md`
- `dossiers/smic-kramarz-philippon-payroll-tax-2001.md`
- `dossiers/smic-lhommeau-remy-2010-mobilite-salariale.md`
- `dossiers/smic-ourliac-nouveau-2012-synthesis-audit.md`
- `dossiers/smic-policy-scenarios.md`
- `dossiers/smic-quantitative-evidence.md`
- `dossiers/smic-quantitative-update-2026.md`
- `dossiers/smic-revaluations-audit-1994-2026.md`
- `dossiers/smic-revaluations-data-1970-1993.md`
- `dossiers/smic-revaluations-data-1994-2026.md`
- `dossiers/smic-sectoral-effects-exemptions-1993-1997.md`
- `dossiers/smic-series-reconciliation-1994-2026.md`
- `dossiers/smic-social-partners-evidence.md`
- `dossiers/smic-tresor-2025-wage-trajectories-audit.md`
- `dossiers/smic-youth-abowd-kramarz-lemieux-margolis-2000.md`
- `dossiers/the-shift-project-diagnostic-methodes-controverses.md`
- `dossiers/tig-peines-alternatives-incarceration.md`
- `dossiers/un-commun-accord-assemblee-citoyenne.md`

### forecasts

- `forecasts/README.md`
- `forecasts/registry.yml`

### governance

- `governance/backlog-review.md`
- `governance/backlog-reviews/2026-11-18.md`
- `governance/issue-domain-map.yml`
- `governance/issue-labels.json`

### hypotheses

- `hypotheses/hypothesis-boundary-norm-without-voter-stigma.yml`
- `hypotheses/hypothesis-independent-critique-vs-challenged-interview.yml`
- `hypotheses/hypothesis-multiarena-cordon-consistency.yml`
- `hypotheses/registry.yml`

### knowledge

- `knowledge/GRAPH.md`
- `knowledge/README.md`
- `knowledge/RELATION_TYPES.yml`
- `knowledge/TAGS.yml`
- `knowledge/TAXONOMY.yml`
- `knowledge/TERRITORIES.yml`
- `knowledge/concepts/pref-robustness.yml`
- `knowledge/concepts/registry.yml`
- `knowledge/concepts/shift-project-physical-economy.yml`
- `knowledge/domains/economy.md`
- `knowledge/domains/education.md`
- `knowledge/domains/energy.md`
- `knowledge/domains/politics.md`
- `knowledge/domains/security.md`
- `knowledge/graph.yml`
- `knowledge/mechanisms/registry.yml`

### research

- `research/analysis/parcoursup-2025-protocol.md`
- `research/analysis/parcoursup-cev-2026-protocol.md`
- `research/datasets/registry.yml`
- `research/foucher-comparaison-generationnelle.md`
- `research/studies/registry.yml`

### schemas

- `schemas/claim.schema.json`
- `schemas/concept.schema.json`
- `schemas/dataset.schema.json`
- `schemas/dossier.schema.json`
- `schemas/forecast.schema.json`
- `schemas/hypothesis.schema.json`
- `schemas/ingestion-batch.schema.json`
- `schemas/mechanism.schema.json`
- `schemas/source.schema.json`
- `schemas/study.schema.json`
- `schemas/territory.schema.json`

### scripts

- `scripts/analysis/analyze_parcoursup_2025.py`
- `scripts/analysis/audit_smic_decomposition_1996_2008.py`
- `scripts/analysis/audit_smic_power_decomposition_1971_2001.py`
- `scripts/analysis/audit_smic_real_purchasing_power_2001_2008_tef2010.py`
- `scripts/analysis/audit_smic_real_purchasing_power_2014_2025.py`
- `scripts/analysis/audit_smic_revaluations.py`
- `scripts/analysis/reconstruct_smic_monthly_purchasing_power.py`
- `scripts/analysis/trace_knowledge_impact.py`
- `scripts/report/generate_backlog_view.py`
- `scripts/validate/audit_issue_labels.py`
- `scripts/validate/check_synthesis_freshness.py`
- `scripts/validate/sync_issue_labels.py`
- `scripts/validate/validate_issue_domain_map.py`
- `scripts/validate/validate_registry.py`
- `scripts/validate/validate_syntheses.py`

### sources

- `sources/README.md`
- `sources/batches/README.md`
- `sources/registry.yml`
- `sources/smic-senate-1994-decomposition.yml`
- `sources/the-shift-project.yml`

### syntheses

- `syntheses/antoine-foucher-pacte-intergenerationnel.md`
- `syntheses/comparaison-quantitative-scenarios-energie-2026.md`
- `syntheses/comparaison-scenarios-transition-2026.md`
- `syntheses/cordon-sanitaire-belgique-efficacite.md`
- `syntheses/debat-barrage-cordon-sanitaire.md`
- `syntheses/parcoursup-education.md`
- `syntheses/pref-2026.md`
- `syntheses/protocole-comparatif-strategies-reponse-idees-antidemocratiques.md`
- `syntheses/registry.yml`
- `syntheses/smic-france.md`
- `syntheses/the-shift-project.md`
- `syntheses/tig-france.md`
- `syntheses/un-commun-accord-assemblee-citoyenne.md`

### templates

- `templates/ingestion-batch.yml`
- `templates/subject-synthesis.md`

### tests

- `tests/test_analyze_parcoursup_2025.py`
- `tests/test_backlog_view.py`
- `tests/test_issue_domain_map.py`
- `tests/test_parcoursup_2025_analysis.py`
- `tests/test_smic_decomposition_1996_2008.py`
- `tests/test_smic_monthly_reconstruction.py`
- `tests/test_smic_openfisca.py`
- `tests/test_smic_power_decomposition_1971_2001.py`
- `tests/test_smic_real_purchasing_power_2001_2008_tef2010.py`
- `tests/test_smic_real_purchasing_power_2014_2025.py`
- `tests/test_smic_revaluations_audit.py`
- `tests/test_sync_issue_labels.py`
- `tests/test_synthesis_freshness.py`
- `tests/test_trace_knowledge_impact.py`
- `tests/test_validate_registry.py`

### tools

- `tools/smic_openfisca.py`

## Limites et suite

- Le rapport n'affirme pas que chaque fichier est un objet métier : il sépare explicitement fiches canoniques, registres, code, tests, données, documentation et configuration.
- Étape suivante : implémenter le contrôle de couverture ciblé dans le validateur existant, avec exceptions fondées sur les chemins et conventions déjà documentés ; aucun nouveau schéma ni registre.
- Après implémentation : tests négatifs, exécution locale/CI, contrôle des écarts sur le corpus actuel, puis mesure x10/x100 si le coût le justifie.
