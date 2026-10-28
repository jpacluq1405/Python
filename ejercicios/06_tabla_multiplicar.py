"""Ejercicio 6: imprime la tabla de multiplicar."""
try:
    numero = int(input("¿Qué tabla quieres ver? "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
except ValueError:
    print("Introduce un número entero.")
