from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json_file():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv_file():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products_list = read_json_file()
    elif source == 'csv':
        products_list = read_csv_file()
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error='Product not found')

        filtered_products = []
        for product in products_list:
            if product.get('id') == product_id:
                filtered_products.append(product)

        if not filtered_products:
            return render_template('product_display.html', error='Product not found')

        return render_template('product_display.html', products=filtered_products)

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
