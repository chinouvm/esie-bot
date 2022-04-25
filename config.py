from pydantic import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    GITTOKEN: str
    TENORKEY: str

    class Config:
        env_file = ".env"


settings = Settings()
