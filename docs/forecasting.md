# Prévisions probabilistes

## Objet

Une prévision est une proposition datée portant sur une issue future observable, assortie d'une probabilité et d'une règle de résolution. Elle permet d'évaluer rétrospectivement la calibration des anticipations de Society Lab.

Elle ne doit pas être confondue avec :
- une **hypothèse**, qui propose un mécanisme explicatif ;
- un **scénario**, qui décrit une trajectoire conditionnelle ;
- une **projection**, qui prolonge un modèle sous des hypothèses données ;
- une **recommandation**, qui exprime un choix d'action.

## Conditions d'admission

Avant publication, une prévision doit avoir :
1. une question non ambiguë et suffisamment circonscrite ;
2. un événement ou indicateur observable, avec unité, population, territoire et période ;
3. une probabilité entre 0 et 1 ;
4. une date d'émission et une échéance ;
5. une règle de résolution définissant les cas positifs, négatifs et indéterminés ;
6. une source de résolution crédible, idéalement primaire ;
7. une justification, les hypothèses et, si possible, une classe de référence.

Éviter les formulations élastiques (« probablement », « significativement », « dans un avenir proche ») sans seuil ni horizon définis.

## Versionnement et intégrité

La probabilité initiale est conservée. Une mise à jour ne remplace jamais silencieusement une prévision antérieure : elle ajoute une entrée datée à l'historique. Les révisions doivent expliquer les nouvelles informations qui les motivent. Une prévision ne peut être modifiée rétroactivement pour mieux correspondre au résultat.

Les prévisions abandonnées, devenues impossibles à résoudre ou rendues obsolètes par un changement de définition sont marquées comme telles et accompagnées d'une explication. Elles ne sont pas arbitrairement comptées comme fausses.

## Résolution

La résolution intervient à l'échéance ou lorsque la règle définie est satisfaite. Le résultat est :
- open : elle n'est pas encore résolue ;
- resolved_true : l'événement défini s'est produit ;
- resolved_false : l'événement défini ne s'est pas produit ;
- indeterminate : les données ou la définition ne permettent pas de trancher ;
- withdrawn_superseded : la prévision a été retirée ou remplacée selon une règle documentée.

La source, la date, la valeur observée et l'application de la règle doivent être consignées.

## Évaluation

Pour un événement binaire, le score de Brier est :

\[
BS = \frac{1}{N}\sum_{i=1}^{N}(p_i-o_i)^2
\]

où p_i est la probabilité enregistrée et o_i vaut 1 si l'événement se produit et 0 sinon. Le score moyen varie de 0 (prévisions parfaites) à 1 (erreurs maximales) ; plus bas est meilleur.

Ne calculer le score que sur les prévisions résolues selon des règles fixées à l'avance. Publier avec le score :
- le nombre de prévisions et la part exclue comme indéterminée ;
- les horizons et familles de questions ;
- la distribution des probabilités ;
- une comparaison à une base simple ou classe de référence lorsque possible ;
- des diagnostics de calibration et de résolution.

Ne pas agréger sans précaution des événements fortement dépendants, des horizons ou des difficultés très différents. Un score sur un petit échantillon est très incertain. La calibration nécessite un ensemble suffisamment large de prévisions comparables ; elle ne se déduit pas d'un cas isolé.

## Publication

Les prévisions ouvertes peuvent être publiées avec leur incertitude et leurs limites. Le site ne doit pas afficher un classement ou un score global tant que le volume et la comparabilité des prévisions ne permettent pas une interprétation raisonnable.

Voir le [schéma Forecast](../schemas/forecast.schema.json) et la [méthodologie générale](../METHODOLOGY.md).
