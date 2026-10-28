"""Ejercicio 10: usa una función para comprobar números primos."""
def es_primo(numero: int) -> bool:
    """Devuelve True si numero es primo."""
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True

try:
    numero = int(input("Introduce un número entero: "))
    print(f"{numero} es primo." if es_primo(numero) else f"{numero} no es primo.")
except ValueError:
    print("Introduce un número entero válido.")
