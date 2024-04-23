from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from src.shop.crud import ProductRepository, CategoryRepository
from src.shop.schemas import Create_product_model, Create_category_model, Edit_category_model

from src.database import get_async_session, async_session_maker

router = APIRouter(
    prefix="/Shop",
    tags= ["Shop"]
)

@router.post("/add_category")
async def add_category(new_category_model:Create_category_model):
    new_category = await CategoryRepository.create_category(new_category_model)
    return {"id": new_category.id}

@router.get("/get_all_categories")
async def get_all_categories():
    all_categories = await CategoryRepository.get_all_categories()
    return all_categories

@router.get("/get_category/{category_id}")
async def get_category(category_id:int):
    category = await CategoryRepository.get_category(category_id)
    return category

@router.patch("/edit_category/{category_id}")
async def edit_category(category_id:int, edit_category_model:Edit_category_model):
    edit_category = await CategoryRepository.edit_category(category_id, edit_category_model)
    return edit_category