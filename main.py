import time
import math


def logica_de_negocio():
    """
    Esta es tu aplicación real.
    Ya no tiene importaciones de 'codecarbon' ni lógica extraña.
    """
    print("--- 🚀 Arrancando Proyecto 1 (Clean Code) ---")

    # Simulamos carga de trabajo
    size = 15000
    print(f"Procesando {size} elementos complejos...")

    # Carga CPU
    data = [math.sqrt(i) * math.tan(i) for i in range(size)]

    # Simulamos espera de base de datos o API
    time.sleep(2)

    print(f"--- ✅ Proyecto 1 Terminado Exitosamente ---")


if __name__ == "__main__":
    logica_de_negocio()