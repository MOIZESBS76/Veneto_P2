from src.domain.entities import Order
from src.domain.interfaces import OrderRepository, PricingStrategy

class ProcessOrderUseCase:
    def __init__(self, repository: OrderRepository, strategy: PricingStrategy):
        self.repository = repository
        self.strategy = strategy

    def execute(self, order: Order) -> str:
        # Aplica o padrão Strategy para calcular o preço
        order.total_price = self.strategy.calculate(order.base_price)
        return self.repository.save(order)