"""Legacy compatibility wrapper for the GenesisPrime CLI."""

from __future__ import annotations

import sys
from typing import List, Optional

from primecodex_cli import genesis_main


def main(argv: Optional[List[str]] = None) -> None:
    args = [sys.argv[0]] + (list(argv) if argv is not None else sys.argv[1:])
    genesis_main(args)


if __name__ == "__main__":  # pragma: no cover
    main()