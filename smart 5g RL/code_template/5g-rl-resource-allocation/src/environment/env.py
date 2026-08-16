from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from .channel import ChannelConfig, ChannelModel
from .metrics import StepMetrics
from .traffic import TrafficConfig, TrafficGenerator
from .users import UserGroup


@dataclass
class EnvConfig:
    total_prbs: int = 50
    max_steps: int = 500
    seed: int = 11


class ResourceAllocationEnv:
    """Minimal 5G RAN environment.

    Action format: dict with integer PRBs per class.
    Example: {"embb": 20, "urllc": 20, "mmtc": 10}
    """

    def __init__(self, cfg: EnvConfig | None = None) -> None:
        self.cfg = cfg or EnvConfig()
        self.rng = np.random.default_rng(self.cfg.seed)
        self.traffic = TrafficGenerator(TrafficConfig(), self.rng)
        self.channel = ChannelModel(ChannelConfig(), self.rng)
        self.users = {
            "embb": UserGroup("embb"),
            "urllc": UserGroup("urllc"),
            "mmtc": UserGroup("mmtc"),
        }
        self.step_count = 0

    def reset(self) -> dict[str, float]:
        self.step_count = 0
        for group in self.users.values():
            group.queue = 0.0
            group.transmitted_last_step = 0.0
        self.channel = ChannelModel(ChannelConfig(), self.rng)
        return self._get_state()

    def step(self, action: dict[str, int]) -> tuple[dict[str, float], float, bool, dict]:
        self.step_count += 1

        self._validate_action(action)
        arrivals = self.traffic.sample_arrivals()
        cqi = self.channel.step()

        for k in self.users:
            self.users[k].queue += arrivals[k]

        transmitted = {}
        for k in self.users:
            capacity = action[k] * cqi[k]
            tx = min(self.users[k].queue, capacity)
            self.users[k].queue -= tx
            self.users[k].transmitted_last_step = tx
            transmitted[k] = tx

        metrics = self._compute_metrics(action, transmitted)
        reward = self._compute_reward(metrics)
        done = self.step_count >= self.cfg.max_steps
        info = {
            "arrivals": arrivals,
            "cqi": cqi,
            "transmitted": transmitted,
            "metrics": metrics,
        }
        return self._get_state(), reward, done, info

    def _get_state(self) -> dict[str, float]:
        # TODO(STUDENT): Expand representation with richer features.
        return {
            "available_prbs": float(self.cfg.total_prbs),
            "embb_queue": float(self.users["embb"].queue),
            "urllc_queue": float(self.users["urllc"].queue),
            "mmtc_queue": float(self.users["mmtc"].queue),
            "embb_cqi": float(self.channel.cqi["embb"]),
            "urllc_cqi": float(self.channel.cqi["urllc"]),
            "mmtc_cqi": float(self.channel.cqi["mmtc"]),
        }

    def _validate_action(self, action: dict[str, int]) -> None:
        required = {"embb", "urllc", "mmtc"}
        if set(action.keys()) != required:
            raise ValueError("Action must include embb, urllc, mmtc keys")
        if any(v < 0 for v in action.values()):
            raise ValueError("PRB values must be non-negative")
        if sum(action.values()) > self.cfg.total_prbs:
            raise ValueError("Action exceeds total PRB budget")

    def _compute_metrics(self, action: dict[str, int], transmitted: dict[str, float]) -> StepMetrics:
        throughput = float(sum(transmitted.values()))
        latency_proxy = float(self.users["urllc"].queue)
        queue_total = float(sum(u.queue for u in self.users.values()))
        packet_loss_proxy = max(0.0, queue_total - 1000.0) / 1000.0
        utilization = float(sum(action.values()) / self.cfg.total_prbs)
        return StepMetrics(
            throughput=throughput,
            latency=latency_proxy,
            packet_loss=packet_loss_proxy,
            utilization=utilization,
        )

    def _compute_reward(self, m: StepMetrics) -> float:
        # TODO(STUDENT): Replace with justified multi-objective reward.
        return (1.0 * m.throughput) - (2.0 * m.latency) - (5.0 * m.packet_loss)
