print(
    "Parte 1 | Questão 1: Crie um programa que receba uma string como entrada do usuário e use um loop for para criar uma lista com cada caractere da string."
)
print()

entrada = input("Digite uma string: ")
lista_de_caracteres = []

for caractere in entrada:
    lista_de_caracteres.append(caractere)

print("Lista de caracteres:", lista_de_caracteres)
