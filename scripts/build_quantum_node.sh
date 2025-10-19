#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Configuration ---
CORE_DIR="core"
BIN_DIR="bin"
NODE_BINARY_NAME="quantumd"

# --- Script ---

echo "🚀 Starting Quantum Blockchain Node Build..."

# 1. Check for Go installation
if ! command -v go &> /dev/null
then
    echo "❌ Go is not installed. Please install Go and try again."
    exit 1
fi

echo "✅ Go is installed."
GO_VERSION=$(go version)
echo "   - Version: $GO_VERSION"

# 2. Create output directory if it doesn't exist
if [ ! -d "$BIN_DIR" ]; then
    echo "🔧 Creating build output directory: $BIN_DIR"
    mkdir -p "$BIN_DIR"
else
    echo "👍 Build output directory already exists: $BIN_DIR"
fi

# 3. Fetch dependencies
if [ -f "go.mod" ]; then
    echo "📦 Fetching Go module dependencies..."
    go mod tidy
else
    echo "⚠️ Warning: go.mod not found. Skipping dependency fetch."
fi

# 4. Build the node
echo "🏗️ Compiling the blockchain node from '$CORE_DIR'..."
go build -o "$BIN_DIR/$NODE_BINARY_NAME" "./$CORE_DIR"

echo "✅ Build successful!"
echo "   - Node binary created at: $BIN_DIR/$NODE_BINARY_NAME"
echo "🎉 Quantum node build process complete."
