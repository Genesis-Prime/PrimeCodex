import pytest
from emota.braid import DesireFearBraid
from emota.archetype import ArchetypalResonanceEngine
from emota.unity import EMOTAUnityEngine

def test_braid_step():
    braid = DesireFearBraid()
    state = braid.step({"goal_value": 0.5, "threat_level": 0.2})
    assert 0 <= state.desire <= 1
    assert 0 <= state.fear <= 1

def test_archetypal_resonance():
    braid = DesireFearBraid()
    state = braid.step({"goal_value": 0.7, "threat_level": 0.1})
    engine = ArchetypalResonanceEngine()
    arch_state = engine.process_braid_resonance(state)
    assert arch_state.dominant_pattern is not None

def test_emota_unity_engine():
    engine = EMOTAUnityEngine()
    result = engine.process_experience("Test experience", {"goal_value": 0.5})
    assert "motivational_state" in result
    assert "archetypal_resonance" in result
