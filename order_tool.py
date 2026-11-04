# order_tool.py
# Author: aevlin


class OrderLookup:
    """A tool that knows about orders."""

    def __init__(self, orders):
        # Save the orders dictionary.
        self.orders = orders

    def find_order_id(self, text):
        # Search the message for a known order ID.
        for order_id in self.orders:
            if order_id in text.upper():
                return order_id

        # Return None if no matching order is found.
        return None

    def find_status(self, order_id):
        # Check whether the order exists.
        if order_id in self.orders:
            return self.orders[order_id]

        # Return None if the order is unknown.
        return None
