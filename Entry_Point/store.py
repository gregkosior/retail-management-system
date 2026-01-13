class Store:
    def __init__(self, products):
        self.products = products

    def get_product_name_and_prices(self):
        product_name = []
        product_price = []
        for product in self.products.values():
            product_name.append(product["name"])
            product_price.append(product["price_retail"])
        return product_name, product_price

    def get_products_above_price(self, min_price):
        expensive_products = []
        for product in self.products.values():
            if product["price_retail"] > min_price:
                expensive_products.append((product["name"], product["price_retail"]))
        return expensive_products
