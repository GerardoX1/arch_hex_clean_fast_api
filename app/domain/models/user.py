from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    """
    Entidad principal que representa a un Usuario en tu dominio.
    No depende de librerías externas ni de frameworks.
    """

    id: Optional[int]
    username: str
    email: str
    created_at: datetime
