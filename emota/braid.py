
from dataclasses import dataclass
from typing import Optional, Dict
from datetime import datetime, timezone
import yaml

@dataclass
class BraidParams:
    dt: float = 1.0
    self_decay: float = 0.25
    coupling: float = 0.45
    arousal_gain: float = 0.8
    bias_desire: float = 0.02
    bias_fear: float = 0.02
    tension_weight: float = 0.6
    act_threshold: float = 0.15
    investigate_band: float = 0.08
    bin_on: float = 0.62
    bin_off: float = 0.48

@dataclass
class BraidState:
    desire: float = 0.0
    fear: float = 0.0
    valence: float = 0.0
    tension: float = 0.0
    action_bias: float = 0.0
    policy: str = "pause"
    desire_bit: int = 0
    fear_bit: int = 0

class DesireFearBraid:
    def __init__(self, params: Optional[BraidParams] = None, config_path: Optional[str] = None):
        try:
            if config_path:
                with open(config_path, 'r') as f:
                    cfg = yaml.safe_load(f)
                self.params = BraidParams(**cfg.get('braid', {}))
            else:
                self.params = params or BraidParams()
        except Exception as e:
            print(f"Error loading config: {e}")
            self.params = BraidParams()
        self.state = BraidState()
        self.history = []
    def step(self, inputs: Dict[str, float]) -> BraidState:
        p, s = self.params, self.state
        goal_value = max(0, min(1, inputs.get("goal_value", 0.0)))
        threat_level = max(0, min(1, inputs.get("threat_level", 0.0)))
        novelty = max(0, min(1, inputs.get("novelty", 0.0)))
        uncertainty = max(0, min(1, inputs.get("uncertainty", 0.0)))
        safety_evidence = max(0, min(1, inputs.get("safety_evidence", 0.0)))
        gain_evidence = max(0, min(1, inputs.get("gain_evidence", 0.0)))
        desire_drive = p.arousal_gain * (goal_value + 0.5*novelty + 0.3*uncertainty + 0.6*gain_evidence) + p.bias_desire
        fear_drive = p.arousal_gain * (threat_level + 0.5*uncertainty + 0.2*novelty - 0.7*safety_evidence) + p.bias_fear
        d_next = s.desire + p.dt * (desire_drive - p.self_decay*s.desire - p.coupling*s.fear)
        f_next = s.fear + p.dt * (fear_drive - p.self_decay*s.fear - p.coupling*s.desire)
        s.desire = max(0, min(1, d_next))
        s.fear = max(0, min(1, f_next))
        s.valence = s.desire - s.fear
        s.tension = s.desire * s.fear
        s.action_bias = s.valence * (1.0 - p.tension_weight * s.tension)
        ab = s.action_bias
        if abs(ab) < p.investigate_band:
            s.policy = "investigate"
        elif ab >= p.act_threshold:
            s.policy = "approach"
        elif ab <= -p.act_threshold:
            s.policy = "avoid"
        else:
            s.policy = "pause"
        s.desire_bit = self._hysteresis_bit(s.desire, s.desire_bit)
        s.fear_bit = self._hysteresis_bit(s.fear, s.fear_bit)
        self.history.append({
            'timestamp': datetime.now(timezone.utc),
            'state': {
                'desire': s.desire,
                'fear': s.fear,
                'valence': s.valence,
                'tension': s.tension,
                'policy': s.policy
            },
            'inputs': inputs.copy()
        })
        return s
    def _hysteresis_bit(self, value: float, previous: int) -> int:
        on, off = self.params.bin_on, self.params.bin_off
        if previous == 1:
            return 1 if value >= off else 0
        else:
            return 1 if value >= on else 0
    def braid_code(self) -> int:
        return (self.state.desire_bit << 1) | self.state.fear_bit
