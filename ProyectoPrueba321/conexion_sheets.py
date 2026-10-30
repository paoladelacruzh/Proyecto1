import gspread

def obtener_datos():
    cliente = gspread.service_account(filename="credencialesdemo.json")
    
    archivo = cliente.open("Copia de Registro de Matrículas (respuestas)")
    
    hoja = archivo.worksheet("Respuestas")
    
    datos = hoja.get_all_records()
    return datos