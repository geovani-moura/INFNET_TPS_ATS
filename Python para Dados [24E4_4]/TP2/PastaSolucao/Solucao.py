import csv
import json
import pandas as pd
from datetime import datetime
import ast
import uuid 
import numpy as np

print('1. (★) Abrindo as Portas:')
print('''
Escreva um programa que leia o arquivo ""rede_INFNET_atualizado.txt" que foi elaborado no seu TP1, 
que contém dados básicos dos usuários (nome, idade, cidade, estado) - INFNETianos;
Utilizando a biblioteca csv, exporte um arquivo “INFwebNet.csv” contendo os mesmos dados.
''')

def LerCSV(nomeArquivo, divisor):
    """
    Lê um arquivo CSV, processa seus dados e retorna uma lista de registros como dicionários.

    O CSV pode conter campos complexos, como tuplas e listas, que serão tratados:
    - O campo "Localização(Cidade, Estado)" é convertido para uma tupla `(cidade, estado)` se armazenado como string.
    - O campo "Amigos(Lista)" é convertido para uma lista de strings se armazenado como string separada por vírgulas.

    Args:
        nomeArquivo (str): Caminho do arquivo CSV a ser lido.
        divisor (str): Caractere que separa os campos no CSV.

    Returns:
        list[dict]: Lista de registros, onde cada registro é representado como um dicionário.
    """
    with open(nomeArquivo, "r", encoding="utf-8") as ler:
        leitorCSV = csv.reader(ler, delimiter=divisor)
        cabecalho = next(leitorCSV)
        dados = []
        
        for linha in leitorCSV:
            registro = dict(zip(cabecalho, linha))
            
            ##Tratativa para arrumar o CSV que erroneamente deixei com 2 tipos diferentes de dados no mesmo campo
            if registro["Localização(Cidade, Estado)"]:
                localizacao = registro["Localização(Cidade, Estado)"]
                if "(" in localizacao and ")" in localizacao:
                    registro["Localização(Cidade, Estado)"] = eval(localizacao)
                else: 
                    cidade, estado = [item.strip() for item in localizacao.split(",")]
                    registro["Localização(Cidade, Estado)"] = (cidade, estado)
            
            if registro["Amigos(Lista)"]:
                registro["Amigos(Lista)"] = registro["Amigos(Lista)"].split(', ')
            
            dados.append(registro)
    
    return dados

def EscreverCSV(nomeArquivo, divisor, dados):
    """
    Escreve uma lista de registros em um arquivo CSV.

    Cada registro é um dicionário, e os campos complexos, como tuplas e listas, são convertidos:
    - Tuplas são convertidas para strings.
    - Listas são convertidas para strings separadas por vírgulas.

    Args:
        nomeArquivo (str): Caminho do arquivo CSV a ser escrito.
        divisor (str): Caractere que separa os campos no CSV.
        dados (list[dict]): Lista de registros, onde cada registro é representado como um dicionário.
    """
    with open(nomeArquivo, "w", newline="", encoding="utf-8") as escrever:
        escritor = csv.writer(escrever, delimiter=divisor)
        
        cabecalho = dados[0].keys()
        escritor.writerow(cabecalho)
        
        for registro in dados:
            linha = []
            
            for key in cabecalho:
                valor = registro[key]
                if isinstance(valor, tuple): 
                    valor = str(valor)
                elif isinstance(valor, list):  
                    valor = ", ".join(valor)
                
                linha.append(valor)
            
            escritor.writerow(linha)

dadosExercicio1 = LerCSV("rede_INFNET_atualizado.txt", "|")
EscreverCSV("INFwebNet.csv", "|", dadosExercicio1)
print("*"*100)


print('2. (★★) Estruturando os Dados:')
print('''
Utilizando apenas as bibliotecas csv e json, leia os dados do arquivo csv criado no item anterior, 
parseie as informações para uma estrutura json e exporte o arquivo “INFwebNET.json” devidamente estruturado.
''')

def EscreverJSON(nomeArquivo, dados):
    """
    Escreve uma lista de registros ou dados em um arquivo JSON.

    Os dados fornecidos serão gravados no formato JSON com indentação para facilitar a leitura.
    A codificação UTF-8 é utilizada para suportar caracteres especiais.

    Args:
        nomeArquivo (str): Caminho do arquivo JSON a ser criado ou sobrescrito.
        dados (list[dict] | dict): Dados a serem gravados no arquivo. Pode ser uma 
        lista de dicionários ou um único dicionário.
    """
    with open(nomeArquivo, "w", encoding="utf-8") as nomeArquivo:
        json.dump(dados, nomeArquivo, ensure_ascii=False, indent=4)

dadosExercicio2 = LerCSV("INFwebNet.csv", "|")
EscreverJSON("INFwebNet.json", dadosExercicio2)

print("*"*100)

print('3. (★★) Cadastro Simplificado:')
print('''
Crie um programa que permita ao usuário inserir novos INFNETianos (nome, idade, cidade, estado) e 
salve essas informações no arquivo "“INFwebNET.json", utilizando o módulo json.
''')


