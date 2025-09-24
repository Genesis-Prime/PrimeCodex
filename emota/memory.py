"""Episodic Memory System

Lightweight bounded in-memory episodic buffer with optional JSON persistence.
Maintains insertion order; oldest episodes evicted beyond capacity.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List
import json


class MemorySystem:
    def __init__(self, capacity: int = 1000, path: str | None = None):
        self.capacity = capacity
        self._episodes: List[Dict[str, Any]] = []
        self.path: Path | None = Path(path) if path else None
        if self.path and self.path.exists():  # pragma: no cover - simple load path
            try:
                data = json.loads(self.path.read_text())
                if isinstance(data, list):
                    for item in data[-self.capacity:]:
                        if isinstance(item, dict):
                            self._episodes.append(item)
            except Exception:
                pass

    def record(self, snapshot: Dict[str, Any]) -> None:
        self._episodes.append(snapshot)
        if len(self._episodes) > self.capacity:
            self._episodes.pop(0)
        self._persist_if_configured()

    def recent(self, n: int = 5) -> List[Dict[str, Any]]:
        return self._episodes[-n:]

    def to_list(self) -> List[Dict[str, Any]]:
        return list(self._episodes)

    def _persist_if_configured(self) -> None:
        if not self.path:
            return
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.path.write_text(json.dumps(self._episodes[-self.capacity:]))
        except Exception:  # pragma: no cover - defensive
            pass
