# 5G RAN Resource Allocation with Reinforcement Learning

Ce dossier fournit une structure pedagogique complete pour un projet etudiant de recherche/ingenierie sur l'allocation de ressources RAN 5G avec apprentissage par renforcement.

Objectif central:

> Apprendre a allouer dynamiquement des ressources radio limitees entre eMBB, URLLC et mMTC, puis comparer les approches RL aux baselines classiques sous contraintes QoS.

## Ce que contient ce dossier

- Un cadre projet en 5 niveaux progressifs
- Des documents de recherche et d'evaluation
- Des templates de livrables et de rapports
- Une specification claire de ce que l'enseignant fournit vs ce que les etudiants implementent

## Demarrage rapide

1. Lire [docs/project_description.md](docs/project_description.md)
2. Lire [docs/assignment_specification.md](docs/assignment_specification.md)
3. Lire les regles de generation de donnees dans [docs/synthetic_data.md](docs/synthetic_data.md)
4. Distribuer les templates dans [templates](templates)
5. Evaluer avec [rubrics/grading_rubric.md](rubrics/grading_rubric.md)

## Mode Open Project

Ce projet est en mode ouvert:

- Pas de timeline imposee
- Progression flexible selon le niveau de chaque equipe
- Validation par jalons techniques (simulateur, baselines, RL, analyse)

## Progression par niveaux

- Niveau 0: Comprendre le probleme 5G, slicing et QoS
- Niveau 1: Construire un simulateur simplifie
- Niveau 2: Implementer des baselines non-RL
- Niveau 3: Formuler le probleme en MDP et concevoir la reward
- Niveau 4: Evaluer des algorithmes RL
- Niveau 5: Etendre vers des axes de recherche avances

## Livrables minimaux attendus

1. Rapport de recherche
2. Depot de code reproductible
3. Simulateur fonctionnel
4. Au moins 3 baselines classiques
5. Au moins 1 methode RL
6. Experiences comparatives
7. Etude d'ablation
8. Discussion des resultats
9. Presentation finale

## Arborescence recommandee pour le depot etudiant

Voir [docs/recommended_repo_structure.md](docs/recommended_repo_structure.md).

## Note pedagogique

Ne pas imposer PPO au depart. Les etudiants doivent justifier leur formulation MDP, leur reward et leur choix d'algorithme en fonction des contraintes du probleme.

Les etudiants doivent aussi generer des donnees synthetiques pour entrainer et evaluer leurs politiques.
