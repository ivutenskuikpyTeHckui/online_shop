from typing import Annotated

from fastapi import APIRouter, Body, Query

from src.cart.crud import CartRepository
from src.cart.schemas import Create_Cart_model, Update_Cart_model

router = APIRouter(
    prefix="/Cart",
    tags= ["Cart"]
)


@router.post("/add_product_to_cart")
async def add_product_to_cart(user_id: Annotated[int, Body()], 
                              new_cart_model:Annotated[Create_Cart_model, Body()]
                              ):
    new_cart_model = await CartRepository.add_product_to_cart(user_id, new_cart_model)
    return new_cart_model


@router.get("/get_products_from_cart")
async def get_products_from_cart(user_id: Annotated[int, Query()]):
    products_from_cart = await CartRepository.get_cart(user_id)
    return products_from_cart


@router.patch("/edit_cart")
async def edit_cart(user_id: Annotated[int, Body()], 
                    product_id: Annotated[int, Body()],
                    update_model: Annotated[Update_Cart_model, Body()]
                    ):
    updated_model = await CartRepository.edit_cart(user_id, product_id, update_model)
    return updated_model


@router.delete("/delete_products_from_cart")
async def delete_products_from_cart(user_id: Annotated[int, Body()],
                                    product_id: Annotated[int, Body()]
                                    ):
    deleted_product = await CartRepository.delete_product_from_cart(user_id, product_id)
    return deleted_product