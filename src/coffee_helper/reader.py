from csv import DictReader
from pathlib import Path


def read_files(files: list[Path]) -> list[dict]:
    """
    Reads multiple CSV files and returns a list of dict.

    Args:
        files (list[Path]): List of CSV file paths.

    Returns:
        list[dict]: list of rows as dict.
    """

    rows: list[dict] = []

    for file in files:
        with open(file, "r", encoding="utf-8-sig") as f:
            reader: DictReader = DictReader(f)
            rows.extend(reader)

    return rows
