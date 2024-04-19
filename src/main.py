from fastapi import FastAPI

from src.shop.router import router as router_shop

app = FastAPI()


app.include_router(router_shop)