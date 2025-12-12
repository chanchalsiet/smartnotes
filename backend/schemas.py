from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    full_name: str
    first_name: str
    last_name: str
    username: str
    email: str
    password: str


class UpdateUser(BaseModel):
    full_name: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    password: Optional[str]
    status: Optional[str]


class UserLogin(BaseModel):
    email: str
    password: str


class NoteCreate(BaseModel):
    note: str
    file_path: Optional[str] = None


class UpdateNotes(BaseModel):
    notes: str

