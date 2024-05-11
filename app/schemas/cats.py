from typing import Optional

from pydantic import BaseModel, Field, validator

from app.core.const import WRONG_CAT_NAME


class CatCreate(BaseModel):
    """Собственно кот."""
    name: str = Field(max_length=20, title='Имя', description='Кота имя')
    age: Optional[int]

    class Config:
        title = 'Класс Кота'

    @validator('name')
    def validate_name(cls, value: str):
        if value.lower() == WRONG_CAT_NAME.lower():
            raise ValueError(f'{WRONG_CAT_NAME} не кот!')
        return value
