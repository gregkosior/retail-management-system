class Wholesale:
    def __init__(self):
        self.catalog = {}

    def add_product(self, product_name, price):
        if price < 0:
            raise ValueError("Wholesale price must be positive.")
        self.catalog[product_name] = price

    def get_price(self, product_name):
        if product_name not in self.catalog:
            raise KeyError("Product not available in wholesale.")
        return self.catalog[product_name]

    def list_products(self):
        return self.catalog.copy()
