
// Class to methods mapping for dynamic UI
const classMethods = {
    store: [
        { name: 'get_product_name_and_prices', label: 'Product Names & Prices' },
        { name: 'get_products_above_price', label: 'Products Above Price' }
    ],
    warehouse: [
        { name: 'get_stock_report', label: 'Stock Report' },
        { name: 'add_stock', label: 'Add Stock' },
        { name: 'remove_stock', label: 'Remove Stock' }
    ],
    wholesale: [
        { name: 'list_products', label: 'List Products' },
        { name: 'get_price', label: 'Get Price' }
    ]
};

document.addEventListener('DOMContentLoaded', () => {
    const navBtns = document.querySelectorAll('.main-btn');
    navBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            navBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            showSubmenu(btn.dataset.class);
        });
    });
});

function showSubmenu(className) {
    const submenu = document.getElementById('submenu');
    submenu.innerHTML = '';
    const methods = classMethods[className];
    if (!methods) return;
    methods.forEach(method => {
        const btn = document.createElement('button');
        btn.className = 'submenu-btn';
        btn.textContent = method.label;
        btn.onclick = () => handleMethodClick(className, method.name);
        submenu.appendChild(btn);
    });
    document.getElementById('output').innerHTML = '<em>Select an action...</em>';
}

function handleMethodClick(className, methodName) {
    if (className === 'store') {
        if (methodName === 'get_product_name_and_prices') {
            fetch('/api/store/get_product_name_and_prices')
                .then(res => res.json())
                .then(data => {
                    let html = '<b>Product Names & Prices:</b><ul>';
                    data.names.forEach((name, i) => {
                        html += `<li>${name} - ${data.prices[i]} PLN</li>`;
                    });
                    html += '</ul>';
                    showOutput(html);
                });
        } else if (methodName === 'get_products_above_price') {
            const minPrice = prompt('Show products above what price? (PLN)', '100');
            if (minPrice !== null) {
                fetch(`/api/store/get_products_above_price/${minPrice}`)
                    .then(res => res.json())
                    .then(data => {
                        let html = `<b>Products above ${minPrice} PLN:</b><ul>`;
                        data.forEach(p => {
                            html += `<li>${p.name} - ${p.price} PLN</li>`;
                        });
                        html += '</ul>';
                        showOutput(html);
                    });
            }
        }
    } else if (className === 'warehouse') {
        if (methodName === 'get_stock_report') {
            fetch('/api/warehouse/get_stock_report')
                .then(res => res.json())
                .then(data => {
                    let html = '<b>Warehouse Stock Report:</b><ul>';
                    Object.entries(data).forEach(([name, qty]) => {
                        html += `<li>${name}: ${qty} units</li>`;
                    });
                    html += '</ul>';
                    showOutput(html);
                });
        } else if (methodName === 'add_stock') {
            const product = prompt('Product name to add stock:');
            const qty = prompt('Quantity to add:');
            if (product && qty) {
                fetch(`/api/warehouse/add_stock/${encodeURIComponent(product)}/${qty}`, {method: 'POST'})
                    .then(res => res.json())
                    .then(data => {
                        if (data.success) showOutput('Stock added successfully.');
                        else showOutput('Error: ' + data.error);
                    });
            }
        } else if (methodName === 'remove_stock') {
            const product = prompt('Product name to remove stock:');
            const qty = prompt('Quantity to remove:');
            if (product && qty) {
                fetch(`/api/warehouse/remove_stock/${encodeURIComponent(product)}/${qty}`, {method: 'POST'})
                    .then(res => res.json())
                    .then(data => {
                        if (data.success) showOutput('Stock removed successfully.');
                        else showOutput('Error: ' + data.error);
                    });
            }
        }
    } else if (className === 'wholesale') {
        if (methodName === 'list_products') {
            fetch('/api/wholesale/list_products')
                .then(res => res.json())
                .then(data => {
                    let html = '<b>Wholesale Catalog:</b><ul>';
                    Object.entries(data).forEach(([name, price]) => {
                        html += `<li>${name}: ${price} PLN</li>`;
                    });
                    html += '</ul>';
                    showOutput(html);
                });
        } else if (methodName === 'get_price') {
            const product = prompt('Product name to get price:');
            if (product) {
                fetch(`/api/wholesale/get_price/${encodeURIComponent(product)}`)
                    .then(res => res.json())
                    .then(data => {
                        if (data.price !== undefined) showOutput(`${product}: ${data.price} PLN`);
                        else showOutput('Error: ' + data.error);
                    });
            }
        }
    }
}

function showOutput(html) {
    document.getElementById('output').innerHTML = html;
}
