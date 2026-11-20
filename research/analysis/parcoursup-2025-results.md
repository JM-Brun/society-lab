# Parcoursup 2025 — résultats descriptifs par formation

**Exécution du 20 novembre 2026.** Analyse du jeu ministériel `fr-esr-parcoursup`, campagne du 15 janvier au 10 septembre 2025, hors apprentissage. L'unité d'observation est une formation dans un établissement. Le jeu public associe des agrégats à chaque formation et les sommes de vœux portent sur des comptes par formation. [Protocole](parcoursup-2025-protocol.md) · [Issue #2](https://github.com/JM-Brun/society-lab/issues/2).

## Export et contrôle du schéma

Le [catalogue du ministère](https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-parcoursup) et l'export analysé comptent **14 252 lignes et 118 colonnes**. La [notice méthodologique](https://data.enseignementsup-recherche.gouv.fr/api/datasets/1.0/fr-esr-parcoursup/attachments/methodologie_opendata_2025pdf/) annonce 115 variables et 14 252 enregistrements. Le [portail interministériel](https://www.data.gouv.fr/datasets/parcoursup-2025-voeux-de-poursuite-detudes-et-de-reorientation-dans-lenseignement-superieur-et-reponses-des-etablissements) signale une mise à jour le 9 mars 2026 ayant complété le taux d'accès et le rang pour certaines formations. Les sept champs officiels ci-dessous figurent dans l'en-tête contrôlé. Ces constats ne suffisent pas à reconstituer les changements de colonnes entre les versions.

| Élément | Valeur vérifiée |
|---|---|
| Téléchargement UTC | 2026-11-20 à 08:36:39 |
| Taille | 12 880 730 octets |
| SHA-256 | `1feded562330eb353b1522a163f7cf090acdd14091d911e0425045a4f4ef6d06` |
| Format | UTF-8 avec BOM, séparateur point-virgule |
| Session et identifiants | 2025 sur toutes les lignes, 14 252 identifiants `cod_aff_form` renseignés et distincts |
| Valeurs manquantes | Aucune pour les 21 compteurs analysés, 97 régions non renseignées conservées dans le groupe `[missing]` |
| Sélectivité | Deux libellés textuels dans l'export, `formation sélective` (11 056) et `formation non sélective` (3 196). La notice illustre cette variable par un code numérique. Les sorties reprennent le texte de l'export. |

| Champ officiel | Lignes renseignées | Lignes vides |
|---|---:|---:|
| `taux_acces_ens` | 14 237 | 15 |
| `part_acces_gen`, `part_acces_tec`, `part_acces_pro` (chacun) | 14 252 | 0 |
| `ran_grp1` | 14 191 | 61 |
| `ran_grp2` | 6 124 | 8 128 |
| `ran_grp3` | 3 668 | 10 584 |

La présence d'une valeur dans l'export établit sa disponibilité brute. Les groupes d'appel varient par formation. Aucun de ces sept champs n'est utilisé pour produire les ratios de cette note, et aucune valeur officielle manquante n'a été imputée.

## Résultats descriptifs

Le ratio **vœux de phase principale / capacité** a une médiane de **10,54** par formation, avec un intervalle interquartile de **5,37 à 22,63** sur 14 248 formations à capacité positive. Le ratio des sommes sur ce même périmètre est 16,96. La médiane décrit la formation centrale, tandis que le ratio des sommes pondère les formations par leur capacité.

| Ensemble du fichier | 14 252 formations |
|---|---:|
| Places (`capa_fin`) | 769 351 |
| Vœux comptés en phase principale (`nb_voe_pp`) | 13 052 197 |
| Classés en phase principale (`nb_cla_pp`) | 9 373 484 |
| Comptes ayant reçu une proposition, toutes phases (`prop_tot`) | 4 140 259 |
| Acceptations, toutes phases (`acc_tot`) | 660 752 |
| Acceptations en phase principale (`acc_pp`) | 602 578 |
| Acceptations en phase complémentaire (`acc_pc`) | 58 174 |

Les fichiers d'agrégats calculent les ratios sur les sommes complètes des groupes. Parmi les groupes comparés, les formations sélectives ont 19,93 vœux de phase principale par place et les non sélectives 13,01. Le ratio vaut 26,31 en Île-de-France, 14,54 en Pays de la Loire, 12,44 pour les BTS et 10,02 pour les licences. Ces comparaisons brutes reflètent notamment la composition de l'offre et les comportements de candidature.

| Profil des néo-bacheliers, tous établissements | Parmi les comptes de vœux en phase principale (9 511 460) | Parmi les acceptations de la campagne (485 250) |
|---|---:|---:|
| Bac général | 71,18 % | 68,36 % |
| Bac technologique | 18,85 % | 19,49 % |
| Bac professionnel | 9,97 % | 12,15 % |
| Boursiers, toutes voies | 18,53 % (1 762 018) | 20,42 % (99 070) |

La colonne de gauche est pondérée par les comptes de vœux en phase principale et la colonne de droite par les acceptations sur l'ensemble de la campagne. La comparaison décrit deux compositions. Elle ne permet d'estimer ni un taux d'admission par voie ou statut boursier ni un effet des règles de sélection.

## Contrôles de plausibilité

- Les 19 groupes de régions (valeurs absentes incluses), les 11 groupes de filières et les deux modalités de sélectivité restituent chacun 14 252 formations. Les acceptations totales concordent ligne à ligne avec la somme des deux phases ; les trois voies du bac reconstituent le total des acceptations des néo-bacheliers.
- Quatre capacités nulles rendent le ratio demande/capacité indéfini. Le maximum observé, 904,67, correspond à 10 856 vœux de phase principale pour 12 places. Les valeurs sources sont conservées.
- Trois formations ont un classé de plus que de vœux de phase principale (`cod_aff_form` 4053, 21618 et 44813). La cause reste indéterminée. Les ratios bruts de classement de ces trois formations excèdent donc 1 et doivent être lus avec cette réserve.
- 1 941 formations déclarent plus d'acceptations sur la campagne que de places. Ce constat conforte l'usage d'un ratio descriptif de comptes. Le fichier ne mesure pas un taux d'occupation des établissements.

## Reproduire et réutiliser

Le [manifeste d'exécution](../../data/derived/parcoursup-2025/manifest.json) contient l'URL exacte de l'export, les horodatages, l'empreinte et la liste ordonnée des colonnes. Les tableaux versionnés ventilent les comptes [par région](../../data/derived/parcoursup-2025/by_region.csv), [par filière](../../data/derived/parcoursup-2025/by_filiere.csv) et [par sélectivité](../../data/derived/parcoursup-2025/by_select_form_raw.csv). L'exécution régénère aussi `formation_indicators.csv`, conservé hors dépôt avec le fichier source pour limiter le volume versionné.

Source des données et des dérivés : Ministère de l'Enseignement supérieur, SIES, [Parcoursup 2025](https://www.data.gouv.fr/datasets/parcoursup-2025-voeux-de-poursuite-detudes-et-de-reorientation-dans-lenseignement-superieur-et-reponses-des-etablissements), version du 9 mars 2026, Licence Ouverte 2.0.

```bash
python scripts/analysis/analyze_parcoursup_2025.py \
  --input /chemin/vers/fr-esr-parcoursup.csv \
  --output-dir /chemin/vers/resultats-parcoursup-2025 \
  --source-url 'https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-parcoursup/exports/csv'
```

L'option `--downloaded-at-utc` enregistre l'heure réelle de récupération si elle est connue. Vérifier l'empreinte avant de comparer les résultats à cet instantané.
