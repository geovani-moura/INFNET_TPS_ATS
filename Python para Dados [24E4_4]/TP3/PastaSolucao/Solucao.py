import csv
import pandas as pd
import os
import sqlite3
import re
from datetime import datetime
from sqlalchemy import create_engine

print('1. Tratamento de Erros ao Carregar Arquivo')
print('''
Abra o arquivo "dados_usuarios.csv" usando o bloco try...except. 
Exiba uma mensagem de erro se o arquivo não for encontrado (erro específico) 
e informe ao usuário que o arquivo está em falta.
''')
def ler_csv(nomeArquivo, divisor):           
    """
    Lê um arquivo CSV e retorna as colunas e os dados presentes nele.

    Args:
        nomeArquivo (str): Nome do arquivo CSV a ser lido.
        divisor (str): Caractere utilizado para separar os campos no arquivo CSV.

    Returns:
        dict: Dicionário contendo as colunas e os dados do arquivo CSV, ou None se o arquivo não for encontrado.
    
    Exceções:
        FileNotFoundError: Caso o arquivo não seja encontrado no local especificado.
    """         
    try:
        with open(nomeArquivo, "r", encoding="utf-8") as ler:
            leitorCSV = csv.reader(ler, delimiter=divisor)
            cabecalho = next(leitorCSV)
            dados = []
        
            for linha in leitorCSV:
                registro = dict(zip(cabecalho, linha))   
                dados.append(registro)

            return {'colunas': cabecalho, 'dados': dados}
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nomeArquivo}' não foi encontrado. Certifique-se de que ele está no local correto.")
        return None

retorno_errado = ler_csv('errado/dados_usuarios.csv', ';')
print("*"*100)


print('2. Explorando Dados do Excel')
print('''
Abra o arquivo "dados_usuarios.csv", que contém informações dos usuários. 
Exiba as 10 primeiras linhas do arquivo e liste todas as colunas presentes no arquivo.
''')
retorno_certo = ler_csv('dados_usuarios.csv', ';')
if retorno_certo:
    colunas = retorno_certo['colunas']
    primeiros_dados = retorno_certo['dados'][:10]
    print(f"Colunas: {colunas}")
    print("10 Primeiros:")
    for i, linha in enumerate(primeiros_dados, start=1):
        print(f"{i}: {linha}")

print("*"*100)


print('3. Manipulação de Dados Básica')
print('''
Usando Pandas, selecione apenas os usuários com idade maior que 30 e 
salve esses dados em um novo arquivo chamado "INFwebNET_30mais.xlsx".
''')
def ler_panda_csv(nomeArquivo, separador):
    """
    Lê um arquivo CSV e retorna um DataFrame.

    Args:
        nomeArquivo (str): Caminho do arquivo CSV a ser lido.
        separador (str): O separador utilizado no arquivo CSV.

    Returns:
        pd.DataFrame: DataFrame contendo os dados do arquivo CSV.
    """
    return pd.read_csv(nomeArquivo, sep=separador)

def escrever_panda_xlsx(df, nomeArquivo):
    """
    Escreve os dados de um DataFrame em um arquivo Excel.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados a serem escritos no arquivo.
        nomeArquivo (str): Nome do arquivo Excel onde os dados serão salvos.

    """
    df.to_excel(nomeArquivo, index=False)

df3 = ler_panda_csv('dados_usuarios.csv', ';')
filtro3 = df3[df3['idade'] > 30]
escrever_panda_xlsx(filtro3, 'INFwebNET_30mais.xlsx')

print("*"*100)


print('4. Limpeza de Dados')
print('''
Para o DataFrame anterior proceda com as seguintes tarefas de limpeza de dados:
a. Remova todos os usuários que não possuírem e-mail válido cadastrado.
b. Preencha os valores ausente do campo “cidade” com o texto “Não Informada”.
c. Preencha os dados ausentes na coluna “estado” com “ZZ”.
''')
def limpar_dados_email(df):
    """
    Limpa os dados da coluna 'email', atribuindo None aos valores que não correspondem ao formato de e-mail válido.

    Args:
        df (pd.DataFrame): DataFrame contendo a coluna 'email' a ser verificada e limpa.

    Returns:
        pd.DataFrame: DataFrame com a coluna 'email' limpa, contendo None nos casos de e-mails inválidos.
    """

    df['email'] = df['email'].apply(
        lambda x: x if pd.isna(x) or pd.Series(x).str.match(r'^[\w\.-]+@[\w\.-]+\.\w+$').bool() else None
    )
    return df

