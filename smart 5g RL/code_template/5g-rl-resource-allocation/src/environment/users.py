from __future__ import annotations

from dataclasses import dataclass


@dataclass
class UserGroup:
    name: str
    queue: float = 0.0
    transmitted_last_step: float = 0.0
