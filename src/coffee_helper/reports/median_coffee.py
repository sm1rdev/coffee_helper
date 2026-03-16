from collections import defaultdict
from statistics import median
from tabulate import tabulate

from coffee_helper.reports.base import BaseReport


class MedianCoffeeSpentReport(BaseReport):
    name = "median-coffee"

    def generate(self, rows: list[dict]) -> str:
        students: dict[str, list] = defaultdict(list)

        for row in rows:
            students[row['student']].append(int(row['coffee_spent']))

        result = []

        for student, values in students.items():
            result.append([student, median(values)])

        result.sort(key=lambda x: x[1], reverse=True)

        return tabulate(
            result,
            headers=[
                "student", "median_coffee"
            ],
            tablefmt="grid"
        )
