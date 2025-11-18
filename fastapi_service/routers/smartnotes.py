from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database, auth

router = APIRouter(prefix="/smartnotes", tags = ["SmartNotes"])

@router.post("/", response_model=schemas.NoteResponse)
def create_note(note: schemas.NoteCreate, db: Session = Depends(database.get_db), user: models.User = Depends(auth.get_current_user)):
    new_note = models.Note(**note.dict(), user_id=user.id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@router.get("/", response_model=list[schemas.NoteResponse])
def get_notes(db: Session = Depends(database.get_db), user: models.User = Depends(auth.get_current_user)):
    return db.query(models.Note).filter(models.Note.user_id == user.id).all()