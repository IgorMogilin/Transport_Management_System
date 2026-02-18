from typing import TYPE_CHECKING

from common.enums import VehicleStatus
from sqlalchemy import UUID, ForeignKey, String
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import Base, HasId, Mixin

if TYPE_CHECKING:
    from db.models.user import User


class Vehicle(Base, HasId, Mixin):
    """
    Модель транспорта.
    """

    __tablename__ = "vehicle"

    license_plate: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        comment="Государственный номер",
    )
    status: Mapped[VehicleStatus] = mapped_column(
        SQLEnum(VehicleStatus, native_enum=False),
        server_default=VehicleStatus.IDLE,
        comment="Статус транспорта",
    )
    specs: Mapped[dict] = mapped_column(
        JSONB,
        server_default="{}",
        comment="Характеристики транспорта",
    )
    driver_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("user.id", ondelete="SET NULL"),
        unique=True,
        comment="Номер водительского удостоверения",
    )
    driver: Mapped["User"] = relationship(
        "User",
        back_populates="vehicle",
        primaryjoin="User.id == Vehicle.driver_id",  # Иначе AmbiguousForeignKeysError
    )
