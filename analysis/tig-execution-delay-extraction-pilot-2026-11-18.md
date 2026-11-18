# Pilote d’extraction vérifiée — délais d’exécution des TIG

**Date : 18 novembre 2026**  
**Claim contrôlé :** `CLAIM-TIG-EXECUTION-DELAY-2025`  
**Source primaire :** Cour des comptes, *Évaluation de deux peines alternatives à l’incarcération*, mars 2025, notamment p. 47 et annexe 5, p. 151.

## Résultat principal

Le chiffre de **16,7 mois** est confirmé dans le rapport primaire. Il désigne le délai moyen entre la date de condamnation et la fin d’exécution pour les **TIG ou sursis-TIG prononcés en 2020 et exécutés dans les trois ans**, sur données administratives SSER/DACG (rapport, p. 47 et annexe 5, p. 151).

La mesure est donc conditionnelle à l’exécution dans les 36 mois. Elle ne décrit pas le délai moyen de l’ensemble des mesures prononcées en 2020. Les mesures converties, encore en cours à trois ans ou en échec ne sont pas dans le groupe des mesures exécutées qui sert au calcul du délai. Le tableau ne donne pas l’effectif exact utilisé pour calculer la moyenne : ce dénominateur numérique reste à obtenir auprès du SSER/DACG.

## Ne pas confondre les séries

| Indicateur | Valeur | Population / méthode | Interprétation |
|---|---:|---|---|
| Délai national SSER/DACG | **16,7 mois (moyenne)** | TIG ou sursis-TIG prononcés en 2020 et exécutés dans les trois ans | Cohorte nationale conditionnelle à l’exécution |
| Enquête directe de la Cour | **16 mois** | TIG autonomes terminés dans les neuf SPIP étudiés | Échantillon de terrain, non comparable directement au chiffre national |
| Enquête directe de la Cour | **20 mois** | TIG en incluant les sursis-TIG | Même enquête de terrain ; périmètre élargi |
| Condamnation → prise en charge SPIP | **2,5 mois (médiane)** | Enquête de la Cour dans neuf SPIP | Médiane, non moyenne |
| Prise en charge SPIP → affectation à un CPIP | **21 jours (moyenne)** | Enquête de la Cour | Étape administrative distincte |
| Prise en charge SPIP → affectation à un poste | **6,1 mois (moyenne)** | Enquête de la Cour | Étape distincte du délai total |
| Prise en charge SPIP → affectation à un poste | **7,9 mois (moyenne)** | Enquête flash DAP ; TIG affectés entre le 15/09/2023 et le 15/10/2023 | Fenêtre d’observation ciblée, pas la cohorte nationale |
| Affectation au poste → fin des heures | **5,7 mois (moyenne)** | Enquête de la Cour | Durée pouvant inclure interruptions et changements |
| Fin des heures → fin de mesure enregistrée dans APPI | **2 mois (moyenne)** | Enquête de la Cour | Délai de clôture / enregistrement distinct |

L’enquête de terrain de la Cour porte sur des TIG terminés entre le quatrième trimestre 2023 et le premier trimestre 2024 dans neuf SPIP. Elle ne doit pas être fusionnée avec la cohorte administrative nationale de prononcés 2020.

## Issues de la cohorte à trois ans

La Cour rapporte, trois ans après le prononcé :
- **75 %** exécutés ;
- **9 %** convertis en une autre peine ;
- **5 %** encore non exécutés ;
- **11 %** en échec imputable au condamné.

Les 16 % constitués par les deux dernières catégories ne doivent pas être décrits comme « non exécutés » sans préciser qu’ils agrègent des mesures encore en cours et des échecs imputables. Le rapport indique aussi que le taux d’exécution ou de conversion atteint 21 % à 12 mois, 74 % à 24 mois et 84 % à 36 mois.

La note méthodologique de la Cour précise que le SSER observe les TIG prononcés une année N à 12, 24 et 36 mois. Cette méthode rend comparables le délai d’exécution et le taux d’exécution d’une cohorte, mais le rapport indique qu’elle ne permet pas alors d’étudier les TIG prononcés après 2020. La note signale également une limite de périmètre concernant l’identification des obligations de TIG au sein des sursis probatoires ; l’analyse présentée est limitée aux peines de TIG et aux anciens sursis-TIG.

## Extraction structurée ajoutée

Le claim `CLAIM-TIG-EXECUTION-DELAY-2025` conserve son statut `under_review`. Sa vérification de source comporte maintenant un objet `extraction` avec :
- type `reported_result` ;
- valeur numérique 16.7 et unité « mois » ;
- population, période, territoire et définition du délai ;
- dénominateur formulé explicitement comme cohorte conditionnelle, avec mention que l’effectif exact n’est pas publié dans le tableau ;
- méthode d’extraction manuelle.

Aucun effectif, intervalle de confiance ou précision statistique non publié n’a été ajouté. Le chiffre de 16,7 mois n’est pas recalculé à partir des pourcentages d’issues.

## Limites et travail restant

1. **Effectif du dénominateur :** obtenir le nombre exact de mesures exécutées dans les trois ans entrant dans le calcul des 16,7 mois, ainsi que les règles d’inclusion/exclusion.
2. **Distribution des délais :** rechercher moyenne, médiane, quartiles, P90 et éventuels traitements des valeurs extrêmes ; ne pas déduire une distribution de la seule moyenne.
3. **Actualisation :** retrouver les séries SSER/DACG ou TIG 360° postérieures à la cohorte 2020, en documentant les ruptures de définition et les délais de consolidation.
4. **Chaîne complète :** reconstituer séparément prononcé → transmission → prise en charge SPIP → affectation CPIP → affectation poste → démarrage → fin des heures → clôture APPI, ainsi que conversion, suspension et échec.
5. **Données territoriales :** conduire la démarche de l’issue #22 en Loire-Atlantique sans extrapoler les moyennes nationales ni présumer d’un déficit de capacité.
6. **Comparabilité :** conserver séparément la cohorte administrative nationale, l’échantillon des neuf SPIP et les enquêtes flash DAP ; comparer uniquement les étapes ayant les mêmes bornes, populations et fenêtres temporelles.

## Références

- Cour des comptes, rapport intégral (PDF) : https://www.ccomptes.fr/sites/default/files/2025-03/20250304-Evaluation-2-peines-alternatives-a-l-incarceration.pdf
- Cour des comptes, publication et documents associés : https://ccomptes.fr/fr/publications/evaluation-de-deux-peines-alternatives-lincarceration
- Sénat, *L’exécution à la peine*, rapport d’information : https://www.senat.fr/rap/r25-002/r25-00212.html

## Conclusion

Le chiffre de 16,7 mois est suffisamment localisé et défini pour être extrait de manière structurée. Il reste un indicateur descriptif de délai parmi les mesures exécutées dans les trois ans, pas une mesure du délai moyen de toutes les peines de TIG prononcées, ni une mesure isolée du temps avant affectation ou démarrage. Le statut du claim reste donc `under_review` jusqu’à l’obtention des effectifs exacts, à l’actualisation des séries et à la clarification des étapes non couvertes par la statistique nationale.
