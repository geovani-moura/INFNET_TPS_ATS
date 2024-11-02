import os
import pandas as pd
import random

os.system('cls' if os.name == 'nt' else 'clear')

print("1 - Aquecendo os motores ⭐")
print('''Crie uma lista chamada ‘usuarios’ que contenha ao menos 5 listas. 
      Cada lista interna deve representar um usuário do INFwebNET com as seguintes 
      informações: nome (string), idade (inteiro), cidade (string) e estado (string).''')
usuarios = [
    ["Maria da Silva", 45, "São Paulo", "SP"],
    ["José Santos", 52, "São Paulo", "SP"],
    ["Ana Oliveira", 28, "São Paulo", "SP"],
    ["João Pereira", 33, "São Paulo", "SP"],
    ["Carlos Sousa", 40, "São Paulo", "SP"]
]
for usuario in usuarios:
    print(f'Usuarios: {usuario}')
print("*"*100)

print("2 - Perfil ⭐⭐")
print('''Escreva um programa que leia os dados da lista ‘usuarios’ criada no exercício 
      anterior e crie um dicionário para cada usuário. 
      Cada dicionário deve ter as chaves "nome" e "idade" com os respectivos valores, e a 
      chave "localização" contendo uma tupla (cidade, estado). 
      Armazene esses dicionários em uma nova lista chamada perfis.''')
perfis = []
for usuario in usuarios:
    perfil = {
        "nome": usuario[0],
        "idade": usuario[1],
        "localizacao": (usuario[2], usuario[3])
    }
    perfis.append(perfil)
for perfil in perfis:
    print(f'Perfil: {perfil}')
print("*"*100)

print("3 - Comparando Estruturas ⭐⭐⭐")
print('''Explique, em poucas palavras, as principais diferenças entre uma lista, um dicionário 
      e uma tupla em Python. Dê exemplos de como cada estrutura pode ser usada no contexto da 
      análise de dados do INFwebNET.''')
#Lista: É uma sequência de itens em ordem. Você pode adicionar, remover e alterar itens facilmente. Cada item na lista tem uma posição (índice). 
# No INFwebNET, uma lista pode guardar vários usuários, onde cada usuário é uma lista de informações pessoais.
usuarioList = [
    ["Maria", 45, "São Paulo", "SP"],
    ["José", 52, "São Paulo", "SP"]
]
print(f'Lista: {usuarioList}')

#Dicionário: Guarda dados como pares "chave-valor". Cada chave é única e permite acessar o valor ligado a ela. 
# No INFwebNET, podemos usar dicionários para guardar informações detalhadas de cada usuário, como nome, idade e localização.
usuarioDic = {
    "nome": "Maria",
    "idade": 45,
    "localização": ("São Paulo", "SP")
}
print(f'Dicionário: {usuarioDic}')

#Tupla: É parecida com uma lista, mas seus itens não podem ser alterados. Útil para dados fixos que não vão mudar. 
# No INFwebNET, uma tupla pode representar a localização de um usuário (cidade e estado), pois essa informação geralmente não muda.
localizacaoTupla = ("São Paulo", "SP")
print(f'Tupla: {localizacaoTupla}')
print("*"*100)

print("4 - Limpando o terreno ⭐⭐")
print('''Alguns usuários do INFwebNET forneceram informações incompletas. 
      Remova da lista perfis todos os perfis que não possuem as informações 
      de "nome" ou "cidade". Mantenha a lista perfis original intacta, criando 
      uma nova lista chamada perfis_validos para armazenar os perfis válidos.''')
perfis_validos = []
for perfil in perfis:
    if perfil.get('nome') and perfil['localizacao'][0]:
        perfis_validos.append(perfil)

for perf_val in perfis_validos:
    print(f'Perfis Validos: {perf_val}')
print("*"*100)

print('5 - Carregando dados ⭐⭐⭐')
print('''Crie uma implementação que leia os dados presentes no arquivo "base_inicial.txt" 
      e os armazene na lista perfis_validos, criando novas palavras-chave para os dados 
      adicionais encontrados. (O arquivo está disponível no repositório.)''')
perfis_validos_mesclar = []
class Perfil_Valido:
    def __init__(self, nome, idade, localizacao, amigos):
        self.nome = nome
        self.idade = idade
        self.localizacao = localizacao
        self.amigos = amigos
    
    def __repr__(self):
        return f"Perfil_Valido(nome='{self.nome}', idade={self.idade}, localizacao='{self.localizacao}', amigos={self.amigos})"
      
def add_perfil_valido(nome, idade, localizacao, amigos):
    perfil = Perfil_Valido(nome, idade, localizacao, amigos)
    perfis_validos_mesclar.append(perfil)
    
