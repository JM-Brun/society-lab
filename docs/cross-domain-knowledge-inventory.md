---
id: "CROSS-DOMAIN-KNOWLEDGE-INVENTORY-2026-11-18"
title: "Inventaire initial des connaissances et des rapprochements inter-domaines"
status: "working_inventory"
last_reviewed: "2026-11-18"
related_issue: 112
related_framework: "docs/cross-domain-knowledge-framework.md"
---

# Inventaire initial des connaissances et des rapprochements inter-domaines

## 1. Objet et méthode

Cet inventaire est une photographie documentaire du dépôt au 18 novembre 2026. Il prépare la mise en relation des sujets existants ; il ne constitue pas une revue scientifique exhaustive et ne transforme pas les pistes de rapprochement en résultats.

Les constats structurels ont été établis à partir de `knowledge/graph.yml`, `knowledge/RELATION_TYPES.yml`, `knowledge/concepts/registry.yml`, des pages de domaines, dossiers et synthèses. Les chiffres de structure sont reproductibles en recompilant les registres ; ils ne mesurent pas la qualité scientifique des relations.

## 2. État structurel du graphe

| Indicateur | État observé | Interprétation |
|---|---:|---|
| Relations enregistrées | 585 | Le graphe est déjà substantiel. |
| Objets distincts référencés par les arêtes | 407 | Il s'agit des objets effectivement présents dans les extrémités des relations, pas nécessairement de tous les objets du dépôt. |
| Concepts dans le registre | 15 | La couche de concepts réutilisables est encore compacte. |
| Nœuds de type MECHANISM référencés dans le graphe | 0 | Malgré le type de nœud prévu par la documentation, les mécanismes ne sont pas encore matérialisés comme objets reliés. |
| Relations REL-EXPLAINS enregistrées | 0 | Le type existe dans l'ontologie, mais n'est pas encore utilisé dans le graphe observé. |

### Répartition des relations

| Type | Nombre | Part approximative |
|---|---:|---:|
| REL-INCLUDES | 282 | 48,2 % |
| REL-ABOUT | 159 | 27,2 % |
| REL-SUPPORTS | 86 | 14,7 % |
| REL-TRANSCRIBES | 19 | 3,2 % |
| REL-CHILD-OF | 8 | 1,4 % |
| REL-QUALIFIES | 9 | 1,5 % |
| REL-GEOGRAPHICALLY-WITHIN | 7 | 1,2 % |
| REL-CITES | 4 | 0,7 % |
| REL-USES | 2 | 0,3 % |
| REL-SUMMARIZES | 1 | 0,2 % |
| **Total** | **585** | **100 %** |

Les relations d'organisation et de rattachement (notamment `REL-INCLUDES` et `REL-ABOUT`) dominent. C'est cohérent avec un graphe qui documente les dossiers, sources et périmètres, mais cela montre que la couche qui décrit les mécanismes, les transmissions et les interdépendances entre domaines reste à construire.

Les 86 relations `REL-SUPPORTS` ne doivent pas être assimilées à 86 validations causales : elles relient des sources ou études à des claims ou hypothèses et leur portée dépend de chaque justification.

### Limite ontologique identifiée

L'ontologie actuelle comporte `REL-EXPLAINS` (CONCEPT → MECHANISM), mais aucun type générique ne décrit clairement :
- un mécanisme qui transmet un effet d'un domaine à un autre ;
- une influence directionnelle entre deux mécanismes ou objets ;
- une condition qui modifie l'intensité ou le sens d'un effet ;
- une boucle de rétroaction entre mécanismes ;
- un arbitrage ou transfert entre acteurs, groupes, territoires ou générations.

Il ne faut pas ajouter ces types à la hâte : il faut d'abord examiner les validateurs et les registres, définir le cycle de vie des objets MECHANISM, puis tester le schéma sur un petit nombre de relations sourcées. Cette évolution est suivie dans l'issue #112.

