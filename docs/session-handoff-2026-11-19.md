# Reprise de session — 19 novembre 2026

## État du dépôt vérifié

- Dépôt : `JM-Brun/society-lab`
- Branche de référence : `main`
- Commit observé au début de la session : `134ec3b6d22bd9d4053399b66c506caae6bd2bd7`
- Visibilité : public ; accès de lecture et d'écriture disponible.
- Issues ouvertes : 25 au moment de l'inventaire.
- Pull requests ouvertes : aucune au moment de l'inventaire.
- Aucun résultat scientifique nouveau n'est revendiqué par cette note.

Cette photographie est datée : vérifier à nouveau les issues, PR, branches et exécutions CI avant toute reprise.

## Bilan des acquis à préserver

Le dépôt dispose déjà de registres canoniques, de schémas, d'un graphe typé, de dossiers et synthèses, de procédures d'ingestion, de contrôles CI, d'une gouvernance des issues et d'indicateurs de pilotage. Les travaux récents ont notamment consolidé les liens Markdown, classifié les fichiers Markdown non mappés, réconcilié des doublons documentaires et relié plusieurs audits d'études SMIC aux registres canoniques.

Ne pas créer de registre, graphe, taxonomie ou synthèse parallèle lorsqu'un artefact canonique existe déjà. Toute nouvelle relation probante doit être sourcée et qualifiée ; une proximité thématique ne constitue pas une causalité.

## Priorités de reprise

### P0 — Contrôler le backlog et les validations

