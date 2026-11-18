# Audit initial du pipeline d'ingestion et de production des connaissances

**Date :** 18 novembre 2026  
**Périmètre :** dépôt `JM-Brun/society-lab`, branche `main`  
**Commit de référence :** `0363723e9f32217b4eccffe4276db22f83503500`  
**Issue de suivi :** [#114 — Auditer et fiabiliser le pipeline complet](https://github.com/JM-Brun/society-lab/issues/114)

> Ce document est une photographie initiale fondée sur l'inspection des documents d'architecture, des schémas, du validateur principal, des registres et de la CI. Il ne constitue pas encore un audit exhaustif de chaque fiche ni un benchmark de performance. Les constats sont séparés des points restant à tester.

## 1. Conclusion exécutive

Society Lab dispose déjà d'une base sérieuse : source de vérité Git, registres canoniques, schémas JSON, taxonomies contrôlées, graphe typé, protocole d'ingestion, principes de provenance et CI. L'architecture est cohérente avec un corpus documentaire versionné et ne justifie pas, à ce stade, l'introduction d'une base graphe externe.

En revanche, la documentation actuelle décrit mieux les principes que l'exécution opérationnelle. Les contrats d'extraction, la traçabilité fine entre passage source et connaissance, les contrôles sémantiques du graphe, la gestion des versions et les mesures de scalabilité doivent être renforcés et démontrés sur des cas réels.

**Verdict : architecture de départ pertinente ; chaîne de traitement partiellement formalisée et contrôlée ; qualité scientifique non certifiée par la CI.** Ne pas présenter l'ensemble du processus comme entièrement automatisé ou validé.

## 2. Éléments effectivement présents

### 2.1 Architecture et gouvernance documentaire

Documents examinés :
- `docs/architecture.md`
- `docs/ingestion-protocol.md`
- `docs/metadata-and-naming.md`
- `docs/source-policy.md`
- `docs/licensing.md`
- `docs/uncertainty-and-revisions.md`
- `METHODOLOGY.md`
- `knowledge/GRAPH.md`

Points solides :
- Le dépôt Git est désigné comme source de vérité ; les vues éditoriales sont dérivées.
- Les couches Evidence, Knowledge & Research, Graph et Publication sont distinguées.
- Le protocole couvre découverte, déduplication, identification, droits, qualification, extraction, mise en relation, revue, publication et maintenance.
- Les extractions IA sont explicitement des propositions à vérifier dans les sources originales.
- Les limites, désaccords, résultats contradictoires et révisions sont reconnus comme éléments de premier rang.
- Les droits des tiers ne sont pas assimilés à la licence globale du dépôt.

Limite : les étapes ne définissent pas encore systématiquement un contrat d'exécution avec entrées, sorties, états, contrôles, erreurs, reprise et critères de passage.

### 2.2 Schémas et registres

Schémas présents pour :
- sources, études, datasets ;
- claims, hypothèses, prévisions ;
- concepts, mécanismes, territoires ;
- dossiers.

Le validateur principal référence les registres de ces objets et applique les schémas JSON correspondants. Il vérifie aussi les identifiants, les domaines et tags, plusieurs références typées, ainsi que l'existence et la compatibilité des extrémités des relations du graphe.

Les schémas posent des bases utiles :
- source : titre, type, langue, date, URL/DOI, périmètres, méthode, limites, financement/conflits, licence et accès ;
- étude : type d'étude, sources, domaines, méthode, population/unité, résultats et limites ;
- dataset : fournisseur, sources, périmètres, unité d'observation, variables, licence, date de récupération, version, empreinte et transformations ;
- claim : type et statut, périmètre, preuves favorables et contraires, vérifications par source, provenance, révisions ;
- concept : identifiant, définition, domaines, tags et alias ;
- mécanisme : description, direction, étapes, conditions, acteurs, indicateurs, horizon, études favorables/défavorables, claims et limites.

Limites à examiner :
- Les métadonnées de localisation des éléments extraits et la chaîne de transformation ne sont pas encore un contrat partagé de bout en bout entre source, étude, dataset et claim.
- Les informations de version et d'identification persistante ne sont pas uniformément requises, ce qui est normal pour certains types de sources mais nécessite des règles conditionnelles explicites.
- Les objets et fichiers hors des registres actuellement énumérés doivent être inventoriés et leurs règles de validation explicitées.

### 2.3 Graphe et ontologie

`knowledge/GRAPH.md` distingue correctement relations documentaires et relations épistémiques, et exige une justification pour les relations probantes. `knowledge/RELATION_TYPES.yml` définit des relations orientées avec types d'objets autorisés et inverses.

Le validateur vérifie :
- l'existence des nœuds référencés ;
- le type autorisé des extrémités ;
- l'existence du type de relation ;
- l'unicité des identifiants d'arêtes.

Il ne démontre pas, à lui seul, que chaque justification est précise, localisable, fraîche ou scientifiquement suffisante. Les contrôles automatiques de cohérence entre relations embarquées dans les fiches et arêtes du graphe, de synonymie/doublons sémantiques et de qualité des mécanismes restent à examiner.

Le travail transversal de l'issue #112 doit rester articulé à cet audit : ne pas créer de registre ni de graphe parallèle. La distinction entre concept, mécanisme théorique, mécanisme observé, représentation pédagogique et relation causale doit être préservée.

### 2.4 CI et tests

Le workflow `.github/workflows/validate.yml` :
1. installe Python 3.12, PyYAML et jsonschema ;
2. exécute `scripts/validate/validate_registry.py` ;
3. vérifie la correspondance dossiers/synthèses ;
4. signale la fraîcheur des synthèses ;
5. exécute les tests unitaires ;
6. vérifie que les fichiers de schéma sont du JSON valide.

Sur le commit de référence, le workflow **Validate knowledge base** (run 796) et le scan de secrets (run 69) ont réussi. La PR #113 a été intégrée dans `main` avant cette photographie.

Cette réussite atteste uniquement du passage des contrôles implémentés. La validation syntaxique des schémas JSON n'est pas une validation de leur adéquation métier ; les tests unitaires existants ne constituent pas un test de charge du corpus complet.

## 3. Lacunes et risques à instruire

| Domaine | Constat initial | Vérification ou amélioration attendue |
|---|---|---|
| Pipeline | Étapes documentées, contrats opérationnels incomplets | Entrées/sorties, statuts, erreurs, reprise et critères de sortie |
| Lots | Manifeste minimal décrit | Identifiants de lot, critères, décisions, rejets, doublons et journal |
| Provenance | Principes présents, champs dispersés selon les objets | Traçabilité source → localisateur → extraction → objet → publication |
| Extraction | Fiche minimale textuelle | Contrats spécifiques aux textes, tableaux, graphiques et données |
| Vérification | Statuts disponibles pour les claims | Contrôler la cohérence entre statut, localisateur et preuve réellement vérifiée |
| Métadonnées | Schémas utiles mais hétérogènes | Règles conditionnelles, versions, dates, langue, licence, accès et transformations |
| Déduplication | Règles bibliographiques décrites | Cas DOI/URL/versions/traductions/rapports issus d'un même programme |
| Concepts | Schéma minimal utile | Alias, définitions concurrentes, périmètre et détection des doublons |
| Mécanismes | Schéma descriptif présent | Statut épistémique, portée, conditions et preuves contradictoires |
| Relations | Types et extrémités contrôlés | Justification localisable, statut, temporalité, cohérence fiche/graphe |
| Maintenance | Errata et rétractations mentionnés | Propagation contrôlée des changements vers claims, graphes et synthèses |
| Scalabilité | Validation globale en CI | Mesures de temps/mémoire et essais sur corpus ×10/×100 |
| Ergonomie | Plusieurs guides séparés | Parcours opératoire unique avec liens, exemples et décisions de renvoi |

## 4. Points précis à vérifier dans le code

Le validateur `scripts/validate/validate_registry.py` est le centre des contrôles actuels. L'audit détaillé doit notamment vérifier :
- la couverture de tous les types d'objets effectivement présents dans le dépôt ;
- les champs de références imbriqués et les références portées par le graphe ;
- la cohérence des inverses déclarés dans `RELATION_TYPES.yml` ;
- les relations dupliquées, les cycles interdits ou suspects et les arêtes sans justification exploitable ;
- les références territoriales, organisations, méthodes et analyses ;
- la cohérence des métadonnées entre fiches sources, études, datasets et claims ;
- les fichiers qui ne sont pas enregistrés dans les registres canoniques ;
- la validation des dates et formats, notamment les formats de langue et les URI ;
- la qualité des messages d'erreur et la durée d'exécution à différentes tailles de corpus.

Ne pas ajouter de contraintes bloquantes avant d'avoir mesuré les données existantes et prévu une migration explicite.

## 5. Architecture cible — principes à conserver

1. Un seul registre canonique par type d'objet ; les vues et exports sont dérivés.
2. Pas d'automatisation qui transforme une extraction en fait vérifié sans contrôle humain.
3. La provenance est attachée à l'élément de connaissance et pas seulement à la fiche source générale.
4. Les objets source, étude, dataset, résultat, claim, concept et mécanisme restent distincts.
5. Les relations épistémiques ont une justification précise et une portée ; les liens d'organisation ne sont pas des preuves.
6. Les identifiants restent stables ; les corrections et versions sont traçables.
7. Les contrôles techniques détectent des incohérences ; ils ne délivrent pas de certification scientifique.
8. Pas de migration vers une base externe tant que les besoins de requête, de volume ou de collaboration ne le justifient pas.

## 6. Cas pilotes recommandés

- **Parcoursup (#2)** : source administrative, dictionnaire de données, extraction reproductible, unité d'observation, dénominateurs et résultats descriptifs.
- **ADEME Saison 2 (#110)** : API/catalogue, versions, acquisition de données brutes, empreintes, harmonisation et comparabilité.
- **SMIC** : séries historiques, révisions de sources, versions, unités monétaires, calculs reproductibles et controverses.
- **TIG** : sources institutionnelles, cohortes, indicateurs de délai, périmètres et dénominateurs.
- **Relations inter-domaines (#112)** : concepts/mécanismes, direction, portée, temporalité et garde-fous causaux.

Ces cas servent à tester un même pipeline sur des formes de preuve différentes, sans créer de parcours éditoriaux concurrents.

## 7. Séquence de travail proposée

1. Inventorier les objets, registres, schémas, fichiers et champs réellement utilisés.
2. Construire une matrice de traçabilité sur quelques objets complets.
3. Définir le contrat d'extraction et les métadonnées manquantes à partir des cas pilotes.
4. Renforcer les validateurs par petits changements rétrocompatibles et tests négatifs.
5. Mesurer la performance avant toute optimisation ou changement de stockage.
6. Documenter la maintenance et la propagation des révisions.
7. Migrer les fiches existantes par lots contrôlés, avec rapport de couverture et sans perte de contenu.

## 8. Statut

**Audit initial réalisé ; audit opérationnel et exhaustif à poursuivre.**

Aucune conclusion n'est tirée ici sur la qualité de chaque source ou claim individuel. Les écarts à confirmer, les tests à écrire et les migrations sont suivis dans l'issue [#114](https://github.com/JM-Brun/society-lab/issues/114).

## 9. Audit technique complémentaire — inventaire et contrôles croisés

Cette section complète la photographie initiale après inspection du contenu réel des registres et du code du validateur.

### 9.1 Volume et répartition observés

Comptage des entrées structurées présentes dans les registres au moment de l'audit (18 novembre 2026) :

| Registre | Entrées |
|---|---:|
| Sources | 214 |
| Études | 59 |
| Jeux de données | 14 |
| Claims | 83 |
| Hypothèses | 22 |
| Dossiers | 25 |
| Concepts | 15 |
| Mécanismes | 0 |
| Prévisions | 0 |
| Relations du graphe avant nettoyage | 596 |

Tailles observées : registre des sources ~237 Ko, études ~97 Ko, claims ~117 Ko et graphe ~175 Ko. Ces volumes ne démontrent pas un problème de performance ; ils signalent en revanche que plusieurs registres contiennent déjà les fiches complètes et ne sont plus de simples index légers.

La documentation `sources/README.md` présente le registre comme un index léger et prévoit `records/` et `batches/` si le volume le justifie. Ces répertoires ne sont pas encore présents dans l'arborescence inspectée. Il faut décider explicitement à quel seuil découper les fiches individuelles et comment conserver un index canonique, sans lancer une migration massive uniquement sur la base de la taille actuelle.

Les schémas et registres des mécanismes et prévisions existent, mais leurs registres sont vides. Il s'agit donc de capacités prévues, pas encore de processus éprouvés sur des objets réels. Le chantier des mécanismes devra notamment produire au moins un exemple complet, sourcé et revu avant de considérer le contrat opérationnel.

### 9.2 Défauts de validation confirmés

L'inspection du code a confirmé deux angles morts précis :
- le validateur contrôlait les références de premier niveau, mais pas `concept_ids` dans les dossiers ;
- il ne vérifiait pas les `source_id` imbriqués dans `source_verifications` des claims.

Le schéma JSON autorisait donc ces références sans que le validateur vérifie l'existence de leurs cibles. Le validateur a été complété pour couvrir ces deux cas, et des tests unitaires négatifs et positifs ont été ajoutés dans `tests/test_validate_registry.py`.

Le contrôle du graphe vérifiait les types et les extrémités, mais n'imposait pas en code la justification non vide pourtant exigée par `knowledge/GRAPH.md`. Il vérifie maintenant cette exigence.

### 9.3 Doublons de relations observés et traités

L'inventaire des 596 arêtes a identifié sept triplets dupliqués (même type, même nœud source et même nœud cible), avec des identifiants différents et des justifications partiellement complémentaires. Il ne s'agissait pas de doublons stricts de texte : chaque paire apportait une précision utile, mais le modèle du graphe n'avait pas de règle explicite pour gérer plusieurs justifications d'une même relation.

Sur la branche de cette PR, les sept paires ont été consolidées en une seule arête chacune, en fusionnant leurs justifications sans supprimer les nuances documentaires. Le graphe passe ainsi de 596 à 589 arêtes. Le validateur signale désormais toute nouvelle répétition d'un même triplet afin d'éviter le retour de cette ambiguïté.

Cette règle suppose qu'une arête représente une relation sémantique unique entre deux objets. Si plusieurs éléments de preuve doivent être associés au même lien, ils doivent être regroupés dans la justification ou, à terme, portés par une structure de preuves dédiée — pas dupliqués sous plusieurs identifiants d'arête.

### 9.4 Écart entre architecture déclarée et objets opérationnels

L'architecture cite notamment les objets Institution/ORG, Method/METHOD et Analysis/ANALYSIS comme objets fondamentaux, et plusieurs types de relations autorisent ces catégories. En revanche, l'inventaire des registres et schémas actuellement chargés par le validateur ne comporte pas de registres canoniques complets pour ces trois types.

À ce stade, aucune migration ne doit être engagée sans cas d'usage réel. Il faut soit créer ces contrats lorsque le premier objet de ce type est nécessaire, soit préciser dans l'architecture qu'il s'agit de types futurs ou de références textuelles non autonomes. Ne pas laisser entendre qu'un type est déjà géré de bout en bout alors qu'il n'a ni registre ni schéma validé.

### 9.5 Limites qui restent ouvertes

- Le validateur ne mesure toujours pas la performance ; les tailles observées servent de référence initiale, pas de benchmark.
- Les métadonnées de localisation et d'extraction restent hétérogènes entre sources, études, datasets et claims.
- Le registre des lots d'ingestion n'est pas encore matérialisé par des manifestes réels dans l'arborescence inspectée.
- La détection de doublons bibliographiques et de concepts sémantiquement proches n'est pas automatisée.
- Les contrôles de cohérence entre les relations embarquées dans les fiches et le graphe ne sont pas complets.
- Les objets de mécanisme ne disposent pas encore d'un cas réel qui éprouve les statuts et les preuves contradictoires.
- Aucun test de charge ×10/×100 n'a été exécuté.

### 9.6 Modifications techniques incluses dans cette PR

- Ajout du contrôle des références `concept_ids` et des références imbriquées `source_verifications[*].source_id`.
- Exigence d'une justification non vide sur chaque arête.
- Détection des doublons sémantiques de triplets `(type, from, to)`.
- Consolidation des sept paires de relations repérées, avec conservation des précisions dans les justifications.
- Ajout de tests unitaires couvrant les références valides/invalides, les justifications absentes, les doublons et les extrémités incompatibles.

Les contrôles CI doivent être exécutés sur la tête finale de la PR avant de considérer ces changements comme validés.

## 10. Formalisation des lots d'ingestion

Le contrat des lots est maintenant matérialisé :
- schéma JSON dédié : `schemas/ingestion-batch.schema.json` ;
- modèle réutilisable : `templates/ingestion-batch.yml` ;
- règles de stockage et de conservation : `sources/batches/README.md` ;
- procédure opérationnelle : section « Contrat opérationnel des lots » de `docs/ingestion-protocol.md`.

Le validateur examine les manifestes YAML déposés dans `sources/batches/` lorsqu'ils existent. Il contrôle le schéma, l'unicité des identifiants de lots et de candidates, la résolution des sources sélectionnées, les cibles des doublons, les cycles de doublons, l'unicité d'une source sélectionnée dans un lot et l'absence de candidates reportées dans un lot clos.

Le modèle est testé contre son schéma. Des tests unitaires couvrent également les références de sources, les doublons et les états de clôture.

**Limite assumée :** aucun manifeste réel n'a été ajouté artificiellement, car l'historique des collectes antérieures n'est pas suffisamment consigné pour reconstruire leurs critères et décisions sans spéculation. Le contrat est prêt ; il doit maintenant être utilisé lors des prochaines ingestions et, si des traces fiables existent, appliqué rétrospectivement par lots documentés.

## 11. Couverture réelle des métadonnées

Un comptage des champs renseignés a été effectué sur les enregistrements JSON intégrés aux registres YAML. Il mesure la présence d'une valeur non vide, pas sa justesse ni sa pertinence. Un champ absent n'est pas automatiquement une erreur : certains champs sont conditionnels au type de source. En revanche, l'absence ne doit pas être confondue avec une vérification concluant « aucun », « non applicable » ou « information non publiée ».

### 11.1 Sources — 214 fiches

| Champ | Renseigné | Lecture |
|---|---:|---|
| URL | 214/214 | Couverture complète |
| Langue, domaines, tags | 214/214 | Couverture complète |
| Méthodologie, limites | 214/214 | Très bonne présence déclarative ; qualité à évaluer |
| Organisme | 212/214 | Quasi complet |
| Portée temporelle | 187/214 | 87 % |
| Portée géographique | 177/214 | 83 % |
| Date de publication | 150/214 | 70 % |
| Auteurs individuels | 46/214 | 21 % ; attendu variable selon la nature de la source |
| DOI | 5/214 | Non généralisable à toutes les sources |
| Licence | 1/214 | Lacune importante à instruire |
| Financement/conflits | 0/214 | Aucune valeur explicite dans le champ actuel |
| Statut d'accès | 214/214 | Présent partout, mais ne remplace pas l'évaluation des droits |

La couverture complète de `methodology` et `limitations` ne garantit pas leur qualité : il faut contrôler si les valeurs sont réellement spécifiques à chaque source ou si certaines formules génériques sont utilisées.

La présence d'un statut d'accès ne remplace pas une revue des droits. La politique demande de vérifier licences, conditions d'accès et restrictions avant archivage ou republication ; pourtant, le champ `license` est renseigné dans une seule fiche. Il faut distinguer « licence identifiée », « tous droits réservés », « domaine public », « accès restreint », « non applicable » et « non vérifié », sans inférer une licence depuis l'accessibilité d'une URL.

### 11.2 Études — 59 fiches

| Champ | Renseigné |
|---|---:|
| Sources, question, méthodes | 59/59 |
| Population/unité, portée géographique et temporelle | 59/59 |
| Résultats clés, limites, statut de revue | 59/59 |
| Jeux de données associés | 6/59 |
| Notes de revue | 32/59 |
| Financement/conflits | 0/59 |

Les champs structurants de description sont bien présents. La couverture de `dataset_ids` est nécessairement variable selon les études ; elle doit toutefois être contrôlée lorsque l'étude exploite des données identifiables. Les informations de financement/conflits sont absentes du champ dans les 59 fiches : il faut pouvoir consigner explicitement « non déclaré », « non applicable » ou « non examiné ».

### 11.3 Jeux de données — 14 fiches

| Champ | Renseigné |
|---|---:|
| Fournisseur, sources, périmètres, période, unité, variables | 14/14 |
| Statut d'accès, version/vintage, limites | 14/14 |
| URL | 13/14 |
| Licence | 12/14 |
| Notes de transformation | 7/14 |
| Date de récupération | 0/14 |
| Empreinte de fichier | 0/14 |

La date de récupération et l'empreinte ne sont pas nécessairement applicables à toutes les données (API vivante, données agrégées, source non téléchargeable). Il faut donc un contrat conditionnel : lorsqu'un fichier ou instantané est acquis et conservé, date, version et empreinte doivent permettre de retrouver exactement l'entrée analysée. Pour une API ou une donnée évolutive, documenter plutôt la requête, la date d'extraction, les paramètres et la réponse/version disponible. Les transformations doivent être décrites dès qu'une harmonisation ou un calcul modifie les données.

### 11.4 Claims — 83 fiches

| Champ | Renseigné |
|---|---:|
| Périmètre, domaines, sources, éléments favorables, limites | 83/83 |
| Études associées | 69/83 |
| Vérifications par source | 28/83 |
| Provenance explicite | 26/83 |
| Contre-preuves | 1/83 |
| Meilleur contre-argument | 15/83 |
| Hypothèses explicites | 5/83 |
| Historique de révision | 3/83 |
| Déclencheurs de révision | 6/83 |
| Objet `confidence` | 0/83 |

La présence de `supporting_evidence` dans chaque claim est un bon socle, mais elle ne suffit pas à prouver que l'élément a été localisé et vérifié dans la source. Les champs `source_verifications` et `provenance` sont renseignés dans environ un tiers des claims. C'est la priorité de migration la plus importante pour la traçabilité fine.

Le champ `counter_evidence` quasi absent ne signifie pas que toutes les affirmations ont été examinées et qu'aucune preuve contraire n'existe. Le schéma ne distingue pas encore clairement « aucune contre-preuve identifiée après revue » de « contre-preuves non recherchées ». Même distinction pour la provenance et l'historique : absence de champ ne vaut pas absence de transformation ou de révision.

L'objet `confidence` est défini mais n'est utilisé dans aucune fiche. Il ne faut pas le remplir mécaniquement : décider si le statut qualitatif actuel suffit ou si une probabilité calibrée apporte une information utile. Ne pas introduire de score artificiel.

### 11.5 Hypothèses, dossiers et concepts

- Hypothèses : les 22 fiches ont un mécanisme explicatif, des alternatives et une justification de confiance ; 19/22 référencent des études favorables et 1/22 des études contradictoires. La date de revue n'est renseignée que dans 3/22 fiches.
- Dossiers : les 25 fiches ont un résumé, une question, des périmètres et une date de revue. Les références vers claims, études, hypothèses et concepts sont variables selon le contenu et ne doivent pas être rendues obligatoires sans examiner le rôle du dossier.
- Concepts : les 15 fiches ont une définition et des alias ; 14/15 ont des tags. Le petit volume et la présence d'alias constituent une bonne base, mais il reste à examiner les synonymes entre concepts distincts.

### 11.6 Décisions à prendre avant toute migration

1. Introduire des états explicites pour les vérifications de droits, de financement/conflits et de contre-preuves : non examiné, examiné sans élément identifié, information non publiée, non applicable, information identifiée.
2. Ne pas remplacer les valeurs inconnues par « aucun » ou « non applicable » sans vérification.
3. Définir des champs conditionnels pour les jeux de données statiques, les API et les sources non téléchargeables.
4. Prioriser la migration des claims structurants : localisateur, statut de vérification et provenance de l'extraction.
5. Échantillonner les fiches pour contrôler la qualité sémantique des valeurs déjà présentes, notamment les méthodologies et limites génériques.
6. Publier un rapport de couverture automatique séparant champ absent, explicitement inconnu, non applicable et vérifié.

Ces chiffres constituent un état de référence du corpus à la date de l'audit. Ils ne sont pas des notes de qualité et ne doivent pas servir à classer mécaniquement les sources ou les sujets.

