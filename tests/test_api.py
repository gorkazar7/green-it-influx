from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_matrix_load():
    """
    Carga específica para el endpoint de Matrices.
    Se repetirá 30 veces para generar huella medible.
    """
    print("\n🧮 Testeando Matrices...")
    for _ in range(30):
        response = client.get("/heavy-matrix")
        assert response.status_code == 200

def test_crypto_load():
    """
    Carga específica para el endpoint de Criptografía.
    Se repetirá 50 veces porque el hashing es muy rápido.
    """
    print("\n🔐 Testeando Criptografía...")
    for _ in range(50):
        response = client.get("/heavy-crypto")
        assert response.status_code == 200