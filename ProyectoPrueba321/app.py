from conexion_sheets import obtener_datos

print("Conectando con Google Sheets...")
datos = obtener_datos()

print("¡CONEXIÓN Y CARGA DE DATOS DE MATRÍCULA EXITOSA :D!")
for fila in datos:
    print(fila)