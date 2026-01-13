
import sys
import os
from flask import Flask, jsonify, send_from_directory
from pathlib import Path

# Add parent directory to sys.path for imports
sys.path.append(str(Path(__file__).resolve().parent.parent))

from csv_loader import load_products
from Entry_Point.store import Store
from Entry_Point.warehouse import Warehouse
from Entry_Point.wholesale import Wholesale

app = Flask(__name__, static_folder='static')

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "produkty_sklep_rozszerzone.csv"

# --- LOAD DATA ---
products = load_products(str(CSV_PATH))
store = Store(products)
warehouse = Warehouse()
wholesale = Wholesale()

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


# --- Store endpoints ---
@app.route('/api/store/get_product_name_and_prices')
def api_store_get_product_name_and_prices():
    names, prices = store.get_product_name_and_prices()
    return jsonify({"names": names, "prices": prices})

@app.route('/api/store/get_products_above_price/<float:min_price>')
def api_store_get_products_above_price(min_price):
    result = store.get_products_above_price(min_price)
    return jsonify([{"name": name, "price": price} for name, price in result])

# --- Warehouse endpoints ---
@app.route('/api/warehouse/get_stock_report')
def api_warehouse_get_stock_report():
    return jsonify(warehouse.get_stock_report())

@app.route('/api/warehouse/add_stock/<product_name>/<int:quantity>', methods=['POST'])
def api_warehouse_add_stock(product_name, quantity):
    try:
        warehouse.add_stock(product_name, quantity)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route('/api/warehouse/remove_stock/<product_name>/<int:quantity>', methods=['POST'])
def api_warehouse_remove_stock(product_name, quantity):
    try:
        warehouse.remove_stock(product_name, quantity)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

# --- Wholesale endpoints ---
@app.route('/api/wholesale/list_products')
def api_wholesale_list_products():
    return jsonify(wholesale.list_products())

@app.route('/api/wholesale/get_price/<product_name>')
def api_wholesale_get_price(product_name):
    try:
        price = wholesale.get_price(product_name)
        return jsonify({"price": price})
    except Exception as e:
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
