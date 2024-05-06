from sqlalchemy import select, delete, update
from sqlalchemy.orm import joinedload

from src.shop.models.cart import Cart

from src.cart.schemas import (
    Create_Cart_model,
    Update_Cart_model
)

from src.database import async_session_maker


class CartRepository:

    @staticmethod
    async def add_product_to_cart(
        user_id:int,
        new_cart_model: Create_Cart_model,
    ) -> Cart:
        async with async_session_maker() as session:
            
            cart_model = new_cart_model.model_dump()
            cart_model['user_id'] = user_id
            print(cart_model)
            new_cart_column = Cart(**cart_model)
            session.add(new_cart_column)
            await session.commit()
            
            return {"status":"success"}
    

    @staticmethod
    async def get_cart(user_id:int) -> list[Cart]:
        async with async_session_maker() as session:
            query = (
                select(Cart).
                where(user_id==user_id).
                options(joinedload(Cart.product))
            )

            columns = await session.scalars(query)
            
            return list(columns)


    @staticmethod
    async def edit_cart(user_id:int,
                        product_id:int,
                        update_model: Update_Cart_model,
                        ):
        async with async_session_maker() as session:
            stmt = (
                update(Cart).
                where(user_id==user_id).
                where(product_id==product_id).
                values(**update_model.model_dump(exclude_none=True))
            )

            await session.execute(stmt)
            await session.commit()

            return {"status": "success"}
        

    @staticmethod
    async def delete_product_from_cart(user_id:int, 
                                       product_id:int
                                       ):
        async with async_session_maker() as session:
            stmt = (
                delete(Cart).
                where(Cart.product_id==product_id, Cart.user_id==user_id)
            )
            print(stmt)
            await session.execute(stmt)
            await session.commit()

            return {"status": "success"}