# Audit de cohérence de la chronologie SMIC 1994–2026

- **Dataset audité :** [CSV événementiel](../data/smic-revaluations-1994-2026.csv)
- **Périmètre :** 42 lignes d'événements, du 1er juillet 1994 au 1er juin 2026.
- **Date de contrôle :** 15 novembre 2026.
- **Nature du contrôle :** cohérence interne des taux, dates, variations publiées et catégories ; ce contrôle ne remplace pas la vérification de chaque valeur dans le texte réglementaire ou la série source.

## Synthèse

Le CSV comporte 42 événements et conserve 2025 comme une année sans changement du taux horaire (11,88 €), plutôt que de créer une fausse ligne de revalorisation. Les catégories ont été normalisées pour les hausses mixtes de 1995, 1997 et juillet 2012 : elles comprennent une composante automatique et une composante discrétionnaire, et ne sont donc pas des coups de pouce « purs ».

Les pourcentages du CSV sont les variations publiées ou documentées par les sources, arrondies selon leurs conventions. Ils ne doivent pas être remplacés mécaniquement par le ratio des montants horaires affichés, eux-mêmes arrondis au centime. Le ratio recalculé à partir des montants affichés sert uniquement de contrôle de cohérence.

## Contrôles réalisés

1. **Structure :** 10 colonnes attendues sur chaque ligne ; 42 événements ; dates triées chronologiquement.
2. **Taux :** valeurs numériques positives et dates d'effet uniques.
3. **Variations :** comparaison du pourcentage documenté au ratio calculé entre taux affichés consécutifs. Un écart peut provenir des arrondis, d'une base réglementaire non arrondie ou d'un périmètre de comparaison distinct ; il doit être expliqué avant toute correction.
4. **Taxonomie :** distinction entre indexation annuelle, déclenchement automatique infra-annuel, coup de pouce intégré à une hausse, convergence GMR et changement de calendrier.
5. **2025 :** absence de hausse conservée comme information de période dans les notes du dossier ; aucune ligne événementielle artificielle ajoutée.

## Écarts de pourcentage à examiner

Le tableau ci-dessous liste les écarts supérieurs à 0,06 point entre le pourcentage de source et le ratio calculé à partir des montants horaires arrondis du CSV.

| Date | Variation documentée (%) | Ratio des taux affichés (%) | Écart (point) |
|---|---:|---:|---:|
| 1999-07-01 | 1.24 | 1.305 | -0.065 |

Cet écart est expliqué par le passage francs/euros : 40,22 F à 40,72 F correspond à +1,24 %, tandis que le ratio de 6,13 € à 6,21 € est affecté par l'arrondi des deux montants convertis. Le contrôle confirme l'intérêt de conserver les taux dans leur unité source, ou les valeurs non arrondies, lorsque l'on recalcule des variations historiques.

## Taxonomie retenue

- `ordinary_annual` : revalorisation selon la formule annuelle, sans coup de pouce identifié dans la source consultée.
- `ordinary_annual_with_discretionary_boost` : hausse comprenant indexation et composante discrétionnaire.
- `automatic_inflation_trigger` : déclenchement infra-annuel automatique lié au seuil d'inflation.
- `gmr_convergence` : convergence des garanties mensuelles de rémunération après la réforme des 35 heures.
- `calendar_change` : événement lié au déplacement de la date annuelle de revalorisation.
- Les hausses mixtes ne sont pas étiquetées comme un coup de pouce intégral : seule la fraction discrétionnaire documentée doit être interprétée comme telle.

## Limites et suite

- Le CSV est une chronologie des événements de taux, pas une série complète des minima applicables pendant la coexistence des GMR.
- Les contributions de l'indexation et du coup de pouce doivent rester séparées des variations de taux total.
- Les taux horaires ne mesurent ni le pouvoir d'achat annuel des personnes, ni le revenu disponible des ménages, ni les effets sur l'emploi.
- La prochaine validation doit rapprocher les valeurs du CSV avec les séries mensuelles INSEE et les tableaux DARES / rapports institutionnels, puis construire une série annuelle en euros constants et une table de correspondance des GMR.

## Conclusion opérationnelle

Le dataset est exploitable comme chronologie événementielle provisoire, à condition de conserver ses conventions, ses sources et ses limites. Il ne doit pas encore être utilisé comme variable causale brute dans une régression : les ruptures institutionnelles, les dates infra-annuelles, les minima GMR et les changements de formule nécessitent une préparation distincte.
