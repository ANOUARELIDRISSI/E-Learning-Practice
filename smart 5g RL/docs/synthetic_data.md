# Synthetic Data Generation Guide

## Objective

Students must generate synthetic data to train and evaluate resource-allocation policies in a fully reproducible way.

## Why Synthetic Data

- Reproducible experiments
- Controlled stress scenarios
- No dependency on proprietary operator traces
- Easier ablation and robustness testing

## Data to Generate per Time Step

1. Traffic arrivals by class
2. Channel quality indicators by class or user
3. Packet deadlines/latency budget (especially URLLC)
4. Optional random events (bursts, fades, outages)

## Minimal Schema

At time step t, generate:

- embb_arrivals_bits
- urllc_arrivals_packets
- mmtc_arrivals_packets
- embb_cqi
- urllc_cqi
- mmtc_cqi
- optional_event_flag

## Suggested Generators

## Traffic

- eMBB: high-rate, burst-capable process
- URLLC: small packets with strict deadlines
- mMTC: many low-size sporadic arrivals

Example choices:

- Poisson arrivals for baseline
- Markov-modulated process for bursty traffic
- Time-of-day profile multiplier for load variation

## Channel

- Start simple: bounded random walk for CQI
- Advanced: fading-inspired stochastic process with correlation

## Random Seed Policy

Use at least 3 fixed seeds for all compared methods.

Example:

- seed_train = [11, 22, 33]
- seed_eval = [101, 202, 303]

## Scenario Packs (Required)

Create at least these synthetic scenario sets:

1. Balanced traffic
2. URLLC-heavy stress
3. mMTC-heavy stress
4. Bursty mixed traffic
5. Degraded channel condition

## Output Format

Allow two modes:

- Online generation inside environment step loop
- Offline generated traces saved as CSV or Parquet

Required fields if offline:

- time_step
- class_or_user_id
- arrivals
- cqi
- deadline_ms (if applicable)
- scenario_id
- seed

## Validation Checks

Before training, verify:

- Non-negative arrivals
- CQI bounds respected
- Reproducibility across identical seed
- Distinct behavior across scenarios

## Student Deliverable for Data

Each team must submit:

1. Data-generation code
2. Generator configuration file
3. Short note explaining distributions and assumptions
4. Sanity plots for arrivals and CQI over time
