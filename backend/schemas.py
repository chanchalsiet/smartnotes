from pydantic import BaseModel
from typing import Optional, List


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

class NoteResponse(BaseModel):
    id: int
    notes: str
    has_files: bool
    files: List[FileResponse] = []

    class Config:
        orm_mode = True

class FileBase(BaseModel):
    filename: str
    file_path: str

class FileCreate(FileBase):
    pass

class FileOut(FileBase):
    id: int
    uploaded_at: datetime
    class Config:
        orm_mode = True
