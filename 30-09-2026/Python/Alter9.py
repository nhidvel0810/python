num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))

if num2 != 0:
    if num1 % num2 == 0:
        print(num1, "es divisible por", num2)
    else:
        print(num1, "NO es divisible por", num2)
else:
    print("No se puede dividir por cero")