from csv import DictReader
from pathlib import Path


def read_files(files: list[Path]) -> list[dict]:
    rows: list[dict] = []

    for file in files:
        with open(file, "r", encoding="utf-8-sig") as f:
            reader: DictReader = DictReader(f)
            rows.extend(reader)

    return rows
