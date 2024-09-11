print(
    """
    Parte 3 | Questão 4: 
    Mini projeto 4: Processamento de Textos Jurídicos 

    Um escritório de advocacia deseja automatizar parte do processo de análise de contratos, extraindo informações relevantes de documentos longos.

    1. Desenvolva um programa que receba o texto completo de um contrato e extraia todas as cláusulas que mencionem valores monetários. 
    Os valores devem ser identificados e exibidos em uma lista separada.
    2. Implemente uma função que, dada uma lista de termos legais, verifique quantas vezes cada termo aparece no contrato 
    e exiba as ocorrências em ordem decrescente de frequência.
    """
)
print()

from collections import Counter

termos_legais = ["contrato", "obrigação", "penalidade", "rescisão", "cláusula"]

texto_contrato = """
Contrato de Compra e Venda

Cláusula 1: O vendedor, João Silva, e o comprador, Maria Oliveira, celebram este contrato de compra e venda referente ao imóvel localizado na Rua das Flores, nº 123, Bairro Jardim, Cidade Exemplo.

Cláusula 2: O valor total do imóvel é de R$ 500.000,00 (quinhentos mil reais). O pagamento será feito em duas parcelas: a primeira de R$ 250.000,00 (duzentos e cinquenta mil reais) no ato da assinatura do contrato e a segunda de R$ 250.000,00 (duzentos e cinquenta mil reais) na data de entrega das chaves.

Cláusula 3: O vendedor se compromete a entregar o imóvel livre de quaisquer ônus ou dívidas, e em perfeito estado de conservação.

Cláusula 4: O comprador terá um prazo de 30 dias para inspecionar o imóvel e notificar o vendedor sobre qualquer vício ou defeito encontrado.

Cláusula 5: Em caso de rescisão do contrato por parte do comprador, será cobrada uma multa equivalente a 10% do valor total do imóvel. Se a rescisão ocorrer por parte do vendedor, o comprador receberá uma compensação de 10% do valor total pago até a data da rescisão.

Cláusula 6: Este contrato entra em vigor na data de sua assinatura e é regido pelas leis vigentes no país.

Cláusula 7: Multa de R$ 500,00 por dia, por atraso.

Assinaturas:
_______________________________
João Silva - Vendedor

_______________________________
Maria Oliveira - Comprador

Data: ____/____/____
"""

def extrair_clausulas(texto):
    clausulas_com_valores = []
    linhas = texto.split('\n')
    for linha in linhas:
        if 'cláusula' in linha.lower() and any(palavra in linha for palavra in ['R$', 'reais']):
            clausulas_com_valores.append(linha.strip())
    return clausulas_com_valores

def contar_termos_legais(texto, termos):
    palavras = texto.lower().split()
    contagem = Counter(palavra.strip('.,:;()') for palavra in palavras if palavra.strip('.,:;()') in termos)
    return dict(sorted(contagem.items(), key=lambda item: item[1], reverse=True))

def iniciar():
    clausulas = extrair_clausulas(texto_contrato)
    ocorrencias = contar_termos_legais(texto_contrato, termos_legais)
    
    print("Cláusulas com Valores Monetários:")
    for clausula in clausulas:
        print(f"- {clausula}")

    print("\nOcorrências de Termos Legais:")
    for termo, freq in ocorrencias.items():
        print(f"{termo}: {freq}")

iniciar()
