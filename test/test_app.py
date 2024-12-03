import pytest
from app import app  # Importez l'application Flask depuis votre fichier principal

@pytest.fixture
def client():
    """Fixture pour configurer un client de test Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Tester si la route principale renvoie un statut 200 et un contenu HTML."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"<html" in response.data  # Vérifie qu'il renvoie du HTML

def test_burger_sales_endpoint(client):
    """Tester si l'endpoint /api/burger_sales renvoie les ventes de burgers."""
    response = client.get('/api/burger_sales')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)  # Vérifie que les données sont un dictionnaire
    assert all(isinstance(key, str) and isinstance(value, (int, float)) for key, value in data.items())

def test_drink_sales_endpoint(client):
    """Tester si l'endpoint /api/drink_sales renvoie les ventes de boissons."""
    response = client.get('/api/drink_sales')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)  # Vérifie que les données sont un dictionnaire
    assert all(isinstance(key, str) and isinstance(value, (int, float)) for key, value in data.items())

def test_monthly_revenue_endpoint(client):
    """Tester si l'endpoint /api/monthly_revenue renvoie le revenu mensuel."""
    response = client.get('/api/monthly_revenue')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)  # Vérifie que les données sont un dictionnaire
    assert all(isinstance(key, str) and isinstance(value, (int, float)) for key, value in data.items())

def test_category_sales_endpoint(client):
    """Tester si l'endpoint /api/category_sales renvoie les ventes par catégorie."""
    response = client.get('/api/category_sales')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)  # Vérifie que les données sont un dictionnaire
    assert all(isinstance(key, str) and isinstance(value, (int, float)) for key, value in data.items())

def test_invalid_endpoint(client):
    """Tester un endpoint non existant pour vérifier la gestion des erreurs 404."""
    response = client.get('/api/invalid_endpoint')
    assert response.status_code == 404
