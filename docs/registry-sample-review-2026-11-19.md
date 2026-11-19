# Revue d'échantillon des registres — 19 novembre 2026

**Périmètre :** contrôle statique de fiches déjà présentes dans les registres Source, Study, Dataset et Claim. Cette revue ne remplace pas la vérification des publications originales, ne valide pas les chiffres et ne constitue pas une revue humaine indépendante.

## 1. Échantillon retenu

| Objet | Identifiant | Raison du choix |
|---|---|---|
| Source | `SOURCE-OECD-PIAAC-DATA-METHODOLOGY-2023` | Documentation méthodologique d'une enquête de compétences |
| Source | `SOURCE-DEPP-INSERJEUNES-2026` | Documentation d'indicateurs d'insertion |
| Source | `SOURCE-CEREQ-GENERATION-2021-BTS-MATCHING-2026` | Documentation d'un appariement administratif |
| Study | `STUDY-PIAAC-2023-FRANCE-COMPETENCES` | Enquête transversale et analyse des compétences |
| Study | `STUDY-INSERJEUNES-INSERTION-2023` | Indicateurs agrégés d'insertion |
| Study | `STUDY-CEREQ-GENERATION-2021-BTS-MATCHING` | Étude de faisabilité/documentation de l'appariement |
| Dataset | `DATASET-PIAAC-2023-FRANCE` | Microdonnées et indicateurs pondérés |
| Dataset | `DATASET-INSERJEUNES-2023` | Indicateurs agrégés par formation/établissement |
| Dataset | `DATASET-CEREQ-GENERATION-2021-BTS-MATCHED` | Données appariées à accès conditionnel |
| Claim | `CLAIM-PARCOURSUP-2026-APPLICANTS` | Exemple de claim avec extraction et vérification structurées |
| Claim | `CLAIM-PISA-2022-SOCIOECONOMIC-GAP` | Exemple de claim sans `source_verifications` |

## 2. Constats par chaîne de données

### PIAAC

- La source de documentation identifie l'OCDE, le deuxième cycle et la vague 2023 ; la date est renseignée à l'année (2024).
- La fiche Study décrit le plan d'enquête, la population française hors DROM, les méthodes, les résultats et les limites.
- La fiche Dataset précise l'unité adulte échantillonnée, les domaines évalués, la version et les précautions sur les poids et valeurs plausibles.
- La licence/les conditions de réutilisation sont mentionnées comme « à vérifier » dans la fiche Dataset ; la fiche Source ne fournit pas de licence.

**Évaluation :** chaîne documentaire relativement complète pour une analyse descriptive, mais pas prête à soutenir une analyse sans examen du manuel, des poids, des valeurs plausibles, des variables et des conditions de réutilisation. Le caractère transversal interdit d'interpréter directement les associations comme des effets causaux.

### InserJeunes

- La source documente le dispositif administratif, son champ et ses limites.
- La fiche Study précise les sortants de la voie professionnelle, les méthodes d'appariement administratif, les horizons et les limites.
- La fiche Dataset énumère les taux d'emploi salarié, la poursuite d'études et les variables de formation ; elle précise que l'unité exacte doit être vérifiée pour chaque fichier.
- La licence indique que les conditions sont précisées sur le portail et doivent être vérifiées pour chaque fichier.

**Évaluation :** bonne description du champ et des indicateurs, mais une extraction effective doit documenter le fichier exact, son millésime, les dénominateurs, les cellules supprimées/masquées, les horizons réellement disponibles et l'unité de chaque indicateur. Ne pas raccorder directement ces agrégats à des trajectoires salariales individuelles.

### Céreq Génération 2021 / Base Tous salariés

- La source publique indique qu'un appariement expérimental a été réalisé et que des documents de gouvernance des données existent.
- La fiche Study décrit le potentiel et les limites, mais les taux de rapprochement, le dictionnaire final, les biais de sélection et les résultats ne sont pas documentés.
- La fiche Dataset indique `access_status: request_required`, un accès et des conditions de diffusion à vérifier, et décrit les variables sous réserve du périmètre effectivement apparié.

**Évaluation :** piste probatoire prioritaire, mais pas dataset librement disponible. La page publique est accessible (`Source.access_status: open`) tandis que le dataset est à accès sur demande : cette distinction est cohérente si elle est comprise comme accessibilité de la documentation versus accès aux microdonnées. Il faut préserver cette distinction dans les synthèses.

