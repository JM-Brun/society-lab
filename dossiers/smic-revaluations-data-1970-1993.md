# Reconstitution tabulaire des revalorisations du SMIC (1970–1993)

- **Identifiant :** DATASET-SMIC-REVALUATIONS-1970-1993
- **Date de constitution :** 14 novembre 2026
- **Données :** [CSV des revalorisations](../data/smic-revaluations-1970-1993.csv)
- **Statut :** transcription vérifiée du tableau historique du Sénat ; harmonisation avec les rapports ultérieurs encore nécessaire.

## 1. Source primaire de la série

Le tableau 3 du rapport d'information du Sénat n° 504 (seconde session ordinaire 1993–1994), intitulé « Le glissement annuel du SMIC en juillet de 1970 à 1992 », fournit pour 1970–1993 :
- le montant horaire brut en francs ;
- la hausse annuelle observée ;
- la contribution de l'évolution des prix ;
- la contribution de la moitié de l'évolution réelle du taux de salaire horaire (TSH) ;
- l'obligation légale calculée ;
- le coup de pouce résiduel au-delà de l'obligation légale.

La transcription du CSV reprend les valeurs publiées, sans recalcul ni correction des arrondis. Le rapport précise que les prix sont mesurés de mai à mai (hors tabac à partir de 1993), et que le demi-TSH est calculé d'avril à avril en francs constants. Source : Sénat, rapport n° 504, 1993–1994, tableau 3, p. 160 environ dans la pagination imprimée, lignes 4983–5024 de l'extraction textuelle : https://www.senat.fr/rap/1993-1994/i1993_1994_0504.pdf

## 2. Lecture des résultats

| Période | Hausse observée | Prix | 1/2 TSH | Obligation légale | Coup de pouce |
|---|---:|---:|---:|---:|---:|
| 1970–1971 | 11,1 % | 5,8 % | 2,1 % | 8,0 % | 2,6 % |
| 1972–1973 | 11,7 % | 5,4 % | 2,4 % | 8,0 % | 3,4 % |
| 1973–1974 | 20,9 % | 7,2 % | 2,8 % | 10,2 % | 9,7 % |
| 1974–1975 | 23,1 % | 13,5 % | 1,9 % | 15,6 % | 6,4 % |
| 1980–1981 | 15,2 % | 13,8 % | 0,4 % | 14,2 % | 0,9 % |
| 1981–1982 | 19,4 % | 12,7 % | 0,7 % | 13,5 % | 5,2 % |
| 1985–1986 | 9,2 % | 6,5 % | 0,0 % | 6,5 % | 2,6 % |
| 1986–1987 | 3,4 % | 2,3 % | 1,0 % | 3,4 % | 0,0 % |
| 1992–1993 | 2,3 % | 1,8 % | 0,5 % | 2,3 % | 0,0 % |

Les colonnes sont les valeurs de la source. Un contrôle arithmétique simple montre que les composantes prix + demi-TSH + coup de pouce ne reproduisent pas toujours le taux total : l'écart atteint 1,2 point en 1973–1974 et 1,3 point en 1974–1975. Il ne faut donc pas attribuer ces écarts aux seuls arrondis. Ils peuvent tenir aux conventions de calcul, aux bases successives et aux périodes de référence ; leur origine doit être réconciliée dans les sources méthodologiques avant tout recalcul. Le CSV conserve les chiffres publiés sans ajustement.

## 3. Un point de vigilance : les chiffres de 1973 et 1981

Le rapport du groupe d'experts de 2020 mentionne un coup de pouce maximal de 10,1 % en 1973 et de 6,9 % en 1981. Le tableau du Sénat de 1994 donne respectivement 9,7 % pour le glissement annuel de juillet 1973 et 5,2 % pour le glissement à la date du 1er juin 1981.

Ces chiffres ne doivent pas être fusionnés ni l'un considéré comme une erreur sans examen. Les dates de référence, la définition du « coup de pouce », les fenêtres d'indices et la méthode de décomposition peuvent différer. Le CSV conserve la mesure du Sénat, identifiée comme telle. La réconciliation avec le rapport 2020 est un travail séparé.

## 4. Limites d'interprétation

1. Il s'agit d'un glissement annuel à une date donnée, non de la variation moyenne annuelle du SMIC.
2. Les montants sont en francs courants ; ils ne constituent pas une série de pouvoir d'achat.
3. La mesure du TSH et les règles légales ont changé au fil du temps ; les valeurs ne peuvent pas être recalculées avec la formule contemporaine.
4. Les valeurs du tableau sont descriptives et ne permettent pas d'identifier les effets causaux des hausses sur l'emploi, les heures, les prix ou les marges.
5. Le tableau s'arrête en 1993. Les périodes suivantes nécessitent d'autres sources et une classification séparée des GMR, du changement de calendrier, des règles d'indexation et des revalorisations anticipées.

## 5. Synthèse opérationnelle

**Constat établi :** de 1970 à 1982, plusieurs revalorisations annuelles comportent des coups de pouce substantiels ; en 1973–1974, le tableau du Sénat chiffre celui-ci à 9,7 points, et en 1981–1982 à 5,2 points selon sa convention. À partir du milieu des années 1980, les coups de pouce recensés dans ce tableau sont faibles ou nuls.

**Ce que cela ne démontre pas :** que les hausses les plus fortes aient causé à elles seules la compression salariale, une hausse ou une baisse de l'emploi, ou une variation du niveau de vie des ménages.

**Prochaine étape :** harmoniser le tableau du Sénat avec le rapport du groupe d'experts 2020 et les séries INSEE des taux horaires ; reconstruire séparément les changements de taux infra-annuels et les années de transition institutionnelle après 1993.
