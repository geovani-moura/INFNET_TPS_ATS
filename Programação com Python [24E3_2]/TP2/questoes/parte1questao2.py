print(
    """
    Parte 1 | Questão 2: 
    Crie um programa que peça ao usuário para inserir números um de cada vez até que ele digite 0. Armazene esses números em uma lista usando um loop while.
    """
)
print()

numeros = []

while True:
    numero = int(input("Digite um número (digite 0 para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

print(numeros)
