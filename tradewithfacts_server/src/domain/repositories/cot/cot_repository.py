import time
from datetime import datetime, timedelta

import pandas as pd

from src.domain.entities.asset import Asset, ReportedAssets
from src.domain.entities.cot.cftc import CFTC
from src.domain.entities.cot.cot_record import COTRecord
from src.domain.entities.cot.cot_report import COTReport
from src.domain.repositories.cot.base.abstract_cot_report_downloader import AbstractCOTReportDownloader
from src.domain.repositories.cot.base.abstract_cot_repository import AbstractCOTRepository
from src.domain.repositories.cot.cot_report_downloader import COTReportDownloader
from src.util.dataframe_operator import DataFrameOperator
from src.util.helper import Helper
from src.util.logger import Logger


class COTRepository(AbstractCOTRepository):

    def __init__(self, storage_details: dict, cot_report_downloader: AbstractCOTReportDownloader):
        self._storage_details = storage_details
        self._cot_report_downloader = cot_report_downloader

    def fetch_latest_report(self, assets: list[Asset]) -> COTReport:
        data: pd.DataFrame = self._fetch(years_to_fetch=1)
        dataframe_operator: DataFrameOperator = DataFrameOperator(data)
        assets_market_and_contract_names: list[str] = list(map(lambda asset: CFTC.name_of(asset), assets))
        filtered_data = (
            dataframe_operator
            .keep_only_values("Market and Exchange Names", assets_market_and_contract_names)
            .keep_only_values(
                "As of Date in Form YYYY-MM-DD",
                [data["As of Date in Form YYYY-MM-DD"].iloc[0]]
            )
            .operate
        )
        return COTRepository._build_cot_report(filtered_data)


    @staticmethod
    def _build_cot_report(filtered_data: pd.DataFrame):
        cot_records: list[COTRecord] = [COTRecord.from_dict(row.to_dict()) for _, row in filtered_data.iterrows()]
        storage_details: dict = Helper.get_storage_details("cot_report")
        return COTReport(
            as_of=storage_details["as_of"],
            valid_till=storage_details["valid_till"],
            records=cot_records
        )

    def fetch_historical_report(self, asset: Asset, period) -> COTReport:
        data: pd.DataFrame = self._fetch(years_to_fetch=2)
        dataframe_operator = DataFrameOperator(data)
        filtered_data: pd.DataFrame = (
            dataframe_operator
            .keep_only_values("Market and Exchange Names", values_to_keep=[CFTC.name_of(asset)])
            .operate
        ).iloc[: period]
        return COTRepository._build_cot_report(filtered_data)

    def _fetch(self, years_to_fetch: int) -> pd.DataFrame:
        if self._is_report_outdated():
            Logger.log("Downloading latest COT report.")
            new_cot_reports: list[pd.DataFrame] = self._cot_report_downloader.download(years_to_fetch)
            for i in range(len(new_cot_reports)):
                report = pd.concat(new_cot_reports[: i + 1])
                self._cot_report_downloader.store_locally(self._storage_details, report, i + 1)
        return pd.read_csv(
            self._storage_details["storage"][f"{years_to_fetch}{"yr" if years_to_fetch == 1 else "yrs"}"],
            index_col=0
        )

    def _is_report_outdated(self) -> bool:
        released_as_of: datetime = datetime.strptime(self._storage_details["as_of"], "%Y-%m-%d")
        downloaded_date: datetime = released_as_of + timedelta(days=3)
        current_date: datetime = datetime.now()
        next_available_date: datetime = current_date + timedelta(days=(4 - current_date.weekday()) % 7)
        if next_available_date.date() - downloaded_date.date() > timedelta(days=14):
            return True
        if current_date.date() >= next_available_date.date():
            if current_date.time() >= datetime.strptime("15:30", "%H:%M").time() \
                    and released_as_of < downloaded_date + timedelta(days=4):
                return True
        return False


if __name__ == '__main__':
    repository = COTRepository(Helper.get_storage_details("cot_report"), COTReportDownloader())
    start = time.time()
    latest_report: COTReport = repository.fetch_latest_report(ReportedAssets.all)
    #print(latest_report.to_dict())
    #historical_report: COTReport = repository.fetch_historical_report(ReportedAssets.dji, 4)
    stop = time.time()
    print(f"time: {stop - start}")


