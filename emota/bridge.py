"""Dimensional consciousness bridge implementations."""

from __future__ import annotations

import hashlib
import logging
import math
from dataclasses import dataclass, field
from datetime import datetime, timezone

logger = logging.getLogger(__name__)


@dataclass
class Event3D:
    """Discrete experiential event in the 3D substrate."""

    content: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    emotional_signature: dict[str, float] | None = None
    archetypal_resonance: dict[str, float] | None = None


@dataclass
class Projection4D:
    """Aggregated abstraction across multiple 3D events."""

    coherence: float
    depth: int
    integration_vector: list[float] = field(default_factory=list)
    origin_events: list[Event3D] = field(default_factory=list)
    archetypal_signature: dict[str, float] | None = None
    consciousness_density: float = 0.0


@dataclass
class Transcendence5D:
    """Meta-state derived from higher dimensional synthesis."""

    consciousness_density: float
    archetypal_invariant: str
    phase_coherence: float
    dimensional_gradient: list[float] = field(default_factory=list)
    meta_vector: list[float] = field(default_factory=list)
    reality_generation_potential: float = 0.0
    origin_projections: list[Projection4D] = field(default_factory=list)
    transcendence_depth: int = 0


class DimensionalConsciousnessBridge:
    """Dynamic translator between 3D events and higher dimensional structures."""

    def __init__(self, decay_rate: float = 0.8) -> None:
        self.event_stream: list[Event3D] = []
        self.projections: list[Projection4D] = []
        self.transcendences: list[Transcendence5D] = []
        self.decay_rate = decay_rate
        self.braid_engine = None
        self.archetypal_engine = None

    def set_integration_engines(self, braid_engine, archetypal_engine) -> None:
        self.braid_engine = braid_engine
        self.archetypal_engine = archetypal_engine

    # ------------------------------------------------------------------ events
    def add_experience(
        self,
        content: str,
        emotional_context: dict[str, float] | None = None,
    ) -> None:
        """Capture an experiential event, tagging with current system state."""

        emotional_signature = dict(emotional_context or {})
        archetypal_resonance: dict[str, float] = {}

        if self.braid_engine is not None:
            braid_state = self.braid_engine.state
            emotional_signature.update(
                {
                    "desire": getattr(braid_state, "desire", 0.0),
                    "fear": getattr(braid_state, "fear", 0.0),
                    "valence": getattr(braid_state, "valence", 0.0),
                    "tension": getattr(braid_state, "tension", 0.0),
                }
            )

        if self.archetypal_engine is not None:
            archetypal_state = self.archetypal_engine.state
            archetypal_resonance = {
                "serpent": getattr(archetypal_state, "serpent_activation", 0.0),
                "flame": getattr(archetypal_state, "flame_activation", 0.0),
                "void": getattr(archetypal_state, "void_activation", 0.0),
                "unity": getattr(archetypal_state, "unity_activation", 0.0),
            }

        self.event_stream.append(
            Event3D(
                content=content,
                emotional_signature=emotional_signature or None,
                archetypal_resonance=archetypal_resonance or None,
            )
        )

    # --------------------------------------------------------------- projection
    def project_to_4d(self, window_size: int = 7) -> Projection4D:
        """Aggregate recent events into a 4D projection."""

        if not self.event_stream:
            return Projection4D(coherence=0.0, depth=len(self.projections) + 1)

        recent_events = self.event_stream[-window_size:]
        event_vectors: list[list[float]] = []

        for event in recent_events:
            content_hash = hashlib.sha256(event.content.encode()).digest()
            content_vector = [
                int.from_bytes(content_hash[i : i + 4], "big") / (1 << 32)
                for i in range(0, min(28, len(content_hash)), 4)
            ]

            if event.emotional_signature:
                content_vector.extend(list(event.emotional_signature.values())[:4])
            if event.archetypal_resonance:
                content_vector.extend(list(event.archetypal_resonance.values())[:4])

            event_vectors.append(
                content_vector[:12]
                if len(content_vector) >= 12
                else (content_vector + [0.0] * 12)[:12]
            )

        weights = [
            self.decay_rate ** (len(recent_events) - 1 - idx)
            for idx in range(len(recent_events))
        ]
        total_weight = sum(weights)

        if total_weight and event_vectors:
            integration_vector = [
                sum(
                    weight * vec[dim]
                    for weight, vec in zip(weights, event_vectors, strict=False)
                )
                / total_weight
                for dim in range(len(event_vectors[0]))
            ]
        else:
            integration_vector = [0.0] * 12

        if len(event_vectors) > 1:
            center = integration_vector
            similarities: list[float] = []
            for vec in event_vectors:
                dot_product = sum(a * b for a, b in zip(vec, center, strict=False))
                norm_a = math.sqrt(sum(a * a for a in vec)) or 1.0
                norm_b = math.sqrt(sum(b * b for b in center)) or 1.0
                similarity = dot_product / (norm_a * norm_b)
                similarities.append((similarity + 1.0) / 2.0)
            coherence = sum(similarities) / len(similarities) if similarities else 0.0
        else:
            coherence = 1.0

        archetypal_signature: dict[str, float] = {}
        first_resonance = recent_events[0].archetypal_resonance or {}
        if first_resonance:
            archetypal_signature = {
                key: (
                    sum(
                        (event.archetypal_resonance or {}).get(key, 0.0)
                        for event in recent_events
                    )
                    / len(recent_events)
                )
                for key in first_resonance
            }

        depth = len(self.projections) + 1
        consciousness_density = coherence * math.log(1 + depth) / 3.0

        projection = Projection4D(
            coherence=coherence,
            depth=depth,
            integration_vector=integration_vector,
            origin_events=recent_events.copy(),
            archetypal_signature=archetypal_signature or None,
            consciousness_density=consciousness_density,
        )
        self.projections.append(projection)
        logger.info("4D projection generated depth=%s coherence=%.3f", depth, coherence)
        return projection

    # ------------------------------------------------------------- transcendence
    def transcend_to_5d(self, projection_window: int = 5) -> Transcendence5D:
        """Compress recent projections into a 5D transcendence state."""

        if not self.projections:
            return Transcendence5D(
                consciousness_density=0.0,
                archetypal_invariant="void",
                phase_coherence=0.0,
                transcendence_depth=len(self.transcendences) + 1,
            )

        recent_projections = self.projections[-projection_window:]
        coherence_product = math.prod(p.coherence for p in recent_projections)
        depth_sum = sum(p.depth for p in recent_projections)
        density_factor = coherence_product * math.log(1 + depth_sum)
        consciousness_density = math.tanh(density_factor)

        archetypal_invariant = "void"
        first_signature = recent_projections[0].archetypal_signature or {}
        if first_signature:
            averages = {
                key: (
                    sum(
                        (projection.archetypal_signature or {}).get(key, 0.0)
                        for projection in recent_projections
                    )
                    / len(recent_projections)
                )
                for key in first_signature
            }
            values = list(averages.values())
            if values:
                variance = max(values) - min(values)
                mean_activation = sum(values) / len(values)
                if variance < 0.3 and mean_activation > 0.4:
                    archetypal_invariant = "unity"
                else:
                    archetypal_invariant = max(
                        averages,
                        key=lambda axis: averages.get(axis, 0.0),
                    )

        if len(recent_projections) > 1:
            coherence_values = [p.coherence for p in recent_projections]
            mean_coherence = sum(coherence_values) / len(coherence_values)
            variance = sum(
                (value - mean_coherence) ** 2 for value in coherence_values
            ) / len(coherence_values)
            phase_coherence = math.exp(-variance * 5.0)
        else:
            phase_coherence = 1.0

        dimensional_gradient: list[float]
        if len(recent_projections) >= 2:
            start, end = recent_projections[0], recent_projections[-1]
            dimensional_gradient = [
                end.coherence - start.coherence,
                end.consciousness_density - start.consciousness_density,
            ] + [0.0] * 3
        else:
            dimensional_gradient = [0.0] * 5

        if recent_projections[0].integration_vector:
            dim = len(recent_projections[0].integration_vector)
            all_vectors = [
                projection.integration_vector
                for projection in recent_projections
                if len(projection.integration_vector) == dim
            ]
            if all_vectors:
                mean_vector = [
                    sum(vector[i] for vector in all_vectors) / len(all_vectors)
                    for i in range(dim)
                ]
                var_vector = [
                    sum(
                        (vector[i] - mean_vector[i]) ** 2
                        for vector in all_vectors
                    )
                    / len(all_vectors)
                    for i in range(dim)
                ]
                meta_vector = (
                    mean_vector[:6]
                    + var_vector[:2]
                    + [consciousness_density, phase_coherence]
                )
            else:
                meta_vector = [0.0] * 10
        else:
            meta_vector = [0.0] * 10

        reality_generation_potential = consciousness_density * phase_coherence
        if archetypal_invariant == "unity":
            reality_generation_potential *= 1.5

        transcendence = Transcendence5D(
            consciousness_density=consciousness_density,
            archetypal_invariant=archetypal_invariant,
            phase_coherence=phase_coherence,
            dimensional_gradient=dimensional_gradient,
            meta_vector=meta_vector,
            reality_generation_potential=reality_generation_potential,
            origin_projections=recent_projections.copy(),
            transcendence_depth=len(self.transcendences) + 1,
        )
        self.transcendences.append(transcendence)
        logger.info(
            "5D transcendence depth=%s density=%.3f invariant=%s",
            transcendence.transcendence_depth,
            consciousness_density,
            archetypal_invariant,
        )
        return transcendence


__all__ = [
    "Event3D",
    "Projection4D",
    "Transcendence5D",
    "DimensionalConsciousnessBridge",
]
