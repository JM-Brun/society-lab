# Évaluation des pilotes de traçabilité — 18 novembre 2026

**Statut :** audit documentaire sur les fichiers présents dans `main`. Les localisateurs des documents originaux n'ont pas tous été revérifiés ; ce document ne certifie donc pas les extractions historiques.

## 1. Résultat de l'audit des contrats existants

L'examen des schémas `source`, `study`, `dataset` et `claim`, du protocole d'ingestion et de fiches réelles confirme que Society Lab dispose déjà d'une base substantielle :

- `source.schema.json` distingue titre original, auteurs, organisme, date de publication, type, langue, périmètres, méthode, limites, financement/conflits, licence et statut d'accès.
- `study.schema.json` prévoit question de recherche, méthode, unité/population, périmètres, résultats, limites, financement/conflits et statut de revue.
- `dataset.schema.json` prévoit producteur, sources, unité d'observation, variables, couverture géographique et temporelle, licence, accès, date de récupération, version/millésime, empreinte et transformations.
- `claim.schema.json` prévoit déjà `source_verifications`, un localisateur, un statut de vérification et une extraction typée avec méthode, valeur, unité, dénominateur, population, période, géographie, définition, transformation, date et auteur de l'extraction.
- `ingestion-protocol.md` prescrit déjà une localisation précise et une vérification sur l'original.

**Conclusion :** il serait prématuré de créer un schéma d'extraction concurrent. Le premier chantier est de tester l'application du contrat existant, de préciser ses règles d'usage et de vérifier les références entre objets.

### 1.1 Écarts observés

| Zone | Constat dans les fichiers examinés | Risque / action |
|---|---|---|
| Source | Le schéma ne prévoit pas explicitement de date de consultation, de version consultée ni de provenance champ par champ des métadonnées. | Distinguer métadonnée déclarée par l'éditeur, vérifiée, inférée et inconnue ; ne pas rendre ces champs obligatoires sans stratégie de migration. |
| Dataset | Le schéma prévoit `retrieved_at`, `version_or_vintage`, `file_hash` et `transformation_notes`, mais ces champs restent facultatifs. | Définir quand ils sont requis selon le type de dataset et la disponibilité réelle des artefacts. |
| Claim | Le schéma permet une extraction détaillée, mais les deux claims qualitatifs pilotes consultés ne renseignent pas `source_verifications`. | Une référence à une source ne suffit pas à établir qu'un passage a été vérifié. |
| Extraction | Le localisateur est une chaîne libre et ne distingue pas formellement page imprimée, page PDF, tableau, cellule, variable ou fragment web. | Ajouter une convention documentaire et des exemples avant de changer le schéma. |
| Historique | La révision Git conserve les modifications, mais l'événement de consultation ou de vérification n'est pas toujours un objet lisible séparément. | Tester le besoin d'un journal d'inspection après les pilotes, sans créer de registre prématurément. |
| Lineage | Les références source/étude/dataset/claim existent, mais elles ne donnent pas systématiquement le chemin jusqu'à un passage ou une donnée précise. | Construire la matrice de traçabilité sur des cas réels et contrôler les liens orphelins. |

## 2. Pilote qualitatif : comparaison Wallonie–Flandre

**Dossier :** `dossiers/cordon-sanitaire-belgique-efficacite.md`  
**Claim :** `CLAIM-BELGIUM-WALLONIA-FLANDERS-CORDON-2021`  
**Source référencée :** `SOURCE-BELGIUM-CORDON-WALLONIA-FLANDERS-2021`  
**Question :** dans quelle mesure les environnements politiques et médiatiques différenciés contribuent-ils aux trajectoires divergentes de la droite radicale en Wallonie et en Flandre ?

### État observé

La claim est explicitement interprétative et `under_review`. Elle mentionne une étude qualitative et ses limites, dont l'impossibilité d'isoler l'effet causal propre du cordon. Une première série de `source_verifications` a été ajoutée après consultation de la version de référence : méthode (p. 599), interprétation comparative (pp. 599–600 et 607–614) et explications concurrentes (pp. 601–606). Ces localisateurs vérifient l'argument publié par l'autrice ; ils ne constituent pas une vérification indépendante des entretiens, dont les matériaux ne sont pas publiquement reproduits dans l'article.

