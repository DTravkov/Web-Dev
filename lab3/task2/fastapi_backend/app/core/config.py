from enum import StrEnum
from pydantic_settings import BaseSettings, SettingsConfigDict

#config... config never changes...
class Settings(BaseSettings):
    """ Application settings. Injected from env """

    PROJECT_NAME: str = "wp-bot"

    DEBUG: bool = False

    DATABASE_URL: str = "sqlite+aiosqlite:///../database/database.db"
    DATABASE_URL_TEST_SYNC: str = "../database/test_database.db"
    

    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8",
    )


settings = Settings()

        