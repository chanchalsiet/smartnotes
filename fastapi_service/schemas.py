from _pydantic import BaseModel
from typing import Optional, List

class NoteBase(BaseModel):
    notes: str


class NoteCreate(NoteBase):
    pass

class NoteResponse(NoteBase):
    id : int
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    user_name : str
    email : str


class UserCreate(UserBase):
    pass

class NoteResponse(UserBase):
    id : int
    class Config:
        orm_mode = True

class Token(BaseModel)
    access_token :str
    token_type :str