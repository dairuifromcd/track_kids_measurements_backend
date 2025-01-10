#!/usr/bin/env bash
set -e  # Exit immediately if a command exits with a non-zero status

echo "=== Step 1: Byte-compile (syntax check) ==="
python -m compileall .

echo
echo "=== Step 2: Lint with flake8 (syntax/style checks) ==="
flake8 .

echo
echo "=== Step 3: Static type checks with mypy ==="
mypy .

echo
echo "=== Step 4: Run tests with pytest ==="
pytest

echo
echo "All checks passed!"
