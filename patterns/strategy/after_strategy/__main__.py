from order import Order
from shipping_cost import ShippingCost

def fedex_strategy():
    return 3.0

def ups_strategy():
    return 4.0

def new_strategy():
    return 10.0

# Test Fedex shipping

order = Order()
strategy = fedex_strategy
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0


# Test Fedex shipping

order = Order()
strategy = ups_strategy
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

# Test Fedex shipping

order = Order()
strategy = new_strategy
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 10.0