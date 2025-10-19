#!/usr/bin/env bash
set -euo pipefail
WWW_DIR="$(dirname "$0")/../www"
PORT="${1:-8000}"
cd "$WWW_DIR"
echo "Starting simple HTTP server at http://localhost:$PORT"
python3 -m http.server "$PORT" >/dev/null 2>&1 &
PID=$!
echo $PID > "../logs/server.pid" 2>/dev/null || true
echo "Server PID: $PID"
echo "Open http://localhost:$PORT in your browser to view the page."
