"""Legacy compatibility wrapper for the Typer-based PrimeCodex EMOTA CLI."""

from __future__ import annotations

import argparse
import json
import sys
from typing import List, Optional

from primecodex_cli import execute_emota


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="PrimeCodex EMOTA Unity CLI (compat mode)")
    parser.add_argument("experience", nargs="?", help="Experience text (omit to read stdin)")
    parser.add_argument("--goal", type=float, default=0.5, help="Goal value (0-1)")
    parser.add_argument("--threat", type=float, default=0.0, help="Threat level (0-1)")
    parser.add_argument("--novelty", type=float, default=0.0, help="Novelty (0-1)")
    parser.add_argument("--uncertainty", type=float, default=0.0, help="Uncertainty (0-1)")
    parser.add_argument("--config", type=str, default="emota/config.yaml", help="Path to config YAML")
    parser.add_argument("--memory-path", type=str, help="Path to persist episodic memory JSON")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser


def main(argv: Optional[List[str]] = None) -> None:
    args_list = argv if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(args_list)

    experience_text = args.experience or sys.stdin.read().strip()
    if not experience_text:
        parser.error("Experience text must be provided either as an argument or via stdin.")

    result = execute_emota(
        experience_text,
        args.goal,
        args.threat,
        args.novelty,
        args.uncertainty,
        args.config,
        args.memory_path,
    )
    output = json.dumps(result, indent=2 if args.pretty else None)
    print(output)


if __name__ == "__main__":  # pragma: no cover
    main()
