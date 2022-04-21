from pydantic import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    GITHUB_TOKEN: str
    TENORKEY: str

    class Config:
        env_file = ".env"


settings = Settings()