def LerJSON(nomeArquivo):
    """
    Lê e retorna o conteúdo de um arquivo JSON.

    Args:
        nomeArquivo (str): Caminho do arquivo JSON a ser lido.

    Returns:
        dict | list: Dados lidos do arquivo JSON.
    """
    with open(nomeArquivo, "r", encoding="utf-8") as ler:
        return json.load(ler)

def getNome():
    """
    Solicita ao usuário o nome e retorna o valor digitado. 
    Caso nenhum valor seja fornecido, retorna "Geovani".

    Returns:
        str: Nome fornecido pelo usuário ou o valor padrão "Geovani".
    """
    retorno = input("Nome: ").strip() or "Geovani"
    print(f"Valor Digitado: {retorno}")
    return retorno

def getIdade():
    """
    Solicita ao usuário a idade e retorna o valor digitado.
    Caso nenhum valor seja fornecido, retorna "32".

    Returns:
        str: Idade fornecida pelo usuário ou o valor padrão "32".
    """
    retorno = input("Idade: ").strip() or "32"
    print(f"Valor Digitado: {retorno}")
    return retorno

def getCidade():
    """
    Solicita ao usuário o nome da cidade e retorna o valor digitado.
    Caso nenhum valor seja fornecido, retorna "São Paulo".

    Returns:
        str: Cidade fornecida pelo usuário ou o valor padrão "São Paulo".
    """
    retorno = input("Cidade: ").strip() or "São Paulo"
    print(f"Valor Digitado: {retorno}")
    return retorno

def getEstado():
    """
    Solicita ao usuário o estado e retorna o valor digitado.
    Caso nenhum valor seja fornecido, retorna "SP".

    Returns:
        str: Estado fornecido pelo usuário ou o valor padrão "SP".
    """
    retorno = input("Estado: ").strip() or "SP"
    print(f"Valor Digitado: {retorno}")
    return retorno

def addINFNETiano():
    """
    Solicita ao usuário as informações de um novo INFNETiano, como nome, idade, cidade e estado.
    As entradas não fornecidas recebem valores padrão.

    Returns:
        dict: Dicionário contendo os dados do INFNETiano:
            - "Nome" (str): Nome do INFNETiano.
            - "Idade" (str): Idade do INFNETiano.
            - "Localização(Cidade, Estado)" (list[str]): Lista contendo cidade e estado.
    """
    nome = getNome()
    idade = getIdade()
    cidade = getCidade()
    estado = getEstado()
    return {"Nome": nome, "Idade": idade, "Localização(Cidade, Estado)": [cidade, estado]}

dadosExercicio3 = LerJSON("INFwebNet.json")
loop = input("Quer adicionar um INFNETiano? (s/n): ").strip().lower()
while loop == "s":
    dadosExercicio3.append(addINFNETiano())
    loop = input("Quer adicionar outro INFNETiano? (s/n): ").strip().lower()

EscreverJSON("INFwebNet.json", dadosExercicio3)
print("*"*100)


print('4. (★) Análise com Pandas:')
print('''
Utilize o Pandas para ler o arquivo "“INFwebNET.json". Calcule a média de idade dos INFNETianos e exiba o resultado.
''')

def LerPandaJSON(nomeArquivo):
    """
    Lê um arquivo JSON e o carrega em um DataFrame do pandas.

    Args:
        nomeArquivo (str): Caminho do arquivo JSON a ser lido.

    Returns:
        pandas.DataFrame: O conteúdo do arquivo JSON carregado em um DataFrame.
    """
    return pd.read_json(nomeArquivo, encoding="utf-8")

df4 = LerPandaJSON("INFwebNet.json")
df4["Idade"] = pd.to_numeric(df4["Idade"], errors="coerce")

somaIdades = 0
quantidade = 0

for idade in df4["Idade"]:
    if not pd.isna(idade):
        somaIdades += idade
        quantidade += 1

mediaIdade = int(somaIdades / quantidade)
print(f"A média de idade dos INFNETianos é: {mediaIdade:.2f}")
print("*"*100)


print('5. (★★★) Ampliando as Informações:')
print('''
Elabore uma função que permita inserir novos INFNETianos na rede INFwebNet incluindo novos campos de dados. 
Além dos dados já existentes poderão serem incluídos os campos “hobbys” que conterá uma lista de atividades de 
interesse do INFNETiano, um campo “coding” que deverá conter uma lista de linguagens de programação que 
INFNETiano utiliza e uma lista de dicionários contendo os campos “jogos” e “plataforma”, onde o usuário poderá 
informar os jogos favoritos e a respectiva plataforma na qual o INFNETiano jogou aquele jogo.
''')

def addHobbies():
    """
    Solicita ao usuário a inserção de até 5 hobbies. O usuário pode adicionar 
    hobbies individualmente ou decidir não adicionar mais.

    Retorna:
        list: Lista contendo até 5 hobbies inseridos pelo usuário.
    """
    retornoLista = []
    while len(retornoLista) < 5: 
        retorno = input("Digite um hobby: (Exemplo: Jogar, Nadar, Estudar): ").strip() or "Brincar"
        print(f"Valor Digitado: {retorno}")
        if retorno:
            retornoLista.append(retorno)
        if len(retornoLista) < 5:
            adicionar_mais = input("Deseja adicionar mais hobbies? (s/n): ").strip().lower()
            if adicionar_mais != 's':
                break
        else:
            print("Limite de 5 hobbies atingido.")
            break
    return retornoLista

