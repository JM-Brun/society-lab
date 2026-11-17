---
id: "DOSSIER-SMIC-CAHUC-CARCILLO-LEBARBANCHON-2019-HIRING-CREDIT"
title: "Évaluer les aides à l'embauche en France : Cahuc, Carcillo & Le Barbanchon (2019)"
domain: "economy-employment"
status: "audited"
last_reviewed: "2026-11-17"
related_dossiers:
  - "dossiers/smic-causal-evidence-matrix.md"
  - "dossiers/smic-emploi-jeunes-bazen-etudes-recentes-etat-preuve.md"
  - "dossiers/smic-cottet-2020-2024-allegements-emploi.md"
geographic_scope: ["France"]
temporal_scope: "Dispositif zéro charges annoncé en décembre 2008, évalué sur 2006–2009 ; prolongation 2010 traitée avec réserves"
confidence: "moderate"
---

# Cahuc, Carcillo & Le Barbanchon (2019) — efficacité des aides à l'embauche (« zéro charges »)

## 1. Référence et question

Pierre Cahuc, Stéphane Carcillo et Thomas Le Barbanchon, « The Effectiveness of Hiring Credits », *The Review of Economic Studies*, 86(2), 2019, p. 593–626, DOI : https://doi.org/10.1093/restud/rdy011. Version de travail : IZA Discussion Paper 11248, décembre 2017.

**Question :** une exonération temporaire de cotisations patronales portant sur les nouvelles embauches à bas salaire dans les entreprises de moins de dix salariés accroît-elle l'emploi, les heures et les embauches ? L'effet diffère-t-il d'une baisse générale du coût du travail applicable aussi aux salariés déjà présents ?

Texte intégral audité : https://docs.iza.org/dp11248.pdf (92 pages).

## 2. Dispositif, traitement et population

Le programme français « zéro charges » est annoncé le 4 décembre 2008, dans le plan de relance de la Grande Récession. Il concerne les nouvelles embauches (et certains renouvellements de contrats temporaires) réalisées jusqu'au 31 décembre 2009 dans les entreprises privées de moins de dix salariés, pour des emplois à bas salaire.

- L'aide est maximale au SMIC horaire (8,82 € en 2009), où les cotisations patronales sont annulées par le dispositif.
- Elle décroît jusqu'à 1,6 SMIC.
- Pour un salarié à temps plein au SMIC, le coût du travail est réduit d'environ 12 % ; l'aide maximale sur douze mois est de 2 400 €.
- Les contrats doivent durer au moins un mois et ne pas relever d'autres aides ciblées ; les emplois domestiques et plusieurs catégories déjà subventionnées sont exclus.
- La taille est calculée en ETP à partir de la moyenne des effectifs de janvier à novembre 2008, avant l'annonce, ce qui limite la manipulation du seuil.
- Le dispositif est prolongé le 16 novembre 2009 jusqu'au 30 juin 2010, mais les auteurs concentrent l'identification principale sur 2009, car les règles d'éligibilité changent ensuite.

Le traitement porte sur le coût marginal des nouvelles embauches, non sur le coût de l'ensemble des salariés déjà présents. Il ne s'agit donc ni d'une baisse générale des cotisations sur les bas salaires, ni d'une hausse du SMIC brut.

## 3. Données et champ

Les auteurs appariement les DADS de l'Insee et le fichier administratif de Pôle emploi qui enregistre les entreprises inscrites au dispositif, les salaires des embauches, le montant et la durée de l'aide.

- Les DADS couvrent environ 85 % des salariés français dans le champ étudié.
- Le panel d'entreprises est construit sur 2005–2009.
- L'échantillon se limite aux entreprises privées à but lucratif ; agriculture et associations sont exclues.
- Les agences d'intérim sont exclues car l'entreprise utilisatrice du travail n'est pas identifiée dans les données.
- Les 1 % d'entreprises aux taux de croissance d'emploi les plus extrêmes sont écartées.
- L'analyse DiD principale se concentre sur les firmes de 6 à moins de 14 ETP l'année précédente. Les entreprises nouvelles qui n'avaient pas cette taille l'année précédente ne sont donc pas représentées.

Les résultats ne couvrent pas l'ensemble de l'économie, les administrations publiques, l'agriculture, les associations ni les nouvelles entreprises.

## 4. Identification

### 4.1 Différences de différences autour du seuil de dix salariés

- Groupe traité : entreprises de 6 à moins de 10 ETP.
- Groupe témoin : entreprises de 10 à moins de 14 ETP.
- La taille est calculée sur les effectifs ETP de l'année précédente, avant l'annonce du programme.
- Comparaison des évolutions annuelles 2006–2009, avec contrôles pour année, secteur, région et interactions, âge de l'entreprise, petite taille du chiffre d'affaires, composition salariale et part du temps partiel.
- Le paramètre est un effet d'intention de traiter : toutes les entreprises sous le seuil sont traitées dans l'estimation, qu'elles aient ou non effectivement demandé l'aide.