## 3. Contrôle des claims

### Exemple avec traçabilité structurée

`CLAIM-PARCOURSUP-2026-APPLICANTS` possède :
- une proposition descriptive et un périmètre explicite ;
- une source et une étude liées ;
- une entrée `source_verifications` au statut `source_checked` ;
- un localisateur qui identifie les sections des deux communiqués ;
- une extraction de résultat avec valeur, unité, population, période, géographie, définition, méthode et date ;
- une provenance de type `source_extracted`.

C'est un exemple utile de traçabilité, mais pas un modèle universel à imposer dès la découverte. Le contrôle direct des pages originales et l'adéquation du localisateur restent les éléments déterminants.

### Exemple sans vérification formalisée

`CLAIM-PISA-2022-SOCIOECONOMIC-GAP` relie une source et une étude et décrit une portée, mais ne comporte pas de `source_verifications` dans la fiche examinée.

**Interprétation :** ce n'est pas automatiquement une erreur de schéma ou la preuve que le claim est faux. C'est un candidat pertinent pour le profil « claim_checked » : retrouver le passage/tableau, vérifier la définition des quartiles et l'écart, puis enregistrer le localisateur, la date et le statut de contrôle. Le claim reste `under_review` dans le registre.

## 4. Écarts classés

| Écart observé | Classe | Action recommandée | Ne pas faire |
|---|---|---|---|
| Licence absente ou « à vérifier » | Inconnue / non vérifiée | Vérifier les conditions du fichier précis avant extraction ou diffusion | Remplir par une licence supposée |
| Unité InserJeunes à confirmer par fichier | Précision insuffisante | Examiner dictionnaire, documentation et fichier exact | Déduire une unité unique pour tous les indicateurs |
| Taux et variables Céreq non publiés | Information inaccessible dans la documentation examinée | Demander documentation technique, dictionnaire, taux d'appariement et conditions d'accès | Présenter les variables potentielles comme observées ou disponibles |
| Claim PISA sans vérification formalisée | Traçabilité incomplète à l'étape de vérification | Ajouter une vérification avec localisateur après contrôle de la publication | Modifier le statut sans vérification |
| PIAAC transversal | Limite méthodologique intrinsèque | Limiter l'inférence à la description/association | Conclure à un effet causal formation-compétences-emploi |
| Source Céreq ouverte, dataset sur demande | Différence entre accès à la documentation et accès aux données | Maintenir des statuts d'accès distincts | Déduire que les données sont librement téléchargeables |

## 5. Conséquences pour la matrice

1. La matrice doit conserver des profils d'étape distincts : une fiche découverte n'a pas à comporter un localisateur d'extraction ni une vérification de claim.
2. Pour le profil `extracted`, exiger la traçabilité de la valeur : localisateur, unité, dénominateur, population, période, définition et méthode.
3. Pour le profil `claim_checked`, exiger une vérification de chaque source effectivement mobilisée, ou une justification explicite de non-applicabilité.
4. Pour les datasets, distinguer documentation accessible, accès aux données, licence de réutilisation et artefact effectivement récupéré.
5. Pour les claims causaux, ajouter un examen méthodologique propre au type de claim ; la présence de références n'est pas une stratégie d'identification.

## 6. Limites de cette revue

- Les constats proviennent du contenu actuellement enregistré dans les quatre registres ; les publications et fichiers sources n'ont pas été réouverts dans cette passe.
- La revue porte sur des propriétés de premier niveau et leur cohérence apparente ; elle ne vérifie pas les chiffres ou les méthodes des sources originales.
- L'échantillon est ciblé sur la chaîne éducation-compétences-emploi-salaires et n'est pas représentatif des 379 fiches.
- Aucune donnée, aucun statut, aucun claim et aucune relation du graphe n'a été modifié.

## 7. Suite proposée

1. Revue humaine de cette note et de la matrice #165.
2. Contrôle des sources originales PIAAC et InserJeunes, avec extraction contrôlée seulement après vérification des fichiers, millésimes, licences, unités et dénominateurs.
3. Demande/collecte de la documentation technique Céreq.
4. Sélection d'un claim par type (descriptif, causal, normatif) pour éprouver les exigences de vérification sans imposer un modèle uniforme.
5. Conception éventuelle d'un validateur de profil séparé des schémas canoniques.

**Décision :** aucun changement de schéma ni migration de masse n'est justifié par cet échantillon statique seul.
