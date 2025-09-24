"""Unified Typer-based CLI for PrimeCodex."""

from __future__ import annotations

import json
import sys
from typing import Any

import typer

from emota.unity import EMOTAUnityEngine
from genesis_prime import GenesisPrime

app = typer.Typer(
    add_completion=False,
    help=(
        "PrimeCodex unified interface for EMOTA Unity experiences "
        "and GenesisPrime tools."
    ),
)

genesis_app = typer.Typer(help="Prime number exploration commands")
app.add_typer(genesis_app, name="genesis")


# ---------------------------------------------------------------------------


def _resolve_experience(experience: str | None) -> str:
    if experience:
        return experience
    data = sys.stdin.read().strip()
    if not data:
        typer.echo(
            "Experience text must be provided either as an argument or via stdin.",
            err=True,
        )
        raise typer.Exit(code=1)
    return data


def _format_list(numbers: list[int], max_per_line: int = 10) -> str:
    if not numbers:
        return "None"
    lines = []
    for idx in range(0, len(numbers), max_per_line):
        chunk = numbers[idx : idx + max_per_line]
        lines.append(", ".join(map(str, chunk)))
    return "\n".join(lines)


def execute_emota(
    experience: str | None,
    goal: float,
    threat: float,
    novelty: float,
    uncertainty: float,
    config: str,
    memory_path: str | None,
) -> dict[str, Any]:
    text = _resolve_experience(experience)
    engine = EMOTAUnityEngine(config_path=config, memory_path=memory_path)
    inputs = {
        "goal_value": goal,
        "threat_level": threat,
        "novelty": novelty,
        "uncertainty": uncertainty,
    }
    return engine.process_experience(text, inputs)


# ---------------------------------------------------------------------------
# EMOTA Unity command


@app.command("emota")
def emota_command(
    experience: str | None = typer.Argument(
        None,
        help="Experience text (omit to read from stdin)",
    ),
    goal: float = typer.Option(
        0.5,
        min=0.0,
        max=1.0,
        help="Goal value (0-1)",
    ),
    threat: float = typer.Option(
        0.0,
        min=0.0,
        max=1.0,
        help="Threat level (0-1)",
    ),
    novelty: float = typer.Option(
        0.0,
        min=0.0,
        max=1.0,
        help="Novelty measure (0-1)",
    ),
    uncertainty: float = typer.Option(
        0.0,
        min=0.0,
        max=1.0,
        help="Uncertainty measure (0-1)",
    ),
    config: str = typer.Option(
        "emota/config.yaml",
        help="Path to configuration YAML",
    ),
    memory_path: str | None = typer.Option(
        None,
        help="Path to persist episodic memory JSON",
    ),
    pretty: bool = typer.Option(False, help="Pretty-print JSON output"),
) -> None:
    """Process an experience through the EMOTA Unity engine."""

    result = execute_emota(
        experience,
        goal,
        threat,
        novelty,
        uncertainty,
        config,
        memory_path,
    )
    indent = 2 if pretty else None
    typer.echo(json.dumps(result, indent=indent))


# ---------------------------------------------------------------------------
# GenesisPrime commands


def _genesis_instance() -> GenesisPrime:
    return GenesisPrime()


@genesis_app.command("check")
def genesis_check(number: int) -> None:
    """Check whether a number is prime."""

    gp = _genesis_instance()
    result = gp.is_prime(number)
    typer.echo(f"{number} is {'prime' if result else 'not prime'}")


@genesis_app.command("generate")
def genesis_generate(
    count: int | None = typer.Option(
        None,
        "--count",
        min=1,
        help="Generate the first N primes",
    ),
    limit: int | None = typer.Option(
        None,
        "--limit",
        min=2,
        help="Generate primes up to LIMIT",
    ),
) -> None:
    """Generate prime numbers either by count or by upper limit."""

    if count is None and limit is None:
        raise typer.BadParameter("Provide either --count or --limit")
    gp = _genesis_instance()
    if count is not None:
        primes = gp.generate_primes_sequence(count)
        typer.echo(f"First {count} primes:")
    else:
        primes = gp.generate_primes_sieve(limit or 0)
        typer.echo(f"Primes up to {limit} ({len(primes)} found):")
    typer.echo(_format_list(primes))


