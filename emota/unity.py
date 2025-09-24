from emota.braid import DesireFearBraid
from emota.archetype import ArchetypalResonanceEngine
from emota.memory import MemorySystem
from emota.logging_utils import configure_logger
from typing import Any, Dict, Optional

class EMOTAUnityEngine:
    def __init__(self, identity_name: str = "Prime", config_path: Optional[str] = None,
                 memory_path: Optional[str] = None, log_level: str = "INFO", json_logging: bool = False) -> None:
        self.identity_name = identity_name
        self.braid_engine = DesireFearBraid(config_path=config_path)
        self.archetypal_engine = ArchetypalResonanceEngine()
        self.logger = configure_logger(level=log_level, json_mode=json_logging)
        self.memory_path = memory_path
        self.memory = MemorySystem.load(memory_path) if memory_path else MemorySystem()

    def snapshot(self, braid_state: Any, archetypal_state: Any, content: str, inputs: Dict[str, float]) -> Dict[str, Any]:  # pragma: no cover trivial
        return {
            "identity": self.identity_name,
            "content": content,
            "inputs": inputs,
            "motivational_state": {
                "desire": braid_state.desire,
                "fear": braid_state.fear,
                "valence": braid_state.valence,
                "tension": braid_state.tension,
                "policy": braid_state.policy,
                "braid_code": self.braid_engine.braid_code()
            },
            "archetypal_resonance": {
                "dominant_pattern": archetypal_state.dominant_pattern.value if archetypal_state.dominant_pattern else None,
                "serpent_activation": archetypal_state.serpent_activation,
                "flame_activation": archetypal_state.flame_activation,
                "void_activation": archetypal_state.void_activation,
                "unity_activation": archetypal_state.unity_activation,
                "resonance_mode": archetypal_state.resonance_mode,
                "harmonic_frequency": archetypal_state.harmonic_frequency
            }
        }

    def process_experience(self, content: str, environmental_inputs: Optional[Dict[str, float]] = None) -> Dict[str, Any]:
        environmental_inputs = environmental_inputs or {}
        braid_state = self.braid_engine.step(environmental_inputs)
        archetypal_state = self.archetypal_engine.process_braid_resonance(braid_state)
        snap = self.snapshot(braid_state, archetypal_state, content, environmental_inputs)
        self.memory.record(snap)
        if self.memory_path:
            try:
                self.memory.save(self.memory_path)
            except Exception as e:  # pragma: no cover
                self.logger.error({"event": "memory_save_failed", "error": str(e)})
        self.logger.info({"event": "experience_processed", "policy": snap["motivational_state"]["policy"], "braid_code": snap["motivational_state"]["braid_code"]})
        return snap
