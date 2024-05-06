from typing import Annotated

from fastapi import APIRouter, Body, Query

from src.cart.schemas import Create_Cart_model, Update_Cart_model

router = APIRouter(
    prefix="/Cart",
    tags= ["Cart"]
)


@router.post("/add_product_to_cart")
async def add_product_to_cart(user_id: Annotated[int, Body()], 
                              new_cart_model:Annotated[Create_Cart_model, Body()]
                              ):
    pass


@router.get("/get_products_from_cart")
async def get_products_from_cart(user_id: Annotated[int, Body()]):
    pass


@router.patch("/edit_cart")
async def edit_cart(user_id: Annotated[int, Body()], 
                    update_model: Annotated[Update_Cart_model, Body()]
                    ):
    pass


@router.delete("/delete_products_from_cart")
async def delete_products_from_cart(user_id: Annotated[int, Query()]):
    pass