from sqlalchemy import Column, DateTime, Integer, String

# Ejemplo: from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()

# Suponiendo que ya tienes una instancia de Base del core
# (o de donde manejes tu engine y session).


class UserORM:  # Normalmente hereda de Base
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)
    created_at = Column(DateTime)

    def save(self):
        """
        Lógica para guardar en DB.
        Podrías usar la sesión de SQLAlchemy directamente.
        """
        pass
