from typing import Optional

from pydantic import BaseModel


class Create_category_model(BaseModel):
    
    name: str
    description: str

class Edit_category_model(BaseModel):

    name: Optional[str] = None
    description: Optional[str] = None

class Create_product_model(BaseModel):

    name: str
    designer: str
    size: str
    color: str
    price: float