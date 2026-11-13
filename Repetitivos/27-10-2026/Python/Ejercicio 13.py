# Ejercicio 13: Introducir un número entero positivo (N) y realizar la suma de la siguiente serie.
# S=1+1/2+1/3+1/4+...+1/N
# Visualizar por pantalla el resultado (S)

# Entrada

acum=0
veces= int(input("Introduce un numero positivo: "))

# Proceso

for i in range (1,veces+1):
    acum=acum+1/i

# Salida

print ("El resultado es: ",acum)