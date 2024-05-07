from typing import Annotated

from fastapi import APIRouter, Body, Query

from src.wishlist.crud import WishListRepository
from src.wishlist.schemas import Create_Wishlist_model

router = APIRouter(
    prefix="/Wishlist",
    tags= ["Wishlist"]
)


@router.post("/add_product_to_wishlist")
async def add_product_to_wishlist(wishlist_model:Create_Wishlist_model):
    new_product_to_wishlist = await WishListRepository.add_product_to_wishlist(wishlist_model)
    return new_product_to_wishlist

@router.get("/get_wishlist")
async def get_wishlist(user_id:Annotated[int, Query()]):
    wishlist = await WishListRepository.get_wishlist(user_id)
    return wishlist

@router.delete("/delete_product_from_wishlist")
async def delete_product_from_wishlist(user_id:Annotated[int, Body()],
                                       product_id:Annotated[int, Body()]
                                       ):
    del_product = await WishListRepository.delete_product_from_wishlist(product_id, user_id)
    return del_product