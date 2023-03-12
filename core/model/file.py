from .user import User
from core.http import create_file, save_file, delete_file, update_file


class File:
    def __init__(self, id: int, name: str, path: str, size: int, permission: int, created_at: str, updated_at: str, owner_id: int, group_id: int, modify_by: int, directory_id: int = None):
        self.id = id
        self.name = name
        self.path = path
        self.size = size
        self.permission = permission
        self.created_at = created_at
        self.updated_at = updated_at
        self.owner_id = owner_id
        self.group_id = group_id
        self.modify_by = modify_by
        self.directory_id = directory_id
        self._owner = None
        self._group = None
        self._modify_by = None
        self._directory = None

    def __str__(self):
        return f'File(name={self.name}, path={self.path}, size={self.size}, permission={self.permission}, created_at={self.created_at}, updated_at={self.updated_at}, owner_id={self.owner_id}, group_id={self.group_id}, modify_by={self.modify_by}, directory_id={self.directory_id})'

    @property
    def owner(self):
        if self._owner is None:
            self._owner = User.get_by_id(self.owner_id)
        return self._owner

    @property
    def group(self):
        if self._group is None:
            self._group = Group.get_by_id(self.group_id)
        return self._group

    @property
    def directory(self):
        if self._directory is None:
            self._directory = Directory.get_by_id(self.directory_id)
        return self._directory

    @property
    def modified_by(self):
        if self._modify_by is None:
            self._modify_by = User.get_by_id(self.modify_by)
        return self._modify_by

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data['id'], data["name"], data["path"], data["size"], data["permission"], data["created_at"], data["updated_at"], data["owner_id"], data["group_id"], data["modified_by"], data["directory_id"])

    @staticmethod
    def create_file(data: dict):
        status, res = create_file(data)
        if status:
            return True, res['path']
        else:
            return False, res

    @staticmethod
    def save_file(data: dict):
        status, res = save_file(data)
        if status:
            return True, File.from_dict(res)
        else:
            return False, res

    @staticmethod
    def delete_one(id: int):
        return delete_file(id)

    def update_permission(id: int, permission: int):
        return update_file({
            'file_id': id,
            'permission': permission
        })
