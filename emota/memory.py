"""Memory Subsystem Placeholder

Intended responsibilities (future):
- Short-term state buffering
- Episodic trace formation
- Retrieval & consolidation strategies
"""

import json
from pathlib import Path
from typing import Any, List, Dict, Sequence


class MemorySystem:
    def __init__(self, capacity: int = 1000) -> None:
        self._capacity: int = capacity
        self._episodes: List[Dict[str, Any]] = []

    def record(self, snapshot: Dict[str, Any]) -> None:  # pragma: no cover - simple logic
        self._episodes.append(snapshot)
        if len(self._episodes) > self._capacity:
            self._episodes.pop(0)

    def recent(self, n: int = 5) -> Sequence[Dict[str, Any]]:  # pragma: no cover - simple logic
        return self._episodes[-n:]

    def to_dict(self) -> Dict[str, Any]:  # pragma: no cover - serialization helper
        return {"capacity": self._capacity, "episodes": self._episodes}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):  # pragma: no cover
        inst = cls(capacity=int(data.get("capacity", 1000)))
        for ep in data.get("episodes", [])[-inst._capacity:]:
            if isinstance(ep, dict):
                inst.record(ep)
        return inst

    def save(self, path: str | Path) -> None:  # pragma: no cover - IO side effect
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)

    @classmethod
    def load(cls, path: str | Path):  # pragma: no cover - IO side effect
        p = Path(path)
        if not p.exists():
            return cls()
        with p.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return cls.from_dict(data)
