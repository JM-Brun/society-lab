# Audit de couverture du graphe de connaissances

Date : 18 novembre 2026

Instantané audité : `main` au commit `6df590bd6907515adf99511d22858759804d0203`.

## Objet et méthode

Mesurer la couverture des registres canoniques par le graphe `knowledge/graph.yml` et par les références structurées déjà présentes dans les registres. L'objectif est de distinguer :
- les objets présents dans un registre ;
- les objets ayant au moins une relation explicite dans le graphe ;
- les objets cités par les champs de référence structurés d'un autre objet ;
- les objets qui ne présentent aucun de ces liens.

Le relevé est calculé à partir des entrées JSON intégrées dans les registres YAML et des 606 relations du graphe. Les références examinées sont `source_ids`, `study_ids`, `dataset_ids`, `hypothesis_ids`, `claim_ids`, `concept_ids`, `supporting_study_ids`, `challenging_study_ids` et `source_verifications[].source_id`. Les mentions textuelles dans les notes ne sont pas comptées comme relations structurées.

## Inventaire et couverture

| Type d'objet | Entrées | Avec au moins une arête du graphe | Avec une arête autre que `REL-ABOUT` |
|---|---:|---:|---:|
| Sources | 220 | 184 | 144 |
| Études | 62 | 60 | 60 |
| Jeux de données | 14 | 12 | 10 |
| Claims | 83 | 80 | 80 |
| Hypothèses | 22 | 22 | 22 |
| Dossiers | 25 | 25 | 25 |
| Concepts | 15 | 15 | 12 |
| Mécanismes | 0 | 0 | 0 |
| **Total** | **441** | **398** | **353** |

Le graphe comprend 606 arêtes :
- `REL-INCLUDES` : 290
- `REL-ABOUT` : 168
- `REL-SUPPORTS` : 84
- `REL-TRANSCRIBES` : 19
- `REL-CHILD-OF` : 8
- `REL-SUMMARIZED-BY` : 8
- `REL-QUALIFIES` : 8
- `REL-CITES` : 7
- `REL-GEOGRAPHICALLY-WITHIN` : 7
- `REL-USES` : 6
- `REL-SUMMARIZES` : 1

Les 168 arêtes `REL-ABOUT` relient principalement des objets à des domaines. Elles sont utiles pour la navigation thématique, mais ne doivent pas être considérées comme une preuve de traçabilité documentaire ou épistémique. C'est pourquoi une deuxième mesure exclut ces arêtes.

## Objets sans relation explicite

### Nœuds sans aucune arête du graphe

- Sources : 36
- Études : 2
- Datasets : 2
- Claims : 3
- Hypothèses, dossiers et concepts : 0

Les objets sans arête peuvent néanmoins être mentionnés dans les notes ou reliés par un champ de registre ; inversement, une simple arête `REL-ABOUT` ne constitue pas un lien de preuve.

### Objets sans arête et sans référence structurée entrante

