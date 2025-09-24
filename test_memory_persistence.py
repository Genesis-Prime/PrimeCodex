import json
from pathlib import Path
from emota.unity import EMOTAUnityEngine

def test_memory_persistence(tmp_path):
    mem_file = tmp_path / "memory.json"
    engine = EMOTAUnityEngine(memory_path=str(mem_file))
    engine.process_experience("Test 1", {"goal_value": 0.3})
    engine.process_experience("Test 2", {"goal_value": 0.6})
    assert mem_file.exists()
    data = json.loads(mem_file.read_text())
    assert len(data["episodes"]) >= 2
    # Reload
    engine2 = EMOTAUnityEngine(memory_path=str(mem_file))
    assert len(engine2.memory.recent(2)) == 2