from typing import Final


class CFTC:
    """
    The Commodity Futures Trading Commission (CFTC) is a U.S. government agency responsible for regulating the
    derivative markets, which include futures and options.
    """

    MARKET_AND_EXCHANGE_NAMES: Final[dict[str, str]] = {
        "AUD": "AUSTRALIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE",
        "GBP": "BRITISH POUND - CHICAGO MERCANTILE EXCHANGE",
        "CAD": "CANADIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE",
        "EUR": "EURO FX - CHICAGO MERCANTILE EXCHANGE",
        "JPY": "JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE",
        "CHF": "SWISS FRANC - CHICAGO MERCANTILE EXCHANGE",
        "USD": "USD INDEX - ICE FUTURES U.S.",
        "NZD": "NZ DOLLAR - CHICAGO MERCANTILE EXCHANGE",
        "BTC": "BITCOIN - CHICAGO MERCANTILE  EXCHANGE",
        "SPX": "S&P 500 CONSOLIDATED - CHICAGO MERCANTILE EXCHANGE",
        "NDX": "NASDAQ MINI - CHICAGO MERCANTILE EXCHANGE",
        "DJI": "DJIA x $5 - CHICAGO BOARD OF TRADE",
        "RTY": "RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE",
        "TNX": "UST 10Y NOTE - CHICAGO BOARD OF TRADE",
        "WTI": "WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE",
        "XAU": "GOLD - COMMODITY EXCHANGE INC.",
        "XAG": "SILVER - COMMODITY EXCHANGE INC.",
        "XCU": "COPPER- #1 - COMMODITY EXCHANGE INC.",
        "XPT": "PLATINUM - NEW YORK MERCANTILE EXCHANGE",
    }

    @staticmethod
    def name_of(asset_code: str) -> str:
        """
        :param asset_code: The code of the asset.
        :return: The asset contract and market name.
        """
        if asset_code not in CFTC.MARKET_AND_EXCHANGE_NAMES:
            raise ValueError(f"No market and exchange name is associated with asset_code: {asset_code}.")
        return CFTC.MARKET_AND_EXCHANGE_NAMES[asset_code]
