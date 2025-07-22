from sqlalchemy.orm import Session
from . import models, schemas

def create_note(db: Session, note: schemas.NoteCreate):
    db_note = models.Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_notes(db: Session):
    return db.query(models.Note).all()

def get_note_by_id(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()

def update_note(db: Session, note_id: int, note: schemas.NoteCreate):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if db_note is None:
        return None
    db_note.title = note.title
    db_note.content = note.content
    db.commit()
    db.refresh(db_note)
    return db_note

def delete_note(db: Session, note_id: int):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if db_note is None:
        return None
    db.delete(db_note)
    db.commit()
    return db_note

def search_notes(db: Session, query: str):
    return db.query(models.Note).filter(
        (models.Note.title.contains(query)) | (models.Note.content.contains(query))
    ).all()
