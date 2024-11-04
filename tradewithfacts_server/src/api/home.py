from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

from src.api.cot import cot


home = FastAPI()
home.include_router(cot, prefix="/cot_report")

limiter = Limiter(key_func=get_remote_address)
# noinspection PyUnresolvedReferences
home.state.limiter = limiter

home.add_exception_handler(
    429,
    lambda request, exception: JSONResponse(
        content={"message": "Rate limit exceeded. Please try again later in 5 minutes."},
        status_code=429
    )
)

# noinspection PyTypeChecker
home.add_middleware(SlowAPIMiddleware)


@home.get("/")
@limiter.limit("5/minute")
async def root(request: Request):
    content: dict[str, str] = {"message": "Welcome to TradeWithFacts!"}
    status_code: int = 200
    return JSONResponse(content, status_code)


if __name__ == '__main__':
    ...