def add_perfil_valido_anterior():
    for perfil in perfis_validos:
        amigos = []
        nome = perfil.get('nome')
        idade = perfil.get('idade')
        cidade = perfil['localizacao'][0]
        estado = perfil['localizacao'][1]   
        localizacao = (cidade, estado)    
        add_perfil_valido(nome, idade, localizacao, amigos)

def ler_csv():  
    diretorio = os.getcwd()
    diretorio_e_arquivo = os.path.join(diretorio, 'base_inicial.txt')        
    lista_perfis = []
    with open(diretorio_e_arquivo, 'r', encoding='utf-8') as arquivo:
        arquivo.readline() 
        for linha in arquivo:            
            dados = linha.strip().split('?')              
            nome = dados[0].strip()
            idade = dados[1].strip()
            cidade = dados[2].strip()
            estado = dados[3].strip()
            amigos = dados[4:] if len(dados) > 4 else []

            localizacao = f"{cidade}, {estado}" if cidade and estado else ''
            perfil = Perfil_Valido(nome, idade, localizacao, amigos)
            lista_perfis.append(perfil)            
    return lista_perfis

add_perfil_valido_anterior()
perfil_colecao = ler_csv()
for perfil in perfil_colecao:
    if perfil.nome.strip(): 
        add_perfil_valido(perfil.nome, perfil.idade, perfil.localizacao, perfil.amigos)
    
perfis_validos = []
for perfil in perfis_validos_mesclar:
    perfis_validos.append(perfil)    
        
print('Perfis validos atualizados:')
for perfil in perfis_validos:
    print(f'Perfil: {perfil}')
print("*"*100)

print('6 - Concatenando dados ⭐')
print('''Com os dados carregados no exercício anterior, adicione os usuários dos exercícios 1 e 2, definindo um padrão para 
      lidar com os dados ausentes e salve estas informações em um arquivo "rede_INFNET.txt".''')
class Usuario:
    def __init__(self, nome, idade, localizacao, amigos):
        self.nome = nome
        self.idade = idade
        self.localizacao = localizacao
        self.amigos = amigos    
    def __repr__(self):
        return f"Dados(nome='{self.nome}', idade={self.idade}, localizacao='{self.localizacao}', amigos={self.amigos})"    
    
usuarios_concatenados = [];
def add_usuario_exerc_1_2():
    for perfil in perfis:
        amigos = []
        nome = perfil.get('nome')
        idade = perfil.get('idade')
        cidade = perfil['localizacao'][0]
        estado = perfil['localizacao'][1]   
        localizacao = (cidade, estado)
        usuarios_concatenados.append(Usuario(nome, idade, localizacao, amigos))     
           
usuario_colecao = ler_csv()
for usuario in usuario_colecao:
    usuarios_concatenados.append(Usuario(usuario.nome, usuario.idade, usuario.localizacao, usuario.amigos))    
    
diretorio = os.getcwd()
diretorio_e_arquivo = os.path.join(diretorio, 'rede_INFNET.txt') 
with open(diretorio_e_arquivo, "w", encoding="utf-8") as file:
    file.writelines('Nome|Idade|Localização(Cidade, Estado)|Amigos(Lista)\n')
    for usuario in usuarios_concatenados:
        file.writelines(f"{usuario.nome}|{usuario.idade}|{usuario.localizacao}|{', '.join(usuario.amigos)}\n")          
print("*"*100)


print('7 - Concatenando dados ⭐')
print('''Com o dicionário criado no exercício anterior, adicione um novo amigo ao set de amigos de um usuário específico.''')
diretorio = os.getcwd()
diretorio_e_arquivo = os.path.join(diretorio, 'rede_INFNET.txt') 
df = pd.read_csv(diretorio_e_arquivo, sep='|', header=0, 
                     names=["Nome", "Idade", "Localização(Cidade, Estado)", "Amigos(Lista)"])
def add_amigo(nome, novo_amigo):
    if nome in df['Nome'].values:
        indice = df[df['Nome'] == nome].index[0]
        amigos_existentes = df.at[indice, 'Amigos(Lista)']
        if amigos_existentes: 
            df.at[indice, 'Amigos(Lista)'] += f", {novo_amigo}"
        else: 
            df.at[indice, 'Amigos(Lista)'] = novo_amigo
    else:
        print("Nome não encontrado.")
print('Add ao usuaio joão um amigo chamado Geovani')
add_amigo("João", "Geovani")
print('Add ao usuaio Ana um amigo chamado Geovani')
add_amigo("Ana", "Geovani")
df.to_csv(diretorio_e_arquivo, sep='|', index=False)

