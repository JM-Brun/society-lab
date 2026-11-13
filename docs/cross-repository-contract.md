# Contrat d'intégration inter-dépôts

**Statut :** contrat d'architecture initial — à réviser après les premiers échanges réellement matérialisés.  
**Révisé :** 2026-11-13.

## 1. Objet et règle directrice

Society Lab appartient à un écosystème de projets de connaissance, d'apprentissage, de recherche appliquée et de présentation professionnelle. Cet écosystème doit permettre la réutilisation raisonnée des méthodes et des résultats sans fusionner les dépôts, leurs graphes, leurs publics ni leurs niveaux de confidentialité.

**Une proximité thématique ne constitue pas une intégration.** Une interface n'est considérée comme réelle que si elle est documentée, vérifiable et utile : lien stable, référence versionnée, contrat de données, procédure de transfert ou artefact effectivement réutilisé.

Le dépôt Git Society Lab demeure la source de vérité de ses objets, de ses analyses et de ses décisions. Les pages Quarto, index et exports sont des projections éditoriales ou techniques dérivées.

## 2. Responsabilités et propriété canonique

| Espace | Responsabilité canonique | Relation légitime avec Society Lab | Frontière à préserver |
|---|---|---|---|
| Wiki de connaissances généraliste (privé) | Définitions et explications conceptuelles réutilisables, relations entre concepts | Référence conceptuelle interne ; transfert d'une définition générale si nécessaire à une analyse | Ne pas rendre le site public dépendant d'une page privée ; pas de copie intégrale |
| Laboratoire LLM public | Parcours pédagogique LLM, exercices, visualisations, implémentations et expériences reproductibles | Réutiliser une méthode ou un résultat LLM lorsqu'il éclaire une question sociétale | Ne pas confondre démonstration pédagogique et preuve sociétale |
| Projet scientifique J-DriftX public | Modèles, hypothèses physiques, méthodes numériques, code et preuves propres au projet | Référence méthodologique éventuelle pour la modélisation ou l'évaluation | Ne pas transférer une conclusion d'un domaine à un autre sans justification |
| Espace professionnel privé | Compétences personnelles, diagnostics, preuves privées et décisions de carrière | Peut référencer en privé un artefact Society Lab comme expérience de travail | Aucun score, diagnostic, donnée personnelle ou décision privée dans Society Lab |
| Portfolio professionnel public | Présentation sélective d'artefacts et affirmations professionnelles vérifiés | Peut présenter un dossier Society Lab après revue de publication et vérification de ses résultats | Le portfolio ne certifie pas à lui seul la qualité scientifique ; aucune affirmation anticipée |
| Society Lab | Sources, études, jeux de données, claims, hypothèses, concepts, mécanismes, institutions, débats, analyses, méthodes et dossiers sociétaux | Propriétaire de ses questions, de ses preuves et de ses conclusions | Ne devient ni wiki généraliste, ni cours LLM, ni registre de compétences |

Cette table décrit des responsabilités cibles. Elle ne prétend pas que chaque interface est déjà matérialisée.

## 3. Interfaces et statut initial

Les statuts ci-dessous sont des constats documentaires initiaux, non une certification exhaustive de tous les dépôts.

| Interface | Statut initial | Condition pour devenir une intégration vérifiée |
|---|---|---|
| Society Lab ↔ Wiki généraliste | À formaliser | Référence interne à un concept canonique ; explication publique autonome et sourcée si nécessaire |
| Society Lab ↔ LLM Lab | Complémentarité potentielle, non démontrée | Référence vers un exercice, une expérience ou une méthode précise, avec version et limites |
| Society Lab ↔ J-DriftX | Complémentarité potentielle, non démontrée | Réutilisation explicite d'une méthode avec justification de transférabilité |
| Society Lab ↔ espace professionnel privé | Séparation nécessaire ; transfert privé possible | Référence à un artefact et à une preuve, sans importer les données personnelles |
| Society Lab ↔ portfolio public | Publication éventuelle, non automatique | Revue de publication, résultats réellement exécutés, sources accessibles et formulation proportionnée |

Ne pas ajouter de liens artificiels pour rendre la matrice plus complète. Une interface peut rester absente si aucun besoin réel ne justifie le couplage.

## 4. Identifiants, graphes et correspondances

Society Lab conserve ses propres identifiants sémantiques typés (SOURCE-*, STUDY-*, DATASET-*, CLAIM-*, HYPOTHESIS-*, CONCEPT-*, MECHANISM-*, ORG-*, ANALYSIS-*, METHOD-*, DOSSIER-*, etc.).

Aucun identifiant global ne doit être imposé. Les identifiants de compétences, de concepts généralistes, de modules pédagogiques et d'objets de recherche répondent à des besoins différents.

