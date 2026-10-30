from conexion_sheets import obtener_datos

def contar_total_cursos(registros):
    total_cursos = 0
    for registro in registros:
        cursos = registro.get("Cursos matriculados")
        if cursos:
            lista_cursos = [c.strip() for c in str(cursos).split(",") if c.strip()]
            total_cursos += len(lista_cursos)
    return total_cursos

def contar_por_sexo(registros):
    resumen_sexo = {"Masculino": 0, "Femenino": 0}
    for registro in registros:
        sexo = registro.get("Sexo")
        if sexo in resumen_sexo:
            resumen_sexo[sexo] += 1
        elif sexo:
            resumen_sexo[sexo] = resumen_sexo.get(sexo, 0) + 1
    return resumen_sexo

datos = obtener_datos()

total_cursos = contar_total_cursos(datos)
print(f"Total de cursos matriculados: {total_cursos}")

conteo_sexo = contar_por_sexo(datos)
print(f"Total por sexo -> Masculino: {conteo_sexo.get('Masculino', 0)}, Femenino: {conteo_sexo.get('Femenino', 0)}")
