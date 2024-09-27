import os
from decimal import Decimal
import time

estoque_inicial = """
Notebook Dell;201;15;3200.00;4500.00#
Notebook Lenovo;202;10;2800.00;4200.00#
Mouse Logitech;203;50;70.00;150.00#
Mouse Razer;204;40;120.00;250.00#
Monitor Samsung;205;10;800.00;1200.00#
Monitor LG;206;8;750.00;1150.00#
Teclado Mecânico Corsair;207;30;180.00;300.00#
Teclado Mecânico Razer;208;25;200.00;350.00#
Impressora HP;209;5;400.00;650.00#
Impressora Epson;210;3;450.00;700.00#
Monitor Dell;211;12;850.00;1250.00#
Monitor AOC;212;7;700.00;1100.00
"""

estoque = []

def obter_new_id():
    """
    Retorna o maior ID das tarefas na lista.

    Returns:
        int: O maior ID ou 0 se a lista estiver vazia.
    """
    retorno = 0
    if not estoque:
        return 0
    retorno = max(produto.id for produto in estoque)
    return retorno + 1

class Produto:
    def __init__(self, codigo, descricao, quantidade, preco_compra_item, preco_venda_item):        
        self.id = codigo if codigo is not None else obter_new_id()
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco_compra_item = Decimal(preco_compra_item)
        self.preco_venda_item = Decimal(preco_venda_item)

def inicializa_estoque():
    linhas = estoque_inicial.replace('\n', '').strip().split('#')    
    for linha in linhas:
        if linha.strip():  
            descricao, codigo, quantidade, preco_compra_item, preco_venda_item = linha.split(';')            
            produto = Produto(int(codigo), descricao, int(quantidade), preco_compra_item, preco_venda_item)
            estoque.append(produto)

# Executa a inicialização de estoque
inicializa_estoque()

def limpar_tela():
    """
    Pula varias linhas para dar a impresão de ter limpado o console
    """
    for i in range(30):
        print()

def mostrar_estoque(ordem, crescente=True, busca_id=None, busca_descricao=None):
    """
    Exibe todo o estoque cadastrado com seus detalhes, ordenado por um atributo específico.
    Permite filtrar a listagem por ID ou descrição.
    
    Parâmetros:
    - ordem: O atributo pelo qual o estoque será ordenado (ex: 'quantidade').
    - crescente: Define se a ordenação será crescente (True) ou decrescente (False).
    - busca_id: Se informado, busca por um item com o ID correspondente.
    - busca_descricao: Se informado, busca por itens que contenham a descrição.
    """
    print("========= Listagem de Estoque =========")
    
    if len(estoque) < 1:
        print(">>>>> Não há produtos cadastrados! <<<<<")
    else:
        estoque_filtrado = estoque
        
        # Filtrar pelo ID se fornecido
        if busca_id is not None:
            estoque_filtrado = [item for item in estoque_filtrado if item.id == busca_id]
        
        # Filtrar pela descrição se fornecido
        if busca_descricao:
            estoque_filtrado = [item for item in estoque_filtrado if busca_descricao.lower() in item.descricao.lower()]

        # Verificar se há resultados após a busca
        if len(estoque_filtrado) == 0:
            print(">>>>> Nenhum produto encontrado com o critério de busca informado. <<<<<")
        else:
            # Ordena e exibe o estoque filtrado
            for item in sorted(estoque_filtrado, key=lambda x: getattr(x, ordem), reverse=not crescente):
                print(f"{item.id} | "
                      f"{item.descricao} | "
                      f"{item.quantidade} | "
                      f"R$ {item.preco_compra_item} | "
                      f"R$ {item.preco_venda_item} ")
    
    print("=======================================")




def mostrar_opcoes():
    """
    Exibe as opções disponíveis para o usuário.
    """
    print("=======================================")
    print("========== Ações disponíveis ==========")    
    print("=======================================")
    print(">>>>>>>>>> Listagens e Buscas <<<<<<<<<<")
    print()
    print(f"0 - Listar Produtos")
    print(f"1 - Listar Produtos por Quantidade Crescente")
    print(f"2 - Listar Produtos por Quantidade Decrescente")
    print(f"3 - Buscar por codigo do Produtos")
    print(f"4 - Buscar por Descrição do Produtos")
    print()
    print(">>>>>>>>>> Cadastro e Alterações <<<<<<<<<<")
    print()
    print(f"10 - Cadastrar Produtos")

    if len(estoque) > 0:
        print(f"\n4 - Excluir tarefa")
        print(f"\n5 - Mudar status")
        print(f"\n6 - Mudar prioridade")
    print(f"\n99 - Sair")
    print("=======================================")

def escolha_opcao():
    """
    Solicita ao usuário que escolha uma opção.

    Returns:
        int: Opção escolhida pelo usuário.
    """
    entrada = input("Escolha uma opção: ")
    print(f"[{entrada.strip()}]")
    if entrada.strip() == "":
        return 0
    return int(entrada)

def obter_id():
    """
    Solicita e retorna o ID do produto informado pelo usuário, convertido para inteiro.
    """
    try:
        return int(input("Informe o ID do produto: "))
    except ValueError:
        print("ID inválido! Por favor, insira um número válido.")
        return None


def obter_descricao():
    """
    Solicita e retorna a descrição do produto informada pelo usuário.
    """
    return input("Informe a descrição ou parte dela: ")


def adicionar_produto():
    """
    Adiciona uma nova tarefa à lista de tarefas com base na entrada do usuário.
    """
    codigo = None
    descricao = input("Digite a descrição da produto: ")
    quantidade = input("Digite a quantidade do produto: ")
    preco_compra_item = input("Digite a preço de compra do produto: Exemplo[50.00]: ")
    preco_venda_item = input("Digite a preço de venda do produto: Exemplo[100.00]: ")
    produto = Produto(codigo, descricao, quantidade, preco_compra_item, preco_venda_item)
    estoque.append(produto)

def mostrar_menu():
    """
    Exibe o menu principal e processa a opção escolhida pelo usuário.
    """
    mostrar_opcoes()
    opcao = escolha_opcao()
    return opcao

def menu():
    """
    Exibe o menu principal e processa a opção escolhida pelo usuário.
    """
    # Listagens e Buscas
    opcao = mostrar_menu()
    if opcao == 0:
        limpar_tela()
        mostrar_estoque('id', 1)
        menu()
    elif opcao == 1:
        limpar_tela()
        mostrar_estoque('quantidade', 1)
        menu()
    elif opcao == 2:
        limpar_tela()
        mostrar_estoque('quantidade', 0)
        menu()
    elif opcao == 3:
        limpar_tela()
        id1 = obter_id()
        mostrar_estoque('id', 1, busca_id = id1)
        menu()
    elif opcao == 4:
        limpar_tela()
        descricao = obter_descricao()
        mostrar_estoque('id', 1, busca_descricao = descricao)
        menu()

    # Cadastro e Alterações
    elif opcao == 10:
        limpar_tela()
        adicionar_produto()
        menu()

menu()