print(
    """
    Parte 2 | Questão 1: 
    Defina uma função chamada potencia que receba dois números como argumento, a base e o expoente. O expoente deve ter um valor padrão de 2. 
    A função deve calcular e retornar a base elevada ao expoente.
    """
)
print()


def potencia(base, expoente=2):
     """
    Calcula a potência da base elevada ao expoente.
    
    Args:
        base (int | float): A base a ser elevada.
        expoente (int, optional): O expoente ao qual a base será elevada. O padrão é 2.
    
    Return:
        int | float: Resultado da base elevada ao expoente.
    """
    # Código de implementação da função.
    return base**expoente


resultado1 = potencia(3, 4)
print(resultado1)

resultado2 = potencia(5)
print(resultado2)
