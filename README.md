# Society Lab

**Comprendre les grands enjeux de société par la recherche, les preuves et la pensée systémique.**

Society Lab est un projet documentaire indépendant de compilation critique, de mise en relation des connaissances et de synthèse des transformations politiques, économiques, sociales, environnementales et technologiques. Il étudie les recherches et débats déjà existants ; il ne conduit pas ses propres expériences.

## Finalité et méthode éditoriale

Society Lab rassemble des études scientifiques, sociologiques et politiques, des expérimentations déjà publiées, des données, des évaluations, des travaux historiques, des rapports et des débats argumentés. Le but est d'en tirer des bilans compréhensibles, sourcés, non partisans et proportionnés au niveau réel des preuves. Non partisan ne signifie pas fausse équivalence : les arguments sont présentés loyalement, mais leur poids dépend de leur documentation et de leur robustesse. Voir la [charte éditoriale et méthode de synthèse](docs/editorial-charter.md).

## Trois approches complémentaires

- **Knowledge** — structurer les concepts, institutions, mécanismes et connaissances.
- **Research** — examiner les publications, données, méthodes et résultats.
- **Analysis** — confronter les explications, expliciter les arbitrages et produire des synthèses révisables.

## Principes

- Les affirmations importantes sont traçables jusqu'à leurs sources.
- Faits, résultats empiriques, interprétations, hypothèses et jugements de valeur sont distingués.
- Les sources primaires sont privilégiées lorsque cela est pertinent.
- Les preuves sont évaluées par rapport à une question et une méthode, pas à la seule réputation de leur émetteur.
- Les désaccords sont présentés loyalement, sans fausse équivalence entre niveaux de preuve.
- Les incertitudes, limites et révisions sont documentées.
- L'IA assiste la recherche, mais ne valide pas seule les conclusions.

## Périmètre territorial

Society Lab adopte une approche **multiscalaire, d'abord ancrée en France**, inscrite dans son contexte européen et ouverte aux dynamiques internationales et mondiales. Les neuf niveaux de référence vont du monde à l'Île de Nantes : monde, international/transnational, Europe, France, Pays de la Loire, Loire-Atlantique, Nantes Métropole, Nantes et Île de Nantes.

Cette liste est un cadre d'analyse, pas une hiérarchie administrative stricte. L'international est une dimension transversale ; l'Europe ne se réduit pas à l'Union européenne ; Nantes Métropole, la commune de Nantes et l'Île de Nantes désignent des périmètres différents. Chaque recherche précise les territoires observés, les juridictions compétentes, la population, la période et les limites géographiques pertinentes.

L'analyse circule dans les deux sens : les dynamiques globales et européennes aident à expliquer les situations françaises et locales ; les observations, initiatives et résultats locaux permettent en retour de tester, nuancer et enrichir les interprétations plus générales. Les liens latéraux entre territoires (réseaux, flux, coopérations, comparaisons et interdépendances) sont également pris en compte. Voir [le référentiel territorial](knowledge/TERRITORIES.yml) et [le cadre d'analyse multiscalaire](docs/multiscalar-analysis.md).

## Architecture de connaissance

Le dépôt organise les contenus autour d'objets identifiés et reliés :
- **Sources, études et jeux de données** : provenance et éléments de preuve.
- **Affirmations et hypothèses** : propositions examinées, statut et limites.
- **Concepts, mécanismes et institutions** : base de connaissance structurée.
- **Dossiers et analyses** : synthèses transversales et résultats reproductibles.
- **Graphe de connaissances** : relations typées entre objets, conservées dans Git et exportables.

Les domaines sont définis dans [la taxonomie](knowledge/TAXONOMY.yml), les tags dans [le vocabulaire contrôlé](knowledge/TAGS.yml) et les relations dans [l'ontologie légère](knowledge/RELATION_TYPES.yml). Voir [métadonnées et nomenclature](docs/metadata-and-naming.md), [graphe](knowledge/GRAPH.md) et [protocole d'ingestion](docs/ingestion-protocol.md).

## Premier dossier de recherche

- [The Shift Project : diagnostic, méthodes, propositions et controverses](dossiers/the-shift-project-diagnostic-methodes-controverses.md) — dossier critique sur le think tank, son cadre de la double contrainte carbone, ses méthodes, son financement, ses propositions et les controverses documentées ; voir aussi la [synthèse](syntheses/the-shift-project.md).
- [Audit du PREF 2026 : robustesse, scénarios et conditions de mise en œuvre](dossiers/pref-2026-audit-robustesse-scenarios.md) — analyse du rapport technique, des vingt chantiers, des variantes, des bouclages et des limites à auditer ; voir aussi la [synthèse PREF](syntheses/pref-2026.md).
- [Comparer les trajectoires françaises de transition](dossiers/comparaison-scenarios-transition-pref-rte-ademe-negawatt-snbc3.md) — matrice comparative PREF, RTE, ADEME, négaWatt et SNBC 3 ; voir aussi la [synthèse](syntheses/comparaison-scenarios-transition-2026.md).

## Dossiers de recherche

