from dataclasses import dataclass, field
from typing import List

@dataclass
class Order:
    id: str
    customer_name: str
    items: List[str]
    base_price: float
    total_price: float = 0.0
    is_weekend: bool = False