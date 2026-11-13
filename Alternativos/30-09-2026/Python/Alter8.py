import math

a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

discriminante = b**2 - 4*a*c

if discriminante >= 0:
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print("Las raíces reales son x1 =", x1, "y x2 =", x2)
else:
    print("Las raíces no son reales (el discriminante es negativo)")