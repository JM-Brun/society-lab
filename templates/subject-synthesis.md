---
id: "SYNTHESIS-<DOMAIN>-<SLUG>"
title: "<Titre clair du sujet>"
domain: "<domaine>"
status: "draft" # draft | in_review | provisional | validated | superseded
last_reviewed: "YYYY-MM-DD"
owner: ""
related_dossiers: []
related_claims: []
related_studies: []
related_datasets: []
geographic_scope: []
temporal_scope: ""
confidence: "low" # low | moderate | high; justify below
---

# Synthèse — <Titre du sujet>

> **En une phrase :** <réponse courte et nuancée à la question centrale.>

## 1. Synthèse exécutive

En 5 à 10 lignes : question étudiée, réponse provisoire, résultats les plus robustes, principal désaccord ou incertitude, conséquence pratique. Cette section doit pouvoir être lue seule.

## 2. Question et périmètre

- **Question de recherche :**
- **Pourquoi la question importe :**
- **Périmètre géographique :**
- **Période étudiée :**
- **Population / unités observées :**
- **Ce qui est explicitement hors périmètre :**

## 3. Principaux constats

| Constat | État (établi / probable / exploratoire / contesté) | Preuve principale | Limite importante |
|---|---|---|---|
| | | | |

Ne pas transformer une corrélation en causalité. Préciser pour chaque chiffre sa source, sa date, son champ, son dénominateur et son unité.

## 4. Ce que montrent les preuves

### Faits et données établis
- 

### Résultats des études et méthodes
- Pour chaque étude importante : question, population, période, méthode, résultat, incertitudes et validité externe.
- Distinguer résultats descriptifs, estimations causales, simulations et projections.

### Points de convergence
- 

## 5. Débat contradictoire

| Position / mécanisme | Meilleur argument | Éléments qui l'étayent | Contre-preuves / objections | Appréciation |
|---|---|---|---|---|
| | | | | |

Présenter loyalement les positions des parties prenantes sans traiter leurs déclarations comme des preuves empiriques. Éviter la fausse équivalence : qualifier la qualité des preuves.

## 6. Incertitudes, limites et désaccords non résolus

- **Incertitudes de mesure :**
- **Limites des données :**
- **Biais et limites d'identification :**
- **Résultats contradictoires :**
- **Informations manquantes :**
- **Ce qui pourrait faire changer la conclusion :**

## 7. Conclusion raisonnée

Répondre directement à la question. Distinguer :
1. ce que les éléments disponibles permettent d'affirmer ;
2. ce qu'ils rendent plausible sans le démontrer ;
3. ce qu'ils ne permettent pas de conclure.

**Niveau de confiance :** faible / modéré / élevé — justification explicite et proportionnée à la qualité, la convergence et l'actualité des preuves.

## 8. Implications et options d'action (si pertinent)

| Option | Bénéfices attendus | Coûts / risques / effets secondaires | Conditions de réussite | Indicateurs |
|---|---|---|---|---|
| | | | | |

Séparer les constats empiriques des arbitrages normatifs. Rendre explicites les critères et pondérations ; ne pas masquer les choix de valeur dans un score unique.

## 9. Déclinaison territoriale et temporelle (si pertinente)

Préciser les échelles effectivement documentées, les différences de contexte, les transferts entre territoires et les limites de comparabilité. Ne jamais extrapoler à un niveau géographique plus fin que les données.

## 10. Questions ouvertes et prochaines étapes

Classer les travaux par priorité, avec livrable attendu et condition de validation.

| Priorité | Question / travail | Livrable | Condition pour considérer le point traité |
|---|---|---|---|
| P1 | | | |

## 11. Sources essentielles et traçabilité

Lister en priorité les sources primaires et les études déterminantes. Pour chacune : référence complète, date, lien, type de source, apport exact et limites. Relier les affirmations importantes aux identifiants du registre de claims, sources et études du dépôt.

## 12. Historique des révisions

| Date | Modification | Motif / nouvelle preuve |
|---|---|---|
| YYYY-MM-DD | Création | |

---

## Registre et automatisation

Toute création d'un nouveau dossier principal dans `dossiers/registry.yml` doit être accompagnée d'une entrée correspondante dans `syntheses/registry.yml` et d'un fichier de synthèse. Le contrôle GitHub Actions vérifie la correspondance des identifiants, l'existence des fichiers, les métadonnées obligatoires et les sections minimales. Les documents d'approfondissement d'un sujet existant peuvent être rattachés à sa synthèse principale sans créer artificiellement une nouvelle synthèse.

## Contrôle qualité avant publication

- [ ] La réponse courte est visible dès le début et compréhensible seule.
- [ ] Les faits, interprétations, hypothèses, simulations et jugements de valeur sont séparés.
- [ ] Les chiffres ont un périmètre, une période, un dénominateur et une source.
- [ ] Les arguments contradictoires sont présentés dans leur meilleure version.
- [ ] La qualité des preuves est évaluée ; aucune fausse équivalence.
- [ ] Les limites, incertitudes et explications concurrentes sont explicites.
- [ ] Chaque conclusion importante renvoie à une preuve ou est qualifiée.
- [ ] Les recommandations rendent visibles leurs arbitrages normatifs.
- [ ] Les liens vers dossiers, claims, études, données et graphe sont à jour.
- [ ] La date et le statut de la synthèse sont renseignés.