@genesis_app.command("factors")
def genesis_factors(number: int) -> None:
    """Return the prime factors of a number."""

    gp = _genesis_instance()
    factors = gp.prime_factors(number)
    if factors:
        factors_str = " × ".join(map(str, factors))
        typer.echo(f"{number} = {factors_str}")
        unique = sorted(set(factors))
        if len(unique) != len(factors):
            typer.echo(f"Unique prime factors: {', '.join(map(str, unique))}")
    else:
        typer.echo(f"{number} has no prime factors (less than 2)")


@genesis_app.command("next")
def genesis_next(number: int) -> None:
    """Find the next prime after the provided number."""

    gp = _genesis_instance()
    result = gp.next_prime(number)
    typer.echo(f"Next prime after {number}: {result}")


@genesis_app.command("prev")
def genesis_prev(number: int) -> None:
    """Find the previous prime before the provided number."""

    gp = _genesis_instance()
    result = gp.prev_prime(number)
    if result is None:
        typer.echo(f"No prime before {number}")
    else:
        typer.echo(f"Previous prime before {number}: {result}")


@genesis_app.command("twin")
def genesis_twin(number: int) -> None:
    """Check whether a number is part of a twin prime pair."""

    gp = _genesis_instance()
    if gp.is_twin_prime(number):
        if gp.is_prime(number + 2):
            typer.echo(f"{number} is a twin prime (pair: {number}, {number + 2})")
        else:
            typer.echo(f"{number} is a twin prime (pair: {number - 2}, {number})")
    else:
        if gp.is_prime(number):
            typer.echo(f"{number} is prime but not a twin prime")
        else:
            typer.echo(f"{number} is not prime")


@genesis_app.command("range")
def genesis_range(start: int, end: int) -> None:
    """Return primes within the inclusive range [start, end]."""

    if start > end:
        raise typer.BadParameter("Start must be less than or equal to end")
    gp = _genesis_instance()
    primes = [p for p in gp.generate_primes_sieve(end) if start <= p <= end]
    typer.echo(f"Primes in range [{start}, {end}] ({len(primes)} found):")
    typer.echo(_format_list(primes))


@genesis_app.command("stats")
def genesis_stats() -> None:
    """Show cached statistics from GenesisPrime."""

    gp = _genesis_instance()
    stats = gp.get_stats()
    typer.echo("GenesisPrime Statistics:")
    typer.echo(f"  Cached primes: {stats['cached_primes']}")
    typer.echo(f"  Largest cached: {stats['largest_cached']}")


# ---------------------------------------------------------------------------
# Entry point helpers


def _invoke_with_args(argv: list[str]) -> None:
    original = sys.argv[:]
    try:
        sys.argv = argv
        app()
    finally:
        sys.argv = original


def _should_insert_emota(argv: list[str]) -> bool:
    if len(argv) <= 1:
        return True
    first = argv[1]
    if first in {"emota", "genesis", "--help", "-h", "--version"}:
        return False
    if first.startswith("-"):
        return True
    return True


def main(argv: list[str] | None = None) -> None:  # pragma: no cover
    args = list(argv) if argv is not None else sys.argv[:]
    if _should_insert_emota(args):
        args.insert(1, "emota")
    _invoke_with_args(args)


def emota_main(argv: list[str] | None = None) -> None:  # pragma: no cover
    args = list(argv) if argv is not None else sys.argv[:]
    if len(args) <= 1 or args[1] != "emota":
        args.insert(1, "emota")
    _invoke_with_args(args)


def genesis_main(argv: list[str] | None = None) -> None:  # pragma: no cover
    args = list(argv) if argv is not None else sys.argv[:]
    if len(args) <= 1:
        args.insert(1, "genesis")
    elif args[1] != "genesis":
        args.insert(1, "genesis")
    _invoke_with_args(args)


if __name__ == "__main__":  # pragma: no cover
    main()