def addCoding():
    """
    Solicita ao usuário a inserção de até 5 linguagens de programação. O usuário pode adicionar 
    linguagens individualmente ou decidir não adicionar mais.

    Retorna:
        list: Lista contendo até 5 linguagens de programação inseridas pelo usuário.
    """
    retornoLista = []
    while True:
        retorno = input("Digite uma linguagem de programação: (Exemplo: C#, Java, Javascript): ").strip() or "Python"
        print(f"Valor Digitado: {retorno}")
        if retorno:
            retornoLista.append(retorno)
        if len(retornoLista) < 5:
            adicionar_mais = input("Deseja adicionar mais linguagens de programação? (s/n): ").strip().lower()
            if adicionar_mais != 's':
                break
        else:
            print("Limite de 5 linguagens de programação atingido.")
            break
    return retornoLista

def addJogosEPlataformas():
    """
    Solicita ao usuário a inserção de até 5 jogos e suas respectivas plataformas. O usuário pode adicionar jogos e 
    plataformas individualmente ou decidir não adicionar mais.

    Retorna:
        list: Lista de listas, onde cada sublista contém o nome do jogo e sua plataforma correspondente.
    """
    jogosPlataformas = []
    while len(jogosPlataformas) < 5:
        jogo = input("Digite um Jogo: (Exemplo: The Witcher 3)").strip() or "Jogo"
        print(f"Valor Digitado: {jogo}")
        if jogo:
            plataforma = input(f"Digite a plataforma do jogo '{jogo}': (Exemplo: Xbox, PC): ").strip() or "Plataforma"
            print(f"Valor Digitado: {plataforma}")
            if plataforma:
                jogosPlataformas.append([jogo, plataforma])
        
        if len(jogosPlataformas) < 5:
            adicionar_mais = input("Deseja adicionar mais Jogos e Plataformas? (s/n): ").strip().lower()
            if adicionar_mais != 's':
                break
        else:
            print("Limite de 5 jogos e plataformas atingido.")
            break

    return jogosPlataformas

def addNovosCamposINFNETiano():
    """
    Solicita a inserção de novos dados para um INFNETiano, incluindo hobbies, linguagens de 
    programação e jogos com plataformas.

    Retorna:
        dict: Dicionário contendo os dados básicos do INFNETiano, além de campos adicionais para hobbies, 
        linguagens de programação e jogos com plataformas.
    """
    dados = addINFNETiano() 
    hobbies = addHobbies()
    coding = addCoding()
    jogosEPlataforma = addJogosEPlataformas()
    return dados | { "Hobbies": hobbies, "Coding": coding, "Jogos": jogosEPlataforma}

dadosExercicio5 = LerJSON("INFwebNet.json")
loop = input("Quer adicionar um INFNETiano com novos campos? (s/n): ").strip().lower()
while loop == "s":
    usuario = addNovosCamposINFNETiano()
    dadosExercicio5.append(usuario)
    loop = input("Quer adicionar outro INFNETiano? (s/n): ").strip().lower()

EscreverJSON("INFwebNet.json", dadosExercicio5)
print("*"*100)


print('6. (★★) Dados Delimitados:')
print('''
A INFwebNET recebeu um arquivo "dados_usuarios_novos.txt" com dados dos novos INFNETianos separados por ponto e vírgula (;). 
Utilize o módulo csv para ler esse arquivo, especificando o delimitador correto. 
(O arquivo está disponível no repositório específico do TP2).
''')

def LerCSVNovos(nomeArquivo, divisor):
    """
    Lê um arquivo CSV, processa e converte os dados em um formato estruturado, tratando campos 
    específicos como listas ou tuplas.

    Parâmetros:
        nomeArquivo (str): O nome ou caminho do arquivo CSV a ser lido.
        divisor (str): O caractere que separa os campos no arquivo CSV (por exemplo, ',' ou '|').

    Retorna:
        list: Uma lista de dicionários, onde cada dicionário contém os dados de um usuário processados a partir do CSV.
              As chaves incluem "Nome", "Email", "Idade", "DataDeNascimento", "Localização(Cidade, Estado)", "Hobbies",
              "Coding" e "Jogos(Nome, Plataforma)".
    """
    with open(nomeArquivo, "r", encoding="utf-8") as ler:
        leitorCSV = csv.reader(ler, delimiter=divisor)
        cabecalho = next(leitorCSV)
        dados = []
        
        for linha in leitorCSV:
            registro = dict(zip(cabecalho, linha))

            jogosSTR = registro["jogos"]
            jogos = ast.literal_eval(jogosSTR)
            jogos = [[jogo[0], jogo[1]] for jogo in jogos]

            hobbies = ast.literal_eval(registro["hobbies"])
            coding = ast.literal_eval(registro["linguagens de programação"])

            dado = { 
                "Nome": registro["nome"] + registro["sobrenome"],
                "Email": registro["email"],
                "Idade": registro["idade"],
                "DataDeNascimento": registro["data de nascimento"],
                "Localização(Cidade, Estado)": (registro["cidade"], registro["estado"]),
                "Hobbies": hobbies,
                "Coding": coding, 
                "Jogos(Nome, Plataforma)": jogos
            }            
                        
            dados.append(dado)
    
    return dados

