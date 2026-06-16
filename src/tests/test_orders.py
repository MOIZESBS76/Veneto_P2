import pytest
from src.domain.entities import Order
from src.api.routes import PricingFactory

def test_deve_calcular_preco_padrao_em_dia_util():
    """TDD: Garante que em dias úteis o preço não tenha acréscimo"""
    base_price = 100.0
    strategy = PricingFactory.get_strategy(is_weekend=False)
    
    total = strategy.calculate(base_price)
    
    assert total == 100.0

def test_deve_aplicar_acrescimo_de_50_por_cento_no_final_de_semana():
    """TDD: Garante que a Strategy de final de semana aplique os 50% extras"""
    base_price = 100.0
    strategy = PricingFactory.get_strategy(is_weekend=True)
    
    total = strategy.calculate(base_price)
    
    assert total == 150.0

def test_criacao_de_entidade_pedido():
    """Verifica se a entidade Order está sendo instanciada corretamente"""
    pedido = Order(id="1", customer_name="Moizes", items=["Pizza"], base_price=80.0)
    
    assert pedido.customer_name == "Moizes"
    assert pedido.base_price == 80.0