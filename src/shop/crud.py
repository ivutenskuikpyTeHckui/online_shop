from fastapi import Depends

from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from src.shop.models.product import Product
from src.shop.models.category import Category


from src.database import async_session_maker, get_async_session

from src.shop.schemas import (Create_category_model, Create_product_model)

class ProductRepository:
    @staticmethod
    async def create_product(name:str,
                                designer:str,
                                size:str,
                                color:str,
                                price:float, 
                                session:AsyncSession,
                                ) -> Product:
        product = Product(
            name=name,
            designer=designer,
            size=size,
            color=color,
            price=price,
        )

        session.add(product)
        await session.commit()

        return product
    

class CategoryRepository:
    @staticmethod
    async def create_category(
        category:Create_category_model, 
    ) -> Category:
        async with async_session_maker() as session:
            data = category.model_dump()
            new_category = Category(**data)
            session.add(new_category)
            await session.commit()

            return new_category
    
    @staticmethod
    async def get_all_categories() -> list[Category]:
        async with async_session_maker() as session:
            query = (
                select(Category)
            ).order_by(Category.id)

            categories = await session.scalars(query)

            return list(categories)
        
    @staticmethod
    async def get_category() -> Category:
        async with async_session_maker() as session:
            query = (
                select(Category)
                .where()
            )


async def demo_m2m(session:AsyncSession):
    # return "hello"
    pants = await ProductRepository.create_product(
        name="штаны",
        designer="балантьяга",
        size="м",
        color="черный",
        price=4,
        session=session,
    )
    shoes = await ProductRepository.create_product(
        name="туфли",
        designer="балантьяга",
        size="42",
        color="черный",
        price=7,
        session=session,
    )
  
    category = await CategoryRepository.create_category("качество", "супер", session)

    category = await session.scalar(
        select(Category)
        .where(Category.id == category.id)
        .options(selectinload(Category.products),)
    )

    category.products.append(pants)
    category.products.append(shoes)

    await session.commit()

async def m2m():
    async with async_session_maker() as session:
        await demo_m2m(session)
    return "success"



# nw_ctgr = Create_category_model(name="fff", description="ffff")
# async def main():
#     async with async_session_maker as session:
#         await CategoryRepository.create_category(nw_ctgr, session)