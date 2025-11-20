from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import HTTPException, Header, Request
from werkzeug.security import generate_password_hash, check_password_hash
from config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES

print(SECRET_KEY)

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

# def get_current_user(Authorization: str = Header(None)):
#     # debug prints are useful while developing:
#     print("---- DEBUG ----")
#     print("Authorization header received:", Authorization)
#
#     if not Authorization:
#         print("ERROR: No Authorization header found")
#         raise HTTPException(status_code=401, detail="Missing Authorization header")
#
#     try:
#         parts = Authorization.split(" ")
#         # Expect e.g. ["Bearer", "<token>"]
#         if len(parts) != 2 or parts[0].lower() != "bearer":
#             print("ERROR: Invalid Authorization format", parts)
#             raise HTTPException(status_code=401, detail="Invalid Authorization format")
#         token = parts[1]
#         print("Extracted token:", token)
#     except Exception as e:
#         print("ERROR while splitting Authorization:", str(e))
#         raise HTTPException(status_code=401, detail="Invalid Authorization format")
#
#     payload = decode_token(token)
#     # payload should be dictionary with "user_id"
#     print("Decoded payload:", payload)
#     user_id = payload.get("user_id")
#     if not user_id:
#         raise HTTPException(status_code=401, detail="Invalid token payload")
#     return user_id
def get_current_user(request: Request, response: Response):
    token = request.cookies.get("access_token")
    if token:
        try:

    print("COOKIE TOKEN =", token)
    if not token:
        raise HTTPException(status_code=401, detail="Missing token")
    payload = decode_token(token)
    user_id = payload.get("user_id")
    return user_id

def create_refresh_token(user_id):
    expire = datetime.utcnow()+timedelta(days=7)
    playload = {"user_id": user_id, "exp": expire, "type": "refresh"}
    return jwt.encode(playload, SECRET_KEY, algorithm="HS256")

def logout_user(token : str):
    TOKEN_BLACKLIST.add(token)
    return True