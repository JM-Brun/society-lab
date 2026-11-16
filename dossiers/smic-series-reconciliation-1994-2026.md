# Réconciliation des séries du SMIC, 1994–2026

- **Identifiant :** DOSSIER-SMIC-SERIES-RECONCILIATION-1994-2026
- **Date de contrôle :** 16 novembre 2026
- **Périmètre :** France hors Mayotte pour les taux contemporains ; séries anciennes en francs lorsqu'indiqué.
- **Fichiers :** [chronologie des événements](../data/smic-revaluations-1994-2026.csv), [moyennes annuelles](../data/smic-annual-averages-1994-2026.csv), [audit événementiel](smic-revaluations-audit-1994-2026.md).

## 1. Conclusion générale

La série doit être lue comme quatre objets distincts, qui ne sont pas interchangeables :

1. **Taux horaire légal à une date d'effet** : montant brut en vigueur à chaque entrée en vigueur. C'est l'unité du CSV événementiel.
2. **Glissement annuel à date fixe** : variation entre deux dates comparables, souvent juillet à juillet. Il peut inclure plusieurs événements intermédiaires et ne doit pas être ajouté aux hausses datées.
3. **Moyenne annuelle du taux horaire** : moyenne des taux légaux en vigueur au cours des douze mois. Elle est distincte du taux de fin d'année et du pouvoir d'achat.
4. **GMR** : garanties mensuelles de rémunération liées au passage aux 35 heures. Elles protégeaient le salaire mensuel lors de la réduction du temps de travail et ne sont pas des taux horaires SMIC supplémentaires.

La chronologie événementielle 1994–2026 comporte 42 changements effectifs jusqu'au 1er juin 2026. Le 1er décembre 2026 est annoncé politiquement mais n'est pas encore une observation effective dans ce CSV. Le taux de 2025 est resté à 11,88 € toute l'année.

## 2. Réconciliation des rapports 2009 et 2020 et des sources primaires (1973, 1981)

### 2.1 Source méthodologique INSEE (1992) et tableau du Sénat (1994)

L'annexe INSEE « L'évolution du SMIC de 1970 à 1991 » définit précisément le coup de pouce comme le résidu au-delà de l'obligation légale, sur un glissement du SMIC de juillet à juillet :

- prix d'avril à avril (p1) et de mai à mai (p2) ;
- taux de salaire horaire ouvrier (TSH) d'avril à avril, exprimé en francs constants ;
- l'obligation légale combine l'indexation sur les prix de mai à mai et au moins la moitié du gain réel du TSH ;
- si s est la hausse nominale observée et m la hausse correspondant à l'obligation légale, le coup de pouce c est calculé multiplicativement : (1 + c/100) = (1 + s/100) / (1 + m/100). Ce n'est donc pas simplement s moins m.

Le tableau 3 du rapport du Sénat de 1994 reprend une décomposition analogue et précise ses colonnes : prix de mai à mai, moitié du TSH réel d'avril à avril, obligation légale et coup de pouce. Il donne :

| Épisode | Hausse du SMIC sur la fenêtre | Obligation légale | Coup de pouce résiduel |
|---|---:|---:|---:|
| Juillet 1973 | +20,9 % | 10,2 % | 9,7 % |
| 1er juin 1981 | +19,4 % | 13,5 % | 5,2 % |

Le 1er juin 1981 est une date d'effet atypique : le glissement annuel se termine au 1er juin, non au 1er juillet. Le relèvement de 10 % souvent cité pour juin 1981 correspond au passage immédiat de 15,20 F au 1er mars à 16,72 F au 1er juin (+10 %). Ce n'est ni le glissement annuel de 19,4 %, ni le résidu discrétionnaire de 5,2 %.

### 2.2 Groupe d'experts 2009 : distinguer les deux rapports

Le rapport de **juin 2009** contient le graphique 2 de décomposition historique sur 1970–2008, attribué à la Direction générale du travail. Il précise que les évolutions du graphique sont mesurées **de juillet à juillet** ; il distingue inflation, moitié du gain de pouvoir d'achat du SHBO, coups de pouce et convergence des GMR. L'annexe 1 fournit en outre une table des taux et des composantes pour juillet 1996–juillet 2008. C'est cette même publication qui fonde le CSV de décomposition 1996–2008.

