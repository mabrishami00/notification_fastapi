from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REDIS_URL: str
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str

    class Config:
        env_file = "/home/mahdi/Documents/rss_project/notification_fastapi/.env"


settings = Settings()
