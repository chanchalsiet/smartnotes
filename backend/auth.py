import logging
from fastapi import HTTPException, Header, Request, Response
from jose import jwt, JWTError
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES
import pdb
logging.getLogger().setLevel(logging.INFO)
logging.error(SECRET_KEY)

TOKEN_BLACKLIST = set()


def hash_password(password):
    return generate_password_hash(password)


def verify_password(hashed, plain):
    return check_password_hash(hashed, plain)


def create_access_token(user_id):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"user_id": user_id, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_token(token: str):
    if token in TOKEN_BLACKLIST:
        raise HTTPException(status_code=401, detail="Token invalid (logged out)")
    try:
        # Correct: use jwt.decode to verify the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def get_current_user(request: Request, response: Response):
    token = request.cookies.get("access_token")

    token = request.headers.get('Authorization', token)
    #print("ACCESS TOKEN =", token)

    if not token:
        raise HTTPException(status_code=401, detail="Missing token")
    else:
        token = token.split("Bearer ")[-1]

    try:
        payload = decode_token(token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    logging.info(f"Authenticated User Id is: {user_id}")
    return user_id


def create_refresh_token(user_id):
    expire = datetime.utcnow()+timedelta(days=7)
    playload = {"user_id": user_id, "exp": expire, "type": "refresh"}
    return jwt.encode(playload, SECRET_KEY, algorithm="HS256")

def logout_user(token : str):
    TOKEN_BLACKLIST.add(token)
    return True