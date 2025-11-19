from fastapi import FastAPI
import math
import hashlib
import random

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "Ready"}


@app.get("/heavy-matrix")
def matrix_operations():
    """
    ENDPOINT 1: Simula operaciones de álgebra lineal.
    Multiplicación de matrices (CPU + Memoria intensiva).
    """
    size = 150
    # Crear dos matrices aleatorias
    matrix_a = [[random.random() for _ in range(size)] for _ in range(size)]
    matrix_b = [[random.random() for _ in range(size)] for _ in range(size)]

    # Multiplicación simple O(n^3) para generar carga
    result = [[sum(a * b for a, b in zip(row_a, col_b))
               for col_b in zip(*matrix_b)]
              for row_a in matrix_a]

    return {"task": "matrix_mult", "elements": size * size}


@app.get("/heavy-crypto")
def crypto_mining():
    """
    ENDPOINT 2: Simula minería o hashing de contraseñas.
    Pura carga de CPU aritmética.
    """
    block_data = "GreenIT_Transaction_" + str(random.random())
    difficulty = 4  # Dificultad artificial

    # Hashing repetitivo (PBKDF2 style simulation)
    current_hash = block_data
    for _ in range(5000):
        current_hash = hashlib.sha256(current_hash.encode()).hexdigest()

    return {"task": "crypto_hash", "last_hash": current_hash[:10]}