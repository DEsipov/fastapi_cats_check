from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Тренировка на кошках.'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'

    class Config:
        env_file = '.env'


settings = Settings()
