# Relais de session — audit de traçabilité et dataset SMIC

**Date :** 18 novembre 2026  
**Périmètre :** continuité du pilote quantitatif SMIC 1970–1993 et de l'audit du pipeline documentaire  
**Issue de coordination :** [#114 — Auditer et fiabiliser le pipeline complet d’ingestion et de production des connaissances](https://github.com/JM-Brun/society-lab/issues/114)

Ce document est un point de reprise pour une future session. Il distingue les constats déjà vérifiés, les hypothèses à tester et les travaux qui restent ouverts. Il ne vaut ni validation scientifique globale du dataset, ni clôture de l'audit du pipeline.

## 1. État confirmé au moment du relais

### 1.1 Dataset SMIC 1970–1993

Fichiers de référence :
- `data/smic-revaluations-1970-1993.csv`
- `research/datasets/registry.yml`
- `docs/smic-1970-1993-arithmetic-audit-2026-11.md`
- `docs/pilot-traceability-assessment-2026-11.md`
- `scripts/analysis/audit_smic_revaluations.py`
- `tests/test_smic_revaluations_audit.py`

Éléments déjà réalisés :
- Les périodes ont été réalignées sur les douze mois précédant la date d'effet : première observation `1969-1970` au 1er juillet 1970 ; dernière `1992-1993` au 1er juillet 1993 ; exception du 1er juin 1981.
- Les 24 lignes portent un localisateur vers la ligne correspondante du tableau 3.
- Le validateur contrôle notamment l'alignement période/date et la présence du localisateur.
- La lecture OCR litigieuse de juillet 1978 a été arbitrée visuellement : 10,85 F dans les tableaux 2 et 3. Aucune correction numérique n'était nécessaire.
- Les chiffres publiés n'ont pas été remplacés par des calculs dérivés.

### 1.2 Contrôle supplémentaire du tableau 2

Le PDF original du rapport sénatorial a été rouvert et la page du tableau 2 a été examinée visuellement :
- Tableau 2, page imprimée 165 (page PDF 157).
- Pour 1970, le tableau affiche 3,27 F au 1er janvier, 3,36 F au 1er avril et 3,50 F au 1er juillet.
- Il montre ainsi plusieurs dates de revalorisation au cours d'une année civile. Il faut donc distinguer la variation entre deux dates homologues (le glissement annuel du tableau 3) de la succession des hausses infra-annuelles.
- Cette observation ne résout pas, à elle seule, l'écart arithmétique de la ligne du 1er juillet 1970.

Source primaire : [rapport du Sénat, annexe 2, sous-annexe 4](https://www.senat.fr/rap/1993-1994/i1993_1994_0504.pdf), tableaux 2 et 3, pages imprimées 165–166 (pages PDF 157–158).

### 1.3 Écart de 1970 : toujours ouvert

Ligne du 1er juillet 1970 dans le tableau 3 :
- variation observée : 11,1 % ;
- obligation légale : 8,0 % ;
- coup de pouce : 2,6 % ;
- composition multiplicative exploratoire des deux composantes : environ 10,81 %.

L'écart d'environ 0,29 point ne peut pas être attribué au seul arrondi au dixième. Les chiffres sources restent inchangés. Ne pas présenter la composition multiplicative comme la formule officielle tant que la méthode historique et ses bases ne sont pas établies.

## 2. Travaux à reprendre — ordre recommandé

### Priorité 1 — Résoudre ou circonscrire l'écart 1970

1. Relever exactement dans le tableau 3 la définition et les notes associées à chaque colonne, y compris les dates de référence des indices.
2. Reconstituer indépendamment le glissement du SMIC entre juillet 1969 et juillet 1970 à partir de la série historique, en retrouvant explicitement le taux de juillet 1969 dans une source primaire.
3. Reconstituer séparément les composantes prix et moitié du TSH avec leurs fenêtres propres (prix mai-à-mai ; TSH réel avril-à-avril selon les notes du tableau), sans les supposer identiques à la fenêtre juillet-à-juillet du taux horaire.
4. Identifier la formule exacte utilisée par le rapport pour passer de ces composantes à l'obligation légale, puis au coup de pouce. Tester les bases et séquences de calcul ; ne pas choisir la formule qui « colle » simplement au résultat.
5. Comparer, si nécessaire, avec les séries historiques INSEE et documenter les différences de millésime, champ, date d'effet, indice et arrondi.
6. Conclure explicitement : écart expliqué, écart dû aux conventions, ou écart non réconciliable avec les sources accessibles. Dans tous les cas, garder les valeurs publiées et les calculs de contrôle dans des champs distincts.

### Priorité 2 — Réconcilier les épisodes 1973 et 1981 avec le rapport d'experts 2020

Pour chaque épisode :
- récupérer les graphiques/tableaux et leurs notes ;
- identifier la fenêtre exacte, la base, le dénominateur et la définition de « coup de pouce » ;
- distinguer hausse à une date donnée et glissement annuel ;
- contrôler si le rapport de 2020 reprend la même source ou une série recalculée ;
- ne pas traiter les écarts 9,7 % / 10,1 % (1973) et 5,2 % / 6,9 % (1981) comme des erreurs avant cette comparaison.

### Priorité 3 — Renforcer le pilote sans sur-ingénierie

- Vérifier les 24 lignes contre les pages originales, pas seulement la présence des localisateurs.
- Ajouter des tests de non-régression ciblés : nombre de lignes attendu, dates uniques et ordonnées, format des localisateurs, unités et bornes numériques plausibles.
- Si des calculs dérivés sont ajoutés, les stocker séparément des transcriptions publiées avec formule, paramètres, version du code et date d'exécution.
- Ne créer un schéma Extraction autonome que si plusieurs usages réels démontrent que `source_verifications` ne suffit pas.

### Priorité 4 — Poursuivre l'audit global de traçabilité

Dans l'issue #114 :
- compléter la matrice source → version → inspection → localisateur → extraction → étude/dataset → claim → relation de graphe → dossier/synthèse ;
- tester les références et liens orphelins sur des objets réels ;
- auditer la qualité des justifications des relations, pas seulement leur validité structurelle ;
- définir les événements de mise à jour, errata, rétractations et changements de version ;
- mesurer les performances sur un corpus représentatif avant toute décision d'architecture supplémentaire.

## 3. Garde-fous à conserver

- Ne jamais écraser une valeur publiée par un calcul dérivé.
- Ne pas confondre moyenne annuelle, taux à date d'effet et glissement annuel.
- Ne pas comparer des pourcentages sans vérifier période, population, unité, base et dénominateur.
- Ne pas inférer une causalité d'une décomposition comptable ou d'une concordance arithmétique.
- Ne pas promouvoir automatiquement le niveau de confiance d'une donnée parce que son format passe la validation.
- Ne pas lancer de migration de masse ni créer de schéma concurrent avant preuve du besoin.
- Documenter les désaccords et résultats nuls plutôt que de les lisser.

## 4. État CI connu

Sur le commit `5c5f82ff490d897bfa73cf38a8e9e57ec2afc8b5` :
- workflow **Validate knowledge base**, run [44304999120](https://github.com/JM-Brun/society-lab/actions/runs/44304999120) : `success` ;
- workflow **Secret scanning**, run [44304999292](https://github.com/JM-Brun/society-lab/actions/runs/44304999292) : `success`.

Ces résultats valident les contrôles automatisés exécutés sur ce commit, pas la totalité des extractions ni leur interprétation scientifique.

## 5. Point d'entrée pour la prochaine session

Commencer par le tableau 3 et ses notes, puis documenter explicitement les fenêtres distinctes :
- taux SMIC : juillet-à-juillet (ou juin 1980–juin 1981 pour l'observation de juin 1981) ;
- prix : mai-à-mai ;
- moitié du TSH réel : avril-à-avril.

Ensuite, rechercher le taux de juillet 1969 et refaire le calcul du glissement observé. Ne modifier aucun chiffre du CSV avant d'avoir identifié la méthode et les sources exactes. Mettre à jour ce relais et l'issue #114 avec les résultats, même si l'écart reste ouvert.
