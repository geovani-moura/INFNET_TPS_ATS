print(
    """
    Parte 2 | Questão 3: 
    Crie uma função chamada imprime_dados que recebe diversos dados de um produto (nome, preço, quantidade em estoque) 
    como argumentos passados obrigatoriamente por palavras-chave e os imprima de forma organizada.
    """
)
print()


def imprime_dados(*, nome, preco, quantidade):
     """
    Imprime os dados de um produto de forma organizada.
    
    Args:
        nome (str): Nome do produto.
        preco (float): Preço do produto.
        quantidade (int): Quantidade em estoque do produto.
    
    Return:
        None
    """
    # Código de implementação da função.
    print(f"Nome do produto: {nome}")
    print(f"Preço: R${preco:.2f}")
    print(f"Quantidade em estoque: {quantidade}")


imprime_dados(nome="Produto X", preco=29.89, quantidade=37)
