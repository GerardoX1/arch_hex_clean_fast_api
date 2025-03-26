from datetime import datetime

from app.application.dto.user_dto import UserCreateDTO, UserResponseDTO
from app.application.interfaces.user_repository import IUserRepository
from app.domain.models.user import User
from app.domain.services.user_service import UserService


class CreateUserUseCase:
    """
    Caso de uso para crear un nuevo usuario.
    No depende de la infraestructura,
    pero sí requiere una interfaz para el repositorio de usuarios.
    """

    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, user_data: UserCreateDTO) -> UserResponseDTO:
        user = User(
            id=None,
            username=user_data.username,
            email=user_data.email,
            created_at=datetime.utcnow(),
        )

        # Validación de dominio
        if not UserService.validate_user_email(user):
            raise ValueError("El email no es válido")

        # Persistencia
        new_user = self.user_repository.create(user)

        # Construimos la respuesta en base al User creado
        return UserResponseDTO(
            id=new_user.id,
            username=new_user.username,
            email=new_user.email,
            created_at=new_user.created_at,
        )
