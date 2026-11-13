# Ejercicio 20: Mostrar N números de la sucesión de Fibonacci.
# Los dos primeros son 1, 1; el resto: suma de los dos anteriores.

# Entrada
N = int(input("¿Cuántos números de Fibonacci quieres? "))

# Proceso y Salida
if N <= 0:
    print("Debe ser un número positivo.")
elif N == 1:
    print("1")
elif N == 2:
    print("1, 1")
else:
    fib1, fib2 = 1, 1
    print("1, 1", end="")
    for i in range(3, N + 1):
        fib_siguiente = fib1 + fib2
        print(f", {fib_siguiente}", end="")
        fib1, fib2 = fib2, fib_siguiente
    print()  # Salto de línea final

print("¡Ya hemos terminado!")