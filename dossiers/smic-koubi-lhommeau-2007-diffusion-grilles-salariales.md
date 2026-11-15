# Koubi & Lhommeau (2007) — diffusion des hausses du SMIC dans les grilles salariales (2000–2005)

**Référence complète.** Malik Koubi et Bertrand Lhommeau (Dares), « Les effets de diffusion de court terme des hausses du Smic dans les grilles salariales des entreprises de dix salariés ou plus sur la période 2000-2005 », dans *Les salaires en France, édition 2007*, Insee Références, dossier, pp. 67–81. Publication Insee du 1er novembre 2007.

- Page Insee : https://www.insee.fr/fr/statistiques/1373191
- PDF de l'ouvrage (chapitre pp. 67–81) : https://www.bnsp.insee.fr/ark:/12148/bc6p07d21j6.pdf
- Notice Insee : https://www.insee.fr/fr/statistiques/1373191?q=augmentation+du+smic&sommaire=1373193

## 1. Question, population et période

Les auteurs cherchent à mesurer comment une revalorisation du SMIC se transmet aux salaires de base situés au-dessus du minimum, selon leur position dans la hiérarchie salariale et selon le délai écoulé depuis la revalorisation.

La période d'observation couvre 2000–2005, période particulièrement délicate : les hausses du SMIC sont fortes, notamment 2003–2005, mais elles se superposent à la convergence des garanties mensuelles de rémunération (GMR) et du SMIC horaire après le passage aux 35 heures. Il ne s'agit donc pas d'une succession de hausses « pures » du SMIC.

