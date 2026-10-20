# Programa que calcule la tabla de multiplicar de un número.

num = int(input("Dame un número positivo: "))

while num >= 0:
    for i in range(1, 11):
        rdo = num * i
        print(f"{num} * {i} = {rdo}")
        
    num = int(input("Si decides continuar dame otro número positivo"))

print("¡Ya hemos terminado!")