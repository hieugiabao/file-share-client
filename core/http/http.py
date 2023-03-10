import requests
from modules.app_settings import Settings
from typing import List, Tuple
from functools import wraps
# from core.model.user import User

token = ''
user = None


def is_authorized(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if token == '':
            return False, 'Not login yet'
        else:
            return func(*args, **kwargs)
    return wrapper


def token_expried():
    global token
    global user
    token = ''
    user = None
    store_token_in_local_cache(token)


def store_token_in_local_cache(token: str):
    with open(Settings.TOKEN_CACHE_FILE, 'w+') as f:
        f.write(token)


def load_token_from_local_cache():
    try:
        with open(Settings.TOKEN_CACHE_FILE, 'r') as f:
            global token
            token = f.read()
            return True
    except FileNotFoundError:
        return False


def login(username, password):
    url = Settings.SERVER_ORIGIN + '/login'
    data = {'username': username, 'password': password}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        global token
        token = response.json().get('token')
        # store token in local cache file
        store_token_in_local_cache(token)

        return (token, None)
    elif response.status_code == 401:
        return (None, 'Invalid username or password')
    else:
        return (None, 'Something went wrong')


def register(username, password, display_name):
    url = Settings.SERVER_ORIGIN + '/register'
    data = {'username': username, 'password': password,
            'display_name': display_name}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return True, None
    elif response.status_code == 409:
        return False, 'Username already exists'
    else:
        return False, 'Something went wrong'


@is_authorized
def logout():
    global user
    global token
    url = Settings.SERVER_ORIGIN + '/logout'
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        token = ''
        user = None
        store_token_in_local_cache(token)
        return True, None
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    else:
        return False, 'Something went wrong'


def get_user_info(id: int):
    url = Settings.SERVER_ORIGIN + '/user/info'
    data = {'user_id': id}
    response = requests.get(url, params=data)
    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 404:
        return False, 'User not found'
    else:
        return False, 'Something went wrong'


@is_authorized
def get_me_info():
    url = Settings.SERVER_ORIGIN + '/me/info'
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json = response.json()
        return True, json
    elif response.status_code == 401:
        token_expried()
        return True, None
    else:
        return False, 'Something went wrong'


@is_authorized
def get_me_group():
    global user
    global token
    url = Settings.SERVER_ORIGIN + '/me/group'
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    else:
        return False, 'Something went wrong'


@is_authorized
def get_group_info(id: int):
    url = Settings.SERVER_ORIGIN + '/group/info'
    data = {'group_id': id}
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.get(url, params=data, headers=headers)
    if response.status_code == 200:  # group found
        return True, response.json()
    elif response.status_code == 401:  # token expired
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 403:
        return False, 'You are not a member of this group'
    elif response.status_code == 404:  # group not found
        return False, 'Group not found'
    else:  # something went wrong
        return False, 'Something went wrong'


@is_authorized
def get_group_file_node(id: int):
    url = Settings.SERVER_ORIGIN + '/group/node'
    data = {'group_id': id}
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.get(url, params=data, headers=headers)
    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 403:
        return False, 'You are not a member of this group'
    elif response.status_code == 404:
        return False, 'Group not found'
    else:
        return False, 'Something went wrong'


@is_authorized
def create_group(data: dict):
    url = Settings.SERVER_ORIGIN + '/group/create'
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:

        return True, response.json()
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    else:
        return False, 'Something went wrong'


@is_authorized
def update_group(data: dict):
    url = Settings.SERVER_ORIGIN + '/group/update'
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 404:
        return False, 'Group not found'
    elif response.status_code == 403:
        return False, 'You are not the owner of this group'
    else:
        return False, 'Something went wrong'


@is_authorized
def delete_group(data: dict):
    url = Settings.SERVER_ORIGIN + '/group/delete'
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.delete(url, data=data, headers=headers)
    if response.status_code == 200:
        return True, None
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 404:
        return False, 'Group not found'
    elif response.status_code == 403:
        return False, 'You are not the owner of this group'
    else:
        return False, 'Something went wrong'


@is_authorized
def join_group(code: str):
    url = Settings.SERVER_ORIGIN + '/group/join'
    data = {'code': code}
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 404:
        return False, 'Group not found'
    elif response.status_code == 403:
        return False, 'You are already a member of this group'
    else:
        return False, 'Something went wrong'


@is_authorized
def leave_group(code: str):
    url = Settings.SERVER_ORIGIN + '/group/leave'
    data = {'code': code}
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 404:
        return False, 'Group not found'
    elif response.status_code == 403:
        return False, 'You are not a member of this group'
    else:
        return False, 'Something went wrong'


@is_authorized
def kick_member(code: str, member_id: int):
    url = Settings.SERVER_ORIGIN + '/group/kick'
    data = {'code': code, 'member_id': member_id}
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 404:
        return False, 'Group or member not found'
    elif response.status_code == 403:
        return False, 'You are not the owner of this group'
    elif response.status_code == 400:
        return False, 'You can not kick yourself'
    else:
        return False, 'Something went wrong'


@is_authorized
def get_directory_node(id: int):
    url = Settings.SERVER_ORIGIN + '/directory/getchild'
    data = {'directory_id': id}
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.get(url, params=data, headers=headers)
    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 403:
        return False, 'You are not permission to access this directory'
    elif response.status_code == 404:
        return False, 'Directory not found'
    else:
        return False, 'Something went wrong'


@is_authorized
def get_directory_info(id: int):
    url = Settings.SERVER_ORIGIN + '/directory/info'
    data = {'directory_id': id}
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.post(url, params=data, headers=headers)
    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 403:
        return False, 'You are not permission to access this directory'
    elif response.status_code == 404:
        return False, 'Directory not found'
    else:
        return False, 'Something went wrong'


@is_authorized
def create_directory(data: dict):
    url = Settings.SERVER_ORIGIN + '/directory/create'
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        return True, None
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 403:
        return False, 'You are not the owner of this group'
    elif response.status_code == 400:
        return False, 'Directory name already exists'
    elif response.status_code == 404:
        return False, 'Group not found'
    else:
        return False, 'Something went wrong'


@is_authorized
def update_directory(id: int, permission: int):
    url = Settings.SERVER_ORIGIN + '/directory/update'
    data = {
        'directory_id': id,
        'permission': permission
    }
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        return True, None
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 403:
        return False, 'You are not permission to update this directory'
    elif response.status_code == 404:
        return False, 'Directory not found'
    else:
        return False, 'Something went wrong'


@is_authorized
def delete_directory(id: int):
    url = Settings.SERVER_ORIGIN + '/directory/delete'
    data = {
        'directory_id': id
    }
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.delete(url, data=data, headers=headers)
    if response.status_code == 200:
        return True, None
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 403:
        return False, 'You are not permission to delete this directory'
    elif response.status_code == 404:
        return False, 'Directory not found'
    else:
        return False, 'Something went wrong'


@is_authorized
def get_file_info(id: int):
    url = Settings.SERVER_ORIGIN + '/file/info'
    data = {
        'file_id': id
    }
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.get(url, params=data, headers=headers)
    if response.status_code == 200:
        return True, None
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 403:
        return False, 'You are not permission to access this file'
    elif response.status_code == 404:
        return False, 'Directory not found'
    else:
        return False, 'Something went wrong'


@is_authorized
def create_file(data: dict):
    url = Settings.SERVER_ORIGIN + '/file/create'
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 403:
        return False, 'You are not the permission to create file here'
    elif response.status_code == 404:
        return False, 'Group or directory not found'
    else:
        return False, 'Something went wrong'


@is_authorized
def update_file(data: dict):
    url = Settings.SERVER_ORIGIN + '/file/update'
    headers = {
        'Authorization': 'Basic ' + token
    }
    response = requests.put(url, data=data, headers=headers)
    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 403:
        return False, 'You are not the permission to update file here'
    elif response.status_code == 404:
        return False, 'Group or directory not found'
    else:
        return False, 'Something went wrong'


@is_authorized
def delete_file(id: int):
    url = Settings.SERVER_ORIGIN + '/file/delete'
    headers = {
        'Authorization': 'Basic ' + token
    }
    data = {
        'file_id': id
    }
    response = requests.delete(url, data=data, headers=headers)
    if response.status_code == 200:
        return True, None
    elif response.status_code == 401:
        token_expried()
        return False, 'Token Expired'
    elif response.status_code == 403:
        return False, 'You are not the permission to delete file here'
    elif response.status_code == 404:
        return False, 'Group or directory not found'
    else:
        return False, 'Something went wrong'


def init_data() -> Tuple[bool, str | None]:
    load_token_from_local_cache()
    if token == '':
        return False, 'Token not found'
    return get_me_info()
