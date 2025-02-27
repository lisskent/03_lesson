import requests

BASE_URL = "https://ru.yougile.com/api-v2"


# Замените эти переменные на ваши реальные данные
class GetKey:
    def get_auth_token():
        url = f"{BASE_URL}/auth/keys"
        data = {
            "login": "mymail@here.com",
            "password": "SuperStrongPassword123",
            "companyId": "7452a291-7268-43f6-b4ae-90f94f005fa5"
        }
        response = requests.post(url, json=data)
        return response.json().get("key")
