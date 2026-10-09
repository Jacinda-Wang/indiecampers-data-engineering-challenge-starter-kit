# Starter environment

The repository contains a working Python 3.12 environment, CLI shell, DuckDB dependency, and pytest smoke test. The business pipeline is intentionally not implemented.

Run every command below from the repository root. Docker Compose is the required
supported runtime and review path: the build, CLI, tests, and completed pipeline
must work through Compose. Local Python is an optional convenience, not a separate
submission requirement.

The submission window is one week of elapsed time. Use the suggested 8–12
focused-hour timebox and document unfinished work rather than exceeding it. Contact
the hiring team for deadline or accessibility accommodations without penalty.
See the [challenge brief](../README.md) for the core behavior, including at least
one meaningful SQL transformation for current-state selection or daily report
aggregation. Your remaining internal architecture is up to you.

## Docker Compose (required)

Use Docker with Compose v2 or later. Docker Desktop on Windows or macOS can use
the default numeric user `1000:1000`. The commands below use single lines so they
also work in Windows PowerShell.

On Linux, first set your host IDs in the same Bash/sh terminal used for **all**
Compose build and run commands:

```bash
export LOCAL_UID="$(id -u)" LOCAL_GID="$(id -g)"
```

Use your normal non-root account, not `sudo`. Compose runs the app as
`${LOCAL_UID:-1000}:${LOCAL_GID:-1000}` with writable `HOME=/tmp`, so Linux output
files belong to your host user rather than root. The repository directory must be
writable by that user. These variables are not needed for Docker Desktop's default
Windows/macOS route. No privileged container or Docker socket mount is needed.

Validate and build the environment:

```bash
docker compose config
docker compose build
```

Run the starter help and smoke test:

```bash
docker compose run --rm app python -m booking_pipeline --help
docker compose run --rm app pytest -q
```

After implementing the pipeline, run it with:

```bash
docker compose run --rm app python -m booking_pipeline --input-dir /workspace/data --database /workspace/booking_operations.duckdb
```

The repository is mounted at `/workspace`, so the DuckDB file created by the last command is available on the host. Generated `*.duckdb` files are ignored by Git.

Run the same pipeline command again against the same database to demonstrate
idempotency. Reviewers of other people's submissions must use an isolated review
environment; ordinary Docker alone is not a security sandbox for untrusted code.

## Local Python (optional convenience)

For Bash/zsh with Python 3.12:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -c constraints.txt -e ".[dev]"
python -m booking_pipeline --help
pytest -q
```

After implementing the pipeline:

```bash
python -m booking_pipeline --input-dir data --database booking_operations.duckdb
```

Repeat that command to check idempotency. On Windows, prefer the supported Docker
Desktop route above; local Python setup is not required.

## Dependency baseline and line endings

The tested runtime/test baseline is DuckDB `1.5.6` and pytest `8.4.2`, recorded in
`constraints.txt`. Both the Docker build and optional local install use these
constraints; `pyproject.toml` keeps broader compatibility ranges. The Docker base
image is `python:3.12.9-slim-bookworm`. These are baseline pins, not a full transitive
dependency lock. Release validation must include an actual Docker image build and
the Compose help and test commands; `docker compose config` alone is not enough.

`.gitattributes` keeps tracked text files at LF on all supported platforms and
marks DuckDB databases and WALs as binary. Keep those attributes enabled on Windows;
use Docker Desktop and the default UID/GID rather than Linux's `id` commands.

## Starter boundaries

The following functions deliberately raise `NotImplementedError`:

- `booking_pipeline.database.connect_database`
- `booking_pipeline.pipeline.run_pipeline`

The supplied test checks only that Python, DuckDB, and the CLI environment work. Add your own tests for validation, source versioning, duplicates, stale updates, reruns, rejected records, audits, and report metrics.
