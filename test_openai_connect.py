import os
import sys
import types
import pytest

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

API_KEY_PRESENT = bool(os.getenv("OPENAI_API_KEY"))

@pytest.mark.skipif(not API_KEY_PRESENT, reason="No API key set; skipping live OpenAI tests")
def test_openai_chat_completion(monkeypatch):
    from openai_connect import client

    class DummyChoice:
        def __init__(self):
            self.message = types.SimpleNamespace(content="ok")

    class DummyResponse:
        def __init__(self):
            self.choices = [DummyChoice()]

    def fake_create(**kwargs):
        return DummyResponse()

    monkeypatch.setattr(client.chat.completions, "create", lambda **kwargs: fake_create(**kwargs))
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Test"}]
    )
    assert response.choices[0].message.content == "ok"

