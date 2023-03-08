
class File:
    def __init__(self, name: str, path: str, size: int, permission: int, created_at: str, updated_at: str, owner_id: int, group_id: int, modify_by: int, directory_id: int = None):
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
        return self.name

    @property
    def owner(self) -> User:
        if self._owner is None:
            self._owner = User.get_by_id(self.owner_id)
        return self._owner

    @property
    def group(self) -> Group:
        if self._group is None:
            self._group = Group.get_by_id(self.group_id)
        return self._group

    @property
    def directory(self) -> Directory:
        if self._directory is None:
            self._directory = Directory.get_by_id(self.directory_id)
        return self._directory

    @property
    def modified_by(self) -> User:
        if self._modify_by is None:
            self._modify_by = User.get_by_id(self.modified_by)
        return self._modify_by
