from dataclasses import dataclass
from decimal import *
from domain.product import Product


@dataclass
class PromoProduct(Product):
    old_price: Decimal
    discount_percent: int

