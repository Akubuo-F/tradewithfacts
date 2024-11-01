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

    @property
    def percentage_net(self) -> float:
        net: int = self.long - self.short
        return self._calculate_percentage(net, self.long, self.short)

    @property
    def percentage_change_in_net(self) -> float:
        percentage_change_in_long: float = self._calculate_percentage(self.change_in_long, self.long, -self.change_in_long)
        percentage_change_in_short: float = self._calculate_percentage(self.change_in_short, self.short, -self.change_in_short)
        return percentage_change_in_long - percentage_change_in_short

    @staticmethod
    def _calculate_percentage(value: int, long: int, short: int):
        """
        :param value: the value whose percentage should be calculated.
        :param long: number of long contracts.
        :param short: number of short contracts.
        :return: returns the percentage of the given value.
        """
        total: int = long + short
        return round((value / total) * 100, ndigits=1) if total != 0 else 0