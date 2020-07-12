from dataclasses import dataclass
from decimal import *


@dataclass
class Product:
    name: str
    current_price: Decimal
