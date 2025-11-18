# from fastapi import APIRouter, Depends, HTTPException
# from fastapi.security import OAuth2PasswordRequestForm
# from passlib.context import CryptContext
# from datetime import timedelta
# from fastapi_jwt_auth import AuthJWT
#
# router = APIRouter()
#
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#
# fake_user = {
#     "username": "ramu",
#     "password": pwd_context.hash("ramu123")  # hashed password
# }
#
# @router.post("/login")
# def login(form_data: OAuth2PasswordRequestForm = Depends(), Authorize: AuthJWT = Depends()):
#     if form_data.username != fake_user["username"] or \
#        not pwd_context.verify(form_data.password, fake_user["password"]):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#
#     access_token = Authorize.create_access_token(
#         subject=form_data.username,
#         expires_time=timedelta(hours=1)
#     )
#     return {"access_token": access_token}
