from typing import TYPE_CHECKING

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.enums import UserRole
from src.db.base import BaseModel

if TYPE_CHECKING:
    from src.models.vehicle import Vehicle


class User(BaseModel):
    """
    Модель пользовтеля.
    """

    __tablename__ = "user"

    email: Mapped[str] = mapped_column(String(254), unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String(60), nullable=False)
    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole, native_enum=False),
        nullable=False,
        default=UserRole.DRIVER,
        server_default="driver",
    )
    name: Mapped[str] = mapped_column(String(70), nullable=False)
    surname: Mapped[str] = mapped_column(String(70), nullable=False)
    phone_number: Mapped[str | None] = mapped_column(String(24), nullable=True)
    vehicle: Mapped["Vehicle"] = relationship("Vehicle", back_populates="driver")
