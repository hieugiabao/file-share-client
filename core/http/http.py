import requests


class HttpHandle:
    @staticmethod
    def login(username, password):
        url = 'http://localhost:8000/login'
        data = {'username': username, 'password': password}
        response = requests.post(url, params=data)
        if response.status_code == 200:
            return (response.json().get('token'), None)
        elif response.status_code == 401:
            return (None, 'Invalid username or password')
        else:
            return (None, 'Something went wrong')

    @staticmethod
    def register(username, password, display_name):
        url = 'http://localhost:8000/register'
        data = {'username': username, 'password': password,
                'display_name': display_name}
        response = requests.post(url, params=data)
        if response.status_code == 200:
            return True, None
        elif response.status_code == 409:
            return False, 'Username already exists'
        else:
            return False, 'Something went wrong'
