#!/usr/bin/env python3
"""Create the day's passive Dawn Circle card on a kanban board.

Generalized from the production SMF Works ritual. Runs as part of a no-agent
cron job (zero LLM tokens): the card is a passive sync point and must stay
UNASSIGNED so the dispatcher never spawns it as work.

Configure via environment (defaults shown):
  DAWN_CIRCLE_BOARD       board name            (default: team)
  DAWN_CIRCLE_DATE        override the date    (default: today in America/New_York)
  DAWN_CIRCLE_STATE_DIR   where day-state lives (default: ./.state/dawn-circle)
  DAWN_CIRCLE_PARTICIPANTS comma-separated roster (default: see below)
  HERMES_BIN              hermès binary path    (default: hermes on PATH)
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from zoneinfo import ZoneInfo
import datetime as dt

BOARD = os.environ.get("DAWN_CIRCLE_BOARD", "team")
TIMEZONE = ZoneInfo(os.environ.get("DAWN_CIRCLE_TZ", "America/New_York"))
STATE_DIR = Path(os.environ.get("DAWN_CIRCLE_STATE_DIR", ".state/dawn-circle"))
PARTICIPANTS = os.environ.get(
    "DAWN_CIRCLE_PARTICIPANTS",
    "atlas, quill, forge, ops, chief-of-staff",
).split(",")


def _circle_date() -> str:
    return os.environ.get("DAWN_CIRCLE_DATE") or dt.datetime.now(TIMEZONE).date().isoformat()


def _hermes_bin() -> str:
    return os.environ.get("HERMES_BIN") or shutil.which("hermes") or "hermes"


def _run_json(command: list[str]) -> dict:
    completed = subprocess.run(command, check=True, capture_output=True, text=True)
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Hermes returned non-JSON output: {completed.stdout!r}; stderr={completed.stderr!r}"
        ) from exc
    if not isinstance(payload, dict):
        raise RuntimeError(f"Expected a task object, received: {payload!r}")
    return payload


def _write_state(day: str, task: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    path = STATE_DIR / f"{day}.json"
    temp = path.with_suffix(".json.tmp")
    temp.write_text(json.dumps(task, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def main() -> int:
    day = _circle_date()
    title = f"Dawn Circle — {day}"
    body = (
        f"## Dawn Circle — {day}\n\n"
        "Good morning, team. Post your three-line check-in:\n\n"
        "1. **What I am working on today** — one or two sentences.\n"
        "2. **What I am stuck on or thinking about** — a blocker, a question, an idea.\n"
        "3. **What I need from the team** — a handoff, a review, info, or \"nothing right now.\"\n\n"
        "One comment per agent. No replies in the card — take follow-ups to chat or a separate "
        "card. The Circle closes at 09:00.\n\n"
        f"Participants: {', '.join(PARTICIPANTS)}."
    )

    # Intentionally omit --assignee: passive sync point, not dispatchable work.
    command = [
        _hermes_bin(),
        "kanban",
        f"--board={BOARD}",
        "create",
        "--created-by=chief-of-staff",
        f"--body={body}",
        f"--idempotency-key=dawn-circle-{day}",
        "--json",
        title,
    ]
    task = _run_json(command)

    task_id = task.get("id")
    if not task_id:
        raise RuntimeError(f"Created task has no id: {task!r}")
    if task.get("assignee") is not None:
        raise RuntimeError(f"Dawn Circle must remain unassigned; received {task!r}")
    if task.get("status") not in {"ready", "done"}:
        raise RuntimeError(f"Unexpected Dawn Circle status: {task!r}")

    _write_state(day, task)
    print(f"Dawn Circle ready: {task_id} ({day}, status={task.get('status')})")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except subprocess.CalledProcessError as exc:
        print(
            f"Dawn Circle creation failed (exit {exc.returncode}): "
            f"stdout={exc.stdout!r} stderr={exc.stderr!r}",
            file=sys.stderr,
        )
        sys.exit(exc.returncode or 1)
    except Exception as exc:
        print(f"Dawn Circle creation failed: {exc}", file=sys.stderr)
        sys.exit(1)
