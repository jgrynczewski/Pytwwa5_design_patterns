from order import Order
from shipping_cost import ShippingCost


# Test Fedex shipping

order = Order()
cost_calculator = ShippingCost(lambda order: 3.0)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0


# Test Fedex shipping

order = Order()
cost_calculator = ShippingCost(lambda order: 4.0)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

# Test Fedex shipping

order = Order()
cost_calculator = ShippingCost(lambda order: 10)
cost = cost_calculator.shipping_cost(order)
assert cost == 10.0