## 3. Concepts transversaux déjà disponibles

Les identifiants ci-dessous existent dans `knowledge/concepts/registry.yml`. Ils doivent être réutilisés avant toute création de concepts proches.

| Concept canonique | Domaines déjà déclarés | Dossiers où il peut jouer un rôle transversal |
|---|---|---|
| `CONCEPT-DOUBLE-CARBON-CONSTRAINT` | Énergie, environnement, économie | Shift Project, PREF et scénarios de transition |
| `CONCEPT-PHYSICAL-ECONOMY` | Énergie, environnement, économie | Shift Project, comparaison des trajectoires, capacité productive |
| `CONCEPT-ROBUSTNESS-OF-TRANSITION` | Énergie, environnement, économie | PREF, RTE, ADEME, négaWatt et conditions de déploiement |
| `CONCEPT-SCENARIO-SENSITIVITY-ANALYSIS` | Énergie, environnement, économie | Comparaison de scénarios et analyse des hypothèses |
| `CONCEPT-DECLASSEMENT-ECONOMIQUE-RELATIF` | Économie, société | Antoine Foucher, comparaison générationnelle |
| `CONCEPT-PACTE-INTERGENERATIONNEL` | Économie, finances, société | Antoine Foucher, transferts, patrimoine et investissements |
| `CONCEPT-ARBITRAGE-DEPENSES-PUBLIQUES-INVESTISSEMENT` | Économie, finances | Antoine Foucher, finances publiques, investissement collectif |
| `CONCEPT-CAPACITE-PRODUCTIVE` | Économie, technologie, énergie | SMIC, industrie, énergie, compétences et investissement |
| `CONCEPT-ENERGY-ACCOUNTING-PERIMETER` | Énergie, environnement, économie | Comparaison quantitative ADEME, RTE, négaWatt et SNBC |

Les six concepts relatifs à la démocratie délibérative et à l'explication causale alternative restent pertinents pour les domaines politique, institutionnel, médiatique et scientifique ; ils ne sont pas artificiellement intégrés à la cartographie économique.

## 4. Première matrice de rapprochement des dossiers existants

Les statuts de cette matrice qualifient la relation entre dossiers, pas la vérité d'une hypothèse causale.

| Dossiers à croiser | Concepts / mécanismes déjà présents | Question transversale à instruire | Statut de départ |
|---|---|---|---|
| SMIC ↔ éducation / Parcoursup | Compétences, qualification, segmentation, progression salariale, mobilité, capacité productive | Comment les inégalités de formation et d'accès aux diplômes se prolongent-elles dans les emplois, les salaires et les trajectoires ? | Rapprochement thématique fondé ; chaîne empirique à documenter. |
| SMIC ↔ énergie / transition | Coûts de production, prix, marges, productivité, intensité énergétique, capacité productive | Comment les chocs énergétiques et les transformations sectorielles interagissent-ils avec les coûts salariaux et leur répercussion ? | Mécanismes économiques candidats ; aucune relation causale générale présumée. |
| Éducation ↔ énergie / transition | Compétences, formation continue, reconversion, besoins sectoriels et territoriaux | Les capacités de formation et les reconversions suivent-elles le rythme et la géographie des investissements de transition ? | Question documentable ; données d'offre de formation et besoins de main-d'œuvre à rapprocher. |
| TIG ↔ finances publiques / institutions / emploi | Coûts complets, capacité institutionnelle, tutorat, coordination, insertion, coût d'opportunité | Quels coûts sont supportés par les administrations et organismes d'accueil, et sous quelles conditions le TIG contribue-t-il à l'insertion sans substitution à l'emploi rémunéré ? | Coûts administratifs partiels et contraintes opérationnelles déjà documentés ; effets d'insertion et coûts complets à consolider. |
| Pacte intergénérationnel ↔ éducation / énergie / finances | Pacte intergénérationnel, investissement public, capacité productive, contraintes matérielles et dette | Comment répartir entre générations le financement, les risques et les bénéfices des investissements éducatifs, énergétiques et productifs ? | Cadre conceptuel déjà présent ; arbitrages normatifs et effets causaux à distinguer. |
| Transition énergétique ↔ finances publiques / territoires | Robustesse, investissements, dépendances, coûts, emplois et répartition | Quels territoires, ménages, secteurs et niveaux de gouvernement supportent les coûts et captent les bénéfices selon les scénarios ? | Pistes déjà identifiées dans les dossiers de scénarios ; harmonisation des périmètres et preuves distributives nécessaire. |

