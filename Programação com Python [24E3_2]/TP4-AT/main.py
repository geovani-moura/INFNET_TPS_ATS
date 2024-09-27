import decimal
import os
from decimal import Decimal
import time

# Variaveis
estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"

estoque = []

# Classes
class Produto:
    def __init__(self, codigo, descricao, quantidade, preco_compra_item, preco_venda_item):        
        self.id = codigo if codigo is not None else obter_new_id()
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco_compra_item = Decimal(preco_compra_item)
        self.preco_venda_item = Decimal(preco_venda_item)

# Funções Globais
def limpar_tela():
    """
    Pula varias linhas para dar a impresão de ter limpado o console
    """
    for i in range(50):
        print()

# Mostrar
def mostrar_estoque(ordem, crescente=True, busca_id=None, busca_descricao=None, busca_esgotado=None, busca_min_quantidade=None):
    """
    Exibe o estoque de produtos cadastrados com seus detalhes, permitindo ordenar e filtrar os itens com base em diferentes critérios.

    Parâmetros:
    - ordem (str): O atributo pelo qual os produtos serão ordenados (ex: 'quantidade', 'preco_venda_item').
    - crescente (bool): Define se a ordenação será crescente (True) ou decrescente (False). Padrão é crescente.
    - busca_id (int, opcional): Se fornecido, exibe apenas o produto com o ID correspondente.
    - busca_descricao (str, opcional): Se fornecido, exibe produtos que contenham a descrição especificada.
    - busca_esgotado (bool, opcional): Se True, exibe apenas produtos cujo estoque está esgotado (quantidade <= 0).
    - busca_min_quantidade (int, opcional): Se fornecido, exibe produtos com quantidade menor ou igual ao valor especificado.

    Funcionalidade:
    - Filtra a lista de produtos conforme os critérios fornecidos, como ID, descrição, estoque esgotado ou quantidade mínima.
    - Ordena os produtos com base no atributo especificado e na ordem (crescente ou decrescente).
    - Exibe uma tabela formatada com os detalhes do produto (ID, descrição, quantidade, preço de custo, preço de venda).

    Validações:
    - Se nenhum produto for encontrado com os filtros aplicados, uma mensagem de erro é exibida.
    - Se não houver produtos no estoque, informa que o estoque está vazio.
    """
    print("=" * 37 + " Listagem de Estoque " + "=" * 37)
    
    if len(estoque) < 1:
        print(">>>>> Não há produtos cadastrados! <<<<<")
    else:
        estoque_filtrado = estoque
        
        # Filtrar pelo ID se fornecido
        if busca_id is not None:
            estoque_filtrado = [item for item in estoque_filtrado if item.id == busca_id]
        
        # Filtrar pela descrição se fornecido
        if busca_descricao is not None:
            estoque_filtrado = [item for item in estoque_filtrado if busca_descricao.lower() in item.descricao.lower()]

        # Filtrar produtos esgotados
        if busca_esgotado is not None:
            estoque_filtrado = [item for item in estoque_filtrado if int(item.quantidade) <= 0]

        # Filtrar produtos pela quantidade mínima
        if busca_min_quantidade is not None:
            estoque_filtrado = [item for item in estoque_filtrado if int(item.quantidade) <= busca_min_quantidade]

        # Verificar se há resultados após a busca
        if len(estoque_filtrado) == 0:
            print(">>>>> Nenhum produto encontrado com o critério de busca informado. <<<<<")
        else:
            # Exibir cabeçalho formatado
            print("{:<10} {:<35} {:<12} {:<15} {:<15}".format("ID", "Descrição", "Quantidade", "Preço de Custo", "Preço de Venda"))
            print("=" * 95)
            
            # Ordena e exibe o estoque filtrado
            for item in sorted(estoque_filtrado, key=lambda x: getattr(x, ordem), reverse=not crescente):
                print("{:<10} {:<35} {:<12} R$ {:<14.2f} R$ {:<14.2f}".format(
                    item.id,
                    item.descricao,
                    item.quantidade,
                    item.preco_compra_item,
                    item.preco_venda_item
                ))
    
    print("=" * 95)

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
    print(f"5 - Buscar por Produtos Esgotados")
    print(f"6 - Buscar por Produtos por Quantidade Minima")
    print()
    print(">>>>>>>>>> Cadastro, Exclusões e Alterações <<<<<<<<<<")
    print()
    print(f"10 - Cadastrar Produtos")
    if len(estoque) > 0:
        print(f"11 - Excluir Produtos")
        print(f"12 - Alterar Quantidade")
        print(f"13 - Alterar Preço")
    print()
    print(">>>>>>>>>> Relatorios <<<<<<<<<<")
    print()
    print(f"20 - Calcular valor total do estoque")
    print(f"21 - Cálculo do lucro presumido")
    print(f"22 - Relatorio Geral")
    print()
    print("=======================================")
    print(f"\n99 - Sair")
    print("=======================================")

