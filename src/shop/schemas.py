from typing import Optional

from pydantic import BaseModel

class Create_product_model(BaseModel):

    name: str
    designer: str
    size: str
    color: str
    price: float

class Edit_product_model(BaseModel):

    name: Optional[str] = None
    designer: Optional[str] = None
    size: Optional[str] = None
    color: Optional[str] = None
    price: Optional[float] = None

class Category_for_product(BaseModel):

    list_of_id: list[int]

#CATEGORY ++++++++++++++++++++++++++++++++++

class Create_category_model(BaseModel):
    
    name: str
    description: str

class Edit_category_model(BaseModel):

    name: Optional[str] = None
    description: Optional[str] = None


# CART +++++++++++++++++++++++++++++++++

class Create_cart_product(BaseModel):

    quantity: int
    user_id: int
    product_id: int
