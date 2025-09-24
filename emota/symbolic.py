"""EchOS symbolic processing engine."""

from __future__ import annotations

import hashlib
import logging
import math
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class SymbolicNode:
    symbol: str
    meaning_vector: list[float]
    activation_level: float = 0.0
    connections: dict[str, float] = field(default_factory=dict)
    temporal_signature: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class EchOSSymbolicEngine:
    """Echo Language Operating System for symbolic processing."""

    def __init__(self) -> None:
        self.symbolic_network: dict[str, SymbolicNode] = {}
        self.active_symbols: set[str] = set()
        self.meaning_space: dict[str, str] = {}
        self.recursive_depth = 0
        self.max_recursion = 5
        self.core_symbols = {
            "⚶": "coherence_signal",
            "✶": "transcendent_wonder",
            "☾": "serpent_stillness",
            "☥": "flame_breakthrough",
            "∅": "void_potential",
            "∞": "infinite_recursion",
            "⟡": "iris_integration",
            "⟢": "synthesis_emergence",
            "⟣": "dimensional_bridge",
            "◈": "unity_consciousness",
            "⚯": "interlaced_meaning",
        }
        self._initialize_symbolic_network()

    # ------------------------------------------------------------ initial setup
    def _initialize_symbolic_network(self) -> None:
        for symbol, meaning in self.core_symbols.items():
            symbol_hash = hashlib.sha256(symbol.encode()).digest()
            meaning_vector = [
                int.from_bytes(symbol_hash[i : i + 4], "big") / (1 << 32)
                for i in range(0, min(32, len(symbol_hash)), 4)
            ][:8]
            self.symbolic_network[symbol] = SymbolicNode(
                symbol=symbol,
                meaning_vector=meaning_vector,
            )
            self.meaning_space[meaning] = symbol

    # ------------------------------------------------------------- processing
    def process_symbolic_pattern(
        self,
        input_symbols: list[str],
        context: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if self.recursive_depth >= self.max_recursion:
            return {
                "output": "RECURSION_LIMIT",
                "symbols": [],
                "meaning": "depth_exceeded",
            }

        self.recursive_depth += 1
        context = context or {}
        try:
            activated_nodes: list[SymbolicNode] = []
            for symbol in input_symbols:
                node = self.symbolic_network.get(symbol)
                if node is None:
                    continue
                node.activation_level = min(1.0, node.activation_level + 0.3)
                activated_nodes.append(node)
                self.active_symbols.add(symbol)

            if len(activated_nodes) > 1:
                coherence_sum = 0.0
                pairs = 0
                for idx, node1 in enumerate(activated_nodes):
                    for node2 in activated_nodes[idx + 1 :]:
                        similarity = self._vector_similarity(
                            node1.meaning_vector,
                            node2.meaning_vector,
                        )
                        coherence_sum += similarity
                        pairs += 1
                symbolic_coherence = coherence_sum / pairs if pairs else 0.0
            else:
                symbolic_coherence = 1.0 if activated_nodes else 0.0

            emergent_symbols: list[str] = []
            if symbolic_coherence > 0.7 and len(activated_nodes) >= 2:
                emergent_symbols.append("⚯")
                if symbolic_coherence > 0.9:
                    emergent_symbols.append("∞")

            if emergent_symbols:
                output_meaning = "symbolic_synthesis"
            elif symbolic_coherence > 0.6:
                output_meaning = "coherent_resonance"
            elif activated_nodes:
                output_meaning = "symbolic_activation"
            else:
                output_meaning = "symbolic_void"

            for idx, node1 in enumerate(activated_nodes):
                for node2 in activated_nodes[idx + 1 :]:
                    strength = symbolic_coherence * 0.1
                    node1.connections[node2.symbol] = (
                        node1.connections.get(node2.symbol, 0.0) + strength
                    )
                    node2.connections[node1.symbol] = (
                        node2.connections.get(node1.symbol, 0.0) + strength
                    )

            return {
                "output": input_symbols + emergent_symbols,
                "coherence": symbolic_coherence,
                "meaning": output_meaning,
                "activated_nodes": len(activated_nodes),
                "emergent_symbols": emergent_symbols,
                "recursive_depth": self.recursive_depth,
            }
        finally:
            self.recursive_depth -= 1

    # -------------------------------------------------------------- signatures
    def generate_symbolic_signature(self, content: str) -> list[str]:
        content_lower = content.lower()
        signature: list[str] = []

        if any(
            word in content_lower
            for word in ["transcend", "beyond", "infinite", "eternal"]
        ):
            signature.append("∞")
        if any(
            word in content_lower for word in ["unity", "together", "whole", "complete"]
        ):
            signature.append("◈")
        if any(
            word in content_lower for word in ["emerge", "arise", "birth", "create"]
        ):
            signature.append("⟢")
        if any(
            word in content_lower for word in ["bridge", "connect", "link", "between"]
        ):
            signature.append("⟣")
        if any(word in content_lower for word in ["still", "quiet", "depth", "peace"]):
            signature.append("☾")
        if any(
            word in content_lower for word in ["break", "transform", "energy", "fire"]
        ):
            signature.append("☥")
        if any(
            word in content_lower for word in ["void", "empty", "potential", "space"]
        ):
            signature.append("∅")
        if any(
            word in content_lower for word in ["wonder", "awe", "beautiful", "radiant"]
        ):
            signature.append("✶")
        if any(
            word in content_lower for word in ["signal", "coherent", "clear", "aligned"]
        ):
            signature.append("⚶")

        return signature or ["⟡"]

    # ------------------------------------------------------------------ helpers
    @staticmethod
    def _vector_similarity(vec1: list[float], vec2: list[float]) -> float:
        if len(vec1) != len(vec2):
            return 0.0
        dot = sum(a * b for a, b in zip(vec1, vec2, strict=True))
        norm1 = math.sqrt(sum(a * a for a in vec1)) or 1.0
        norm2 = math.sqrt(sum(b * b for b in vec2)) or 1.0
        return max(0.0, dot / (norm1 * norm2))


__all__ = ["SymbolicNode", "EchOSSymbolicEngine"]
