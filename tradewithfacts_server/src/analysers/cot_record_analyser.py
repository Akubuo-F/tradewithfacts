from src.analysers.base.abstract_cot_record_analyser import AbstractCOTRecordAnalyser
from src.domain.entities.asset import ReportedAssets
from src.domain.entities.cot.cot_record import COTRecord
from src.domain.entities.reading import Reading
from src.domain.repositories.cot.cot_report_downloader import COTReportDownloader
from src.domain.repositories.cot.cot_repository import COTRepository
from src.util.helper import Helper


class COTRecordAnalyser(AbstractCOTRecordAnalyser):

    def __init__(self, cot_record: COTRecord | None = None):
        """
        :param cot_record: The COT record to be analysed.
        """
        super().__init__(cot_record)

    def analyse_changes_in_sentiment(self) -> Reading:
        """
        Analyses the current sentiment of speculators based on the percentage change in their net positions.
        :return: A reading indicating bullish, bearish, or neutral sentiment.
        """
        speculators_percentage_change_in_net: float = self._cot_record.speculators.positions.percentage_change_in_net
        if speculators_percentage_change_in_net > 0:
            return Reading.bullish
        elif speculators_percentage_change_in_net < 0:
            return Reading.bearish
        return Reading.neutral

    def analyse_hedging_activity(self) -> Reading:
        """
        Analyses the hedging activity of hedgers based on the percentage change in their net positions.
        :return: A reading indicating bullish, bearish, or neutral hedging activity.
        """
        hedgers_percentage_change_in_net: float = self._cot_record.hedgers.positions.percentage_change_in_net
        if hedgers_percentage_change_in_net > 0:
            return Reading.bullish
        elif hedgers_percentage_change_in_net < 0:
            return Reading.bearish
        return Reading.neutral

    def analyse_sentiment_trend(self, historical_records: list[COTRecord]) -> Reading:
        """
        Analyses the latest sentiment trend of speculators' net positions over a specified period.
        :param historical_records: A list of COT records representing historical data.
        :return: A reading indicating bullish, bearish, or neutral trend.
        """
        recent_net_trend: int = sum(record.speculators.positions.percentage_net for record in historical_records)
        average_net: float = recent_net_trend / len(historical_records)
        if average_net > recent_net_trend:
            return Reading.bullish
        elif average_net < recent_net_trend:
            return Reading.bearish
        return Reading.neutral

    def analyse_extremes(self) -> Reading:
        """
        Analyses extreme sentiment based on the percentage net positions of speculators and hedgers.
        :return: A reading indicating bullish, bearish, or neutral extremes.
        """
        threshold: float = 30.0
        speculators_percentage_net: float = self._cot_record.speculators.positions.percentage_net
        hedgers_percentage_net: float = self._cot_record.hedgers.positions.percentage_net
        if speculators_percentage_net > threshold and hedgers_percentage_net < -threshold:
            return Reading.bearish
        elif speculators_percentage_net < -threshold and hedgers_percentage_net > threshold:
            return Reading.bullish
        return Reading.neutral


if __name__ == '__main__':
    analyser = COTRecordAnalyser()
    cot_repository = COTRepository(Helper.get_storage_details("cot_report"), COTReportDownloader())
    latest_cot_report = cot_repository.fetch_latest_report(ReportedAssets.all)
    print(f"Latest COT Report AS OF: {latest_cot_report.as_of}\n")
    for record in latest_cot_report.records:
        analyser.set_record_to_analyse(record)
        historical_reports = cot_repository.fetch_historical_report(record.asset, 4)
        overall_score: int = analyser.analyse_overall_score(historical_reports.records)
        speculators = record.speculators
        hedgers = record.hedgers
        print(f"{record.asset.name} {record.asset.asset_type.value}")
        print(f"changes_in_sentiment = {analyser.analyse_changes_in_sentiment().name}")
        print(f"Hedging activity = {analyser.analyse_hedging_activity().name}")
        print(f"Sentiment_trend = {analyser.analyse_sentiment_trend(historical_reports.records).name}")
        print(f"Extremes = {analyser.analyse_extremes().name}")
        print(f"Overall score = {overall_score}% {"Bullish" if overall_score > 0 else "Bearish"}")
        print(f"Speculators = {speculators.to_dict()}, net = {speculators.positions.percentage_net}%, net_change = {speculators.positions.percentage_change_in_net}%")
        print(f"Hedgers = {hedgers.to_dict()}, net = {hedgers.positions.percentage_net}%, net_change = {hedgers.positions.percentage_change_in_net}%")
        print("\n")
