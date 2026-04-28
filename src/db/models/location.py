from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, HasId, Mixin


class Location(Base, HasId, Mixin):
    """
    Модель географической локации.
    """

    __tablename__ = "location"

    city: Mapped[str] = mapped_column(String(100), nullable=False, comment="Город")
    address: Mapped[str] = mapped_column(String(200), nullable=False, comment="Адрес")
    latitude: Mapped[float | None] = mapped_column(Float, nullable=True, comment="Широта")
    longitude: Mapped[float | None] = mapped_column(Float, nullable=True, comment="Долгота")
