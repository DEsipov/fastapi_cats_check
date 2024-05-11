from typing import Optional

from fastapi import Path, Query, APIRouter

from app.core.const import Tag

router = APIRouter()


@router.get(
    '/example/{name}',
    tags=[Tag.COMMON],
    summary='Сложение',
    response_description='Возвращает сумму',
)
async def example(*,
                  name: str = Path(min_length=2, max_length=20),
                  num: Optional[int] = Query(title='Число', ge=1, le=10, alias='num')
                  ):
    """Сумма."""
    return [name, num]
