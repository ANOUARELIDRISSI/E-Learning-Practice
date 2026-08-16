from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass
class ChannelConfig:
    min_cqi: float = 0.2
    max_cqi: float = 1.0
    drift_std: float = 0.05


class ChannelModel:
    def __init__(self, cfg: ChannelConfig, rng: np.random.Generator) -> None:
        self.cfg = cfg
        self.rng = rng
        self.cqi = {"embb": 0.7, "urllc": 0.8, "mmtc": 0.6}

    def step(self) -> dict[str, float]:
        """Bounded random-walk CQI.

        TODO(STUDENT): Explore correlated fading models.
        """
        for k in self.cqi:
            self.cqi[k] += float(self.rng.normal(0.0, self.cfg.drift_std))
            self.cqi[k] = float(np.clip(self.cqi[k], self.cfg.min_cqi, self.cfg.max_cqi))
        return dict(self.cqi)
