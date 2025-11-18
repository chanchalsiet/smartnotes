from fastapi import FastAPI
from fastapi_service.routers import users
from fastapi_jwt_auth import AuthJWT

app = FastAPI()

@AuthJWT.load_config
def get_config():
    from pydantic import BaseModel
    class Settings(BaseModel):
        authjwt_secret_key: str = "supersecretkey"
    return Settings()

app.include_router(users.router)
