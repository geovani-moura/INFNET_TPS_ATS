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
ordem_estoque = 'id'

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

def redirecionando():
    """
    Exibe uma mensagem de "Redirecionando" com pontos animados para indicar espera.
    """
    mensagem = "Redirecionando"
    print(mensagem, end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)
    print()

def limpar_tela():
    """
    Limpa a tela do terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_estoque():
    """
    Exibe todo o estoque cadastrado com seus detalhes.
    """
    print("========= Listagem de Estoque =========")
    if len(estoque) < 1:
        print(">>>>> Não há produtos cadastradas! <<<<<")
    else:
        for item in sorted(estoque, key=lambda x: getattr(x, ordem_estoque)):
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
    print("========== Ações disponíveis ==========")    
    print(f"\n1 - Adicionar Produto")
    if len(estoque) > 0:
        print(f"\n2 - Excluir tarefa")
        print(f"\n3 - Mudar status")
        print(f"\n4 - Mudar prioridade")
    print(f"\n5 - Sair")
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


def menu():
    """
    Exibe o menu principal e processa a opção escolhida pelo usuário.
    """
    limpar_tela()
    mostrar_estoque()
    mostrar_opcoes()
    opcao = escolha_opcao()
    if opcao == 0:
        menu()
    elif opcao == 1:
        adicionar_produto()
        redirecionando()
        menu()

limpar_tela()
menu()