## 5. Les cinq chaînes d'analyse à privilégier

### A. Éducation → compétences → emploi → salaires → productivité

**Dossiers de départ :** Parcoursup et égalité des chances ; synthèse SMIC ; dossier Antoine Foucher.

**Chaîne à examiner :** conditions sociales et acquis initiaux → orientation et accès aux formations → conditions d'études et diplomation → compétences mobilisées dans l'emploi → mobilité et progression salariale → productivité et partage de la valeur.

**Garde-fous :**
- Parcoursup n'est qu'une étape d'affectation ; ne pas lui attribuer les inégalités construites en amont ou les résultats après admission.
- Le diplôme n'est pas une mesure directe de compétence ni de productivité.
- Les associations entre diplôme, emploi et salaire ne suffisent pas à isoler le rendement causal de la formation.
- Distinguer les cohortes, spécialités, territoires, secteurs et horizons.

### B. Énergie → coûts sectoriels → prix / marges / investissement → emploi et compétences

**Dossiers de départ :** Shift Project ; audit PREF et comparaison des scénarios ; SMIC et mécanismes de transmission.

**Chaîne à examiner :** prix et disponibilité des vecteurs énergétiques → exposition des secteurs et chaînes d'approvisionnement → coûts unitaires → arbitrages prix/marges/volumes/investissement → demande de travail et besoins de compétences → effets sur salaires, territoires et finances publiques.

**Garde-fous :**
- Une trajectoire énergétique est conditionnelle ; ce n'est pas une prévision certaine.
- Les scénarios doivent avoir des périmètres énergétiques compatibles avant comparaison.
- Les effets diffèrent selon contrats, intensité énergétique, pouvoir de marché, technologie et capacité d'investissement.
- Ne pas déduire des créations ou suppressions nettes d'emplois de simples volumes d'emplois sectoriels annoncés.

### C. Institutions → capacité d'exécution → coûts complets → résultats publics

**Dossiers de départ :** TIG ; domaines institutions et sécurité ; finances publiques.

**Chaîne à examiner :** règles et décisions → capacité des services et partenaires → affectation et exécution → délais et qualité de mise en œuvre → résultats pénaux et sociaux → coûts directs et coûts transférés.

**Garde-fous :**
- Distinguer coût budgétaire, coût complet et coût social.
- Ne pas assimiler une capacité nominale à une capacité effectivement mobilisable.
- Les comparaisons de récidive doivent tenir compte de la sélection des publics et des conditions d'exécution.
- Ne pas présenter l'insertion comme effet établi sans indicateur et suivi adaptés.

### D. Finances publiques → investissement → capacité productive → trajectoires générationnelles

**Dossiers de départ :** Antoine Foucher ; SMIC et système socio-fiscal ; scénarios énergétiques.

**Chaîne à examiner :** recettes et dépenses → financement, dette et arbitrages → investissement matériel et immatériel → capacités de production, d'innovation et de formation → revenus, patrimoine, services publics et risques transmis aux générations.

**Garde-fous :**
- Une part élevée de dépenses courantes ne démontre pas un effet d'éviction causal.
- Distinguer investissement comptable, investissement humain, maintenance, dépenses de fonctionnement et transferts.
- Tenir compte des effets macroéconomiques, du cycle, des taux, des recettes et des externalités.
- Séparer diagnostic empirique et choix normatif de répartition.

