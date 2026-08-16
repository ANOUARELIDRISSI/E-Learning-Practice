# 5G RL Resource Allocation - Student Code Template

This is a starter template for the open project on 5G RAN resource allocation using reinforcement learning.

## Learning Goal

Build a simulator, compare classical baselines, then design and evaluate RL methods for eMBB, URLLC, and mMTC allocation.

## Project Status

What is provided:

- Runnable simulator skeleton
- Synthetic data generator
- Baseline policy interfaces and simple implementations
- Experiment entry points
- Unit-test skeleton

What students must complete:

- Better state representation
- Better action representation
- Reward engineering
- RL algorithm implementations
- Training strategy and hyperparameter tuning
- Robust evaluation and ablations

## Setup with uv (required)

1. Install uv:

```powershell
pip install uv
```

2. Create virtual environment:

```powershell
uv venv
```

3. Activate environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Install project in editable mode with dev dependencies:

```powershell
uv pip install -e .[dev]
```

## Quick Start

Generate synthetic data:

```powershell
python scripts/generate_synthetic_data.py --steps 2000 --seed 11 --output data/synthetic_trace.csv
```

Run baseline experiment:

```powershell
python experiments/baseline_experiments.py
```

Run tests:

```powershell
pytest -q
```

## Suggested Workflow

1. Read comments marked TODO(STUDENT).
2. Validate simulator with baselines first.
3. Add RL method and compare against baselines.
4. Report metrics beyond reward (latency, loss, fairness, reliability).
