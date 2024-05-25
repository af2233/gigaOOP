from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import async_session_maker
from db.models.theme import Theme
from db.schemas.theme import ThemeCreate, ThemeUpdate, ThemeInDB

theme_router = APIRouter()


async def get_db() -> AsyncSession:
    async with async_session_maker() as session:
        yield session


@theme_router.post("/", response_model=ThemeInDB)
async def create_theme(theme: ThemeCreate, db: AsyncSession = Depends(get_db)):
    db_theme = Theme(**theme.dict())
    db.add(db_theme)
    await db.commit()
    await db.refresh(db_theme)
    return db_theme


@theme_router.get("/{theme_id}", response_model=ThemeInDB)
async def read_theme(theme_id: int, db: AsyncSession = Depends(get_db)):
    theme = await db.get(Theme, theme_id)
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    return theme
