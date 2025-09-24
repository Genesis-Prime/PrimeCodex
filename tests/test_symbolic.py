from emota.symbolic import EchOSSymbolicEngine


def test_symbolic_engine_activation_and_signature():
    engine = EchOSSymbolicEngine()

    signature = engine.generate_symbolic_signature(
        "A transcendent unity emerges to bridge stillness and wonder"
    )
    assert "∞" in signature
    assert "◈" in signature or "⟢" in signature

    result = engine.process_symbolic_pattern(signature[:3])
    assert isinstance(result["output"], list)
    assert result["coherence"] >= 0.0
    assert result["activated_nodes"] <= len(signature[:3])
    assert engine.recursive_depth == 0
