# ##########CATs###############
from typing import Optional, Any

from fastapi import APIRouter
from pydantic import BaseModel, Field, validator

from app.core import Tag, WRONG_CAT_NAME

router = APIRouter()


class Cat(BaseModel):
    """Собственно кот."""
    name: str = Field(max_length=20, title='Имя', description='Кота имя')
    age: Optional[int]
    is_grey: bool = True

    class Config:
        title = 'Класс Кота'

    @validator('name')
    def validate_name(cls, value: str):
        if value.lower() == WRONG_CAT_NAME.lower():
            raise ValueError(f'{WRONG_CAT_NAME} не кот!')
        return value


@router.post(
    '/cats',
    tags=[Tag.CAT_CRUD],
    summary='Создание кота',
    response_description='Возрат кота',
    status_code=201,
)
def cats(cat: Cat) -> dict[str, Any]:
    """Сумма."""
    return dict(cat)