def preencher_dados_cidade(df):
    """
    Preenche os valores ausentes na coluna 'cidade' com o valor 'Não Informada'.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados a serem modificados.

    Returns:
        pd.DataFrame: DataFrame com os valores ausentes na coluna 'cidade' preenchidos com 'Não Informada'.
    """
    df.loc[:, 'cidade'] = df['cidade'].fillna('Não Informada')
    return df

def preencher_dados_estado(df):
    """
    Preenche os valores ausentes na coluna 'estado' com o valor 'ZZ'.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados a serem modificados.

    Returns:
        pd.DataFrame: DataFrame com os valores ausentes na coluna 'estado' preenchidos com 'ZZ'.
    """
    df.loc[:, 'estado'] = df['estado'].fillna('ZZ')
    return df

df4 = limpar_dados_email(df3)
df4 = preencher_dados_cidade(df4)
df4 = preencher_dados_estado(df4)
print(df4)

print("*"*100)


print('5. Combinação de Arquivos Excel')
print('''
A INFwebNET possui dados históricos de usuários em arquivo Excel com o nome “INFwebNET_Historico.xlsx”, 
onde há duas tabelas, “INFwebNET2022” e “INFwebNET2023”, cada uma referente a um ano.
Use um bloco try...except para carregar as planilhas do arquivo "INFwebNET_Historico.xlsx" e, 
se o arquivo for carregado com sucesso, exiba o número total de linhas de cada planilha. 
Caso ocorra uma exceção, mostre uma mensagem de erro apropriada.
''')

