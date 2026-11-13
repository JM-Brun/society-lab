# Prototype de microsimulation du SMIC avec OpenFisca-France

- **Dossier parent :** [Augmenter le SMIC en France](../dossiers/smic-france-tradeoffs.md)
- **Socle empirique :** [Revue des travaux économiques existants](../dossiers/smic-economists-literature-review.md)
- **Cadre de comparaison :** [Scénarios de politique publique](../dossiers/smic-policy-scenarios.md)
- **Statut :** prototype technique reproductible ; validation métier et audit des résultats encore requis
- **Version initiale :** 13 novembre 2026

## 1. Place de cet outil dans la recherche

**OpenFisca n'est pas le point de départ de l'analyse du SMIC.** Le dossier s'appuie d'abord sur les études empiriques, les rapports d'économistes, les évaluations de politiques passées et les comparaisons internationales déjà publiées. Voir la [revue des travaux économiques](../dossiers/smic-economists-literature-review.md).

Le prototype intervient uniquement en complément, pour calculer les conséquences mécaniques de règles socio-fiscales sur des cas-types définis. Il ne permet pas d'identifier les effets causaux d'une hausse du SMIC sur l'emploi, les prix, les heures travaillées, les marges ou la productivité. Il ne remplace donc ni les évaluations empiriques ni les modèles économiques publiés.

Avant d'ajouter une simulation, formuler la question non résolue par la littérature, expliquer pourquoi un calcul existant ne suffit pas, et préciser la valeur ajoutée attendue. Si la littérature répond déjà à la question, la synthèse critique de ces travaux est préférable à une nouvelle simulation.

## 2. Cas-types et conventions actuelles

Le prototype contient quatre cas-types : personne seule à temps plein au SMIC ; parent isolé à 80 % ; couple avec un salarié au SMIC et un second à 80 % avec un enfant ; couple avec deux salariés à temps plein au SMIC.

Chaque cas est comparé sous une référence et des hausses brutes hypothétiques de 1 %, 3 % et 5 %. Le calcul annuel est une **année-type annualisée** : le salaire mensuel de référence observé depuis juin 2026 est appliqué aux douze mois de l'année de législation 2026 pour comparer des situations stabilisées. Il ne reconstitue pas le revenu effectivement perçu en 2026. Les scénarios de hausse sont des variations de salaires saisies dans les situations, pas une modification de la loi sur le SMIC.

## 3. Exécution reproductible

Installer le paquet officiel :

```bash
python -m pip install -r requirements-openfisca.txt
python tools/smic_openfisca.py
```

Exemple :

```bash
python tools/smic_openfisca.py --gross-monthly-smic 1867.02 --uplifts 0 2 4 6
```

Le programme émet un JSON avec les versions exactes d'OpenFisca-France et d'OpenFisca-Core, les conventions d'annualisation, le salaire brut du ménage, le revenu disponible annuel et son équivalent mensuel, ainsi que l'écart au scénario de référence. Le scénario de référence à 0 % est calculé même s'il n'est pas explicitement demandé.

Tests de structure :

```bash
python -m unittest discover -s tests -p "test_smic_openfisca.py"
```

## 4. Hypothèses et limites

- La référence de 1 867,02 € brut mensuels correspond au SMIC mensuel brut de 35 heures en France hors Mayotte depuis le 1er juin 2026 ; elle devra être actualisée pour toute autre année.
- Les dates de naissance sont des hypothèses de cas-types, pas des caractéristiques de personnes réelles.
- OpenFisca-France est figé à la version 176.1.7 ; la version effective d'OpenFisca-Core est enregistrée dans la sortie JSON.
- Le modèle applique une hausse proportionnelle aux salaires bruts saisis. Il ne modifie pas les minima conventionnels, les salaires des personnes non concernées ni les grilles.
- Les situations ne sont pas représentatives et ne permettent pas d'estimer combien de personnes gagnent ou perdent à l'échelle nationale.
- Les loyers, autres ressources, patrimoine, frais de garde et paramètres individuels non renseignés ne sont pas connus. Les sorties doivent être auditées avant tout usage substantiel.
- Vérifier les prestations effectivement activées, notamment prime d'activité, aides au logement, fiscalité et prestations familiales.
- Aucune réaction comportementale ou macroéconomique n'est modélisée : emploi, heures, prix, productivité, marges et réactions des entreprises ou ménages.
- Le prototype ne produit donc aucun résultat sur l'emploi, la pauvreté nationale, l'inflation ou le coût macro-budgétaire.

**Règle de publication :** ne publier aucun chiffre avant d'avoir exécuté le script dans un environnement identifié, vérifié les variables calculées, contrôlé les hypothèses et conservé les sorties reproductibles.

## 5. Critère d'utilisation future

Une extension du prototype ne sera justifiée que si les quatre conditions suivantes sont réunies :

1. Une question précise reste ouverte après examen de la littérature existante.
2. Les variables nécessaires sont disponibles et correctement documentées dans OpenFisca-France.
3. La simulation apporte une information complémentaire identifiable, et non une simple répétition d'un résultat publié.
4. Les résultats sont présentés comme des calculs conditionnels de cas-types, avec sensibilité et limites, et confrontés aux résultats empiriques publiés.

Les questions de comportement des entreprises, d'emploi, de prix et de productivité nécessitent des données et des méthodes économétriques ou structurelles adaptées ; elles ne doivent pas être ajoutées artificiellement au prototype statique.

## 6. Sources techniques

- [Dépôt officiel OpenFisca-France](https://github.com/openfisca/openfisca-france)
- [OpenFisca-France 176.1.7 sur PyPI](https://pypi.org/project/OpenFisca-France/176.1.7/)
- [Documentation OpenFisca — exécuter une simulation](https://openfisca.org/doc/simulate/run-simulation.html)
- [Documentation OpenFisca — API Python](https://openfisca.org/doc/openfisca-python-api/simulations.html)

Le code et les règles du modèle évoluent : toute réplication doit figer la version utilisée.