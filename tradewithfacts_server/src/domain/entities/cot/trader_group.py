from typing import Final

from src.domain.entities.cot.positions import Positions


class TraderGroup:
    """
    A group of traders that have positions on an asset reported in the COT report.
    """

    def __init__(self, positions: Positions):
        """
        :param positions: Positions help by this group of traders
        """
        self.positions: Final[Positions] = positions

    def to_dict(self) -> dict:
        return self.positions.to_dict()
