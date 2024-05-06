from sqlalchemy import select, delete, update
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from src.shop.models.cart import Cart
from src.shop.models.product import Product

from src.cart.schemas import (
    Create_Cart_model,
)

from src.database import async_session_maker


class CartRepository:

    @staticmethod
    async def add_cart_product(
        new_cart_model: Create_Cart_model,
    ) -> Cart:
        async with async_session_maker() as session:
            pass
    

    @staticmethod
    async def get_all_cart_procucts():
        pass


    @staticmethod
    async def edit_cart():
        pass


    @staticmethod
    async def delete_cart_products():
        pass