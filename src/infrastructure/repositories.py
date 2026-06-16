from src.domain.entities import Order
from src.domain.interfaces import OrderRepository
from .database import MongoSingleton

class MongoOrderRepository(OrderRepository):
    def __init__(self):
        self.db = MongoSingleton().connection

    def save(self, order: Order) -> str:
        print(f"Salvando pedido {order.id} no banco: {self.db}")
        return "ID_GERADO_PELO_BANCO"