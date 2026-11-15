#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

action="${1:-status}"
echo "=== Managing bob's game local development servers: $action ==="

if [ "$action" = "start" ]; then
    echo "Starting Vite Dev Server..."
    (cd "$ROOT_DIR/bobsgameweb" && npm run dev > /tmp/vite.log 2>&1 &)
    echo "Starting AI Proxy Server (port 8080)..."
    (cd "$ROOT_DIR/bobsgameweb/server" && node ai_proxy.js > /tmp/ai_proxy.log 2>&1 &)
    echo "Servers launched in background. Check /tmp/vite.log and /tmp/ai_proxy.log"
elif [ "$action" = "stop" ]; then
    echo "Stopping background node servers..."
    pkill -f "vite" || true
    pkill -f "ai_proxy.js" || true
    echo "Servers stopped."
elif [ "$action" = "restart" ]; then
    pkill -f "vite" || true
    pkill -f "ai_proxy.js" || true
    sleep 1
    (cd "$ROOT_DIR/bobsgameweb" && npm run dev > /tmp/vite.log 2>&1 &)
    (cd "$ROOT_DIR/bobsgameweb/server" && node ai_proxy.js > /tmp/ai_proxy.log 2>&1 &)
    echo "Servers restarted."
elif [ "$action" = "status" ]; then
    echo "Checking server status:"
    if pgrep -f "vite" > /dev/null; then
        echo " - Vite Dev Server: RUNNING"
    else
        echo " - Vite Dev Server: STOPPED"
    fi
    if pgrep -f "ai_proxy.js" > /dev/null; then
        echo " - AI Proxy Server: RUNNING"
    else
        echo " - AI Proxy Server: STOPPED"
    fi
else
    echo "Usage: $0 {start|stop|restart|status}"
fi
