from sqlalchemy import select, delete, update
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from src.shop.models.product import Product
from src.shop.models.category import Category


from src.database import async_session_maker

from src.shop.schemas import (
    Create_category_model, 
    Create_product_model, 
    Edit_category_model, 
    Category_for_product,
    Edit_product_model,
)

class ProductRepository:

    @staticmethod
    async def create_product(
                            new_product_model:Create_product_model,
                            list_of_category:Category_for_product,
                            ) -> Product:
        async with async_session_maker() as session:
            product = Product(**new_product_model.model_dump())

            session.add(product)
            
            for n in range(len(list_of_category.list_of_id)):
                category = await session.scalar(
                    select(Category).
                    where(Category.id == list_of_category.list_of_id[n]).
                    options(selectinload(Category.products),),
                )

                category.products.append(product)

            await session.commit()

            return product
    
    @staticmethod
    async def get_all_products() -> list[Product]:
        async with async_session_maker() as session:
            query = (
                select(Product).
                options(
                    selectinload(Product.categories),
                )
            )

            products = await session.scalars(query)

            return list(products)
        
    @staticmethod
    async def get_product(product_id:int) -> Product:
        async with async_session_maker() as session:
            query = (
                select(Product).
                where(Product.id == product_id).
                options(
                    selectinload(Product.categories),
                )
            )

            product = await session.scalar(query)

            return product
        
    @staticmethod
    async def edit_product(product_id:int, product_model:Edit_product_model):
        async with async_session_maker() as session:
                
            stmt = (
                update(Product).
                where(Product.id == product_id).
                values(
                    product_model.model_dump(exclude_none=True)
                )
            )

            await session.execute(stmt)
            await session.commit()

            return {"status": "success"}
        
    @staticmethod
    async def delete_product(product_id:int):
        async with async_session_maker() as session:

            stmt = (
                delete(Product).
                where(Product.id == product_id)
            )

            await session.execute(stmt)
            await session.commit()
            
            return {"status": "success"}


class CategoryRepository:

    @staticmethod
    async def create_category(
        category:Create_category_model, 
    ) -> Category:
        async with async_session_maker() as session:
            stmt = category.model_dump()
            new_category = Category(**stmt)
            session.add(new_category)
            await session.commit()

            return new_category
    
    @staticmethod
    async def get_all_categories() -> list[Category]:
        async with async_session_maker() as session:
            query = (
                select(Category).
                order_by(Category.id)
            )

            categories = await session.scalars(query)

            return list(categories)
        
    @staticmethod
    async def get_category(category_id:int) -> Category:
        async with async_session_maker() as session:
            query = (
                select(Category).
                where(Category.id == category_id).
                options(selectinload(Category.products))
            )

            category = await session.scalar(query)

            return category
        
    @staticmethod
    async def get_category_with_products(category_id:int) -> Category:
        async with async_session_maker() as session:

            query = (
                select(Category).
                where(Category.id == category_id).
                options(selectinload(Category.products))
            ) 
            
            category = await session.scalar(query)

            await session.commit()

            return category

    @staticmethod
    async def edit_category(category_id:int, category_model:Edit_category_model):
        async with async_session_maker() as session:
            stmt = (
                update(Category).
                where(Category.id == category_id).
                values(**category_model.model_dump(exclude_none=True))
            )

            await session.execute(stmt)
            await session.commit()
            
            return {"status": "success"}
        
    @staticmethod
    async def delete_category(category_id:int):
        async with async_session_maker() as session:
            stmt = (
                delete(Category).
                where(Category.id == category_id)
            )
            await session.execute(stmt)
            await session.commit()

            return {"status": "success"}


class WishListRepository:

    @staticmethod
    async def add_product():
        pass