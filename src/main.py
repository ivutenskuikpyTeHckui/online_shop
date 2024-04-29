from fastapi import FastAPI
from fastapi_users import FastAPIUsers


from src.shop.router import router as router_shop


from src.auth.models import User
from src.auth.base_config import auth_backend
from src.auth.manager import get_user_manager

app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


# нужно добавить user_schema from schemas и посмотреть get_current_user в fastapi_users

# app.include_router(
#     fastapi_users.get_register_router(auth_backend),
#     prefix="/auth/register",
#     tags=["auth"],
# )

app.include_router(router_shop)

