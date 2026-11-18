# Pilote d’extraction vérifiée — claims Parcoursup 2026

- **Date de contrôle :** 18 novembre 2026
- **Périmètre :** trois claims Parcoursup 2026
- **Nature :** contrôle direct des pages officielles et extraction structurée dans `claims/registry.yml`
- **Statuts :** conservés à `under_review` ; ce pilote ne constitue pas une revue indépendante ni une validation globale de l'équité de la procédure.

## 1. Résultat

Trois claims ont reçu un objet `source_verifications[*].extraction` facultatif et renseigné :

| Claim | Élément extrait | Localisateur | Réserve principale |
|---|---|---|---|
| `CLAIM-PARCOURSUP-2026-APPLICANTS` | 1 046 000 candidats | Communiqués ministériels des 28 mai et 19 octobre 2026 | Agrégat multi-catégories ; ne pas assimiler aux seuls lycéens ou néo-bacheliers |
| `CLAIM-PARCOURSUP-2026-NEW-BACHELORS-OFFER` | 93,7 % | Note Flash SIES n° 2026-26, page HTML de présentation | Le passage consulté ne donne pas le numérateur brut ; 81,0 % ont accepté une proposition, indicateur distinct |
| `CLAIM-PARCOURSUP-2026-LYCEENS-OFFER` | 603 910 et deux taux publiés : 91,5 % / 91,4 % | Communiqué HTML du 19 octobre ; PDF du bilan, p. 10 | Divergence d'un dixième de point entre les deux supports officiels |

## 2. Écart documentaire à ne pas masquer

Le communiqué HTML ministériel du 19 octobre 2026 indique **603 910 lycéens**, soit **91,5 %** des lycéens ayant formulé des vœux. Le PDF officiel « Bilan de la procédure d'admission Parcoursup 2026 », page 10, indique le même effectif de **603 910**, mais un taux de **91,4 %**.

Le pilote conserve les deux valeurs dans l'extraction et ajoute cette divergence aux limites du claim. Il ne choisit pas arbitrairement l'une des deux, ne modifie pas le statut et ne déduit pas un dénominateur exact à partir de pourcentages arrondis. La résolution nécessite de retrouver les dénominateurs non arrondis et la convention de calcul/arrondi utilisée pour chaque support.

Cette différence illustre pourquoi l'extraction doit conserver le support, le localisateur et la formulation exacte, et pas seulement une valeur recopiée dans une synthèse.

## 3. Ce que le pilote démontre — et ne démontre pas

Il démontre que le schéma permet de consigner, dans la fiche claim existante :
- le type d'élément extrait et la valeur publiée ;
- l'unité, la population, la période, la géographie et la définition de l'indicateur ;
- le localisateur au niveau de chaque vérification ;
- la méthode et la date d'extraction ;
- une réserve documentaire lorsque deux supports d'une même source divergent.

Il ne démontre pas :
- que les taux mesurent l'équité des admissions ;
- que les populations des trois indicateurs sont interchangeables ;
- que le taux de 91,4 % ou celui de 91,5 % est le bon taux définitif ;
- que les données agrégées permettent de reconstituer les trajectoires individuelles ;
- que les claims peuvent passer à `supported`.

## 4. Décisions de méthode

1. Garder les statuts `under_review`.
2. Ne pas renseigner de confiance probabiliste sur la base de ce seul contrôle.
3. Ne pas remplacer les dénominateurs absents par des estimations calculées à partir de pourcentages arrondis.
4. Conserver les deux valeurs officielles discordantes jusqu'à réconciliation.
5. Distinguer le nombre de candidats, le nombre de lycéens ayant reçu une proposition, le taux de néo-bacheliers ayant reçu une proposition et le taux ayant accepté une proposition.
6. Étendre le pilote aux tableaux détaillés et fichiers téléchargeables seulement après identification de leurs définitions et de leur millésime exact.

## 5. Sources primaires contrôlées

- Communiqué du ministère du 19 octobre 2026 : https://www.enseignementsup-recherche.gouv.fr/fr/parcoursup-2026-des-resultats-stables-dans-un-contexte-de-progression-historique-des-candidatures-104400
- Communiqué du ministère du 28 mai 2026 : https://www.enseignementsup-recherche.gouv.fr/fr/la-phase-d-admission-parcoursup-ouvre-mardi-2-juin-2026-19h-103022
- Note Flash SIES n° 2026-26 : https://www.enseignementsup-recherche.gouv.fr/fr/parcoursup-2026-les-propositions-d-admission-dans-l-enseignement-superieur-104448
- PDF du bilan Parcoursup 2026 : https://www.enseignementsup-recherche.gouv.fr/sites/default/files/2026-10/Bilan%20de%20la%20proc%C3%A9dure%20d%27admission%20Parcoursup%202026_0.pdf

## 6. Étape suivante

- Réconcilier les 91,4 % / 91,5 % avec les effectifs non arrondis et les définitions de population.
- Examiner les tableaux et fichiers détaillés de la Note Flash SIES avant d'ajouter des numérateurs ou des ventilations.
- Appliquer le même protocole à un résultat quantitatif TIG, en séparant soigneusement les cohortes, les événements et les dénominateurs.
