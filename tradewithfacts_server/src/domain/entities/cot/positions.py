from typing import Final


class Positions:
    """
    Positions on an asset held by a group of traders.
    """

    def __init__(self, long: int, short: int, change_in_long, change_in_short):
        """
        :param long: Number of long contracts.
        :param short: Number of short contracts.
        :param change_in_long: Change in long contracts from the previous week.
        :param change_in_short: Change in short contracts from the previous week.
        """
        self.long: Final[int] = long
        self.short: Final[int] = short
        self.change_in_long: Final[int] = change_in_long
        self.change_in_short: Final[int] = change_in_short

    def to_dict(self) -> dict:
        return {
            "long": self.long,
            "short": self.short,
            "change_in_long": self.change_in_long,
            "change_in_short": self.change_in_short
        }