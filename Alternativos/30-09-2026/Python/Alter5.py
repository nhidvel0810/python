import math

opcion = input("Introduce 'A' para área o 'L' para longitud: ").upper()
radio = float(input("Introduce el radio: "))

if opcion == 'A':
    area = math.pi * (radio ** 2)
    print("El área de la circunferencia es:", area)
elif opcion == 'L':
    longitud = 2 * math.pi * radio
    print("La longitud de la circunferencia es:", longitud)
else:
    print("Opción no válida")