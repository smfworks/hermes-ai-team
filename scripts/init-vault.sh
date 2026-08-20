#!/usr/bin/env bash
# Initialize the agent-team vault (second brain) directory tree.
# Idempotent: safe to run again.
#
# Usage:  bash scripts/init-vault.sh [BASE]
#   BASE defaults to "$HOME/AgentVault"

set -euo pipefail

BASE="${1:-$HOME/AgentVault}"

mkdir -p \
  "$BASE/Research/papers" \
  "$BASE/Research/market" \
  "$BASE/Research/alignment" \
  "$BASE/Writing/drafts" \
  "$BASE/Writing/published" \
  "$BASE/Writing/templates" \
  "$BASE/Team" \
  "$BASE/Archive"

echo "Vault ready at: $BASE"
find "$BASE" -type d | sort
