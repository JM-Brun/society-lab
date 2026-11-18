# Revue des 25 sources sans relation structurée — 18 novembre 2026

## Objet et méthode

Cette revue reprend les 25 sources listées dans l'audit de couverture du graphe. Chaque source a été comparée aux dossiers canoniques, aux synthèses et aux registres de relations. Une relation `REL-INCLUDES` n'est ajoutée que lorsque le contenu d'un dossier mobilise explicitement la ressource. Elle documente une inclusion documentaire, pas une validation scientifique de la source.

## Relations ajoutées dans cette réconciliation

17 liens dossier → source ont été ajoutés à `knowledge/graph.yml` :

| Dossier | Sources | Interprétation |
|---|---|---|
| `DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE` | `SOURCE-ATIGIP-TIG360-PLATFORM`, `SOURCE-MINJUSTICE-TIG-47000-PLACES-2026` | Outil de gestion des postes et annonce de stock national ; ni l'un ni l'autre ne mesure la disponibilité locale effective. |
| `DOSSIER-SMIC-FRANCE-TRADEOFFS` | `SOURCE-CGT-SALAIRES-2000-2026`, `SOURCE-CFDT-SMIC-NEGOCIATIONS-2026`, `SOURCE-CFDT-BRANCH-GRIDS-2026`, `SOURCE-CFTC-SMIC-GRIDS-2026`, `SOURCE-FO-CONGRESS-RESOLUTION-2026`, `SOURCE-UNSA-SMIC-COUP-POUCE-2025`, `SOURCE-CFE-CGC-SMIC-GRIDS-2026`, `SOURCE-MEDEF-PLFSS-RELIEFS-2024`, `SOURCE-U2P-CAPEB-SALAIRES-2026`, `SOURCE-MEDEF-SALAIRES-COUT-TRAVAIL-2025`, `SOURCE-U2P-SMIC-1500-2026`, `SOURCE-MEDEF-SMIC-CONFERENCE-2026` | Positions déclarées d'organisations et propos rapportés. Ces liens ne signifient pas que les affirmations économiques de ces acteurs sont démontrées. Les deux sources journalistiques restent secondaires. |
| `DOSSIER-UN-COMMUN-ACCORD-DELIBERATIVE-ASSEMBLY` | `SOURCE-UN-COMMUN-ACCORD-ABOUT`, `SOURCE-UN-COMMUN-ACCORD-HOMEPAGE` | Sources primaires sur la présentation, les rôles et les actualités de l'organisateur ; les garanties annoncées restent à vérifier indépendamment. |
| `DOSSIER-ANTOINE-FOUCHER-PACTE-INTERGENERATIONNEL` | `SOURCE-EDITION-AUBE-ANTOINE-FOUCHER-2026` | Référence déjà déclarée dans le champ `source_ids` du dossier ; relation explicite ajoutée pour la navigation du graphe. Source éditoriale pour les métadonnées, non validation des thèses. |

## Sources conservées sans nouvelle relation

| Source | Décision et motif |
|---|---|
| `SOURCE-FO-POUVOIR-ACHAT-2026` | Conservée comme contexte sur l'épargne salariale et le pouvoir d'achat ; le dossier de positions SMIC ne mobilise pas explicitement cette ressource pour une revendication de salaire minimum. |
| `SOURCE-NEUMARK-WASCHER-FRANCE-YOUTH-1997` | Aucune référence structurée explicite retrouvée vers une étude ou un dossier dans cet audit ciblé ; ne pas la rattacher à une étude par simple proximité thématique. Vérifier l'objet bibliographique et sa mobilisation dans la prochaine revue des études historiques. |
| `SOURCE-ABOWD-KRAMARZ-MARGOLIS-NBER-1999` | Ne pas confondre avec le chapitre Abowd–Kramarz–Lemieux–Margolis de 2000 et son working paper antérieur : l'étude de 1999 est distincte. Aucun lien documentaire explicite vers cette source n'a été établi ici. |
| `SOURCE-DARES-INFLATION-SALAIRES-2023` | Publication potentiellement pertinente pour le dossier SMIC, mais aucune relation source→étude/dossier/claim n'a été justifiée par une référence structurée explicite dans cette passe. À vérifier dans la revue des dossiers statistiques DARES. |
| `SOURCE-DARES-SMIC-REVAL-2026` | Source administrative pertinente pour les bénéficiaires directs, mais aucun objet structuré n'a été relié à cette source dans cette passe. Vérifier l'existence d'une étude ou claim dédiée avant de créer un lien. |
| `SOURCE-UK-DFE-2024-HARASSMENT-CENSORSHIP` | Revue de preuves de contexte sur le harcèlement et la censure dans l'enseignement supérieur anglais ; aucun dossier/claim du dépôt ne la mobilise explicitement dans les références structurées examinées. |
| `SOURCE-TADROS-2022-RIGHTS-NOPLATFORMING` | Analyse normative autonome ; ne pas la transformer en preuve empirique d'efficacité du no-platforming. Aucun lien structuré explicite retrouvé. |
| `SOURCE-LIBERAL-DEFENSE-NOPLATFORMING-2024` | Analyse normative autonome ; aucun dossier/claim ne la mobilise explicitement dans les références structurées examinées. |

## Bilan

- 25 sources examinées.
- 17 relations documentaires justifiées ajoutées.
- 8 sources conservées sans relation artificielle.
- Aucun nouveau type de relation, schéma, registre ou identifiant métier.
- Aucune claim créée ou promue.
- Les sources de position d'acteur restent distinctes des preuves empiriques ; les sources normatives restent distinctes des mesures d'effets.

