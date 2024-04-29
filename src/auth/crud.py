from sqlalchemy import select, delete, update
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User


from src.database import async_session_maker
from src.auth.schemas import (
    UserCreate,
    UserRead,
    UserUpdate
)

class AuthRepository:

    @staticmethod
    async def create_user():
        pass