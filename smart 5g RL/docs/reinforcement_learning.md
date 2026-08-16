# Reinforcement Learning Guidance

## Pedagogical Principle

Students must not begin with an RL library and default PPO.

They must first:

1. Understand the networking problem
2. Build the simulator
3. Establish classical baselines
4. Then formalize RL

## MDP Elements

## State

Minimal state can include:

- available_prbs
- queue lengths by class
- optional per-class channel quality
- optional current latency indicators (especially URLLC)

Students should justify and iteratively improve representation.

## Action

Example aggregated action:

- PRBs_eMBB
- PRBs_URLLC
- PRBs_mMTC

Subject to budget constraint:

PRBs_eMBB + PRBs_URLLC + PRBs_mMTC <= total_PRBs

## Reward

Do not provide a fixed final formula.

Students should design and justify a weighted objective balancing:

- Throughput gains
- Latency penalties
- Packet loss penalties
- QoS violation penalties
- Resource waste penalties

## Algorithm Pathway

- Beginner: tabular Q-learning on very simplified settings
- Intermediate: DQN with discretized action space
- Advanced: PPO or constrained variants for richer action/state spaces

## Required Comparison

RL results are only meaningful if compared against strong baselines.

Minimum comparison set:

- Random
- Round Robin
- Priority-based
- Proportional allocation
- At least one RL method
