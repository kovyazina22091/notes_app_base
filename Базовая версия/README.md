# Note Service (FastAPI + SQLite)

Мини-сервис для управления заметками. Реализован на FastAPI с использованием SQLAlchemy и SQLite.  
Позволяет создавать, просматривать, редактировать, удалять и искать текстовые заметки.

## Стек технологий

- **Python 3.10+
- **FastAPI** — веб-фреймворк
- **SQLAlchemy** — ORM
- **SQLite** — встроенная база данных
- **Pydantic** — валидация данных

---

## Установка и запуск

1. **Распакуйте архив**

2. **Создайте и активируйте виртуальное окружение (опционально):**
python -m venv .venv
source .venv/bin/activate         # Для Linux/macOS
.venv\Scripts\activate            # Для Windows

4. **Установите зависимости:**
pip install -r requirements.txt

5. **Запустите сервер:**
uvicorn app.main:app --reload

6. **Откройте документацию:**
http://127.0.0.1:8000/docs

---

# Эндпоинты API
Метод	URL	 Описание
POST /notes/	Создать новую заметку
GET	/notes/	Получить список всех заметок
GET	/notes/{id}	Получить заметку по ID
PUT	/notes/{id}	Обновить заметку по ID
DELETE	/notes/{id}	Удалить заметку по ID
GET	/notes/search/?q=word	Найти заметки по ключевому слову

# Пример запроса (cURL)
**Создание заметки:**

curl -X POST "http://127.0.0.1:8000/notes/" \
     -H "Content-Type: application/json" \
     -d '{"title": "Первая заметка", "content": "Это текст"}'

**Получение всех заметок:**

curl -X GET "http://127.0.0.1:8000/notes/"

**Поиск:**

curl -X GET "http://127.0.0.1:8000/notes/search/?q=текст"

## Тестирование

Перед запуском тестов установите переменную окружения:

$env:PYTHONPATH = "."  # Windows
export PYTHONPATH=. # Linux/macOS

Затем запустите тесты: pytest

# Структура проекта

notes_app/
├── app/
│   ├── main.py          # Точка входа (FastAPI app)
│   ├── models.py        # SQLAlchemy модели
│   ├── schemas.py       # Pydantic схемы
│   ├── crud.py          # CRUD-операции
│   └── database.py      # Настройка БД
│
├── tests/
│    └── test_main.py    # Тесты pytest
│
├── notes.db             # SQLite база данных
├── requirements.txt     # Зависимости
└── README.md            # Инструкция (вы здесь)


# Валидация и ошибки
- Поля title и content не могут быть пустыми
- Если заметка с заданным id не найдена — возвращается 404 Not Found
- При неверном теле запроса — 422 Unprocessable Entity

# Примечания
- Swagger доступен по адресу: /docs
- Также доступна альтернативная документация ReDoc по адресу: /redoc

