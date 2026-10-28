"""Ejercicio 4: determina si un número es par o impar."""
try:
    numero = int(input("Escribe un número entero: "))
    print("Es par." if numero % 2 == 0 else "Es impar.")
except ValueError:
    print("Debes introducir un número entero.")
