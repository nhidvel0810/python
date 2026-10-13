nota = float(input("Introduce la nota del alumno: "))

if nota < 0 or nota > 10:
    print("Nota fuera de rango válido (0 a 10)")
elif nota < 5:
    print("Suspenso")
elif nota < 6:
    print("Suficiente")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")