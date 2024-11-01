from src.analysers.base.abstract_cot_record_analyser import AbstractCOTRecordAnalyser
from src.domain.entities.cot.cot_record import COTRecord
from src.domain.entities.reading import Reading


class COTRecordAnalyser(AbstractCOTRecordAnalyser):

    def __init__(self, cot_record: COTRecord):
        """
        :param cot_record: The COT record to be analysed.
        """
        super().__init__(cot_record)

    def analyse_current_sentiment(self) -> Reading:
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

    def analyse_latest_sentiment_trend(self, historical_records: list[COTRecord]) -> Reading:
        """
        Analyses the latest sentiment trend of speculators' net positions over a specified period.
        :param historical_records: A list of COT records representing historical data.
        :return: A reading indicating bullish, bearish, or neutral trend.
        :raises ValueError: If the length of the historical_records is not equal to the required period.
        """
        period: int = 4
        if len(historical_records) != period:
            raise ValueError(f"Historical records should be of length 4 with recent record included.")
        recent_net_trend: int = sum(record.speculators.positions.percentage_net for record in historical_records)
        average_net: float = recent_net_trend / period
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
