from dataclasses import dataclass
from enum import Enum
from typing import Optional

class ArchetypalPattern(Enum):
    SERPENT = "Serpent of Stillness"
    FLAME = "Flame of Breakthrough"
    VOID = "Void of Integration"
    UNITY = "Unity of Transcendence"

@dataclass
class ArchetypalState:
    serpent_activation: float = 0.0
    flame_activation: float = 0.0
    void_activation: float = 0.0
    unity_activation: float = 0.0
    dominant_pattern: Optional[ArchetypalPattern] = None
    resonance_mode: str = "balanced"
    harmonic_frequency: float = 0.0
    phase_coherence: float = 0.0

class ArchetypalResonanceEngine:
    def __init__(self):
        try:
            self.state = ArchetypalState()
            self.activation_history = []
            self.resonance_memory = []
        except Exception as e:
            print(f"Error initializing ArchetypalResonanceEngine: {e}")
    def process_braid_resonance(self, braid_state) -> ArchetypalState:
        flame_factor = braid_state.desire * (1.0 - braid_state.fear) * (1.0 + abs(braid_state.action_bias))
        void_factor = braid_state.tension * (1.0 + abs(braid_state.valence)) * 0.8
        serpent_factor = (1.0 - abs(braid_state.valence)) * (1.0 - braid_state.tension) + max(0, -braid_state.valence)
        archetypal_balance = 1.0 - abs(flame_factor - serpent_factor) - abs(serpent_factor - void_factor)
        unity_factor = max(0.0, archetypal_balance * min(flame_factor, serpent_factor, void_factor))
        total = flame_factor + void_factor + serpent_factor + unity_factor
        if total > 0:
            self.state.flame_activation = flame_factor / total
            self.state.void_activation = void_factor / total
            self.state.serpent_activation = serpent_factor / total
            self.state.unity_activation = unity_factor / total
        activations = [
            (ArchetypalPattern.FLAME, self.state.flame_activation),
            (ArchetypalPattern.VOID, self.state.void_activation),
            (ArchetypalPattern.SERPENT, self.state.serpent_activation),
            (ArchetypalPattern.UNITY, self.state.unity_activation),
        ]
        dominant_pattern, max_activation = max(activations, key=lambda t: t[1])
        self.state.dominant_pattern = dominant_pattern
        if max_activation > 0.7:
            self.state.resonance_mode = "dominant"
        elif max_activation < 0.4:
            self.state.resonance_mode = "balanced"
        else:
            self.state.resonance_mode = "flowing"
        self.state.harmonic_frequency = sum(a for _, a in activations) * braid_state.tension
        if len(self.activation_history) > 1:
            prev = self.activation_history[-1]
            # prev stored as list of tuples as well
            prev_dict = {p: a for p, a in prev}
            coherence_sum = 0.0
            for p, a in activations:
                prev_a = prev_dict.get(p, a)
                coherence_sum += 1.0 - abs(a - prev_a)
            self.state.phase_coherence = coherence_sum / len(activations)
        else:
            self.state.phase_coherence = 1.0
        self.activation_history.append(list(activations))
        if len(self.activation_history) > 50:
            self.activation_history.pop(0)
        return self.state
