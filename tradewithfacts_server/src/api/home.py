from fastapi import FastAPI
from fastapi.responses import JSONResponse


home_route = FastAPI()

@home_route.get("/")
async def root():
    content: dict[str, str] = {"message": "Welcome to TradeWithFacts"}
    status_code: int = 200
    return JSONResponse(content, status_code)