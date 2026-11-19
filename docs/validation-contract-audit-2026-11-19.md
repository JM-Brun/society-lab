# Audit ciblé des contrats de validation — 19 novembre 2026

## Portée et méthode

Audit en lecture seule du dépôt `JM-Brun/society-lab` sur la branche `main`, à partir des registres canoniques, du graphe YAML, des schémas JSON et du validateur. Les écarts de rapprochement sont des éléments à arbitrer, pas des erreurs automatiquement corrigibles.

## 1. PR #179 — intégration vérifiée

La PR [#179](https://github.com/JM-Brun/society-lab/pull/179) est **fusionnée** dans `main` par le commit `afe4c8cf15914c7fb8a1b13b1498b6154333aa52`.

Sur le commit de correction `8d91d66db81c18d147b97be4b2143155b23f7694`, les workflows déclenchés par la PR sont terminés avec succès :
- **Validate knowledge base** : succès ; job `validate`, dont tests unitaires et validation JSON Schema ;
- **Secret scanning** : succès.

Le statut combiné du commit de merge ne publie pas de statuts individuels (liste vide), mais les deux exécutions PR sont explicitement terminées avec `conclusion=success`. Les contrôles métier ajoutés détectent auto-parenté/cycles territoriaux et incohérences des inverses déclarés. Les inverses réservés non déclarés restent tolérés.

## 2. Taxonomies : slugs de domaines et groupes de tags

État observé :
- 15 domaines dans `knowledge/TAXONOMY.yml` ;
- 15 slugs présents, valides et uniques sans distinction de casse ;
- 38 tags dans `knowledge/TAGS.yml` ;
- six groupes utilisés : `method` (11), `evidence` (5), `status` (3), `lens` (6), `scale` (11), `horizon` (2).

Le validateur contrôlait déjà l'unicité des identifiants DOMAIN/TAG, mais pas l'unicité/forme des slugs ni l'appartenance des tags à un vocabulaire de groupes. Cette PR ajoute :
- une syntaxe de slug stable `^[a-z0-9]+(?:-[a-z0-9]+)*$` ;
- l'unicité des slugs sans distinction de casse ;
- une liste explicite des six groupes effectivement utilisés, avec rejet des groupes inconnus ou absents ;
- des tests positifs et négatifs.

Toute introduction d'un nouveau groupe doit donc être accompagnée d'une décision taxonomique, de sa documentation et d'un test. Aucun tag existant n'est renommé ni déplacé.

## 3. Références géographiques : inventaire et contrat proposé

### Constat mesuré

Les quatre registres portant actuellement le champ `geographic_scope` contiennent :
- sources : 183 fiches sur 220, 233 valeurs ;
- études : 62 sur 62, 97 valeurs ;
- jeux de données : 14 sur 14, 20 valeurs ;
- dossiers : 25 sur 25, 64 valeurs.

Soit **284 fiches, 414 valeurs et 50 libellés distincts**. Aucun de ces enregistrements ne contient actuellement d'identifiant `TERRITORY-*` dans les registres examinés.

Les valeurs mélangent plusieurs sémantiques :
- territoires administratifs ou lieux : France, Loire-Atlantique, Nantes, Nantes Métropole, Île de Nantes ;
- ensembles géographiques ou politiques : Europe, Union européenne, zone euro, international ;
- échantillons/comparateurs : 17 pays, 27 pays européens, comparateurs OCDE, OCDE ;
- unités administratives ou d'observation : académies, régions, départements, établissements ;
- territoires infranationaux ou systèmes juridiques distincts : Flandre, Wallonie, England and Wales, Scotland, Northern Ireland ;
- valeurs incertaines : « À préciser à partir du texte intégral », « Expérience d'enquête ; contexte à préciser dans le texte intégral ».

Ces valeurs ne sont donc ni toutes des territoires, ni toutes des périmètres administratifs, ni toutes convertibles vers le référentiel territorial.

### Contrat recommandé — sans migration immédiate

1. **Conserver `geographic_scope`** comme champ textuel historique, lisible et non destructif. Ne pas le remplacer par des identifiants.
2. Réserver les identifiants `TERRITORY-*` aux lieux/territoires explicitement représentés dans `knowledge/TERRITORIES.yml`. Un groupe de pays, une population, une juridiction, un échantillon, un comparateur ou une aire fonctionnelle ne devient pas automatiquement un territoire.
3. À terme, ajouter un champ facultatif distinct (par exemple `geographic_scope_ids`) dans les schémas concernés, en complément du texte. Il ne contiendrait que les correspondances exactes validées humainement ; les valeurs non résolues resteraient dans le champ textuel.
4. Distinguer dans la documentation le territoire étudié, la juridiction compétente, l'aire fonctionnelle, le territoire vécu et le groupe de comparaison. Le lien parent géographique ne doit pas servir à encoder une simple proximité ou une relation institutionnelle.
5. Procéder par lots : inventaire des libellés, proposition de correspondances, revue humaine, ajout des identifiants facultatifs, contrôle des références, puis seulement mesure de couverture. Garder les valeurs d'origine et journaliser toute normalisation.

**Décision :** aucune conversion automatique n'est effectuée dans cette PR. Le contrat doit être approuvé avant toute évolution des schémas ou des fiches.

## 4. Relations des fiches et arêtes du graphe

Le graphe contient **684 arêtes** : ABOUT 168, SUPPORTS 87, INCLUDES 326, USES 6, GEOGRAPHICALLY-WITHIN 7, CHILD-OF 8, SUMMARIZED-BY 8, TRANSCRIBES 21, SUMMARIZES 1, QUALIFIES 8 et CITES 44.

Le rapprochement des références explicites des dossiers avec les arêtes `REL-INCLUDES` donne :

| Références déclarées dans les dossiers | Paires déclarées | Paires présentes dans le graphe | Absentes du graphe | Paires du graphe non déclarées dans les fiches |
|---|---:|---:|---:|---:|
| `study_ids` | 45 | 38 | 7 | 10 |
| `claim_ids` | 49 | 40 | 9 | 22 |
| `hypothesis_ids` | 34 | 22 | 12 | 0 |
| `concept_ids` | 17 | 11 | 6 | 0 |
| **Total** | **145** | **111** | **34** | **32** |

Pour les études, 6 références `dataset_ids` sont déclarées ; 5 correspondent à une arête `REL-USES` étude → dataset.

Interprétation et garde-fous :
- ces champs de fiche et les arêtes sont deux représentations qui se recouvrent partiellement, pas nécessairement des duplications sémantiquement identiques ;
- `source_ids` sur une étude ou un claim n'implique pas à lui seul une arête `SUPPORTS` : la référence bibliographique ne prouve pas que la source étaye le claim ;
- les liens d'inclusion d'un dossier, l'utilisation d'un dataset et l'appui probatoire sont des relations différentes ;
- les 34 liens présents dans les fiches mais absents du graphe, les 32 liens du graphe absents des listes de fiches et le lien étude→dataset manquant doivent être arbitrés individuellement ;
- ne pas synchroniser automatiquement les deux côtés, ni supprimer les arêtes supplémentaires avant d'avoir identifié la source de vérité et le sens métier de chaque champ.

Le validateur actuel contrôle l'existence et le typage des arêtes, ainsi que plusieurs références croisées des fiches ; il ne garantit pas leur équivalence exhaustive. Le prochain livrable doit être une matrice de correspondance par champ et type de relation, avec exceptions justifiées et décision de source de vérité.

## 5. Contraintes conditionnelles des schémas

L'inspection des schémas montre des conditions métier dans :
- `schemas/mechanism.schema.json` : un mécanisme à statut probant (supported/mixed/challenged/rejected) doit fournir au moins un lien vers études ou claims ;
- `schemas/ingestion-batch.schema.json` : règles conditionnelles pour les décisions selected, duplicate, excluded, inaccessible, et pour la clôture d'un lot ;
- `schemas/forecast.schema.json` : aucune règle `if/then` ou `oneOf/anyOf` conditionnelle repérée ; les contraintes sont actuellement principalement structurelles et bornées.

Cette PR ajoute une suite de tests dédiée qui vérifie les cas valides et invalides des conditions mechanism et ingestion-batch, y compris chaque décision et le statut closed. Elle ne modifie pas les schémas ni les données.

## 6. Scalabilité ×10 / ×100

Le corpus de référence interrogé comprend 441 fiches dans les neuf registres canoniques (220 sources, 62 études, 14 datasets, 83 claims, 22 hypothèses, 25 dossiers, 15 concepts, 0 mécanisme et 0 forecast), plus 684 arêtes. Ces volumes sont le point de départ.

La PR ajoute `scripts/audit/benchmark_validation_scale.py`, exécuté par `tests/test_validation_scale_benchmark.py` sur les facteurs ×1, ×10 et ×100. Le script :
- clone les objets avec des identifiants uniques et remappe leurs références internes ;
- conserve les taxonomies partagées et évite de dupliquer les arêtes territoriales statiques ;
- exécute les validations de schémas, d'identifiants, de références croisées et d'arêtes sur les corpus synthétiques ;
- rapporte le nombre de fiches/arêtes, le temps de construction du corpus synthétique, le temps de validation, le temps total et le pic mémoire Python.

**Limite de mesure :** le benchmark couvre la validation des registres et du graphe en mémoire ; il ne mesure pas la génération du site, les appels externes, ni la qualité scientifique. Les chiffres seront ceux du runner GitHub Actions et doivent être interprétés comme un benchmark comparatif reproductible, non comme une mesure universelle.

Les premières mesures de CI restent à relever sur le nouveau commit. Les seuils de régression seront définis après observation des rapports ×1/×10/×100, et non fixés arbitrairement.
