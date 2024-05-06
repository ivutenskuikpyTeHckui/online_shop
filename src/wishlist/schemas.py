from pydantic import BaseModel

class Create_Wishlist_model(BaseModel):

    user_id: int
    product_id: int