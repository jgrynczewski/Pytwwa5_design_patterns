from order import Order
from shipper import Shipper
from shipping_cost import ShippingCost

# Test Fedex shipping

order = Order(Shipper.fedex)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

# Test UPC shipping

order = Order(Shipper.upc)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

# Test Postal shipping

order = Order(Shipper.postal)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0