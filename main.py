from ingesta import extraer_datos_api
from ingesta import guardar_en_mongodb

# --- Bloque principal de ejecución ---
if __name__ == "__main__":
    print("--- INICIANDO FASE 1: EXTRACCIÓN ---")
    datos = extraer_datos_api()
    
    print("\n--- INICIANDO FASE 2: CARGA EN MONGODB ---")
    guardar_en_mongodb(datos)