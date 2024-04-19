from typing import List

from sqlalchemy import String, Text, ForeignKey, Table, Column, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class ProductCategoryAssociation(Base):
    __tablename__ = "product_category_association"
    __table_args__ = (
        UniqueConstraint(
                "product_id", 
                "category_id", 
                name="idx_product_category",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id", ondelete="CASCADE"))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id", ondelete="CASCADE"))