print(
    """
    Parte 1 | Questão 3: 
    Escreva um programa que receba uma lista de números (você pode definir a lista inicialmente, mas certifique-se que o código 
    funcionará para quaisquer listas numéricas) e utilize um loop for para calcular a média dos valores da lista.
    """
)
print()

numeros = [10, 20, 30, 40, 50]

soma = 0
for numero in numeros:
    soma += numero

media = soma / len(numeros)

print(media)
