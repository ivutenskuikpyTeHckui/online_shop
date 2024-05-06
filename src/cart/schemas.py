from typing import Optional

from pydantic import BaseModel

class Create_Cart_model(BaseModel):

    quantity: int
    product_id: int

class Update_Cart_model(BaseModel):

    quantity: Optional[int] = None
