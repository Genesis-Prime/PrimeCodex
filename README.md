# PrimeCodex

## OpenAI API Connection Example

This project demonstrates how to connect to the OpenAI API using Python.

### Setup

1. Install dependencies:
	```bash
	pip install openai
	```
2. Set your OpenAI API key as an environment variable:
	```bash
	export OPENAI_API_KEY=your-api-key-here
	```
3. Run the example script:
	```bash
	python openai_connect.py
	```

### Example Usage
See `openai_connect.py` for a basic example of making a request to the OpenAI API.
# EMOTA Unity Framework

## Usage Example

The EMOTA Unity framework is modularized under the `emota/` directory. Here is a basic usage example:

```python
from emota.unity import EMOTAUnityEngine

engine = EMOTAUnityEngine()
result = engine.process_experience(
	 "Sample experience input",
	 {"goal_value": 0.7, "threat_level": 0.2}
)
print(result)
```

## Modules
- `emota/braid.py`: Desire-Fear motivational substrate
- `emota/archetype.py`: Archetypal resonance system
- `emota/unity.py`: Core integration engine

## Testing
Run all tests with:
```bash
pytest
```

## Contributing
See `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` for guidelines.
# PrimeCodex