Lorsqu'une correspondance inter-dépôts est utile, la qualifier explicitement comme :
- **exacte** : les deux références désignent réellement le même objet ou concept dans le périmètre défini ;
- **partielle** : elles se recouvrent sans être équivalentes ;
- **analogue** : elles partagent une fonction ou une structure, sans identité sémantique ;
- **ambiguë** : les informations ne suffisent pas à trancher ;
- **absente** : aucune correspondance défendable n'a été établie.

Toute correspondance utile doit préciser les deux identifiants et dépôts, le type de correspondance, sa justification, la version ou le commit observé, la date de revue et, si nécessaire, les limites. Une correspondance ne doit jamais être inférée d'un simple nom similaire ou d'un tag partagé.

Les graphes restent locaux à leur dépôt. Une relation REL-ABOUT ou REL-USES de Society Lab n'est pas automatiquement équivalente à une relation d'un autre graphe. Ne pas fusionner les graphes ni importer leurs arêtes sans mapping explicite et revue sémantique.

## 5. Contrat de preuve et de transfert

Tout élément transféré vers une analyse Society Lab doit conserver :
1. sa source et sa provenance ;
2. son statut épistémique (donnée, résultat rapporté, interprétation, hypothèse, jugement) ;
3. son périmètre (population, unité, période, territoire) ;
4. sa méthode et ses principales limites ;
5. la version consultée et la date de vérification.

Une publication, une page pédagogique, un notebook ou un test logiciel ne devient pas une preuve d'une affirmation sociétale par sa seule existence. Pour une méthode transférée, expliciter ce qui est réutilisé, les hypothèses qui changent et les vérifications nécessaires.

Dans Society Lab, conserver la distinction entre source, étude, dataset, claim, hypothèse et analyse. Le graphe organise les relations ; il ne valide pas les conclusions.

## 6. Frontières privé/public et publication

- Les dépôts publics doivent pouvoir être lus, construits et compris sans accès à un dépôt privé.
- Une page publique ne doit pas présenter un lien privé comme une ressource accessible au lecteur.
- Les références privées nécessaires à la coordination restent dans les espaces privés ; ne pas publier de crosswalk révélant des identifiants, diagnostics ou détails personnels.
- Ne pas copier automatiquement des fichiers, registres, historiques, prompts, données ou résultats d'un dépôt vers un autre.
- Toute publication d'un artefact Society Lab dans un portfolio exige une revue distincte : droits des sources, données personnelles, reproductibilité, limites, statut des résultats et intérêt pour le lecteur.
- L'ouverture du code ou du dépôt ne rend pas automatiquement réutilisables les documents, jeux de données ou contenus tiers.

## 7. Dépendances techniques

Les dépôts ne doivent pas avoir de dépendance de build ou de CI vers un dépôt privé. Une indisponibilité ou un changement d'accès d'un dépôt voisin ne doit pas casser la construction du site Society Lab.

Privilégier les liens HTTP(S) vers des artefacts publics stables, les références de commit lorsque la reproductibilité l'exige et les citations des sources originales. Éviter les sous-modules, synchronisations et imports automatiques tant qu'un besoin démontré ne les justifie pas.

Les exports de graphe, index et pages de site sont des vues dérivées. Toute donnée importée doit conserver sa provenance et pouvoir être reconstruite ou vérifiée.

## 8. Exemple : dossier Parcoursup

Le dossier Parcoursup est une recherche sociétale autonome. Il ne constitue pas par défaut :
- une preuve de compétence personnelle ;
- un exercice du parcours pédagogique LLM ;
- une validation scientifique d'une méthode générique ;
- un résultat publiable avant exécution, contrôle et interprétation de l'analyse.

Une fois les analyses effectivement exécutées et revues, certains artefacts peuvent éventuellement être référencés depuis le portfolio. La décision de publication doit alors distinguer le travail réalisé, les résultats observés, les limites méthodologiques et les compétences que l'artefact permet réellement d'illustrer.

## 9. Revue de conformité

Pour toute nouvelle interface, la revue doit répondre à ces questions :
- Quel dépôt possède l'information canonique ?
- Quel besoin concret justifie le lien ou le transfert ?
- La référence est-elle stable, typée, versionnée et vérifiable ?
- La correspondance est-elle exacte, partielle, analogue ou incertaine ?
- Les droits et le niveau de confidentialité autorisent-ils le transfert ?
- Le dépôt consommateur reste-t-il autonome si la référence disparaît ?
- La preuve transférée est-elle adaptée à la conclusion proposée ?
- Le transfert introduit-il une duplication ou une dépendance de maintenance ?

Une interface non documentée reste « non vérifiée ». Une absence d'interface n'est pas en soi un défaut. Toute modification de ce contrat doit être réalisée par une PR revue, sans synchronisation automatique implicite.