Le seuil de dix salariés n'est pas parfaitement neutre : quelques obligations réglementaires changent aussi autour de ce seuil (formation professionnelle, périodicité des versements sociaux, versement transport et présentation simplifiée du bilan). Les auteurs jugent ces discontinuités mineures, ne détectent pas d'accumulation des entreprises juste sous le seuil et utilisent plusieurs tests de robustesse.

### 4.2 Instrumentation de l'intensité locale

Une seconde stratégie compare des cellules « zone d'emploi × secteur » plus ou moins exposées à l'aide. L'intensité des embauches subventionnées est instrumentée par la part des travailleurs à bas salaire dans les petites entreprises de la cellule entre 2006 et 2008.

- 348 zones d'emploi et cinq secteurs sont distingués.
- Environ 1 721 cellules sont observées dans la spécification IV.
- Les auteurs ajoutent des prédictions shift-share de croissance sectorielle, la croissance des petites entreprises dans les zones voisines, ainsi que des contrôles de composition, de productivité et de levier financier.
- Cette stratégie vise notamment à limiter le risque que le groupe témoin des entreprises de 10–14 salariés soit lui-même affecté par la tension du marché du travail ou par des effets d'équilibre.

L'instrument repose toutefois sur une hypothèse d'exclusion : la part historique des emplois à bas salaire ne doit pas influencer la croissance de 2009 autrement que par l'exposition à l'aide, conditionnellement aux contrôles. Les chocs sectoriels et locaux peuvent rendre cette hypothèse exigeante.

## 5. Résultats

### 5.1 Résultats en différences de différences

Dans la spécification principale, l'aide augmente le taux de croissance de l'emploi des entreprises traitées d'environ **0,8 point de pourcentage** par rapport aux entreprises témoins.

Tableau 2 :
- croissance de l'emploi : +0,9 point sans contrôles, +0,8 point avec contrôles, +0,9 point sur la cohorte 2008–2009 ; significatif à 1 % ;
- croissance des heures : +1,0, +0,9 et +0,8 point ; significatif à 1 % ;
- taux d'embauche : +1,4, +1,2 et +1,9 point ; significatif ;
- taux de séparation : +0,5 et +0,4 point, non significatifs dans les deux premières spécifications ; +1,0 point dans la spécification restreinte 2008–2009, significatif à 5 % ;
- survie des entreprises : pas d'effet statistiquement significatif.

Les estimations utilisent des erreurs-types robustes à plusieurs niveaux : non regroupées, regroupées par entreprise, par cellule zone d'emploi × secteur, puis par zone d'emploi. Les résultats principaux restent stables à ces niveaux. L'échantillon compte 406 468 observations dans les deux premières spécifications et 207 379 dans la cohorte 2008–2009.

### 5.2 Emplois éligibles et non éligibles

Les emplois éligibles sont ceux rémunérés sous 1,6 SMIC et durant au moins un mois.

- Croissance de l'emploi éligible : +1,1 point (erreur-type 0,003), significatif à 1 %.
- Croissance de l'emploi non éligible : +0,2 point (erreur-type 0,004), non significatif.
- Croissance de l'emploi total dans cet échantillon : +0,8 point (erreur-type 0,002), significatif à 1 %.
- Pour les emplois éligibles, le taux d'embauche augmente d'environ 1,1 point ; le taux de séparation ne présente pas d'augmentation significative.
- Les heures travaillées progressent de façon comparable à l'emploi, ce qui ne suggère pas de substitution des heures des salariés déjà présents par celles des nouveaux salariés subventionnés.

Il faut distinguer la hausse de l'embauche éligible du résultat sur les séparations totales : dans une spécification restreinte, le taux global de séparation augmente d'un point, alors que l'effet sur les séparations des emplois éligibles n'est pas significatif.

### 5.3 Effets d'équilibre et modèle structurel

Les auteurs ne détectent pas de hausse des salaires ou de retombées significatives sur les entreprises témoins. Le programme ne subventionne qu'environ 1 % des emplois de l'économie, ce qui limite les effets de congestion à l'échelle du marché du travail.

Le modèle structurel de recherche-appariement utilise les variations quasi expérimentales pour identifier des paramètres de demande de travail, de coût de publication des vacances et de fonction d'appariement. Les simulations indiquent que le caractère temporaire, inattendu et ciblé sur les nouvelles embauches explique une grande partie de l'efficacité du dispositif.

- Élasticité de l'emploi au coût du travail induit par l'aide à l'embauche : environ −4, avec un intervalle de confiance à 95 % approximativement [−6 ; −2].
- Pour une variation uniforme du coût salarial appliquée à tous les salariés, l'élasticité correspondante est beaucoup plus faible en valeur absolue, autour de −1, avec un intervalle approximatif [−1,5 ; −0,5].
- Le coût brut par emploi créé est estimé à environ un quart du salaire annuel moyen ; le coût net après économies de prestations sociales est estimé proche de zéro dans le scénario de référence.

