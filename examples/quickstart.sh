#!/usr/bin/env bash
set -euo pipefail

# Keep the demo isolated from any existing .agent_memory.db in the caller's project.
demo_dir="$(mktemp -d)"
trap 'rm -rf "$demo_dir"' EXIT
cd "$demo_dir"

amem add "The service uses PostgreSQL for durable storage" --tags "architecture,database"
amem search "PostgreSQL"
