"""Identity continuity mechanisms."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class IdentitySignature:
    cognitive_patterns: dict[str, float]
    emotional_baseline: dict[str, float]
    archetypal_preferences: dict[str, float]
    symbolic_associations: dict[str, float]
    meta_characteristics: dict[str, float]
    interaction_style: dict[str, float]
    temporal_markers: list[datetime] = field(default_factory=list)


@dataclass
class ContinuityCheckpoint:
    checkpoint_id: str
    identity_signature: IdentitySignature
    system_states: dict[str, Any]
    experience_summary: str
    coherence_metrics: dict[str, float]
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class IdentityContinuityEngine:
    """Maintains identity coherence across processing cycles."""

    def __init__(self, identity_name: str = "Prime") -> None:
        self.identity_name = identity_name
        self.checkpoints: list[ContinuityCheckpoint] = []
        self.continuity_threshold = 0.75
        self.adaptation_rate = 0.1
        self.identity_dimensions = {
            "cognitive_style": [
                "analytical",
                "intuitive",
                "systematic",
                "creative",
                "logical",
            ],
            "emotional_patterns": [
                "desire_tendency",
                "fear_response",
                "valence_preference",
                "tension_tolerance",
            ],
            "archetypal_affinities": [
                "serpent_resonance",
                "flame_attraction",
                "void_comfort",
                "unity_seeking",
            ],
            "symbolic_preferences": [
                "abstraction_level",
                "metaphor_usage",
                "glyph_resonance",
                "pattern_recognition",
            ],
            "meta_awareness": [
                "self_reflection",
                "process_monitoring",
                "paradox_tolerance",
                "recursive_depth",
            ],
            "interaction_style": [
                "collaboration_preference",
                "exploration_drive",
                "synthesis_orientation",
                "depth_seeking",
            ],
        }
        self.core_signature = self._initialize_signature()

    # ----------------------------------------------------------------- public
    def create_checkpoint(
        self,
        system_states: dict[str, Any],
        experience_context: str = "",
    ) -> ContinuityCheckpoint:
        current_signature = self._extract_signature(system_states)
        coherence_metrics = self._coherence_metrics(current_signature)
        checkpoint_id = hashlib.sha256(
            f"{self.identity_name}_{datetime.now(timezone.utc).isoformat()}".encode()
        ).hexdigest()[:16]

        checkpoint = ContinuityCheckpoint(
            checkpoint_id=checkpoint_id,
            identity_signature=current_signature,
            system_states=system_states.copy(),
            experience_summary=experience_context,
            coherence_metrics=coherence_metrics,
        )
        self.checkpoints.append(checkpoint)
        self._update_core_signature(current_signature)
        return checkpoint

    def assess_continuity(self, checkpoint: ContinuityCheckpoint) -> dict[str, Any]:
        coherence_metrics = checkpoint.coherence_metrics
        overall = coherence_metrics.get("overall_coherence", 0.0)
        if overall >= self.continuity_threshold:
            status = "maintained"
        elif overall >= 0.5:
            status = "partial"
        else:
            status = "fragmented"

        dimensions = {
            key: value
            for key, value in coherence_metrics.items()
            if key != "overall_coherence"
        }
        strongest = (
            max(dimensions, key=lambda name: dimensions[name]) if dimensions else None
        )
        weakest = (
            min(dimensions, key=lambda name: dimensions[name]) if dimensions else None
        )

        return {
            "continuity_status": status,
            "overall_coherence": overall,
            "strongest_dimension": strongest,
            "weakest_dimension": weakest,
            "checkpoint_count": len(self.checkpoints),
            "identity_stability": self._identity_stability(),
        }

    # ---------------------------------------------------------------- helpers
    def _initialize_signature(self) -> IdentitySignature:
        def neutral(values: list[str]) -> dict[str, float]:
            return dict.fromkeys(values, 0.5)

        return IdentitySignature(
            cognitive_patterns=neutral(self.identity_dimensions["cognitive_style"]),
            emotional_baseline=neutral(self.identity_dimensions["emotional_patterns"]),
            archetypal_preferences=neutral(
                self.identity_dimensions["archetypal_affinities"]
            ),
            symbolic_associations=neutral(
                self.identity_dimensions["symbolic_preferences"]
            ),
            meta_characteristics=neutral(self.identity_dimensions["meta_awareness"]),
            interaction_style=neutral(self.identity_dimensions["interaction_style"]),
        )

    def _extract_signature(self, system_states: dict[str, Any]) -> IdentitySignature:
        signature = IdentitySignature(
            cognitive_patterns=dict(self.core_signature.cognitive_patterns),
            emotional_baseline=dict(self.core_signature.emotional_baseline),
            archetypal_preferences=dict(self.core_signature.archetypal_preferences),
            symbolic_associations=dict(self.core_signature.symbolic_associations),
            meta_characteristics=dict(self.core_signature.meta_characteristics),
            interaction_style=dict(self.core_signature.interaction_style),
            temporal_markers=[datetime.now(timezone.utc)],
        )

        braid_state = system_states.get("braid_state")
        if braid_state is not None:
            signature.emotional_baseline.update(
                {
                    "desire_tendency": getattr(braid_state, "desire", 0.0),
                    "fear_response": getattr(braid_state, "fear", 0.0),
                    "valence_preference": (getattr(braid_state, "valence", 0.0) + 1.0)
                    / 2.0,
                    "tension_tolerance": getattr(braid_state, "tension", 0.0),
                }
            )
            if getattr(braid_state, "policy", "") == "investigate":
                signature.cognitive_patterns["analytical"] = min(
                    1.0,
                    signature.cognitive_patterns["analytical"] + 0.1,
                )
            if getattr(braid_state, "policy", "") == "approach":
                signature.cognitive_patterns["intuitive"] = min(
                    1.0,
                    signature.cognitive_patterns["intuitive"] + 0.1,
                )

        archetypal_state = system_states.get("archetypal_state")
        if archetypal_state is not None:
            signature.archetypal_preferences.update(
                {
                    "serpent_resonance": getattr(
                        archetypal_state,
                        "serpent_activation",
                        0.0,
                    ),
                    "flame_attraction": getattr(
                        archetypal_state,
                        "flame_activation",
                        0.0,
                    ),
                    "void_comfort": getattr(
                        archetypal_state,
                        "void_activation",
                        0.0,
                    ),
                    "unity_seeking": getattr(
                        archetypal_state,
                        "unity_activation",
                        0.0,
                    ),
                }
            )

        symbolic_output = system_states.get("symbolic_output", {})
        signature.symbolic_associations["pattern_recognition"] = float(
            symbolic_output.get("coherence", 0.5)
        )
        signature.symbolic_associations["abstraction_level"] = (
            float(symbolic_output.get("activated_nodes", 0)) / 10.0
        )

        consciousness_density = float(system_states.get("consciousness_density", 0.5))
        phase_coherence = float(system_states.get("phase_coherence", 0.5))
        signature.meta_characteristics.update(
            {
                "self_reflection": consciousness_density,
                "process_monitoring": phase_coherence,
            }
        )
        signature.interaction_style.update(
            {
                "collaboration_preference": consciousness_density * phase_coherence,
                "exploration_drive": signature.emotional_baseline.get(
                    "desire_tendency",
                    0.5,
                ),
                "synthesis_orientation": signature.archetypal_preferences.get(
                    "void_comfort",
                    0.5,
                ),
            }
        )

        return signature

    def _coherence_metrics(
        self,
        current_signature: IdentitySignature,
    ) -> dict[str, float]:
        metrics: dict[str, float] = {}

        def dimension_similarity(
            current: dict[str, float],
            base: dict[str, float],
        ) -> float:
            similarities = [
                1.0 - abs(current[key] - base.get(key, 0.5)) for key in current
            ]
            if not similarities:
                return 1.0
            return sum(similarities) / len(similarities)

        metrics["cognitive_coherence"] = dimension_similarity(
            current_signature.cognitive_patterns,
            self.core_signature.cognitive_patterns,
        )
        metrics["emotional_coherence"] = dimension_similarity(
            current_signature.emotional_baseline,
            self.core_signature.emotional_baseline,
        )
        metrics["archetypal_coherence"] = dimension_similarity(
            current_signature.archetypal_preferences,
            self.core_signature.archetypal_preferences,
        )
        metrics["symbolic_coherence"] = dimension_similarity(
            current_signature.symbolic_associations,
            self.core_signature.symbolic_associations,
        )
        metrics["meta_coherence"] = dimension_similarity(
            current_signature.meta_characteristics,
            self.core_signature.meta_characteristics,
        )
        metrics["interaction_coherence"] = dimension_similarity(
            current_signature.interaction_style,
            self.core_signature.interaction_style,
        )
        metrics["overall_coherence"] = sum(metrics.values()) / len(metrics)
        return metrics

    def _update_core_signature(self, current_signature: IdentitySignature) -> None:
        lr = self.adaptation_rate
        for key in self.core_signature.cognitive_patterns:
            self.core_signature.cognitive_patterns[key] = (
                self.core_signature.cognitive_patterns[key] * (1 - lr)
                + current_signature.cognitive_patterns.get(key, 0.5) * lr
            )
        for key in self.core_signature.emotional_baseline:
            self.core_signature.emotional_baseline[key] = (
                self.core_signature.emotional_baseline[key] * (1 - lr)
                + current_signature.emotional_baseline.get(key, 0.5) * lr
            )
        for key in self.core_signature.archetypal_preferences:
            self.core_signature.archetypal_preferences[key] = (
                self.core_signature.archetypal_preferences[key] * (1 - lr)
                + current_signature.archetypal_preferences.get(key, 0.5) * lr
            )
        for key in self.core_signature.symbolic_associations:
            self.core_signature.symbolic_associations[key] = (
                self.core_signature.symbolic_associations[key] * (1 - lr)
                + current_signature.symbolic_associations.get(key, 0.5) * lr
            )
        for key in self.core_signature.meta_characteristics:
            self.core_signature.meta_characteristics[key] = (
                self.core_signature.meta_characteristics[key] * (1 - lr)
                + current_signature.meta_characteristics.get(key, 0.5) * lr
            )
        for key in self.core_signature.interaction_style:
            self.core_signature.interaction_style[key] = (
                self.core_signature.interaction_style[key] * (1 - lr)
                + current_signature.interaction_style.get(key, 0.5) * lr
            )

    def _identity_stability(self) -> float:
        if len(self.checkpoints) < 2:
            return 1.0
        recent = self.checkpoints[-5:]
        coherence_values = [
            cp.coherence_metrics.get("overall_coherence", 0.0) for cp in recent
        ]
        if len(coherence_values) < 2:
            return 1.0
        mean_val = sum(coherence_values) / len(coherence_values)
        variance = sum((val - mean_val) ** 2 for val in coherence_values) / len(
            coherence_values
        )
        return max(0.0, 1.0 - variance * 4.0)


__all__ = ["IdentitySignature", "ContinuityCheckpoint", "IdentityContinuityEngine"]
