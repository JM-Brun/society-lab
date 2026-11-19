# Pilote transversal — éducation, compétences, emploi et salaires

Date : 19 novembre 2026  
Base : `main` au commit `fd9c85e86b6970ea8a593d31e2138218ec1be526`  
Issue de pilotage : [#112](https://github.com/JM-Brun/society-lab/issues/112)

## Synthèse

Le dépôt possède déjà plusieurs briques pertinentes pour examiner la chaîne éducation → compétences → emploi → salaires, mais elles ne forment pas encore un parcours empirique continu.

- Les inégalités scolaires et les écarts de compétences sont documentés par des études descriptives (Insee/DEPP, PISA).
- PIAAC mesure des compétences d'adultes et recueille des variables de contexte sur la situation professionnelle, mais son enquête est transversale.
- InserJeunes décrit l'insertion salariée à court terme des sortants de la voie professionnelle, principalement sous forme d'indicateurs agrégés.
- Le Panel Tous salariés permet de suivre des trajectoires annuelles d'emploi et de rémunération, mais ne relie pas à lui seul les trajectoires de formation et de compétences.
- L'appariement expérimental Céreq Génération 2021 / Base Tous salariés constitue le pont potentiel le plus direct entre formation et trajectoires salariales. Les taux d'appariement, le dictionnaire final, les biais de sélection, les résultats et les conditions d'accès restent toutefois à documenter.

**Conclusion opérationnelle :** le corpus autorise une cartographie des étapes et des sources, pas une conclusion causale sur le rendement salarial de la formation ou des compétences. Aucun mécanisme causal ni nouvelle arête épistémique n'est ajouté dans ce pilote.

## 1. Inventaire des briques existantes

| Étape | Objet canonique | Ce qu'il permet d'étudier | Limite structurante |
|---|---|---|---|
| Inégalités scolaires | `STUDY-SOCIAL-INEQUALITIES-SCHOOL-2025` | Écarts d'acquis selon l'origine sociale, dès les premières étapes scolaires | Étude descriptive ; les écarts ne décomposent pas les mécanismes causaux |
| Compétences à 15 ans | `STUDY-OECD-PISA-2022-FRANCE` | Scores standardisés et gradient socio-économique ; la fiche rapporte un écart de 113 points en mathématiques entre quartiles supérieur et inférieur | Ne mesure ni l'accès au supérieur ni les trajectoires d'emploi |
| Diplômes et transmission | `STUDY-OECD-INTERGEN-EDUCATION-ATTAINMENT-2025` | Association entre diplôme parental et diplôme des 25–34 ans | Association intergénérationnelle descriptive, pas effet causal isolé |
| Compétences adultes | `STUDY-PIAAC-2023-FRANCE-COMPETENCES` / `DATASET-PIAAC-2023-FRANCE` | Littératie, numératie, résolution adaptative de problèmes, diplômes et variables de situation sur le marché du travail | Enquête transversale ; pondérations et valeurs plausibles à respecter ; les scores ne couvrent pas toutes les compétences professionnelles |
| Insertion professionnelle | `STUDY-INSERJEUNES-INSERTION-2023` / `DATASET-INSERJEUNES-2023` | Emploi salarié à 6, 12, 18 et 24 mois selon millésime, poursuite d'études et résultats par formation/établissement | Champ limité à la voie professionnelle ; indicateurs agrégés ; emploi salarié et qualité/continuité de l'emploi incomplets |
| Pont formation–salaires | `STUDY-CEREQ-GENERATION-2021-BTS-MATCHING` / `DATASET-CEREQ-GENERATION-2021-BTS-MATCHED` | Appariement expérimental entre parcours Génération 2021 et Base Tous salariés | Taux de rapprochement, variables finales, attrition, biais de sélection, résultats et accès sécurisé non documentés dans les fiches actuelles |
| Trajectoires salariales | `STUDY-INSEE-PANEL-TOUS-SALARIES-TRAJECTORIES` / `DATASET-INSEE-PANEL-TOUS-SALARIES` | Trajectoires annuelles de salaire, d'emploi et d'employeur ; panel depuis 1976 | Accès soumis à conditions ; ruptures DADS/DSN et changements de champ ; absence de lien formation sans appariement |

Les études PIAAC, InserJeunes et Céreq sont explicitement rattachées aux domaines `DOMAIN-EDUCATION` et `DOMAIN-ECONOMY`. Le Panel Tous salariés est actuellement rattaché à l'économie seule.

## 2. État des claims et du graphe

### Claims existants

Les claims éducatifs déjà présents portent notamment sur :
- les écarts PISA de performance en mathématiques ;
- les écarts d'acquis associés à l'origine sociale dès l'entrée en maternelle ;
- la transmission intergénérationnelle des diplômes ;
- les indicateurs de propositions d'admission Parcoursup.

Ils restent au statut `under_review` dans le registre courant. Aucun claim n'est actuellement relié par `study_ids` aux trois études transversales PIAAC, InserJeunes et Céreq. Cela indique une absence de résultats structurés dans ces fiches, et non la preuve qu'aucun résultat n'existe dans les publications.

### Relations déjà présentes

Sur le `main` audité :
- 684 relations au total ;
- 87 `REL-SUPPORTS`, 326 `REL-INCLUDES`, 168 `REL-ABOUT`, 44 `REL-CITES`, 21 `REL-TRANSCRIBES` et 6 `REL-USES` (les autres types sont détaillés dans le registre du graphe).
- Les trois études PIAAC, InserJeunes et Céreq disposent de relations `REL-USES` vers leurs datasets, de liens thématiques `REL-ABOUT` vers les domaines éducation/économie et de liens bibliographiques `REL-CITES` vers leurs sources.
- Aucune fiche de mécanisme n'est actuellement enregistrée dans `knowledge/mechanisms/registry.yml`.

Ces liens sont des rattachements documentaires et thématiques. Ils ne démontrent pas que les compétences causent l'emploi ou les salaires. Les comptes par mots-clés ne sont pas publiés comme KPI : ils mélangent des références et des mentions textuelles, et ne constituent pas une mesure sémantique fiable.

## 3. Carte de recherche — pas un graphe causal validé

```text
Origine sociale / parcours scolaire
              |
              v
      Diplômes / formation
              |
              v
  Compétences mesurées (PIAAC)
              |
              v
     Accès et stabilité en emploi
              |
              v
       Salaires / progression
```

Ce schéma ordonne des étapes d'investigation ; ses flèches ne sont pas des relations causales établies. Chaque transition requiert des données et une stratégie d'identification adaptées.

Facteurs à documenter avant toute interprétation causale : origine sociale, âge et cohorte, spécialité et niveau de diplôme, expérience, secteur et profession, territoire, conjoncture locale, santé, genre, migration, sélection dans l'emploi salarié et sélection dans l'appariement administratif.

## 4. Lacunes probatoires à traiter

1. **Compétences → emploi :** exploiter PIAAC avec ses poids, valeurs plausibles et variables de contexte ; expliciter le caractère transversal et les associations conditionnelles.
2. **Formation → insertion :** extraire les indicateurs InserJeunes par formation, niveau, établissement et horizon ; conserver séparément emploi salarié et poursuite d'études.
3. **Formation → salaire :** obtenir la documentation technique du rapprochement Céreq/BTS–Base Tous salariés : population éligible, taux de matching, variables, attrition, périodes, champ salarial, confidentialité et modalités d'accès.
4. **Trajectoires salariales :** clarifier l'accès au Panel Tous salariés, les ruptures de série et les filtres de champ constant ; ne pas inférer le niveau de compétence à partir du seul salaire.
5. **Comparabilité :** distinguer les populations et unités d'observation (élève, adulte échantillonné, sortant de formation, individu apparié, emploi salarié annuel). Les indicateurs agrégés InserJeunes ne peuvent pas être raccordés directement à des salaires individuels.

## 5. Décisions et prochaines actions

| Priorité | Action | Critère de sortie |
|---|---|---|
| P0 | Demander/collecter la documentation complète du rapprochement Céreq et de son accès | Taux d'appariement, population, dictionnaire, attrition, champs et limites explicités |
| P1 | Faire une extraction contrôlée de PIAAC et de ses métadonnées | Tableau de variables, pondérations, valeurs plausibles et périmètres documentés |
| P1 | Extraire un premier tableau InserJeunes par niveau et spécialité | Valeurs, dénominateurs, millésime, champ et horizon enregistrés |
| P2 | Examiner la possibilité d'appariement avec le Panel Tous salariés | Conditions d'accès, variables et ruptures de mesure documentées |
| P2 | Revoir les claims et synthèses concernés | Claims atomiques, localisateurs et statuts de vérification ; aucune conclusion non étayée |
| P3 | Décider si une fiche `MECHANISM` est justifiée | Mécanisme explicite, conditions de portée, études favorables et contradictoires, alternatives et indicateurs |

Aucune nouvelle arête causale ne doit être ajoutée pour matérialiser le schéma de recherche. Les relations documentaires existantes peuvent être enrichies seulement lorsque les sources, localisateurs et objets concernés sont vérifiés.

## 6. Synthèse opérationnelle

Le maillon le mieux documenté est l'existence de données sur les compétences, l'insertion et les salaires prises séparément. Le maillon le moins assuré est leur raccordement longitudinal au niveau individuel, notamment formation → emploi → rémunération. Le projet d'appariement Céreq est la piste prioritaire, mais son potentiel ne doit pas être confondu avec un jeu de données accessible ni avec des résultats déjà observés.

**À la prochaine session :** obtenir la documentation technique du projet Céreq ; à défaut, documenter précisément les inconnues et avancer séparément sur les extractions PIAAC et InserJeunes. Maintenir la distinction entre descriptif, association, prédiction et effet causal.
