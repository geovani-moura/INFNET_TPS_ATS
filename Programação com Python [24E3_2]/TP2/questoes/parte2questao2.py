print(
    "Crie uma função chamada maior_valor que receba três números como trê argumentos posicionais, exiba o maior número na tela e retorne uma lista ordenada contendo estes números."
)
print()


def maior_valor(a, b, c):
    maior = max(a, b, c)
    print(maior)
    return sorted([a, b, c])


resultado = maior_valor(7, 3, 5)
print(resultado)
