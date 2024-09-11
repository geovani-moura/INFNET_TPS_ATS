print(
    """
    Parte 3 | Questão 1: 
    Mini Projeto 3: Gerenciamento de Senhas 

    Um administrador de sistemas precisa desenvolver uma ferramenta para gerenciar senhas de usuários em uma rede corporativa.

    1. Desenvolva uma função que gera senhas aleatórias seguras, atendendo aos critérios: 
    mínimo de 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais.
    2. Implemente uma função que receba uma senha do usuário e verifique se ela atende aos 
    critérios de segurança mencionados. Para cada senha que não atender aos critérios, sugerir uma senha nova.
    3. Crie um programa que criptografa uma lista de senhas utilizando uma cifra de substituição 
    (similar à cifra de Cesar) considerando todos os caracteres imprimíveis da tabela ASCII e armazene o resultado. 
    Inclua uma função para descriptografar as senhas quando necessário.
    """
)
print()

import random
import string

DESLOCAMENTO = 4
TAMANHO = 12

def gerar_senha(TAMANHO):
    if TAMANHO < 8:
        raise ValueError("A senha deve ter pelo menos 8 caracteres.")
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(TAMANHO))
    return senha

def verificar_senha(senha):
    criterios = []
    if len(senha) < 8:
        criterios.append("A senha deve ter pelo menos 8 caracteres.")
    if not any(c.isupper() for c in senha):
        criterios.append("A senha deve conter pelo menos uma letra maiúscula.")
    if not any(c.islower() for c in senha):
        criterios.append("A senha deve conter pelo menos uma letra minúscula.")
    if not any(c.isdigit() for c in senha):
        criterios.append("A senha deve conter pelo menos um número.")
    if not any(c in string.punctuation for c in senha):
        criterios.append("A senha deve conter pelo menos um caractere especial.")
    
    return criterios

def sugerir_senha():
    while True:
        senha = gerar_senha(TAMANHO)
        criterios = verificar_senha(senha)
        if not criterios:
            return senha

def criptografar(senha, deslocamento):
    caracteres = string.printable.replace(' ', '')  # Remove espaços dos caracteres imprimíveis
    senha = senha.replace(' ', '')  # Remove espaços da senha
    tabela_cripto = str.maketrans(caracteres, caracteres[deslocamento:] + caracteres[:deslocamento])
    return senha.translate(tabela_cripto)

def descriptografar(senha, deslocamento):
    caracteres = string.printable.replace(' ', '')  # Remove espaços dos caracteres imprimíveis
    tabela_cripto = str.maketrans(caracteres[deslocamento:] + caracteres[:deslocamento], caracteres)
    return senha.translate(tabela_cripto)

def obter_senha():
    return input("Digite a senha: ")

def iniciar():
    senha_usuario = obter_senha()
    criterios = verificar_senha(senha_usuario)
    
    if criterios:
        print("A senha fornecida não atende aos critérios de segurança:")
        for criterio in criterios:
            print(f"* {criterio}")
        print("Sugerindo uma nova senha...")
        senha_sugerida = sugerir_senha()
        print(f"Senha sugerida: {senha_sugerida}")
        senha_sugerida_criptografada = criptografar(senha_sugerida, DESLOCAMENTO)
        print(f"Senha sugerida criptografada: {senha_sugerida_criptografada}")
    else:
        print("A senha fornecida atende a todos os critérios de segurança.")
        senha_criptografada = criptografar(senha_usuario, DESLOCAMENTO)
        print(f"Senha criptografada: {senha_criptografada}")
        
        senha_descriptografada = descriptografar(senha_criptografada, DESLOCAMENTO)
        print(f"Senha descriptografada: {senha_descriptografada}")

iniciar()

