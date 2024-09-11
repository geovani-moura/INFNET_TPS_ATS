print(
    """
    Parte 1 | Questão 2: 
    Crie um script em Python que substitua todas as ocorrências de uma palavra específica em uma frase 
    por outra palavra fornecida pelo usuário. Utilize um texto de exemplo de sua preferência e escolha a 
    palavra a ser substituída, mas a lógica precisa funcionar para outros casos.
    """
)
print()

frase_exemplo = "A biblioteca está cheia de livros interessantes e novas histórias."
palavra_a_substituir = input("Digite a palavra que deseja substituir: ")
nova_palavra = input("Digite a nova palavra: ")

frase_modificada = frase_exemplo.replace(palavra_a_substituir, nova_palavra)
print("Frase modificada:", frase_modificada)

