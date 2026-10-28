"""Ejercicio 8: juego de adivinar un número aleatorio."""
import random
secreto = random.randint(1, 100)
intentos = 0
print("He pensado un número del 1 al 100.")
while True:
    try:
        intento = int(input("Tu intento: "))
    except ValueError:
        print("Escribe un número entero.")
        continue
    intentos += 1
    if intento < secreto:
        print("Demasiado pequeño. Prueba otra vez.")
    elif intento > secreto:
        print("Demasiado grande. Prueba otra vez.")
    else:
        print(f"¡Correcto! Lo conseguiste en {intentos} intentos.")
        break