- [Éducation](knowledge/domains/education.md) — page thématique reliant les connaissances, sources, études, données, affirmations, hypothèses et priorités de recherche.
- [Sécurité, justice et libertés](knowledge/domains/security.md) — page thématique sur les politiques de sécurité, l'exécution des peines, l'efficacité pénale et les libertés.
- [Économie, emploi et productivité](knowledge/domains/economy.md) — page thématique sur les salaires, le marché du travail, les entreprises et la productivité.
- [Énergie et ressources](knowledge/domains/energy.md) — page thématique sur les systèmes énergétiques, les ressources, les infrastructures et les dépendances.
- [Travaux d'intérêt général : efficacité pénale, coûts et freins au déploiement en France](dossiers/tig-peines-alternatives-incarceration.md) — dossier de recherche sur le recours au TIG en France, les comparaisons européennes, la récidive, la dissuasion et les conditions d'exécution ; voir aussi la [synthèse TIG](syntheses/tig-france.md).
- [Augmenter le SMIC en France : pouvoir d'achat, emploi, salaires et finances publiques](dossiers/smic-france-tradeoffs.md) — dossier contradictoire sur le salaire minimum, son indexation, ses effets économiques et ses interactions socio-fiscales ; [revue des travaux économiques](dossiers/smic-economists-literature-review.md), [synthèse quantitative des résultats](dossiers/smic-quantitative-evidence.md), [positions des partenaires sociaux](dossiers/smic-social-partners-evidence.md) et [synthèse générale du sujet](syntheses/smic-france.md).
- [Parcoursup et l'égalité des chances dans le système éducatif français](dossiers/parcoursup-education-equity.md) — dossier pilote en cours, avec registres de preuves et protocole quantitatif ; voir aussi la [synthèse Parcoursup](syntheses/parcoursup-education.md).
- [Politique et démocratie](knowledge/domains/politics.md) — page thématique sur les partis, les élections, le pluralisme et les conditions de la vie démocratique.
- [Un commun accord : initiative citoyenne et assemblée délibérative](dossiers/un-commun-accord-assemblee-citoyenne.md) — analyse du panel tiré au sort, du dispositif d'information et de délibération, des garanties annoncées et des six dilemmes ; voir la [synthèse provisoire](syntheses/un-commun-accord-assemblee-citoyenne.md).
- [Débat, barrage et cordon sanitaire](dossiers/debat-barrage-cordon-sanitaire.md) — comparaison Belgique–Allemagne–France des stratégies de débat, de non-coalition, de démarcation médiatique et de barrage électoral ; voir le [protocole de revue systématique](dossiers/protocole-revue-systematique-cordon-sanitaire.md), la [matrice de preuves multi-arènes](dossiers/matrice-preuves-cordon-sanitaire.md), le [dossier spécialisé sur le modèle belge](dossiers/cordon-sanitaire-belgique-efficacite.md) et la [synthèse dédiée](syntheses/debat-barrage-cordon-sanitaire.md).
- [Protocole comparatif des stratégies de réponse aux idées antidémocratiques](dossiers/protocole-comparatif-strategies-reponse-idees-antidemocratiques.md) — cartographie documentaire des travaux existants sur la contradiction, l'analyse indépendante, la pédagogie, les explications alternatives et l'exposition médiatique ; aucune expérimentation n'est prévue par Society Lab.

## Synthèses des sujets

Chaque sujet de recherche doit disposer d'une synthèse autonome, datée et révisable, qui présente les constats, les preuves, les controverses, les limites, les conclusions et les travaux restant à mener. Les synthèses ne remplacent pas les dossiers détaillés ni les registres structurés. La correspondance entre dossiers principaux et synthèses est tenue dans le [registre des synthèses](syntheses/registry.yml) et vérifiée automatiquement par GitHub Actions.

- [Synthèse TIG — France](syntheses/tig-france.md)
- [Synthèse SMIC — France](syntheses/smic-france.md)
- [Synthèse Parcoursup — égalité des chances](syntheses/parcoursup-education.md)
- [Synthèse débat, barrage et cordon sanitaire](syntheses/debat-barrage-cordon-sanitaire.md)
- [Synthèse documentaire des stratégies de réponse aux idées antidémocratiques](syntheses/protocole-comparatif-strategies-reponse-idees-antidemocratiques.md)
- [Modèle réutilisable de synthèse](templates/subject-synthesis.md)

## Documents fondateurs

- [Charte éditoriale et méthode de synthèse](docs/editorial-charter.md)
- [Audit transversal de l'état des connaissances et des synthèses](docs/audit-transversal-etat-des-connaissances.md) — bilan comparatif des dossiers, preuves, synthèses, graphes et priorités de consolidation.
- [Charte fondatrice](CHARTER.md)
- [Méthodologie](METHODOLOGY.md)
- [Architecture](docs/architecture.md)
- [Feuille de route](docs/roadmap.md)
- [Politique des sources](docs/source-policy.md)
- [Politique de licences](docs/licensing.md)
- [Prévisions probabilistes](docs/forecasting.md) et [registre des prévisions](forecasts/README.md)
- [Incertitudes et révisions](docs/uncertainty-and-revisions.md)
- [Guide de contribution](CONTRIBUTING.md)
- [Contrat d'intégration inter-dépôts](docs/cross-repository-contract.md)

## État du projet

Les structures de métadonnées, taxonomie transversale, types de relations et registres sont initialisés. Un premier dossier pilote sur Parcoursup et l'égalité des chances dans l'éducation est en cours ; ses sources et affirmations restent à examiner. Le dossier énergie demeure un chantier ultérieur.

## Langue et statut

La documentation éditoriale est principalement en français. Les sources peuvent être dans toute langue ; leur langue originale et les éventuelles traductions sont indiquées. Society Lab est un projet personnel public et indépendant, sans affiliation institutionnelle implicite.