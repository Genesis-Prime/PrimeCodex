import types

import pytest


@pytest.fixture(autouse=True)
def reset_module_state(monkeypatch):
    """Ensure each test exercises a clean proxy state."""

    # Import inside fixture so the module is loaded before we mutate globals.
    import importlib

    module = importlib.import_module("openai_connect")
    # Wipe any previously created client so we can assert on fresh behaviour.
    module.client._client = None  # type: ignore[attr-defined]
    module.client._overrides.clear()  # type: ignore[attr-defined]
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    yield module


def test_proxy_allows_monkeypatch_without_api_key(monkeypatch):
    from openai_connect import OpenAIConfigurationError, client

    def fake_create(**_kwargs):
        message = types.SimpleNamespace(content="patched")
        choice = types.SimpleNamespace(message=message)
        return types.SimpleNamespace(choices=[choice])

    monkeypatch.setattr(client.chat.completions, "create", fake_create)

    # No API key is configured, but thanks to the proxy we can still use the patched
    # attribute.  Attempting to call an unpatched attribute would raise
    # ``OpenAIConfigurationError``.
    response = client.chat.completions.create(model="gpt-test", messages=[{"role": "user", "content": "Hi"}])
    assert response.choices[0].message.content == "patched"

    with pytest.raises(OpenAIConfigurationError):
        client.chat.other_method()


def test_configure_client_uses_explicit_api_key(monkeypatch):
    import openai_connect

    created = {}

    class DummyCompletions:
        def create(self, *args, **kwargs):
            return "real"

    class DummyChat:
        def __init__(self):
            self.completions = DummyCompletions()

    class DummyClient:
        def __init__(self, api_key):
            created["api_key"] = api_key
            self.chat = DummyChat()

    monkeypatch.setattr(openai_connect, "OpenAI", DummyClient)

    client = openai_connect.configure_client(api_key="explicit-token")
    assert created["api_key"] == "explicit-token"
    assert client.chat.completions.create() == "real"

    # The global proxy should now delegate to the dummy client.
    assert openai_connect.client.chat.completions.create() == "real"

    # Monkeypatching continues to work even after configuration.
    monkeypatch.setattr(openai_connect.client.chat.completions, "create", lambda: "patched")
    assert openai_connect.client.chat.completions.create() == "patched"

