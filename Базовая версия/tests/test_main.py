from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_note():
    response = client.post("/notes/", json={"title": "Тестовая", "content": "Тестовый контент"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Тестовая"
    assert data["content"] == "Тестовый контент"
    assert "id" in data
    assert "created_at" in data


def test_get_notes():
    response = client.get("/notes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_search_notes():
    response = client.get("/notes/search/?q=Тест")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_note():
    create_response = client.post("/notes/", json={"title": "До обновления", "content": "Контент"})
    note_id = create_response.json()["id"]

    update_response = client.put(f"/notes/{note_id}", json={"title": "После обновления", "content": "Новый контент"})
    assert update_response.status_code == 200
    updated = update_response.json()
    assert updated["title"] == "После обновления"
    assert updated["content"] == "Новый контент"


def test_delete_note():
    create_response = client.post("/notes/", json={"title": "Для удаления", "content": "Удалить меня"})
    note_id = create_response.json()["id"]

    delete_response = client.delete(f"/notes/{note_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Заметка удалена"
