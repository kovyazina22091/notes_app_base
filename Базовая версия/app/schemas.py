from pydantic import BaseModel, Field
from datetime import datetime

class NoteBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1)

class NoteBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Название заметки не может быть пустым или слишком длинным")
    content: str = Field(..., min_length=1, description="Содержимое заметки не может быть пустым")

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    pass

class Note(NoteBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

