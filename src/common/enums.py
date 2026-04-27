from enum import auto

from strenum import UppercaseStrEnum


class UserRole(UppercaseStrEnum):
    """
    Роли пользователей в системе.
    """

    ADMIN = auto()
    MANAGER = auto()
    DRIVER = auto()


class VehicleStatus(UppercaseStrEnum):
    """
    Статусы автомобиля.
    """

    IDLE = auto()
    BUSY = auto()
    REPAIR = auto()


class OrderStatus(UppercaseStrEnum):
    """
    Статус заказа.
    """

    NEW = auto()
    ASSIGNED = auto()
    LOADING = auto()
    TRANSIT = auto()
    DELIVERED = auto()
    CANCELED = auto()
