from argparse import Namespace
from tabulate import tabulate

from coffee_helper.reader import read_files
from coffee_helper.reports import REPORTS
from coffee_helper.reports.base import BaseReport
from coffee_helper.utils import get_args


def main() -> None:
    args: Namespace = get_args()

    if args.report not in REPORTS:
        raise ValueError(f"Unknown report: {args.report}")

    rows: list[dict] = read_files(args.files)

    report: BaseReport = REPORTS[args.report]

    report.generate(rows)


if __name__ == "__main__":
    main()
