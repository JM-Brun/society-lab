# Audit de faisabilité des KPIs — 18 novembre 2026

**Périmètre :** instantané de la branche `main` contrôlé le 18 novembre 2026. Lecture des registres, schémas, graphe et fichiers associés. Les résultats sont reproductibles à partir des sources canoniques ; aucune donnée métier n'a été modifiée.

## Résultats vérifiés

| Élément | Résultat | Interprétation |
|---|---:|---|
| Sources | 220 | Dénominateur du KPI de couverture documentaire |
| Relations du graphe | 633 | Graphe analysé intégralement |
| Relations typées de contribution documentaire | 441 | Types retenus : SUPPORTS, QUALIFIES, INCLUDES, USES, CITES, TRANSCRIBES et TRANSCRIBED-FROM |
| Sources avec au moins une relation documentaire valide | 169 / 220 (76,8 %) | KPI calculable ; 51 sources sans relation retenue |
| Intégrité des relations | 0 justification vide ; 0 identifiant de relation dupliqué ; 0 triplet dupliqué ; 0 endpoint inconnu | Les 633 relations ont des extrémités enregistrées et une justification non vide |
| Nœuds indexés pour vérifier les endpoints | 476 identifiants | Inclut registres, domaines, territoires et identifiants de synthèse |
| Claims | 83 | Population mesurable |
| Statuts des claims | 52 `under_review`, 27 `partially_supported`, 1 `supported`, 3 `superseded` | Champ canonique : `status` |
| Claims actifs avec conclusion documentée | 28 / 80 (35 %) | Conclusion explicite, sans interprétation comme taux de vérité |
| Dossiers actifs | 25 | Dénominateur indépendant issu de `dossiers/registry.yml` ; tous au statut `researching` |
| Associations dossier/synthèse | 25 / 25 | Correspondance exacte entre les 25 dossiers et les 25 entrées du registre |
| Fichiers de synthèse distincts | 11 | Tous les chemins déclarés existent ; plusieurs dossiers peuvent partager une synthèse |

## Méthode de calcul

### 1. Couverture documentaire des sources — calculable

Formule :

`sources ayant au moins une relation documentaire valide / sources du registre`

Sont retenues les relations `REL-SUPPORTS`, `REL-QUALIFIES`, `REL-INCLUDES`, `REL-USES`, `REL-CITES`, `REL-TRANSCRIBES` et `REL-TRANSCRIBED-FROM`. La source peut être à l'une ou l'autre extrémité. Une relation n'est comptée que si son identifiant est présent et unique, sa justification non vide et ses deux endpoints connus.

Les relations `REL-ABOUT` seules sont exclues : elles expriment un rattachement thématique, pas une contribution documentaire. Les relations de synthèse et de hiérarchie territoriale ne sont pas comptées non plus.

Résultat vérifié : **169 / 220 = 76,8 %** ; 51 identifiants de sources ne disposent d'aucune relation retenue. Ce résultat mesure la structuration documentaire, pas la qualité des sources ni la force probante de leur contenu.

### 2. Claims avec conclusion documentée — calculable

Le schéma `schemas/claim.schema.json` impose le champ `status`. Le dénominateur comprend les claims actifs, hors `superseded`. Le numérateur inclut les statuts conclusifs : `supported`, `partially_supported`, `contested`, `not_supported` et `insufficient_evidence`.

Instantané : 83 claims, dont 3 superseded ; 28 claims actifs ont une conclusion explicite, soit **28 / 80 = 35 %**. Les 52 autres claims actifs sont `under_review`.

Ce KPI mesure la présence d'une conclusion épistémique documentée, quelle qu'en soit l'orientation. Il ne mesure ni un taux de vérité, ni une validation indépendante. Les statuts de `source_verifications` décrivent des contrôles par source et restent distincts.

### 3. Couverture des synthèses — calculable

Le dénominateur indépendant est le registre `dossiers/registry.yml`, pas le registre des synthèses lui-même. Les statuts actifs sont `scoping`, `researching`, `draft`, `under_review` et `published` ; `archived` est exclu.

Contrôles effectués :
- 25 dossiers actifs et 25 associations dans `syntheses/registry.yml` ;
- chaque identifiant de dossier est présent exactement une fois dans les associations ;
- aucune association orpheline ou manquante ;
- les 25 chemins de dossier et les 11 chemins de synthèse distincts existent ;
- le partage d'une même synthèse par plusieurs dossiers est intentionnel et ne doit pas être compté comme un doublon de dossier.

Résultat : **25 / 25 = 100 %**. Il s'agit d'une couverture de présence et d'intégrité des fichiers, pas d'une évaluation de la qualité ou de la fraîcheur des synthèses. Réutiliser `scripts/validate/validate_syntheses.py` et `scripts/validate/check_synthesis_freshness.py` pour les contrôles complémentaires déjà disponibles, sans les dupliquer.

### 4. Connectivité du graphe — diagnostic seulement

Le nombre de relations et la présence de références valides ne suffisent pas à définir un taux global de connectivité. Les objets n'ont pas tous vocation à être reliés de la même manière ; les règles d'éligibilité par type restent à formaliser.

