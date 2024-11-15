from typing import List

from pydantic_settings import BaseSettings


class EnvironmentVars(BaseSettings):
    app_name: str = "Xray APP"
    backend_cors_origins: List[str] = ["*"]

    host: str = "0.0.0.0"
    port: int = 5000

    xray_app_version: str = "0.1.0"

ENV_VARS = EnvironmentVars()