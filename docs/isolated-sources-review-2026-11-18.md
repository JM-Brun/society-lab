# Revue des 25 sources sans relation structurée

Date : 18 novembre 2026  
Périmètre : instantané `main` après la réconciliation #151.  
Référence initiale : `docs/structured-knowledge-graph-audit-2026-11-18.md`.

## Objectif et règle de décision

Cette revue qualifie individuellement les 25 sources qui ne présentent ni arête dans `knowledge/graph.yml`, ni référence structurée entrante identifiée dans l'audit. Elle ne cherche pas à réduire artificiellement le nombre de nœuds isolés.

Une relation n'est ajoutée que si le registre établit un lien précis vers un objet cible : citation bibliographique, transcription d'un jeu de données, source explicitement mobilisée par une claim, ou inclusion documentée dans un dossier. Une position d'acteur est une preuve de ce que cet acteur affirme, pas une preuve de la validité empirique de son affirmation. Une page institutionnelle descriptive ne prouve pas l'efficacité d'un dispositif. Les sources normatives ne sont pas des évaluations empiriques.

## Résultats source par source

| Source | Fonction documentaire | Décision sur le graphe |
|---|---|---|
| `SOURCE-ATIGIP-TIG360-PLATFORM` | Présentation officielle de la plateforme et de ses fonctionnalités opérationnelles | Conserver isolée à ce stade. Cible potentielle : claim sur le stock/capacité de postes TIG, mais la page décrit l'outil et non la disponibilité locale effective ; aucune claim de registre ne la cite explicitement. |
| `SOURCE-MINJUSTICE-TIG-47000-PLACES-2026` | Communication ministérielle annonçant 47 000 places et leur répartition | Conserver isolée à ce stade. Cible potentielle : `CLAIM-TIG-NATIONAL-POSTS-2018-2025`, sous réserve de vérifier que le chiffre 2026 et le périmètre de « places » sont compatibles avec la claim existante. Ne pas assimiler places recensées et places mobilisables. |
| `SOURCE-CGT-SALAIRES-2000-2026` | Revendication salariale confédérale | Conserver isolée : source primaire d'une position d'acteur, mais aucun claim atomique du registre ne porte sur le contenu précis de cette revendication. |
| `SOURCE-CFDT-SMIC-NEGOCIATIONS-2026` | Communiqué CFDT sur l'ouverture des négociations salariales | Conserver isolée : documente une position datée ; ne constitue pas une preuve d'effet économique. |
| `SOURCE-CFDT-BRANCH-GRIDS-2026` | Position CFDT et suivi des négociations de branches | Conserver isolée : les chiffres de branches doivent être rapprochés des textes conventionnels et de leurs dates d'effet avant création d'une claim. |
| `SOURCE-CFTC-SMIC-GRIDS-2026` | Position CFTC sur SMIC, grilles et allègements | Conserver isolée : propositions normatives, non résultats évalués ; aucune claim dédiée n'est actuellement référencée. |
| `SOURCE-FO-POUVOIR-ACHAT-2026` | Position FO sur le déblocage de l'épargne salariale | Conserver isolée : sujet connexe au pouvoir d'achat mais pas une preuve sur le niveau du SMIC ni une revendication salariale chiffrée. |
| `SOURCE-MEDEF-PLFSS-RELIEFS-2024` | Déclaration commune patronale sur les allègements | Conserver isolée : position collective sur le coût du travail ; ne pas attribuer cette position à chaque organisation ni la traiter comme évaluation causale. |
| `SOURCE-U2P-CAPEB-SALAIRES-2026` | Position professionnelle sur salaires, SMIC et charges des TPE artisanales | Conserver isolée : source de position ; les effets avancés doivent être confrontés à des données et simulations distinctes. |
| `SOURCE-MEDEF-SALAIRES-COUT-TRAVAIL-2025` | Entretien d'un représentant du MEDEF | Conserver isolée : déclaration d'acteur, pas une mesure des effets d'une hausse du SMIC. |
| `SOURCE-FO-CONGRESS-RESOLUTION-2026` | Résolution confédérale normative | Conserver isolée : la cible revendiquée est une position politique, non une estimation empirique. La date d'adoption exacte reste à contrôler. |
| `SOURCE-UNSA-SMIC-COUP-POUCE-2025` | Position UNSA en faveur d'un coup de pouce | Conserver isolée : source primaire d'une position ; ne mesure pas les effets sur pauvreté ou emploi. |
| `SOURCE-CFE-CGC-SMIC-GRIDS-2026` | Article de presse rapportant des propos de la CFE-CGC | Conserver isolée : source secondaire ; retrouver le communiqué ou l'enregistrement primaire avant d'en faire une claim institutionnelle. |
| `SOURCE-U2P-SMIC-1500-2026` | Article de presse rapportant une déclaration du président de l'U2P | Conserver isolée : source secondaire ; distinguer déclaration médiatique, mandat formel et conditionnalité sur les allègements. |
| `SOURCE-MEDEF-SMIC-CONFERENCE-2026` | Article de presse rapportant les réactions du MEDEF | Conserver isolée : source secondaire ; ne pas confondre réaction à une annonce et preuve sur l'emploi. |
| `SOURCE-NEUMARK-WASCHER-FRANCE-YOUTH-1997` | Article académique sur un épisode historique et l'emploi des jeunes | Candidat à une relation `REL-CITES` depuis une fiche Study dédiée, si elle existe ou est créée après lecture du texte intégral. Pas d'arête ajoutée : accès limité au résumé et identification/robustesse à auditer. |
| `SOURCE-ABOWD-KRAMARZ-MARGOLIS-NBER-1999` | Working paper NBER sur les salaires minimums en France et aux États-Unis | Candidat à une relation `REL-CITES` depuis une fiche Study dédiée. Pas d'arête ajoutée : vérifier l'articulation avec les travaux Abowd déjà présents et éviter de compter plusieurs versions d'un même travail comme preuves indépendantes. |
| `SOURCE-DARES-INFLATION-SALAIRES-2023` | Analyse administrative des salaires, minima conventionnels et inflation | Candidat à une relation `REL-CITES`/ `REL-SUPPORTS` après identification de la fiche Study ou des claims exactes. Aucune claim existante identifiée dans l'audit comme la citant ; les constats descriptifs ne doivent pas être convertis en causalité. |
| `SOURCE-DARES-SMIC-REVAL-2026` | Statistique administrative sur les bénéficiaires directs de la revalorisation 2026 | Candidat à une relation vers une claim descriptive sur les bénéficiaires 2026, mais la claim existante doit être vérifiée pour confirmer qu'elle cite bien cette publication et le même champ. Aucune arête ajoutée sur simple proximité thématique. |
| `SOURCE-UK-DFE-2024-HARASSMENT-CENSORSHIP` | Revue rapide institutionnelle sur harcèlement et censure dans l'enseignement supérieur anglais | Conserver isolée jusqu'à rattachement explicite à une Study ou claim. Elle documente des fréquences et des limites de mesure, pas l'efficacité du no-platforming. |
| `SOURCE-TADROS-2022-RIGHTS-NOPLATFORMING` | Analyse juridique et normative des droits liés au no-platforming | Conserver isolée : source normative. Une relation à une Study de revue de littérature est possible si une fiche d'étude la cite explicitement ; elle ne doit pas soutenir une claim d'efficacité empirique. |
| `SOURCE-LIBERAL-DEFENSE-NOPLATFORMING-2024` | Défense normative libérale du no-platforming | Conserver isolée : argumentation normative, non preuve empirique. À relier à une étude bibliographique uniquement après traçabilité explicite. |
| `SOURCE-UN-COMMUN-ACCORD-ABOUT` | Présentation institutionnelle des rôles, de l'équipe et des garants | Conserver isolée temporairement. La source est pertinente pour le dossier dédié, mais les rôles déclarés doivent être reliés à des claims descriptives vérifiables et ne valent pas évaluation indépendante des garanties. |
| `SOURCE-UN-COMMUN-ACCORD-HOMEPAGE` | Page d'accueil et actualités de l'initiative | Conserver isolée temporairement. Source primaire de communication et de calendrier, mais non inventaire exhaustif ni évaluation indépendante. |
| `SOURCE-EDITION-AUBE-ANTOINE-FOUCHER-2026` | Notice éditoriale et biographie d'auteur | Conserver isolée : utile aux métadonnées bibliographiques, mais pas à l'étayage des propositions économiques du livre. |