def ler_historico(arquivo):
    """
    Lê os dados das planilhas 'INFwebNET2022' e 'INFwebNET2023' de um arquivo Excel.

    Args:
        arquivo (str): Caminho do arquivo Excel contendo as planilhas.

    Returns:
        tuple: Dois DataFrames contendo os dados das planilhas 'INFwebNET2022' e 'INFwebNET2023', respectivamente.

    Raises:
        FileNotFoundError: Se o arquivo não for encontrado.
        ValueError: Se as planilhas 'INFwebNET2022' ou 'INFwebNET2023' não estiverem no arquivo.
        Exception: Se ocorrer qualquer outro erro inesperado.
    """
    try:
        df_2022 = pd.read_excel(arquivo, sheet_name='INFwebNET2022')
        df_2023 = pd.read_excel(arquivo, sheet_name='INFwebNET2023') 
        return df_2022, df_2023
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
    except ValueError:
        print(f"Erro: Não foi possível encontrar as planilhas 'INFwebNET2022' ou 'INFwebNET2023' no arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

ler_historico('errado/INFwebNET_Historico.xlsx')
print("-"*100)
ler_historico('INFwebNET_Historico.xlsx')
df5_2022, df5_2023 = ler_historico('INFwebNET_Historico.xlsx')
print(f"Número total de linhas de 2022: {len(df5_2022)}")
print(f"Número total de linhas de 2023: {len(df5_2023)}")

print("*"*100)


print('6. Combinação de Arquivos Excel')
print('''
Carregue a informação das duas planilhas, combine as informações em um único 
DataFrame e remova duplicatas baseado na coluna "id".
''')
def juntar_df(df1, df2):
    """
    Junta dois DataFrames em um único DataFrame, mantendo o índice contínuo.

    Args:
        df1 (pd.DataFrame): Primeiro DataFrame a ser unido.
        df2 (pd.DataFrame): Segundo DataFrame a ser unido.

    Returns:
        pd.DataFrame: DataFrame resultante da união dos dois DataFrames.
    """
    return pd.concat([df1, df2], ignore_index=True)   

def remover_duplicado(df, campo):
    """
    Remove duplicatas de um DataFrame com base em um campo específico.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados.
        campo (str): Nome do campo utilizado para verificar duplicatas.

    Returns:
        pd.DataFrame: DataFrame sem duplicatas baseadas no campo especificado.
    """
    return df.drop_duplicates(subset=campo)

df6_2022, df6_2023 = ler_historico('INFwebNET_Historico.xlsx')
df6 = juntar_df(df6_2022, df6_2023)
df6 = remover_duplicado(df6, 'id')
print(f"Número total de linhas de 2022 e 2023: {len(df6)}")

print("*"*100)


print('7. Carregando Dados em SQL')
print('''
Conecte-se a um banco de dados SQLite chamado "INFwebNET_DB.db" usando SQLAlchemy. 
Carregue os dados combinados do item anterior para uma tabela chamada "Usuarios_Historicos".
''')
def carregar_dados_Usuarios_Historicos(df):
    """
    Carrega os dados do DataFrame na tabela 'Usuarios_Historicos' do banco de dados SQLite.

    Args:
        df (pd.DataFrame): DataFrame com os dados a serem carregados.

    Raises:
        Exception: Lança uma exceção caso ocorra um erro ao carregar os dados no banco de dados.
    """
    try:
        engine = create_engine(f"sqlite:///INFwebNET_DB.db")        
        df.to_sql('Usuarios_Historicos', con=engine, if_exists='replace', index=False)
        print('Tabela Usuarios_Historicos carregada com sucesso.')
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados no banco de dados: {e}")

carregar_dados_Usuarios_Historicos(df6)
print("*"*100)


print('8. Consultando o Banco de Dados SQL')
print('''
Escreva uma consulta usando Pandas que retorne apenas os usuários com idade entre 22 e 30 anos 
existentes na tabela “Usuarios_Historicos”. Exiba o resultado na tela.
''')
def consultar_usuarios_idade():
    """
    Consulta a tabela 'Usuarios_Historicos' no banco de dados para retornar os usuários com idade entre 22 e 30 anos.

    Returns:
        pd.DataFrame: DataFrame contendo os dados dos usuários com idade entre 22 e 30 anos.

    Raises:
        Exception: Lança uma exceção caso ocorra um erro ao consultar o banco de dados.
    """
    try:
        engine = create_engine("sqlite:///INFwebNET_DB.db")
        
        consulta_sql = """
        SELECT * FROM Usuarios_Historicos
        WHERE idade BETWEEN 22 AND 30;
        """

        df_resultado = pd.read_sql(consulta_sql, con=engine)
        
        return df_resultado
        
    except Exception as e:
        print(f"Ocorreu um erro ao consultar o banco de dados: {e}")

df8 = consultar_usuarios_idade()
print(df8)
print("*"*100)


print('9. Consolidando Dados')
print('''
Utilizando o Pandas e SQLAlchemy crie uma nova tabela no banco de dados chamada 
“Consolidado” e insira nesta tabela todos os dados obtidos nos itens anteriores.
''')
def carregar_dados_consolidado(df):
    """
    Carrega os dados do DataFrame na tabela 'Consolidado' do banco de dados SQLite.

    Args:
        df (pd.DataFrame): DataFrame com os dados a serem carregados.

    Raises:
        Exception: Lança uma exceção caso ocorra um erro ao carregar os dados no banco de dados.
    """
    try:
        engine = create_engine(f"sqlite:///INFwebNET_DB.db")        
        df.to_sql('Consolidado', con=engine, if_exists='replace', index=False)
        print('Tabela Consolidado carregada com sucesso.')
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados no banco de dados: {e}")

carregar_dados_consolidado(df6)
carregar_dados_consolidado(df8)

print("*"*100)


print('10. Atualizando idade')
print('''
Consulte todos os dados da tabela “Consolidado” e recalcule a idade de todos os usuários 
considerando a data de 22 de julho de 2024. Exporte os dados atualizados para uma tabela 
SQL chamada “Consolidado_Atualizado”.
''')
def consultar_consolidado():
    """
    Consulta os dados da tabela 'Consolidado' no banco de dados SQLite e retorna o resultado como um DataFrame.

    Returns:
        pd.DataFrame: DataFrame contendo os dados da tabela 'Consolidado'.

    Raises:
        Exception: Lança uma exceção caso ocorra algum erro ao consultar o banco de dados.
    """
    try:
        engine = create_engine("sqlite:///INFwebNET_DB.db")
        
        consulta_sql = "SELECT * FROM Consolidado"

        df_resultado = pd.read_sql(consulta_sql, con=engine)
        
        return df_resultado
        
    except Exception as e:
        print(f"Ocorreu um erro ao consultar o banco de dados: {e}")

def recalcular_idade(data_nascimento, data_referencia='2024-07-22'):
    """
    Recalcula a idade com base na data de nascimento e na data de referência fornecida.

    Args:
        data_nascimento (str): Data de nascimento do usuário em formato 'YYYY-MM-DD'.
        data_referencia (str, opcional): Data de referência para calcular a idade, no formato 'YYYY-MM-DD'. O padrão é '2024-07-22'.

    Returns:
        int or None: A idade calculada ou None caso ocorra um erro no processamento da data de nascimento.
    
    Raises:
        Exception: Lança uma exceção caso ocorra um erro ao processar a data de nascimento.
    """
    idade = None
    if(data_nascimento):
        try:
            nascimento = pd.to_datetime(data_nascimento, errors='raise', dayfirst=False)
        except Exception as e:
            print(f"Erro ao processar a data de nascimento {data_nascimento}: {e}")
            return None
    
        referencia = datetime.strptime(data_referencia, '%Y-%m-%d')    
        idade = referencia.year - nascimento.year - ((referencia.month, referencia.day) < (nascimento.month, nascimento.day))    
    return idade

df10 = consultar_consolidado()
df10['idade'] = df10['data de nascimento'].apply(recalcular_idade)
print('id | idade | data de nascimento')
for index, usuario in df10.head(10).iterrows():
    print(usuario['id'], usuario['idade'], usuario['data de nascimento'])

print("*"*100)


print('11. Exceção Customizada para Dados Ausentes')
print('''
Implemente uma função que leia os dados da tabela “Consolidado” e lance uma exceção customizada chamada 
"DadosAusentesError" se alguma coluna apresentar um dado faltante. Utilize um bloco try...except para 
capturar essa exceção e listar o e-mail do INFNETiano em questão caso a exceção seja levantada, e 
salve o e-mail em um arquivo txt chamado, “dados_ausentes.txt”.
''')

class DadosAusentesError(Exception):
    """
    Exceção customizada para erros relacionados à ausência de dados em campos obrigatórios.
    Esta exceção é utilizada para identificar e tratar registros com dados faltantes.
    """
    pass

def verificar_dados_ausentes(df):
    """
    Verifica se há dados ausentes no DataFrame e lança uma exceção 'DadosAusentesError' com o e-mail do usuário.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados a serem verificados.

    Raises:
        DadosAusentesError: Exceção lançada quando dados ausentes são encontrados, incluindo o e-mail do usuário.
    """
    if df.isnull().any().any():
        usuarios_ausentes = df[df.isnull().any(axis=1)]
        for _, usuario in usuarios_ausentes.iterrows():
            raise DadosAusentesError(f'{usuario['email']}')

def salvar_dados_ausentes(emails):
    """
    Salva os e-mails de usuários com dados ausentes em um arquivo de texto.

    Args:
        emails (list): Lista contendo os e-mails dos usuários com dados ausentes.

    Writes:
        Cria ou sobrescreve o arquivo 'dados_ausentes.txt' com os e-mails fornecidos, um por linha.
    """
    with open('dados_ausentes.txt', 'w') as file:
        for email in emails:
            file.write(f"{email}\n")

def gerar_erro():
    """
    Atualiza a tabela 'Consolidado', definindo o valor do sobrenome como NULL para o registro com id = '892deb27'.
    
    Raises:
        Exception: Lança uma exceção caso ocorra algum erro ao atualizar o banco de dados.
    """
    try:
        engine = create_engine("sqlite:///INFwebNET_DB.db")
        
        with engine.connect() as conexao:
            update_sql = """
            UPDATE Consolidado
            SET sobrenome = NULL
            WHERE id = '892deb27'
            """
            conexao.execute(update_sql)
            print("Registro atualizado com sucesso.")
    
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar o banco de dados: {e}")

try:
    gerar_erro()
    df_consolidado = consultar_consolidado()
    verificar_dados_ausentes(df_consolidado)
    print('Não foi encontrado nenhum usuario com dados ausentes')
except DadosAusentesError as e:
    email_ausente = str(e)
    print(f"Dados ausentes encontrados para o e-mail: {email_ausente}")    
    salvar_dados_ausentes([email_ausente])

print("*"*100)


print('12. Try…Except Completo')
print('''
Escreva uma função que leia todos os arquivos: 
“dados_usuario.csv”, “INFwebNET_30mais.xlsx", “INFwebNET_Historico.xlsx”, "INFwebNET_DB.db" 
e “dados_ausentes.txt” utilizando uma estrutura try...except completa de forma que 
cada tentativa de leitura seja feita dentro de um try que capture e lide com os 
seguintes tipos de exceções: `FileNotFoundError`, `MemoryError`, `RuntimeError`, 
`EOFError`, `OSError`, `ConnectionError`, `TimeoutError` e `PermissionError`.
a. Lide com cada tipo de exceção exibindo uma mensagem apropriada e siga para o 
próximo arquivo ou encerre o programa quando for apropriado.
b. Utilize um bloco else para exibir a quantidade de linhas existentes no arquivo lido
c. Utilize um bloco finally para garantir o fechamento do arquivo ou da conexão.
''')


def ler_csv(arquivo, divisor=';'):
    """
    Lê um arquivo CSV e retorna os dados como um DataFrame.

    Args:
        arquivo (str): Caminho para o arquivo CSV.
        divisor (str): Caractere usado como delimitador no arquivo CSV. O padrão é ';'.

    Returns:
        pd.DataFrame: Dados lidos do arquivo CSV.
    """
    diretorio_atual = os.path.dirname(os.path.realpath(__file__))
    diretorio_recuado = os.path.dirname(diretorio_atual)
    caminho_completo = os.path.join(diretorio_recuado, arquivo)
    return pd.read_csv(caminho_completo, delimiter=divisor)

def ler_xlsx(arquivo):
    """
    Lê um arquivo Excel (.xlsx) e retorna os dados como um DataFrame.

    Args:
        arquivo (str): Caminho para o arquivo Excel.

    Returns:
        pd.DataFrame: Dados lidos do arquivo Excel.
    """
    return pd.read_excel(arquivo)

def ler_txt(arquivo):
    """
    Lê um arquivo de texto (.txt) e retorna o conteúdo como uma lista de linhas.

    Args:
        arquivo (str): Caminho para o arquivo de texto.

    Returns:
        list: Lista de linhas lidas do arquivo de texto.
    """
    with open(arquivo, 'r') as f:
        dados = f.readlines()
    return dados

def ler_usuarios_historicos():
    """
    Lê os dados da tabela 'Usuarios_Historicos' no banco de dados SQLite e retorna como um DataFrame.

    Returns:
        pd.DataFrame: DataFrame contendo os dados da tabela 'Usuarios_Historicos'.
    """
    engine = create_engine("sqlite:///INFwebNET_DB.db")        
    consulta_sql = "SELECT * FROM Usuarios_Historicos"
    df_resultado = pd.read_sql(consulta_sql, con=engine)        
    return df_resultado

def ler_consolidado():
    """
    Lê os dados da tabela 'Consolidado' no banco de dados SQLite e retorna como um DataFrame.

    Returns:
        pd.DataFrame: DataFrame contendo os dados da tabela 'Consolidado'.
    """
    engine = create_engine("sqlite:///INFwebNET_DB.db")        
    consulta_sql = "SELECT * FROM Consolidado"
    df_resultado = pd.read_sql(consulta_sql, con=engine)        
    return df_resultado
        
def ler_arquivos():
    """
    Lê uma lista de arquivos (CSV, XLSX, DB, TXT) e exibe a quantidade de registros contidos em cada um.
    Tenta ler os arquivos e captura exceções para lidar com erros de leitura.

    Exceções tratadas:
        FileNotFoundError: Arquivo não encontrado.
        MemoryError: Falta de memória ao tentar ler o arquivo.
        RuntimeError: Erro genérico durante a execução.
        EOFError: Erro no final do arquivo.
        OSError: Erro de sistema operacional ao tentar acessar o arquivo.
        PermissionError: Erro de permissão ao acessar o arquivo.
        sqlite3.OperationalError: Erro ao acessar banco de dados SQLite.
    """
    arquivos = [
        "dados_usuarios.csv", 
        "INFwebNET_30mais.xlsx", 
        "INFwebNET_Historico.xlsx",          
        "dados_ausentes.txt",
        "INFwebNET_DB.db"
    ]
    
    for arquivo in arquivos:
        try:
            if arquivo.endswith('.csv'):
                df_csv = ler_csv(arquivo)
                print(f"Arquivo: {arquivo} | Quantidade: [{len(df_csv)}")
            elif arquivo.endswith('.xlsx'):
                df_xlsx = ler_xlsx(arquivo)
                print(f"Arquivo: {arquivo} | Quantidade: [{len(df_xlsx)}]")
            elif arquivo.endswith('.db'):
                df_use_his = ler_usuarios_historicos()
                df_con = ler_consolidado()
                print(f"DB [{arquivo}] lido com sucesso.")
                print(f" -> Tabela [Usuarios Historico] | Quantidade: [{len(df_use_his)}]")
                print(f" -> Tabela [Consolidados] | Quantidade: [{len(df_con)}]")
            elif arquivo.endswith('.txt'):
                dados = ler_txt(arquivo)
                print(f"Arquivo: {arquivo} | Quantidade: [{len(dados)}]")
            else:
                print(f"Tipo de arquivo {arquivo} não reconhecido.")
        except (FileNotFoundError, MemoryError, RuntimeError, EOFError, OSError, PermissionError, sqlite3.OperationalError) as e:
            print(f"Erro ao tentar ler o arquivo {arquivo}: {str(e)}")

ler_arquivos()


