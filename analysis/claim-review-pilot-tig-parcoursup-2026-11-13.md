# Revue pilote des affirmations — TIG et Parcoursup

- **Date :** 13 novembre 2026
- **Périmètre :** 20 objets Claim présents dans `claims/registry.yml`
- **Dossiers concernés :** Parcoursup / égalité des chances ; TIG / peines alternatives
- **Nature de la revue :** audit structurel et méthodologique des fiches, pas une vérification documentaire des sources.

## 1. Résultat exécutif

Les 20 fiches existantes sont compatibles avec l'ancien noyau du schéma Claim, mais aucune ne mobilise encore les nouveaux champs qui rendent la preuve et la révision auditables :

- aucune fiche ne documente de `source_verifications` ;
- aucune ne renseigne la `provenance` des énoncés ;
- aucune ne formule de `best_counterargument` ;
- aucune ne consigne d'`assumptions` explicites ;
- aucune ne conserve d'`counter_evidence` structurée ;
- aucune ne donne de confiance probabiliste argumentée.

Ce constat ne signifie pas que les sources sont fausses ou que les affirmations sont infondées. Il signifie que leur degré de vérification n'est pas encore démontré par les métadonnées des fiches. Le statut `under_review` est donc cohérent et doit être conservé jusqu'à l'examen effectif des documents originaux.

**Aucune probabilité de confiance n'est ajoutée dans cette revue.** En attribuer une sans contrôle des sources, des définitions et des éléments contraires donnerait une précision artificielle.

## 2. Problèmes transversaux

### 2.1 Traçabilité des sources

Les fiches référencent généralement des sources et parfois des études, mais pas le passage précis qui soutient chaque proposition. Pour les affirmations quantitatives, il manque notamment, selon les cas : page, tableau ou figure, unité, dénominateur, population exacte, période, définition de l'indicateur et éventuelles ruptures de série.

La présence d'un identifiant SOURCE dans une fiche ou dans le graphe n'est pas une preuve que la source originale a été ouverte et que le passage a été contrôlé.

### 2.2 Atomicité des affirmations

Plusieurs fiches réunissent des propositions qui pourraient être confirmées ou infirmées séparément. Cela complique la révision et peut conduire à conserver une affirmation entière alors qu'une partie seulement est étayée.

### 2.3 Contradiction et arguments adverses

Les limites sont souvent présentes et utiles, mais elles ne remplacent pas un contre-argument formulé dans sa version la plus forte. Une fiche doit distinguer :
- les éléments qui soutiennent la proposition ;
- les éléments qui la contredisent ;
- les explications alternatives ;
- le meilleur argument adverse ;
- les observations qui conduiraient à réviser la conclusion.

### 2.4 Statuts et confiance

Les fiches sont majoritairement `under_review`. Il ne faut pas les faire passer automatiquement à `supported` au seul motif qu'une source institutionnelle est citée. Le statut porte sur la proposition dans son périmètre, pas sur la réputation de l'émetteur. La confiance numérique restera facultative et ne sera renseignée qu'après une revue argumentée.

## 3. Points de revue prioritaires — TIG

### A. Récidive : proposition trop composite

`CLAIM-TIG-RECIDIVISM-5Y-2025` regroupe au moins trois résultats distincts :
1. un taux brut de récidive à cinq ans proche de 60 % ;
2. un résultat ajusté sur la probabilité de récidive comparant TIG et emprisonnement ferme ;
3. des résultats différenciés sur la fréquence et la gravité des récidives.

**Action recommandée :** scinder en fiches distinctes, chacune avec son indicateur, son horizon, sa population, sa méthode et sa formulation. La première est descriptive ; les suivantes sont des résultats empiriques comparatifs dont l'interprétation causale dépend des hypothèses d'identification. Ne pas transformer « correction économétrique » en preuve causale sans examiner le modèle, les variables et les tests de robustesse.