## Bilan et suites ciblées

- 25/25 sources examinées individuellement.
- 0 arête ajoutée : aucune relation de preuve ou de citation n'est suffisamment établie par les références structurées disponibles dans cet instantané.
- 2 sources TIG sont des candidates prioritaires à réexaminer avec les claims sur le stock national de postes et la capacité opérationnelle.
- 4 sources SMIC de recherche/statistique sont candidates à une réconciliation avec les claims descriptives et les fiches Study ; les références exactes doivent être établies avant toute arête.
- 13 sources de positions d'acteurs sociaux/patronaux/politiques sont conservées comme matériaux de position, sans les transformer en preuves empiriques.
- 3 sources sur le no-platforming sont conservées selon leur fonction empirique ou normative distincte.
- 2 pages Un commun accord sont des sources primaires de présentation ; elles appellent des claims descriptives séparées des évaluations indépendantes.
- 1 notice éditoriale reste une référence bibliographique.

### Travail restant

1. Vérifier les quatre candidates SMIC contre les claims et études existantes, en particulier les champs `source_ids` et `source_verifications`, puis créer seulement les liens effectivement cités.
2. Contrôler les deux sources TIG par rapport à `CLAIM-TIG-NATIONAL-POSTS-2018-2025` et aux documents opérationnels locaux ; séparer stock recensé, postes ouverts, capacité mobilisable et activité réelle.
3. Vérifier si les sources Neumark–Wascher et Abowd–Kramarz–Margolis correspondent à des études déjà enregistrées ou à des travaux distincts ; lire les textes primaires et dédoublonner les versions.
4. Compléter la bibliographie de la revue no-platforming sans confondre argument normatif, données de fréquence et effet causal.
5. Pour Un commun accord, créer des claims descriptives atomiques seulement si les informations de présentation sont reprises et vérifiables ; chercher séparément les audits externes et documents de gouvernance.
6. Recalculer l'audit de couverture après ces réconciliations. Le nombre de sources isolées n'est pas un KPI de qualité et ne doit pas devenir un seuil bloquant.

Aucun schéma, registre, type de relation ou identifiant métier n'a été ajouté dans cette revue.
