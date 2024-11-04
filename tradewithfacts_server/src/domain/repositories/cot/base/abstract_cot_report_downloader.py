from abc import ABC, abstractmethod

import pandas as pd


class AbstractCOTReportDownloader(ABC):
    """
    Responsible for Downloading the COT report.
    """

    @abstractmethod
    def download(self, years_to_download) -> list[pd.DataFrame]:
        """
        :param years_to_download: The amount of years to download.
        :return: The downloaded COT report in a data frames.
        """
        ...

    @abstractmethod
    def store_locally(self, storage_details: dict, report: pd.DataFrame, years_count: int) -> None:
        """
        :param storage_details: details about the storage.
        :param report: COT report as a data frame.
        :param years_count: Years of report you are storing.
        :return: None
        """