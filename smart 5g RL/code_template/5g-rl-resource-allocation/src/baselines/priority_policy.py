from __future__ import annotations


class PriorityPolicy:
    """Simple fixed-priority policy: URLLC > eMBB > mMTC."""

    def act(self, total_prbs: int, queues: dict[str, float]) -> dict[str, int]:
        alloc = {"embb": 0, "urllc": 0, "mmtc": 0}
        remaining = total_prbs

        urllc_need = int(min(remaining, queues.get("urllc", 0)))
        alloc["urllc"] = urllc_need
        remaining -= urllc_need

        embb_need = int(min(remaining, queues.get("embb", 0)))
        alloc["embb"] = embb_need
        remaining -= embb_need

        alloc["mmtc"] = remaining
        return alloc
