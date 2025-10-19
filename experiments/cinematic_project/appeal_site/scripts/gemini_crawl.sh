#!/usr/bin/env bash
set -euo pipefail
PAGE_URL="${1:-http://localhost:8000/index.html}"
OUTFILE="$(dirname "$0")/../logs/gemini_response.json"

if [ -z "${GEMINI_API_KEY:-}" ]; then
  echo "ERROR: Please set GEMINI_API_KEY environment variable first."
  echo ' export GEMINI_API_KEY="YOUR_KEY"'
  exit 2
fi

echo "Fetching page content from $PAGE_URL..."
PAGE_CONTENT=$(curl -sS "$PAGE_URL" | sed 's/"/\\"/g' | sed ':a;N;$!ba;s/\n/\\n/g')

echo "Sending page content to Gemini API for review..."
curl -sS "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H "Content-Type: application/json" \
  -H "X-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -d "{
    \"contents\": [
      {\"parts\": [{\"text\": \"Please review the following HTML page for clarity, suggested edits for tone and legal risk for public posting, and create a short safe-public summary (redacted) suitable for public posting. Page follows:\\n\\n$PAGE_CONTENT\"}]}
    ]
  }" > "$OUTFILE"

echo "Gemini response saved to: $OUTFILE"
