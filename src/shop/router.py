from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from src.shop.crud import ProductRepository, CategoryRepository
from src.shop.schemas import Create_product_model, Create_category_model
from src.database import get_async_session, async_session_maker

router = APIRouter(
    prefix="/Shop",
    tags= ["Shop"]
)

# @router.post("/add_product")
# async def add_product(new_product_model:Create_product_model, session:AsyncSession = Depends(get_async_session)):
#     new_product = await ProductRepository.create_product(session, **new_product_model.model_dump())
#     return new_product


# @router.get("/get_product")
# async def get_product(product_id:int, session:AsyncSession = Depends(get_async_session)):
    # query = selec

@router.post("/add_category")
async def add_category(new_category_model:Create_category_model):
    new_category = await CategoryRepository.create_category(new_category_model)
    return {"id": new_category.id}

@router.get("/get_all_categories")
async def get_all_categories():
    all_categories = await CategoryRepository.get_all_categories()
    return all_categories

