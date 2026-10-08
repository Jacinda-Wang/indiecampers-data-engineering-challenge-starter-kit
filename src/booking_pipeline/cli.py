import argparse
from collections.abc import Sequence
from pathlib import Path

from booking_pipeline.pipeline import run_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build current bookings and daily depot operations metrics."
    )
    parser.add_argument(
        "--input-dir",
        required=True,
        type=Path,
        help="Directory containing depots.csv and bookings_*.csv files.",
    )
    parser.add_argument(
        "--database",
        required=True,
        type=Path,
        help="Path to the DuckDB database to create or update.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    run_pipeline(input_dir=args.input_dir, database_path=args.database)
    return 0
