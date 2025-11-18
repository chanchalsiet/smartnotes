import os
from dotenv import load_dotenv
load_dotenv()

class Settings():
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "defaultsecret")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 20

settings = Settings()

# class Config:
#     SQLALCHEMY_DATABASE_URI = (
#         postgresql://chanchal:ramu123 @ localhost:5432/admin
#     )
#     # 'postgresql://chanchal:YOUR_PASSWORD@localhost:5432/admin'
#     SQLALCHEMY_TRACK_MODIFICATIONs = False
#     SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")