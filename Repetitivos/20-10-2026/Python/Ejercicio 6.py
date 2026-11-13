# Ejercicio 6: Introducir números enteros y calcular el máximo. Repetir según el usuario.

maximo = None
continuar = "S"

while continuar.upper() == "S":
    
    # Entrada
    
    num = int(input("Introduce un número entero: "))
    
    # Proceso
    
    if maximo is None or num > maximo:
        maximo = num

    continuar = input("¿Quieres introducir otro número? (S/N): ")

# Salida

if maximo is not None:
    print(f"El número máximo introducido es: {maximo}")
else:
    print("No se introdujo ningún número.")

print("¡Ya hemos terminado!")