# Ejercicio 7: Introducir números enteros y calcular el mínimo. Repetir según el usuario.

# Inicialización de variables

minimo = None
continuar = "S"

# Proceso principal (bucle while)

while continuar.upper() == "S":
    
    # Entrada
    
    entrada = input("Introduce un número entero: ").strip()
    
    # Validación: si está vacío, pedimos otro
    
    if entrada == "":
        print("No has introducido ningún número. Por favor, inténtalo de nuevo.")
        continue
    
    try:
        num = int(entrada)
        
        # Proceso: actualizar el mínimo si es necesario
        
        if minimo is None or num < minimo:
            minimo = num
        
        # Preguntar si desea continuar
        
        continuar = input("¿Quieres introducir otro número? (S/N): ").strip()
        
    except ValueError:
        print("¡Error! No es un número entero válido. Por favor, inténtalo de nuevo.")

# Salida final

if minimo is not None:
    print(f"El número mínimo introducido es: {minimo}")
else:
    print("No se introdujo ningún número.")

print("¡Ya hemos terminado!")