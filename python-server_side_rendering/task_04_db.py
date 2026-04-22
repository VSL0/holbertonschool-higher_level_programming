import sqlite3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except:
        return []

def read_csv(filename):
    products = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except:
        pass
    return products

def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append(dict(row))
        conn.close()
    except sqlite3.Error:
        return None
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")
    
    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    elif source == 'sql':
        data = read_sql()
        if data is None:
            return render_template('product_display.html', error="Database error")
    
    if product_id:
        try:
            target_id = int(product_id)
            filtered_data = [p for p in data if p['id'] == target_id]
            if not filtered_data:
                return render_template('product_display.html', error="Product not found")
            data = filtered_data
        except (ValueError, TypeError):
            return render_template('product_display.html', error="Product not found")
            
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
