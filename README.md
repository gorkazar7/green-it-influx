# 🌿 Sistema de Auditoría Green IT: Análisis Comparativo de APIs

Este proyecto implementa una arquitectura de Ingeniería de Software
Sostenible para medir, comparar y visualizar el consumo energético de
microservicios.

A diferencia de soluciones simples, este sistema permite comparar la
eficiencia energética de distintos algoritmos (ej. Álgebra Lineal vs
Criptografía) dentro de una misma API, guardando un histórico detallado.

## 🏗️ Arquitectura del Sistema

-   **FastAPI App:** Microservicio con endpoints de distinta naturaleza
    computacional.
-   **Test Driven Audit:** Usamos pytest para generar carga realista. No
    medimos la API en reposo, medimos su respuesta bajo estrés.
-   **Eco-Runner Universal:** Un wrapper agnóstico que envuelve la
    ejecución de los tests con CodeCarbon e inyecta metadatos (tags) a
    la base de datos.
-   **Persistencia:** Los datos se envían a InfluxDB (Cloud o Local).
-   **Visualización:** Dashboards en Grafana para comparar tendencias.

## 📂 Estructura del Proyecto

    MI-PROYECTO/
    │
    ├── .github/workflows/
    │   └── eco-pipeline.yml     <-- Pipeline de Auditoría Dual
    │
    ├── api.py                   <-- App FastAPI con endpoints Heavy
    ├── tests/
    │   └── test_api.py          <-- Tests de Carga (Pytest)
    │
    ├── monitoring/              <-- Infraestructura Local (Opcional)
    │   └── docker-compose.yml   <-- Stack InfluxDB + Grafana
    │
    ├── requirements.txt         <-- Dependencias (FastAPI, CodeCarbon...)
    └── README.md

**Nota:** El script `emissions_runner_api.py` (el motor de auditoría) se
descarga dinámicamente en el pipeline desde el repositorio central
**eco-utils** para mantener este código limpio.

## 🚀 Guía de Puesta en Marcha

### 1. Requisitos Previos

Necesitas una instancia de InfluxDB. Puedes usar la versión Cloud
(gratuita) o levantarla en local:


``` bash
cd monitoring
docker-compose up -d
```

-   **InfluxDB:** http://localhost:8086\
-   **Grafana:** http://localhost:3000

### 2. Configuración de Secretos (GitHub)

Ve a **Settings → Secrets** en tu repositorio y añade:

  ------------------------------------------------------------------------------------------------------------
  Secreto                 Descripción                        Ejemplo
  ----------------------- ---------------------------------- -------------------------------------------------
  INFLUXDB_URL            URL de la API de Influx            `https://us-east-1-1.aws.cloud2.influxdata.com` o
                                                             `https://tudominio-ngrok.com`

  INFLUXDB_TOKEN          Token de Escritura                 `mzDnVmtj8dLOuE1Oo...`
  ------------------------------------------------------------------------------------------------------------

### 3. Configuración del Pipeline

El archivo `eco-api-pipeline.yml` ya está configurado para enviar los datos
al Bucket `greenit` y Organización `Dev Team`.\
Si cambias estos nombres en InfluxDB, actualízalos en el YAML.

## 📊 Cómo interpretar los resultados

### En GitHub Actions (Inmediato)

Al finalizar cada push, verás un **Resumen de Trabajo (Job Summary)**
con una tabla comparativa:

  Endpoint      CO2 (kg)     Energía (kWh)   Duración (s)
  ------------- ------------ --------------- --------------
  Matrices 🧮   0.00001523   0.00004123      5.21
  Cripto 🔐     0.00002891   0.00009122      8.45

Esto te permite ver rápidamente si tu nueva implementación de hashing es
más eficiente que la anterior.

### En Grafana (Histórico)

Para ver la evolución temporal, crea un panel con esta consulta
**Flux**:

``` flux
from(bucket: "greenit")
  |> range(start: -30d)
  |> filter(fn: (r) => r["_measurement"] == "carbon_footprint")
  |> filter(fn: (r) => r["endpoint"] == "matrix_mult" or r["endpoint"] == "crypto_hash")
  |> group(columns: ["endpoint"])
  |> aggregateWindow(every: 1d, fn: mean, createEmpty: false)
```

Esto generará un gráfico de líneas donde podrás comparar cómo evoluciona
el consumo de cada parte de tu sistema por separado.