Le rapport de **décembre 2009** n'est pas la source du graphique historique : il documente surtout la règle applicable à l'époque et le changement de calendrier. Pour une revalorisation au 1er juillet, il retient les prix de mai à mai et le pouvoir d'achat du SHBO de mars à mars. À compter de janvier 2010, les fenêtres deviennent novembre à novembre pour les prix et septembre à septembre pour le SHBO. La transition de janvier 2010 est particulière : les périodes déjà prises en compte en juillet 2009 sont retranchées ; le rapport utilise donc mai-novembre 2009 pour les prix et mars-septembre 2009 pour le SHBO.

Ces fenêtres de 2009 ne doivent pas être rétroprojetées automatiquement sur les épisodes des années 1970 et 1980. Le graphique de juin 2009 établit le glissement total juillet-juillet, mais ne publie pas les séries mensuelles ni le détail des mois de référence utilisés pour chacune des composantes historiques.

### 2.3 Groupe d'experts 2020 : divergence à conserver

Le rapport 2020, dans son graphique 2 sur 1970–1989, cite un coup de pouce maximal de **10,1 % en 1973** et de **6,9 % en 1981**. La source indiquée sous le graphique est la **Direction du Trésor** ; les périodes sont étiquetées 1970–1971 à 1988–1989, sans indication explicite des mois de début et de fin. Le graphique historique du rapport de juin 2009 est une autre source : il est attribué à la Direction générale du travail et précise explicitement un glissement juillet-juillet. Rien dans les rapports consultés ne démontre que les deux graphiques utilisent une série identique. Pour le graphique 2020, les mois de référence des indices de prix et de SHBO ainsi que la formule opérationnelle du coup de pouce ne sont pas publiés.

L'exemple de lecture du graphique 2020 présente une décomposition empilée : pour 1970–1971, environ 9,8 % au total, répartis entre 5,3 % d'inflation, 2,4 % de demi-gain réel du SHBO et 2,2 % de coup de pouce. Cette présentation ne fournit pas l'équation de calcul du résidu. À l'inverse, l'INSEE 1992 définit explicitement le coup de pouce de façon multiplicative : (1 + c/100) = (1 + s/100) / (1 + m/100). Cette différence de convention est une explication possible des écarts, mais elle ne suffit pas à les résoudre sans les séries sources.

Les valeurs 10,1 % et 6,9 % du rapport 2020 ne sont donc pas directement substituables aux 9,7 % et 5,2 % du tableau INSEE/Sénat. Le CSV 1970–1993 conserve les valeurs du tableau du Sénat ; les valeurs du rapport 2020 restent documentées comme une autre reconstruction publiée, sans correction arbitraire du CSV.

### 2.4 Contrôle du taux horaire de juillet 1978

Le CSV 1970–1993 conserve 10,85 F au 1er juillet 1978. Le tableau 2 du rapport du Sénat donne bien 10,85 F dans la chronologie des taux ; le tableau 3 de décomposition indique 10,65 F pour cette même date. L'INSEE 1992 donne également 10,85 F. Il s'agit d'une incohérence interne du tableau 3, pas d'une raison de remplacer le taux légal par 10,65 F. La note du CSV a été corrigée pour refléter le sens exact de cette divergence.

## 3. Reconstruction 1994–2026 : ruptures et mécanismes

