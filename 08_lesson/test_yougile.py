import requests
from getkey import GetKey

BASE_URL = "https://ru.yougile.com/api-v2"
API_TOKEN = GetKey.get_auth_token()
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Позитивные тесты


# Создает новый проект и проверяет, что статус ответа 201
def test_create_project():
    url = f"{BASE_URL}/projects"
    data = {
        "title": "Test Project",
        "users": {
        }
    }
    response = requests.post(url, json=data, headers=HEADERS)
    assert response.status_code == 201


# Обновляет существующий проект и проверяет, что статус ответа 200
def test_update_project():
    project_id = create_test_project()
    url = f"{BASE_URL}/projects/{project_id}"
    data = {
        "title": "Updated Test Project"
    }
    response = requests.put(url, json=data, headers=HEADERS)
    assert response.status_code == 200


# Получает проект по ID и проверяет, что статус ответа 200 и ID соответствует ожидаемому
def test_get_project():
    project_id = create_test_project()
    url = f"{BASE_URL}/projects/{project_id}"
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 200
    assert response.json().get("id") == project_id

# Негативные тесты


# Пытается создать проект без имени и ожидает ошибку 400
def test_create_project_without_name():
    url = f"{BASE_URL}/projects"
    data = {
        "description": "This project has no name."
    }
    response = requests.post(url, json=data, headers=HEADERS)
    assert response.status_code == 400


# Пытается обновить несуществующий проект и ожидает ошибку 404
def test_update_nonexistent_project():
    url = f"{BASE_URL}/projects/999999"  # Предполагаем, что такого проекта нет
    data = {
        "title": "Updated Test Project"
    }
    response = requests.put(url, json=data, headers=HEADERS)
    assert response.status_code == 404


# Пытается получить несуществующий проект и ожидает ошибку 404
def test_get_nonexistent_project():
    url = f"{BASE_URL}/projects/999999"  # Предполагаем, что такого проекта нет
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 404


# Вспомогательная функция для создания тестового проекта
def create_test_project():
    url = f"{BASE_URL}/projects"
    data = {
        "title": "Temporary Project",
        "users": {
        }
    }
    response = requests.post(url, json=data, headers=HEADERS)
    return response.json().get("id")
