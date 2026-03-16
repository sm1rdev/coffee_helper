from abc import ABC, abstractmethod


class BaseReport(ABC):
    """
    Abstract base class for all reports.

    All reports must implement the `generate` method.
    """

    @abstractmethod
    def generate(self, rows: list[dict]) -> tuple[str, list]:
        """
        Generates a report from the given student data.

        Args:
            rows (list[dict]): List of CSV rows as dictionaries.

        Returns:
            tuple[str, list]: 
                - str: Formatted report string for console output
                - list: Raw report data for testing or further processing
        """

        pass
