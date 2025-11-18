from passlib.context import CryptContent
from jose import jwt, JWTError
from datetime import datetime, timedelta

pwt_context = CryptContext(schemas = ["bcrypt"], deprecated = "auto")
SECRET_KEY = "supersecretjwtkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password: str):
    return pwt_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict):
    to.encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

