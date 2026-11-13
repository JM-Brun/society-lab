# Architecture de Society Lab

## Objectif
Séparer les sources, les objets de connaissance, les travaux d'analyse et les publications. Le dépôt Git est la source de vérité ; le site Quarto est une vue éditoriale construite à partir des contenus sélectionnés.

## Couches logiques
1. **Evidence** : documents, publications, données et métadonnées de provenance. Les ressources tierces ne sont stockées que si leur licence, leur taille et leur nature le permettent.
2. **Knowledge & research** : concepts, institutions, mécanismes, études, affirmations, hypothèses, débats et analyses.
3. **Publication** : dossiers et pages éditorialisées, compréhensibles indépendamment et reliés aux sources.

## Arborescence cible
```text
society-lab/
├── README.md
├── CHARTER.md
├── METHODOLOGY.md
├── CONTRIBUTING.md
├── knowledge/
│   ├── TAXONOMY.yml
│   ├── concepts/
│   ├── institutions/
│   └── mechanisms/
├── sources/registry.yml
├── research/{studies,datasets}/
├── claims/registry.yml
├── hypotheses/
├── debates/
├── dossiers/
├── analysis/{quantitative,qualitative,notebooks}/
├── data/{metadata,processed,derived}/
├── schemas/
├── scripts/
├── tests/
├── docs/
└── site/
    ├── _quarto.yml
    ├── index.qmd
    ├── domains/
    ├── dossiers/
    ├── methods/
    └── assets/
```
Cette arborescence est une cible évolutive. Les répertoires seront créés lorsqu'un contenu ou un besoin les justifie.

## Objets fondamentaux
- Source : document ou ressource d'origine.
- Dataset : jeu de données et documentation.
- Study : recherche ou étude avec méthode identifiable.
- Claim : proposition précise susceptible d'être examinée.
- Hypothesis : explication proposée.
- Concept : notion ou mécanisme.
- Institution : organisme pertinent.
- Debate : désaccord structuré.
- Analysis : travail analytique documenté ou reproductible.
- Dossier : synthèse éditoriale transversale.

## Identifiants
Les identifiants sont sémantiques, stables, uniques et indépendants du chemin du fichier. Ils n'embarquent pas un verdict susceptible de changer.

Exemples : `DOMAIN-ENERGY`, `CONCEPT-PUBLIC-DEBT`, `ORG-EUROSTAT`, `SOURCE-IEA-WEO-2025`, `CLAIM-IMMIGRATION-FISCAL-BALANCE`, `DOSSIER-EUROPEAN-ENERGY-TRANSITION`.

Les collisions sont résolues par un suffixe distinctif documenté, jamais par la réutilisation d'un identifiant.

## Relations
Relations prévues : Study supports/contradicts/qualifies Claim ; Study uses Dataset ; Source published-by Institution ; Claim depends-on Hypothesis ; Concept explains Mechanism ; Dossier examines Claim et references Study ; Domain includes Concept.

Les relations doivent pointer vers des identifiants existants et seront validées automatiquement lorsque les registres seront implémentés.

## Données et reproductibilité
Conserver les données brutes uniquement lorsque leur licence, taille et conditions le permettent. Sinon, préférer métadonnées, scripts de téléchargement et instructions de reproduction. Documenter provenance, date d'extraction, transformations, unités et limites. Aucun secret ni donnée personnelle inutile dans Git.

## Publication Quarto
Le site est une projection éditoriale, pas une seconde source de vérité. La construction et le déploiement doivent échouer si les contrôles bloquants échouent.

## Automatisation
Contrôles prévus : validation YAML/JSON et schémas, unicité des identifiants, références internes, relations, tests d'analyse et construction Quarto. Ces contrôles ne certifient pas la qualité scientifique.