Champ : entreprises/établissements de 10 salariés ou plus du secteur marchand non agricole. L'enquête Acemo trimestrielle interroge environ 20 000 entreprises dans le dispositif d'étude (34 000 unités dans l'enquête source avant filtres ; établissements de 250 salariés ou plus enquêtés exhaustivement). Les unités de moins de 500 salariés restent quatre ans dans l'échantillon ; les plus grandes sont suivies de façon permanente.

Les auteurs suivent des **postes représentatifs de grilles salariales**, pas des individus : 12 niveaux-types, construits à partir de quatre catégories socioprofessionnelles (ouvriers, employés, professions intermédiaires, cadres) et trois niveaux de qualification pour chacune.

Sur 2 594 094 observations initiales, les filtres conservent 1 973 738 observations représentant 151 590 postes différents. Sont notamment éliminés ou corrigés les salaires et horaires extrêmes, les évolutions suspectes, les postes de moins de 100 heures mensuelles et les postes observés moins de sept trimestres. Ces filtres visent à réduire les changements de composition et les erreurs de suivi des postes.

## 2. Données et variables

Source principale : enquête trimestrielle Acemo de la Dares. Elle fournit pour chaque poste-type un salaire brut de base, un horaire mensuel et la catégorie/niveau de qualification. Les primes, compléments de salaire, heures supplémentaires individualisées et épargne salariale ne sont pas inclus.

Les auteurs apparient Acemo à la base Dares-Urssaf de suivi de la réduction du temps de travail afin d'identifier la date de passage à 35 heures et la GMR applicable. Cette base ne couvre toutefois pas tous les établissements passés à 35 heures : elle repose sur les déclarations ouvrant droit aux allégements Aubry II et comporte des exclusions et des dates parfois imparfaitement renseignées.

Le salaire minimum de référence est construit comme une moyenne pondérée du SMIC et des différentes GMR, selon les effectifs concernés. La tranche salariale de chaque poste est exprimée relativement au SMIC ou à la GMR pertinente.

Deux résultats sont étudiés :
- salaire horaire de base ;
- salaire mensuel de base.

Les auteurs n'étudient ni les rémunérations totales, ni le revenu disponible, ni l'emploi, les heures effectivement travaillées, les prix ou les marges.

## 3. Stratégie empirique

Le modèle porte sur la variation logarithmique du salaire de base du poste i au trimestre t :

```text
Δlog(wᵢₜ) = effets temporels
          + caractéristiques entreprise (secteur/taille ou effets fixes)
          + effets de la RTT
          + catégorie socioprofessionnelle
          + tranche salariale relative au minimum
          + (tranche salariale × variation du minimum)
          + résidu
```

La variable d'évolution du minimum est la moyenne pondérée du SMIC et des GMR. Son interaction avec les tranches de salaire permet d'estimer une élasticité distincte à chaque niveau de la grille.

Les spécifications trimestrielles exploitent davantage de variation temporelle. Les spécifications annuelles ne disposent que de cinq points annuels ; les auteurs avertissent que les comportements d'entreprise et l'hétérogénéité non observée pèsent davantage à cet horizon. Les variantes comprennent des contrôles secteur/taille, puis des effets fixes d'entreprise ; les auteurs indiquent également des estimations avec effets fixes de poste.

**Il ne s'agit pas d'une différence-de-différences avec groupe témoin externe, ni d'une discontinuité autour d'un seuil.** L'identification repose sur la variation temporelle des minima, les différences d'exposition selon les tranches salariales et les contrôles introduits. La causalité doit donc être interprétée avec prudence.

## 4. Résultats chiffrés

### 4.1. Effet à un trimestre

Dans la spécification trimestrielle avec effets fixes d'entreprise, une hausse de 1 % du minimum est associée à :
- +0,392 % pour les salaires entre 1 et 1,1 SMIC ;
- +0,202 % entre 1,1 et 1,2 SMIC ;
- +0,155 % entre 1,2 et 1,3 SMIC ;
- +0,116 % entre 1,3 et 1,4 SMIC ;
- +0,069 % entre 1,4 et 1,5 SMIC.

Les résultats sans effets fixes d'entreprise sont très proches. L'effet est donc fortement concentré au voisinage du minimum dans les premiers mois.

### 4.2. Effet à un an

Les estimations annuelles sont plus élevées, mais plus sensibles aux effets fixes d'entreprise :
- 1–1,1 SMIC : 0,473 sans effets fixes d'entreprise ; 1,188 avec effets fixes ;
- 1,1–1,2 SMIC : 0,358 ; 0,796 ;
- 1,2–1,3 SMIC : 0,287 ; 0,520 ;
- 1,3–1,4 SMIC : 0,271 ; 0,357 ;
- 1,4–1,5 SMIC : 0,311 ; 0,490.

Les auteurs demandent explicitement de traiter les élasticités supérieures à 1 avec la marge d'incertitude du modèle et de les lire comme « proches de l'unité », non comme une transmission précisément supérieure à 100 %.

Le délai est substantiel : pour les postes à 1,4–1,5 SMIC, l'effet estimé passe de 0,07 % à un trimestre à 0,31–0,49 % à un an. Pour cette tranche, l'effet immédiat représente seulement 14 à 22 % de l'effet annuel. Les auteurs situent une partie de l'ajustement différé au premier trimestre de l'année suivant la hausse du SMIC.

### 4.3. Descriptif des revalorisations 2000–2005

Entre le deuxième et le troisième trimestre, les salaires horaires de base progressent en moyenne de 1,8 % pour les postes à 1–1,1 SMIC, 1,3 % à 1,1–1,2 SMIC, 1 % à 1,2–1,3 SMIC ; la progression est au plus de 0,6 % au-dessus de 1,4 SMIC.

La proportion de salariés concernés par les relèvements du SMIC ou de la GMR au 1er juillet passe de 13,6 % en 2000 à 16,3 % en 2005 (champ excluant notamment apprentis, secteur public local et d'État, agriculture, intérim et domestique). Il s'agit d'une mesure de l'exposition directe aux minima, pas de la part totale bénéficiant de la diffusion indirecte.

## 5. Mécanismes proposés

Les auteurs soulignent la volonté des partenaires sociaux de préserver une hiérarchie salariale cohérente dans l'entreprise. La diffusion peut être simultanée, par indexation partielle des différents niveaux de grille, mais aussi différée lors des négociations salariales ultérieures.

La corrélation temporelle entre revalorisations de postes de grille est élevée : les postes ouvriers et employés subissent le « même traitement » dans plus de 82 % des cas, tandis que la corrélation entre postes cadres et ouvriers est plus faible, autour de 76 %. « Même traitement » signifie ici revalorisation (pas nécessairement du même montant) ou absence de revalorisation au même trimestre.

Les résultats montrent aussi que, toutes choses modélisées égales par ailleurs, les salaires ont une dynamique spontanée plus favorable en haut de la hiérarchie ; la hausse du minimum compense en partie ce désavantage relatif des bas salaires.

## 6. Audit critique et limites

1. **Petites entreprises exclues.** Le champ commence à 10 salariés. Les auteurs rappellent que 41 % des salariés rémunérés au SMIC travaillent dans les entreprises de moins de 10 salariés. La validité externe pour une partie importante des bénéficiaires directs est donc limitée.
2. **Postes, pas personnes.** La méthode suit des postes représentatifs de grilles ; elle ne mesure pas les carrières individuelles, les changements d'employeur, les sorties de l'emploi ou les effets de composition à l'échelle de la main-d'œuvre.
3. **Salaire de base seulement.** Les primes et compléments, qui représentent selon les références citées 12,6 % de la rémunération moyenne et 13,1 % pour les salariés au SMIC, ne sont pas mesurés. Une substitution entre salaire de base et compléments pourrait atténuer la transmission sur la rémunération totale.
4. **RTT et GMR.** Les revalorisations 2000–2005 sont imbriquées dans la convergence des minima après la réduction du temps de travail. Le minimum utilisé est un agrégat pondéré du SMIC et des GMR : les estimations ne sont pas l'effet d'une hausse isolée du SMIC horaire.
5. **Mesure imparfaite du traitement RTT.** La base d'appariement ne couvre pas tous les établissements passés aux 35 heures et certaines dates/variables sont imparfaitement renseignées.
6. **Identification non expérimentale.** Les effets temporels, la conjoncture salariale et le SMIC sont simultanément déterminés. La règle d'indexation du SMIC inclut la moitié des gains de pouvoir d'achat du SHBO, ce qui introduit une circularité potentielle entre salaire de base et minimum.
7. **Estimation annuelle fragile.** Seulement cinq observations annuelles et une forte sensibilité aux effets fixes d'entreprise. Les estimations dépassant l'unité doivent être lues comme proches de l'unité selon les auteurs.
8. **Pas d'évaluation de l'emploi.** Le papier ne permet pas de conclure sur les embauches, destructions d'emplois, heures, prix, marges, productivité ou coût budgétaire.

## 7. Synthèse probatoire

**Constat robuste dans le champ observé :** les revalorisations du minimum se diffusent au-delà du salaire directement concerné, et la diffusion décroît avec la distance au minimum à court terme. Elle est plus lente et plus importante à un an pour les salaires intermédiaires.

**Ordres de grandeur :** à un trimestre, +1 % du minimum est associé à environ +0,39 % du salaire de base entre 1 et 1,1 SMIC, mais seulement +0,07 % entre 1,4 et 1,5 SMIC. À un an, les estimations correspondantes sont environ +0,47 à +1,19 % et +0,31 à +0,49 %, selon la spécification.

**Limite de causalité :** les auteurs mesurent une transmission conditionnelle au sein de grilles d'entreprises, dans un contexte de convergence des GMR et de RTT. Il ne faut pas transformer ces coefficients en effets causaux universels, ni les extrapoler aux TPE, aux rémunérations totales ou à l'emploi.

**Conclusion opérationnelle pour le dossier SMIC :** une revalorisation n'améliore pas uniquement le salaire des personnes exactement au minimum ; elle comprime et réorganise une partie de la hiérarchie salariale, avec un effet diffusé dans le temps. L'ampleur dépend du niveau de salaire, des pratiques de négociation, de la taille de l'entreprise et des règles institutionnelles. Cela établit un mécanisme salarial, pas un bilan global bénéfice/coût.

## 8. Références connexes à confronter

- Cette, Chouard & Verdugo (2011/2012), « Les effets des hausses du Smic sur le salaire moyen », *Économie et Statistique* n°448–449 : série agrégée 1970–2009 et décomposition des causes de revalorisation.
- Goaran & Muller (2011), « Les effets des hausses du Smic sur les salaires mensuels dans les entreprises de dix salariés ou plus de 2006 à 2009 » : prolongement sur la période postérieure.
- Lhommeau (2005), « Les perspectives salariales des bas salaires dans les années 1990 » : mobilité salariale individuelle, objet distinct de la diffusion des grilles.
