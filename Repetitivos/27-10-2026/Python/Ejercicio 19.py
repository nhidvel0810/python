# Ejercicio 19: Calcular el capital con interés fijo durante N años.
# Mostrar por año: año, capital inicio, beneficio, capital fin.

# Entrada
año_inicio = int(input("Año de inicio: "))
capital = float(input("Capital inicial: "))
interes = float(input("Interés anual (%): "))
años = int(input("Número de años: "))

# Proceso y Salida
print("\nResumen de la inversión:")
for i in range(años):
    año_actual = año_inicio + i
    beneficio = capital * (interes / 100)
    capital_final = capital + beneficio
    print(f"Año {año_actual}:")
    print(f"  - Capital a principios: {round(capital, 2)} €")
    print(f"  - Beneficio: {round(beneficio, 2)} €")
    print(f"  - Capital a fin de año: {round(capital_final, 2)} €")
    capital = capital_final  # Actualizamos para el próximo año

print("¡Ya hemos terminado!")