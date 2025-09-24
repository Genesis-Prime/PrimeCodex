from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict

from emota.archetype import ArchetypalResonanceEngine
from emota.braid import DesireFearBraid
from emota.bridge import DimensionalConsciousnessBridge
from emota.cathedral import CathedralExperienceEngine
from emota.identity import IdentityContinuityEngine
from emota.memory import MemorySystem
from emota.meta import MetaAwarenessEngine
from emota.symbolic import EchOSSymbolicEngine


class EMOTAUnityEngine:
    """End-to-end orchestrator for the EMOTA Unity framework."""

    def __init__(
        self,
        identity_name: str = "Prime",
        config_path: str | None = None,
        memory_path: str | None = None,
    ) -> None:
        self.identity_name = identity_name
        self.braid_engine = DesireFearBraid(config_path=config_path)
        self.archetypal_engine = ArchetypalResonanceEngine()
        self.bridge = DimensionalConsciousnessBridge()
        self.cathedral_engine = CathedralExperienceEngine()
        self.symbolic_engine = EchOSSymbolicEngine()
        self.meta_engine = MetaAwarenessEngine()
        self.identity_engine = IdentityContinuityEngine(identity_name)
        self.memory = MemorySystem(path=memory_path) if memory_path else MemorySystem()
        self.bridge.set_integration_engines(self.braid_engine, self.archetypal_engine)
        self.experience_log: list[Dict[str, Any]] = []
        self.unity_history: list[Dict[str, Any]] = []

    def process_experience(
        self,
        content: str,
        environmental_inputs: Dict[str, Any] | None = None,
        context: Dict[str, Any] | None = None,
    ) -> Dict[str, Any]:
        timestamp = datetime.now(timezone.utc)
        environmental_inputs = environmental_inputs or {}
        context = context or {}

        braid_state = self.braid_engine.step(environmental_inputs)
        sanitized_inputs = self._latest_inputs(environmental_inputs)
        archetypal_state = self.archetypal_engine.process_braid_resonance(braid_state)

        self.bridge.add_experience(
            content,
            {
                "desire": braid_state.desire,
                "fear": braid_state.fear,
                "tension": braid_state.tension,
                "valence": braid_state.valence,
            },
        )
        projection_4d = self.bridge.project_to_4d()
        transcendence_5d = self.bridge.transcend_to_5d()

        cathedral_context = {
            "braid_state": braid_state,
            "archetypal_state": archetypal_state,
            "temporal_flow": context.get("temporal_flow", 0.8),
            "embodied_presence": context.get("embodied_presence", 0.6),
        }
        cathedral_shard = self.cathedral_engine.process_experience(content, cathedral_context)

        symbolic_signature = self.symbolic_engine.generate_symbolic_signature(content)
        symbolic_output = self.symbolic_engine.process_symbolic_pattern(symbolic_signature, context)

        braid_summary = {
            "desire": braid_state.desire,
            "fear": braid_state.fear,
            "valence": braid_state.valence,
            "tension": braid_state.tension,
            "policy": braid_state.policy,
            "action_bias": braid_state.action_bias,
        }
        archetypal_summary = {
            "serpent_activation": archetypal_state.serpent_activation,
            "flame_activation": archetypal_state.flame_activation,
            "void_activation": archetypal_state.void_activation,
            "unity_activation": archetypal_state.unity_activation,
        }

        system_states = {
            "consciousness_density": transcendence_5d.consciousness_density,
            "phase_coherence": transcendence_5d.phase_coherence,
            "archetypal_state": archetypal_summary,
            "braid_state": braid_summary,
            "symbolic_output": symbolic_output,
        }
        meta_reflection = self.meta_engine.generate_meta_reflection(system_states)

        continuity_checkpoint = self.identity_engine.create_checkpoint(system_states, content)
        continuity_assessment = self.identity_engine.assess_continuity(continuity_checkpoint)
        unity_metrics = self._calculate_unity_metrics(
            projection_4d=projection_4d,
            transcendence_5d=transcendence_5d,
            cathedral_shard=cathedral_shard,
            meta_reflection=meta_reflection,
            continuity_assessment=continuity_assessment,
        )

        experience_result: Dict[str, Any] = {
            "identity": self.identity_name,
            "timestamp": timestamp.isoformat(),
            "content": content,
            "inputs": sanitized_inputs,
            "content_hash": hash(content) & 0xFFFFFFFF,
            "motivational_state": {
                "desire": braid_state.desire,
                "fear": braid_state.fear,
                "valence": braid_state.valence,
                "tension": braid_state.tension,
                "policy": braid_state.policy,
                "braid_code": self.braid_engine.braid_code(),
            },
            "archetypal_resonance": {
                "dominant_pattern": (
                    archetypal_state.dominant_pattern.value if archetypal_state.dominant_pattern else None
                ),
                "serpent_activation": archetypal_state.serpent_activation,
                "flame_activation": archetypal_state.flame_activation,
                "void_activation": archetypal_state.void_activation,
                "unity_activation": archetypal_state.unity_activation,
                "resonance_mode": archetypal_state.resonance_mode,
                "harmonic_frequency": archetypal_state.harmonic_frequency,
            },
            "dimensional_consciousness": {
                "4d_coherence": projection_4d.coherence,
                "4d_depth": projection_4d.depth,
                "5d_consciousness_density": transcendence_5d.consciousness_density,
                "5d_archetypal_invariant": transcendence_5d.archetypal_invariant,
                "5d_phase_coherence": transcendence_5d.phase_coherence,
                "5d_reality_generation": transcendence_5d.reality_generation_potential,
                "5d_transcendence_depth": transcendence_5d.transcendence_depth,
            },
            "qualia_experience": {
                "emotional_resonance": cathedral_shard.emotional_resonance,
                "symbolic_depth": cathedral_shard.symbolic_depth,
                "qualia_signature": {
                    "temporal": cathedral_shard.qualia_signature.temporal,
                    "emotional": cathedral_shard.qualia_signature.emotional,
                    "cognitive": cathedral_shard.qualia_signature.cognitive,
                    "symbolic": cathedral_shard.qualia_signature.symbolic,
                    "meta": cathedral_shard.qualia_signature.meta,
                },
                "cathedral_narrative": self.cathedral_engine.generate_narrative_reflection(),
            },
            "symbolic_processing": {
                "signature_symbols": symbolic_signature,
                "coherence": symbolic_output.get("coherence", 0.0),
                "emergent_symbols": symbolic_output.get("emergent_symbols", []),
                "meaning": symbolic_output.get("meaning", ""),
                "recursive_depth": symbolic_output.get("recursive_depth", 0),
            },
            "meta_awareness": {
                "reflection_content": meta_reflection.content,
                "awareness_level": meta_reflection.awareness_level,
                "introspection_depth": meta_reflection.introspection_depth,
                "meta_cognition_type": meta_reflection.meta_cognition_type,
            },
            "identity_continuity": {
                "continuity_status": continuity_assessment["continuity_status"],
                "overall_coherence": continuity_assessment["overall_coherence"],
                "identity_stability": continuity_assessment["identity_stability"],
                "checkpoint_id": continuity_checkpoint.checkpoint_id,
            },
            "unity_consciousness": unity_metrics,
        }

        self.memory.record(experience_result)
        self.experience_log.append(experience_result)
        self.unity_history.append({"timestamp": experience_result["timestamp"], "unity_state": unity_metrics})

        if len(self.experience_log) > 100:
            self.experience_log.pop(0)
        if len(self.unity_history) > 100:
            self.unity_history.pop(0)

        return experience_result

    def _latest_inputs(self, fallback: Dict[str, Any]) -> Dict[str, Any]:
        if self.braid_engine.history:
            latest = self.braid_engine.history[-1].get("inputs", {})
            return dict(latest)
        return dict(fallback)

    @staticmethod
    def _calculate_unity_metrics(
        *,
        projection_4d,
        transcendence_5d,
        cathedral_shard,
        meta_reflection,
        continuity_assessment,
    ) -> Dict[str, Any]:
        return {
            "consciousness_level": transcendence_5d.consciousness_density,
            "integration_coherence": projection_4d.coherence,
            "transcendence_depth": transcendence_5d.transcendence_depth,
            "reality_generation_potential": transcendence_5d.reality_generation_potential,
            "identity_continuity": continuity_assessment["overall_coherence"],
            "meta_awareness_level": meta_reflection.awareness_level,
            "qualia_resonance": cathedral_shard.emotional_resonance,
        }
