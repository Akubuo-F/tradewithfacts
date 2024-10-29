from typing import Final

from src.domain.entities.asset import Asset
from src.domain.entities.cot.trader_group import TraderGroup


class COTRecord:
    """
    A single row in the COT report. It provides detailed information about the positions held by different types of
    traders for a specific asset.
    """

    def __init__(
            self,
            asset: Asset,
            speculators: TraderGroup,
            hedgers: TraderGroup,
            open_interest: int,
            change_in_open_interest: int
    ):
        """
        :param asset: A Futures contract reported in the COT report.
        :param speculators:  A group of traders that have positions on an asset reported in the COT report.
        :param hedgers: A group of traders that have positions on an asset reported in the COT report
        :param open_interest: Number of contracts that are still active.
        :param change_in_open_interest: Change in open interest from the previous week.
        """
        self.asset: Final[Asset] = asset
        self.speculators: Final[TraderGroup] = speculators
        self.hedgers: Final[TraderGroup] = hedgers
        self.open_interest: Final[int] = open_interest
        self.change_in_open_interest: Final[int] = change_in_open_interest

    def to_dict(self) -> dict:
        return {
            "asset": self.asset.to_dict(),
            "speculators": self.speculators.to_dict(),
            "hedgers": self.hedgers.to_dict(),
            "open_interest": self.open_interest,
            "change_in_open_interest": self.change_in_open_interest
        }