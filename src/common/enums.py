from enum import StrEnum, auto

from strenum import UppercaseStrEnum


class UserRole(StrEnum):
    """
    Роли пользователей в системе.
    """

    ADMIN = "admin"
    MANAGER = "manager"
    DRIVER = "driver"


class VehicleStatus(UppercaseStrEnum):
    """
    Статусы автомобиля.
    """

    IDLE = auto()
    BUSY = auto()
    REPAIR = auto()


class OrderStatus(StrEnum):
    """
    Статус заказа.
    """

    NEW = "new"
    ASSIGNED = "assigned"
    LOADING = "loading"
    TRANSIT = "transit"
    DELIVERED = "delivered"
    CANCELED = "cancelled"
