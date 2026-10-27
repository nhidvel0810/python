# python
En este apartado iré publicando los ejercicios de python que vayamos haciendo en clase:

Secuenciales, alternativos y los repetitivos.
Ejemplos:

Secuencial:

import math

# Pedimos el radio
radio = float(input("Introduce el radio del círculo: "))

# Calculamos el área
area = math.pi * (radio ** 2)

# Mostramos el resultado con dos decimales
print(f"El área del círculo es: {area:.2f}")

Alternativo:

letra = input("Introduce una letra: ").lower()

if letra in 'aeiouáéíóú':
    print("Es una vocal")
else:
    print("Es una consonante")

Repetitivo: con For:

# Entrada

n = int(input("Introduce un número entero: "))

# Proceso y Salida

print(f"Tabla de multiplicar del {n}:")
for i in range(1, 11):
    resultado = n * i
    print(f"{n} * {i} = {resultado}")

# Salida final

print("¡Ya hemos terminado!")

Repetitivo con While:

num = int(input("Dame un número positivo: "))

while num >= 0:
    for i in range(1, 11):
        rdo = num * i
        print(f"{num} * {i} = {rdo}")
        
    num = int(input("Si decides continuar dame otro número positivo"))

print("¡Ya hemos terminado!")
