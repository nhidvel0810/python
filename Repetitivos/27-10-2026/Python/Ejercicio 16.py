# Ejercicio 16: Introducir edad y sexo (H ó M) mientras la edad sea positiva.
# Se pide: hombres, media hombres, mujeres, media mujeres.

# Inicialización
hombres = 0
mujeres = 0
suma_hombres = 0
suma_mujeres = 0

# Entrada y Proceso
edad = int(input("Introduce una edad (negativa para terminar): "))

while edad >= 0:
    sexo = input("Introduce el sexo (H/M): ").upper()
    if sexo == "H":
        hombres += 1
        suma_hombres += edad
    elif sexo == "M":
        mujeres += 1
        suma_mujeres += edad
    else:
        print("Sexo no válido. Se omitirá este registro.")
    
    edad = int(input("Introduce otra edad (negativa para terminar): "))

# Salida
if mujeres > 0:
    media_mujeres = suma_mujeres / mujeres
    print(f"- Se han introducido {mujeres} mujeres y la media de edad es de {round(media_mujeres, 2)} años.")
else:
    print("- No se han introducido mujeres.")

if hombres > 0:
    media_hombres = suma_hombres / hombres
    print(f"- Se han introducido {hombres} hombres y la media de edad es de {round(media_hombres, 2)} años.")
else:
    print("- No se han introducido hombres.")

print("¡Ya hemos terminado!")