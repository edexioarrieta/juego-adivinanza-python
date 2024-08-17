

import random


numero_secreto = random.randint(1,101)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("Bienvenido al juego de adivinar el numero secreto")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("¡Game over! No has podido adivinar dentro de los 5 intentos")
        break

    entrada = input("Introduce un numero del 1 al 100: ")
    numero =  int(entrada)

    if numero == numero_secreto:
        print("Felicitaciones has adivinado el numero secreto")
        adivinado = True

    elif numero < numero_secreto:
        print("El numero es mayor al numero ingresado")
    else:
        print("El numero es menor al numero ingresado")

    cant_intentos += 1