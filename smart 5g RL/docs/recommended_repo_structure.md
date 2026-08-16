# Recommended Repository Structure

```text
5g-rl-resource-allocation/
|
|-- README.md
|-- docs/
|   |-- project_description.md
|   |-- 5g_background.md
|   |-- reinforcement_learning.md
|   |-- evaluation.md
|   `-- research_questions.md
|
|-- src/
|   |-- environment/
|   |   |-- __init__.py
|   |   |-- env.py
|   |   |-- users.py
|   |   |-- traffic.py
|   |   |-- channel.py
|   |   `-- metrics.py
|   |
|   |-- baselines/
|   |   |-- random_policy.py
|   |   |-- round_robin.py
|   |   `-- priority_policy.py
|   |
|   |-- agents/
|   |   |-- q_learning.py
|   |   |-- dqn.py
|   |   `-- ppo.py
|   |
|   `-- utils/
|       |-- config.py
|       `-- logger.py
|
|-- experiments/
|   |-- baseline_experiments.py
|   |-- train_dqn.py
|   |-- train_ppo.py
|   `-- evaluate.py
|
|-- notebooks/
|   |-- 01_environment_demo.ipynb
|   |-- 02_baselines.ipynb
|   `-- 03_results_analysis.ipynb
|
|-- tests/
|   |-- test_environment.py
|   |-- test_allocation.py
|   `-- test_metrics.py
|
|-- results/
|   `-- .gitkeep
|
|-- requirements.txt
`-- .gitignore
```

## Advice

Use this as a target architecture, not a hard constraint. Teams may adapt structure if reproducibility and clarity are preserved.
