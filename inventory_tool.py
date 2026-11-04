# inventory_tool.py
# Exercise 3 - Inventory Lookup Tool


class InventoryLookup:
    """A tool that checks product inventory."""

    def __init__(self, inventory):
        # Save the inventory dictionary.
        self.inventory = inventory

    def find_product(self, text):
        """Find a known product mentioned in a message."""
        for product in self.inventory:
            if product.lower() in text.lower():
                return product
        return None

    def count_for(self, product):
        """Return the stock count or None if unknown."""
        if product in self.inventory:
            return self.inventory[product]
        return None
