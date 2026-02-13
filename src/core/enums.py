from enum import StrEnum


class UserRole(StrEnum):
    """
    Роли пользователей в системе.
    """

    ADMIN = "admin"
    MANAGER = "manager"
    DRIVER = "driver"


class VehicleStatus(StrEnum):
    """
    Статусы автомобиля.
    """

    IDLE = "idle"
    BUSY = "busy"
    REPAIR = "repair"


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
