from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/notes/", response_model=schemas.Note)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    new_note = crud.create_note(db=db, note=note)
    return new_note

@app.get("/notes/", response_model=List[schemas.Note])
def read_notes(db: Session = Depends(get_db)):
    return crud.get_notes(db)

@app.get("/notes/{note_id}", response_model=schemas.Note)
def read_note(note_id: int, db: Session = Depends(get_db)):
    db_note = crud.get_note_by_id(db, note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Заметка не найдена")
    return db_note

@app.put("/notes/{note_id}", response_model=schemas.Note)
def update_note(note_id: int, note: schemas.NoteCreate, db: Session = Depends(get_db)):
    updated = crud.update_note(db, note_id, note)
    if updated is None:
        raise HTTPException(status_code=404, detail="Заметка не найдена")
    return updated

@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_note(db, note_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Заметка не найдена")
    return {"message": "Заметка удалена"}

@app.get("/notes/search/", response_model=List[schemas.Note])
def search_notes(q: str, db: Session = Depends(get_db)):
    return crud.search_notes(db, q)