Le nombre d'objets isolés devrait être recalculé par le validateur de couverture après fusion : les liens ajoutés concernent des sources et dossiers déjà existants. Cette revue ne prétend pas résoudre les liens potentiellement manquants dans les dossiers DARES ou dans la littérature historique sur le SMIC ; elle les conserve explicitement comme travail restant plutôt que de produire des arêtes conjecturales.

## Seconde passe de vérification — références textuelles explicites

Une vérification du contenu des dossiers, au-delà des seuls champs `source_ids`, a retrouvé cinq références explicites supplémentaires. Elles sont ajoutées au graphe dans une PR complémentaire :

| Dossier | Source | Justification |
|---|---|---|
| `DOSSIER-SMIC-HISTORICAL-EPISODES` | `SOURCE-NEUMARK-WASCHER-FRANCE-YOUTH-1997` | L'étude est décrite et citée pour l'épisode de juin 1981 ; résultat limité à l'emploi des jeunes. |
| `DOSSIER-SMIC-HISTORICAL-EPISODES` | `SOURCE-ABOWD-KRAMARZ-MARGOLIS-NBER-1999` | Résultats sur les trajectoires d'emploi et référence NBER WP 6996 ; dépendance avec le travail de 1997/2000 explicitement signalée. |
| `DOSSIER-SMIC-DARES-BENEFICIAIRES-INFLATION-2021-2024` | `SOURCE-DARES-INFLATION-SALAIRES-2023` | Publication primaire listée en tête du dossier et résultats descriptifs repris. |
| `DOSSIER-SMIC-HISTORICAL-EPISODES` | `SOURCE-DARES-INFLATION-SALAIRES-2023` | Publication citée pour l'épisode inflationniste 2021–2023. |
| `DOSSIER-SMIC-HISTORICAL-EPISODES` | `SOURCE-DARES-SMIC-REVAL-2026` | Publication du 15 octobre 2026 explicitement citée pour compléter la chronologie des bénéficiaires directs. |

Ces cinq liens sont documentaires. Ils ne convertissent pas les résultats descriptifs DARES en effets causaux et ne transforment pas les études historiques en loi générale.

## Sources toujours sans relation justifiée après la seconde passe

Quatre sources demeurent isolées à l'issue de cette revue :

- `SOURCE-FO-POUVOIR-ACHAT-2026` : la ressource traite du déblocage de l'épargne salariale et du pouvoir d'achat, pas d'une position chiffrée sur le SMIC. Aucun dossier canonique examiné ne l'utilise explicitement. La conserver comme ressource de contexte, sans l'attacher artificiellement au dossier SMIC.
- `SOURCE-UK-DFE-2024-HARASSMENT-CENSORSHIP` : revue de preuves sur le harcèlement et la censure dans l'enseignement supérieur anglais. Aucun dossier ou claim examiné ne la cite explicitement. Une intégration éventuelle exige un dossier sur la liberté académique et les politiques institutionnelles, ou une justification d'extension du périmètre du dossier comparatif.
- `SOURCE-TADROS-2022-RIGHTS-NOPLATFORMING` : analyse normative juridique/philosophique des droits à une tribune. Elle ne doit pas être traitée comme preuve d'efficacité empirique du no-platforming. Aucun lien explicite n'a été retrouvé dans les dossiers examinés.
- `SOURCE-LIBERAL-DEFENSE-NOPLATFORMING-2024` : défense normative du no-platforming non violent et mise en balance des droits. Même décision : conserver comme référence normative ; ne pas créer de relation empirique ou causale sans dossier qui l'analyse explicitement.

## Travail restant priorisé

1. **Terminer le rapprochement des références no-platforming** : vérifier le périmètre et les références du protocole comparatif, de la matrice de preuves et des claims existantes ; si les deux articles normatifs sont réellement mobilisés, les référencer explicitement dans un dossier de cadrage normatif distinct de la matrice empirique.
2. **Décider du devenir de la revue UK DfE** : déterminer si le dossier doit couvrir les politiques de liberté académique et le harcèlement universitaire. Si oui, expliciter la question de recherche et les indicateurs ; sinon, conserver la source comme référence non mobilisée.
3. **Rechercher une destination pertinente à la source FO** : vérifier si un dossier sur l'épargne salariale/pouvoir d'achat existe ou est planifié. À défaut, la garder comme source isolée de contexte.
4. **Recalculer la couverture du graphe après les PR #154 et la PR complémentaire** : vérifier le nombre et le type d'objets isolés, les références entrantes et les éventuels doublons. Ne pas utiliser le nombre d'objets isolés comme objectif de performance.
5. **Ajouter des tests de graphe ciblés** : référence source/dossier absente, type de relation autorisé, identifiant dupliqué, justification manquante ou vide, et cohérence entre références explicites des dossiers et arêtes. Prévoir tests négatifs et fixtures synthétiques sans imposer de nouvelles relations aux sources de contexte.
6. **Étendre le rapport de couverture** : séparer sources non mobilisées, sources mobilisées dans le texte mais non liées, objets sans relation entrante/sortante et objets dont la relation est potentiellement redondante.
7. **Clore la revue uniquement après validation humaine** des liens, de la qualification des sources et de la cohérence des synthèses SMIC/TIG/no-platforming.

Aucune relation supplémentaire ne doit être créée pour les quatre sources ci-dessus tant qu'une mobilisation documentaire précise n'est pas établie.

