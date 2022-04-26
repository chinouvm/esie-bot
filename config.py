from pydantic import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    DEVTOKEN: str
    GITTOKEN: str
    TENORKEY: str
    REDDIT_CLIENTID: str
    REDDIT_CLIENTSECRET: str
    REDDIT_USERAGENT: str
    APPID: int
    DEVID: int

    class Config:
        env_file = ".env"


settings = Settings()