| Période | Régime de taux et calendrier | Mécanisme à isoler |
|---|---|---|
| 1994–1998 | Taux horaire annuel au 1er juillet ; deux dates d'effet en 1996 | Mai 1996 : seuil d'inflation automatique ; juillet 1996 : revalorisation annuelle. Les hausses de 1995 et 1997 incluent des coups de pouce documentés. |
| 1999–2002 | Coexistence du SMIC horaire et des garanties mensuelles liées aux 35 heures | Les GMR protègent le salaire mensuel des salariés passés à 35 h ; cinq générations de GMR se créent entre 1998 et 2002. |
| 2003–2005 | Convergence progressive du SMIC et des GMR | La loi du 17 janvier 2003 programme la convergence au 1er juillet 2005. La hausse réelle du SMIC horaire sur 2003–2005 est évaluée à 11,4 % par le rapport parlementaire ; ce n'est pas un coup de pouce ordinaire isolé. |
| 2006–2009 | Retour à un minimum horaire unifié ; revalorisation annuelle en juillet jusqu'en 2009 | Mai 2008 : déclenchement automatique de l'inflation ; juillet 2008 : ajustement annuel complémentaire. Le glissement juillet-juillet 2008 est +3,2 %. |
| 2010–2012 | Calendrier annuel déplacé au 1er janvier à compter de 2010 | Janvier 2010 est une transition six mois après juillet 2009. Décembre 2011 est un déclenchement automatique distinct de janvier 2012. Juillet 2012 : +2 %, dont 0,6 point de coup de pouce et 1,4 point d'indexation anticipée. |
| 2013–2020 | Formule annuelle révisée ; calendrier au 1er janvier | Référence salariale élargie du SHBO au SHBOE à partir de 2013 ; indice des prix du premier quintile hors tabac depuis 2014. Pas de coup de pouce entre 2012 et novembre 2024 selon le rapport 2024. |
| 2021–2024 | Plusieurs déclenchements automatiques infra-annuels | Les hausses de 2021–2023 sont déclenchées par le seuil d'inflation. Le 1er novembre 2024 est une revalorisation annuelle anticipée, et non un déclenchement infra-annuel automatique. |
| 2025 | Taux maintenu à 11,88 € toute l'année | Pas de nouvelle ligne d'événement : la hausse de novembre 2024 anticipe la revalorisation automatique attendue en janvier 2025. |
| 2026 | 12,02 € au 1er janvier ; 12,31 € au 1er juin | Janvier : +1,18 % selon la formule annuelle ; juin : +2,41 % après franchissement du seuil d'inflation. Le 1er décembre +1,6 % a été annoncé le 9 novembre, mais reste un événement futur à confirmer par le texte réglementaire et le taux horaire officiel. |

## 4. GMR et transition des 35 heures : ne pas confondre les minima

Les lois Aubry ont instauré des garanties mensuelles pour éviter une baisse de rémunération mensuelle lors du passage de 39 à 35 heures. Les GMR étaient des montants mensuels, définis selon la date de passage aux 35 heures, et indexés différemment du SMIC horaire. Cinq GMR ont coexisté avec le SMIC horaire, soit six niveaux de minimum au total ; « six minima » ne signifie donc pas six GMR. Le rapport du Sénat 2004–2005 identifie cinq générations :

- GMR 1 : passage avant le 1er juillet 1999 ;
- GMR 2 : passage avant le 1er juillet 2000 ;
- GMR 3 : passage avant le 1er juillet 2001 ;
- GMR 4 : passage avant le 1er juillet 2002 ;
- GMR 5 : régime le plus récent, qui sert de cible de convergence.

La création de nouvelles GMR s'arrête après juillet 2002. La loi Fillon du 17 janvier 2003 programme leur convergence vers la GMR 5 au 1er juillet 2005. Les coups de pouce différentiels prévus sur 2003–2005 correspondent à cette convergence : en termes réels, 11,4 % pour le SMIC horaire, 4,9 % pour GMR 1, 3,6 % pour GMR 2, 1,8 % pour GMR 3, 0,6 % pour GMR 4 et 0 % pour GMR 5. Le rapport du Sénat de novembre 2004 donne des valeurs de GMR et des projections de convergence ; pour les taux horaires finalement appliqués, la série INSEE/DARES fait foi (7,19 € en 2003, 7,61 € en 2004, 8,03 € en 2005).

La réforme des 35 heures a aussi affecté le rythme du SHBO et les négociations salariales avant même la convergence finale. L'étude des effets de 2003–2005 doit donc contrôler simultanément la baisse de durée légale, les GMR, la convergence et les allègements de cotisations.

## 5. Moyennes annuelles : série distincte du taux légal de fin d'année

Le nouveau fichier annuel rassemble les moyennes annuelles officielles du taux horaire brut de 1994 à 2025. Elles sont par exemple de 5,37 € en 1994, 8,61 € en 2008, 9,31 € en 2012, 10,85 € en 2022, 11,69 € en 2024 et 11,88 € en 2025.

Pour 2026, la moyenne annuelle n'est pas encore définitive. Le fichier fournit seulement une moyenne partielle janvier-octobre de 12,17 €, calculée sur cinq mois à 12,02 € puis cinq mois à 12,31 €. Cette valeur ne doit pas être présentée comme une moyenne annuelle officielle.

La moyenne du taux horaire ne mesure ni le salaire mensuel effectivement reçu, ni le nombre d'heures travaillées, ni le revenu disponible. Le pouvoir d'achat annuel doit être analysé avec les indices de prix et les séries de pouvoir d'achat publiées séparément par l'INSEE/DARES.

## 6. Correction du classement de novembre 2024

