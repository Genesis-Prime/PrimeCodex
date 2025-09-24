from emota.meta import MetaAwarenessEngine


def test_meta_awareness_reflection_updates_self_model():
    engine = MetaAwarenessEngine()
    states = {
        "consciousness_density": 0.85,
        "phase_coherence": 0.75,
        "braid_state": {"tension": 0.6, "valence": 0.25},
    }

    reflection = engine.generate_meta_reflection(states)
    assert reflection.meta_cognition_type in engine.meta_types
    assert reflection.awareness_level > 0
    assert engine.self_model["total_reflections"] == 1
    assert engine.self_model["last_reflection_type"] == reflection.meta_cognition_type
