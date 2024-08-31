print(
    """
    Parte 3 | Questão 1: 
    Simulador de Investimentos
    Crie um programa que simule o crescimento de um investimento ao longo de um período. O programa deve solicitar ao usuário o valor inicial do 
    investimento, a taxa de juros anual e o número de anos. Em seguida, escreva uma função que calcule o valor final do investimento ao final de 
    cada ano e armazene esses valores em uma lista. Imprima o valor acumulado ano a ano (lembre-se que se trata de juros compostos).
    """
)
print()


def calcular_valores_investimento(valor_inicial, taxa_juros_anual, anos):
    valores = []
    valor_acumulado = valor_inicial
    taxa_juros_decimal = taxa_juros_anual / 100

    for ano in range(1, anos + 1):
        valor_acumulado *= 1 + taxa_juros_decimal
        valores.append(valor_acumulado)

    return valores


valor_inicial = float(input("Digite o valor inicial do investimento: "))
taxa_juros_anual = float(input("Digite a taxa de juros anual (em %): "))
anos = int(input("Digite o número de anos: "))

valores_acumulados = calcular_valores_investimento(
    valor_inicial, taxa_juros_anual, anos
)

for ano, valor in enumerate(valores_acumulados, start=1):
    print(f"Ano {ano}: R${valor:.2f}")