dados = LerCSVNovos('dados_usuarios_novos.txt', ';')
print("*"*100)


print('7. (★★★) Organizando a Bagunça:')
print('''
Após ter obtido dados de diferentes bases de dados você precisa avançar um passo e reunir todas as informações do INFwebNet 
em um único DataFrame Pandas. (Lembre-se de estruturar as Séries adequadamente).
''')

def ReunirINFwebNet():
    """
    Une dois conjuntos de dados (antigo e novo) em um único DataFrame, garantindo que todas as entradas 
    possuam um identificador único ("ID").
    
    A função realiza os seguintes passos:
    1. Converte as listas de dados antigos e novos em DataFrames.
    2. Adiciona uma coluna "ID" caso ela não exista em ambos os DataFrames.
    3. Preenche os valores ausentes na coluna "ID" com valores únicos gerados por `uuid.uuid4()`.
    4. Concatena os dois DataFrames em um único DataFrame unificado.
    
    Retorna:
        pd.DataFrame: Um DataFrame unificado contendo os dados antigos e novos, com uma coluna "ID" única para cada linha.
    """
    old = pd.DataFrame(dadosAntigosExercicio7)
    new = pd.DataFrame(dadosNovosExercicio7)

    if "ID" not in old.columns:
        old["ID"] = np.nan
    if "ID" not in new.columns:
        new["ID"] = np.nan

    old["ID"] = old["ID"].fillna("").apply(lambda x: x if x else uuid.uuid4().hex)
    new["ID"] = new["ID"].fillna("").apply(lambda x: x if x else uuid.uuid4().hex)

    dfUnificado = pd.concat([old, new], ignore_index=True)
    
    return dfUnificado

def EscreverPandaJSON(nomeArquivo, df):
    """
    Escreve um DataFrame do Pandas em um arquivo JSON.

    A função converte um DataFrame em um formato JSON, utilizando a orientação 'records' 
    para criar uma lista de objetos JSON,
    onde cada linha do DataFrame se torna um objeto JSON.

    Parâmetros:
    nomeArquivo (str): O nome do arquivo JSON a ser criado ou substituído.
    df (pd.DataFrame): O DataFrame do Pandas a ser exportado para o arquivo JSON.

    Retorno:
    None: A função não retorna nada. O DataFrame é salvo no arquivo especificado.
    
    Exemplo de uso:
    EscreverPandaJSON("dados.json", meu_dataframe)
    """
    df.to_json(nomeArquivo, orient="records", force_ascii=False, indent=4)

dadosAntigosExercicio7 = LerJSON("INFwebNet.json")
dadosNovosExercicio7 = LerCSVNovos('dados_usuarios_novos.txt', ';')
df_exercicio7 = ReunirINFwebNet()
EscreverPandaJSON("INFwebNet.json", df_exercicio7)
print("*"*100)


print('8. (★★) Criando Informações:')
print('''
Crie uma nova coluna no dataset chamada “ano_nascimento” considerando a data atual e informação presente na coluna idade.
''')

def calculaAnoNascimento(df):
    """
    Calcula o ano de nascimento com base na idade dos indivíduos no DataFrame.

    A função recebe um DataFrame com a coluna "Idade" e calcula o ano de nascimento
    para cada linha, subtraindo a idade atual do ano atual. A coluna "ano_nascimento"
    é então adicionada ao DataFrame.

    Parâmetros:
    df (pd.DataFrame): O DataFrame contendo uma coluna "Idade", com as idades dos indivíduos.

    Retorno:
    pd.DataFrame: O DataFrame original com a coluna adicional "ano_nascimento", 
                  que contém os anos de nascimento calculados.

    Observações:
    - Se a idade for ausente (NaN ou vazia), o ano de nascimento será atribuído como `None`, 
      mas posteriormente será preenchido com o valor `0` e convertido para inteiro.
    - O ano atual é calculado dinamicamente com base na data do sistema.

    Exemplo de uso:
    df = calculaAnoNascimento(df)
    """
    anoAtual = datetime.now().year
    anoNascimento = []

    for idade in df["Idade"]:
        if pd.notna(idade) and idade != "":
            data = anoAtual - int(float(idade))
            anoNascimento.append(data)
        else:
            anoNascimento.append(None)

    df["ano_nascimento"] = anoNascimento
    df["ano_nascimento"] = df["ano_nascimento"].fillna(0).astype(int)
    return df

df8 = calculaAnoNascimento(df_exercicio7)
EscreverPandaJSON("INFwebNet.json", df8)
print("*"*100)


