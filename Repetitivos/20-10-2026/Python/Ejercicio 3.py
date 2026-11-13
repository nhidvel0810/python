# Ejercicio 3: Introducir un número entero y visualizar si es POSITIVO, NEGATIVO o NULO. Repetir según el usuario.

continuar = "S"

while continuar.upper() == "S":
    
    # Entrada
    
    num = int(input("Introduce un número entero: "))
    
    # Proceso y Salida
    
    if num > 0:
        print("POSITIVO")
    elif num < 0:
        print("NEGATIVO")
    else:
        print("NULO")

    continuar = input("¿Quieres repetir? (S/N): ")

# Salida final

print("¡Ya hemos terminado!")