# Retail Management System

A full-stack **Retail Management System** built in Python, focused on real-world business logic such as store operations, warehouse stock control, and wholesale integration.

The project was designed with **clean architecture**, modular backend structure, and a simple web-based frontend consuming backend logic.

---

## 🚀 Features

### Store
- Display product names and prices
- Filter products above a given price
- CSV-based product data loading

### Warehouse
- Stock report
- Add stock
- Remove stock
- Minimum stock threshold logic (ready for automation)

### Wholesale
- Supplier catalog
- Wholesale prices
- Backend-ready for auto-reorder logic

### Frontend
- Web UI with buttons mapped to backend classes and methods
- Dynamic rendering of store, warehouse, and wholesale data
- Backend logic reused without modification

---

## 🧠 Architecture

Retail-Management-System/
├── App/
│ ├── store.py
│ ├── warehouse.py
│ ├── wholesale.py
│ ├── csv_loader.py
│
├── data/
│ └── produkty_sklep_rozszerzone.csv
│
├── frontend/
│ ├── index.html
│ ├── app.js
│ └── style.css
│
├── app.py # Backend + frontend server
├── main.py # CLI / entry point
└── README.md

yaml
Skopiuj kod

---

## 📦 Technologies

- Python 3.11
- CSV data processing
- Modular backend architecture
- HTML / CSS / JavaScript (frontend)
- Flask-style routing (local server)

---

## ▶️ How to run

### 1. Clone repository
```bash
git clone https://github.com/your-username/retail-management-system.git
cd retail-management-system
2. Run backend
bash
Skopiuj kod
python app.py
3. Open browser
cpp
Skopiuj kod
http://127.0.0.1:5000
📈 Future Improvements
Database integration (SQLite / PostgreSQL)

Authentication & roles

Auto-reorder logic using AI

REST API separation

Dashboard charts & analytics
