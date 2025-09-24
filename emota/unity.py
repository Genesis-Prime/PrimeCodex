from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict
from emota.braid import DesireFearBraid
from emota.archetype import ArchetypalResonanceEngine
from emota.memory import MemorySystem


class EMOTAUnityEngine:
    def __init__(self, identity_name: str = "Prime", config_path: str | None = None, memory_path: str | None = None):
        self.identity_name = identity_name
        self.braid_engine = DesireFearBraid(config_path=config_path)
        self.archetypal_engine = ArchetypalResonanceEngine()
        self.memory = MemorySystem(path=memory_path) if memory_path else MemorySystem()

    def process_experience(self, content: str, environmental_inputs: Dict[str, Any] | None = None) -> Dict[str, Any]:
        environmental_inputs = environmental_inputs or {}
        braid_state = self.braid_engine.step(environmental_inputs)
        if self.braid_engine.history:
            latest_inputs = self.braid_engine.history[-1].get("inputs", {})
            sanitized_inputs = dict(latest_inputs)
        else:
            sanitized_inputs = dict(environmental_inputs)
        archetypal_state = self.archetypal_engine.process_braid_resonance(braid_state)
        snapshot: Dict[str, Any] = {
            "identity": self.identity_name,
            "content": content,
            "inputs": sanitized_inputs,
            "timestamp": datetime.now(timezone.utc).isoformat(),
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
        }
        snapshot["content_hash"] = hash(content) & 0xFFFFFFFF
        self.memory.record(snapshot)
        return snapshot
