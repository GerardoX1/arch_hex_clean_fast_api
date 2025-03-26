from app.domain.models.user import User


class UserService:
    """
    Servicio de Dominio para lógica más compleja relacionada a 'User'.
    """

    @staticmethod
    def validate_user_email(user: User) -> bool:
        # Ejemplo simple de validación.
        return "@" in user.email
