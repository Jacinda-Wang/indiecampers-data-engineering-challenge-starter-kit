from pathlib import Path


def run_pipeline(input_dir: Path, database_path: Path) -> None:
    """Process booking batches into the required DuckDB models."""
    raise NotImplementedError(
        "Implement ingestion, validation, current-state merging, and reporting"
    )
