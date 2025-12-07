from fastapi import FastAPI, Depends, HTTPException, Header, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import User
from schemas import UserCreate, UpdateUser, UserLogin, NoteCreate, UpdateNotes
from fastapi.staticfiles import StaticFiles
import crud
import auth

from sqlalchemy import text
from sqlalchemy import event
app = FastAPI(title="SmartNotes API")
# app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")

import pdb
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://13.58.138.43:8000/",
    "*",
    "http://13.58.138.43:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # allow all methods
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()  # create a new session uvicorn backend.main:app --reload
    try:
        yield db          # provide session to route
    finally:
        db.close()


@app.get("/api")
def home():
    return {"message": "SmartNotes API Running"}
    
# Health check
@app.get("/api/health")
def health():
    return {"message": "SmartNotes API Running"}
@app.post("/api/login")
def login(data: UserLogin, response: Response, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, data.email)
    if not user or not auth.verify_password(user.password, data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth.create_access_token(user.id)
    refresh_token = auth.create_access_token(user.id)
    # set response header
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        samesite="strict"
    )
    # set reference response header
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        samesite="strict"
    )
    return {"access_token": token,"token_type": "bearer", "username": user.username, "user_id": user.id}


@app.post("/api/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        (User.email == user.email) | (User.username == user.username)).first()
    print(existing_user)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email or username already exists")
    hashed_pw = auth.hash_password(user.password)

    # Create user
    new_user = User(
        full_name=user.full_name,
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        email=user.email,
        password=hashed_pw
    )
    print(new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"status": "new_user","query": existing_user, "user_id": new_user.id}


@app.get("/api/users/profile")
def user_profile(user_id: int = Depends(auth.get_current_user),db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    return user


@app.post("/api/update_user/{user_id}")
def update_user(user_id: int, user: UpdateUser,db: Session = Depends(get_db), user_logged: int = Depends(auth.get_current_user)):
    # user_logged is the id extracted from JWT
    db_user = crud.update_user(db, user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"status": "success", "user": db_user}


@app.delete("/api/delete_user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), user_logged: int = Depends(auth.get_current_user)):
    db_user = crud.delete_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail = "User not found")
    return {"status": "sucess", "message": f"User {user_id} deleted"}

@app.delete("/api/delete_all_user")
def delete_all_user(db: Session = Depends(get_db)):
    count = crud.delete_all_user(db)
    return {"status": "sucess", "message": f"Deleted {count} user(s)"}


@app.get("/api/all_users")
def get_all_user(db: Session = Depends(get_db)):
    users = crud.get_all_users(db)
    return {"status": "success", "users": users}


@app.post("/api/add_notes")
def add_notes(
    note: NoteCreate,
    user_id: int = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):

    return crud.create_note(db, note, user_id)


@app.post("/api/edit_notes/{notes_id}")
def edit_notes(notes_id: int, note: UpdateNotes, db: Session = Depends(get_db)):
    db_notes = crud.update_notes(db, notes_id, note)
    if not db_notes:
        raise HTTPException(status_code=404, detail="note not found")
    return {"status": "success", "note": db_notes}


@app.get("/api/all_notes")
def get_all_notes(db: Session = Depends(get_db)):
    notes = crud.get_all_notes(db)
    return {"notes": notes}

@app.get("/api/all_notes_by_user")
def get_notes_by_user( user_id: int = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    notes = crud.get_notes_by_user(db, user_id)
    return {"notes": notes}

@app.post("/api/delete_notes/{notes_id}")
def delete_notes(notes_id: int, db: Session = Depends(get_db)):
    db_notes = crud.delete_notes(db, notes_id)
    if not db_notes:
        raise HTTPException(status_code=404, detail="notes not found")
    return {"status": "sucess", "message": f"notes  {notes_id} deleted"}
@app.post("/api/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return {"message": "Logged out succesfully"}
