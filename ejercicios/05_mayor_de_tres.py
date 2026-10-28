"""Ejercicio 5: encuentra el mayor de tres números."""
try:
    numeros = [float(input(f"Número {i}: ")) for i in range(1, 4)]
    print("El mayor es:", max(numeros))
except ValueError:
    print("Introduce números válidos.")
