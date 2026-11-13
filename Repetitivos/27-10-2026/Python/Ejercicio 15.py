# Ejercicio 15: Introducir un número entero positivo y realizar el FACTORIAL de ese número.

# Entrada
N = int(input("Introduce un número entero positivo: "))

# Proceso
if N < 0:
    factorial = None
elif N == 0 or N == 1:
    factorial = 1
else:
    factorial = 1
    for i in range(2, N + 1):
        factorial *= i

# Salida
if N < 0:
    print("El número debe ser positivo o cero.")
else:
    print(f"El factorial de {N} es: {factorial}")

print("¡Ya hemos terminado!")