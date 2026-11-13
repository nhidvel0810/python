# Ejercicio 17: Introducir número de lista y nota de 10 alumnos.
# Se pide: alumno con máxima nota, mínima nota y media.

# Inicialización
max_nota = -1
min_nota = 11
suma = 0
alumno_max = 0
alumno_min = 0

# Entrada y Proceso
for i in range(1, 11):
    num_lista = int(input(f"Alumno {i} - Número de lista: "))
    nota = int(input(f"Alumno {i} - Nota: "))
    
    suma += nota
    
    if nota > max_nota:
        max_nota = nota
        alumno_max = num_lista
    if nota < min_nota:
        min_nota = nota
        alumno_min = num_lista

# Salida
media = suma / 10
print(f"1º Alumno con máxima nota: número {alumno_max}, nota {max_nota}")
print(f"2º Alumno con mínima nota: número {alumno_min}, nota {min_nota}")
print(f"3º Media de la asignatura: {round(media, 2)}")

print("¡Ya hemos terminado!")