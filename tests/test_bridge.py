from emota.bridge import DimensionalConsciousnessBridge


def test_bridge_generates_projection_and_transcendence():
    bridge = DimensionalConsciousnessBridge()

    for idx in range(4):
        bridge.add_experience(f"Experience {idx}", {"affect": 0.2 * idx})

    first_projection = bridge.project_to_4d()
    assert len(first_projection.integration_vector) == 12
    assert first_projection.depth == 1
    assert first_projection.coherence >= 0.0

    bridge.add_experience("Integration spike", {"affect": 0.9})
    bridge.project_to_4d()

    transcendence = bridge.transcend_to_5d()
    assert transcendence.transcendence_depth == len(bridge.transcendences)
    assert 0.0 <= transcendence.phase_coherence <= 1.0
    assert len(transcendence.meta_vector) == 10
    assert transcendence.reality_generation_potential >= 0.0
