import subprocess
import sys

import duckdb


def test_duckdb_is_available() -> None:
    with duckdb.connect(":memory:") as connection:
        assert connection.execute("SELECT 42").fetchone() == (42,)


def test_module_help_is_available() -> None:
    completed = subprocess.run(
        [sys.executable, "-m", "booking_pipeline", "--help"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0
    assert "--input-dir" in completed.stdout
    assert "--database" in completed.stdout
