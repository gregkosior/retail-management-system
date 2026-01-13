# Project: Retail Management System
# Start date: 2026-01-13
# Start time: 09:00
# Author: [Twoje imię]
#
# Description:
# Backend-first system for managing a retail store,
# warehouse stock and wholesale supply.
#
# This file is the initial single-file prototype.
# The project will be refactored into modules later.


CATEGORIES = (
    "dairy",
    "bakery",
    "beverages",
    "snacks",
    "household"
)

ORDER_STATUSES = (
    "created",
    "processed",
    "completed"
)

PRODUCTS = {
    1: {"name": "Milk", "category": "dairy", "price": 2.50},
    2: {"name": "Bread", "category": "bakery", "price": 1.80},
    3: {"name": "Butter", "category": "dairy", "price": 3.20},
    4: {"name": "Cheese", "category": "dairy", "price": 4.50},
    5: {"name": "Apple Juice", "category": "beverages", "price": 2.00},
    6: {"name": "Water", "category": "beverages", "price": 1.20},
    7: {"name": "Chips", "category": "snacks", "price": 2.80},
    8: {"name": "Chocolate", "category": "snacks", "price": 2.30},
    9: {"name": "Soap", "category": "household", "price": 1.50},
    10: {"name": "Toilet Paper", "category": "household", "price": 4.00}
}

catalog = {
    "Milk" : 1.30,
    "Bread" : 0.90,
}

class Store:
    def __init__(self, products):
        self.products = products
    def get_product_name_and_prices(self):
        product_name = []
        product_price = []
        for product, details in self.products.items():
            product_name.append(details["name"])
            product_price.append(details["price"])
        return product_name, product_price
        
    def get_products_above_price(self, min_price):
        expensive_products = []
        for product in self.products.values():
            if product["price"] > min_price:
                expensive_products.append((product["name"], product["price"]))
        return expensive_products
    



class Warehouse:
    def __init__(self):
        self.stock = {}
    def add_stock(self,product_name, quantity):
           if quantity < 0:
               raise ValueError("Quantity must be greater than zero.")
           if product_name in self.stock:
               self.stock[product_name] += quantity
           else:
               self.stock[product_name] = quantity
    def remove_stock(self,product_name, quantity):
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



if __name__ == "__main__":
    store = Store(PRODUCTS)
    warehouse = Warehouse()
    wholesale = Wholesale()

    print("Retail Management System started successfully.")
    
    names, prices = store.get_product_name_and_prices()
    print("Product Names:", names)
    print("Product Prices:", prices)
   
    expensive = store.get_products_above_price(3.00)
    for name, price in expensive:
        print(f" {name}: {price}")
        
    print("\n----Warehouse Operations----")
    warehouse.add_stock("Milk", 50)
    warehouse.add_stock("Bread", 30)
    warehouse.add_stock("Cheese", 20)
    

  
if __name__ == "__main__":

    print("=== Retail Management System ===")

    # --- INIT OBJECTS ---
    store = Store(PRODUCTS)
    warehouse = Warehouse()
    wholesale = Wholesale()

    # --- STORE OPERATIONS ---
    print("\n--- Store Products ---")
    names, prices = store.get_product_name_and_prices()
    print("Names:", names)
    print("Prices:", prices)

    print("\nProducts above price 3.00:")
    expensive_products = store.get_products_above_price(3.00)
    for name, price in expensive_products:
        print(f"- {name}: ${price:.2f}")

    # --- WAREHOUSE OPERATIONS ---
    print("\n--- Warehouse Operations ---")
    warehouse.add_stock("Milk", 50)
    warehouse.add_stock("Bread", 30)
    warehouse.add_stock("Cheese", 20)

    try:
        warehouse.remove_stock("Milk", 10)
    except (ValueError, KeyError) as error:
        print("Warehouse error:", error)

    print("\nCurrent warehouse stock:")
    for product, quantity in warehouse.get_stock_report().items():
        print(f"- {product}: {quantity} units")

    # --- WHOLESALE OPERATIONS ---
    print("\n--- Wholesale Catalog ---")
    wholesale.add_product("Milk", 1.20)
    wholesale.add_product("Bread", 0.80)
    wholesale.add_product("Cheese", 3.50)

    for product, price in wholesale.list_products().items():
        print(f"- {product}: ${price:.2f}")

    print("\n=== System finished successfully ===")

        
    
    
    
    
    

    
