# Ejercicio 18: Introducir número de lista y 3 notas de Lengua mientras nº lista ≠ 0.
# Se pide: media por alumno y media del grupo.

# Inicialización
suma_grupo = 0
contador = 0

# Entrada y Proceso
num_lista = int(input("Introduce el número de lista (0 para terminar): "))

while num_lista != 0:
    nota1 = int(input("Primera evaluación: "))
    nota2 = int(input("Segunda evaluación: "))
    nota3 = int(input("Tercera evaluación: "))
    
    media_alumno = (nota1 + nota2 + nota3) / 3
    print(f"- El alumno con número de lista {num_lista} tiene un {round(media_alumno, 2)} de nota media.")
    
    suma_grupo += media_alumno
    contador += 1
    
    num_lista = int(input("Introduce el número de lista (0 para terminar): "))

# Salida
if contador > 0:
    media_grupo = suma_grupo / contador
    print(f"- La media del grupo en LENGUA es: {round(media_grupo, 2)}")
else:
    print("- No se introdujeron alumnos.")

print("¡Ya hemos terminado!")