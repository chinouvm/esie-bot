from pydantic import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    TESTSERVERID: int
    SERVERID: int
    GITHUB_TOKEN: str

    class Config:
        env_file = ".env"


settings = Settings()
