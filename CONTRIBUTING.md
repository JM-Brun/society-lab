# Contribuer à Society Lab

Les contributions doivent améliorer la qualité, la traçabilité ou l'accessibilité des contenus.

## Avant de contribuer
- Lire [la charte](CHARTER.md) et [la méthodologie](METHODOLOGY.md).
- Vérifier qu'un objet similaire n'existe pas déjà.
- Préférer une amélioration ciblée à la création de doublons.

## Proposer une source
Fournir autant que possible titre, auteur ou organisme, date, URL originale ou DOI, type de document, périmètre géographique et temporel, méthode, limites et licence. Une source proposée n'est pas automatiquement validée.

## Proposer une affirmation ou une analyse
- Formuler précisément la proposition.
- Définir périmètre et termes.
- Relier les sources pertinentes.
- Signaler éléments contradictoires et limites.
- Distinguer constats, interprétations et jugements de valeur.

## Issues et suivi du travail

Toute nouvelle demande doit préciser son objectif, son contexte, ses dépendances, ses livrables et ses critères d'acceptation. Utiliser le [modèle d'issue](.github/ISSUE_TEMPLATE/task.md) et respecter la [gouvernance des issues](docs/issue-governance.md) ainsi que le [référentiel canonique des labels](governance/issue-labels.json). La priorité est confirmée par triage humain ; ne pas attribuer meta par défaut.

## Modifications
Les changements substantiels sont proposés par pull request. Les contrôles automatisés ne remplacent pas la revue du fond.

## IA
Les contributions assistées par IA sont acceptées si elles sont vérifiées. Le contributeur reste responsable de l'exactitude des références, citations, données et raisonnements.

## Droits et personnes
Ne pas publier de données personnelles non nécessaires, de documents confidentiels ou de contenus tiers en violation de leurs licences. Les désaccords portent sur les arguments et les méthodes, non sur les personnes.

## Vérifications locales avant revue

Ouvrir les travaux en cours en brouillon. Passer la PR en revue pour lancer les checks hébergés, dont les vérifications qui utilisent l’API GitHub.

```bash
python -m pip install PyYAML jsonschema
python scripts/validate/validate_registry.py
python scripts/validate/validate_markdown_links.py --strict
python -m unittest discover -s tests -p 'test_*.py'
quarto render site
python scripts/validate/validate_public_site.py
```

Inclure le rendu Quarto si la contribution modifie le site ou une synthèse publiée. Les tests SMIC et le rejeu du backlog sont inclus dans la suite `unittest`.
