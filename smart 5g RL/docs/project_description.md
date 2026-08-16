# Project Description

## Title

5G RAN Resource Allocation using Reinforcement Learning

## Problem Statement

A 5G base station serves heterogeneous traffic classes with conflicting QoS goals:

- eMBB: high throughput demand
- URLLC: very low latency and high reliability
- mMTC: large number of devices with low-rate traffic

The project asks whether an RL policy can outperform classical allocation strategies while maintaining service-level QoS targets.

## Core Research Question

Can reinforcement learning learn a resource-allocation policy that improves system performance compared to traditional strategies, while respecting eMBB, URLLC and mMTC constraints?

## Simplified Environment Assumptions

- Single cell/base station
- Fixed total PRB budget per time step
- Time-slotted operation
- Traffic arrivals per class
- Optional channel variation (for advanced levels)

## Why this matters

This project sits at the intersection of:

- Wireless networking
- Optimization under constraints
- Sequential decision-making under uncertainty
- Applied machine learning and reproducibility

## Learning Outcomes

By the end, students should be able to:

1. Model a wireless resource allocation problem as an MDP.
2. Build and validate a simulation environment.
3. Design and benchmark classical and RL policies.
4. Define meaningful metrics beyond training reward.
5. Produce research-quality experimental evidence.
