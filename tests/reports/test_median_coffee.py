import pytest
from pathlib import Path

from coffee_helper.reader import read_files
from coffee_helper.reports.median_coffee import MedianCoffeeSpentReport


def get_result(rows: list[dict]) -> list:
    median_coffee_report: MedianCoffeeSpentReport = MedianCoffeeSpentReport()
    result_str, result_list = median_coffee_report.generate(rows)
    return result_list


def test_one_csv_file(samples_dir: Path):
    rows: list[dict] = read_files([samples_dir / "math.csv"])

    result: list[dict] = get_result(rows)

    assert result[0][1] == 650
    assert result[1][1] == 570


def test_all_csv_files(samples_dir: Path):
    rows: list[dict] = read_files(
        [
            samples_dir / "math.csv",
            samples_dir / "physics.csv",
            samples_dir / "programming.csv"
        ]
    )

    result: list[dict] = get_result(rows)

    assert result[0][1] == 700
    assert result[1][1] == 610
    assert result[-1][1] == 140
