# Sistema Profesional de Auditoría Green IT

Este repositorio implementa una arquitectura completa para medir,
auditar y visualizar la huella de carbono de tu software (**Green
Software Engineering**).

Combina auditoría inmediata en GitHub Actions con persistencia histórica
en bases de datos de series temporales.

------------------------------------------------------------------------

## 🏗️ Arquitectura

-   **GitHub Actions:** Ejecuta el código cada vez que haces push.\
-   **Eco-Runner:** Script intermedio que envuelve tu app con
    CodeCarbon.\
-   **InfluxDB:** Base de datos donde se guarda el histórico (commit a
    commit).\
-   **Grafana:** Dashboards para ver la evolución del consumo energético
    en el tiempo.

------------------------------------------------------------------------

## 📂 Estructura del Proyecto

    MI-PROYECTO/
    │
    ├── .github/workflows/
    │   └── eco-pipeline.yml     <-- Automatización CI/CD
    │
    ├── monitoring/              <-- Infraestructura de datos
    │   └── docker-compose.yml   <-- Stack InfluxDB + Grafana
    │
    ├── main.py                  <-- Tu aplicación (Clean Code)
    └── README.md

**Nota:** El script de auditoría (`emissions_runner.py`) se descarga
automáticamente desde un repositorio central de herramientas
(`eco-utils`) para no ensuciar este proyecto.

------------------------------------------------------------------------

## 🚀 Guía de Puesta en Marcha

### **Paso 1: Levantar Infraestructura de Monitoreo (Local o Servidor)**

Si no usas InfluxDB Cloud, levanta tu propio servidor de métricas:

    cd monitoring
    docker-compose up -d

-   **InfluxDB:** http://localhost:8086\
-   **Grafana:** http://localhost:3000\
    (User: admin / Pass: admin)

------------------------------------------------------------------------

### **Paso 2: Configurar Secretos en GitHub**

Para que GitHub pueda enviar los datos a tu base de datos, configura
estos **Secrets**:

#### `INFLUXDB_URL`

-   Local: ejecuta `ngrok http 8086` y usa la URL HTTPS generada.\
-   Cloud: usa la URL proporcionada por InfluxData.

#### `INFLUXDB_TOKEN`

-   Local: toma el valor de `DOCKER_INFLUXDB_INIT_ADMIN_TOKEN` del
    docker-compose.

------------------------------------------------------------------------

## 📊 Visualización

### **1. GitHub Actions (inmediato)**

En la pestaña *Actions* verás un **Job Summary** con la medición del
último commit.

### **2. Grafana (histórico)**

Añade InfluxDB como Data Source (Flux) y usa:

``` flux
from(bucket: "eco-metrics")
  |> range(start: -30d)
  |> filter(fn: (r) => r["_measurement"] == "carbon_footprint")
```

------------------------------------------------------------------------