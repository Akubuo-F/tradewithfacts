import unittest

from src.analysers.base.abstract_cot_record_analyser import AbstractCOTRecordAnalyser
from src.analysers.cot_record_analyser import COTRecordAnalyser
from src.domain.entities.asset import ReportedAssets
from src.domain.entities.cot.cot_record import COTRecord
from src.domain.entities.cot.positions import Positions
from src.domain.entities.cot.trader_group import TraderGroup
from src.domain.entities.reading import Reading


class TestAbstractCOTRecordAnalyser(unittest.TestCase):

    def setUp(self):
        self.mock_record: COTRecord = COTRecord(
            asset=ReportedAssets.xpt,
            speculators=TraderGroup(
                Positions(
                    long=53816,
                    short=18940,
                    change_in_long=7293,
                    change_in_short=804
                )
            ),
            hedgers=TraderGroup(
                Positions(
                    long=13877,
                    short=54612,
                    change_in_long=-294,
                    change_in_short=5902
                )
            ),
            open_interest=81497,
            change_in_open_interest=8530
        )
        self.cot_record_analyser: AbstractCOTRecordAnalyser = COTRecordAnalyser(self.mock_record)
        self.mock_historical_record: list[COTRecord] = [
            COTRecord(
                asset=ReportedAssets.xpt,
                speculators=TraderGroup(
                    Positions(
                        long=46316,
                        short=18184,
                        change_in_long=213,
                        change_in_short=-3518
                    )
                ),
                hedgers=TraderGroup(
                    Positions(
                        long=13680,
                        short=47398,
                        change_in_long=-2035,
                        change_in_short=2143
                    )
                ),
                open_interest=72633,
                change_in_open_interest=-2535
            ),
            COTRecord(
                asset=ReportedAssets.xpt,
                speculators=TraderGroup(
                    Positions(
                        long=46339,
                        short=22582,
                        change_in_long=23,
                        change_in_short=4498
                    )
                ),
                hedgers=TraderGroup(
                    Positions(
                        long=15424,
                        short=46433,
                        change_in_long=1744,
                        change_in_short=-965
                    )
                ),
                open_interest=4346,
                change_in_open_interest=-71
            ),
            COTRecord(
                asset=ReportedAssets.xpt,
                speculators=TraderGroup(
                    Positions(
                        long=46523,
                        short=18136,
                        change_in_long=184,
                        change_in_short=-4546
                    )
                ),
                hedgers=TraderGroup(
                    Positions(
                        long=14171,
                        short=64112,
                        change_in_long=-1253,
                        change_in_short=2277
                    )
                ),
                open_interest=72967,
                change_in_open_interest=-4012
            ),
            COTRecord(
                asset=ReportedAssets.xpt,
                speculators=TraderGroup(
                    Positions(
                        long=53816,
                        short=18940,
                        change_in_long=7293,
                        change_in_short=804
                    )
                ),
                hedgers=TraderGroup(
                    Positions(
                        long=13877,
                        short=54612,
                        change_in_long=-294,
                        change_in_short=5902
                    )
                ),
                open_interest=81497,
                change_in_open_interest=8530
            )
        ]

    def test_analyse_current_sentiment(self):
        current_sentiment: Reading = self.cot_record_analyser.analyse_current_sentiment()
        print(f"Current sentiment = {current_sentiment.name}")

    def test_analyse_hedging_activity(self):
        hedging_activity: Reading = self.cot_record_analyser.analyse_hedging_activity()
        print(f"Hedging activity = {hedging_activity.name}")

    def test_analyse_latest_sentiment_trend(self):
        latest_sentiment_trend: Reading = self.cot_record_analyser.analyse_latest_sentiment_trend(self.mock_historical_record)
        print(f"Latest sentiment trend = {latest_sentiment_trend.name}")

    def test_analyse_extremes(self):
        extremes: Reading = self.cot_record_analyser.analyse_extremes()
        print(f"Extremes = {extremes.name}")


if __name__ == '__main__':
    unittest.main()