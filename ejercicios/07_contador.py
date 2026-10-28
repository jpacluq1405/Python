"""Ejercicio 7: cuenta desde 1 hasta el número indicado."""
try:
    limite = int(input("Cuenta hasta qué número: "))
    if limite < 1:
        print("El número debe ser mayor que cero.")
    else:
        for numero in range(1, limite + 1):
            print(numero)
except ValueError:
    print("Introduce un número entero.")