print('9. (★★) Completando os Dados:')
print('''
Considerando os campos existentes no dataset obtido, utilize o Pandas para preencher adequadamente 2 campos onde houverem valores ausentes. 
Explique e justifique o critério utilizado.
''')
# ------
#Usamos os campos:
#Idade:
#Justificativa: Quando a Idade está em branco, a estratégia utilizada foi tentar calcular a Idade com base na Data de Nascimento. 
#Isso porque a Idade é uma informação diretamente derivada da Data de Nascimento, o que torna esse preenchimento mais preciso e confiável. 
#Caso a Data de Nascimento também esteja ausente, optamos por usar a média de Idade de todos os registros como uma solução temporária, 
#pois essa abordagem fornece um valor razoável para preencher a lacuna.

#Data de Nascimento:
#Justificativa: Quando a Data de Nascimento está em branco, a solução adotada é calcular a Data de Nascimento com 
#base na Idade previamente calculada. O ano de nascimento é obtido subtraindo a Idade do ano atual, e a data é ajustada para 
#o dia 1º de janeiro desse ano. Essa abordagem é válida, pois a Idade já foi derivada com base na data de nascimento, 
#garantindo que o cálculo seja coerente com os dados disponíveis.

def isVazioBrancoNull(campo):
    """
    Verifica se o campo está vazio, em branco ou é nulo (NaN).

    Parâmetros:
    campo (any): O valor a ser verificado.

    Retorno:
    bool: Retorna True se o campo for vazio, branco ou nulo (NaN), caso contrário, retorna False.
    
    Exemplo de uso:
    isVazioBrancoNull(" ")  # Retorna True
    isVazioBrancoNull(None)  # Retorna True
    isVazioBrancoNull("Texto")  # Retorna False
    """
    return pd.isna(campo) or campo == "" or str(campo).strip() == ""

def retirarValoresAusentes(df):
    """
    Substitui valores ausentes (nulos ou em branco) na coluna 'Idade' e 'ano_nascimento' com 
    base em regras específicas:
    - Se a Idade estiver vazia e o ano_nascimento não, calcula a Idade.
    - Se o ano_nascimento estiver vazio e a Idade não, calcula o ano_nascimento.
    - Se ambos estiverem vazios, preenche com a média da Idade.

    Parâmetros:
    df (pd.DataFrame): O DataFrame que será modificado.

    Retorno:
    pd.DataFrame: O DataFrame com valores ausentes nas colunas 'Idade' e 'ano_nascimento' preenchidos.

    Observações:
    - A média da Idade (`mediaIdade`) é usada quando ambos os campos estão ausentes.
    - A função assume que a variável `mediaIdade` foi previamente definida.
    
    Exemplo de uso:
    df = retirarValoresAusentes(df)
    """
    ano_atual = datetime.now().year
    
    for index, row in df.iterrows():
        # Se a Idade estiver vazia e ano_nascimento não, calcula a Idade com base no ano_nascimento
        if isVazioBrancoNull(row["Idade"]) and not isVazioBrancoNull(row["ano_nascimento"]):
            df.at[index, "Idade"] = ano_atual - int(row["ano_nascimento"])
        
        # Se ano_nascimento estiver vazio e Idade não, calcula ano_nascimento com base na Idade
        if isVazioBrancoNull(row["ano_nascimento"]) and not isVazioBrancoNull(row["Idade"]):
            df.at[index, "ano_nascimento"] = f"{ano_atual - int(float(row['Idade']))}"
        
        # Se ambos os campos estiverem vazios, preenche com valores baseados na média da Idade
        if isVazioBrancoNull(row["Idade"]) and isVazioBrancoNull(row["ano_nascimento"]):
            df.at[index, "Idade"] = mediaIdade
            df.at[index, "ano_nascimento"] = f"{ano_atual - int(mediaIdade)}"
    
    return df

df9 = retirarValoresAusentes(df8)
EscreverPandaJSON("INFwebNet.json", df9)
print("*"*100)

print('10. (★) Guardando as Informações:')
print('''
Utilizando o Pandas salve todo o banco de dados do INFwebNet em um arquivo json chamado “INFwebNet_Data.json”
''')

df10 = LerPandaJSON("INFwebNet.json")
EscreverPandaJSON("INFwebNet_Data.json", df10)
print("*"*100)


print('11. (★★) Selecionando Grupos:')
print('''
Utilize o pandas para filtrar os INFNETianos pelo estado onde mora. Salve os usuários de cada estado em um arquivo csv nomeado como 
“grupo_##.csv”, onde ## deve ser substituído pela sigla do estado.
''')

def EscreverPandaCSV(df, nomeArquivo, divisor):
    """
    Escreve um DataFrame em um arquivo CSV.

    Parâmetros:
    df (pd.DataFrame): O DataFrame que será escrito no arquivo CSV.
    nomeArquivo (str): O nome do arquivo CSV onde o DataFrame será salvo.
    divisor (str): O caractere que será usado para separar os valores no CSV (ex: '|' ou ',').

    Retorno:
    Nenhum.

    Exemplo de uso:
    EscreverPandaCSV(df, "saida.csv", "|")
    """
    df.to_csv(nomeArquivo, index=False, encoding="utf-8", sep=divisor)

