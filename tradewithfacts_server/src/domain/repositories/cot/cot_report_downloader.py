import asyncio
import time
from datetime import datetime
from typing import Coroutine

import pandas as pd
from cot_reports import cot_reports as cot

from src.domain.repositories.cot.base.abstract_cot_report_downloader import AbstractCOTReportDownloader
from src.util.helper import Helper


class COTReportDownloader(AbstractCOTReportDownloader):

    def __init__(self, local_csv_storage: str, historical_years: int = 2):
        """
        :param local_csv_storage: local csv file to store the COT report.
        :param historical_years: Downloads historical years worth of COT reports.
        """
        self._local_csv_storage = local_csv_storage
        self._historical_years = historical_years

    @staticmethod
    async def _download_with_thread(year):
        return await asyncio.to_thread(cot.cot_year, year=year, cot_report_type="legacy_fut", store_txt=False, verbose=False)

    async def download(self) -> pd.DataFrame:
        current_year = datetime.now().year
        tasks: list[Coroutine] = [self._download_with_thread(current_year - i) for i in range(self._historical_years)]
        reports = await asyncio.gather(*tasks)
        return pd.concat(reports)

    def store_locally(self, report: pd.DataFrame) -> None:
        report.to_csv(self._local_csv_storage)


if __name__ == '__main__':
    start_time = time.time()

    downloader = COTReportDownloader(Helper.get_storage("10yr_cot_report.csv"))
    data = asyncio.run(downloader.download())
    downloader.store_locally(data)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")