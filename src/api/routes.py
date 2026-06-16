from fastapi import APIRouter, Depends
from src.infrastructure.repositories import MongoOrderRepository
from src.application.use_cases import ProcessOrderUseCase

router = APIRouter()

# Uma simples Factory para as Strategies
class PricingFactory:
    @staticmethod
    def get_strategy(is_weekend: bool):
        from src.domain.interfaces import PricingStrategy
        
        class WeekdayPricing(PricingStrategy):
            def calculate(self, price): return price
            
        class WeekendPricing(PricingStrategy):
            def calculate(self, price): return price * 1.5
            
        return WeekendPricing() if is_weekend else WeekdayPricing()

@router.post("/pedidos")
def criar_pedido(customer: str, price: float, weekend: bool = False):
    from src.domain.entities import Order
    
    repo = MongoOrderRepository()
    strategy = PricingFactory.get_strategy(weekend)
    use_case = ProcessOrderUseCase(repo, strategy)
    
    order = Order(id="123", customer_name=customer, items=["Pizza"], base_price=price, is_weekend=weekend)
    use_case.execute(order)
    
    return {"status": "Pedido processado", "total": order.total_price}