def EscreverPorEstado(df):
    """
    Filtra o DataFrame por estado e escreve arquivos CSV separados por estado.

    Para cada estado encontrado na coluna 'Localização(Cidade, Estado)', a função cria
    um arquivo CSV contendo as linhas correspondentes a esse estado, com o nome do arquivo
    sendo no formato 'grupo_{estado}.csv'. O caractere de separação utilizado no arquivo CSV
    será o pipe ('|').

    Parâmetros:
    df (pd.DataFrame): O DataFrame a ser filtrado e escrito em arquivos CSV.

    Retorno:
    Nenhum.

    Exemplo de uso:
    EscreverPorEstado(df)
    """
    estados = df["Localização(Cidade, Estado)"].dropna().apply(
        lambda x: x[1] if isinstance(x, (list, tuple)) and len(x) > 1 else None
    ).dropna().unique()

    for estado in estados:
        df_filtro = df[df["Localização(Cidade, Estado)"].apply(
            lambda x: isinstance(x, (list, tuple)) and len(x) > 1 and x[1] == estado
        )]
        nomeArquivo = f"grupo_{estado}.csv"
        EscreverPandaCSV(df_filtro, nomeArquivo, '|')

df11 = LerPandaJSON("INFwebNet.json")
EscreverPorEstado(df11)
print("*"*100)


print('12. (★) Agrupando INFNETianos:')
print('''
Crie uma função que seja capaz de filtrar usuários por ano de nascimento, dado dois valores de ano e exiba todos os usuários 
que nasceram nestes anos.
''')

df12 = LerPandaJSON("INFwebNet.json")
def FiltrarPorAnoNascimento(df, ano_inicial, ano_final):
    """
    Filtra um DataFrame com base no ano de nascimento, retornando os registros que possuem
    ano de nascimento dentro do intervalo especificado.

    Parâmetros:
    df (pd.DataFrame): O DataFrame contendo os dados a serem filtrados.
    ano_inicial (int): O ano inicial do intervalo a ser considerado.
    ano_final (int): O ano final do intervalo a ser considerado.

    Retorno:
    pd.DataFrame: Um DataFrame contendo apenas os registros cujos anos de nascimento
                  estão dentro do intervalo especificado.

    Exemplo de uso:
    df_filtrado = FiltrarPorAnoNascimento(df, 1990, 2000)
    """
    usuarios_filtrados = []
    
    for index, row in df.iterrows():
        if not isVazioBrancoNull(row["ano_nascimento"]):
            ano_nascimento = int(row["ano_nascimento"])
            if ano_inicial <= ano_nascimento <= ano_final:
                usuarios_filtrados.append(row)
    
    return pd.DataFrame(usuarios_filtrados)

print(f"Filtro: 1990 a 2000")
usuarios_filtrados = FiltrarPorAnoNascimento(df12, 1990, 2000)
for i, (_, usuario) in enumerate(usuarios_filtrados.iterrows(), start=1):
    if i > 10:
        break
    print(f"Nome: {usuario['Nome']} | Ano de Nascimento: {usuario['ano_nascimento']}")

print("Exemplo contendo apenas os 10 primeiros.")
print("*"*100)


print('13. (★★★) Selecionando INFNETiano:')
print('''
Crie uma função que permita buscar um usuário pelo nome e exiba o(s) INFNETiano(s) 
que possui(em) 
este nome e permita o usuário selecionar o INFNETiano.
''')

def BuscarPorNome(df, nome_busca):
    """
    Busca por um nome dentro de um DataFrame e retorna o registro correspondente ao nome mais 
    próximo encontrado.
    Exibe os resultados encontrados e permite ao usuário escolher um deles.

    Parâmetros:
    df (pd.DataFrame): O DataFrame contendo os dados a serem pesquisados.
    nome_busca (str): O nome (ou parte dele) que será buscado na coluna 'Nome' do DataFrame.

    Retorno:
    dict ou None: Retorna o registro (linha do DataFrame) correspondente ao nome encontrado, 
    ou None se nenhum nome for encontrado.

    Exemplo de uso:
    usuario = BuscarPorNome(df, "Geovani")
    """
    usuarios_encontrados = []
    
    for index, row in df.iterrows():
        if isinstance(row["Nome"], str) and nome_busca.lower() in row["Nome"].lower():
            usuarios_encontrados.append(row)
    
    if usuarios_encontrados:
        for i, usuario in enumerate(usuarios_encontrados, 1):
            print(f"{i}. {usuario['Nome']}")
        
        print('Selecione o número do INFNETiano (Padrão 1 caso não dite nada)')
        escolha = int(input("Número: ") or '1')
        return usuarios_encontrados[escolha - 1]
    else:
        print("Nenhum usuário encontrado com esse nome.")
        return None

df12 = LerPandaJSON("INFwebNet.json")
print("Digite o nome do INFNETiano (Se não digitar nada ele pega todos):")
nome_busca = input("Nome: ")
usuario_selecionado = BuscarPorNome(df12, nome_busca)

if usuario_selecionado is not None:
    print(f"Usuário selecionado: {usuario_selecionado['Nome']}")

print("*"*100)


print('14. (★★) Atualizando Dados:')
print('''
Após o INFNETiano ter sido selecionado no item anterior permita que seus dados sejam atualizados. 
Lembrando que deve haver um limite de até 5 hobbies e 5 jogos.
''')

