# Ejercicio 5: Introducir notas y contar aprobados/suspensos. Repetir según el usuario.

aprobados = 0
suspensos = 0
continuar = "S"

while continuar.upper() == "S":
    
    # Entrada
    
    nota = float(input("Introduce una nota: "))
    
    # Proceso
    
    if nota >= 5:
        aprobados += 1
    else:
        suspensos += 1

    continuar = input("¿Quieres introducir otra nota? (S/N): ")

# Salida

print(f"Aprobados: {aprobados}")
print(f"Suspensos: {suspensos}")
print("¡Ya hemos terminado!")