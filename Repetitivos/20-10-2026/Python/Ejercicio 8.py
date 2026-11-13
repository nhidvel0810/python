# Ejercicio 8: Introducir un número positivo (obligando a repetir si es negativo) y realizar su raíz cuadrada. Usar while.

import math

# Entrada

num = float(input("Introduce un número positivo: "))

while num < 0:
    print("Error: el número debe ser positivo o cero.")
    num = float(input("Introduce un número positivo: "))

# Proceso

raiz = math.sqrt(num)

# Salida

print(f"La raíz cuadrada de {num} es: {raiz}")
print("¡Ya hemos terminado!")