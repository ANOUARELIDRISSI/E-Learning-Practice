from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass
class TrafficConfig:
    embb_lambda: float = 12.0
    urllc_lambda: float = 6.0
    mmtc_lambda: float = 20.0


class TrafficGenerator:
    def __init__(self, cfg: TrafficConfig, rng: np.random.Generator) -> None:
        self.cfg = cfg
        self.rng = rng

    def sample_arrivals(self) -> dict[str, int]:
        """Synthetic arrivals per step.

        TODO(STUDENT): Replace with bursty or time-varying profile.
        """
        return {
            "embb": int(self.rng.poisson(self.cfg.embb_lambda)),
            "urllc": int(self.rng.poisson(self.cfg.urllc_lambda)),
            "mmtc": int(self.rng.poisson(self.cfg.mmtc_lambda)),
        }
