#!/usr/bin/env bash
set -euo pipefail

# Build all web, server, and reference components across the monorepo
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
echo "=== Building bobsgameweb client ==="
cd "$ROOT_DIR/bobsgameweb"

if [ ! -d "node_modules" ]; then
    echo "Installing bobsgameweb dependencies..."
    npm install
fi

echo "Running TypeScript typecheck..."
npm run typecheck

echo "Running Vite client build..."
npx vite build

echo "=== Running test suites ==="
python3 "$ROOT_DIR/scripts/test_runner.py"

echo "=== All builds and tests passed successfully! ==="
