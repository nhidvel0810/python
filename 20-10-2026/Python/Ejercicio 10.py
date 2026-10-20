# Ejercicio 10: Introducir un número entero positivo (N) y realizar la SUMA N-ÉSIMA: S = 1 + 2 + ... + N

# Entrada

n = int(input("Introduce un número entero positivo (N): "))

if n <= 0:
    print("El número debe ser positivo.")
else:
    # Proceso
    
    suma = 0
    for i in range(1, n + 1):
        suma += i
    
    # Salida
    
    print(f"La suma 1 + 2 + ... + {n} es: {suma}")

print("¡Ya hemos terminado!")