def getDataDeNascimento():
    """
    Solicita ao usuário uma nova data de nascimento no formato 'YYYY-MM-DD' e retorna o valor informado.
    Caso o usuário não forneça uma data, um valor padrão ('1992-09-30') é retornado.

    Retorno:
    str: A data de nascimento informada pelo usuário, no formato 'YYYY-MM-DD'.

    Exemplo de uso:
    data_nascimento = getDataDeNascimento()
    """
    retorno = input("Informe a nova Data de Nascimento (YYYY-MM-DD): ") or "1992-09-30"
    print(f"Valor Digitado: {retorno}")
    return retorno

def getEmail():
    """
    Solicita ao usuário um novo email e retorna o valor informado.
    Caso o usuário não forneça um email, um valor padrão ('g@g.com.br') é retornado.

    Retorno:
    str: O email informado pelo usuário.

    Exemplo de uso:
    email = getEmail()
    """
    retorno = input("Informe o novo email: ") or "g@g.com.br"
    print(f"Valor Digitado: {retorno}")
    return retorno

def getAmigos():
    """
    Solicita ao usuário a inserção de nomes de amigos, permitindo que ele adicione vários amigos.
    Retorna uma lista contendo os nomes dos amigos ou uma lista vazia caso nenhum amigo seja inserido.

    Retorno:
    list: Lista de nomes dos amigos inseridos pelo usuário.

    Exemplo de uso:
    amigos = getAmigos()
    """
    amigos = []
    print("Digite o nome de amigos:")

    while True:
        amigo = input("Nome do amigo: ") or "Amigo"
        print(f"Valor Digitado: {amigo}")
        if amigo:
            amigos.append(amigo)
        
        adicionar_mais = input("Deseja adicionar mais um amigo? (s/n): ").strip().lower()
        if adicionar_mais != 's':
            break

    return amigos if amigos else []

def getAnoNascimento(data_nascimento):
    """
    Recebe uma data de nascimento no formato 'YYYY-MM-DD' e retorna o ano de nascimento.

    Parâmetros:
    data_nascimento (str): Data de nascimento no formato 'YYYY-MM-DD'.

    Retorno:
    int: O ano de nascimento extraído da data fornecida.

    Exemplo de uso:
    ano_nascimento = getAnoNascimento("1992-09-30")
    """
    data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')
    return data_nascimento.year

def atualizaINFNETiano(dados_atuais):
    """
    Exibe os dados atuais de um INFNETiano e solicita ao usuário para atualizar esses dados.
    Caso o usuário não forneça informações, são utilizados valores padrão.
    Retorna os dados do INFNETiano atualizados.

    Parâmetros:
    dados_atuais (dict): Dicionário contendo os dados atuais do INFNETiano. O dicionário pode conter as chaves:
        - 'Nome', 'Email', 'DataDeNascimento', 'Localização(Cidade, Estado)', 'Hobbies', 'Coding', 
        - 'Jogos', 'Plataformas', 'ano_nascimento', 'Amigos(Lista)'.
        
    Retorno:
    dict: Dicionário com os dados atualizados do INFNETiano, incluindo:
        - 'Nome', 'Email', 'DataDeNascimento', 'Localização(Cidade, Estado)', 'Hobbies', 'Coding', 
        - 'Jogos(Nome, Plataforma)', 'Plataformas', 'ano_nascimento', 'Amigos(Lista)'.

    Exemplo de uso:
    dados_atualizados = atualizaINFNETiano(dados_atuais)
    """
    print("Dados atuais do INFNETiano:")
    print(f"Nome: {dados_atuais['Nome'] if 'Nome' in dados_atuais else 'Não informado'}")
    print(f"Email: {dados_atuais['Email'] if 'Email' in dados_atuais else 'Não informado'}")
    print(f"Data De Nascimento: {dados_atuais['DataDeNascimento'] if 'DataDeNascimento' in dados_atuais else 'Não informado'}")
    print(f"Localização(Cidade, Estado): {dados_atuais['Localização(Cidade, Estado)'] if 'Localização(Cidade, Estado)' in dados_atuais else 'Não informado'}")
    print(f"Hobbies: {dados_atuais['Hobbies'] if 'Hobbies' in dados_atuais else 'Não informado'}")
    print(f"Coding: {dados_atuais['Coding'] if 'Coding' in dados_atuais else 'Não informado'}")
    print(f"Jogos: {dados_atuais['Jogos'] if 'Jogos' in dados_atuais else 'Não informado'}")
    print(f"Plataformas: {dados_atuais['Plataformas'] if 'Plataformas' in dados_atuais else 'Não informado'}")
    print()

    print("Informe os dados para atualizar (Existe um cadastro padrão caso não digite nada, Exemplo: [Nome: Geovani] [Amigos: Amigo])")
    dados = addINFNETiano() 
    datadeNascimento = getDataDeNascimento()
    email = getEmail()
    amigos = getAmigos()
    hobbies = addHobbies()
    coding = addCoding()
    jogosEPlataformas = addJogosEPlataformas()

    usuario_atualizado = dados | { 
        "DataDeNascimento": datadeNascimento, 
        "Email": email, 
        "Amigos(Lista)": amigos, 
        "Hobbies": hobbies, 
        "Coding": coding, 
        "Jogos(Nome, Plataforma)": jogosEPlataformas,
        "ano_nascimento": getAnoNascimento(datadeNascimento)
    }

    for chave, valor in usuario_atualizado.items():
        if chave in usuario_selecionado:
            usuario_selecionado[chave] = valor

    return usuario_selecionado

