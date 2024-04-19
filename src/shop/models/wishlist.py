from typing import List, TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey, Table, Column, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.auth.models import User
    from src.shop.models.product import Product

class WishList(Base):
    __tablename__ = "wishlist"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="wishlist")

    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    product: Mapped["Product"] = relationship(back_populates="wishlist")
