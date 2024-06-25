# ##########CATs###############
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.const import Tag
from app.core.db import get_async_session
from app.crud.cats import create_cat, get_cats_db
from app.schemas.cats import CatCreate

router = APIRouter()


@router.post(
    '/cats/',
    tags=[Tag.CAT_CRUD],
    summary='Создание кота',
    response_description='Возрат кота',
    status_code=201,
)
async def cats(
        cat: CatCreate,
        session: AsyncSession = Depends(get_async_session)
):
    """Сумма."""
    new_cat = await create_cat(cat, session)
    return new_cat


@router.get(
    '/cats/',
    response_model=list[CatCreate],
)
async def get_cats(
        session: AsyncSession = Depends(get_async_session),
):
    """Список котов и кошек."""
    all_cats = await get_cats_db(session)
    return all_cats
