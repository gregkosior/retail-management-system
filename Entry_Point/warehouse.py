class Warehouse:
    def __init__(self):
        self.stock = {}

    def add_stock(self, product_name, quantity):
        if quantity < 0:
            raise ValueError("Quantity must be greater than zero.")
        if product_name in self.stock:
            self.stock[product_name] += quantity
        else:
            self.stock[product_name] = quantity

    def remove_stock(self, product_name, quantity):
        if product_name not in self.stock:
            raise KeyError("Product not found in warehouse.")
        if quantity > self.stock[product_name]:
            raise ValueError("Not enough stock available.")
        self.stock[product_name] -= quantity

    def get_stock_report(self):
        return self.stock

    def check_and_reorder(self, product_name, threshold, wholesale, reorder_amount=50):
        quantity = self.stock.get(product_name, 0)
        if quantity < threshold:
            try:
                price = wholesale.get_price(product_name)
                self.add_stock(product_name, reorder_amount)
                print(f"Auto-order: {product_name} x {reorder_amount} from wholesale at {price}")
            except KeyError:
                print(f"Auto-order failed: {product_name} not in wholesale")
