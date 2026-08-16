from __future__ import annotations

from dataclasses import dataclass


@dataclass
class StepMetrics:
    throughput: float
    latency: float
    packet_loss: float
    utilization: float


def jain_fairness(values: list[float]) -> float:
    if not values:
        return 0.0
    s = sum(values)
    sq = sum(v * v for v in values)
    if sq == 0:
        return 0.0
    n = len(values)
    return (s * s) / (n * sq)
