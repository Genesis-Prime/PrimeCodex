"""Episodic Memory System

Lightweight bounded in-memory episodic buffer with optional JSON persistence.
Maintains insertion order; oldest episodes evicted beyond capacity.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class MemorySystem:
    def __init__(self, capacity: int = 1000, path: str | None = None):
        self.capacity = capacity
        self._episodes: list[dict[str, Any]] = []
        self.path: Path | None = Path(path) if path else None
        if self.path and self.path.exists():  # pragma: no cover - simple load path
            try:
                data = json.loads(self.path.read_text())
            except Exception as exc:  # pragma: no cover - defensive
                logger.warning("Failed to read memory payload %s: %s", self.path, exc)
                data = None
            if isinstance(data, dict):
                episodes = data.get("episodes", [])
                if isinstance(data.get("capacity"), int) and data["capacity"] > 0:
                    self.capacity = data["capacity"]
            else:
                episodes = data if isinstance(data, list) else []

            for item in episodes[-self.capacity:]:
                if isinstance(item, dict):
                    self._episodes.append(item)

    def record(self, snapshot: dict[str, Any]) -> None:
        self._episodes.append(snapshot)
        if len(self._episodes) > self.capacity:
            self._episodes.pop(0)
        self._persist_if_configured()

    def recent(self, n: int = 5) -> list[dict[str, Any]]:
        return self._episodes[-n:]

    def to_list(self) -> list[dict[str, Any]]:
        return list(self._episodes)

    def _persist_if_configured(self) -> None:
        if not self.path:
            return
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            payload = {
                "capacity": self.capacity,
                "episodes": self._episodes[-self.capacity:],
            }
            self.path.write_text(json.dumps(payload))
        except Exception as exc:  # pragma: no cover - defensive
            logger.exception("Failed to persist memory payload %s", exc)
