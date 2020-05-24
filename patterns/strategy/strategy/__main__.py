from order import Order
from shipping_cost import ShippingCost
from fedex_strategy import FedexStrategy
from ups_strategy import UpsStrategy
from new_strategy import NewStrategy

# Test Fedex shipping

order = Order()
strategy = FedexStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0


# Test Fedex shipping

order = Order()
strategy = UpsStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

# Test Fedex shipping

order = Order()
strategy = NewStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 10.0