# Obter
def obter_new_id():
    """
    Retorna o próximo ID disponível para um novo produto.
    
    A função verifica a lista de produtos e retorna o maior ID existente mais um. 
    Se a lista estiver vazia, retorna 0.

    Returns:
        int: O próximo ID disponível ou 0 se a lista estiver vazia.
    """
    retorno = 0
    if not estoque:
        return 0
    retorno = max(produto.id for produto in estoque)
    return retorno + 1

def obter_produto():
    """
    Solicita ao usuário que insira o ID de um produto e retorna esse ID.
    
    A entrada do usuário é convertida para um número inteiro.

    Returns:
        int: ID do produto inserido pelo usuário.
    """
    return int(input("Digite o ID da produto: "))

def obter_descricao():
    """
    Solicita e retorna a descrição de um produto informada pelo usuário.
    
    O usuário pode inserir uma descrição completa ou apenas parte dela.

    Returns:
        str: Descrição do produto informada pelo usuário.
    """
    return input("Informe a descrição ou parte dela: ")

def obter_minimo_quantidade_produto():
    """
    Solicita ao usuário que insira a quantidade mínima de produtos a serem buscados.
    
    Se o usuário não inserir nada, a função retorna o valor padrão de 5. 
    Se a entrada não for um número válido, retorna o valor padrão.

    Returns:
        int: Quantidade mínima em estoque ou o valor padrão se a entrada for inválida.
    """
    entrada = input("Digite a quantidade mínima [Padrão 5]: ").strip()
    
    if entrada == "":
        return 5
    
    try:
        return int(entrada)
    except ValueError:
        print("Entrada inválida! Usando valor padrão de 5.")
        return 5

def obter_opcao_menu():
    """
    Solicita ao usuário que escolha uma opção do menu e retorna a opção escolhida.
    
    Se o usuário não inserir nada, a função retorna 0.

    Returns:
        int: Opção escolhida pelo usuário do menu.
    """
    entrada = input("Escolha uma opção: ")
    print(f"[{entrada.strip()}]")
    if entrada.strip() == "":
        return 0
    return int(entrada)

def obter_menu():
    """
    Exibe o menu principal e processa a opção escolhida pelo usuário.
    
    A função chama mostrar_opcoes() para exibir as opções e obtém a escolha do usuário 
    através da função obter_opcao_menu().

    Returns:
        int: A opção escolhida pelo usuário do menu.
    """
    mostrar_opcoes()
    opcao = obter_opcao_menu()
    return opcao

def obter_quantidade():
    """
    Solicita ao usuário uma quantidade.

    Returns:
        int: Quantidade de um produto.
    """
    return int(input("Digite o quantidade: "))

def obter_preco():
    """
    Solicita ao usuário um preço.

    Returns:
        decimal: Preço do produto.
    """
    return input("Digite o preco: ")

def obter_valor_total_estoque():
    """
    Calcula o valor total do estoque, multiplicando a quantidade de cada produto
    pelo seu preço de venda.

    Returns:
        Decimal: Valor total do estoque.
    """
    total = Decimal(0) 
    for produto in estoque:
        valor_produto = produto.quantidade * produto.preco_venda_item
        total += valor_produto

    return total

def obter_lucro_presumido():
    """
    Calcula o lucro presumido do estoque, considerando a diferença entre o preço de venda e o custo
    de cada item multiplicado pela quantidade disponível.

    Returns:
        Decimal: Lucro total do estoque.
    """
    lucro_total = Decimal(0)
    
    for produto in estoque:
        lucro_por_item = (produto.preco_venda_item - produto.preco_compra_item) * produto.quantidade        
        lucro_total += lucro_por_item

    return lucro_total

def obter_relatorio_estoque():
    """
    Gera e exibe um relatório completo do estoque com detalhes dos produtos.
    """
    print("=" * 32 + " Relatório Geral do Estoque " + "=" * 32)
    print("Código".ljust(10) + "Descrição".ljust(25) + "Quantidade".ljust(12) + 
          "Custo".rjust(15) + "Preço".rjust(15) + "Valor Total".rjust(15))
    print("=" * 92)  # Linha separadora

    for produto in estoque:
        valor_total = produto.quantidade * produto.preco_venda_item
        linha = (str(produto.id).ljust(10) +
                 produto.descricao.ljust(25) +
                 str(produto.quantidade).ljust(12) +
                 f"R$ {produto.preco_compra_item:.2f}".rjust(15) +
                 f"R$ {produto.preco_venda_item:.2f}".rjust(15) +
                 f"R$ {valor_total:.2f}".rjust(15))
        print(linha)

    print("=" * 92)

# Excluir
def excluir_produto():
    """
    Exclui uma tarefa da lista com base no ID fornecido pelo usuário.
    """
    id = obter_produto()
    for produto in estoque:
        if produto.id == id:
            estoque.remove(produto)
            break
    else:
        print(f"Tarefa {id} não existe.")

