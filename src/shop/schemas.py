from pydantic import BaseModel

class Create_category_model(BaseModel):
    
    name: str
    description: str

class Create_product_model(BaseModel):

    name: str
    designer: str
    size: str
    color: str
    price: float