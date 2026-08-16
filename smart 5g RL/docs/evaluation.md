# Evaluation Protocol

## Rule 1

Do not evaluate solely by RL reward.

## Metrics to Report

## Network Performance

- Total throughput
- Average throughput per user/class
- Spectral efficiency
- Resource utilization

## QoS

- Average latency
- P95 latency
- P99 latency
- Packet loss rate
- Reliability
- QoS violation rate

## Fairness

- Jain fairness index

## RL Behavior

- Episode reward
- Convergence speed
- Training stability
- Inference time per step

## Required Plots

- Throughput vs time
- Latency vs time
- Packet loss vs time
- Resource allocation shares vs time
- Reward vs episode
- QoS violations vs episode

## Experiment Design Minimum

1. Fixed random seeds (at least 3)
2. Same simulator conditions for all methods
3. Hyperparameter table
4. Runtime and compute budget notes
5. Statistical summary (mean and standard deviation)

## Ablation Suggestions

- Remove channel features from state
- Modify reward weights
- Remove latency penalty
- Change action granularity
- Evaluate under traffic shift and channel degradation