Le croisement des deux vues met en évidence 29 objets à examiner en priorité :
- 25 sources : `SOURCE-ATIGIP-TIG360-PLATFORM`, `SOURCE-MINJUSTICE-TIG-47000-PLACES-2026`, `SOURCE-CGT-SALAIRES-2000-2026`, `SOURCE-CFDT-SMIC-NEGOCIATIONS-2026`, `SOURCE-CFDT-BRANCH-GRIDS-2026`, `SOURCE-CFTC-SMIC-GRIDS-2026`, `SOURCE-FO-POUVOIR-ACHAT-2026`, `SOURCE-MEDEF-PLFSS-RELIEFS-2024`, `SOURCE-U2P-CAPEB-SALAIRES-2026`, `SOURCE-MEDEF-SALAIRES-COUT-TRAVAIL-2025`, `SOURCE-FO-CONGRESS-RESOLUTION-2026`, `SOURCE-UNSA-SMIC-COUP-POUCE-2025`, `SOURCE-CFE-CGC-SMIC-GRIDS-2026`, `SOURCE-U2P-SMIC-1500-2026`, `SOURCE-MEDEF-SMIC-CONFERENCE-2026`, `SOURCE-NEUMARK-WASCHER-FRANCE-YOUTH-1997`, `SOURCE-ABOWD-KRAMARZ-MARGOLIS-NBER-1999`, `SOURCE-DARES-INFLATION-SALAIRES-2023`, `SOURCE-DARES-SMIC-REVAL-2026`, `SOURCE-UK-DFE-2024-HARASSMENT-CENSORSHIP`, `SOURCE-TADROS-2022-RIGHTS-NOPLATFORMING`, `SOURCE-LIBERAL-DEFENSE-NOPLATFORMING-2024`, `SOURCE-UN-COMMUN-ACCORD-ABOUT`, `SOURCE-UN-COMMUN-ACCORD-HOMEPAGE`, `SOURCE-EDITION-AUBE-ANTOINE-FOUCHER-2026`.
- 1 étude : `STUDY-LASELVA-ETAL-2026-CLIMATE-PREBUNKING`.
- 2 datasets : `DATASET-SMIC-REAL-POWER-2001-2008-TEF2010`, `DATASET-SMIC-POWER-DECOMPOSITION-1971-2001`.
- 3 claims : `CLAIM-SMIC-MARGINAL-RATES-1P2-2`, `CLAIM-SMIC-WAGE-PROGRESSION-1P2-2`, `CLAIM-SMIC-LOW-WAGE-CAREER-MOBILITY-OECD-2025`.

Ce résultat ne signifie pas que ces objets sont erronés ou inutiles : certains peuvent être des sources de contexte, des positions d'acteurs ou des pièces documentaires qui n'ont pas vocation à soutenir un claim. Chaque cas doit être qualifié avant ajout d'arêtes.

## Diagnostic du validateur actuel

`scripts/validate/validate_registry.py` contrôle :
- l'unicité et le format des identifiants ;
- les schémas et les vocabulaires ;
- les références structurées de premier niveau vers sources, études, datasets, claims, hypothèses et concepts ;
- les références de vérification de sources dans les claims ;
- les extrémités, types, justifications et doublons des relations du graphe.

Il ne mesure pas la couverture du graphe et ne signale pas les objets isolés. Il ne vérifie pas non plus la réciprocité des relations dans les champs des registres, ce qui n'est pas nécessairement souhaitable : le graphe est déjà la représentation relationnelle commune et toutes les relations ne sont pas symétriques.

Le registre `knowledge/mechanisms/registry.yml` est présent mais contient actuellement zéro mécanisme. Le schéma de mécanisme existe ; l'absence de fiches ne doit pas être compensée par des mécanismes artificiels ou des liens causaux inférés automatiquement.

## Décisions recommandées

1. Ne pas rendre bloquant un seuil global de connectivité : les sources de contexte et les objets en cours de qualification peuvent légitimement rester isolés temporairement.
2. Ajouter un rapport de couverture informatif, avec liste des nœuds sans relation et date/SHA de l'instantané, puis suivre les évolutions dans le temps.
3. Traiter les 29 objets « ni arête ni référence entrante » comme une file de revue humaine, en distinguant source contextuelle, artefact de données, étude, claim et objet obsolète.
4. Pour les dossiers prioritaires (SMIC, TIG, Parcoursup), vérifier les liens entre source, étude, dataset, claim, hypothèse, concept et synthèse à partir du contenu réel ; ne pas créer d'arêtes uniquement pour faire monter un taux de couverture.
5. Créer des fiches de mécanismes seulement lorsque le mécanisme est explicité, ses conditions de portée identifiées et ses preuves contradictoires documentées.

## Limites

- Les champs de référence examinés ne comprennent pas les mentions en texte libre, les liens Markdown ni les relations implicites.
- La couverture par arêtes ne mesure ni la qualité de la relation, ni l'indépendance des preuves, ni la validité causale.
- Les références sont orientées : le comptage « entrant » ne préjuge pas d'une relation inverse.
- Les résultats sont un instantané du commit indiqué et devront être recalculés après toute réconciliation.
