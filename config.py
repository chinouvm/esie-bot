from pydantic import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    TESTSERVERID: int
    SERVERID: int

    class Config:
        env_file = ".env"


settings = Settings()
