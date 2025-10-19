#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Configuration ---
BIN_DIR="bin"
NODE_BINARY_NAME="quantumd"
BINARY_PATH="$BIN_DIR/$NODE_BINARY_NAME"

# --- Script ---

echo "🚀 Starting Quantum Blockchain Node..."

# 1. Check if the node binary exists
if [ ! -f "$BINARY_PATH" ]; then
    echo "❌ Node binary not found at '$BINARY_PATH'."
    echo "   Please run the build script first: ./build_quantum_node.sh"
    exit 1
fi

echo "✅ Node binary found. Executing..."
echo "----------------------------------------"

# 2. Run the node
./"$BINARY_PATH"

echo "----------------------------------------"
echo "✅ Node execution finished."
