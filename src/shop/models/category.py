from typing import List, TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey, Table, Column, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

from src.shop.models.product_category_association import ProductCategoryAssociation

if TYPE_CHECKING:
    from src.shop.models.product import Product

class Category(Base):
    __tablename__ = "category"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text)
    products: Mapped[List["Product"]] = relationship(
        secondary=ProductCategoryAssociation.__tablename__, back_populates="categories"
    )