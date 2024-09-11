print(
    """
    Parte 1 | Questão 5: 
    Calcular a soma dos dígitos em uma string numérica fornecida pelo usuário, verificando se todos os caracteres são de fato numéricos.
    Exemplo: “123” Resultado: 1+2+3 = 6
    """
)
print()

entrada = input("Digite uma string numérica: ")

if entrada.isdigit():
    soma = sum(int(digito) for digito in entrada)
    print(f"Soma dos dígitos: {soma}")
else:
    print("A string contém caracteres não numéricos.")
