import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
data = pd.read_csv('fast_food_sales.csv')

# Nombre de ventes de burgers par type
burger_sales = data[data['category'] == 'burger'].groupby('item')['sales'].sum()
burger_sales.plot(kind='bar')
plt.title('Nombre de ventes de burgers par type')
plt.xlabel('Type de burger')
plt.ylabel('Nombre de ventes')
plt.show()

# Nombre de ventes de boissons par type
drink_sales = data[data['category'] == 'drink'].groupby('item')['sales'].sum()
drink_sales.plot(kind='bar')
plt.title('Nombre de ventes de boissons par type')
plt.xlabel('Type de boisson')
plt.ylabel('Nombre de ventes')
plt.show()

# Chiffre d'affaires par mois
data['month'] = pd.to_datetime(data['date']).dt.month
monthly_revenue = data.groupby('month')['revenue'].sum()
monthly_revenue.plot(kind='line')
plt.title('Chiffre d\'affaires par mois')
plt.xlabel('Mois')
plt.ylabel('Chiffre d\'affaires')
plt.show()