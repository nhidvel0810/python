print("--- CALCULADORA ---")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Resto (Módulo)")

opcion = input("Elige una opción (1-5): ")

num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))

if opcion == '1':
    print("Resultado:", num1 + num2)
elif opcion == '2':
    print("Resultado:", num1 - num2)
elif opcion == '3':
    print("Resultado:", num1 * num2)
elif opcion == '4':
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Error: No se puede dividir entre cero")
elif opcion == '5':
    if num2 != 0:
        print("Resultado (resto):", num1 % num2)
    else:
        print("Error: No se puede calcular el resto con cero")
else:
    print("Opción de menú no válida")