# Registre des prévisions

Ce répertoire accueille les prévisions probabilistes de Society Lab, enregistrées avant leur échéance et résolues selon des règles définies à l'avance.

## Règles

- Une prévision est un objet distinct d'une hypothèse, d'un scénario ou d'une projection.
- Chaque prévision utilise un identifiant stable FORECAST-* et le contrat schemas/forecast.schema.json.
- La probabilité initiale, la date d'émission et l'échéance sont conservées.
- Toute révision est datée, motivée et ajoutée à l'historique.
- La résolution cite la source, la valeur observée et la règle appliquée.
- Les prévisions indéterminées ou retirées restent visibles et ne sont pas assimilées à des erreurs.
- Ne pas créer de prévisions uniquement pour augmenter le volume ou produire un score.

## Organisation

Créer une fiche par prévision, par exemple FORECAST-<DOMAINE>-<SUJET>.yml. Le nom de fichier doit rester stable. Les identifiants ne doivent pas contenir de données personnelles.

Voir la [méthodologie de prévision](../docs/forecasting.md) et le [schéma JSON](../schemas/forecast.schema.json).

## État initial

Aucune prévision n'est publiée dans cette première version. Le modèle et les règles sont préparatoires ; un premier lot ne sera créé qu'après définition d'événements résolubles et de sources de résolution adaptées.