Conserver des diagnostics : objets isolés, types incompatibles, relations orphelines et objets sans lien attendu. Ne pas publier de ratio global avant définition du périmètre éligible.

## Prototype et tests

Un calculateur local en lecture seule est ajouté dans `scripts/validate/calculate_project_kpis.py`. Il calcule les trois indicateurs dont le dénominateur est maintenant défendable, à partir des registres canoniques et du graphe, sans réseau ni mutation des fiches. Il propose une sortie Markdown ou JSON et détaille les identifiants non couverts et les anomalies.

Les tests unitaires de `tests/test_project_kpis.py` couvrent notamment :
- relations documentaires valides dans les deux sens ;
- exclusion de `REL-ABOUT` seule ;
- justifications vides, endpoints inconnus et identifiants dupliqués ;
- registres vides et dénominateurs nuls ;
- claims superseded et statuts inconnus ;
- synthèses partagées, dossiers archivés et fichiers de synthèse manquants ;
- identifiants de synthèse répétés dans le registre de correspondance.

Aucune intégration CI n'est ajoutée à ce stade. Il faut d'abord exécuter les tests sur le dépôt, vérifier les sorties du calculateur, puis mesurer son coût sur le corpus actuel et des charges ×10/×100. L'ajout à la CI ne sera envisagé qu'après ces mesures.

## Décisions

1. Les KPIs 1, 2 et 3 sont calculables sans migration de données.
2. Le KPI 4 reste un diagnostic tant que l'éligibilité des objets n'est pas définie.
3. Aucun score composite ni cible arbitraire n'est créé.
4. Les ratios décrivent la structuration et la maintenance documentaires ; ils ne certifient pas la vérité scientifique.
5. Le calculateur reste en lecture seule ; la CI n'est pas modifiée avant validation et benchmark.

**Limite :** les résultats sont un instantané du dépôt au 18 novembre 2026. Toute évolution du schéma, du périmètre ou des relations peut modifier les valeurs et doit être signalée dans les rapports ultérieurs.


## Addendum — intégration CI postérieure à l'audit initial

L'état décrit dans la section « Prototype et tests » ci-dessus correspond à la situation antérieure à l'intégration du benchmark dans la CI. Depuis, le workflow `.github/workflows/validate.yml` exécute `scripts/benchmark/benchmark_project_kpis.py --repeats 3 --scales 1 10 100` dans une étape informative, après le benchmark de validation des schémas de registre. Cette étape ne définit aucun seuil bloquant et ne fait pas échouer la CI sur la valeur d'un KPI.

Exécution de référence sur `main` : [run 44364791315](https://github.com/JM-Brun/society-lab/actions/runs/44364791315), terminé avec succès. Les temps mesurés doivent être lus dans le résumé Actions avant de décider si le benchmark doit rester dans chaque exécution du workflow ou être déplacé vers un déclenchement manuel/périodique. Aucun chiffre de durée n'est repris ici faute de mesure vérifiée dans cet audit.


## Mesure des durées Actions — 18 novembre 2026

Les durées ont été extraites des journaux des jobs Actions, entre le début de chaque commande et le début de la commande suivante. Elles incluent la génération des instantanés synthétiques et l'exécution du script ; elles ne sont pas équivalentes aux seules médianes de validation/calcule.

| Benchmark | Run de référence `44364791315` | PR #157 `44375674389` |
|---|---:|---:|
| Benchmark schémas : durée de l'étape | 26,8 s | 42,2 s |
| Benchmark KPI : durée de l'étape | 7,4 s | 11,6 s |
| Total des deux étapes | 34,2 s | 53,8 s |

Détail du benchmark schémas sur le run de PR : 441 enregistrements à ×1 (0,216764 s médiane), 4 410 à ×10 (1,010848 s) et 44 100 à ×100 (9,064371 s) pour la seule fonction de validation. Le coût de l'étape est supérieur, notamment parce que le benchmark construit et prépare les corpus synthétiques.

Détail du benchmark KPI sur le run de PR :

| Échelle | Chargement YAML médian | Calcul KPI médian | Total médian |
|---|---:|---:|---:|
| ×1 | 1,047114 s | 0,001842 s | 1,048956 s |
| ×10 | 1,051334 s | 0,016635 s | 1,067970 s |
| ×100 | 1,066890 s | 0,198497 s | 1,265387 s |

Les deux runs montrent une variabilité sensible du temps de job ; ils ne justifient pas un seuil de performance rigide. Ils suffisent toutefois à constater que deux étapes informatives ajoutent environ 34 à 54 secondes à une CI, sans contribuer à la validation fonctionnelle de chaque modification.

**Décision :** déplacer les deux benchmarks synthétiques vers un workflow hebdomadaire et déclenchable manuellement. Conserver dans la CI PR/push les validations, tests unitaires, contrôles de schémas et le calcul ordinaire des trois KPIs (sans charges synthétiques). Les résumés Actions du workflow périodique conserveront les mesures de performance.

