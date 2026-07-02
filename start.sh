#!/usr/bin/env bash
set -e
# Install dependencies (Render runs buildCommand, but keep this safe)
pip install -r requirements.txt

# Load environment variables from .env if present
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

python main.py
