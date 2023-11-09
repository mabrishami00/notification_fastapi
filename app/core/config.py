from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    REDIS_URL = 'redis://localhost:6379/2'


settings = Settings()