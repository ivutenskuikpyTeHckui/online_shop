from sqlalchemy import select, delete
from sqlalchemy.orm import joinedload

from src.shop.models.wishlist import WishList

from src.wishlist.schemas import (
    Create_Wishlist_model,
)

from src.database import async_session_maker

class WishListRepository:

    @staticmethod
    async def add_product_to_wishlist(new_wishlist_model:Create_Wishlist_model):
        async with async_session_maker() as session:
            wishlist = WishList(**new_wishlist_model.model_dump())

            session.add(wishlist)
            await session.commit()

            return wishlist

    @staticmethod
    async def get_wishlist():
        pass


    @staticmethod
    async def delete_product_from_wishlist():
        pass