from __future__ import annotations


class RoundRobinPolicy:
    def __init__(self) -> None:
        self.order = ["embb", "urllc", "mmtc"]
        self.offset = 0

    def act(self, total_prbs: int) -> dict[str, int]:
        alloc = {"embb": 0, "urllc": 0, "mmtc": 0}
        for i in range(total_prbs):
            target = self.order[(self.offset + i) % 3]
            alloc[target] += 1
        self.offset = (self.offset + 1) % 3
        return alloc
