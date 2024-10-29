from dataclasses import dataclass, Field
from enum import Enum
from typing import Final


class AssetType(Enum):
    """
    Represents the types of assets reported in the COT report.
    """
    commodity = "COMMODITY"
    currency = "CURRENCY"
    crypto_currency = "CRYPTOCURRENCY"
    index = "INDEX"


class Asset:
    """
    A Futures contract reported in the COT report. This could be anything from commodities like gold or oil to financial
    instruments like currencies or stock indices, detailing the positions held by different types of traders.
    """

    def __init__(self, code: str, name: str, asset_type: AssetType):
        """
        :param code: The code of the asset, e.g. XAU.
        :param name: The name of the asset, e.g. GOLD.
        :param asset_type: The type of the asset, e.g. COMMODITY.
        """
        self.code: Final[str] = code
        self.name: Final[str] = name
        self.asset_type: Final[AssetType] = asset_type

    def to_dict(self) -> dict:
        return {
            "code": self.code,
            "name": self.name,
            "asset_type": self.asset_type
        }

    @property
    def code(self) -> str:
        return self.code

    def __eq__(self, other: "Asset") -> bool:
        return self.code == other.code


class ReportedAssets:
    """
    Collection of predefined assets.
    """
    aud: Final[Asset] = Asset(code="AUD", name="AUSTRALIAN DOLLAR", asset_type=AssetType.currency)
    gbp: Final[Asset] = Asset(code="GBP", name="BRITISH POUND", asset_type=AssetType.currency)
    cad: Final[Asset] = Asset(code="CAD", name="CANADIAN DOLLAR", asset_type=AssetType.currency)
    eur: Final[Asset] = Asset(code="EUR", name="EURO", asset_type=AssetType.currency)
    jpy: Final[Asset] = Asset(code="JPY", name="JAPANESE YEN", asset_type=AssetType.currency)
    chf: Final[Asset] = Asset(code="CHF", name="SWISS FRANC", asset_type=AssetType.currency)
    usd: Final[Asset] = Asset(code="USD", name="U.S. DOLLAR", asset_type=AssetType.currency)
    nzd: Final[Asset] = Asset(code="NZD", name="NEW ZEALAND DOLLAR", asset_type=AssetType.currency)
    currencies: Final[list[Asset]] = [aud, gbp, cad, eur, jpy, chf, usd, nzd]
    btc: Final[Asset] = Asset(code="BTC", name="BITCOIN", asset_type=AssetType.crypto_currency)
    crypto_currencies: Final[list[Asset]] = [btc]
    spx: Final[Asset] = Asset(code="SPX", name="S&P 500", asset_type=AssetType.index)
    ndx: Final[Asset] = Asset(code="NDX", name="NASDAQ-100", asset_type=AssetType.index)
    dji: Final[Asset] = Asset(code="DJI", name="DOW JONES", asset_type=AssetType.index)
    rty: Final[Asset] = Asset(code="RTY", name="RUSSELL 2000", asset_type=AssetType.index)
    tnx: Final[Asset] = Asset(code="TNX", name="10-YEAR U.S. TREASURY NOTES", asset_type=AssetType.index)
    indices: Final[list[Asset]] = [spx, ndx, dji, rty, tnx]
    wti: Final[Asset] = Asset(code="WTI", name="CRUDE OIL", asset_type=AssetType.commodity)
    xau: Final[Asset] = Asset(code="XAU", name="GOLD", asset_type=AssetType.commodity)
    xag: Final[Asset] = Asset(code="XAG", name="SILVER", asset_type=AssetType.commodity)
    xcu: Final[Asset] = Asset(code="XCU", name="COPPER", asset_type=AssetType.commodity)
    xpt: Final[Asset] = Asset(code="XPT", name="PLATINUM", asset_type=AssetType.commodity)
    commodities: Final[list[Asset]] = [wti, xau, xag, xcu, xpt]
    all: Final[list[Asset]] = currencies + crypto_currencies + indices + commodities
