import datetime
from enum import Enum
import os
import time

tarefas = []

def redirecionando():
    """
    Exibe uma mensagem de "Redirecionando" com pontos animados para indicar espera.
    """
    mensagem = "Redirecionando"
    print(mensagem, end="", flush=True)
    for i in range(5):
        time.sleep(1)  # Aguarda 1 segundo
        print(".", end="", flush=True)
    print()  # Quebra de linha após os pontos

def obter_ultimo_id():
    """
    Retorna o maior ID das tarefas na lista.

    Returns:
        int: O maior ID ou 0 se a lista estiver vazia.
    """
    if not tarefas:
        return 0
    return max(tarefa.id for tarefa in tarefas)

class StatusEnum(Enum):
    """
    Enum para representar os status de uma tarefa.
    """
    Pendente = 1
    Em_andamento = 2
    Concluida = 3

class PrioridadeEnum(Enum):
    """
    Enum para representar as prioridades de uma tarefa.
    """
    Alta = 1
    Media = 2
    Baixa = 3

class Tarefa:
    def __init__(self, descricao, prazo_final, prioridade):
        """
        Classe que representa uma Tarefa.

        Args:
            descricao (str): Descrição da tarefa.
            prazo_final (str): Data de prazo final da tarefa no formato "dd/mm/aaaa".
            prioridade (int): Prioridade da tarefa (1-alta, 2-média, 3-baixa).
        """
        self.id = obter_ultimo_id() + 1
        self.descricao = descricao
        self.data_criacao = datetime.datetime.now()
        self.status = StatusEnum(1)
        self.prazo_final = datetime.datetime.strptime(prazo_final, "%d/%m/%Y")
        self.prioridade = int(prioridade)

tarefas.append(Tarefa("Teste1", "01/09/2024", 1))
tarefas.append(Tarefa("Teste2", "01/09/2024", 2))
tarefas.append(Tarefa("Teste3", "01/09/2024", 3))

def adicionar_tarefa():
    """
    Adiciona uma nova tarefa à lista de tarefas com base na entrada do usuário.
    """
    descricao = input("Digite a descrição da tarefa: ")
    prazo_final = input("Digite o prazo final da tarefa (formato: dd/mm/aaaa): ")
    prioridade = input("Digite a prioridade da tarefa (1-alta, 2-média, 3-baixa): ")
    tarefa = Tarefa(descricao, prazo_final, prioridade)
    tarefas.append(tarefa)

def excluir_tarefa():
    """
    Exclui uma tarefa da lista com base no ID fornecido pelo usuário.
    """
    id = escolher_tarefa()
    for tarefa in tarefas:
        if tarefa.id == id:
            tarefas.remove(tarefa)
            break
    else:
        print(f"Tarefa {id} não existe.")

def mudar_status():
    """
    Altera o status de uma tarefa com base no ID e no novo status fornecidos pelo usuário.
    """
    id = escolher_tarefa()
    status = int(input("Digite o status da tarefa (1-Pendente, 2-Em_andamento, 3-Concluida): "))
    for tarefa in tarefas:
        if tarefa.id == id:
            tarefa.status = StatusEnum(status)
            return
    print(f"Tarefa {id} não existe.")

def escolher_tarefa():
    """
    Solicita ao usuário que insira o ID de uma tarefa.

    Returns:
        int: ID da tarefa inserido pelo usuário.
    """
    return int(input("Digite o ID da tarefa: "))

def mudar_prioridade():
    """
    Altera a prioridade de uma tarefa com base no ID e na nova prioridade fornecidos pelo usuário.
    """
    id = escolher_tarefa()
    prioridade = int(input("Digite a nova prioridade da tarefa (1-alta, 2-média, 3-baixa): "))
    for tarefa in tarefas:
        if tarefa.id == id:
            tarefa.prioridade = PrioridadeEnum(prioridade)
            return
    print(f"Tarefa {id} não existe.")

def mostrar_tarefas():
    """
    Exibe todas as tarefas cadastradas com seus detalhes.
    """
    print("========= Listagem de Tarefas =========")
    if len(tarefas) < 1:
        print(">>>>> Não há tarefas cadastradas! <<<<<")
    else:
        for tarefa in tarefas:
            print(f"{tarefa.id} | "
                  f"{tarefa.descricao} | "
                  f"{tarefa.data_criacao.strftime('%d/%m/%Y')} | "
                  f"{StatusEnum(tarefa.status).name} | "
                  f"{tarefa.prazo_final.strftime('%d/%m/%Y')} | "
                  f"{PrioridadeEnum(tarefa.prioridade).name}")
    print("=======================================")

def mostrar_opcoes():
    """
    Exibe as opções disponíveis para o usuário.
    """
    print("========== Ações disponíveis ==========")    
    print(f"\n1 - Adicionar tarefa")
    if len(tarefas) > 0:
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

def menu():
    """
    Exibe o menu principal e processa a opção escolhida pelo usuário.
    """
    limpar_tela()
    mostrar_tarefas()
    mostrar_opcoes()
    opcao = escolha_opcao()
    if opcao == 0:
        menu()
    elif opcao == 1:
        adicionar_tarefa()
        redirecionando()
        menu()
    elif opcao == 2:
        excluir_tarefa()
        redirecionando()
        menu()
    elif opcao == 3:
        mudar_status()
        redirecionando()
        menu()
    elif opcao == 4:
        mudar_prioridade()
        redirecionando()
        menu()
    elif opcao == 5:
        print("Saindo...")
        return
    else:
        menu()

def limpar_tela():
    """
    Limpa a tela do terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()
menu()
