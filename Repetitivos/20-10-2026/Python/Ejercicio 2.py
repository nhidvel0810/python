# Ejercicio 2: Introducir una edad y visualizar si es MAYOR o MENOR de edad. Repetir 5 veces.

# Proceso (con bucle for)

for i in range(1, 6):
    
    # Entrada
    
    edad = int(input(f"({i}/5) Introduce tu edad: "))
    
    # Salida
    
    if edad >= 18:
        print("MAYOR de edad")
    else:
        print("MENOR de edad")

# Salida final

print("¡Ya hemos terminado!")