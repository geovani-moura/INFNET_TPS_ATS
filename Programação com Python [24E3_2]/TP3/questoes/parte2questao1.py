print(
    """
    Parte 2 | Questão 1: 
    Calcular o resultado de uma expressão matemática básica fornecida como string pelo usuário, 
    ignorando espaços, permitindo apenas caracteres numéricos e os operadores +, -, * e /.
    Exemplo: '2 + 3 * 4' Resultado: 14.
    """
)
print()

def calcular_expressao(expressao):
    expressao = expressao.replace(" ", "")
    resultado = 0
    numero_atual = ""
    operador_atual = '+'
    
    for caractere in expressao:
        if caractere.isdigit():
            numero_atual += caractere
        else:
            if numero_atual:
                if operador_atual == '+':
                    resultado += int(numero_atual)
                elif operador_atual == '-':
                    resultado -= int(numero_atual)
                elif operador_atual == '*':
                    resultado *= int(numero_atual)
                elif operador_atual == '/':
                    resultado /= int(numero_atual)
            operador_atual = caractere
            numero_atual = ""
    
    if numero_atual:
        if operador_atual == '+':
            resultado += int(numero_atual)
        elif operador_atual == '-':
            resultado -= int(numero_atual)
        elif operador_atual == '*':
            resultado *= int(numero_atual)
        elif operador_atual == '/':
            resultado /= int(numero_atual)
    
    return resultado

expressao = input("Digite a expressão matemática: ")
resultado = calcular_expressao(expressao)
print(f"Resultado: {resultado}")

