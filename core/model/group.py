
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
    def owner(self) -> User:
        if self._owner is None:
            self._owner = User.get_by_id(self.owner_id)
        return self._owner
