# Parcoursup 2025 — protocole d'analyse descriptive

**Statut :** protocole défini avant import et calculs ; aucun résultat calculé n'est présenté ici.  
**Version :** 1.0 — 13 novembre 2026.

## 1. Question et périmètre

Décrire comment la demande, le classement, les propositions et les admissions varient entre formations, selon le territoire, la filière et la modalité de sélectivité déclarée. Examiner séparément les profils par voie de baccalauréat et le poids des boursiers parmi les néo-bacheliers.

Le fichier officiel décrit 14 252 formations hors apprentissage, avec 115 variables, pour la campagne du 15 janvier au 10 septembre 2025 (extraction du 7 octobre 2025). Il couvre 1 015 200 candidats, dont 652 800 néo-bacheliers. L'unité de ligne est la formation/établissement, pas le candidat individuel.

Source et dictionnaire : [documentation méthodologique officielle](https://data.enseignementsup-recherche.gouv.fr/api/datasets/1.0/fr-esr-parcoursup/attachments/methodologie_opendata_2025pdf/).

## 2. Questions descriptives

1. Comment la demande (vœux), le classement, les propositions et les admissions se distribuent-ils selon les filières et les territoires ?
2. Comment les profils des candidats, des candidats classés et des admis diffèrent-ils selon la voie du bac (générale, technologique, professionnelle) ?
3. Quelle est la part de boursiers parmi les néo-bacheliers ayant formulé des vœux en phase principale et parmi les néo-bacheliers admis ?
4. Comment ces distributions varient-elles selon la modalité brute de select_form ?
5. Quelle est la dispersion entre formations (médiane, quartiles, extrêmes) des indicateurs de demande et de capacité ?

## 3. Variables et définitions opérationnelles

| Étape | Variables | Interprétation |
|---|---|---|
| Offre | capa_fin | Capacité d'accueil |
| Demande | voe_tot, nb_VOE_PP | Effectifs de candidats/vœux enregistrés par formation ; ne pas sommer pour produire un nombre de personnes uniques |
| Classement | nb_cla_PP, nb_cla_pp_BG, nb_cla_pp_BT, nb_cla_pp_BP | Effectifs classés par formation, selon les catégories documentées |
| Proposition | Prop_tot, prop_tot_BG, prop_tot_BT, prop_tot_BP | Effectifs ayant reçu une proposition |
| Admission | Acc_tot, Acc_neobac, Acc_BG, Acc_BT, Acc_BP | Effectifs ayant accepté une proposition (admis) |
| Bourse | nb_VOE_PP_BG_brs, nb_VOE_PP_BT_brs, nb_VOE_PP_BP_brs, Acc_brs | Boursiers parmi les néo-bacheliers en phase principale, puis boursiers parmi les néo-bacheliers admis |
| Territoire | region_etab_aff, dep, acad_mies | Territoire de l'établissement d'accueil |
| Formation | Fili, LIB_FOR_VOE_INS, select_form, contrat_etab | Filière et caractéristiques de la formation |

Les libellés et les définitions du dictionnaire officiel priment sur les noms de variables. Les valeurs de select_form seront conservées dans leur modalité brute dans les premières sorties : leur codage ne sera pas traduit en « sélectif/non sélectif » avant vérification explicite du dictionnaire et de la version du fichier.

## 4. Indicateurs calculés

Au niveau d'une formation, lorsque le dénominateur est strictement positif :

- demande/capacité = nb_VOE_PP / capa_fin ;
- classés/demande = nb_cla_PP / nb_VOE_PP ;
- propositions/demande = Prop_tot / nb_VOE_PP ;
- admissions/capacité = Acc_tot / capa_fin ;
- part de chaque voie parmi les néo-bacheliers candidats en PP = effectif de la voie / somme BG + BT + BP ;
- part de chaque voie parmi les néo-bacheliers admis = Acc_BG, Acc_BT ou Acc_BP / Acc_neobac ;
- part de boursiers parmi les néo-bacheliers candidats en PP = somme des boursiers BG + BT + BP / somme des candidats BG + BT + BP ;
- part de boursiers parmi les néo-bacheliers admis = Acc_brs / Acc_neobac.

Les deux parts de boursiers sont des compositions de populations distinctes : la première concerne les vœux de phase principale, la seconde les admissions cumulées de la campagne. Leur différence n'est **pas** un taux de sélection ni un effet causal.

Les ratios agrégés par région, filière ou sélectivité sont des ratios de sommes de comptes formation par formation. Ils décrivent des volumes de candidatures/formation, pas des probabilités individuelles. Les mêmes candidats peuvent apparaître dans plusieurs formations et les vœux multiples/sous-vœux compliquent toute interprétation en personnes uniques.

## 5. Règles d'agrégation

- Conserver la ligne formation comme unité primaire.
- Produire des tableaux distincts par région, filière agrégée et valeur brute de sélectivité.
- Pour chaque groupe, publier le nombre de formations et les sommes des effectifs, puis les ratios construits à partir de ces sommes.
- Ne jamais additionner les effectifs de formations pour prétendre retrouver le nombre de candidats uniques.
- Présenter en complément la distribution inter-formations (médiane et quartiles), pour éviter que les très grandes formations dominent toute lecture.
- Ne pas comparer les valeurs manquantes à zéro.
- Ne pas fusionner les formations sélectives et non sélectives avant d'avoir vérifié le codage, les définitions et les périmètres.

## 6. Limites et inférences interdites

Le fichier est agrégé par formation : il ne permet pas de reconstruire les trajectoires individuelles, les préférences hiérarchisées (les vœux ne sont pas hiérarchisés dans la phase principale), les choix finaux entre propositions, ni les résultats scolaires après admission.

Le taux d'accès fourni par le ministère est un indicateur distinct, calculé à partir du rang du dernier appelé et du nombre de candidats ayant validé un vœu en phase principale, hors gestion des désistements (GDD). La documentation précise que cet indicateur et la répartition par type de bac des candidats en position de recevoir une proposition ne peuvent pas être recalculés à partir du fichier open data. Ne pas les reconstruire par approximation.

Les écarts observés ne démontrent pas à eux seuls une discrimination, une inégalité de traitement ou un effet causal de la plateforme. Les compositions des candidatures dépendent aussi de l'offre, des préférences, des stratégies de vœux, de l'information, de la mobilité et des mécanismes antérieurs au supérieur.

## 7. Exécution reproductible

Télécharger le CSV depuis la page officielle du jeu de données Parcoursup 2025 et conserver le fichier original hors du dépôt si sa taille ou sa politique de conservation le justifie. Ne jamais modifier le fichier source.

Avec Python standard (aucune dépendance externe) :

    python scripts/analysis/analyze_parcoursup_2025.py --input /chemin/vers/fr-esr-parcoursup.csv --output-dir data/derived/parcoursup-2025

Le script produit des agrégats descriptifs, des indicateurs par formation et un manifeste rappelant l'unité d'analyse et les limites. La distribution du ratio demande/capacité inclut minimum, premier quartile, médiane, troisième quartile et maximum. Les sorties sont des données dérivées, pas des microdonnées.

## 8. Critères d'acceptation

- Le script vérifie les colonnes requises et la session.
- Les valeurs manquantes ne sont pas transformées silencieusement en zéro.
- Les ratios à dénominateur nul sont laissés vides.
- Les agrégations sont explicitement étiquetées comme comptes formation/candidature, non comme personnes uniques.
- Les sorties conservent les valeurs brutes de sélectivité.
- Les tests couvrent les dénominateurs nuls, les valeurs manquantes, les quantiles et le fait que les agrégats comptent des formations (et non des personnes uniques).
- Aucun résultat substantiel n'est publié avant l'exécution sur le fichier officiel et la revue des contrôles.
