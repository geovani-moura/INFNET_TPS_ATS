print(
    """
    Parte 3 | Questão 1: 
    Mini Projeto 1: Validação e Formatação de Dados em um Sistema de Cadastro

    1. Na vida de um desenvolvedor e analista de sistemas a validação de dados é uma etapa extremamente 
    importante que previne diversas dificuldades posteriores à coleta dos dados.

        1. Crie um programa com funções em Python para solicitar ao usuário que insira os dados listados abaixo e valide os seguintes 
        campos de cadastro com as seguintes regras:
        2. CPF: verifique se o CPF possui 11 dígitos e formate-o no padrão "xxx.xxx.xxx-xx".
        3. E-mail: verifique se o e-mail possui um formato válido (com "@" e um domínio válido) e normalize-o para minúsculas. 
        Caracteres alfanuméricos + ‘@’ + Caracteres alfanuméricos + ‘.’ + Caracteres alfabéticos
        4. Telefone: remova caracteres não numéricos e converta o número de telefone para um número inteiro e em uma 
        string formatada como (XX) XXXXX-XXXX ou (XX) XXXX-XXXX e exibindo o inteiro e a string formatada na tela.
    """
)
print()

def obter_cpf():
    return input("Digite o CPF: ").strip()

def obter_email():
    return input("Digite o e-mail: ").strip().lower()

def obter_telefone():
    return input("Digite o telefone: ").strip()

def valida_cpf(cpf):
    cpf_digits = [char for char in cpf if char.isdigit()]
    if len(cpf_digits) != 11:
        return ["Inconsistência no campo CPF por CPF inválido. Deve conter 11 dígitos."]
    return []

def valida_email(email):
    if '@' not in email or '.' not in email:
        return ["Inconsistência no campo E-mail por E-mail inválido."]
    return []

def valida_telefone(telefone):
    telefone_digits = [char for char in telefone if char.isdigit()]
    if len(telefone_digits) not in [10, 11]:
        return ["Inconsistência no campo Telefone por Telefone inválido. Deve conter 10 ou 11 dígitos."]
    return []

def formata_cpf(cpf_digits):
    cpf = ''.join(cpf_digits)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def formata_telefone(telefone_digits):
    telefone = ''.join(telefone_digits)
    if len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    else:
        return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"


def inicio():
    cpf = obter_cpf()
    email = obter_email()
    telefone = obter_telefone()

    inconsistencias = []
    
    inconsistencias.extend(valida_cpf(cpf))
    inconsistencias.extend(valida_email(email))
    inconsistencias.extend(valida_telefone(telefone))
    
    if inconsistencias:
        for inconsistencia in inconsistencias:
            print(inconsistencia)
    else:
        cpf_digits = [char for char in cpf if char.isdigit()]
        telefone_digits = [char for char in telefone if char.isdigit()]
        print()
        print("Resultado:")
        print(f"CPF: {formata_cpf(cpf_digits)}")
        print(f"E-mail: {email}")
        print(f"Telefone: {''.join(telefone_digits)}")

inicio()