# Adicionar
def adicionar_produto():
    """
    Adiciona um novo produto ao estoque com base nas informações fornecidas pelo usuário.

    O usuário é solicitado a inserir a descrição, quantidade, preço de compra e preço de venda do produto.
    Um novo objeto de produto é criado e adicionado à lista de estoque, o ID ou Codigo é grado automaticamente, pegando o 
    max id da lista e somando +1

    Inputs:
        - Descrição do produto (str)
        - Quantidade do produto (int)
        - Preço de compra do produto (Decimal)
        - Preço de venda do produto (Decimal)
    """
    codigo = None
    descricao = input("Digite a descrição da produto: ")
    quantidade = input("Digite a quantidade do produto: ")
    preco_compra_item = input("Digite a preço de compra do produto: Exemplo[50.00]: ")
    preco_venda_item = input("Digite a preço de venda do produto: Exemplo[100.00]: ")
    produto = Produto(codigo, descricao, quantidade, preco_compra_item, preco_venda_item)
    estoque.append(produto)

# Alterar
def alterar_preco():
    """
    Altera o preço de venda do produto fornecido pelo usuário, garantindo que o novo preço não
    seja menor que o preço de custo.
    """
    codigo = obter_produto()   
    preco = Decimal(obter_preco())

    for produto in estoque:
        if produto.id == codigo:
            if preco < produto.preco_compra_item:
                print("Erro: O preço de venda não pode ser menor que o preço de custo!")
                return
            
            produto.preco_venda_item = preco
            return

    print(f"Produto com ID {codigo} não existe.")

def alterar_quantidade():
    """
    Altera a quantidade do produto fornecido pelo usuário, garantindo que o estoque não fique negativo.
    """
    id_produto = obter_produto()
    nova_quantidade = obter_quantidade()
    
    for produto in estoque:
        if produto.id == id_produto:
            if produto.quantidade + nova_quantidade < 0:
                print("Erro: A atualização resultaria em estoque negativo!")
                return
            
            produto.quantidade += nova_quantidade
            return

    print(f"Produto com ID {id_produto} não existe.")

# Inicialização
def inicializa_estoque():
    linhas = estoque_inicial.replace('\n', '').strip().split('#')    
    for linha in linhas:
        if linha.strip():  
            descricao, codigo, quantidade, preco_compra_item, preco_venda_item = linha.split(';')            
            produto = Produto(int(codigo), descricao, int(quantidade), preco_compra_item, preco_venda_item)
            estoque.append(produto)

def voltar_menu():
    input("Pressione enter ou qualquer tecla para voltar ao menu...")
    limpar_tela()
    menu()

def menu():
    """
    Exibe o menu principal e processa a opção escolhida pelo usuário.
    """
    # Listagens e Buscas
    opcao = obter_menu()
    if opcao == 0:
        limpar_tela()
        mostrar_estoque('id', 1)
        voltar_menu()
    elif opcao == 1:
        limpar_tela()
        mostrar_estoque('quantidade', True)
        voltar_menu()
    elif opcao == 2:
        limpar_tela()
        mostrar_estoque('quantidade', False)
        voltar_menu()
    elif opcao == 3:
        limpar_tela()
        id1 = obter_produto()
        mostrar_estoque('id', 1, busca_id = id1)
        voltar_menu()
    elif opcao == 4:
        limpar_tela()
        descricao = obter_descricao()
        mostrar_estoque('id', 1, busca_descricao = descricao)
        voltar_menu()
    elif opcao == 5:
        limpar_tela()
        mostrar_estoque('id', 1, busca_esgotado = True)
        voltar_menu()
    elif opcao == 6:
        limpar_tela()
        quantidade = obter_minimo_quantidade_produto()
        mostrar_estoque('id', 1, busca_min_quantidade = quantidade)
        voltar_menu()

    # Cadastro e Alterações
    elif opcao == 10:
        limpar_tela()
        adicionar_produto()
        voltar_menu()
    elif opcao == 11:
        limpar_tela()
        excluir_produto()
        voltar_menu()
    elif opcao == 12:
        limpar_tela()
        alterar_quantidade()
        voltar_menu()
    elif opcao == 13:
        limpar_tela()
        alterar_preco()
        voltar_menu()

    # Relatorios
    elif opcao == 20:
        limpar_tela()
        total = obter_valor_total_estoque()
        print()
        print(f"Valor total do estoque: R$ {total:.2f}")
        print()
        voltar_menu()
    elif opcao == 21:
        limpar_tela()
        lucro = obter_lucro_presumido()
        print()
        print(f"Lucro total do estoque: R$ {lucro:.2f}")
        print()
        voltar_menu()
    elif opcao == 22:
        limpar_tela()
        obter_relatorio_estoque()
        voltar_menu()

    elif opcao == 99:
        print("Saindo...")
        return

inicializa_estoque()
menu()