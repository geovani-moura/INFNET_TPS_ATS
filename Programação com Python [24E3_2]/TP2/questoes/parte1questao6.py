print(
    """
    Parte 1 | Questão 6: 
    Usando a mesma implementação da questão 5 modifique a função para que, caso nenhum argumento seja passado, exiba uma saudação genérica.
    """
)
print()


def saudacao(nome=None):
     """
    Imprime uma saudação personalizada com o nome fornecido.
    Se nenhum nome for fornecido, imprime uma saudação genérica.
    
    Args:
        nome (str, optional): Nome do usuário para a saudação. Se não fornecido, uma saudação genérica é exibida.
    
    Return:
        None
    """
    # Código de implementação da função.
    if nome:
        print(f"Olá, {nome}!")
    else:
        print("Olá!")


saudacao()
