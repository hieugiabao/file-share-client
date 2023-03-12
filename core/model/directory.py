from .user import User
from .file import File
from core.http import get_directory_node, get_directory_info, create_directory, delete_directory, update_directory

class Directory:
    def __init__(self, id: int, name: str, permission: int, path: str, group_id: int, owner_id: int, created_at: str, parent_id: int):
        self.id = id
        self.name = name
        self.permission = permission
        self.path = path
        self.group_id = group_id
        self.owner_id = owner_id
        self.created_at = created_at
        self.parent_id = parent_id
        self._owner = None
        self._group = None
        self._parent = None
        self._nodes = None
        
    def __str__(self):
        return f'Directory(id={self.id}, name={self.name}, permission={self.permission}, path={self.path}, group_id={self.group_id}, owner_id={self.owner_id}, created_at={self.created_at}, parent_id={self.parent_id})'

    @property
    def owner(self):
        if self._owner is None:
            self._owner = User.get_by_id(self.owner_id)
        return self._owner

    @property
    def parent(self):
        if self.parent_id == 0:
            return None
        if self._parent is None:
            self._parent = Directory.get_by_id(self.parent_id)
        return self._parent

    @property
    def group(self):
        if self._group is None:
            self._group = Group.get_by_id(self.group_id)
        return self._group
    
    @property
    def nodes(self):
        if self._nodes is None:
            status, data = get_directory_node(self.id)
            self._nodes = [
                Directory.from_dict(node['node']) if node['type'] == 'directory' else File.from_dict(node['node']) for node in data
            ] if status else []
        return self._nodes

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["id"], data["name"], data["permission"], data["path"], data["group_id"], data["owner_id"], data["created_at"], data["parent_id"])

    @staticmethod
    def get_by_id(id: int):
        status, data = get_directory_info(id)
        return Directory.from_dict(data) if status else None
    
    @staticmethod
    def create_one(data: dict):
        status, res = create_directory(data)
        if status:
            return True, Directory.from_dict(res)
        else:
            return False, res
        
    @staticmethod
    def delete_one(id: int):
        return delete_directory(id)
    
    @staticmethod
    def update_permission(id: int, permission: int):
        return update_directory(id, permission)