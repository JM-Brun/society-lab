# Cadre d'analyse territoriale multiscalaire

## Finalité

Society Lab est d'abord attentif aux réalités françaises, sans isoler la France des systèmes européens, internationaux et mondiaux dont elle dépend. L'analyse doit aussi pouvoir descendre jusqu'aux territoires vécus et aux projets urbains locaux. Le référentiel des niveaux est maintenu dans [TERRITORIES.yml](../knowledge/TERRITORIES.yml).

## Les neuf repères territoriaux

| Niveau | Périmètre | Questions typiques |
|---|---|---|
| Mondial | Monde | Quelles dynamiques planétaires ou systémiques structurent le phénomène ? |
| International | Relations transnationales | Quels flux, accords, organisations et réseaux relient les territoires ? |
| Européen | Europe, dont UE | Quelles institutions, normes, politiques et comparaisons européennes interviennent ? |
| National | France | Quel rôle jouent l'État, le droit, les politiques et les dynamiques nationales ? |
| Régional | Pays de la Loire | Quelles stratégies et disparités régionales ? |
| Départemental | Loire-Atlantique | Quelles compétences, solidarités, infrastructures et politiques départementales ? |
| Métropolitain | Nantes Métropole | Quels systèmes et arbitrages intercommunaux ? |
| Municipal | Nantes | Quels choix municipaux et effets à l'échelle de la commune ? |
| Infra-urbain | Île de Nantes | Comment les politiques et transformations se traduisent-elles dans les usages et les lieux ? |

Ces niveaux servent à orienter la recherche, pas à imposer une structure uniforme. Le niveau international est transversal. Les périmètres européens varient selon qu'il s'agit de l'UE, du Conseil de l'Europe, de l'EEE ou de l'Europe géographique. L'Île de Nantes n'est pas une collectivité et Nantes Métropole n'est pas la commune de Nantes.

## Trois directions d'analyse

### 1. Contextualisation descendante

Partir des mécanismes globaux ou européens pour examiner leurs effets, relais et médiations en France et dans les territoires locaux. Identifier les mécanismes concrets : réglementation, financement, commerce, prix, migrations, infrastructures, normes, chaînes d'approvisionnement, transferts technologiques ou contraintes écologiques.

### 2. Contextualisation ascendante

Partir d'observations locales pour comprendre comment une transformation est vécue, adaptée, contestée ou mise en œuvre. Les résultats locaux peuvent révéler des mécanismes négligés, invalider une généralisation trop rapide ou contribuer à une comparaison plus large. Ne jamais supposer qu'un cas local est représentatif sans stratégie d'échantillonnage ou justification.

### 3. Relations latérales et rétroactions

Étudier les liens entre territoires qui ne sont pas simplement emboîtés : villes comparables, réseaux de recherche, bassins d'emploi, flux logistiques, coopérations, bassins versants, chaînes de valeur et réseaux associatifs. Documenter aussi les boucles de rétroaction : une initiative locale peut influer sur des politiques métropolitaines, régionales ou nationales, voire être reprise ailleurs.

## Métadonnées territoriales à distinguer

Pour chaque étude, dataset, claim, analyse ou dossier, préciser selon la pertinence :

- `territory_ids` : territoires de référence du référentiel ;
- `observation_geography` : lieu ou périmètre où les observations sont produites ;
- `jurisdiction_ids` : juridictions et autorités compétentes ;
- `functional_geographies` : bassins d'emploi, de mobilité, réseaux, bassins versants ou autres espaces fonctionnels ;
- `comparison_territory_ids` : territoires de comparaison ;
- `geographic_coverage_note` : limites, exclusions, changements de périmètre et précautions.

Ne pas créer tous ces champs lorsqu'ils ne sont pas utiles ; les schémas propres aux objets restent applicables. Un territoire concerné n'est pas nécessairement l'autorité qui décide, et le lieu de collecte n'est pas nécessairement l'espace affecté.

## Règles de raisonnement

1. Préciser la période : les périmètres, compétences et politiques évoluent.
2. Ne pas confondre corrélation spatiale, influence, causalité et simple contexte.
3. Expliciter les médiations institutionnelles, économiques, sociales ou écologiques.
4. Ne pas agréger des données de niveaux différents sans expliquer les unités, dénominateurs et effets d'échelle.
5. Signaler les effets de composition et les biais liés aux frontières administratives (dont le problème des unités spatiales modifiables).
6. Comparer des territoires avec des définitions, périodes et populations compatibles.
7. Distinguer les faits observés, mécanismes supposés, interprétations et recommandations.
8. Mobiliser le contexte mondial pour éclairer le local, et le local pour éprouver les explications générales, sans réduire l'un à l'autre.

## Exemple : une question sur le logement à Nantes

Une analyse robuste pourrait examiner simultanément les usages et projets sur l'Île de Nantes, les politiques de la commune, les leviers de Nantes Métropole, les marchés et politiques du département et de la région, les cadres nationaux du logement, les politiques européennes pertinentes et les tendances macroéconomiques ou énergétiques mondiales. Chaque lien doit être justifié : cette liste n'implique pas que tous les niveaux expliquent chaque variation locale.

## Principe de prudence

La présence d'un niveau dans le référentiel ne signifie ni que les données y sont disponibles, ni que ce niveau est pertinent pour chaque dossier. Le périmètre doit être choisi à partir de la question de recherche et de la disponibilité de preuves adaptées.