**Contre-argument à traiter :** les différences résiduelles de profils, de gravité des faits, d'antécédents et de sélection dans les sanctions peuvent expliquer une partie des écarts observés ; les résultats sur la fréquence ou la gravité peuvent être sensibles aux définitions et aux fenêtres d'observation.

### B. Coût unitaire : ne pas confondre coût observé et efficience

`CLAIM-TIG-UNIT-COST-2025` juxtapose deux montants unitaires. Le dossier indique déjà que le périmètre comptable ne représente pas nécessairement le coût social complet.

**Action recommandée :** vérifier dans le rapport les unités, postes inclus, année de valeur, méthode d'allocation et comparabilité des deux montants. Garder distinctes la comparaison comptable et toute conclusion d'efficience. Une économie nette dépend du scénario réellement remplacé (incarcération, DDSE, autre peine ou absence d'incarcération).

**Contre-argument à traiter :** un coût unitaire inférieur peut refléter un périmètre de coûts différent ou le transfert de charges vers les SPIP, collectivités, associations et tuteurs non rémunérés ; il ne prouve pas qu'une extension du TIG réduit mécaniquement la dépense publique ou sociale.

### C. Prononcé du TIG : séparer le niveau et l'évolution

`CLAIM-TIG-PRONOUNCED-DOWN-2015-2022` combine le volume de 2022 et une baisse relative depuis 2015.

**Action recommandée :** conserver deux propositions ou une proposition principale avec deux mesures clairement distinguées. Contrôler la série, les catégories de TIG incluses, les changements de nomenclature et le périmètre « délits ». Examiner séparément les facteurs explicatifs : alternatives aux poursuites, profils orientés, offre de postes, décisions judiciaires et organisation des SPIP.

### D. Délais d'exécution

`CLAIM-TIG-EXECUTION-DELAY-2025` est un indicateur opérationnel important, mais le point de départ et le point d'arrivée du délai doivent être localisés dans le rapport intégral.

**Action recommandée :** relever la définition exacte, la population et la distribution (moyenne, médiane, dispersion) si disponibles. Ne pas déduire du seul délai un effet causal sur la dissuasion ou la récidive.

### E. Capacité d'accueil et tutorat

`CLAIM-TIG-TUTORS-NETWORK-2021` mesure un stock historique de tuteurs et d'organismes, pas la capacité immédiatement mobilisable. Les affirmations territoriales sur les référents, les collectivités ou les projets programmés sont elles aussi à distinguer des places effectivement ouvertes, vacantes et adaptées.

**Action recommandée :** demander ou rechercher des données agrégées récentes par territoire : postes actifs, vacants, suspendus, délais d'affectation, capacité d'encadrement et taux d'achèvement. Pour la Loire-Atlantique, ne pas publier de cartographie d'offre confirmée à partir de simples pistes de prospection.

## 4. Points de revue prioritaires — Parcoursup et éducation

### A. Dénominateurs distincts

Les affirmations `CLAIM-PARCOURSUP-2026-NEW-BACHELORS-OFFER` et `CLAIM-PARCOURSUP-2026-LYCEENS-OFFER` portent sur des populations différentes. Elles ne doivent pas être rapprochées comme si elles mesuraient le même taux de réussite. Les candidats, lycéens ayant formulé des vœux, néo-bacheliers inscrits, propositions reçues, acceptations et inscriptions sont des populations ou événements différents.

**Action recommandée :** vérifier pour chaque taux le numérateur, le dénominateur, la date d'observation, les exclusions et le traitement des candidats ayant plusieurs statuts. Ajouter une table de définitions communes avant toute comparaison temporelle.

### B. Nombre total de candidats

`CLAIM-PARCOURSUP-2026-APPLICANTS` doit préciser ce que recouvre « candidats » : catégories incluses, doubles inscriptions éventuelles, candidats en réorientation, apprentissage ou autres procédures selon la définition officielle.

### C. Écarts sociaux

`CLAIM-PISA-2022-SOCIOECONOMIC-GAP`, `CLAIM-INSEE-EARLY-SOCIAL-GAPS` et `CLAIM-INTERGEN-EDUCATION-ATTAINMENT-GAP` ne mesurent pas le même phénomène. Ils ne doivent pas être assemblés en une seule chaîne causale sans expliciter les populations, indicateurs et temporalités. Les écarts descriptifs n'identifient pas, à eux seuls, l'effet causal d'une politique, d'un établissement ou de Parcoursup.

**Action recommandée :** retrouver les tableaux exacts, préciser les indices socio-économiques et les catégories de diplôme, documenter les incertitudes statistiques et distinguer association, transmission intergénérationnelle et mécanismes causaux.

### D. Rapports des commissions d'examen des vœux

`CLAIM-PARCOURSUP-CEV-LOCAL-CRITERIA` décrit le cadre institutionnel ; `CLAIM-PARCOURSUP-CEV-REPORTS-2026` porte sur un volume de rapports annoncés comme accessibles. Ni l'une ni l'autre ne prouve les pratiques réelles de classement ou la façon dont chaque dossier individuel est traité.

**Action recommandée :** constituer le cadre de collecte, archiver les versions accessibles, échantillonner selon le protocole existant et distinguer systématiquement critère déclaré, pondération explicite, outil d'aide, classement et décision finale. Ne pas inférer une discrimination ou son absence à partir des seuls rapports.

## 5. Ordre de traitement proposé

| Priorité | Fiches / objets | Travail requis | Condition avant changement de statut |
|---|---|---|---|
| P0 | Récidive TIG | Scinder les résultats, vérifier méthode et indicateurs | Résultats distincts localisés dans le rapport et limites d'identification décrites |
| P0 | Taux Parcoursup 2026 | Vérifier numérateurs, dénominateurs et populations | Table de définitions et valeurs sources retrouvées |
| P1 | Coûts TIG | Vérifier périmètre comptable et scénario de substitution | Unités et postes de coûts documentés |
| P1 | Prononcé TIG et délais | Vérifier séries et définitions | Tableaux et définitions exacts localisés |
| P1 | Écarts sociaux en éducation | Vérifier tableaux, indicateurs et populations | Mesures et limites statistiques documentées |
| P2 | Réseau territorial TIG | Actualiser la capacité réellement disponible | Données locales datées, agrégées et vérifiables |
| P2 | Rapports CEV | Constituer et coder un corpus | Protocole d'échantillonnage et fiabilité du codage appliqués |

## 6. Règles d'édition issues du pilote

1. Ne pas ajouter un statut `source_checked` sans localisation vérifiable dans le document original.
2. Ne pas renseigner `independently_reviewed` sans seconde vérification réellement effectuée et documentée.
3. Ne pas remplir une probabilité de confiance pour donner une apparence de rigueur.
4. Scinder une affirmation lorsque ses composantes peuvent avoir des statuts ou des preuves différents.
5. Conserver les formulations et données initiales dans l'historique Git ; documenter les corrections plutôt que les effacer.
6. Le graphe relie des objets ; il ne certifie pas la validité des affirmations. Une relation `SUPPORTS` ne remplace pas l'examen du passage source.

## 7. Limites de cette revue

Cette revue a porté sur la structure des 20 fiches et sur leur cohérence interne avec les dossiers. Elle n'a pas ouvert et vérifié individuellement toutes les sources primaires, n'a pas recalculé les statistiques, n'a pas reproduit les modèles économétriques et n'a pas audité les décisions réelles d'admission ou d'exécution des peines. Les résultats décrits dans les dossiers restent donc à l'état documentaire indiqué par leurs fiches.

La prochaine étape empirique doit commencer par les sources P0 et les localisateurs précis, et non par l'ajout mécanique de champs aux 20 fiches.
