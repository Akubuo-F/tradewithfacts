from typing import Final

from src.domain.entities.asset import Asset, ReportedAssets


class CFTC:
    """
    The Commodity Futures Trading Commission (CFTC) is a U.S. government agency responsible for regulating the
    derivative markets, which include futures and options.
    """

    MARKET_AND_EXCHANGE_NAMES: Final[dict[Asset, str]] = {
        ReportedAssets.aud: "AUSTRALIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE",
        ReportedAssets.gbp: "BRITISH POUND - CHICAGO MERCANTILE EXCHANGE",
        ReportedAssets.cad: "CANADIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE",
        ReportedAssets.eur: "EURO FX - CHICAGO MERCANTILE EXCHANGE",
        ReportedAssets.jpy: "JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE",
        ReportedAssets.chf: "SWISS FRANC - CHICAGO MERCANTILE EXCHANGE",
        ReportedAssets.usd: "USD INDEX - ICE FUTURES U.S.",
        ReportedAssets.nzd: "NZ DOLLAR - CHICAGO MERCANTILE EXCHANGE",
        ReportedAssets.btc: "BITCOIN - CHICAGO MERCANTILE EXCHANGE",
        ReportedAssets.spx: "S&P 500 Consolidated - CHICAGO MERCANTILE EXCHANGE",
        ReportedAssets.ndx: "NASDAQ MINI - CHICAGO MERCANTILE EXCHANGE",
        ReportedAssets.dji: "DJIA x $5 - CHICAGO BOARD OF TRADE",
        ReportedAssets.rty: "RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE",
        ReportedAssets.tnx: "UST 10Y NOTE - CHICAGO BOARD OF TRADE",
        ReportedAssets.wti: "WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE",
        ReportedAssets.xau: "GOLD - COMMODITY EXCHANGE INC.",
        ReportedAssets.xag: "SILVER - COMMODITY EXCHANGE INC.",
        ReportedAssets.xcu: "COPPER- #1 - COMMODITY EXCHANGE INC.",
        ReportedAssets.xpt: "PLATINUM - NEW YORK MERCANTILE EXCHANGE",
    }

    @staticmethod
    def name_of(asset: Asset) -> str:
        """
        :param asset: The asset whose contract name to return.
        :return: The asset contract and market name.
        """
        if asset not in CFTC.MARKET_AND_EXCHANGE_NAMES:
            raise ValueError(f"No market and exchange name is associated with asset: {asset.name}.")
        return CFTC.MARKET_AND_EXCHANGE_NAMES[asset]

    @staticmethod
    def asset_of(asset_market_and_exchange_name: str) -> Asset:
        for key, value in CFTC.MARKET_AND_EXCHANGE_NAMES.items():
            if value == asset_market_and_exchange_name:
                return key
