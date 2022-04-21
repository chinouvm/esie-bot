from pydantic import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    TESTSERVERID: int
    SERVERID: int
    JIMSERVERID: int
    GITHUB_TOKEN: str
    TENORKEY: str

    class Config:
        env_file = ".env"


settings = Settings()
