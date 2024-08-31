print(
    """
    Parte 2 | Questão 5: 
    Defina uma função chamada exibir_mensagem que receba um argumento obrigatório mensagem e um argumento opcional repeticoes, 
    onde repeticoes tem um valor padrão de 1. A função deve imprimir a mensagem o número de vezes especificado por repeticoes.
    """
)
print()


def exibir_mensagem(mensagem, repeticoes=1):
    for _ in range(repeticoes):
        print(mensagem)


exibir_mensagem("Geovani", repeticoes=3)
