from dataclasses import dataclass
from enum import Enum
import datetime


@dataclass
class Product:
    id: int
    name: str
    cents: int


class OrderStates(Enum):
    CHARGING_CARD = "Charging card"
    PAID = "Paid"
    PICKED_UP = "Picked up"
    DELIVERED = "Delivered"
    REFUNDING = "Refunding"
    FAILED = "Failed"


@dataclass
class OrderStatus:
    product_id: int
    state: OrderStates
    delivered_at: datetime

