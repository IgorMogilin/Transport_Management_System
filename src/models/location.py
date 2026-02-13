from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import BaseModel


class Location(BaseModel):
    """
    Модель географической локации.
    """

    __tablename__ = "location"

    city: Mapped[str] = mapped_column(String(100), nullable=False)
    address: Mapped[str] = mapped_column(String(200), nullable=False)
    latitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    longitude: Mapped[float | None] = mapped_column(Float, nullable=True)
