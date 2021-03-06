from shipper import Shipper


class ShippingCost:
    def shipping_cost(self, order):
        if order.shipper == Shipper.fedex:
            return self._fedex_cost(order)
        elif order.shipper == Shipper.ups:
            return self._ups_cost(order)
        elif order.shipper == Shipper.postal:
            return self._postal_cost(order)
        else:
            raise ValueError(f"Invalid shipper {order.shipper}")


    def _fedex_cost(self, order):
        return 3.0

    def _ups_cost(self, order):
        return 4.0

    def _postal_cost(self, order):
        return 5.0