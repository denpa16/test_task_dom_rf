from sqlalchemy import Column, Integer
from sqlalchemy.orm import as_declarative


@as_declarative()
class Base:
    """Базовый класс моделей."""

    id = Column(Integer, primary_key=True, autoincrement=True)
