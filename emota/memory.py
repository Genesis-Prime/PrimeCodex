"""Memory Subsystem Placeholder

Intended responsibilities (future):
- Short-term state buffering
- Episodic trace formation
- Retrieval & consolidation strategies
"""

class MemorySystem:
    def __init__(self):
        self._episodes = []

    def record(self, snapshot):  # pragma: no cover - trivial placeholder
        self._episodes.append(snapshot)
        if len(self._episodes) > 1000:
            self._episodes.pop(0)

    def recent(self, n=5):  # pragma: no cover - trivial placeholder
        return self._episodes[-n:]
