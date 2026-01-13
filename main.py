from pathlib import Path

from csv_loader import load_products
from Entry_Point.store import Store
from Entry_Point.warehouse import Warehouse
from Entry_Point.wholesale import Wholesale


def main():
    print("=== Retail Management System ===")

    # --- CSV PATH ---
    BASE_DIR = Path(__file__).resolve().parent
    CSV_PATH = BASE_DIR / "data" / "produkty_sklep_rozszerzone.csv"

    # --- LOAD DATA ---
    products = load_products(str(CSV_PATH))
    print(f"Loaded {len(products)} products from CSV")

    # Convert products list to dict for Store (by id)
    products_dict = {p["id"]: p for p in products}

    # --- INIT OBJECTS ---
    store = Store(products_dict)
    warehouse = Warehouse()
    wholesale = Wholesale()

    # Fill warehouse and wholesale with products
    for product in products:
        warehouse.add_stock(product["name"], product["stock"])
        wholesale.add_product(product["name"], product["price_wholesale"])

    print("\n--- Store: Products above price 100 ---")
    expensive_products = store.get_products_above_price(100)
    for name, price in expensive_products:
        print(f"{name} - {price} PLN")

    print("\n--- Warehouse Stock Report ---")
    stock = warehouse.get_stock_report()
    for name, quantity in stock.items():
        print(f"{name}: {quantity} units")

    print("\n--- Wholesale Catalog ---")
    catalog = wholesale.list_products()
    for name, price in catalog.items():
        print(f"{name}: {price} PLN")

    print("\nSystem finished successfully.")


if __name__ == "__main__":
    main()
