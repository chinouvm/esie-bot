from pydantic import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    GITTOKEN: str
    TENORKEY: str
    REDDIT_CLIENTID: str
    REDDIT_CLIENTSECRET: str
    REDDIT_USERAGENT: str

    class Config:
        env_file = ".env"


settings = Settings()
