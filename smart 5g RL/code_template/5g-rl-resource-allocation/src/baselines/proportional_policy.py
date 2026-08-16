from __future__ import annotations


class ProportionalPolicy:
    def act(self, total_prbs: int, queues: dict[str, float]) -> dict[str, int]:
        total_demand = sum(max(0.0, q) for q in queues.values())
        if total_demand <= 0:
            return {"embb": total_prbs // 3, "urllc": total_prbs // 3, "mmtc": total_prbs - 2 * (total_prbs // 3)}

        raw = {k: (queues[k] / total_demand) * total_prbs for k in ["embb", "urllc", "mmtc"]}
        alloc = {k: int(raw[k]) for k in raw}
        assigned = sum(alloc.values())

        for k in sorted(raw, key=raw.get, reverse=True):
            if assigned >= total_prbs:
                break
            alloc[k] += 1
            assigned += 1
        return alloc
