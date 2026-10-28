"""Ejercicio 9: calcula estadísticas de una lista de números."""
entrada = input("Escribe varios números separados por espacios: ").split()
try:
    numeros = [float(valor) for valor in entrada]
    if not numeros:
        print("Debes introducir al menos un número.")
    else:
        print("Cantidad:", len(numeros))
        print("Suma:", sum(numeros))
        print("Media:", sum(numeros) / len(numeros))
        print("Mínimo:", min(numeros))
        print("Máximo:", max(numeros))
except ValueError:
    print("Todos los valores deben ser números.")
