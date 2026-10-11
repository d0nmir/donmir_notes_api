#!/usr/bin/env bash
set -euo pipefail

export PORT="${PORT:-8080}"

python3 app.py &
APP_PID=$!

cleanup() {
    kill "$APP_PID" 2>/dev/null || true
}
trap cleanup EXIT

# Wait until /healthz answers 200 (up to ~10 s) instead of a blind "sleep 1".
ready=0
for _ in $(seq 1 50); do
    if ! kill -0 "$APP_PID" 2>/dev/null; then
        echo "app.py exited before it became ready (is port $PORT busy?)" >&2
        exit 1
    fi
    if python3 -c "import os, urllib.request as u; u.urlopen('http://localhost:%s/healthz' % os.environ['PORT'], timeout=1)" 2>/dev/null; then
        ready=1
        break
    fi
    sleep 0.2
done

if [ "$ready" -ne 1 ]; then
    echo "server did not become ready in time" >&2
    exit 1
fi

python3 test_app.py