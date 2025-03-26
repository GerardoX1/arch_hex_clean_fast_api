from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.models.user import User


class IUserRepository(ABC):
    """
    Puerto (interfaz) para operar con la persistencia de usuarios.
    """

    @abstractmethod
    def create(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[User]:
        raise NotImplementedError
