import pytest
from app.application.Interactors.create_user import CreateUserUseCase
from app.application.dto.user_dto import UserCreateDTO
from app.domain.models.user import User

class FakeUserRepository:
    # Implementación mock
    def create(self, user: User) -> User:
        user.id = 1
        return user
    def get_by_id(self, user_id: int):
        return None
    def list_all(self):
        return []

@pytest.mark.unit
def test_create_user_use_case():
    repo = FakeUserRepository()
    use_case = CreateUserUseCase(repo)

    user_data = UserCreateDTO(username="test", email="test@example.com")
    result = use_case.execute(user_data)

    assert result.id == 1
    assert result.username == "test"
    assert result.email == "test@example.com"