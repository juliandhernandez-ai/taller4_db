import os
import requests
from pymongo import MongoClient
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def extraer_datos_api():
    print("--- FASE 1: EXTRACCIÓN DE DATOS ---")
    url_actual = "https://rickandmortyapi.com/api/character"
    todos_los_personajes = []
    
    # La API entrega 20 registros por página. Iteramos hasta superar el mínimo de 100 requeridos.
    while url_actual and len(todos_los_personajes) < 120:
        print(f"Descargando datos desde: {url_actual}")
        respuesta = requests.get(url_actual)
        
        if respuesta.status_code == 200:
            datos = respuesta.json()
            # Añadimos los personajes de la página actual a nuestra lista acumulativa
            todos_los_personajes.extend(datos["results"])
            # Avanzamos a la siguiente página de la API
            url_actual = datos["info"]["next"]
        else:
            print(f"❌ Error al consultar la API: {respuesta.status_code}")
            break
            
    print(f"✅ Extracción completada. Total descargados: {len(todos_los_personajes)} personajes.\n")
    return todos_los_personajes

def guardar_en_mongodb(datos_crudos):
    print("--- FASE 2: GUARDADO EN MONGODB ---")
    if not datos_crudos:
        print("❌ Error: No hay datos disponibles para guardar.")
        return

    try:
        # Recuperar la URI de conexión guardada de forma segura en el archivo .env
        URI = os.getenv("MONGO_URI")
        
        if not URI:
            raise ValueError("No se encontró la variable 'MONGO_URI' configurada en el archivo .env")
        
        # Inicializar el cliente de MongoDB
        cliente = MongoClient(URI, serverSelectionTimeoutMS=5000)
        
        # Configurar la Base de Datos y Colección con los nombres oficiales de la rúbrica
        db = cliente["taller4_db"]
        coleccion = db["raw_data"]
        
        # 1. LIMPIEZA: Vaciar la colección si ya contiene registros previos
        print("Limpiando registros antiguos de la colección...")
        resultado_borrado = coleccion.delete_many({})
        print(f"🗑️ Se eliminaron {resultado_borrado.deleted_count} documentos antiguos.")
        
        # 2. INSERCIÓN: Almacenar el JSON crudo tal cual llega de la API
        print("Insertando nuevos datos crudos en MongoDB Atlas...")
        resultado_insercion = coleccion.insert_many(datos_crudos)
        print(f"✅ ¡Éxito! Se guardaron correctamente {len(resultado_insercion.inserted_ids)} documentos.")
        
    except Exception as e:
        print(f"❌ Error crítico en el proceso de almacenamiento: {e}")

