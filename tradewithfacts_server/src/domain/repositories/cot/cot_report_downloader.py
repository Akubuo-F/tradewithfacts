import asyncio
import time
from datetime import datetime, timedelta
from multiprocessing.managers import Value
from typing import Coroutine

import pandas as pd
from cot_reports import cot_reports as cot

from src.domain.repositories.cot.base.abstract_cot_report_downloader import AbstractCOTReportDownloader
from src.util.helper import Helper


class COTReportDownloader(AbstractCOTReportDownloader):

    @staticmethod
    async def _download_with_thread(year):
        return await asyncio.to_thread(
            cot.cot_year, year=year,
            cot_report_type="legacy_fut",
            store_txt=False,
            verbose=False
        )

    async def download(self, years_to_download: int) -> list[pd.DataFrame]:
        if years_to_download <= 0:
            raise ValueError("Years to download must be 1 or more.")
        current_year = datetime.now().year
        tasks: list[Coroutine] = [self._download_with_thread(current_year - i) for i in range(years_to_download)]
        return await asyncio.gather(*tasks)

    def store_locally(self, storage_details: dict, report: pd.DataFrame, years_count: int) -> None:
        """
        :param storage_details: details about the storage.
        :param report: COT report as a data frame.
        :param years_count: Years of report you are storing.
        :return: None
        """
        new_as_of: str = report["As of Date in Form YYYY-MM-DD"].iloc[0]
        valid_till: str = COTReportDownloader._get_expiration_date(datetime.strptime(new_as_of, "%Y-%m-%d"))
        storage_details["as_of"] = new_as_of
        storage_details["valid_till"] = valid_till
        years_count_as_string = f"{years_count}{"yr" if years_count == 1 else "yrs"}"
        storage_details["storage"][years_count_as_string] = \
            f"{Helper.get_storage("cot_report")}/{years_count_as_string}.csv"
        report.to_csv(storage_details["storage"][years_count_as_string])
        Helper.update_storage_details("cot_report", storage_details)

    @staticmethod
    def _get_expiration_date(as_of: datetime) -> str:
        expiry_date: datetime = as_of + timedelta(days=14 - 4)
        expiry_date = expiry_date.replace(hour=15, minute=30)
        return expiry_date.strftime("%Y-%m-%d %H:%M:%S")



if __name__ == '__main__':
    start_time = time.time()

    downloader = COTReportDownloader()
    reports = asyncio.run(downloader.download(2))
    for i in range(len(reports)):
        data = pd.concat(reports[: i + 1])
        downloader.store_locally(Helper.get_storage_details("cot_report"), data, i + 1)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")
