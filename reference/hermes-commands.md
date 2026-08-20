# Hermes Agent — Condensed CLI Cheat Sheet

The live authority is the official docs: `https://hermes-agent.nousresearch.com/docs/llms.txt`
(indexes every page) and the CLI itself (`hermes --help`, `hermes <command> --help`).
This sheet is a quick reference for the commands this repo's phases use.

## Install & setup
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
hermes setup          # wizard
hermes model          # model/provider picker
hermes doctor         # health check
hermes chat -q "..."  # one-shot
```

## Profiles & Bots
```bash
hermes profile list | create <name> --clone | use <name> | delete <name>
hermes -p <name> chat          # chat as that profile
hermes -p <name> config set model.default <model>   # pin a model per profile
hermes desktop                 # open the desktop app (Bots tab lives here)
```

## Cron
```bash
hermes cron create "<schedule>" --name "<name>" --prompt "<...>"
hermes cron create "<schedule>" --name "<name>" --script <path> --prompt "<...>"
hermes cron create "<schedule>" --name "<name>" --no-agent --script <path>
hermes cron list | pause <id> | resume <id> | run <id> | edit <id> | remove <id>
```
Schedules: `30m`, `every 2h`, `0 3 * * *`, or an ISO timestamp.

## Kanban
```bash
hermes kanban init --board team
hermes kanban create "Title" --board team --assignee <bot> --body "..."
hermes kanban list | show <id> | comment <id> | assign <id> | complete <id> \
                   | block <id> | unblock <id> | link <a> <b>
hermes kanban dispatch  # gateway-embedded dispatcher (preferred)
hermes kanban daemon    # standalone — avoid if dispatch_in_gateway=true
```

## Curator (skill lifecycle)
```bash
hermes curator status | run | pin <name> | unpin <name> | archive <name> | restore <name>
```

## Memory
```bash
hermes memory setup | status | off | reset
# files: ~/.hermes/profiles/<name>/memories/USER.md and MEMORY.md
```

## Peers (cross-machine bot DMs)
```bash
hermes peer add <name> --url http://host:port --key <API_SERVER_KEY>
hermes peer list
hermes peer dm <name> < /tmp/msg.txt
hermes peer dm <name>/<bot> < /tmp/msg.txt
```

## Sessions & logs
```bash
hermes sessions list | browse | rename <id> <title> | delete <id> | export <path>
hermes logs [-f] [errors]
```

## Key paths
```
~/.hermes/config.yaml                       settings (never secrets)
~/.hermes/.env                              API keys and secrets ONLY
~/.hermes/profiles/<name>/                  a profile / Bot's home
~/.hermes/profiles/<name>/SOUL.md           identity
~/.hermes/profiles/<name>/memories/         USER.md, MEMORY.md
~/.hermes/kanban/boards/<board>/kanban.db   board data
~/.hermes/state.db                          session store
```
