print(
    "Usando a mesma implementação da questão 5 modifique a função para que, caso nenhum argumento seja passado, exiba uma saudação genérica."
)
print()


def saudacao(nome=None):
    if nome:
        print(f"Olá, {nome}!")
    else:
        print("Olá!")


saudacao()
