from typing import List, TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey, Table, Column, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

from src.shop.models.product_category_association import ProductCategoryAssociation

if TYPE_CHECKING:
    from src.shop.models.category import Category
    from src.shop.models.wishlist import WishList
    from src.shop.models.cart import Cart



class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    designer: Mapped[str]
    size: Mapped[str]
    color: Mapped[str]
    price: Mapped[float]
    
    categories: Mapped[List["Category"]] = relationship(
        secondary=ProductCategoryAssociation.__tablename__, back_populates="products"
    )

    wishlist: Mapped[List["WishList"]] = relationship(back_populates="product")

    cart: Mapped[List["Cart"]] = relationship(back_populates="product")
