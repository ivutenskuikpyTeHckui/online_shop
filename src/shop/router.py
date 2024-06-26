from typing import Annotated

from fastapi import APIRouter, Body, Query

from src.shop.crud import ProductRepository, CategoryRepository
from src.shop.schemas import (
    Create_product_model, 
    Create_category_model, 
    Edit_category_model, 
    Category_for_product, 
    Edit_product_model,
    Create_cart_product,
)


router = APIRouter(
    prefix="/Product_Category",
    tags= ["Product_Category"]
)

@router.post("/add_category")
async def add_category(new_category_model:Annotated[Create_category_model, Body()]):
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


@router.get("/get_category_with_products/{category_id}")
async def get_category(category_id:int):
    category = await CategoryRepository.get_category_with_products(category_id)
    return category


@router.patch("/edit_category/{category_id}")
async def edit_category(category_id:int, edit_category_model:Annotated[Edit_category_model, Body()]):
    edit_category = await CategoryRepository.edit_category(category_id, edit_category_model)
    return edit_category


@router.delete("/detele_category")
async def delete_category(category_id:Annotated[int, Query()]):
    del_category = await CategoryRepository.delete_category(category_id)
    return del_category

#РОУТЕРЫ ПРОДУКТОВ ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@router.post("/add_product")
async def add_product(new_product_model:Annotated[Create_product_model, Body()], list_of_category:Annotated[Category_for_product, Body()]):
    new_product = await ProductRepository.create_product(new_product_model, list_of_category)
    return new_product


@router.get("/get_all_products")
async def get_all_products():
    all_products = await ProductRepository.get_all_products()
    return all_products


@router.get("/get_product/{product_id}")
async def get_product(product_id:int):
    product = await ProductRepository.get_product(product_id)
    return product


@router.patch("/edit_product/{product_id}")
async def edit_product(product_id:int, edit_product_model:Edit_product_model):
    edit_product = await ProductRepository.edit_product(product_id, edit_product_model)
    return edit_product


@router.delete("/delete_product")
async def delete_product(product_id:int):
    delete_product = await ProductRepository.delete_product(product_id)
    return delete_product


#РОУТЕРЫ КОРЗИНЫ ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@router.post("/add_cart_product")
async def add_cart_product(cart_product_model:Create_cart_product):
    pass