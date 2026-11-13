import math

# Pedimos el radio
radio = float(input("Introduce el radio del círculo: "))

# Calculamos el área
area = math.pi * (radio ** 2)

# Mostramos el resultado con dos decimales
print(f"El área del círculo es: {area:.2f}")