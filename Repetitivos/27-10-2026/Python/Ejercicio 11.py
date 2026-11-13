# Ejercicio 11: Introducir notas mientras sean positivas. Se pide:
# 1º Cuántos aprobados hay.
# 2º Cuántos suspensos hay.
# 3º Hallar la media.

# Entrada

cont_ap=0
cont_susp=0
acum=0

veces= int(input("Dime el numero de notas: "))
for i in range (veces):

    nota= int (input("Dame una nota: "))
    while nota <0 or nota >10:
        nota=int(input("Dime una nota entre 0 y 10: "))
    
    # Proceso
    
    if nota >5:
        cont_ap=cont_ap+1
    else:
        cont_susp=cont_susp+1

    acum= acum+nota

media=acum/(cont_ap+cont_susp)

# Salida

print ("La media de la nota es: ",media)
print ("Total de aprobados es: ",cont_ap)
print ("Total de suspensos es: ",cont_susp)