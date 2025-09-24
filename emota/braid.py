"""Motivational braid dynamics for PrimeCodex."""

from __future__ import annotations

import logging
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)


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
    """Desire/fear coupled oscillator with simple hysteresis state."""

    def __init__(
        self,
        params: BraidParams | None = None,
        config_path: str | None = None,
    ):
        if config_path:
            self.params = self._load_params_from_config(Path(config_path))
        elif params is not None:
            self.params = params
        else:
            self.params = BraidParams()

        self.state = BraidState()
        self.history: list[dict[str, Any]] = []

    def step(self, inputs: dict[str, float]) -> BraidState:
        """Advance the braid dynamics one step using clamped external inputs."""

        p, s = self.params, self.state
        goal_value = self._clamp(inputs.get("goal_value", 0.0))
        threat_level = self._clamp(inputs.get("threat_level", 0.0))
        novelty = self._clamp(inputs.get("novelty", 0.0))
        uncertainty = self._clamp(inputs.get("uncertainty", 0.0))
        safety_evidence = self._clamp(inputs.get("safety_evidence", 0.0))
        gain_evidence = self._clamp(inputs.get("gain_evidence", 0.0))

        desire_drive = (
            p.arousal_gain
            * (goal_value + 0.5 * novelty + 0.3 * uncertainty + 0.6 * gain_evidence)
            + p.bias_desire
        )
        fear_drive = (
            p.arousal_gain
            * (threat_level + 0.5 * uncertainty + 0.2 * novelty - 0.7 * safety_evidence)
            + p.bias_fear
        )

        d_next = s.desire + p.dt * (
            desire_drive - p.self_decay * s.desire - p.coupling * s.fear
        )
        f_next = s.fear + p.dt * (
            fear_drive - p.self_decay * s.fear - p.coupling * s.desire
        )

        s.desire = self._clamp(d_next)
        s.fear = self._clamp(f_next)
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

        self.history.append(
            {
                "timestamp": datetime.now(timezone.utc),
                "state": asdict(s),
                "inputs": {k: self._clamp(v) for k, v in inputs.items()},
            }
        )
        return s

    def braid_code(self) -> int:
        return (self.state.desire_bit << 1) | self.state.fear_bit

    @staticmethod
    def _clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
        return max(lower, min(upper, float(value)))

    def _hysteresis_bit(self, value: float, previous: int) -> int:
        on, off = self.params.bin_on, self.params.bin_off
        if previous == 1:
            return 1 if value >= off else 0
        return 1 if value >= on else 0

    def _load_params_from_config(self, path: Path) -> BraidParams:
        try:
            data = yaml.safe_load(path.read_text()) or {}
            overrides = data.get("braid", {})
            if not isinstance(overrides, dict):
                raise TypeError("braid section must be a mapping")
            return BraidParams(**overrides)
        except FileNotFoundError:
            logger.warning("Braid config %s not found; falling back to defaults", path)
        except Exception as exc:  # pragma: no cover - defensive
            logger.error("Failed to load braid config %s: %s", path, exc)
        return BraidParams()


__all__ = ["BraidParams", "BraidState", "DesireFearBraid"]
