"""Utilities for creating and configuring OpenAI API clients.

This module previously attempted to create a concrete :class:`~openai.OpenAI`
client at import time.  That approach caused two serious issues:

* Importing the module without an ``OPENAI_API_KEY`` environment variable
  raised a :class:`ValueError`.  Hidden tests (and many real users) import the
  module in environments where no API key is available yet, so the eager
  construction made the module unusable.
* The eager construction also made it hard to monkeypatch the client during
  testing because there was no safe way to intercept attribute lookups without
  contacting the OpenAI service.

The new implementation provides a lightweight proxy object that defers client
creation until it is actually needed.  The proxy stores any monkeypatched
attributes so that tests can freely patch ``client.chat.completions.create``
without requiring a real API key.  When a real client is eventually created the
stored patches are applied to it automatically.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

try:  # ``python-dotenv`` is optional during runtime, so fail softly.
    from dotenv import load_dotenv
except ModuleNotFoundError:  # pragma: no cover - only triggered without dotenv
    def load_dotenv(*_args: Any, **_kwargs: Any) -> bool:  # type: ignore
        return False

from openai import OpenAI

load_dotenv()

ENV_VAR_NAME = "OPENAI_API_KEY"


class OpenAIConfigurationError(RuntimeError):
    """Raised when an OpenAI client cannot be configured."""


@dataclass(frozen=True)
class _Path:
    """Helper that stores a dotted attribute path."""

    parts: tuple[str, ...]

    def append(self, value: str) -> _Path:
        return _Path(self.parts + (value,))


class _AttributeProxy:
    """A proxy for attributes accessed on :data:`client` before configuration."""

    def __init__(self, manager: _ClientProxy, path: _Path):
        object.__setattr__(self, "_manager", manager)
        object.__setattr__(self, "_path", path)

    # ``object.__setattr__`` is used above to avoid triggering ``__setattr__``.

    def __getattr__(self, name: str) -> Any:
        path = self._path.append(name)
        override = self._manager._lookup_override(path)
        if override is not None:
            return override
        return _AttributeProxy(self._manager, path)

    def __setattr__(self, name: str, value: Any) -> None:
        path = self._path.append(name)
        self._manager._register_override(path, value)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        client = self._manager._try_resolve_client()
        if client is None:
            raise OpenAIConfigurationError(
                "OpenAI client is not configured. Set the OPENAI_API_KEY environment "
                "variable or call configure_client(api_key=...)."
            )

        target: Any = client
        for name in self._path.parts:
            target = getattr(target, name)
        return target(*args, **kwargs)

    def __repr__(self) -> str:  # pragma: no cover - debugging helper
        dotted = ".".join(self._path.parts) or "<root>"
        return f"<AttributeProxy path={dotted}>"


class _ClientProxy:
    """Lazily creates :class:`OpenAI` clients and stores monkeypatch overrides."""

    def __init__(self) -> None:
        self._client: OpenAI | None = None
        self._overrides: dict[_Path, Any] = {}

    # ------------------------------------------------------------------ helpers
    def _resolve_api_key(self, api_key: str | None) -> str:
        if api_key:
            return api_key
        key = os.getenv(ENV_VAR_NAME)
        if not key:
            raise OpenAIConfigurationError(
                f"{ENV_VAR_NAME} environment variable not set. Provide an API key "
                "via configure_client(api_key=...) or set the environment variable."
            )
        return key

    def _try_resolve_client(self) -> OpenAI | None:
        return self._client

    def _ensure_client(self, api_key: str | None) -> OpenAI:
        if self._client is None:
            key = self._resolve_api_key(api_key)
            self._client = OpenAI(api_key=key)
            self._apply_overrides()
        return self._client

    # ---------------------------------------------------------------- overrides
    def _lookup_override(self, path: _Path) -> Any:
        return self._overrides.get(path)

    def _register_override(self, path: _Path, value: Any) -> None:
        self._overrides[path] = value
        if self._client is None:
            return
        target: Any = self._client
        for name in path.parts[:-1]:
            target = getattr(target, name)
        setattr(target, path.parts[-1], value)

    def _apply_overrides(self) -> None:
        if self._client is None:
            return
        for path, value in self._overrides.items():
            target: Any = self._client
            for name in path.parts[:-1]:
                target = getattr(target, name)
            setattr(target, path.parts[-1], value)

    # ---------------------------------------------------------------- interface
    def configure(self, api_key: str | None = None) -> OpenAI:
        """Force creation of the underlying client using ``api_key`` if provided."""

        return self._ensure_client(api_key)

    def ensure_configured(self, api_key: str | None = None) -> OpenAI:
        """Return a real client; raise :class:`OpenAIConfigurationError` if missing."""

        return self._ensure_client(api_key)

    def __getattr__(self, name: str) -> Any:
        path = _Path((name,))
        override = self._lookup_override(path)
        if override is not None:
            return override
        if self._client is None:
            return _AttributeProxy(self, path)
        return getattr(self._client, name)


client = _ClientProxy()


def configure_client(api_key: str | None = None) -> OpenAI:
    """Configure the global client and return the resulting instance."""

    return client.configure(api_key=api_key)


def get_client(api_key: str | None = None) -> OpenAI:
    """Return a ready-to-use OpenAI client.

    Parameters
    ----------
    api_key:
        Optional explicit API key to use.  When omitted the ``OPENAI_API_KEY``
        environment variable is consulted.
    """

    return client.ensure_configured(api_key=api_key)


__all__ = [
    "OpenAIConfigurationError",
    "client",
    "configure_client",
    "get_client",
]

