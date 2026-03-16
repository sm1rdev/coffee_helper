from argparse import Namespace
from tabulate import tabulate

from coffee_helper.reader import read_files
from coffee_helper.reports import REPORTS
from coffee_helper.reports.base import BaseReport
from coffee_helper.utils import get_args


def main() -> None:
    """
    Main CLI entry point.

    1. Parses command-line arguments using get_args().
    2. Checks if the selected report exists in REPORTS.
    3. Reads all CSV files.
    4. Generates the selected report.
    5. Prints the report as a formatted table.
    """

    args: Namespace = get_args()

    if args.report not in REPORTS:
        raise ValueError(f"Unknown report: {args.report}")

    rows: list[dict] = read_files(args.files)

    report: BaseReport = REPORTS[args.report]()

    result_str, result_data = report.generate(rows)

    print(result_str)


if __name__ == "__main__":
    main()