1. Refaire l'inventaire des issues ouvertes et des PR, car l'état peut avoir changé depuis le 19 novembre.
2. Vérifier les runs CI et les scans de secrets sur le dernier commit de `main`, et non seulement les résultats historiques mentionnés dans les issues.
3. Contrôler la cohérence des labels et priorités selon `governance/issue-labels.json`.
4. Exécuter pour la première fois le workflow `.github/workflows/backlog-view.yml` après fusion de la PR #130 ; contrôler les 25/26 mappings selon le backlog réellement observé, les éléments non mappés et les dépendances. Ne pas présumer que le nombre historique de mappings correspond au backlog courant.
5. Pour la synchronisation des labels (#125), lancer le dry-run et examiner le rapport avant toute application.

### P1 — Audit des KPIs et qualité du graphe (#156)

1. Exécuter le calculateur en lecture seule et récupérer le rapport courant, notamment `uncovered_source_ids`.
2. Classer chaque source non couverte : contexte, doublon/obsolète, mobilisable mais non reliée, ou ambiguë.
3. Ne créer que les liens justifiés par le contenu et conserver la justification.
4. Vérifier les règles d'éligibilité des dossiers et claims, les identifiants absents/inconnus, les collisions et la compatibilité sémantique des extrémités de relations.
5. Définir une matrice minimale de relations attendues par type d'objet ; exclure explicitement les objets qui peuvent légitimement rester isolés.
6. Publier d'abord des listes d'anomalies et des comptes par type. Ne pas publier de ratio global de connectivité avant validation de l'éligibilité.
7. Comparer les coûts marginaux du benchmark ×1/×10/×100 dans les résumés Actions ; garder le benchmark informatif et sans seuil arbitraire, ou le déplacer vers un workflow manuel/périodique si son coût le justifie.

**Garde-fou :** les KPIs mesurent des propriétés documentaires et techniques, jamais la vérité, la robustesse ou l'exhaustivité scientifique d'un dossier.

### P1 — Audit opérationnel du pipeline (#114)

1. Cartographier le pipeline réellement utilisé, ses entrées/sorties, états, artefacts, erreurs, reprises et critères de passage.
2. Auditer les schémas et métadonnées sur les usages réels : versions, localisateurs, méthodes d'extraction, vérification humaine, unités, populations, périodes et provenance.
3. Distinguer extraction, transcription, résultat rapporté, calcul reproduit, interprétation et hypothèse.
4. Auditer la cohérence entre fiches, registres et arêtes du graphe ; ajouter des tests négatifs ciblés uniquement après caractérisation des anomalies.
5. Articuler ce chantier avec #112 sans dupliquer son travail ontologique.

### P1 — Relations inter-domaines (#112)

Le cadre de lecture transversal et l'inventaire initial sont déjà intégrés à `main`. La photographie historique (585 relations, 407 objets référencés, 15 concepts canoniques) doit être recalculée avant toute conclusion.

Prochaine séquence :
1. Prendre le pilote éducation → compétences → emploi → salaires.
2. Inventorier les études, claims, concepts, mécanismes, acteurs, indicateurs et localisateurs de source déjà présents.
3. Vérifier des parcours inter-graphes positifs, négatifs et ambigus jusqu'aux localisateurs.
4. Contrôler les identifiants, les libellés FR/EN et la reproductibilité des projections.
5. Examiner les validateurs et l'ontologie avant de proposer un type d'objet ou de relation supplémentaire.
6. Ne pas ajouter d'arêtes causales sur la seule base de tags, de cooccurrences ou de plausibilité.

### P1 — Importer les données réelles, sans extrapoler depuis les métadonnées

**Parcoursup (#2)**
- Télécharger le CSV officiel courant et enregistrer URL, horodatage réel, taille, encodage, séparateur et SHA-256.
- Contrôler le schéma et les champs taux d'accès/rang ajoutés en mars 2026, les lignes et les colonnes réellement présentes.
- Exécuter le script existant, contrôler les manifestes et dénominateurs, puis produire une note de résultats sourcée.
- Ne pas assimiler des comptes par formation à des personnes uniques ; ne pas reconstruire les taux officiels manquants ni tirer de causalité des agrégats descriptifs.

**ADEME Transition(s) 2050 Saison 2 (#110)**
- Lire la documentation API et identifier les endpoints et la pagination par vérification réelle.
- Piloter la récupération du premier jeu prioritaire : métadonnées, schéma, export brut ou procédure reproductible, date, identifiant et SHA-256.
- Vérifier complétude, unités, scénarios et périmètres avant harmonisation.
- Étendre ensuite aux six autres jeux prioritaires ; comparer Saison 1 et Saison 2 seulement sur des indicateurs réellement compatibles.
- Ne calculer aucune valeur à partir des seuls nombres d'enregistrements du catalogue.

### P2 — Consolider les dossiers scientifiques

- **SMIC (#25, #26, #27, #28, #29, #36, #82, #83, #84)** : poursuivre l'audit des textes intégraux et annexes, harmoniser les populations/périodes/dénominateurs, séparer effets du SMIC, allègements, contrats aidés et transferts socio-fiscaux. Préserver la conclusion provisoire : le bilan net agrégé n'est pas identifié tant que les effets par acteurs et horizons ne sont pas réconciliés.
- **TIG (#21 à #24)** : harmoniser les cohortes, définitions de récidive, délais prononcé–achèvement, coûts complets et conditions de comparaison ; ne pas interpréter les écarts bruts comme causaux.
- **Autres dossiers** : poursuivre les travaux #91, #103 et #104 selon leurs critères d'acceptation et actualiser les synthèses associées.

### P2 — Gouvernance des issues (#123, #126, #127)

- #123 : produire la vue de backlog par priorité, nature, domaine et dépendance ; ne pas inférer le domaine depuis le titre.
- #126 : obtenir une décision humaine sur les cinq alertes de priorité historiquement relevées (#2, #29, #36, #82, #110), après relecture du contexte actuel ; ne pas reprioriser automatiquement.
- #127 : exécuter et vérifier la première génération réelle de la vue de backlog après fusion de la PR #130.
- #125 : examiner le dry-run avant toute synchronisation effective des labels.

## Ordre conseillé pour la prochaine session

1. Vérifier `main`, CI, PR et backlog courant.
2. Exécuter le workflow de vue de backlog et le dry-run des labels ; consigner les écarts.
3. Produire le rapport KPI courant et commencer le classement des sources non couvertes.
4. Réaliser le pilote de traçabilité inter-domaines éducation–compétences–emploi–salaires.
5. Lancer un pilote d'acquisition réelle Parcoursup ou ADEME selon la disponibilité effective des exports ; ne pas prétendre que l'un est traité tant que les données brutes n'ont pas été obtenues et contrôlées.
6. Mettre à jour les synthèses et graphes concernés, puis documenter les limites et le travail restant dans les issues canoniques.

## Règles de clôture et de publication

- Une issue n'est fermée que lorsque ses critères d'acceptation sont satisfaits et les livrables intégrés, ou lorsqu'une décision explicite de remplacement/non-planification est documentée.
- Une CI verte valide les contrôles exécutés, pas la qualité scientifique globale.
- Distinguer systématiquement fait vérifié, résultat rapporté, calcul reproduit, interprétation et hypothèse.
- Toute synthèse de sujet doit présenter constats, preuves, controverses/limites et conclusions opérationnelles.
- Compléter et maintenir les graphes associés à chaque sujet : concepts, mécanismes, acteurs, indicateurs, sources et controverses.
- Documenter les tâches non terminées dans les issues canoniques et dans le prochain relevé de session.

## Références de pilotage

- [#156 — KPIs et diagnostics du graphe](https://github.com/JM-Brun/society-lab/issues/156)
- [#114 — Audit du pipeline](https://github.com/JM-Brun/society-lab/issues/114)
- [#112 — Lecture transversale](https://github.com/JM-Brun/society-lab/issues/112)
- [#2 — Parcoursup 2025](https://github.com/JM-Brun/society-lab/issues/2)
- [#110 — ADEME Saison 2](https://github.com/JM-Brun/society-lab/issues/110)
- [#123 — Taxonomie des issues](https://github.com/JM-Brun/society-lab/issues/123)
- [#125 — Synchronisation des labels](https://github.com/JM-Brun/society-lab/issues/125)
- [#126 — Revue sémantique du backlog](https://github.com/JM-Brun/society-lab/issues/126)
- [#127 — Vue multidimensionnelle du backlog](https://github.com/JM-Brun/society-lab/issues/127)


## Complément de suivi — 19 novembre 2026, contrôle de reprise

### Contrôles PR #160

- Au contrôle initial, la PR #160 était ouverte et mergeable. Après le commit documentaire complémentaire, elle reste ouverte et non fusionnée, mais GitHub renvoie désormais `mergeable=false` : vérifier la cause (notamment un éventuel conflit avec `main`) avant toute revue finale ou fusion.
- Le diff relu porte toujours sur les deux fichiers attendus (README et note de reprise) ; il totalise maintenant 147 ajouts et aucune suppression. Le contrôle initial, avant complément, portait sur 120 ajouts.
- Les deux contrôles déclenchés sur le commit de la PR sont terminés avec succès :
  - validation de la base de connaissances : run [44476671851](https://github.com/JM-Brun/society-lab/actions/runs/44476671851), job `validate` — success ;
  - scan de secrets : run [44476671860](https://github.com/JM-Brun/society-lab/actions/runs/44476671860), job `Scan repository history for secrets` — success.
- Aucun commentaire de revue n'était présent lors du dernier contrôle. La fusion reste à faire après revue humaine ; la CI verte ne remplace pas cette revue.

### Backlog recontrôlé

Un nouvel inventaire GitHub a trouvé **26 issues ouvertes** et **1 PR ouverte** (la PR #160). La liste des issues a évolué depuis la photographie initiale de 25 issues ; les priorités du présent document doivent donc être recalées sur ce backlog courant, pas sur les anciens décomptes. La PR #160 reste le seul changement en attente dans le dépôt au moment de ce contrôle.

### Travail restant immédiat

1. Obtenir la revue humaine de la PR #160 puis fusionner uniquement après validation de son contenu et des contrôles requis.
2. Sur #156, récupérer le rapport KPI courant et la liste `uncovered_source_ids`, puis classer chaque entrée avant toute correction du graphe. Le fait que le calculateur et le benchmark soient intégrés ne signifie pas que cette revue est terminée.
3. Sur #112, recalculer la photographie du graphe sur le `main` courant puis conduire le pilote éducation → compétences → emploi → salaires avec parcours positifs, négatifs et ambigus jusqu'aux sources.
4. Sur #114, poursuivre la cartographie des étapes réellement exécutées et la matrice de couverture des schémas/validateurs ; coordonner avec #112 sans dupliquer les règles ontologiques.
5. Reprendre le contrôle de #123/#125/#126/#127 : exécuter la vue backlog après la dépendance #130, inspecter le dry-run des labels et faire valider humainement les priorités signalées.
6. Réexaminer les issues sectorielles du backlog reconstitué ; en particulier, ne pas fermer les issues SMIC, TIG, Parcoursup ou ADEME tant que les données, analyses, synthèses et graphes attendus ne sont pas livrés.

**Limites du contrôle :** aucun rapport KPI n'a été exécuté dans cette séquence ; aucun CSV Parcoursup ni export ADEME n'a été téléchargé ; aucune relation du graphe ni conclusion scientifique n'a été modifiée. Les résultats CI ci-dessus portent uniquement sur les deux jobs nommés et sur le commit précédent le complément documentaire. Aucun run associé au nouveau commit `39e8665bacc4845d075459af3cd1d4beb15d5288` n'a été retourné par le contrôle des runs PR ; il faut vérifier les statuts de checks propres à ce commit avant de considérer la PR validée.


## Actualisation après fusion de la PR #160 — 19 novembre 2026

### État de la PR et CI

La PR #160 est fusionnée dans `main` (merge commit `567e43dcb0d780109690353a6ac6f4c7936316ca`). Les workflows `Validate knowledge base` et `Secret scanning` associés au dernier commit documentaire ont terminé avec succès. La note de reprise et son lien README sont donc publiés.

### Recalcul des KPIs sur le main fusionné

Le calculateur `scripts/validate/calculate_project_kpis.py` a été exécuté par le job `validate` du run [44477441297](https://github.com/JM-Brun/society-lab/actions/runs/44477441297), étape `Report project KPIs (read-only)`, avec succès. Instantané : 2026-11-19T07:09:40Z.

| Indicateur | Numérateur / dénominateur | Résultat |
|---|---:|---:|
| Couverture documentaire des sources | 218 / 220 | 99,1 % |
| Claims avec conclusion documentée | 28 / 80 | 35,0 % |
| Dossiers actifs avec synthèse valide | 25 / 25 | 100 % |

Diagnostics associés :
- Deux sources restent sans relation documentaire retenue : `SOURCE-DEFENSEUR-DROITS-JEUNESSES-ORIGINE-2026` et `SOURCE-EU-EDUCATION-MONITOR-2025-FRANCE`. Elles sont conservées en contexte ; aucun lien artificiel n'est justifié.
- Claims : 27 `partially_supported`, 1 `supported`, 52 `under_review` ; 3 `superseded` sont exclus. Aucune anomalie de statut signalée.
- Synthèses : aucun dossier actif sans association/fichiers valides ; 11 fichiers de synthèse distincts pour 25 dossiers actifs.
- Le calculateur rapporte 684 relations et 476 identifiants indexés ; aucune anomalie structurelle n'est remontée par ses contrôles.

La revue historique des 51 sources sans relation retenue (instantané antérieur) a été traitée dans la PR #158 : 49 sources distinctes ont reçu 51 relations documentaires justifiées ; les deux sources ci-dessus demeurent contextuelles. Ne pas reprendre l'ancien décompte 51 comme état courant.

**Interprétation :** ces KPIs mesurent des propriétés documentaires et de maintenance. Ils ne mesurent ni la vérité des claims, ni l'indépendance des preuves, ni la qualité scientifique des synthèses.

### Travail restant recalé

1. **#156 — Connectivité et sémantique :** la matrice de règles attendues par type d'objet est documentée dans `docs/source-linkage-decisions-2026-11-18.md`. Il reste à la traduire en diagnostics déterministes : compatibilité sémantique des endpoints, collisions d'identifiants entre registres, relations orphelines et tests négatifs. Ne pas produire de ratio global avant validation des populations éligibles.
2. **#112 — Transversal :** recalculer l'inventaire des objets et relations sur le main actuel, puis mener le pilote éducation → compétences → emploi → salaires. Documenter les parcours positifs, négatifs et ambigus jusqu'aux localisateurs de preuve ; aucune causalité ne découle d'une cooccurrence.
3. **#114 — Pipeline :** poursuivre l'audit de couverture réelle des schémas et validateurs, des contrats de provenance et des parcours de bout en bout Parcoursup/ADEME/TIG. Prioriser les lacunes testables plutôt qu'une réécriture générale des documents.
4. **#123/#125/#126/#127 — Gouvernance :** recontrôler les workflows backlog et labels, produire le dry-run, examiner les mappings non résolus et demander une validation humaine des priorités.
5. **Parcoursup (#2) et ADEME (#110) :** acquérir les données brutes et conserver URL, date, schéma, unités, périmètre et SHA-256 avant toute analyse quantitative.
6. **SMIC/TIG :** continuer les audits sectoriels, actualiser chaque synthèse et ses relations probantes ; ne pas inférer la causalité à partir des seuls écarts descriptifs.

### Traçabilité GitHub

- Résultats KPI et suite #156 : commentaire [7002394715](https://github.com/JM-Brun/society-lab/issues/156#issuecomment-7002394715).
- PR #160 fusionnée : https://github.com/JM-Brun/society-lab/pull/160.
- Le run 44477441297 confirme le passage du calcul KPI et de l'ensemble du job `validate` ; il ne constitue pas une revue scientifique des dossiers.


## Complément d'audit KPI / graphe — 19 novembre 2026

La PR #162 complète le calculateur KPI afin qu'il vérifie, en plus de l'existence des endpoints et des types de relations, la compatibilité des types `from` et `to` avec `knowledge/RELATION_TYPES.yml`. Le validateur bloquant `scripts/validate/validate_registry.py` effectuait déjà ce contrôle ; le changement aligne donc le diagnostic KPI sur la règle canonique, sans remplacer le validateur.

- Les relations incompatibles sont exclues du calcul de couverture et remontées sous `incompatible_endpoints`.
- L'index des types de nœuds est construit à partir des registres canoniques, domaines, territoires et synthèses.
- Les collisions entre un identifiant de synthèse et un identifiant déjà déclaré dans un autre registre sont signalées ; les associations répétées d'une même synthèse à plusieurs dossiers restent autorisées.
- Tests ajoutés : endpoint sémantiquement incompatible, index des types et collision d'identifiant de synthèse.
- Aucun objet, relation ou claim du graphe courant n'a été modifié.

**État au moment de cette note :** PR #162 ouverte ; une première CI a réussi (118 tests, validation des registres, rapport KPI et secret scan). Un test supplémentaire de collision a ensuite été ajouté ; la CI du dernier commit doit être vérifiée avant revue/fusion.

**Suite :** vérifier la CI du dernier commit de #162, relire le diff, puis faire relire la PR avant fusion. Après intégration, conserver les deux sources contextuelles sans relation et ne pas introduire de ratio global de connectivité sans définir au préalable les populations éligibles.


## Reprise actualisée — 19 novembre 2026, après intégration des PR #170, #171 et #173

### État GitHub revérifié

Le relevé précédent n'est plus actuel. Les PR ont évolué après le contrôle initial :

- PR #170 — tests d'impact Parcoursup : **fusionnée** le 19 novembre 2026 à 13:23:12 UTC.
- PR #171 — liens croisés vers les audits détaillés SMIC : **fusionnée** à 13:23:25 UTC.
- PR #173 — correction de filiation documentaire Kramarz–Philippon : **fusionnée** à 13:24:09 UTC.
- PR #172 — première branche ADEME/traçage : fermée comme **supersédée**, non fusionnée. Sa base était devenue divergente après les trois fusions ; ne pas compter son CI historique comme validation du code repris.
- Inventaire GitHub effectué après ces changements : **24 issues ouvertes** et une PR ouverte au moment du relevé (la nouvelle PR #174).

La fusion de #170 a entraîné la clôture de l'issue #120. Cette clôture ne signifie pas que tous les objectifs historiques de #120 sont réalisés : les parcours Parcoursup sont désormais couverts par tests d'intégration et la suite ADEME est reprise dans #174, mais le journal persistant des décisions de revue, les événements de cycle de vie des sources, la mesure de couverture et la scalabilité restent à traiter dans le cadre de l'audit transversal #114. Ne pas rouvrir #120 uniquement pour conserver une liste de tâches ; rattacher les travaux résiduels à #114 et #110.

### Contenu intégré à préserver

**Parcoursup / traçage (#170, fusionnée)**

Deux tests d'intégration couvrent les sources ministérielles et SIES de Parcoursup 2026 :
- source ministérielle → étude → dataset → claims candidats/lycéens → dossier → synthèse ;
- source SIES → étude → dataset → claim néo-bacheliers → dossier → synthèse.

Ces tests vérifient la traçabilité documentaire existante. Ils ne prouvent pas que le CSV Parcoursup 2025 a été téléchargé, analysé ou reproduit.

**Synthèse SMIC (#171, fusionnée)**

La synthèse `syntheses/smic-france.md` pointe désormais vers les audits détaillés Abowd et al. (chapitre 2000) et Kramarz–Philippon (IZA DP 219). Les fiches courtes et détaillées sont conservées ; aucune preuve n'est comptée deux fois.

**Filiation Kramarz–Philippon (#173, fusionnée)**

Le lien CiteSeerX historique dont le fichier exact n'a pas été vérifié n'est plus présenté comme une version publiée. Le dossier distingue :
- OCFEB Research Memorandum 0006 (version de travail, avril 2000) ;
- IZA DP 219 (version de travail, novembre 2000) ;
- article publié dans le *Journal of Public Economics* (82(1), 2001, p. 115–146, DOI 10.1016/S0047-2727(00)00137-7).

Les tableaux 1 à 3 des deux versions de travail contrôlées concordent sur les résultats centraux. Le texte intégral éditeur n'a pas été comparé ligne à ligne ; ne pas affirmer une identité intégrale des versions. Aucune fiche n'a été supprimée.

### PR #174 — reprise du traçage ADEME depuis le main courant

La PR [#174](https://github.com/JM-Brun/society-lab/pull/174) reprend depuis le `main` courant les changements de traçage initialement préparés dans #172, après fermeture de #172 comme branche supersédée.

Branche : `test/ademe-impact-trace-mainline`  
Commit de tête observé à la création : `06dc097b9394078e529a7fc84b8572ea8ccf086c`.

Changements :
- test réel ADEME Saison 2 : l'arête de graphe `REL-QUANT-DOSSIER-INCLUDES-ADEME-SEASON2` est affichée comme contexte, sans être propagée en dépendance explicite de dossier/synthèse ;
- avertissement explicite : absence de lien détecté ne prouve pas l'absence de dépendance réelle ;
- `source_verifications` n'est lu comme référence source que pour les claims ;
- extension aux mécanismes (`supporting_study_ids`, `challenging_study_ids`, `claim_ids`) et aux prévisions (`claim_ids`) par références typées ;
- tests synthétiques de portée des références et de chemins mécanisme/prévision.

**État de validation au moment de la rédaction :** aucune exécution CI n'était encore retournée pour le commit #174. Le contrôle de runs PR ne renvoyait aucun run. Il faut vérifier les checks du commit de tête avant toute revue ou fusion. La PR a été créée en brouillon ; aucun chiffre ni résultat d'extraction ADEME n'est revendiqué.

La première version #172 avait un CI vert (122 tests) sur son ancien commit, mais ce résultat ne valide pas automatiquement la reprise #174.

### État des issues à reprendre

- **#110 ADEME Saison 2 — ouverte.** Le catalogue global et la documentation sont repérés, mais le premier export prioritaire n'a pas été acquis avec schéma et SHA-256. Étape suivante : identifier l'API réelle depuis sa spécification ou une réponse vérifiée ; ne pas deviner les routes Opendatasoft. Récupérer d'abord « Bilan énergie finale par secteur en 2050 », conserver l'export brut ou une procédure reproductible, métadonnées, horodatage UTC, unités, scénarios, nombre de lignes et empreinte SHA-256. Aucun calcul avant ce contrôle.
- **#114 audit pipeline — ouverte.** Continuer l'inventaire fichiers → registres → schémas → validateurs, le journal durable des décisions de revue, les événements de cycle de vie des sources, les parcours de bout en bout et la couverture de dépendances. Ne pas dupliquer les travaux de #110.
- **#120 — fermée automatiquement après fusion de #170.** Les tests Parcoursup sont livrés ; les tâches restantes listées dans l'ancienne issue sont réaffectées au périmètre transversal #114 et à l'ingestion ADEME #110.
- **#2 Parcoursup — ouverte.** Les tests d'impact ne remplacent pas l'acquisition et l'analyse du CSV officiel 2025. Télécharger, manifester, hasher, contrôler le schéma et les dénominateurs avant calcul.
- **#123, #125, #127 — ouvertes.** Les exécutions réelles de la vue backlog et du dry-run de labels restent à confirmer ; ne pas passer en mode application sans revue du rapport.

### Ordre de reprise recommandé

1. Vérifier les checks CI de #174 sur son commit courant ; inspecter les éventuels conflits/états GitHub et faire relire le diff. Ne pas fusionner sans revue humaine.
2. Mettre à jour les descriptions/commentaires des issues #114 et #110 pour transférer explicitement les tâches résiduelles de #120 et le statut de #174.
3. Poursuivre #110 par acquisition vérifiée du premier export ADEME ; si l'API n'est pas techniquement documentée ou accessible, consigner le blocage précis plutôt que supposer un endpoint.
4. Exécuter le workflow backlog view (#127) et le dry-run de synchronisation des labels (#125), puis examiner les artefacts et comparer avec l'état GitHub courant.
5. Sur #114/#156, reprendre l'audit des validateurs et diagnostics du graphe ; distinguer couverture documentaire, compatibilité sémantique et qualité scientifique.
6. Sur #2, récupérer réellement le CSV Parcoursup 2025 ; les tests Parcoursup 2026 ne doivent pas être présentés comme résultats d'analyse 2025.
7. Continuer les dossiers SMIC/TIG/Foucher en mettant à jour leurs synthèses et graphes canoniques à mesure que les preuves sont contrôlées.

### Règles de statut pour les prochaines sessions

- Ne pas compter une PR fermée comme intégrée : vérifier explicitement `merged=true`.
- Ne pas réutiliser la CI d'une branche supersédée pour valider sa reprise.
- Une issue fermée par une PR n'implique pas que toutes les tâches historiques ont été réalisées ; transférer les tâches restantes vers une issue active cohérente.
- Une arête contextuelle du graphe ne devient pas une dépendance d'impact sans champ de référence typé.
- Une CI verte valide les contrôles automatisés exécutés, pas l'ingestion, la qualité scientifique ou la complétude des sources.
- Maintenir les synthèses et graphes par sujet ; ne pas créer de registre parallèle.
