# Incertitudes et révisions

## Pourquoi un registre ?

Le statut d'une affirmation ne suffit pas à décrire ce qui reste inconnu. Le registre d'incertitudes rend visibles les limites qui pourraient changer une conclusion, les données manquantes, les désaccords méthodologiques et les décisions de révision à prendre.

Il complète les fiches Claim ; il ne crée pas une seconde vérité concurrente. Une incertitude attachée à une affirmation doit référencer son identifiant canonique.

## Catégories d'incertitude

- **Mesure** : indicateur imparfait, définition variable, erreur ou données manquantes.
- **Échantillonnage** : couverture, représentativité, sélection ou attrition.
- **Causalité** : confusion résiduelle, endogénéité, hypothèses d'identification fragiles.
- **Modèle** : choix structurels, paramètres, sensibilité et spécification.
- **Transfert** : validité externe, comparabilité temporelle, géographique ou institutionnelle.
- **Source** : provenance, version, conflit d'intérêts ou vérification incomplète.
- **Normative** : critères de valeur contestés ou arbitrages non explicités.
- **Opérationnelle** : mise en œuvre réelle différente du dispositif théorique.

## Fiche de suivi minimale

Pour chaque incertitude importante, consigner :
- identifiant de l'affirmation ou de l'analyse concernée ;
- description précise de l'inconnue ;
- catégorie ;
- conséquence possible sur l'interprétation ;
- éléments disponibles et éléments manquants ;
- importance pour la conclusion (bloquante, majeure, secondaire) ;
- action de réduction ou raison de ne pas la réduire ;
- responsable ou rôle chargé du suivi, si pertinent ;
- date d'ouverture, prochaine revue et état.

## Journal des révisions

Une révision substantielle doit indiquer :
- date ;
- objet révisé ;
- ancienne et nouvelle formulation ou statut, lorsque cela est utile ;
- élément déclencheur (nouvelle donnée, étude, erratum, correction, critique ou changement de périmètre) ;
- conséquence sur la confiance et les conclusions ;
- liens vers les analyses et sources concernées.

Ne pas réécrire l'historique Git ni effacer une conclusion antérieure sans laisser de trace explicative.

## Modèle à copier

```yaml
id: UNCERTAINTY-EXAMPLE-001
claim_id: CLAIM-EXAMPLE-001
category: causal
description: "Des facteurs non observés peuvent encore différencier les groupes comparés."
importance: major
consequence: "L'effet causal estimé pourrait être surestimé ou sous-estimé."
evidence_available:
  - "Variables observées décrites dans l'étude."
missing_evidence:
  - "Mesure longitudinale plus complète des facteurs de sélection."
action: "Examiner les analyses de sensibilité et rechercher une réplication."
status: open
opened_at: YYYY-MM-DD
next_review: YYYY-MM-DD
```

Ce modèle est un format documentaire de travail, pas encore un objet validé par un schéma ou un registre automatisé. Ne pas créer d'identifiant d'incertitude dans le graphe avant l'adoption d'un contrat de données et de règles de validation.

## Garde-fous

- Une incertitude n'est pas nécessairement une faiblesse : elle peut être irréductible ou inhérente à la question.
- Ne pas convertir une liste d'incertitudes en score artificiel de qualité.
- Distinguer incertitude empirique, désaccord scientifique et désaccord normatif.
- Une absence de données ne justifie pas automatiquement une conclusion dans un sens ou dans l'autre.
- Les incertitudes majeures doivent être visibles dans la synthèse publique, pas enfouies dans les notes techniques.