### E. Transition énergétique → répartition territoriale et intergénérationnelle

**Dossiers de départ :** Shift Project ; PREF / ADEME / RTE / négaWatt / SNBC ; Antoine Foucher.

**Chaîne à examiner :** investissements et infrastructures → localisation des activités et des emplois → coûts et bénéfices territoriaux → fiscalité, prix et accès aux services → dépendances et actifs transmis à long terme.

**Garde-fous :**
- Distinguer les périmètres territoriaux et les compétences institutionnelles.
- Ne pas assimiler dépenses d'investissement, coût net et bénéfice social.
- Documenter les effets sur les ménages et territoires selon les données disponibles.
- Les générations futures ne constituent pas un groupe homogène ; expliciter les scénarios démographiques et distributifs.

## 6. Ce que l'inventaire révèle sur les métadonnées

1. **Concepts :** 15 entrées canoniques sont disponibles. Ne pas créer de synonymes tels que « investissement productif », « capacité industrielle » ou « capital humain » sans vérifier si ces notions sont déjà couvertes par les concepts et dossiers existants.
2. **Mécanismes :** aucun nœud `MECHANISM` n'est actuellement référencé par les relations du graphe. Les chaînes causales restent surtout rédigées dans les dossiers ; elles ne sont pas encore navigables comme objets structurés.
3. **Domaines :** les rattachements multi-domaines existent déjà pour plusieurs concepts, notamment économie-énergie-environnement. Il faut s'assurer que les domaines déclarés reflètent le contenu réel, sans ajouter tous les domaines connexes à chaque objet.
4. **Sources :** chaque relation de preuve doit continuer à renvoyer à une source ou étude identifiable et à un claim précisément borné. Un rapprochement entre deux dossiers ne constitue pas une source.
5. **Synthèses :** les synthèses restent autonomes. Les liens transversaux doivent compléter leurs conclusions, non les remplacer ni créer un index concurrent.
6. **Temporalité et échelle :** les comparaisons doivent conserver les populations, territoires, périodes, secteurs et horizons propres aux sources.

## 7. Séquence de travail recommandée

1. Valider l'inventaire des concepts existants et repérer les objets candidats à fusion ou enrichissement.
2. Définir le schéma minimal d'un objet `MECHANISM` et son cycle de vie, sans modifier tous les dossiers d'un coup.
3. Choisir une seule chaîne pilote : **éducation → compétences → emploi → salaires**, car les dossiers Parcoursup, SMIC et Foucher existent déjà.
4. Relever dans ces dossiers les études et claims qui documentent chaque étape, puis identifier précisément les ruptures de preuve.
5. Enregistrer seulement les mécanismes et relations suffisamment documentés ; conserver les étapes manquantes comme questions de recherche.
6. Répliquer la méthode sur énergie et capacité productive, puis sur TIG et capacité institutionnelle.
7. Mettre à jour les synthèses et les pages de domaines uniquement après que les relations ont été vérifiées.

## 8. Articulation et limites

- Le graphe canonique reste `knowledge/graph.yml`.
- Les concepts canoniques restent dans `knowledge/concepts/registry.yml`.
- Les types de relations restent définis dans `knowledge/RELATION_TYPES.yml`.
- Le cadre méthodologique est décrit dans [cross-domain-knowledge-framework.md](cross-domain-knowledge-framework.md).
- Le suivi des travaux est assuré par [l'issue #112](https://github.com/JM-Brun/society-lab/issues/112).
- L'ingestion des jeux ADEME Saison 2 reste suivie dans [l'issue #110](https://github.com/JM-Brun/society-lab/issues/110) ; les données brutes ne sont pas considérées comme analysées tant qu'elles n'ont pas été récupérées et contrôlées.

Cet inventaire ne prétend pas avoir établi les liens causaux entre les sujets. Il indique où les dossiers se complètent, quelles chaînes explicatives méritent une revue commune et quelles données ou études manquent pour aller plus loin.
