from fastapi import UploadFile, File, Depends, HTTPException, status

from fastapi_users import fastapi_users, FastAPIUsers

from src.auth.manager import get_user_manager

from src.auth.base_config import auth_backend

from src.auth.models import User

from src.auth.schemas import UserRead


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
current_superuser = fastapi_users.current_user(superuser=True)




