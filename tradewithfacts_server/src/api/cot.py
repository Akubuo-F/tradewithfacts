from typing import Any

from fastapi import Request, APIRouter
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address

from src.domain.entities.asset import ReportedAssets
from src.domain.entities.cot.cot_record import COTRecord
from src.domain.entities.cot.cot_report import COTReport
from src.domain.entities.cot.positions import Positions
from src.domain.entities.cot.trader_group import TraderGroup

cot = APIRouter()
limiter = Limiter(key_func=get_remote_address)


@cot.get("/")
@limiter.limit("5/day")
async def mock_report(request: Request):
    records: list[COTRecord] = [
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
        ),
        COTRecord(
            asset=ReportedAssets.aud,
            speculators=TraderGroup(
                Positions(
                    long=102509,
                    short=74830,
                    change_in_long=3458,
                    change_in_short=-4952
                )
            ),
            hedgers=TraderGroup(
                Positions(
                    long=51825,
                    short=9365,
                    change_in_long=-4577,
                    change_in_short=-1125
                )
            ),
            open_interest=186950,
            change_in_open_interest=-6339
        ),
        COTRecord(
            asset=ReportedAssets.ndx,
            speculators=TraderGroup(
                Positions(
                    long=48989,
                    short=46329,
                    change_in_long=146,
                    change_in_short=-1110
                )
            ),
            hedgers=TraderGroup(
                Positions(
                    long=149502,
                    short=162624,
                    change_in_long=1187,
                    change_in_short=1900
                )
            ),
            open_interest=245897,
            change_in_open_interest=4706
        )
    ]
    cot_report: COTReport = COTReport(as_of="2024-10-22", valid_till="2024-11-01", records=records)
    content: dict[str, Any] = {"message": cot_report.to_dict()}
    status_code: int = 200
    return JSONResponse(content, status_code)


if __name__ == '__main__':
    ...
