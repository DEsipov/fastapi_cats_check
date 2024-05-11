from enum import Enum
from typing import Optional

from fastapi import FastAPI, Query, Path

from app.cats import router
from app.core import Tag

app = FastAPI()
app.include_router(router)




@app.get(
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
