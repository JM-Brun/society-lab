# Spécification minimale des données territoriales TIG — Loire-Atlantique

- **Dossier associé :** `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE`
- **Issue :** [#22 — Enquête territoriale pilote en Loire-Atlantique](https://github.com/JM-Brun/society-lab/issues/22)
- **Statut :** modèle de demande et de contrôle ; aucune extraction reçue ni donnée locale analysée
- **Version :** 1.0 — 16 novembre 2026

## 1. Objet

Ce document transforme le protocole d'enquête en spécification minimale exploitable pour discuter avec le SPIP, l'ATIGIP ou le producteur des données TIG 360°. Il vise à éviter qu'un export mélange stocks, flux, cohortes et étapes de parcours.

La demande porte exclusivement sur des données agrégées. Elle ne suppose pas que toutes les variables existent dans TIG 360° ni qu'une extraction territoriale soit techniquement ou juridiquement possible. Le premier échange doit précisément établir cette disponibilité.

## 2. Principes de l'extraction

1. **Période :** trois années civiles récentes complètes, plus l'année en cours séparément si elle est suffisamment documentée.
2. **Date d'extraction :** fournir la date et l'heure de gel des données ; signaler les extractions révisables.
3. **Unité :** distinguer mesures, personnes, postes, places, organismes et heures. Ne jamais employer « nombre de TIG » sans préciser l'unité.
4. **Nature statistique :** identifier chaque tableau comme stock à une date, flux sur une période ou cohorte suivie.
5. **Cohortes :** suivre les mesures selon leur date d'entrée dans une étape ; préciser la fenêtre de maturation et les sorties encore en cours.
6. **Géographie :** privilégier le lieu du poste et le ressort du service ; ne demander une géographie de résidence que si elle est déjà agrégée et sans risque de ré-identification.
7. **Confidentialité :** aucune ligne individuelle, aucun identifiant, aucune date exacte rattachable à une personne, aucun détail d'infraction.
8. **Qualité :** joindre le dictionnaire des variables, les règles de gestion, les changements de définition et les taux de données manquantes.

## 3. Tables agrégées à demander par priorité

| Priorité | Table | Variables minimales | Finalité |
|---|---|---|---|
| P0 | Dictionnaire et métadonnées | définition, unité, source, date de disponibilité, historique, valeurs possibles | Interpréter correctement tout export |
| P0 | Flux de mesures par étape | période/cohorte, étape atteinte, nombre de mesures, statut de sortie | Reconstituer les transitions |
| P0 | Délais par transition | origine, fin, cohorte, effectif, médiane, Q1, Q3, P90, moyenne si disponible | Localiser les goulots d'étranglement |
| P0 | Parc des organismes et postes | organisme/poste agrégé, statut, période d'activité, type de mission, territoire agrégé | Distinguer offre référencée et offre active |
| P1 | Capacité mobilisable | places ou créneaux, capacité horaire, disponibilité, délai de mobilisation, tuteurs disponibles | Estimer la capacité effective |
| P1 | Issues et motifs | démarrage, achèvement, conversion, interruption, non-démarrage, motifs codés | Comprendre les pertes |
| P1 | Heures | prescrites, programmées, réalisées, restantes, par cohorte et issue | Mesurer l'exécution réelle |
| P2 | Accessibilité | classes de temps de trajet ou zones larges, sans adresse ni trajet individuel | Étudier les contraintes territoriales |

**Règle de repli :** si une table n'existe pas, demander la définition la plus proche disponible et consigner explicitement l'écart. Ne pas reconstruire une variable en combinant des agrégats incompatibles.

## 4. Chaîne de parcours et dénominateurs

La chaîne cible est :

`prononcé → saisine/transmission → évaluation → recherche de poste → affectation → démarrage → achèvement / interruption / conversion`

Pour chaque étape, demander les effectifs entrants, les effectifs passés à l'étape suivante et les sorties concurrentes. Le dénominateur d'un taux de transition est le nombre de mesures éligibles et effectivement entrées dans l'étape considérée, dans une cohorte définie.

| Transition | Dénominateur recommandé | Numérateur | Sorties concurrentes à distinguer |
|---|---|---|---|
| Prononcé → saisine | mesures prononcées dans la cohorte | mesures transmises au service | annulation, changement de cadre, donnée manquante |
| Saisine → évaluation | mesures reçues et prises en charge | mesures évaluées | dossier incomplet, impossibilité de joindre, autre sortie |
| Évaluation → affectation | mesures évaluées et considérées compatibles avec une recherche | mesures affectées à un poste | absence de poste adapté, refus, retrait, autre motif |
| Affectation → démarrage | mesures affectées et toujours actives | mesures ayant une première présence | annulation, absence, changement de situation |
| Démarrage → issue | mesures commencées dans une cohorte arrivée à maturité | mesures achevées | interruption, conversion, mesure encore en cours |

Ne pas calculer un taux d'achèvement en divisant les mesures achevées par toutes les mesures prononcées. Ne pas traiter les mesures encore en cours comme des échecs. Publier séparément les cohortes arrivées à maturité et les cohortes censurées.

## 5. Définir la capacité sans confondre les stocks

Pour chaque période, demander si possible les distinctions suivantes :

- **Organisme habilité :** structure autorisée à accueillir, qu'elle ait ou non accueilli récemment.
- **Organisme actif :** structure ayant effectivement accueilli au moins une mesure sur une période définie.
- **Poste référencé :** mission inscrite dans l'outil ou le répertoire, sans présumer de sa disponibilité.
- **Poste actif :** mission encore proposée et validée à la date d'observation.
- **Place/créneau :** possibilité concrète d'accueil, avec volume horaire et calendrier.
- **Place vacante :** capacité non occupée à la date d'observation.
- **Place mobilisable :** place vacante, confirmée par la structure, avec tuteur et conditions d'accueil disponibles dans un délai défini.

Une place vacante n'est pas automatiquement mobilisable. Une structure qui a accueilli un TIG dans l'année n'est pas nécessairement en capacité d'en accueillir un autre immédiatement. Toute mesure de capacité doit indiquer la date d'observation et le délai de mobilisation retenu.

## 6. Nomenclature minimale des issues

Demander les catégories natives du système et leur définition avant toute harmonisation. À défaut, proposer une table de correspondance, sans imposer les catégories suivantes comme si elles étaient celles de TIG 360° :

- achevée ;
- commencée et encore en cours ;
- affectée mais non commencée ;
- non affectée après évaluation ;
- interrompue ;
- convertie ou remplacée par décision compétente ;
- annulée ou devenue sans objet ;
- statut inconnu / données incomplètes.

Les motifs doivent rester agrégés et non stigmatisants : indisponibilité de poste, inadéquation horaire ou géographique, indisponibilité du tutorat, difficulté de coordination, changement de situation, absence ou non-présentation, décision judiciaire, motif administratif, autre, inconnu. Ne pas inférer un motif individuel à partir d'une catégorie agrégée.

## 7. Géographie et confidentialité

Ordre de préférence :

1. département ;
2. Nantes Métropole / reste de la Loire-Atlantique, si la définition territoriale est stable ;
3. grands bassins urbains, périurbains et ruraux définis à partir des données et des mobilités ;
4. commune uniquement si les effectifs et les règles de diffusion le permettent.

Ne pas publier de petites cellules. Le producteur doit fixer ou confirmer un seuil de diffusion ; les cellules sous le seuil sont supprimées ou agrégées. Ne pas tenter de reconstituer les valeurs masquées par soustraction. Ne pas croiser plusieurs ventilations si cela rend une personne ou une structure identifiable.

## 8. Contrôles à effectuer à réception

- [ ] Les unités sont explicites : mesures, personnes, postes, places, organismes ou heures.
- [ ] Chaque tableau indique stock, flux ou cohorte.
- [ ] Les périodes et dates de gel sont documentées.
- [ ] Les définitions et valeurs possibles sont fournies.
- [ ] Les dénominateurs des taux sont vérifiables.
- [ ] Les mesures en cours sont distinguées des mesures en échec.
- [ ] Les délais précisent origine, fin, effectif et traitement des cas non aboutis.
- [ ] Les postes référencés, actifs, vacants et mobilisables ne sont pas confondus.
- [ ] Les données manquantes, changements de nomenclature et révisions sont signalés.
- [ ] Les règles de confidentialité et de suppression des petites cellules sont respectées.
- [ ] Les résultats peuvent être reproduits à partir des tableaux reçus.

## 9. Journal de disponibilité à compléter

| Élément demandé | Disponible | Partiel | Indisponible | Définition / réserve / date |
|---|---:|---:|---:|---|
| Dictionnaire TIG 360° | ☐ | ☐ | ☐ | |
| Flux par étape | ☐ | ☐ | ☐ | |
| Délais par transition | ☐ | ☐ | ☐ | |
| Organismes et postes | ☐ | ☐ | ☐ | |
| Capacité mobilisable | ☐ | ☐ | ☐ | |
| Issues et motifs | ☐ | ☐ | ☐ | |
| Heures prescrites et réalisées | ☐ | ☐ | ☐ | |
| Ventilation territoriale | ☐ | ☐ | ☐ | |
| Règles de confidentialité | ☐ | ☐ | ☐ | |

Ce journal doit être rempli à partir des réponses réellement reçues. Une case non renseignée signifie « non vérifié », pas « indisponible ».

## 10. Formulation courte à joindre à la prise de contact

> Afin de préparer une enquête territoriale non nominative sur les conditions d'exécution des TIG en Loire-Atlantique, nous souhaiterions d'abord connaître les données agrégées qui peuvent être extraites de TIG 360° et leurs définitions. Notre priorité porte sur les flux par étape, les délais entre étapes, les statuts des postes et la capacité réellement mobilisable, ainsi que les issues des mesures par cohorte. Nous ne sollicitons aucune donnée individuelle ni aucun dossier pénal. Si une extraction n'est pas possible, un échange méthodologique sur les indicateurs existants et leurs limites constituerait déjà une première étape utile.

## 11. Règle d'interprétation

Cette spécification ne prouve ni une pénurie de places, ni une défaillance du SPIP, des juridictions ou des structures d'accueil. Elle organise une demande permettant de tester plusieurs explications concurrentes. Tant que les données n'ont pas été obtenues, contrôlées et documentées, les constats territoriaux restent des questions de recherche.

## Références internes

- [Protocole d'enquête territoriale TIG](tig-territorial-inquiry-protocol.md)
- [Suite logique de recherche TIG](tig-research-next-steps.md)
- [Issue #22](https://github.com/JM-Brun/society-lab/issues/22)
