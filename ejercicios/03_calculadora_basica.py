"""Ejercicio 3: operaciones básicas con dos números."""
try:
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    print("Suma:", a + b)
    print("Resta:", a - b)
    print("Multiplicación:", a * b)
    print("División:", a / b if b != 0 else "No se puede dividir entre cero.")
except ValueError:
    print("Por favor, introduce números válidos.")
