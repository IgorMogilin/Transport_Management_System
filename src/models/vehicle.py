from typing import TYPE_CHECKING

from sqlalchemy import JSON, UUID, ForeignKey, String
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.enums import VehicleStatus
from src.db.base import BaseModel

if TYPE_CHECKING:
    from src.models.user import User


class Vehicle(BaseModel):
    """
    Модель транспорта.
    """

    __tablename__ = "vehicle"

    license_plate: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    status: Mapped[VehicleStatus] = mapped_column(
        SQLEnum(VehicleStatus, native_enum=False),
        default=VehicleStatus.IDLE,
        server_default="idle",
        nullable=False,
    )
    specs: Mapped[dict] = mapped_column(JSON, nullable=False, default={}, server_default="{}")
    driver_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=False), ForeignKey("user.id", ondelete="SET NULL"), nullable=True, unique=True
    )
    driver: Mapped["User"] = relationship("User", back_populates="vehicle")
