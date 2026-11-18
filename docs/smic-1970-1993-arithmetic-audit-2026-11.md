# Audit arithmétique et temporel du dataset SMIC 1970–1993

**Date :** 18 novembre 2026  
**Statut :** contrôle documentaire et arithmétique partiel ; les valeurs publiées ne sont pas recalculées ni remplacées.

## 1. Sources et périmètre du contrôle

Source principale : rapport d'information du Sénat, *Emploi et chômage des non-qualifiés en France*, annexe 2, sous-annexe 4 :
- tableau 2, « SMIC horaire brut de 1970 à 1993 », page imprimée 165 (page PDF 157) ;
- tableau 3, « Le glissement annuel du SMIC en juillet de 1970 à 1992 », page imprimée 166 (page PDF 158).

Le tableau 3 présente en réalité les observations datées de juillet 1970 à juillet 1993, avec une observation au 1er juin pour 1981. Les notes définissent les fenêtres : prix de mai à mai ; moitié du TSH réel d'avril à avril ; coup de pouce comme hausses au-delà de l'obligation légale.

## 2. Correction de l'alignement temporel

La colonne `period` du CSV utilisait auparavant des fenêtres décalées d'un an par rapport à la date d'observation. Le taux daté du 1er juillet 1970 et son glissement annuel de 11,1 % portent sur juillet 1969–juillet 1970, et non juillet 1970–juillet 1971.

Les libellés ont donc été réalignés :
- première ligne : `1969-1970`, observation au 1er juillet 1970 ;
- dernière ligne : `1992-1993`, observation au 1er juillet 1993 ;
- exception de calendrier : ligne `1980-1981`, observation au 1er juin 1981.

Aucune date d'effet ni valeur numérique n'a été modifiée. Le registre du dataset précise maintenant que `period` est la fenêtre de douze mois se terminant à `date_effective`.

## 3. Localisateurs ajoutés

Chaque ligne du CSV comporte désormais `source_locator`, qui pointe vers la ligne correspondante du tableau 3, page imprimée 166 / page PDF 158, avec la date d'effet exacte. Cela permet de remonter à l'observation précise plutôt que de s'en tenir à l'URL générale du rapport.

## 4. Contrôle de cohérence des composantes

Les colonnes `legal_obligation_pct` et `discretionary_boost_pct` ne doivent pas être additionnées mécaniquement. Une lecture multiplicative de diagnostic est :

`(1 + obligation / 100) × (1 + coup_de_pouce / 100) − 1`.

Sur les 24 lignes, cette combinaison reproduit de très près la variation observée pour la grande majorité des observations (écarts généralement inférieurs à 0,15 point). Elle ne doit toutefois pas être transformée en règle de validation absolue : les valeurs sont publiées arrondies au dixième et peuvent intégrer des séquences de revalorisations et conventions temporelles différentes.

### Écart restant à examiner : observation 1970

Pour la ligne datée du 1er juillet 1970 :
- variation publiée : 11,1 % ;
- obligation légale publiée : 8,0 % ;
- coup de pouce publié : 2,6 % ;
- combinaison multiplicative calculée sur ces valeurs arrondies : environ 10,81 %, soit un écart d'environ 0,29 point.

Cet écart est trop grand pour être expliqué par le seul arrondi au dixième. Les trois valeurs publiées sont conservées ; aucune correction n'est proposée. Il faut examiner la série détaillée des revalorisations du tableau 2, les dates exactes des hausses intermédiaires et la méthode de calcul de la décomposition avant toute conclusion.

Les autres petits écarts doivent également rester visibles et ne pas être forcés à zéro. Le contrôle est un test de cohérence, pas une preuve que les composantes sont strictement additives ou que la décomposition est homogène sur toute la période.

## 5. Limites et prochaines vérifications

1. Vérifier l'écart de 1970 à partir des revalorisations successives du tableau 2 et, si possible, de la série INSEE historique.
2. Auditer séparément les écarts signalés pour 1973 et 1981 avec le rapport du groupe d'experts SMIC de 2020 ; ne pas comparer des fenêtres ou dénominateurs différents.
3. Ajouter des contrôles automatisés : période cohérente avec la date d'effet, unicité des dates, présence du localisateur, identifiant source valide, valeurs numériques et unités attendues.
4. Conserver les chiffres publiés et les valeurs recalculées dans des champs distincts si des calculs dérivés sont ajoutés ultérieurement.

## 6. Fichiers concernés

- `data/smic-revaluations-1970-1993.csv` — fenêtres temporelles réalignées, localisateur par ligne, note de l'écart 1970.
- `research/datasets/registry.yml` — convention temporelle explicitée.
- `sources/smic-senate-1994-decomposition.yml` — source de référence inchangée ; ses limites et son statut de source primaire demeurent.
