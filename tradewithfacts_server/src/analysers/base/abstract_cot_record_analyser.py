from abc import ABC, abstractmethod

from src.domain.entities.cot.cot_record import COTRecord
from src.domain.entities.reading import Reading


class AbstractCOTRecordAnalyser(ABC):
    """
    Analyses a single row in the COT report to provide insights into market sentiment, hedging activity, trends, and
    extremes.
    """

    def __init__(self, cot_record: COTRecord):
        """
        :param cot_record: The COT record to be analysed.
        """
        self._cot_record = cot_record

    @abstractmethod
    def analyse_current_sentiment(self) -> Reading:
        """
        :return: A reading indicating bullish, bearish, or neutral sentiment.
        """
        ...

    @abstractmethod
    def analyse_hedging_activity(self) -> Reading:
        """
        :return: A reading indicating bullish, bearish, or neutral hedging activity.
        """
        ...

    @abstractmethod
    def analyse_latest_sentiment_trend(self, historical_records: list[COTRecord]) -> Reading:
        """
        :param historical_records: A list of COT records representing historical data.
        :return: A reading indicating bullish, bearish, or neutral trend.
        """
        ...

    @abstractmethod
    def analyse_extremes(self) -> Reading:
        """
        :return: A reading indicating bullish, bearish, or neutral extremes.
        """
        ...
    
    def analyse_overall_score(self, historical_records: list[COTRecord]) -> float:
        """
        Analyses the overall sentiment and trend to provide a general score ranging from -100% (extremely bearish) to
        100% (extremely bullish).
        :param historical_records: A list of COT records representing historical data.
        :return: A value representing the overall sentiment score.
        """
        return sum([
            self.analyse_current_sentiment().value * 0.4,
            self.analyse_hedging_activity().value * 0.2,
            self.analyse_latest_sentiment_trend(historical_records).value * 0.3,
            self.analyse_extremes().value * 0.1
        ]) * 100