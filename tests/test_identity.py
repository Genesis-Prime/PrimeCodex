from types import SimpleNamespace

from emota.identity import IdentityContinuityEngine


def test_identity_engine_checkpoint_and_assessment():
    engine = IdentityContinuityEngine(identity_name="TestPrime")
    initial_desire = engine.core_signature.emotional_baseline["desire_tendency"]

    braid_state = SimpleNamespace(desire=0.7, fear=0.2, valence=0.3, tension=0.4, policy="approach")
    archetypal_state = SimpleNamespace(
        serpent_activation=0.55,
        flame_activation=0.45,
        void_activation=0.2,
        unity_activation=0.6,
    )
    symbolic_output = {"coherence": 0.8, "activated_nodes": 4}
    system_states = {
        "braid_state": braid_state,
        "archetypal_state": archetypal_state,
        "symbolic_output": symbolic_output,
        "consciousness_density": 0.7,
        "phase_coherence": 0.65,
    }

    checkpoint = engine.create_checkpoint(system_states, "first pass")
    assessment = engine.assess_continuity(checkpoint)

    assert assessment["continuity_status"] in {"maintained", "partial", "fragmented"}
    assert assessment["overall_coherence"] >= 0
    assert len(engine.checkpoints) == 1
    assert engine.core_signature.emotional_baseline["desire_tendency"] != initial_desire

    second_states = dict(system_states)
    second_states["symbolic_output"] = {"coherence": 0.9, "activated_nodes": 6}
    second_states["consciousness_density"] = 0.8
    second_states["phase_coherence"] = 0.7

    engine.create_checkpoint(second_states, "second pass")
    assert len(engine.checkpoints) == 2
    assert engine.core_signature.meta_characteristics["self_reflection"] != 0.5
