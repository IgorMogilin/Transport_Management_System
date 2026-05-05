from datetime import datetime
from decimal import Decimal

from sqlalchemy import DECIMAL, UUID, ForeignKey
from sqlalchemy import DateTime as SQLDateTime
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

from src.common.enums import OrderStatus

from .base import Base, HasId, Mixin


class Order(Base, HasId, Mixin):
    """
    Модель заказа.
    """

    __tablename__ = "order"

    manager_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("user.id", ondelete="CASCADE"), nullable=False, comment="ID менеджера"
    )
    driver_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=False), ForeignKey("user.id", ondelete="SET NULL"), nullable=True, comment="ID водителя"
    )
    vehicle_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=False), ForeignKey("vehicle.id", ondelete="SET NULL"), nullable=True, comment="ID автомобиля"
    )
    pickup_location_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("location.id", ondelete="RESTRICT"),
        nullable=False,
        comment="ID места отправления",
    )
    delivery_location_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("location.id", ondelete="RESTRICT"),
        nullable=False,
        comment="ID места назначения",
    )
    departure_date: Mapped[datetime] = mapped_column(
        SQLDateTime(timezone=True), nullable=False, comment="Дата отправления"
    )
    arrival_date: Mapped[datetime] = mapped_column(SQLDateTime(timezone=True), nullable=False, comment="Дата прибытия")
    status: Mapped[OrderStatus] = mapped_column(
        SQLEnum(OrderStatus, native_enum=False),
        default=OrderStatus.NEW.value,  # TODO Не обязательно указывать .value
        server_default="new",  # TODO Одновременное default и server_default обычно избыточно
        nullable=False,
        comment="Статус",
    )
    price: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), nullable=False, comment="Стоимость")
