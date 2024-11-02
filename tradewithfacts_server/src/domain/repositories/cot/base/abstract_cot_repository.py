from abc import ABC, abstractmethod

from src.domain.entities.asset import Asset
from src.domain.entities.cot.cot_report import COTReport


class AbstractCOTRepository(ABC):
    """
    Responsible for fetching, storing, and updating the COT report.
    """

    @abstractmethod
    def fetch_latest_report(self, assets: list[Asset]) -> COTReport:
        """
        :param assets: List of assets reported in the COT report to fetch.
        :return: A COT report of the given assets.
        """

    @abstractmethod
    def fetch_historical_report(self, asset: Asset, period) -> COTReport:
        """
        :param asset: The historical report of the asset reported in the COT report.
        :param period: The length of historical report.
        :return: The historical report of the given asset.
        """
