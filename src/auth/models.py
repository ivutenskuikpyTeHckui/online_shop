from datetime import datetime
from typing import List, TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTable

from sqlalchemy import String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.shop.models.wishlist import WishList
    from src.shop.models.cart import Cart

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    username: Mapped[str] = mapped_column(nullable=True)
    registered_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=True)
    is_active: Mapped[bool] = mapped_column( default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)
    
    wishlist: Mapped[List["WishList"]] = relationship(back_populates="user")

    cart: Mapped[List["Cart"]] = relationship(back_populates="user")

