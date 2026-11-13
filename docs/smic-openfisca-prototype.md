# Prototype de microsimulation du SMIC avec OpenFisca-France

- **Dossier parent :** [Augmenter le SMIC en France](../dossiers/smic-france-tradeoffs.md)
- **Cadre de comparaison :** [Scénarios de politique publique](../dossiers/smic-policy-scenarios.md)
- **Statut :** prototype renforcé ; exécution intégrée à un workflow dédié, validation métier encore requise
- **Version initiale :** 13 novembre 2026

## 1. Objectif et périmètre

Ce prototype prépare une comparaison statique de cas-types de ménages sous plusieurs hypothèses de hausse du salaire brut au voisinage du SMIC. Il s'appuie sur le moteur de règles socio-fiscales OpenFisca-France plutôt que sur un coefficient brut-net forfaitaire.

Cas-types de la première version :

- personne seule travaillant à temps plein au SMIC ;
- parent isolé travaillant à 80 % ;
- couple avec un salarié au SMIC et un second salarié à 80 % du SMIC, avec un enfant ;
- couple avec deux salariés à temps plein au SMIC.

Chaque cas est comparé sous une référence et des hausses brutes hypothétiques de 1 %, 3 % et 5 %. Le calcul annuel est une **année-type annualisée** : le salaire mensuel de référence observé depuis juin 2026 est appliqué aux douze mois de l'année de législation 2026 pour comparer des situations stabilisées. Il ne reconstitue pas le revenu effectivement perçu en 2026, puisque le SMIC a évolué en cours d'année. Cette convention est un scénario de régime constant, pas une photographie historique. Le résultat visé est le revenu disponible annuel du ménage, puis son équivalent mensuel. Les scénarios de hausse sont des variations de salaire saisies dans les situations, pas une modification de la loi sur le SMIC.

## 2. Exécution

Installer le paquet officiel :

```bash
python -m pip install -r requirements-openfisca.txt
python tools/smic_openfisca.py
```

Exemple avec une autre valeur de référence et d'autres scénarios :

```bash
python tools/smic_openfisca.py --gross-monthly-smic 1867.02 --uplifts 0 2 4 6
```

Le programme émet un objet JSON contenant les versions exactes d'OpenFisca-France et d'OpenFisca-Core, les conventions d'annualisation, puis une ligne par ménage et par scénario. Chaque ligne fournit le salaire brut du ménage, le revenu disponible annuel et mensuel équivalent, ainsi que l'écart au scénario de référence du même ménage. Le scénario de référence à 0 % est calculé même s'il n'est pas explicitement demandé. Les tests des structures d'entrée, indépendants de l'installation d'OpenFisca, s'exécutent avec :

```bash
python -m unittest discover -s tests -p "test_smic_openfisca.py"
```

## 3. Hypothèses explicites et précautions

- La référence de 1 867,02 € brut mensuels correspond au SMIC mensuel brut de 35 heures en France hors Mayotte depuis le 1er juin 2026. Elle est paramétrable en ligne de commande et devra être actualisée pour toute année ultérieure.
- Les dates de naissance sont maintenant explicites : adultes nés en 1985/1987 et enfant né en 2018. Ces dates sont des hypothèses de cas-type, à faire varier en sensibilité ; elles ne décrivent aucune personne réelle.
- Le paquet OpenFisca-France est figé dans `requirements-openfisca.txt` à la version 176.1.7 ; la version d'OpenFisca-Core effectivement résolue est enregistrée dans la sortie JSON.
- Le modèle applique une hausse proportionnelle aux salaires bruts saisis. Il ne modifie pas le paramètre légal du SMIC, les minima conventionnels, les salaires des personnes non concernées ni les grilles salariales.
- Les situations sont des cas-types, pas un échantillon représentatif. Elles ne permettent pas d'estimer combien de personnes gagnent ou perdent à l'échelle nationale.
- Les autres ressources, loyers, patrimoine, frais de garde, situation détaillée d'activité et paramètres individuels non renseignés ne doivent pas être interprétés comme des caractéristiques réelles. Les sorties doivent être auditées avant toute utilisation substantielle.
- Le revenu disponible OpenFisca dépend du périmètre et des conventions du modèle. Il faut vérifier les variables et prestations effectivement activées pour l'année choisie, notamment les conditions d'ouverture de la prime d'activité, les aides au logement, la fiscalité et les prestations familiales.
- Une microsimulation statique ne modélise ni destruction/création d'emplois, ni réduction des heures, ni répercussion sur les prix, ni changement de productivité, ni réaction des entreprises ou des ménages.
- Le prototype ne produit donc aucun résultat sur l'emploi, la pauvreté nationale, l'inflation, le coût macro-budgétaire ou le comportement des employeurs.

**Règle de publication :** ne publier aucun chiffre de résultat avant d'avoir exécuté le script dans un environnement identifié, vérifié les variables calculées, contrôlé les hypothèses et conservé la version exacte d'OpenFisca-France ainsi que les sorties reproductibles.

## 4. Prochaines étapes de validation

1. Exécuter le script avec la version OpenFisca-France figée ; archiver les versions Python, OpenFisca-Core et OpenFisca-France.
2. Vérifier les entrées et les sorties par comparaison avec les exemples et tests officiels du modèle.
3. Ajouter des dates de naissance, heures, statut d'activité, logement, loyers, autres revenus et paramètres familiaux documentés ; contrôler la prime d'activité et les aides au logement.
4. Distinguer revenu individuel, revenu disponible du ménage, niveau de vie par unité de consommation et taux marginal effectif.
5. Ajouter les profils de reprise d'emploi et d'horaires variables seulement lorsque les revenus de remplacement et les périodes de référence sont correctement paramétrés.
6. Construire ensuite un module séparé de coût employeur et de cotisations, puis une couche d'analyse de sensibilité.

## 5. Sources techniques

- [Dépôt officiel OpenFisca-France](https://github.com/openfisca/openfisca-france) : modèle français, exemples de situations et API publique.
- [OpenFisca-France 176.1.7 sur PyPI](https://pypi.org/project/OpenFisca-France/176.1.7/) : version utilisée pour le premier environnement reproductible.
- [Documentation OpenFisca — exécuter une simulation](https://openfisca.org/doc/simulate/run-simulation.html) : construction des situations et calculs.
- [Documentation OpenFisca — API Python des simulations](https://openfisca.org/doc/openfisca-python-api/simulations.html) : `SimulationBuilder` et `Simulation.calculate`.
- [Documentation OpenFisca — limites de la microsimulation](https://openfisca.org/doc/) : le moteur calcule les règles modélisées mais ne prédit pas les réactions comportementales.

La version du modèle doit être figée au moment de la réplication : le dépôt OpenFisca-France évolue et une même situation peut produire des résultats différents selon la législation et le code chargés.
