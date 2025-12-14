from sqlalchemy.orm import Session
import models, schemas, auth
from typing import Optional


def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = auth.hash_password(user.password)
    db_user = models.User(
        full_name=user.full_name,
        email=user.email,
        password=hashed_pw,
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def update_user(db: Session, user_id: int, user_data: schemas.UpdateUser):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        return None
    try:
        for key, value in user_data.dict(exclude_unset=True).items():
            if key == "password" and value:
                value = auth.hash_password(value)
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print("ERROR in update_user:", e)
        raise
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session , user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        None
    db.delete(db_user)
    db.commit()
    return db_user

def delete_all_user(db:Session):
    delete_count = db.query(models.User).delete()
    db.commit()
    return deleted_count


def get_all_users(db: Session):
    return db.query(models.User).all()


def create_note(db: Session, notes_text: str, user_id: int):
    note = models.Note(
        notes=notes_text,
        user_id=user_id
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def update_notes(db: Session, notes_id: int, note_data: schemas.UpdateNotes):
    db_note = db.query(models.Note).filter(models.Note.id == notes_id).first()
    if not db_note:
        None
    for key, value in note_data.dict().items():
        setattr(db_note, key, value)
    db.commit()
    db.refresh(db_note)
    return db_note

def delete_notes(db: Session , notes_id: int):
    db_note = db.query(models.Note).filter(models.Note.id == notes_id).first()
    if not db_note:
        None
    db.delete(db_note)
    db.commit()
    return db_note

def get_all_notes(db: Session):
    return db.query(models.Note).all()

def get_notes_by_user(db: Session, user_id: int):
    return db.query(models.Note).filter(models.Note.user_id == user_id).all()