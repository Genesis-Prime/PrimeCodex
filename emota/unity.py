from emota.braid import DesireFearBraid
from emota.archetype import ArchetypalResonanceEngine

class EMOTAUnityEngine:
    def __init__(self, identity_name: str = "Prime", config_path: str | None = None):
        self.braid_engine = DesireFearBraid(config_path=config_path)
        self.archetypal_engine = ArchetypalResonanceEngine()
        # ...other subsystem initializations...
        # For brevity, only core integration shown
    def process_experience(self, content: str, environmental_inputs=None):
        environmental_inputs = environmental_inputs or {}
        braid_state = self.braid_engine.step(environmental_inputs)
        archetypal_state = self.archetypal_engine.process_braid_resonance(braid_state)
        return {
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
