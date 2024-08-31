print(
    """
    Parte 2 | Questão 2: 
    Crie uma função chamada maior_valor que receba três números como trê argumentos posicionais, exiba o maior número na tela e 
    retorne uma lista ordenada contendo estes números.
    """
)
print()


def maior_valor(a, b, c):
    """
    Exibe o maior valor entre três números e retorna uma lista desses números ordenada.

    Args:
        a (int | float): Primeiro número.
        b (int | float): Segundo número.
        c (int | float): Terceiro número.

    Return:
        list: Lista contendo os três números em ordem crescente.
    """
    # Código de implementação da função.
    maior = max(a, b, c)
    print(maior)
    return sorted([a, b, c])


resultado = maior_valor(7, 3, 5)
print(resultado)
