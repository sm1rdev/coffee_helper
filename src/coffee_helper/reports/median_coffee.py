from collections import defaultdict
from statistics import median
from tabulate import tabulate

from coffee_helper.reports.base import BaseReport


class MedianCoffeeSpentReport(BaseReport):
    """
    Report that calculates the median coffee spending per student.

    Attributes:
        name (str): Report name used in the REPORTS registry.
    """

    name = "median-coffee"

    def generate(self, rows: list[dict]) -> tuple[str, list]:
        """
        Calculates the median coffee spending for each student
        and sorts students by descending spending.

        Args:
            rows (list[dict]): CSV data with 'student' and 'coffee_spent' fields.

        Returns:
            tuple[str, list]: 
                - Formatted table string for console output
                - List of [student, median_coffee] pairs for testing
        """

        students: dict[str, list] = defaultdict(list)

        for row in rows:
            students[row['student']].append(int(row['coffee_spent']))

        result = []

        for student, values in students.items():
            result.append([student, median(values)])

        result.sort(key=lambda x: x[1], reverse=True)

        return (tabulate(
            result,
            headers=[
                "student", "median_coffee"
            ],
            tablefmt="grid"
        ), result)
