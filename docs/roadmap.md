# Roadmap

## M0 — Fondations
- [x] Dépôt public créé.
- [x] README, charte, méthodologie, architecture et contribution intégrés.
- [x] Politique initiale des sources, licences et publication documentée.

**Sortie :** mission, périmètre, principes et architecture documentés.

## M1 — Modèle de connaissance
- [x] Taxonomie européenne initiale.
- [x] Référentiel territorial multiscalaire initial France–Europe–monde et Pays de la Loire–Île de Nantes ; validation approfondie des périmètres et métadonnées à poursuivre.
- [x] Conventions d'identifiants et de nomenclature.
- [x] Schémas Source, Study, Dataset, Claim, Hypothesis et Dossier (première version).
- [x] Registres initiaux pour sources, études, datasets, claims, hypothèses et dossiers.
- [x] Vocabulaire contrôlé de tags.
- [x] Ontologie légère des relations et registre initial du graphe.
- [x] Validation automatisée des schémas, identifiants, domaines, tags, références et types de relations (première version ; CI vérifiée sur la PR Éducation).
- [x] Premier cas réel initial reliant sources, études, données, affirmations, hypothèses et dossier (éducation / Parcoursup ; revue approfondie à poursuivre).
- [x] Page thématique Éducation reliant les objets et priorités de recherche.
- [x] Graphe enrichi pour relier les sources, études, jeux de données, affirmations et dossier au domaine Éducation.
- [ ] Ajouter progressivement les concepts et mécanismes réutilisables du domaine.

**Sortie :** un exemple relie les objets et passe les contrôles automatisés.

## M2 — Méthodes opérationnelles
- [x] Protocole initial d'ingestion des sources.
- [ ] Protocole de revue de littérature.
- [ ] Grille d'examen des études.
- [ ] Protocoles quantitatif, qualitatif et comparatif (généraux et réutilisables entre domaines).
- [x] Ajout des exigences de steelman, provenance des énoncés, vérification des passages et reproductibilité quantitative à la méthodologie.
- [x] Première extension rétrocompatible du schéma Claim (steelman, confiance argumentée, vérification des sources, provenance et historique de révision) ; validation complète sur les claims existants à confirmer par CI.
- [x] Registre Forecast initial et intégration de son schéma dans le validateur commun.
- [ ] Formaliser un registre structuré des incertitudes avec schéma dédié ; le modèle documentaire actuel reste non automatisé.
- [ ] Tester les exigences de revue et de vérification sur les dossiers TIG et Parcoursup.

**Sortie :** les méthodes réellement appliquées sont décrites et reproductibles autant que possible.

## M3 — Dossier pilote : Parcoursup et égalité des chances dans l'éducation
- [x] Question et périmètre initiaux.
- [x] Sources institutionnelles initiales et références comparatives.
- [x] Premiers jeux de données identifiés.
- [x] Premières affirmations et hypothèses enregistrées.
- [ ] Télécharger et analyser le CSV Parcoursup 2025 ; contrôler les dénominateurs et publier les sorties reproductibles.
- [ ] Constituer un corpus stratifié et coder les rapports CEV 2026.
- [ ] Études indépendantes et données de trajectoires post-admission.
- [ ] Comparaisons européennes approfondies.
- [ ] Synthèse contradictoire et recommandations.

## M4 — Dossier pilote : transition énergétique européenne
- [ ] Question et périmètre.
- [ ] Concepts et mécanismes.
- [ ] Sources institutionnelles et scientifiques.
- [ ] Jeux de données.
- [ ] Affirmations et hypothèses.
- [ ] Comparaisons européennes.
- [ ] Scénarios, arbitrages et synthèse contradictoire.

**Sortie :** dossier traçable, documenté et révisable.

## M5 — Validation inter-domaines

Le dossier éducation / Parcoursup constitue désormais le premier cas d'application du modèle. La validation inter-domaines portera sur les autres secteurs pour vérifier que la taxonomie et les schémas restent génériques.
- [ ] Finances publiques et dette.
- [ ] Immigration et intégration.
- [ ] IA et transformations du travail.

**Sortie :** modèles réutilisables entre domaines.

## M6 — Publication
- [ ] Configuration Quarto.
- [ ] Navigation par domaines.
- [ ] Pages de méthode et dossiers.
- [ ] Bibliographies et visualisations pertinentes.
- [ ] Workflow GitHub Pages.

**Sortie :** site accessible, compréhensible et aligné sur les contenus validés.

## M7 — Automatisation
- [ ] Ingestion assistée.
- [ ] Détection de doublons.
- [ ] Contrôle des références et du graphe.
- [ ] Extraction assistée des affirmations.
- [ ] Détection de contradictions potentielles.
- [ ] Exports de graphe et rapports de maintenance.
- [ ] Validation d'exemples Forecast et contrôle des règles de résolution.

**Sortie :** tâches répétitives assistées sans déléguer la validation intellectuelle à l'IA.

## M8 — Prévisions et évaluation rétrospective
- [x] Définition méthodologique d'une prévision probabiliste et du score de Brier.
- [x] Première version du schéma Forecast et registre YAML central contrôlé par la validation commune.
- [ ] Constituer un petit ensemble de prévisions datées, résolubles et non redondantes.
- [ ] Définir les règles de résolution et les cas indéterminés.
- [ ] Construire un bilan de calibration avec nombre de prévisions, horizons et base de comparaison.
- [ ] Évaluer les prévisions uniquement après leur échéance et conserver les versions initiales.

**Sortie :** un historique auditable de prévisions et de leurs résolutions, sans objectif artificiel de volume.

## Definition of Done

Un contenu est prêt lorsque son objectif est clair, ses sources sont identifiables, ses références vérifiables, ses limites explicites, ses relations cohérentes et les contrôles applicables passent. La création d'un fichier ou la génération d'un texte par IA ne suffit pas.
