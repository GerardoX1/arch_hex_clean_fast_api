from fastapi import APIRouter, Depends

from app.adapters.database.user_repository_impl import UserRepositoryImpl
from app.application.dto.user_dto import UserCreateDTO, UserResponseDTO
from app.application.interactors.create_user import CreateUserUseCase

router = APIRouter()


@router.post("/", response_model=UserResponseDTO)
def create_user(user_data: UserCreateDTO):
    # Crear instancia del repositorio (en la práctica podrías usar inyección de dependencias).
    user_repository = UserRepositoryImpl()
    create_user_uc = CreateUserUseCase(user_repository)
    return create_user_uc.execute(user_data)
