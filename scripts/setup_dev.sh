#!/usr/bin/env bash
# Development Environment Setup Script for PrimeCodex
# Optimized for GitHub Copilot Coding Agent workflow

set -euo pipefail

echo "🚀 Setting up PrimeCodex development environment..."

# Check Python version
python_version=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
required_version="3.10"

if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 10) else 1)" 2>/dev/null; then
    echo "❌ Python 3.10+ required. Found: $python_version"
    echo "Please install Python 3.10 or higher and try again."
    exit 1
fi

echo "✅ Python version: $python_version"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip --quiet || echo "⚠️  pip upgrade had issues, continuing..."

# Install dependencies with timeout and fallback
echo "📚 Installing dependencies..."
if [ -f "pyproject.toml" ]; then
    echo "Attempting editable install..."
    timeout 120 pip install -e .[dev] --quiet || {
        echo "⚠️  Editable install failed, trying manual dependency installation..."
        pip install pytest openai python-dotenv PyYAML jsonschema ruff bandit safety --quiet --timeout 60 || echo "⚠️  Some packages may not have installed correctly"
    }
else
    # Fallback to manual installation
    pip install pytest openai python-dotenv PyYAML jsonschema ruff bandit safety --quiet --timeout 60 || echo "⚠️  Some packages may not have installed correctly"
fi

# Enable git hooks for secret scanning
echo "🔒 Enabling git hooks for secret scanning..."
if [ -d ".githooks" ]; then
    git config core.hooksPath .githooks
    echo "✅ Git hooks enabled"
else
    echo "⚠️  No .githooks directory found"
fi

# Create config override template if it doesn't exist
if [ ! -f "emota/config.local.yaml" ] && [ -f "emota/config.yaml" ]; then
    echo "📝 Creating local config template..."
    cp emota/config.yaml emota/config.local.yaml
    echo "✅ Created emota/config.local.yaml (you can customize this)"
fi

# Create .env template if it doesn't exist
if [ ! -f ".env.template" ]; then
    echo "🔑 Creating .env template..."
    cat > .env.template << 'EOF'
# OpenAI API Configuration
# Copy this file to .env and add your actual API key
# Never commit .env - it's gitignored for security

OPENAI_API_KEY=your-openai-api-key-here

# Optional: Custom config path
# EMOTA_CONFIG=emota/config.local.yaml

# Optional: Logging level
# LOG_LEVEL=INFO

# Optional: Development mode settings
# DEVELOPMENT=true
EOF
    echo "✅ Created .env.template"
fi

# Run basic tests to verify setup (with timeout)
echo "🧪 Running basic tests to verify setup..."
if timeout 60 python -c "import pytest, openai, yaml, jsonschema; print('Core imports successful')" 2>/dev/null; then
    echo "✅ Core imports working!"
    
    # Try running a quick test if pytest is available
    if timeout 30 python -m pytest --version >/dev/null 2>&1; then
        echo "Running quick test validation..."
        timeout 30 python -m pytest --quiet --tb=no -x || echo "⚠️  Some tests failed, but environment is set up"
    fi
else
    echo "⚠️  Some imports failed, but basic environment is set up"
fi

# Display next steps
echo ""
echo "🎉 Development environment setup complete!"
echo ""
echo "Next steps:"
echo "  1. Copy .env.template to .env and add your OpenAI API key (optional)"
echo "  2. Customize emota/config.local.yaml if needed"
echo "  3. Run 'source .venv/bin/activate' to activate the environment"
echo "  4. Run 'pytest' to run tests"
echo "  5. Run 'python cli.py --help' to see CLI options"
echo ""
echo "For more information, see:"
echo "  - README.md for quick start guide"
echo "  - COPILOT_AGENT.md for AI development guidelines"
echo "  - CONTRIBUTING.md for contribution guidelines"