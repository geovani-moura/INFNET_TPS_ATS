print(
    "Crie uma função chamada imprime_dados que recebe diversos dados de um produto (nome, preço, quantidade em estoque) como argumentos passados obrigatoriamente por palavras-chave e os imprima de forma organizada."
)
print()


def imprime_dados(*, nome, preco, quantidade):
    print(f"Nome do produto: {nome}")
    print(f"Preço: R${preco:.2f}")
    print(f"Quantidade em estoque: {quantidade}")


imprime_dados(nome="Produto X", preco=19.99, quantidade=10)
