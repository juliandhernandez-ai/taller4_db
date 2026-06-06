import requests
from pymongo import MongoClient

def extraer_datos_api():
    """Descarga los datos de la API manejando la paginación."""
    url_actual = "https://rickandmortyapi.com/api/character"
    todos_los_personajes = []
    
    # Repetir hasta superar la barrera de los 100 objetos requeridos
    while url_actual and len(todos_los_personajes) < 100:
        print(f"Descargando página: {url_actual}")
        respuesta = requests.get(url_actual)
        
        if respuesta.status_code == 200:
            datos = respuesta.json()
            # Agregamos los personajes crudos a nuestra lista
            todos_los_personajes.extend(datos["results"])
            
            # Pasamos a la siguiente página
            url_actual = datos["info"]["next"]
        else:
            print(f"Error en la extracción. Código: {respuesta.status_code}")
            break
            
    return todos_los_personajes

def guardar_en_mongodb(datos_crudos):
    print(f"\n--- DIAGNÓSTICO DE GUARDADO ---")
    print(f"1. Datos recibidos para guardar: {len(datos_crudos)} objetos.")
    
    if len(datos_crudos) == 0:
        print("❌ ERROR: La lista de datos está vacía. Como no hay datos, MongoDB NO creará la base de datos.")
        return

    try:
        print("2. Intentando conectar a MongoDB...")
        # NOTA: Si vas a usar Atlas, cambia esta URL por la tuya
        cliente = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
        
        # 3. Forzamos un 'ping' para comprobar si el servidor realmente responde
        cliente.admin.command('ping')
        print("✅ ¡Conexión exitosa al servidor de MongoDB!")

        # 4. Preparando la base de datos y colección
        db = cliente["taller4_db"]
        coleccion = db["raw_data"]
        
        print("5. Insertando los datos...")
        coleccion.insert_many(datos_crudos)
        print("✅ ¡ÉXITO! Los datos fueron insertados. Ve a Compass y dale al botón de Refresh.")
        
    except Exception as e:
        print(f"❌ ERROR CRÍTICO AL CONECTAR O GUARDAR: {e}")