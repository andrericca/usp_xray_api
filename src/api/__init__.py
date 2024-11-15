from fastapi import APIRouter

from api.api_input import router as xay_input_router

app_router = APIRouter(prefix="/api")

app_router.include_router(xay_input_router, tags=["xray-input"])
