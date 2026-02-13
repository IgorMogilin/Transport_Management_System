from datetime import datetime
from decimal import Decimal

from sqlalchemy import DECIMAL, UUID, ForeignKey
from sqlalchemy import DateTime as SQLDateTime
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

from src.core.enums import OrderStatus
from src.db.base import BaseModel


class Order(BaseModel):
    """
    Модель заказа.
    """

    __tablename__ = "order"

    manager_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
    driver_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=False), ForeignKey("user.id", ondelete="SET NULL"), nullable=True
    )
    vehicle_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=False), ForeignKey("vehicle.id", ondelete="SET NULL"), nullable=True
    )
    pickup_location_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("location.id", ondelete="RESTRICT"), nullable=False
    )
    delivery_location_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("location.id", ondelete="RESTRICT"), nullable=False
    )
    departure_date: Mapped[datetime] = mapped_column(SQLDateTime(timezone=True), nullable=False)
    arrival_date: Mapped[datetime] = mapped_column(SQLDateTime(timezone=True), nullable=False)
    status: Mapped[OrderStatus] = mapped_column(
        SQLEnum(OrderStatus, native_enum=False),
        default=OrderStatus.NEW,
        server_default="new",
        nullable=False,
    )
    price: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), nullable=False)
