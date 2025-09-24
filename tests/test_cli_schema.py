import json
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import validate, ValidationError

SCHEMA_PATH = Path("schema/cli_output.schema.json")


def run_cli():
    cmd = [sys.executable, "-m", "primecodex", "--goal", "0.5", "--threat", "0.2", "Sample experience"]
    # Fallback if entrypoint module name not resolvable, call cli.py directly
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
    except Exception:
        out = subprocess.check_output([sys.executable, "cli.py", "--goal", "0.5", "--threat", "0.2", "Sample experience"], text=True)
    return json.loads(out.strip())


@pytest.mark.parametrize("_", [0])
def test_cli_output_schema(_):
    data = run_cli()
    schema = json.loads(SCHEMA_PATH.read_text())
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        pytest.fail(f"Schema validation failed: {e}")
