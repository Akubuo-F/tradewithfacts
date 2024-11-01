from enum import Enum


class Reading(Enum):
    """
    Represents the state of the asset.
    """
    bearish = -1
    neutral = 0
    bullish = 1