from fastapi import APIRouter
from fastapi.responses import JSONResponse
from middlewares.jwt_manager import create_token
from models.user import User


user_router = APIRouter()


@user_router.post("/login", tags=["Auth"])
def login(user: User):
    if (user.email == "admin@gmail.com" and user.password == "123456"):
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)
    else:
        return JSONResponse(status_code=401, content={"message": "Credenciales inválidas, intente de nuevo"})
