// Fetch and display data from backend endpoints (to be implemented)

document.addEventListener('DOMContentLoaded', () => {
    fetchStoreProducts();
    fetchWarehouseStock();
    fetchWholesaleCatalog();
});

function fetchStoreProducts() {
    fetch('/api/store/products_above_100')
        .then(res => res.json())
        .then(data => {
            const ul = document.getElementById('store-products');
            ul.innerHTML = '';
            data.forEach(product => {
                const li = document.createElement('li');
                li.textContent = `${product.name} - ${product.price_retail} PLN`;
                ul.appendChild(li);
            });
        });
}

function fetchWarehouseStock() {
    fetch('/api/warehouse/stock')
        .then(res => res.json())
        .then(data => {
            const ul = document.getElementById('warehouse-stock');
            ul.innerHTML = '';
            Object.entries(data).forEach(([name, quantity]) => {
                const li = document.createElement('li');
                li.textContent = `${name}: ${quantity} units`;
                ul.appendChild(li);
            });
        });
}

function fetchWholesaleCatalog() {
    fetch('/api/wholesale/catalog')
        .then(res => res.json())
        .then(data => {
            const ul = document.getElementById('wholesale-catalog');
            ul.innerHTML = '';
            Object.entries(data).forEach(([name, price]) => {
                const li = document.createElement('li');
                li.textContent = `${name}: ${price} PLN`;
                ul.appendChild(li);
            });
        });
}
