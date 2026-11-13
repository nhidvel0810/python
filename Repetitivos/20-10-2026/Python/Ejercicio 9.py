# Ejercicio 9: Introducir todas las notas de tu primera evaluación y realizar la MEDIA.

# Entrada

cantidad = int(input("¿Cuántas notas tienes? "))
suma = 0

# Proceso

for i in range(cantidad):
    nota = float(input(f"Nota {i+1}: "))
    suma += nota

media = suma / cantidad

# Salida

print(f"La media de tus notas es: {round(media, 2)}")
print("¡Ya hemos terminado!")