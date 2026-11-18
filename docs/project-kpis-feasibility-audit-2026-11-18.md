# Audit de faisabilité des KPIs — 18 novembre 2026

**Périmètre :** lecture des registres, schémas et graphe de la branche `main` au 18 novembre 2026. Audit documentaire en lecture seule ; aucun calculateur, aucune migration et aucune modification des données canoniques.

## Résultats vérifiés

| Élément | Résultat observé | Conséquence |
|---|---:|---|
| Sources dans `sources/registry.yml` | 220 | Dénominateur source disponible |
| Relations dans `knowledge/graph.yml` | 629 | Graphe exploitable par parcours déterministe |
| Sources avec au moins une relation typée de contribution documentaire (SUPPORTS, QUALIFIES, INCLUDES, USES, CITES, TRANSCRIBES et inverse) | 165 / 220 (75 %) | Première mesure calculable de couverture du graphe ; 55 sources n'ont pas ce type de relation |
| Claims dans `claims/registry.yml` | 83 | Population mesurable |
| Statuts des claims | 52 `under_review`, 27 `partially_supported`, 1 `supported`, 3 `superseded` | Le champ canonique est `status`, pas `review_status` |
| Claims actifs avec conclusion épistémique explicite (`supported` ou `partially_supported`) | 28 / 80 (35 %) | KPI calculable, à nommer « Claims avec conclusion documentée » ; ne pas assimiler à une validation scientifique indépendante |
| Vérifications de sources enregistrées dans les claims | 30 entrées `source_checked` observées | Compter les claims concernés nécessite une agrégation par claim ; ne pas utiliser 30 comme numérateur de claims |
| Registre des synthèses | 25 dossiers distincts, 11 chemins de synthèse distincts | Relations plusieurs-dossiers-vers-une-synthèse intentionnelles ; dédupliquer les chemins, mais compter les dossiers pour la couverture |
| Éligibilité des dossiers | Aucun inventaire indépendant des dossiers actifs identifié dans cet audit | Un ratio de couverture calculé uniquement sur le registre des synthèses serait tautologique (25/25 par construction) |

## Conclusions par KPI candidat

### 1. Couverture des sources dans le graphe — calculable

Formule opérationnelle initiale :

`sources ayant au moins une relation typée de contribution documentaire / sources du registre`

Résultat de référence : **165 / 220 = 75 %**. Les relations `REL-ABOUT` seules sont exclues : elles signalent un thème, pas une contribution documentaire. Les relations comptées doivent avoir une justification non vide et des extrémités valides ; le prototype devra contrôler ces conditions et produire la liste des 55 sources sans relation retenue.

Cette mesure porte sur la présence d'un lien documentaire structuré, pas sur la qualité de la source ni sur la force probante du lien.

### 2. Claims avec conclusion documentée — calculable

Le schéma `schemas/claim.schema.json` impose `status` et autorise notamment `unexamined`, `under_review`, `supported`, `partially_supported`, `contested`, `not_supported`, `insufficient_evidence` et `superseded`.

Sur les 83 claims : 3 sont superseded ; parmi les 80 autres, 28 ont une conclusion explicite (`supported` ou `partially_supported`) et 52 sont `under_review`. Référence : **28 / 80 = 35 %**.

Ne pas appeler cela « taux de vérité » ni « vérification indépendante ». Les statuts `contested`, `not_supported` et `insufficient_evidence` devront également compter comme conclusions explicites si ces valeurs apparaissent. Les vérifications au niveau source (`source_verifications.status`) restent un diagnostic séparé.

### 3. Couverture des synthèses — partiellement calculable

`syntheses/registry.yml` fournit 25 associations dossier/synthèse, dont 11 chemins de synthèse distincts. Le registre est conçu comme la correspondance obligatoire des dossiers principaux, mais l'audit n'a pas identifié de registre indépendant permettant de connaître les dossiers actifs qui devraient y figurer.

Conclusion : l'intégrité des associations et l'existence des fichiers sont contrôlables ; un taux de couverture indépendant n'est pas défendable tant qu'un dénominateur externe au registre n'est pas défini. Le script `scripts/validate/check_synthesis_freshness.py` contrôle déjà plusieurs invariants de cohérence et d'existence ; réutiliser ce contrôle au lieu de le dupliquer.

### 4. Connectivité du graphe — diagnostic calculable, ratio non défendable en l'état

Le graphe possède des relations typées et justifiées, mais aucune règle générale ne définit quels types d'objets doivent nécessairement avoir au moins une relation. Un objet autonome ou référentiel peut légitimement être isolé.

Conclusion : produire des listes d'objets isolés et des contrôles de relations orphelines/incompatibles ; ne pas publier de pourcentage de connectivité avant d'avoir défini l'éligibilité par type d'objet.

## Ajustements de spécification requis

- Remplacer toute référence à `review_status` pour les claims par `status`.
- Ne pas présenter `source_verifications` comme un statut global du claim : c'est une liste de contrôles par source, avec sa propre taxonomie.
- Préciser que les liens `REL-ABOUT` seuls ne prouvent pas qu'une source est exploitée.
- Définir la couverture des synthèses comme non calculable en pourcentage tant qu'un dénominateur indépendant n'existe pas.
- Garder la connectivité en diagnostic, sans ratio agrégé.
- Dans chaque rapport, fournir les identifiants inclus, exclus, invalides et inconnus.

## Suite technique recommandée

1. Implémenter un script local en lecture seule pour le KPI 1 et le KPI 2, avec export JSON/Markdown.
2. Ajouter des tests unitaires pour relations sans justification, extrémités inconnues, relation `REL-ABOUT` seule, claims superseded, statuts inconnus et dénominateur nul.
3. Vérifier les 55 sources sans relation documentaire et distinguer les omissions réelles des sources de contexte ou des sources légitimement non mobilisées.
4. Déterminer si un inventaire léger des dossiers actifs existe déjà avant de proposer un mécanisme supplémentaire pour le KPI 3.
5. Mesurer le temps de calcul avant toute intégration CI ; aucun seuil de performance ou objectif de KPI arbitraire.

**Limite de l'audit :** les chiffres ci-dessus sont un instantané reproductible à partir des registres lus. Ils ne certifient pas la qualité scientifique des sources, des affirmations ou des relations.
