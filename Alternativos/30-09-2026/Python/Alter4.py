letra = input("Introduce una letra: ").lower()

if letra in 'aeiouáéíóú':
    print("Es una vocal")
else:
    print("Es una consonante")