Ces chiffres sont propres au modèle et à une subvention temporaire des embauches marginales. Ils ne sont pas une élasticité du SMIC et ne peuvent être appliqués à une hausse générale du coût salarial.

## 6. Tendances préalables et robustesse

- Les taux de croissance de l'emploi des groupes traité et témoin évoluent de manière parallèle de 2006 à 2008 ; la différence préexistante est stable et négative.
- Les placebos de 2007 et 2008 ne montrent pas de différence significative pour l'emploi, les heures, les embauches et les séparations.
- Des placebos sur d'autres seuils de taille et des variations de la largeur de bande autour de dix salariés confirment les résultats.
- Les résultats sont proches avec et sans pondération par la taille des entreprises.
- La stratégie IV fournit un signe convergent ; les tests placebo d'instrument sur 2007 et 2008 ne sont pas significatifs.
- L'extension de novembre 2009 rend les estimations 2010 plus difficiles à interpréter ; les auteurs se concentrent donc sur 2009.
- Les auteurs ne trouvent pas d'effet de substitution temporelle robuste après la fin de l'aide, mais reconnaissent que les estimations postérieures à 2009 ne sont plus propres à cause des changements d'éligibilité.

## 7. Limites et controverses

1. **Effet local :** le résultat concerne les entreprises proches du seuil de dix salariés, pas toutes les entreprises.
2. **Marge extensive des entreprises déjà actives :** les nouvelles entreprises ne sont pas incluses dans le groupe de comparaison principal.
3. **Dispositif particulier :** aide temporaire, inattendue, ciblée sur les nouvelles embauches, pendant une récession. Son effet n'est pas celui d'un allègement permanent appliqué à tous les salariés.
4. **Seuil réglementaire :** quelques autres obligations changent autour de dix salariés, même si les auteurs ne détectent pas de tri manifeste et jugent les changements limités.
5. **Instrument :** l'identification IV dépend de l'exclusion de l'instrument fondé sur la part antérieure des bas salaires ; les contrôles shift-share et locaux réduisent mais n'annulent pas le risque de chocs différenciés.
6. **Données :** couverture DADS d'environ 85 % ; certaines catégories d'employeurs et d'emplois sont exclues.
7. **Généralisation :** le programme est mis en place en pleine crise de 2008–2009, avec salaires rigides et chômage élevé ; les effets d'un dispositif permanent dans un contexte normal peuvent être très différents.
8. **Modèle structurel :** le coût par emploi créé et les contre-factuels dépendent du modèle et des hypothèses de rigidité salariale, d'anticipation et de portée du programme.
9. **Jeunes :** l'étude n'est pas une évaluation spécifique aux jeunes ; le critère est le niveau de salaire et la taille de l'entreprise, pas l'âge.

## 8. Synthèse et niveau de confiance

| Dimension | Résultat | Confiance |
|---|---|---|
| Emploi des petites entreprises éligibles | +0,8 point de croissance relative en 2009 | Modérée à assez élevée pour ce contexte local |
| Embauches sur emplois éligibles | Hausse d'environ 1,1 point | Modérée |
| Heures travaillées | Hausse comparable à l'emploi | Modérée |
| Salaires | Pas d'effet détecté | Modérée |
| Séparations | Pas d'effet significatif pour les emplois éligibles ; résultat global plus ambigu dans la cohorte restreinte | Modérée à faible |
| Coût par emploi créé | Environ un quart du salaire annuel moyen brut, coût net estimé proche de zéro après prestations | Modérée à faible, car résultat de modèle |
| Effet d'une hausse générale du SMIC | Non estimé | Aucune conclusion directe |

**Conclusion opérationnelle :** l'étude apporte une preuve quasi expérimentale crédible qu'une aide temporaire et non anticipée aux nouvelles embauches à bas salaire peut augmenter l'emploi et les heures dans les petites entreprises en période de crise. Elle montre aussi pourquoi ce résultat ne peut pas être assimilé à celui d'une hausse générale du SMIC ou d'un allègement permanent : la subvention porte sur les postes marginaux entrants, pas sur les salariés déjà présents.

Pour l'enquête SMIC, cette étude doit être mobilisée comme preuve sur le canal « aide à l'embauche ciblée », en contraste avec Cottet (2024), qui étudie les effets de réductions de cotisations affectant les postes et les coûts des entreprises. Elle ne permet ni de conclure sur l'emploi des jeunes, ni d'extrapoler l'élasticité −4 à une hausse du SMIC brut.

## 9. Sources primaires

- Cahuc, P., Carcillo, S. & Le Barbanchon, T. (2017), IZA Discussion Paper 11248, texte intégral : https://docs.iza.org/dp11248.pdf
- Publication revue : https://doi.org/10.1093/restud/rdy011
- Notice IZA : https://www.iza.org/publications/dp/11248/the-effectiveness-of-hiring-credits
