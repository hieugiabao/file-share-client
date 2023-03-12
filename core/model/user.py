from core.http import get_user_info, get_me_info

class User:
    def __init__(self, id: int, display_name: str, username: str, status: str = None):
        self.id = id
        self.display_name = display_name
        self.username = username
        self.status = status
        
    def __str__(self):
        return f"User(id={self.id}, display_name={self.display_name}, username={self.username}, status={self.status})"
      
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.id == other.id and self.username == other.username
        
    def __hash__(self):
        return hash(self.id) + hash(self.username)
    
    def to_dict(self):
        return {
            "id": self.id,
            "display_name": self.display_name,
            "username": self.username,
            "status": self.status
        }
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["id"], data["display_name"], data["username"], data["status"])
    
    @staticmethod
    def get_by_id(id: int):
        status, data = get_user_info(id)
        return User.from_dict(data) if status else None
    
    @staticmethod
    def retrieve_from_token():
        status, data = get_me_info()
        return User.from_dict(data) if status == True else None