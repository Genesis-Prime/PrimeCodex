import argparse
import json
import sys
from emota.unity import EMOTAUnityEngine


def build_parser():
    p = argparse.ArgumentParser(description="PrimeCodex EMOTA Unity CLI")
    p.add_argument("experience", nargs="?", help="Experience text (omit to read stdin)")
    p.add_argument("--goal", type=float, default=0.5, help="Goal value (0-1)")
    p.add_argument("--threat", type=float, default=0.0, help="Threat level (0-1)")
    p.add_argument("--novelty", type=float, default=0.0, help="Novelty (0-1)")
    p.add_argument("--uncertainty", type=float, default=0.0, help="Uncertainty (0-1)")
    p.add_argument("--config", type=str, default="emota/config.yaml", help="Path to config YAML")
    p.add_argument("--memory-path", type=str, default=None, help="Persist memory to this JSON file")
    p.add_argument("--log-level", type=str, default="INFO", help="Logging level (INFO, DEBUG, WARNING)")
    p.add_argument("--json-logs", action="store_true", help="Emit JSON structured logs")
    p.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return p


def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.experience:
        experience = args.experience
    else:
        experience = sys.stdin.read().strip()
    engine = EMOTAUnityEngine(
        config_path=args.config,
        memory_path=args.memory_path,
        log_level=args.log_level,
        json_logging=args.json_logs
    )
    inputs = {
        "goal_value": args.goal,
        "threat_level": args.threat,
        "novelty": args.novelty,
        "uncertainty": args.uncertainty,
    }
    result = engine.process_experience(experience, inputs)
    if args.pretty:
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps(result))


if __name__ == "__main__":  # pragma: no cover
    main()
