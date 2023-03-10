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

    @property
    def owner(self):
        if self._owner is None:
            self._owner = User.get_by_id(self.owner_id)
        return self._owner

    @property
    def parent(self):
        if self._parent is None:
            self._parent = Directory.get_by_id(self.parent_id)
        return self._parent

    @property
    def group(self):
        if self._group is None:
            self._group = Group.get_by_id(self.group_id)
        return self._group

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["id"], data["name"], data["permission"], data["path"], data["group_id"], data["owner_id"], data["created_at"], data["parent_id"])
