print(
    """
    Parte 2 | Questão 6: 
    Defina uma função chamada gerar_lista_pares que receba um número n, fornecido pelo usuário, como argumento e retorne uma 
    lista contendo todos os números pares de 0 até n. Utilize um laço for para preencher a lista.
    """
)
print()


def gerar_lista_pares(n):
    lista_pares = []
    for i in range(0, n + 1, 2):
        lista_pares.append(i)
    return lista_pares


n = int(input("Digite um número: "))
pares = gerar_lista_pares(n)
print(pares)