print("*"*100)
print('8 - Verificando Conexões ⭐⭐')
print('''Crie um programa que permita verificar se um determinado usuário foi adicionado como amigo de mais de 4 usuários. 
      Caso tenha, exiba uma mensagem afirmando que o usuário é "popular".''')
diretorio = os.getcwd()
diretorio_e_arquivo = os.path.join(diretorio, 'rede_INFNET.txt') 
df = pd.read_csv(diretorio_e_arquivo, sep='|', header=0, 
                     names=["Nome", "Idade", "Localização(Cidade, Estado)", "Amigos(Lista)"])
def buscar_amigo(nome):
    contagem = 0
    for index, row in df.iterrows():
        amigos = row['Amigos(Lista)'].split(', ') if pd.notna(row['Amigos(Lista)']) else []
        if nome in amigos:
            contagem += 1            
    print(f'Usuario {nome} é amigo de {contagem} pessoas')     
    
print('Buscando por Fernando:')      
buscar_amigo('Fernando')
print('Buscando por Geovani:')      
buscar_amigo('Geovani')


print("*"*100)
print('9 Amigos em Comum ⭐⭐')
print('''Crie um programa que selecione dois perfis aleatórios e utilize sets para armazenar os amigos de cada um desses usuários do INFwebNET. 
      Exiba os amigos em comum entre esses dois usuários, utilizando métodos e operação de sets.''')
diretorio = os.getcwd()
diretorio_e_arquivo = os.path.join(diretorio, 'rede_INFNET.txt') 
df = pd.read_csv(diretorio_e_arquivo, sep='|', header=0, 
                     names=["Nome", "Idade", "Localização(Cidade, Estado)", "Amigos(Lista)"])
usuario_lista = df['Nome'].tolist()
usuario_random1, usuario_random2 = random.sample(usuario_lista, 2)

def obter_amigos(usuario):
    linha = df[df['Nome'] == usuario]
    if not linha.empty:
        amigos = linha['Amigos(Lista)'].values[0]
        return set(amigos.split(', ')) if pd.notna(amigos) else set()
    return set()

amigos_usuario1 = obter_amigos(usuario_random1)
amigos_usuario2 = obter_amigos(usuario_random2)
amigos_em_comum = amigos_usuario1.intersection(amigos_usuario2)

print(f"Usuário 1: {usuario_random1}")
print(f"Amigos de {usuario_random1}: {amigos_usuario1}")
print(f"\nUsuário 2: {usuario_random2}")
print(f"Amigos de {usuario_random2}: {amigos_usuario2}")
print(f"\nAmigos em comum entre {usuario_random1} e {usuario_random2}: {amigos_em_comum}")

print("*"*100)

print('10 Conexões Exclusivas ⭐⭐')
print('''Utilizando os sets do exercício anterior, exiba os amigos que são exclusivos de cada usuário, 
      ou seja, aqueles que não são amigos em comum.''')

amigos_exclusivos_usuario1 = amigos_usuario1 - amigos_em_comum
amigos_exclusivos_usuario2 = amigos_usuario2 - amigos_em_comum

print(f"Usuário 1: {usuario_random1}")
print(f"Amigos de {usuario_random1}: {amigos_usuario1}")
print(f"Amigos exclusivos de {usuario_random1}: {amigos_exclusivos_usuario1}")

print(f"\nUsuário 2: {usuario_random2}")
print(f"Amigos de {usuario_random2}: {amigos_usuario2}")
print(f"Amigos exclusivos de {usuario_random2}: {amigos_exclusivos_usuario2}")

print(f"\nAmigos em comum entre {usuario_random1} e {usuario_random2}: {amigos_em_comum}")

print("*"*100)

print('11 Removendo Conexões ⭐⭐')
print('''Permita que o usuário remova um amigo da lista de conexões de um membro do INFwebNET 
      específico no dicionário criado no exercício 4.''')
print("Lista")

for perfil in perfis_validos:
    amigos = ', '.join(perfil.amigos)
    print(f'Usuario: {perfil.nome} Amigos: {amigos}')
    
usuario_remover = input("Remova um amigo pelo nome (pressione Enter para usar 'Marcos'): ")
usuario_alvo = input("De quem você deseja remover o amigo? (pressione Enter para usar 'João')")

if not usuario_remover.strip():
    usuario_remover = "Marcos"
    
if not usuario_alvo.strip():    
    usuario_alvo = "João"

def remover_amigo(usuario_alvo, amigo_remover):
    for perfil in perfis_validos:
        if perfil.nome.lower() == usuario_alvo.lower():
            if amigo_remover in perfil.amigos:
                perfil.amigos.remove(amigo_remover)
                print(f"{amigo_remover} foi removido da lista de amigos de {usuario_alvo}.")
            else:
                print(f"{amigo_remover} não é amigo de {usuario_alvo}.")
            return
    print(f"Usuário {usuario_alvo} não encontrado.")

