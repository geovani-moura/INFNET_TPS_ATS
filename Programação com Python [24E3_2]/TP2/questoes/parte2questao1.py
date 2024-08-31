print(
    "Defina uma função chamada potencia que receba dois números como argumento, a base e o expoente. O expoente deve ter um valor padrão de 2. A função deve calcular e retornar a base elevada ao expoente."
)
print()


def potencia(base, expoente=2):
    return base**expoente


resultado1 = potencia(3, 4)
print(resultado1)

resultado2 = potencia(5)
print(resultado2)
