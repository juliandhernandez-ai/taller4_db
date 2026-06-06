
# Taller 4 – APIs Públicas, MongoDB y EDA

## Descripción

Este proyecto fue desarrollado para el curso **Bases de Datos para Ciencia de Datos**.

El objetivo consiste en implementar un flujo básico de Ciencia de Datos mediante tres etapas fundamentales:

1. Extracción de información desde una API pública.
2. Almacenamiento de datos crudos (RAW) en MongoDB.
3. Procesamiento y Análisis Exploratorio de Datos (EDA) utilizando Python y Pandas.

Para el desarrollo del taller se seleccionó la API pública de Rick & Morty debido a su facilidad de uso, disponibilidad de datos y estructura JSON adecuada para análisis de datos.

---

# Objetivos del Proyecto

* Consumir datos desde una API REST pública.
* Descargar más de 100 registros.
* Almacenar los datos sin modificar en MongoDB.
* Construir un DataFrame para análisis exploratorio.
* Generar estadísticas descriptivas e insights relevantes.
* Elaborar visualizaciones que permitan interpretar los datos.

---

# API Seleccionada

Se utilizó la API pública de Rick & Morty:

https://rickandmortyapi.com/

La API proporciona información detallada sobre los personajes de la serie, incluyendo:

* Nombre
* Estado
* Especie
* Género
* Origen
* Ubicación actual
* Episodios en los que aparece

---

# Tecnologías Utilizadas

* Python 3.10+
* Requests
* PyMongo
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook
* MongoDB Atlas
* Python Dotenv

---

# Estructura del Proyecto

```text
TALLER4_RICKMORTY_MONGODB
│
├── etl/
│   ├── common/
│   │   ├── config.py
│   │   └── db.py
│   │
│   ├── extract/
│   │   └── extract.py
│   │
│   ├── load/
│   │   └── load.py
│   │
│   └── transform/
│       └── transform.py
│
├── analisis.ipynb
├── main.py
├── requirements.txt
├── .env
├── .env.example
├── README.md
└── .gitignore
```

---

# Instalación

## 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd TALLER4_RICKMORTY_MONGODB
```

## 2. Crear entorno virtual

```bash
python -m venv venv
```

## 3. Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Dependencias Utilizadas

El archivo requirements.txt contiene las librerías necesarias para ejecutar el proyecto.

Principales dependencias:

```text
requests
pymongo
pandas
matplotlib
seaborn
jupyter
python-dotenv
```

---

# Configuración de MongoDB

## Uso de Variables de Entorno

Por razones de seguridad, la URI de conexión a MongoDB no está escrita directamente dentro del código fuente.

La conexión se realiza mediante variables de entorno utilizando la librería `python-dotenv`.

Esto evita exponer credenciales sensibles dentro del repositorio de GitHub.

---

## Crear archivo .env

En la raíz del proyecto crear un archivo llamado:

```text
.env
```

Con el siguiente contenido:

```env
MONGO_URI=mongodb+srv://usuario:password@cluster.mongodb.net/
```

Debe reemplazarse:

* usuario
* password
* cluster.mongodb.net

por los datos reales de la cuenta MongoDB Atlas.

---

## ¿Cómo se obtiene la URI?

Dentro del código se utiliza:

```python
from dotenv import load_dotenv
import os

load_dotenv()

URI = os.getenv("MONGO_URI")
```

La URI es cargada dinámicamente desde el archivo `.env`.

De esta manera:

* Las credenciales no quedan visibles en GitHub.
* Se siguen buenas prácticas de seguridad.
* El código es reutilizable en diferentes entornos.

---

## Archivo .env.example

El proyecto incluye un archivo:

```text
.env.example
```

que sirve como plantilla para que otros usuarios configuren su propia conexión sin modificar el código fuente.

Ejemplo:

```env
MONGO_URI=TU_URI_AQUI
```

---

# Ejecución del Proyecto

Una vez configurado MongoDB Atlas y activado el entorno virtual, ejecutar:

```bash
python main.py
```

---

# Fase 1: Extracción de Datos

Durante esta etapa se consume la API de Rick & Morty mediante peticiones HTTP utilizando la librería Requests.

El proceso:

1. Consulta la API.
2. Descarga los personajes página por página.
3. Acumula los registros en memoria.
4. Continúa hasta superar los 100 registros mínimos solicitados.

La extracción implementada descarga aproximadamente 120 personajes.

Ejemplo de salida:

```text
--- FASE 1: EXTRACCIÓN DE DATOS ---
Descargando datos desde:
https://rickandmortyapi.com/api/character

Descargando datos desde:
https://rickandmortyapi.com/api/character?page=2

...

Extracción completada.
Total descargados: 120 personajes.
```

---

# Fase 2: Almacenamiento en MongoDB

Una vez descargados los datos:

1. Se establece conexión con MongoDB Atlas.
2. Se crea la base de datos:

```text
taller4_db
```

3. Se crea la colección:

```text
raw_data
```

4. Se eliminan registros antiguos.
5. Se insertan nuevamente todos los documentos.

Los datos se almacenan exactamente como son recibidos desde la API, sin modificaciones.

Esto cumple con el requisito de almacenamiento RAW solicitado en el taller.

---

# Base de Datos

## Nombre

```text
taller4_db
```

## Colección

```text
raw_data
```

## Tipo de almacenamiento

JSON crudo proveniente directamente de la API.

---

# Fase 3: Análisis Exploratorio de Datos (EDA)

El análisis se desarrolla en:

```text
analisis.ipynb
```

Desde MongoDB se recuperan los documentos almacenados y se construye un DataFrame de Pandas.

Variables seleccionadas:

* name
* status
* species
* gender
* origin
* episode_count

---

# Actividades de EDA

## Inspección Básica

* Visualización de registros mediante head().
* Verificación de tipos de datos mediante info().
* Identificación de valores nulos.

## Estadísticas e Insights

Se calculan métricas relevantes como:

* Cantidad de personajes por estado.
* Cantidad de personajes por especie.
* Distribución por género.
* Personaje con más apariciones.
* Promedio de episodios por personaje.

## Visualización

Se generan tres gráficos:

### 1. Gráfico de Torta

Distribución porcentual por género.

### 2. Gráfico de Barras

Frecuencia de especies.

### 3. Histograma

Distribución de apariciones en episodios.

---

# Resultados Esperados

* Más de 100 personajes descargados.
* Base de datos MongoDB creada correctamente.
* Colección raw_data poblada con datos RAW.
* DataFrame construido exitosamente.
* Obtención de insights relevantes.
* Generación de visualizaciones interpretables.

---

# Evidencias Incluidas

Para la entrega final se anexan capturas de:

* MongoDB Atlas mostrando la colección creada.
* Conteo de documentos almacenados.
* Ejecución de la extracción.
* Notebook ejecutado.
* Gráfico de torta.
* Gráfico de barras.
* Histograma.
* Resultados de los insights obtenidos.

---

# Autor

Julian

Curso: Bases de Datos para Ciencia de Datos

Universidad de Antioquia

Docente: Miguel Ramos García

