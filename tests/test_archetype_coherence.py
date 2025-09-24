from emota.archetype import ArchetypalResonanceEngine
from emota.braid import DesireFearBraid


def test_archetype_phase_coherence_range():
    braid = DesireFearBraid()
    engine = ArchetypalResonanceEngine()
    # Run several steps with varying inputs
    inputs_sequence = [
        {"goal_value": 0.2, "threat_level": 0.1},
        {"goal_value": 0.7, "threat_level": 0.3, "novelty": 0.4},
        {"goal_value": 0.6, "threat_level": 0.6, "uncertainty": 0.5},
        {"goal_value": 0.9, "threat_level": 0.2, "novelty": 0.3, "uncertainty": 0.2},
    ]
    coherence_values = []
    for inp in inputs_sequence:
        state = braid.step(inp)
        arch = engine.process_braid_resonance(state)
        coherence_values.append(arch.phase_coherence)
    for c in coherence_values:
        assert 0.0 <= c <= 1.0
