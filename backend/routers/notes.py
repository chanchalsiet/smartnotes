from flask_restful import Resource, reqparse
from models import  Note
from db import db
from auth import decode_token

def get_current_user(request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None

    token = auth_header.split(" ")[1]
    user_data = decode_token(token)
    return user_data["id"] if user_data else None

class Notes(Resource):
    def get(self, request):
        user_id = get_current_user(request)
        if not user_id:
            return {"error": "Unauthorized"}, 401

        notes = Note.query.filter_by(user_id = user_id).all()
        return [{"id": n.id, "title": n.title, "content" : n.content} for n in notes]

    def post(self, request):
        user_id = get_current_user(request)
        if not user_id:
            return {"error": "Unauthorized"}, 401

        parser = reqparse.RequestParser()
        parser = add_argument("title")
        parser = add_argument("content")
        data = parser.parse_args()

        new_note = Now(title = data["title"], content = data["content"], user_id = user_id)
        db.session.add(new_note)
        db.session.commit()
        return {"message": "Notes created succesfully"}
















# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from .. import models, schemas, database, auth
#
# router = APIRouter(prefix="/smartnotes", tags = ["SmartNotes"])
#
# @router.post("/", response_model=schemas.NoteResponse)
# def create_note(note: schemas.NoteCreate, db: Session = Depends(database.get_db), user: models.User = Depends(auth.get_current_user)):
#     new_note = models.Note(**note.dict(), user_id=user.id)
#     db.add(new_note)
#     db.commit()
#     db.refresh(new_note)
#     return new_note
#
# @router.get("/", response_model=list[schemas.NoteResponse])
# def get_notes(db: Session = Depends(database.get_db), user: models.User = Depends(auth.get_current_user)):
#     return db.query(models.Note).filter(models.Note.user_id == user.id).all()