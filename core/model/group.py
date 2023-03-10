from typing import List
from core.http import get_group_info, get_me_group

class Group:
    def __init__(self, id: int, name: str, description: str, code: str, owner_id: int, avatar: str, created_at: str, status: str = None):
        self.id = id
        self.name = name
        self.description = description
        self.code = code
        self.owner_id = owner_id
        self.avatar = avatar
        self.created_at = created_at
        self.status = status
        self._owner = None

    def __str__(self):
        return f"Group(id={self.id}, name={self.name}, description={self.description}, code={self.code}, owner_id={self.owner_id}, avatar={self.avatar}, status={self.status})"

    @property
    def owner(self):
        if self._owner is None:
            self._owner = User.get_by_id(self.owner_id)
        return self._owner

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["id"], data["name"], data["description"], data["code"], data["owner_id"], data["avatar"], data["created_at"], data["status"])
    
    @staticmethod
    def get_by_id(id: int):
        status, data = get_group_info(id)
        return Group.from_dict(data) if status else None

    @staticmethod
    def fetch_my_group():
        status, data = get_me_group()
        return [Group.from_dict(group) for group in data] if status else []