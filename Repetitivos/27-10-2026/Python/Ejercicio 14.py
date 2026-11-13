# Ejercicio 14: Introducir un número entero positivo, calcular sus 10 primeras potencias y visualizar el resultado.

# Entrada
N = int(input("Introduce un número entero positivo: "))

# Proceso
if N <= 0:
    print("El número debe ser positivo.")
else:
    print(f"Las 10 primeras potencias de {N} son:")
    for i in range(1, 11):
        potencia = N ** i
        print(f"{N}^{i} = {potencia}")

# Salida

print ("Ya hemos terminado!")