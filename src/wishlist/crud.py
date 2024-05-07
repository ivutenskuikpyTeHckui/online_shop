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
    async def get_wishlist(user_id:int) -> list[WishList]:
        async with async_session_maker() as session:
            query = (
                select(WishList).
                filter(WishList.user_id==user_id).
                options(joinedload(WishList.product)).
                order_by(WishList.id)
            )

            wishlist = await session.scalars(query)
            return list(wishlist)


    @staticmethod
    async def delete_product_from_wishlist(product_id:int, user_id:int):
        async with async_session_maker() as session:
            stmt = (
                delete(WishList).
                filter(WishList.product_id == product_id,
                       WishList.user_id == user_id)
            )

            await session.execute(stmt)
            await session.commit()

            return {"status": "success"}