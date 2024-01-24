def foo_bar(n):
    # Se realiza verificacion si el número es divisible por 3 y/o 5
    divisible_by_3 = n % 3 == 0
    divisible_by_5 = n % 5 == 0

    # Validacion de las condiciones 
    if divisible_by_3 and divisible_by_5:
        return "FooBar"
    elif divisible_by_3:
        return "Foo"
    elif divisible_by_5:
        return "Bar"
    else:
        return str(n)

# Ingreso de datos para confirmacion de la salida , se deja mapeado el ejemplo del problema, pero funciona con cualquier dato.
print("Entrada=9, salida =", foo_bar(9))    # Salida: Foo
print("Entrada=10, salida =", foo_bar(10))  # Salida: Bar
print("Entrada=15, salida =", foo_bar(15))  # Salida: FooBar
print("Entrada=16, salida =", foo_bar(16))  # Salida: 16
