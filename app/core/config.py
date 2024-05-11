from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Тренировка на кошках.'

    class Config:
        env_file = '.env'


settings = Settings()
