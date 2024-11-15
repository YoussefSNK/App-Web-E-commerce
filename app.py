from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

try:
    # Charger les données
    data = pd.read_csv('fast_food_sales.csv')
except Exception as e:
    print(f"Error loading CSV file: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/burger_sales')
def get_burger_sales():
    try:
        burger_sales = data[data['category'] == 'burger'].groupby('item')['sales'].sum().to_dict()
        return jsonify(burger_sales)
    except Exception as e:
        print(f"Error in get_burger_sales: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/api/drink_sales')
def get_drink_sales():
    try:
        drink_sales = data[data['category'] == 'drink'].groupby('item')['sales'].sum().to_dict()
        return jsonify(drink_sales)
    except Exception as e:
        print(f"Error in get_drink_sales: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/api/monthly_revenue')
def get_monthly_revenue():
    try:
        data['month'] = pd.to_datetime(data['date']).dt.month
        monthly_revenue = data.groupby('month')['revenue'].sum().to_dict()
        return jsonify(monthly_revenue)
    except Exception as e:
        print(f"Error in get_monthly_revenue: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)