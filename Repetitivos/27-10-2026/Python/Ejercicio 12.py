# Ejercicio 12: Introducir edades mientras sean positivas, realizar la MEDIA y visualizar si dicha media ha sido mayor o menor de edad.

# Entrada y Proceso
suma = 0
contador = 0

edad = int(input("Introduce una edad (negativa para terminar): "))

while edad >= 0:
    suma += edad
    contador += 1
    edad = int(input("Introduce otra edad (negativa para terminar): "))

# Salida
if contador > 0:
    media = suma / contador
    print("La media de edades es:", round(media, 2))
    if media >= 18:
        print("La media es MAYOR de edad.")
    else:
        print("La media es MENOR de edad.")
else:
    print("No se introdujo ninguna edad válida.")

print("¡Ya hemos terminado!")