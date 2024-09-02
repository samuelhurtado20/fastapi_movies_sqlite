from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from db.database import Base, engine
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
# Para cambiar el nombre de la aplicacion
app.title = "Mi aplicacion con FastAPI"
# Para cambiar la version de la aplicacion
app.version = "0.0.1"
app.add_middleware(ErrorHandler)

app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)