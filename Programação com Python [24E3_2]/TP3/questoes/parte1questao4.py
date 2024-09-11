print(
    """
    Parte 1 | Questão 4: 
    Desenvolva um programa que solicite ao usuário uma frase e imprima o número de caracteres, de palavras e de espaços em branco nesta frase.
    """
)
print()

frase = input("Digite uma frase: ")
num_caracteres = len(frase)
num_palavras = len(frase.split())
num_espacos = frase.count(' ')

print(f"Número de caracteres: {num_caracteres}")
print(f"Número de palavras: {num_palavras}")
print(f"Número de espaços em branco: {num_espacos}")
