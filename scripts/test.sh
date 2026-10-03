#!/usr/bin/env bash
set -euo pipefail

export PORT="${PORT:-8080}"

python3 app.py &
APP_PID=$!

cleanup() {
    kill "$APP_PID" 2>/dev/null || true
}
trap cleanup EXIT

sleep 1

python3 test_app.py