Le dossier rapporte que l'étude de De Jonge (2021) mobilise une comparaison qualitative, des sources historiques et secondaires et 18 entretiens semi-directifs. Le dossier distingue aussi les facteurs concurrents (histoire, offre partisane, réseaux militants, clivages sociaux). Ces éléments sont un bon test de séparation entre :
- ce que l'autrice rapporte ;
- les observations ou déclarations des personnes interrogées ;
- l'interprétation comparative de l'autrice ;
- la synthèse et l'interprétation propres à Society Lab.

### Contrat d'extraction à appliquer

Pour chaque proposition structurante, consigner séparément :
1. le localisateur vérifiable dans l'article (page et section) ;
2. le type d'élément : méthode, résultat qualitatif, citation courte, interprétation de l'autrice ou limite ;
3. l'attribution de la voix (autrice, personne interrogée, source secondaire, synthèse Society Lab) ;
4. le résumé fidèle, sans le présenter comme une citation ;
5. le périmètre régional, temporel et institutionnel ;
6. le statut de vérification sur l'article original ;
7. les explications alternatives et limites de transférabilité.

**Critère de réussite :** un lecteur peut remonter d'une phrase de synthèse à la proposition de la claim, puis à la page/section de l'article, en distinguant résultat rapporté et interprétation éditoriale.

**Limite actuelle :** les passages de l'article sont maintenant localisés et contrôlés, mais les entretiens sous-jacents ne sont pas accessibles pour une vérification indépendante. Le statut `under_review` est maintenu ; ne pas le promouvoir à `supported` sur la seule base de cette étude qualitative.

## 3. Pilote quantitatif : décomposition historique du SMIC, 1970–1993

**Source :** `SOURCE-SENAT-1994-SMIC-DECOMPOSITION`  
**Dataset :** `DATASET-SMIC-REVALUATIONS-1970-1993`  
**Fichier :** `data/smic-revaluations-1970-1993.csv`  
**Unité déclarée :** épisode annuel de revalorisation ; glissement à date d'effet, principalement en juillet.  
**Variables :** taux horaire en francs courants, variation observée, composante prix, moitié du TSH réel, obligation légale et coup de pouce discrétionnaire.

### Atouts pour le test

Le CSV conserve une référence source et une URL à chaque ligne, une méthode de transcription, un niveau de confiance et des notes. Le registre dataset décrit l'unité d'observation, les variables, la période, les transformations et les limites. C'est un cas pertinent pour vérifier les valeurs, les unités, les périodes, les dénominateurs et la distinction entre résultat rapporté et calcul dérivé.

### Vérification documentaire de juillet 1978 — anomalie résolue

La vérification visuelle du PDF original du Sénat a résolu l'écart apparent :
- le tableau 2, page imprimée 157 (page PDF 157), indique 10,85 F au 1er juillet 1978 ;
- le tableau 3, page imprimée 166 (page PDF 158), indique également 10,85 F pour juillet 1978 ;
- la lecture textuelle/OCR du tableau 3 pouvait faire lire 10,65 F, mais l'image de la page montre 10,85 F.

Il ne s'agissait donc pas d'une divergence entre les deux tableaux, mais d'une erreur de lecture OCR. La valeur du CSV (10,85 F) était correcte ; sa note a été corrigée pour expliciter le contrôle et conserver la trace de l'erreur de transcription. Le registre dataset a été rectifié en conséquence. Les deux tableaux concordent sur ce point. Cette vérification porte sur le montant horaire, pas sur l'ensemble des composantes de la décomposition ni sur la réconciliation des écarts avec d'autres publications.

Un contrôle complémentaire a depuis été réalisé sur les 24 lignes du CSV. Il a révélé que les libellés de la colonne `period` étaient décalés d'un an par rapport aux dates d'observation : la première ligne est désormais `1969-1970` (observation du 1er juillet 1970) et la dernière `1992-1993` (observation du 1er juillet 1993). Chaque ligne possède maintenant un localisateur vers sa ligne du tableau 3 (p. imprimée 166 / page PDF 158). Le validateur contrôle la cohérence entre période et date ainsi que la présence du localisateur.

