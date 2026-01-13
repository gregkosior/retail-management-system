import csv

def load_products(csv_path: str) -> list[dict]:
    products = []
    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": int(row["ID produktu"]),
                "name": row["Nazwa produktu"],
                "category": row["Kategoria"],
                "price_retail": float(row["Cena detaliczna (PLN)"]),
                "price_wholesale": float(row["Cena hurtowa (PLN)"]),
                "margin": float(row["Marża sklepu %"]),
                "stock": int(row["Stan magazynowy"]),
                "min_stock": int(row["Minimalny stan magazynowy"]),
                "status": row["Status produktu"],
                "supplier": row["Hurtownia dostawcza"],
            })
    return products
