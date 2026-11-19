# Revue des sources primaires — PIAAC, InserJeunes et Céreq

**Date de revue :** 19 novembre 2026  
**Périmètre :** réouverture des pages institutionnelles référencées par les fiches Source et Dataset. Cette note documente ce que les sources publiques permettent effectivement d'établir. Elle ne constitue ni une extraction de microdonnées, ni une validation de résultats chiffrés enregistrés dans les claims.

## 1. PIAAC — documentation des données et de la méthode

**Fiches concernées**
- `SOURCE-OECD-PIAAC-DATA-METHODOLOGY-2023`
- `STUDY-PIAAC-2023-FRANCE-COMPETENCES`
- `DATASET-PIAAC-2023-FRANCE`

**Source primaire rouverte :** [OCDE — Données et méthodologie du PIAAC](https://www.oecd.org/fr/about/programmes/piaac/piaac-data.html)

### Éléments directement confirmés
- La page OCDE met à disposition les bases du premier et du deuxième cycle, les fichiers à usage public, les livres de codes, les questionnaires et les éléments nécessaires au traitement des données.
- Elle référence les outils d'analyse, les cadres d'évaluation du deuxième cycle, le manuel d'analyse des données 2023 et le rapport technique du deuxième cycle.
- Le rapport technique documente notamment la conception des instruments, les opérations de terrain, le contrôle qualité, l'échantillonnage, la pondération, l'analyse et les produits de données.

### Conséquences pour l'exploitation
- La fiche Dataset décrit correctement une ressource de microdonnées et de documentation, mais « access_status: open » ne dispense pas de vérifier les conditions applicables à chaque fichier et à chaque usage.
- Avant toute extraction, identifier précisément le fichier français, son format, son millésime, son dictionnaire, ses variables de pondération et les instructions de calcul des estimations.
- Les résultats descriptifs doivent suivre les procédures d'analyse complexes indiquées dans la documentation. La page générale consultée ne suffit pas, à elle seule, à valider une procédure statistique particulière ni un résultat chiffré.
- L'enquête transversale ne permet pas, à elle seule, d'identifier l'effet causal d'une formation sur les compétences, l'emploi ou le salaire.

### À obtenir avant extraction
1. Le fichier français exact et sa documentation associée.
2. Le manuel d'analyse 2023 et le rapport technique du deuxième cycle.
3. Les règles de pondération, de variance et de traitement des valeurs plausibles applicables à l'estimation visée.
4. Les conditions de téléchargement, de réutilisation et de redistribution du fichier choisi.

**Décision :** source documentaire confirmée ; extraction non autorisée à ce stade ; licence et procédure statistique à vérifier au niveau du fichier et de l'analyse.

## 2. InserJeunes — définitions, dénominateurs et limites de diffusion

**Fiches concernées**
- `SOURCE-DEPP-INSERJEUNES-2026`
- `STUDY-INSERJEUNES-INSERTION-2023`
- `DATASET-INSERJEUNES-2023`

**Sources primaires rouvertes :**
- [DEPP — InserJeunes : l'insertion des jeunes après une formation en voie professionnelle](https://www.education.gouv.fr/depp/inserjeunes-l-insertion-des-jeunes-apres-une-formation-en-voie-professionnelle-307956)
- [DEPP — Les indicateurs du dispositif InserJeunes : définitions, méthodes de calcul et règles de diffusion (PDF, mise à jour du 17 décembre 2024)](https://www.education.gouv.fr/sites/default/files/document/%C3%89ducation_nationale_DEPP_Pr%C3%A9sentation_synth%C3%A9tique_des_indicateurs_InserJeunes-404799.pdf)
- [DEPP — Méthode de calcul des rémunérations InserJeunes (PDF)](https://www.education.gouv.fr/sites/default/files/document/Education_nationale_DEPP_Note_m%C3%A9thodologique_r%C3%A9mun%C3%A9rations_InserJeunes-404802.pdf)

### Éléments directement confirmés
- Le dispositif apparie les fichiers de suivi des scolarités aux déclarations sociales nominatives (DSN) pour distinguer poursuite d'études, sortie de formation et emploi salarié observé.
- Les indicateurs portent notamment sur la poursuite d'études, l'interruption de formation, l'emploi à 6, 12, 18 et 24 mois et, pour certains sortants en emploi salarié, la rémunération à 12 mois.
- La page institutionnelle indique que les données des sortants 2023 ont été mises à jour le 25 juin 2026, avec des observations d'insertion à 18-24 mois.
- La documentation méthodologique détaillée consultée est datée du 17 décembre 2024 : elle doit donc être considérée comme la documentation des définitions et méthodes décrites à cette date, et non comme une garantie que chaque règle n'a pas évolué depuis.

### Dénominateurs à ne pas confondre
- **Taux de poursuite d'études :** jeunes inscrits l'année suivante / jeunes en année terminale de formation.
- **Taux d'emploi des sortants :** sortants ayant un contrat salarié pendant la semaine de référence / sortants ne poursuivant pas leurs études.
- **Part en emploi dans le devenir des jeunes :** jeunes en emploi à 6 mois / ensemble des jeunes en année terminale, y compris ceux qui poursuivent leurs études.

Ces indicateurs n'ont donc ni le même numérateur ni le même dénominateur. Ils ne doivent pas être comparés ou fusionnés sans expliciter leur définition.

### Fenêtres temporelles et champ
- Les observations d'emploi à 6 et 18 mois utilisent conventionnellement la deuxième semaine de janvier ; celles à 12 et 24 mois utilisent la première semaine de juillet.
- La DSN mesure l'emploi salarié couvert en France ; l'emploi non salarié et l'emploi à l'étranger ne sont pas observés par cet indicateur.
- Le document méthodologique de 2024 signale que les données infra-nationales et par établissement sont cumulées sur deux années scolaires successives afin de limiter les fluctuations liées aux faibles effectifs.
- Il précise également un seuil de diffusion d'au moins 20 jeunes au dénominateur pour les indicateurs concernés. Des règles complémentaires de secret statistique s'appliquent à certains indicateurs de rémunération.
- Les rémunérations publiées concernent les sortants en emploi salarié à 12 mois ; elles sont calculées en salaire net mensuel en équivalent temps plein (EQTP), primes incluses selon la définition du document. Elles ne décrivent donc pas le salaire de l'ensemble des sortants.

### Conséquences pour le registre et l'extraction
1. Remplacer l'expression générique « unité exacte à vérifier pour chaque fichier » par une description différenciée des unités statistiques et des dénominateurs propres à chaque indicateur, lorsque les fichiers correspondants auront été identifiés.
2. Pour chaque fichier extrait, enregistrer : millésime, population couverte, voie de formation, niveau géographique, unité, numérateur, dénominateur, fenêtre d'observation, cumul éventuel de millésimes et règles de suppression.
3. Distinguer taux d'emploi des sortants, part en emploi parmi les jeunes en année terminale et indicateurs de rémunération conditionnels à l'emploi salarié.
4. Ne pas interpréter les différences brutes entre établissements comme des effets causaux de la formation ou de l'établissement. La valeur ajoutée publiée repose sur une modélisation et un ajustement par caractéristiques observées ; elle n'est pas une expérimentation.
5. Vérifier la version courante des documents méthodologiques avant de coder les règles de diffusion dans un validateur.

### Point de métadonnées à corriger ultérieurement
La fiche Source porte `publication_date: 2026-06-25`, alors que la page DEPP indique une publication initiale le 18 février 2026 et une mise à jour des données le 25 juin 2026. Il faut distinguer date de publication et date de mise à jour, plutôt que traiter la seconde comme date de publication sans qualification.

**Décision :** documentation méthodologique publique retrouvée ; extraction contrôlée possible après identification du fichier et de sa licence ; aucun chiffre de claim n'est validé par cette seule revue.

## 3. Céreq — appariement Génération 2021 / Base Tous salariés

**Fiches concernées**
- `SOURCE-CEREQ-GENERATION-2021-BTS-MATCHING-2026`
- `STUDY-CEREQ-GENERATION-2021-BTS-MATCHING`
- `DATASET-CEREQ-GENERATION-2021-BTS-MATCHED`

**Source primaire rouverte :** [Céreq — Détails du projet, fiche 1163](https://projets.cereq.fr/fiche-1163)

### Éléments directement confirmés
- Le projet décrit l'évolution des enquêtes Génération vers une articulation entre données d'enquête et données administratives.
- Pour 2025-2026, la page indique la réalisation des extractions DEPP et SIES, un travail d'expertise et de documentation de l'appariement, ainsi que la rédaction d'une convention et d'un plan de gestion des données.
- Elle indique également que le travail de réalisation et d'expertise de l'appariement de Génération 2021 avec la Base Tous salariés a été réalisé.
- La page ne publie pas les taux de rapprochement, le dictionnaire final, les résultats analytiques ni les règles détaillées d'accès aux données appariées.

### Conséquences
- La fiche Dataset doit rester en `access_status: request_required` tant qu'une modalité d'accès effective n'est pas établie.
- La page publique confirme l'existence et la réalisation de travaux d'appariement ; elle ne confirme pas que le fichier apparié est librement téléchargeable ou exploitable.
- Aucun résultat sur la relation formation-salaire ne peut être inscrit à partir de la seule page de projet.
- Les biais de sélection, les non-réponses, la couverture de la Base Tous salariés et les personnes hors emploi salarié doivent être documentés dans toute analyse ultérieure.

### Informations à demander au Céreq / aux producteurs
1. Convention d'appariement et plan de gestion des données, dans la mesure où leur diffusion est possible.
2. Population éligible, critères de rapprochement et taux de matching par sous-population.
3. Dictionnaire final, périodes couvertes, variables de rémunération et unités statistiques.
4. Traitement des non-appariés, des multi-appariements et des situations hors emploi salarié.
5. Conditions d'accès, environnement sécurisé, licence éventuelle et règles de diffusion des résultats.

**Décision :** existence de l'appariement confirmée ; accès et contenu du dataset non confirmés ; aucune extraction ni conclusion empirique.

## 4. Décisions transversales

| Sujet | État probatoire après réouverture | Prochaine action |
|---|---|---|
| PIAAC | Documentation OCDE et ressources techniques confirmées ; procédure précise et licence du fichier à vérifier | Identifier fichier français, manuel, pondérations et règles d'analyse |
| InserJeunes | Définitions, fenêtres, dénominateurs et limites documentés | Identifier les fichiers 2023 exacts et leurs métadonnées/licences |
| Céreq | Réalisation de l'appariement confirmée par la page projet | Obtenir documentation technique et conditions d'accès |

### Garde-fous
- Cette revue de pages institutionnelles ne valide aucun chiffre de claim.
- Aucun dataset n'a été téléchargé ou analysé dans cette passe.
- Aucune licence n'a été supposée.
- Aucun statut de claim, de dataset ou de source n'a été modifié.
- Aucun lien causal n'est ajouté au graphe.
- Les documents méthodologiques doivent être versionnés : une page actualisée en 2026 et un PDF daté de 2024 ne sont pas nécessairement synchrones.

## 5. Références primaires

- OCDE, [Données et méthodologie du PIAAC](https://www.oecd.org/fr/about/programmes/piaac/piaac-data.html), page consultée le 19 novembre 2026.
- DEPP, [InserJeunes : l'insertion des jeunes après une formation en voie professionnelle](https://www.education.gouv.fr/depp/inserjeunes-l-insertion-des-jeunes-apres-une-formation-en-voie-professionnelle-307956), page publiée le 18 février 2026 et mise à jour des données le 25 juin 2026.
- DEPP, [Les indicateurs du dispositif InserJeunes : définitions, méthodes de calcul et règles de diffusion](https://www.education.gouv.fr/sites/default/files/document/%C3%89ducation_nationale_DEPP_Pr%C3%A9sentation_synth%C3%A9tique_des_indicateurs_InserJeunes-404799.pdf), document mis à jour le 17 décembre 2024.
- DEPP, [Les indicateurs de rémunération InserJeunes](https://www.education.gouv.fr/sites/default/files/document/Education_nationale_DEPP_Note_m%C3%A9thodologique_r%C3%A9mun%C3%A9rations_InserJeunes-404802.pdf).
- Céreq, [Détails du projet — fiche 1163](https://projets.cereq.fr/fiche-1163), page consultée le 19 novembre 2026.
