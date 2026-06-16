from abc import ABC, abstractmethod
from .entities import Order

class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> str:
        pass

class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, base_price: float) -> float:
        pass