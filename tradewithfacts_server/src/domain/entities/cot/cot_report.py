from typing import Final

from src.domain.entities.cot.cot_record import COTRecord


class COTReport:
    """
    Weekly publication by the Commodity Futures Trading Commission (CFTC). It provides a breakdown of the positions held
    by different types of traders in the Futures market, including forex. The report is released every Friday and covers
    data up to the end of the trading day on Tuesday of the same week.
    Forex traders use the COT report to gauge market sentiment and make informed trading decisions based on the
    positions of these major market players.
    """

    def __init__(self, as_of: str, valid_till: str, records: list[COTRecord]):
        """
        :param as_of: Internal release date of the COT report.
        :param valid_till: Valid period of the COT report.
        :param records: List of records in the COT report.
        """
        self.as_of: Final[str] = as_of
        self.valid_till: Final[str] = valid_till
        self.records: Final[list[COTRecord]] = records

    def to_dict(self) -> dict:
        return {
            "as_of": self.as_of,
            "valid_till": self.valid_till,
            "records": list(map(lambda record: record.to_dict(), self.records))
        }