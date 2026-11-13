import math

# Pedimos los dos catetos
cateto_a = float(input("Introduce el valor del primer cateto: "))
cateto_b = float(input("Introduce el valor del segundo cateto: "))

# Calculamos la hipotenusa
hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)

# Mostramos el resultado
print("La hipotenusa es:", hipotenusa)