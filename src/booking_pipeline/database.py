from pathlib import Path

import duckdb


def connect_database(database_path: Path) -> duckdb.DuckDBPyConnection:
    """Open the configured DuckDB database."""
    raise NotImplementedError("Implement DuckDB connection and schema setup")
