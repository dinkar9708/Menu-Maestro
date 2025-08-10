import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = os.environ.get("DATABASE_URL", "YOUR_DATABASE_URL")
    secret_key: str = os.environ.get("SECRET_KEY", "your-secret-key")
    echo_sql: bool = os.environ.get("ECHO_SQL", "True") == "True"
    test: bool = os.environ.get("TEST", "False") == "True"
    project_name: str = os.environ.get("PROJECT_NAME", "My FastAPI project")
    log_level: str = os.environ.get("LOG_LEVEL", "DEBUG")
    model_config = SettingsConfigDict(case_sensitive=False, env_file_encoding='utf-8')
    

settings = Settings()  # type: ignore