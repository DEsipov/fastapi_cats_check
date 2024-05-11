from fastapi import FastAPI

from app.api.cats import router as cat_router
from app.api.other_views import router as other_router
from app.core.config import settings


app = FastAPI(title=settings.app_title)
app.include_router(cat_router)
app.include_router(other_router)