for perfil in perfis_validos:
    if perfil.nome.lower() == usuario_alvo.lower():
        print(f"Amigos de {usuario_alvo} Antes: {perfil.amigos}")
    
remover_amigo(usuario_alvo, usuario_remover)

for perfil in perfis_validos:
    if perfil.nome.lower() == usuario_alvo.lower():
        print(f"Amigos de {usuario_alvo} Depois: {perfil.amigos}")

print("*"*100)

print('12 Salvando o Progresso ⭐⭐')
print('''Após adicionar ou remover amigos, salve o dicionário atualizado 
      em um novo arquivo chamado "rede_INFNET_atualizado.txt".''')

diretorio = os.getcwd()
diretorio_e_arquivo = os.path.join(diretorio, 'rede_INFNET_atualizado.txt') 
with open(diretorio_e_arquivo, "w", encoding="utf-8") as file:
    file.writelines('Nome|Idade|Localização(Cidade, Estado)|Amigos(Lista)\n')
    for perfil in perfis_validos:
        file.writelines(f"{perfil.nome}|{perfil.idade}|{perfil.localizacao}|{', '.join(perfil.amigos)}\n")

print("*"*100)

print('13 Listando Usuários ⭐')
print('''Escreva um programa que leia o arquivo "rede_INFNET.txt" e imprima na tela a 
      lista dos nomes de todos os usuários da rede social.''')
diretorio = os.getcwd()
diretorio_e_arquivo = os.path.join(diretorio, 'rede_INFNET.txt') 
df13= pd.read_csv(diretorio_e_arquivo, sep='|', header=0, 
                     names=["Nome", "Idade", "Localização(Cidade, Estado)", "Amigos(Lista)"])

for index, row in df13.iterrows():
        nome1 = row['Nome']
        print(f'Nome do Usuario: {nome1}')

print("*"*100)

print('14 Quantidade de Amigos ⭐⭐')
print('''Crie uma função que leia o arquivo "rede_INFNET.txt" e mostre quantos amigos cada 
      usuário possui, imprimindo o nome do usuário e a quantidade de amigos.''')
diretorio = os.getcwd()
diretorio_e_arquivo = os.path.join(diretorio, 'rede_INFNET.txt') 
df14 = pd.read_csv(diretorio_e_arquivo, sep='|', header=0, 
                     names=["Nome", "Idade", "Localização(Cidade, Estado)", "Amigos(Lista)"])

for index, row in df14.iterrows():
        nome2 = row['Nome']
        amigos = row['Amigos(Lista)'].split(', ') if pd.notna(row['Amigos(Lista)']) else []
        quantidade_amigos = len(amigos)
        print(f'Nome do Usuario: {nome2} | Quantidade de amigos: {quantidade_amigos}')
print("*"*100)

print('15 Usuários Mais Populares ⭐⭐⭐')
print('''Analise o arquivo "rede_INFNET_atualizado.txt" e identifique os 5 usuários que foram 
      marcados como amigos pelo maior número de usuários cadastrados. Exiba o nome desses 
      usuários e a quantidade de amigos que cada um possui.''')
diretorio = os.getcwd()
diretorio_e_arquivo = os.path.join(diretorio, 'rede_INFNET_atualizado.txt') 
df15 = pd.read_csv(diretorio_e_arquivo, sep='|', header=0, 
                     names=["Nome", "Idade", "Localização(Cidade, Estado)", "Amigos(Lista)"])

contagem_amigos = {}
for index, row in df15.iterrows():
    amigos = row['Amigos(Lista)'].split(', ') if pd.notna(row['Amigos(Lista)']) else []
    for amigo in amigos:
        if amigo in contagem_amigos:
            contagem_amigos[amigo] += 1
        else:
            contagem_amigos[amigo] = 1
            
usuarios_populares = sorted(contagem_amigos.items(), key=lambda x: x[1], reverse=True)[:5]
print("Os 5 usuários mais marcados como amigos:")
for usuario, quantidade in usuarios_populares:
    print(f"{usuario}: {quantidade} amigos")
    
print("*"*100)

print('16 Lidando com arquivos ⭐⭐')
print('''Explique com suas palavras a importância de utilizar o 
      recurso ‘with’ ao lidar com arquivos em Python.''')
print('R: O principal motivo de se usar o ‘with’ é evitar de deixar os arquivos abertos, pois sem ele você precisa fechar manualmente, as vezes o codigo pode dar erro antes de conseguir fechar o arquivo, deixando ele aberto impossibilitando que outro processo o abra, já com o ‘with’ mesmo dando erro ele mesmo fecha o arquivo sem salvar.')

print("*"*100)