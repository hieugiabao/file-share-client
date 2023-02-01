import requests


class HttpHandle:
    @staticmethod
    def login(username, password) -> str | None:
        url = 'http://localhost:8000/login'
        data = {'username': username, 'password': password}
        response = requests.post(url, params=data)
        if response.status_code == 200:
            return response.json().get('token')
        else:
            return None
