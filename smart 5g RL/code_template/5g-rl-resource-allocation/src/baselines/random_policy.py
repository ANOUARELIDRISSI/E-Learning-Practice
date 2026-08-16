from __future__ import annotations

import numpy as np


class RandomPolicy:
    def __init__(self, seed: int = 11) -> None:
        self.rng = np.random.default_rng(seed)

    def act(self, total_prbs: int) -> dict[str, int]:
        cuts = sorted(self.rng.integers(0, total_prbs + 1, size=2).tolist())
        embb = cuts[0]
        urllc = cuts[1] - cuts[0]
        mmtc = total_prbs - cuts[1]
        return {"embb": int(embb), "urllc": int(urllc), "mmtc": int(mmtc)}
