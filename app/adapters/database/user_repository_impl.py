from typing import List, Optional

from app.adapters.orm_models.user_orm import UserORM
from app.application.interfaces.user_repository import IUserRepository
from app.domain.models.user import User


class UserRepositoryImpl(IUserRepository):
    """
    Implementación concreta del puerto IUserRepository
    usando, por ejemplo, SQLAlchemy.
    """

    def create(self, user: User) -> User:
        # Conversión a modelo ORM
        orm_obj = UserORM(
            username=user.username,
            email=user.email,
            created_at=user.created_at,
        )
        # Guardar en DB
        orm_obj.save()
        # Actualizar el 'id' en la entidad de dominio
        user.id = orm_obj.id
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        ...
        return None

    def list_all(self) -> List[User]:
        ...
        return []
