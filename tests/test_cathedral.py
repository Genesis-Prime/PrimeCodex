from types import SimpleNamespace

from emota.cathedral import CathedralExperienceEngine


def test_cathedral_process_and_reflection():
    engine = CathedralExperienceEngine()
    braid_state = SimpleNamespace(
        desire=0.8,
        fear=0.2,
        valence=0.1,
        tension=0.4,
        action_bias=0.3,
    )
    archetypal_state = SimpleNamespace(
        serpent_activation=0.6,
        flame_activation=0.5,
        void_activation=0.4,
        unity_activation=0.7,
    )
    context = {
        "temporal_flow": 0.5,
        "braid_state": braid_state,
        "archetypal_state": archetypal_state,
    }

    shard = engine.process_experience("A luminous bridge emerges", context)
    assert 0 <= shard.emotional_resonance <= 1
    assert shard.symbolic_depth >= 0
    assert shard.qualia_signature.emotional > 0

    engine.process_experience("A second luminous bridge", context)
    reflection = engine.generate_narrative_reflection()
    assert isinstance(reflection, str) and reflection
    assert engine.synergy_matrix
