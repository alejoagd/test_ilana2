def es_numero_feliz(n):
    def suma_cuadrados_digitos(num):
        # Función auxiliar para calcular la suma de los cuadrados de los dígitos
        return sum(int(digit) ** 2 for digit in str(num))

    # Utilizamos un conjunto para detectar ciclos infinitos
    seen_numbers = set()

    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = suma_cuadrados_digitos(n)

    return n == 1

# Ejemplos de uso:
print(es_numero_feliz(19))  # True
print(es_numero_feliz(2))   # False
print(es_numero_feliz(7))   # True
