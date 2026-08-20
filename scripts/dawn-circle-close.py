#!/usr/bin/env python3
"""Close the day's Dawn Circle card at the end of its morning window.

Generalized from the production SMF Works ritual. Same env config as
dawn-circle-create.py.

NOTE (learned in production): `hermes kanban show <id> --json` wraps the task
under a `task` key, while `hermes kanban list --json` returns flat task dicts.
This close script unwraps both shapes — a bug in naive "verify after close"
scripts caused 7 silent days of failed verification.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Any
from zoneinfo import ZoneInfo
import datetime as dt

BOARD = os.environ.get("DAWN_CIRCLE_BOARD", "team")
TIMEZONE = ZoneInfo(os.environ.get("DAWN_CIRCLE_TZ", "America/New_York"))
STATE_DIR = Path(os.environ.get("DAWN_CIRCLE_STATE_DIR", ".state/dawn-circle"))


def _circle_date() -> str:
    return os.environ.get("DAWN_CIRCLE_DATE") or dt.datetime.now(TIMEZONE).date().isoformat()


def _hermes_bin() -> str:
    return os.environ.get("HERMES_BIN") or shutil.which("hermes") or "hermes"


def _run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, check=True, capture_output=True, text=True)


def _run_json(command: list[str]) -> Any:
    completed = _run(command)
    return json.loads(completed.stdout)


def _unwrap_task(obj: Any) -> dict:
    """Normalise `show --json` (wrapped under `task`) and `list --json` (flat)."""
    if isinstance(obj, dict) and "task" in obj and isinstance(obj["task"], dict):
        return obj["task"]
    return obj if isinstance(obj, dict) else {}


def _state_path(day: str) -> Path:
    return STATE_DIR / f"{day}.json"


def _find_task(day: str, title: str) -> dict:
    path = _state_path(day)
    if path.exists():
        payload = json.loads(path.read_text(encoding="utf-8"))
        task_id = payload.get("id")
        if task_id:
            task = _unwrap_task(
                _run_json(
                    [
                        _hermes_bin(),
                        "kanban",
                        f"--board={BOARD}",
                        "show",
                        str(task_id),
                        "--json",
                    ]
                )
            )
            if task.get("title") == title:
                return task

    tasks = _run_json([_hermes_bin(), "kanban", f"--board={BOARD}", "list", "--archived", "--json"])
    if not isinstance(tasks, list):
        raise RuntimeError(f"Expected a task list, received: {tasks!r}")
    matches = [task for task in tasks if task.get("title") == title]
    if not matches:
        raise RuntimeError(f"No Dawn Circle card found for {day}")
    if len(matches) > 1:
        raise RuntimeError(f"Multiple Dawn Circle cards found for {day}: {matches!r}")
    return matches[0]


def _write_state(day: str, task: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    path = _state_path(day)
    temp = path.with_suffix(".json.tmp")
    temp.write_text(json.dumps(task, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def main() -> int:
    day = _circle_date()
    title = f"Dawn Circle — {day}"
    task = _find_task(day, title)
    task_id = task.get("id")
    if not task_id:
        raise RuntimeError(f"Dawn Circle task has no id: {task!r}")
    if task.get("assignee") is not None:
        raise RuntimeError(f"Dawn Circle must remain unassigned; received {task!r}")

    if task.get("status") == "done":
        _write_state(day, task)
        print(f"Dawn Circle already closed: {task_id} ({day})")
        return 0
    if task.get("status") == "archived":
        raise RuntimeError(f"Dawn Circle was archived before closing: {task!r}")

    summary = f"Dawn Circle closed at 09:00 on {day}."
    _run(
        [
            _hermes_bin(),
            "kanban",
            f"--board={BOARD}",
            "complete",
            str(task_id),
            f"--result={summary}",
            f"--summary={summary}",
        ]
    )
    closed = _unwrap_task(
        _run_json([_hermes_bin(), "kanban", f"--board={BOARD}", "show", str(task_id), "--json"])
    )
    if closed.get("status") != "done":
        raise RuntimeError(f"Dawn Circle did not close cleanly: {closed!r}")

    _write_state(day, closed)
    print(f"Dawn Circle closed: {task_id} ({day})")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except subprocess.CalledProcessError as exc:
        print(
            f"Dawn Circle closure failed (exit {exc.returncode}): "
            f"stdout={exc.stdout!r} stderr={exc.stderr!r}",
            file=sys.stderr,
        )
        sys.exit(exc.returncode or 1)
    except Exception as exc:
        print(f"Dawn Circle closure failed: {exc}", file=sys.stderr)
        sys.exit(1)
