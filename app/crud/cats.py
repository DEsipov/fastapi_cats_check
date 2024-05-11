from sqlalchemy import select

from app.core.db import AsyncSessionLocal
from app.models import Cat
from app.schemas.cats import CatCreate


async def create_cat(
        new_cat: CatCreate,
        session: AsyncSessionLocal,
) -> Cat:
    # Конвертируем объект MeetingRoomCreate в словарь.
    new_cat_data = new_cat.dict()
    # Создаём объект модели Cat.
    db_cat = Cat(**new_cat_data)
    session.add(db_cat)
    session.commit()
    await session.commit()
    await session.refresh(db_cat)
    return db_cat


async def get_cats_db(session: AsyncSessionLocal):
    cats = await session.execute(select(Cat))
    return cats.scalars().all()
