from typing import Optional

from pydantic import BaseModel

class Create_Cart_model(BaseModel):

    quantity: int
    user_id: int 
    product_id: int

class Update_Cart_model(BaseModel):

    quantity: Optional[int] = None
    user_id: Optional[int] = None 
    product_id: Optional[int] = None