def AtualizarJSON(nomeArquivo, id_usuario, campo, valor_novo):
    """
    Atualiza um campo específico de um usuário no arquivo JSON.

    A função busca o usuário pelo ID e atualiza o valor do campo especificado com o novo valor. Após a atualização, 
    os dados são reescritos no arquivo JSON.

    Parâmetros:
    nomeArquivo (str): O nome do arquivo JSON onde os dados dos usuários estão armazenados.
    id_usuario (str): O ID do usuário a ser atualizado.
    campo (str): O nome do campo que será atualizado (ex: "Nome", "Email", etc).
    valor_novo (str): O novo valor que será atribuído ao campo especificado.

    Exemplo de uso:
    AtualizarJSON("usuarios.json", "12345", "Email", "novoemail@dominio.com")
    """
    usuarios = LerJSON(nomeArquivo)
    for usuario in usuarios:
        if usuario['ID'] == id_usuario:
            usuario[campo] = valor_novo
            break
    EscreverJSON(nomeArquivo, usuarios)

usuarioAlterado = atualizaINFNETiano(usuario_selecionado)
for chave, valor in usuarioAlterado.items():
    id = usuario_selecionado['ID']
    AtualizarJSON('INFwebNet.json', id, chave, valor)
print("*"*100)


print('15. (★★) Trending:')
print('''
Elabore um recurso que permita exibir as 5 linguagens mais citadas entre os INFNETianos e exiba contagem de vezes que cada uma foi citada.
''')

def listarLinguagens(df, coluna="Coding"):
    """
    Extrai todas as linguagens de programação de uma coluna específica de um DataFrame.

    A função percorre as entradas da coluna indicada (por padrão, "Coding") no DataFrame e extrai todas as linguagens
    de programação, assumindo que cada entrada seja uma lista. As linguagens são então reunidas em uma lista única.

    Parâmetros:
    df (pd.DataFrame): O DataFrame contendo os dados.
    coluna (str): O nome da coluna que contém a lista de linguagens. O padrão é "Coding".

    Retorna:
    list: Uma lista contendo todas as linguagens de programação presentes na coluna especificada.

    Exemplo de uso:
    linguagens = listarLinguagens(df)
    """
    linguagens = []
    for lista in df[coluna]:
        if isinstance(lista, list): 
            linguagens.extend(lista)
    return linguagens

def contarLinguagens(lista_linguagens):
    """
    Conta a frequência de cada linguagem de programação em uma lista.

    A função recebe uma lista de linguagens de programação e retorna um dicionário que mapeia cada linguagem
    à sua respectiva contagem de ocorrências.

    Parâmetros:
    lista_linguagens (list): Uma lista contendo linguagens de programação.

    Retorna:
    dict: Um dicionário com as linguagens como chave e as suas contagens como valor.

    Exemplo de uso:
    contagem = contarLinguagens(linguagens)
    """
    contagem = {}
    for linguagem in lista_linguagens:
        if linguagem in contagem:
            contagem[linguagem] += 1
        else:
            contagem[linguagem] = 1
    return contagem

def topLinguagens(contagem_linguagens, quantidade):
    """
    Retorna as linguagens de programação mais populares com base nas contagens.

    A função recebe um dicionário com as contagens das linguagens e retorna as linguagens mais frequentes.
    O número de linguagens retornadas é determinado pelo parâmetro `quantidade`.

    Parâmetros:
    contagem_linguagens (dict): Um dicionário com as linguagens como chave e as suas contagens como valor.
    quantidade (int): O número de linguagens mais populares a serem retornadas.

    Retorna:
    list: Uma lista de tuplas contendo a linguagem e a sua contagem, ordenada da mais popular para a menos popular.

    Exemplo de uso:
    top_5 = topLinguagens(contagem, 5)
    """
    return sorted(contagem_linguagens.items(), key=lambda x: x[1], reverse=True)[:quantidade]

def obterLinguagens(top):
    """
    Obtém as linguagens de programação mais populares a partir dos dados em um arquivo JSON.

    A função carrega os dados de linguagens de programação, conta a frequência de cada linguagem
    e retorna as `top` linguagens mais populares.

    Parâmetros:
    top (int): O número de linguagens mais populares a ser retornado.

    Retorna:
    list: Uma lista de tuplas contendo as linguagens e suas contagens, ordenadas pela popularidade.
    """
    df15 = LerPandaJSON("INFwebNet.json")
    todasLinguagens = listarLinguagens(df15)
    contagemLinguagens = contarLinguagens(todasLinguagens)
    return topLinguagens(contagemLinguagens, top)

top = 5
linguagensTop = obterLinguagens(top)

print(f"As {top} linguagens mais citadas entre os INFNETianos são:")
for linguagem, quantidade in linguagensTop:
    print(f"{linguagem}: {quantidade} vezes")