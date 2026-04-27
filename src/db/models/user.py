from typing import TYPE_CHECKING

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.common.enums import UserRole

from .base import Base, HasId, Mixin

if TYPE_CHECKING:
    from db.models.vehicle import Vehicle


class User(Base, HasId, Mixin):
    """
    Модель пользователя.
    """

    __tablename__ = "user"

    email: Mapped[str] = mapped_column(String(254), unique=True, index=True, nullable=False, comment="Email")
    password: Mapped[str] = mapped_column(String(60), nullable=False, comment="Пароль")
    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole, native_enum=False),
        nullable=False,
        default=UserRole.DRIVER.value,
        server_default="driver",
        comment="Роль",
    )
    name: Mapped[str] = mapped_column(String(70), nullable=False, comment="Имя")
    surname: Mapped[str] = mapped_column(String(70), nullable=False, comment="Фамилия")
    phone_number: Mapped[str | None] = mapped_column(String(24), nullable=True, comment="Номер телефона")
    vehicle: Mapped["Vehicle"] = relationship(
        "Vehicle",
        back_populates="driver",
        primaryjoin="User.id == Vehicle.driver_id",
    )
