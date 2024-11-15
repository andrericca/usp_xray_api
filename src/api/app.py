from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import app_router
from core import logger
from core.settings import ENV_VARS

APP_TITLE = f"{ENV_VARS.app_name} - {ENV_VARS.xray_app_version}"
logger.info("Starting app | %s", APP_TITLE)

app = FastAPI(title=APP_TITLE)
app.include_router(app_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in ENV_VARS.backend_cors_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)