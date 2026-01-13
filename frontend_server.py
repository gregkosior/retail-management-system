from flask import Flask, jsonify, send_from_directory
from pathlib import Path
from csv_loader import load_products
from Entry_Point.store import Store
from Entry_Point.warehouse import Warehouse
from Entry_Point.wholesale import Wholesale

app = Flask(__name__, static_folder='frontend')

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "produkty_sklep_rozszerzone.csv"

# --- LOAD DATA ---
products = load_products(str(CSV_PATH))
store = Store(products)
warehouse = Warehouse()
wholesale = Wholesale()

# Populate warehouse and wholesale with products
def populate_backend():
    for product in products:
        warehouse.add_stock(product['name'], product['stock'])
        wholesale.add_product(product['name'], product['price_wholesale'])

populate_backend()

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/store/products_above_100')
def api_store_products():
    result = [p for p in products if p['price_retail'] > 100]
    return jsonify(result)

@app.route('/api/warehouse/stock')
def api_warehouse_stock():
    return jsonify(warehouse.get_stock_report())

@app.route('/api/wholesale/catalog')
def api_wholesale_catalog():
    return jsonify(wholesale.list_products())

if __name__ == '__main__':
    app.run(debug=True)
