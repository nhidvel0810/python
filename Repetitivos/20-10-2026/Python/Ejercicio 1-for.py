# Ejercicio 1: Introducir un número entero y realizar su tabla de multiplicar. Formato: N*1=R, N*2=R, ...

# Entrada

n = int(input("Introduce un número entero: "))

# Proceso y Salida

print(f"Tabla de multiplicar del {n}:")
for i in range(1, 11):
    resultado = n * i
    print(f"{n} * {i} = {resultado}")

# Salida final

print("¡Ya hemos terminado!")