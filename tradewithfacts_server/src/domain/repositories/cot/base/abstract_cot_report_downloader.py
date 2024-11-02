from abc import ABC, abstractmethod

import pandas as pd


class AbstractCOTReportDownloader(ABC):
    """
    Responsible for Downloading the COT report.
    """

    @abstractmethod
    def download(self) -> pd.DataFrame:
        """
        :return: The downloaded COT report in a data frame.
        """
        ...

    @abstractmethod
    def store_locally(self, report: pd.DataFrame) -> None:
        """
        :param report: COT report as a data frame.
        :return: None
        """