L'écart arithmétique de 1970 reste ouvert : 11,1 % de variation observée contre environ 10,81 % issus d'une combinaison multiplicative exploratoire des composantes publiées (8,0 % et 2,6 %). Les valeurs sont conservées et cet écart doit être expliqué à partir des revalorisations détaillées du tableau 2. Voir `docs/smic-1970-1993-arithmetic-audit-2026-11.md`.

### Contrat d'extraction à appliquer

Pour chaque ligne, au minimum :
1. référence de la source et version consultée ;
2. localisateur exact (page imprimée, page PDF, numéro et intitulé du tableau, ligne/période) ;
3. transcription du taux et des composantes telles que publiées ;
4. unité et convention temporelle (glissement à date d'effet, non moyenne annuelle) ;
5. nature de la valeur : rapportée ou recalculée ;
6. règle de calcul si recalcul ;
7. note de divergence, source de contrôle et décision de réconciliation ;
8. statut de vérification et date de revue.

**Critère de réussite :** recalculer les contrôles arithmétiques possibles sans écraser les chiffres publiés, et expliquer chaque écart d'arrondi ou de convention. Les taux nominaux ne doivent pas être interprétés comme des variations de pouvoir d'achat ni comme des effets sur l'emploi.

## 4. Ce que ces pilotes enseignent sur le modèle de données

Les deux cas utilisent le même chemin général, mais ne doivent pas être forcés dans une fiche d'extraction identique :

- Le pilote qualitatif a besoin de localisateurs textuels, d'attribution de voix, de contexte, de méthode d'enquête et de distinction entre observation et interprétation.
- Le pilote quantitatif a besoin de localisateurs tabulaires, de valeurs, unités, période, population/unité, définitions, transformations et contrôles de cohérence.
- Les deux ont besoin d'une provenance de la version consultée, d'un statut de vérification, d'une limite explicite et d'un lien vers l'objet canonique qui réutilise l'extraction.

Le schéma de claim actuel couvre déjà une partie importante des besoins quantitatifs, mais il ne représente pas à lui seul une collection d'extractions réutilisables par plusieurs claims. Il faudra décider, après les pilotes, si ce besoin justifie un objet Extraction autonome ou si une extension minimale des vérifications de claims suffit.

## 5. Plan d'exécution révisé

1. **Anomalie 1978 résolue :** les tableaux 2 et 3 donnent tous deux 10,85 F ; conserver le localisateur visuel et la trace de l'erreur OCR. La confrontation INSEE reste utile comme contrôle externe, mais n'est plus nécessaire pour arbitrer entre ces deux tableaux.
2. **Pilote qualitatif partiellement complété :** localisateurs et premières extractions contrôlés dans l'article de De Jonge ; reste à vérifier la granularité des passages de la section médias, l'appendice d'entretiens et l'attribution précise des citations/voix avant d'élargir la claim.
3. **Renseigner les vérifications existantes** dans les claims pilotes uniquement après contrôle des documents originaux.
4. **Évaluer les champs de provenance source** et les conditions d'obligation selon les types de sources.
5. **Tester les validateurs** sur des exemples positifs et négatifs : localisateur absent, valeur sans unité, période incohérente, extraction IA non vérifiée, source inconnue.
6. **Décider ensuite** si des événements d'inspection et des objets Extraction autonomes sont nécessaires.
7. Documenter les résultats, les limites et les migrations dans l'issue #114 avant toute généralisation.

## 6. Règle de non-régression

Aucun pilote ne doit :
- modifier silencieusement les données sources ou les valeurs transcrites ;
- transformer un statut de vérification en appréciation globale de qualité ;
- faire disparaître une contradiction historique ou une valeur alternative ;
- confondre date de publication, date de consultation, date d'observation et date d'effet ;
- convertir une extraction ou une proximité de graphe en preuve causale ;
- imposer une migration de masse aux claims et datasets historiques.

La réussite du pilote est la traçabilité intelligible et vérifiable, pas le nombre de champs remplis.
