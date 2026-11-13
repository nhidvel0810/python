# Ejercicio 4: Introducir 5 edades y visualizar cuántos son mayores de edad.

# Inicialización
mayores = 0

# Proceso

for i in range(1, 6):
    
    # Entrada
    
    edad = int(input(f"Edad {i}: "))
    
    # Proceso
    
    if edad >= 18:
        mayores += 1

# Salida

print(f"De las 5 personas, {mayores} son mayores de edad.")
print("¡Ya hemos terminado!")