Le CSV événementiel classait initialement le 1er novembre 2024 comme déclenchement infra-annuel automatique. Ce classement est corrigé. Le rapport du groupe d'experts de novembre 2024 indique que le Gouvernement a avancé de deux mois la revalorisation annuelle attendue au 1er janvier 2025 : la formule automatique aurait donné environ +1,95 % selon l'indice d'octobre ; le taux a été porté à +2 % dès le 1er novembre. Le rapport précise qu'il n'y a pas eu de coup de pouce entre janvier 2012 et novembre 2024, et qu'aucune hausse supplémentaire n'était attendue en janvier 2025 si les données provisoires étaient confirmées.

La décision est discrétionnaire quant au calendrier, mais elle ne constitue pas un coup de pouce au sens d'une hausse au-delà de la formule légale. Le CSV utilise désormais la classe « anticipated_annual_automatic ».

## 7. Annonce de décembre 2026 : statut hors série réalisée

Le 9 novembre 2026, le Gouvernement a annoncé une hausse totale de 1,6 % au 1er décembre. La transcription officielle qualifie cette décision de « coup de pouce » ; le communiqué de Bercy du 13 novembre la décrit comme supérieure à la revalorisation légale. Les sources primaires consultées ne publient toutefois pas de décomposition chiffrée entre part automatique et part discrétionnaire : le partage « 1,0 + 0,6 point » ne doit donc pas être enregistré comme une ventilation officielle vérifiée. À la date de ce contrôle (16 novembre), l'annonce reste hors du CSV événementiel des taux effectifs : le taux horaire brut et le texte réglementaire d'application doivent être vérifiés après publication.

## 8. Limites et contrôles encore nécessaires

- Les valeurs du CSV événementiel sont des montants légaux à des dates d'effet ; les taux de variation publiés et les ratios calculés à partir de montants arrondis peuvent différer.
- Le CSV retient désormais +3,05 % en 2006, valeur publiée dans l'annexe du rapport du groupe d'experts de juin 2009. Le ratio des taux affichés 8,27/8,03 donne environ +2,99 % ; le rapport ne fournit pas les taux sous-jacents non arrondis permettant de reproduire exactement l'écart. La correction porte donc sur le pourcentage documenté, pas sur le taux légal de 8,27 €.
- Les rapports 2009 et 2020 ne fournissent pas les séries mensuelles complètes qui permettraient d'harmoniser les coups de pouce de 1973 et 1981.
- Les moyennes annuelles ne doivent pas être utilisées comme taux légal à une date ni comme indicateur du revenu annuel.
- Les évolutions descriptives du taux, des bénéficiaires ou des salaires ne démontrent pas l'effet causal des hausses sur l'emploi, les prix, les marges ou la pauvreté.

## Sources principales

- INSEE, « L'évolution du SMIC de 1970 à 1991 », *Les salaires en 1990*, annexe 1 : https://www.bnsp.insee.fr/ark:/12148/bc6p06z40qt.pdf
- Sénat, rapport d'information n° 504 (1993–1994), tableaux 2 à 4 : https://www.senat.fr/rap/1993-1994/i1993_1994_0504.pdf
- Groupe d'experts SMIC, rapport de juin 2009, annexe 1 : https://dares.travail-emploi.gouv.fr/sites/default/files/d8fa752e7f09a16b5f95c0ff7b482262/Smic_rapport_2009%20%28juin%29.pdf
- Groupe d'experts SMIC, rapport de décembre 2009 : https://www.tresor.economie.gouv.fr/Articles/284b121f-b187-4280-b327-05f18064c3fa/files/bbaf996b-d48f-49bb-bc6c-d44fdf15a3d1
- Groupe d'experts SMIC, rapport 2020, chapitre VI / graphique 2 : https://travail-emploi.gouv.fr/sites/travail-emploi/files/files-spip/pdf/smic_rapport_2020.pdf
- Groupe d'experts SMIC, rapport 2024, chap. 1, tableau I.1 et encadré I.1 : https://www.strategie-plan.gouv.fr/files/files/Publications/2024/SMIC/FS-2025-SMIC-RAPPORT-2024-12f%C3%A9v25.pdf
- Sénat, rapport général 2004–2005, annexe GMR : https://www.senat.fr/rap/l04-074-334/l04-074-3341.pdf
- INSEE, données annuelles du SMIC 1980–2026 : https://www.insee.fr/fr/statistiques/1375188
- INSEE, série mensuelle du SMIC horaire brut, idBank 000822484 : https://www.insee.fr/fr/statistiques/serie/000822484
