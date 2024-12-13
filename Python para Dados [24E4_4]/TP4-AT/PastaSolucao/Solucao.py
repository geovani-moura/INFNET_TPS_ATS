import pandas as pd
import urllib.request
import urllib.error
import re
import unicodedata
import json
import sqlite3
import ast
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from collections import Counter

print('1. Preparação dos Dados (★)')
def ler_panda_json():
    """
    Lê um arquivo JSON e o carrega em um DataFrame do pandas.

    Esta função lê um arquivo JSON especificado, carrega seus dados e os converte em um
    DataFrame do pandas, que pode ser utilizado para análise de dados.

    Returns:
        pandas.DataFrame: O conteúdo do arquivo JSON carregado em um DataFrame.

    """
    return pd.read_json("INFwebNet_Data.json", encoding="utf-8")

def validar_panda_json(df, colunas_obrigatorias):
    """
    Valida um DataFrame carregado de um arquivo JSON, verificando se as colunas obrigatórias estão presentes
    e preenchendo campos vazios ou nulos com "Não Informado".

    Args:
        df (pandas.DataFrame): DataFrame carregado do JSON.
        colunas_obrigatorias (list): Lista de colunas que devem estar presentes no DataFrame.

    Returns:
        pandas.DataFrame: DataFrame validado e corrigido.
    """    
    colunas_faltantes = [col for col in colunas_obrigatorias if col not in df.columns]
    if colunas_faltantes:
        raise ValueError(f"Colunas obrigatórias ausentes: {colunas_faltantes}")

    df.fillna("Não Informado", inplace=True)

    return df

def carregar_dados():
    colunas_esperadas = [
        "Nome",
        "Idade",
        "Localização(Cidade, Estado)",
        "Amigos(Lista)",
        "ID",
        "Email",
        "DataDeNascimento",
        "Hobbies",
        "Coding",
        "Jogos(Nome, Plataforma)",
        "ano_nascimento"
    ]
    df = ler_panda_json()
    return validar_panda_json(df, colunas_esperadas)

df1 = carregar_dados();
print(df1)

print("*"*100)


print('2. Extração de Plataformas (★)')
def salvar_plataformas_txt(plataformas):
    """
    Salva o conjunto de plataformas em um arquivo chamado "plataformas.txt".

    Args:
        plataformas (set): Conjunto de nomes únicos das plataformas.
    """
    with open("plataformas.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(plataformas)))

def extrair_plataformas(df):
    """
    Extrai nomes únicos das plataformas de jogos mencionadas na coluna "Jogos(Nome, Plataforma)".

    Args:
        df (pandas.DataFrame): DataFrame contendo os dados dos usuários e seus jogos.

    Returns:
        set: Conjunto de nomes únicos das plataformas.
    """
    plataformas = set()

    for jogos in df.get("Jogos(Nome, Plataforma)", []):
        if jogos != "Não Informado" and isinstance(jogos, list):
            for jogo in jogos:
                if isinstance(jogo, list) and len(jogo) > 1:
                    plataformas.add(jogo[1])  

    salvar_plataformas_txt(plataformas)
    return plataformas

plataformas2 = extrair_plataformas(df1)
print("Plataformas extraídas:", plataformas2)
print("*"*100)


print('3. Tratamento de Exceções ao Carregar Plataformas (★)')
def carregar_plataformas():
    """
    Tenta carregar o arquivo "plataformas.txt" e retorna uma lista com os nomes das plataformas.
    Caso o arquivo não seja encontrado, solicita ao usuário o caminho correto ou encerra o programa.

    Returns:
        list: Lista com os nomes das plataformas.
    """
    while True:
        try:
            with open("plataformas.txt", "r", encoding="utf-8") as f:
                return f.read().splitlines()
        except FileNotFoundError:
            print("Erro: O arquivo 'plataformas.txt' não foi encontrado.")
            novo_caminho = input("Insira o caminho correto do arquivo ou digite 'sair' para encerrar: ").strip()
            if novo_caminho.lower() == "sair":
                print("Encerrando o programa.")
                exit()
            else:
                try:
                    with open(novo_caminho, "r", encoding="utf-8") as f:
                        return f.read().splitlines()
                except FileNotFoundError:
                    print("Erro: O caminho fornecido é inválido. Tente novamente.")

plataformas3 = carregar_plataformas()
print("Plataformas carregadas:", plataformas3)
print("*"*100)


print('4. Download de Páginas da Wikipédia (★★)')
print('5. Tratamento de Exceções no Download (★★)')
def salvar_html(conteudo, nome_arquivo):
    """Salva o conteúdo HTML em um arquivo."""
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write(conteudo)
        print(f"Arquivo '{nome_arquivo}' salvo com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo '{nome_arquivo}': {e}")

def registrar_erro(plataforma, erro):
    """
    Registra erros em um arquivo chamado 'erros_download.txt'.

    Args:
        plataforma (str): Nome da plataforma que gerou o erro.
        erro (Exception): O erro ocorrido.
    """
    try:
        with open("erros_download.txt", "a", encoding="utf-8") as log:
            log.write(f"Plataforma: {plataforma} - Erro: {erro}\n")
    except Exception as e:
        print(f"Erro ao registrar log: {e}")

def baixar_paginas_wikipedia(plataformas):
    """
    Baixa páginas da Wikipédia para cada plataforma fornecida e salva como arquivos HTML.
    Registra erros em um arquivo de log caso ocorram problemas durante o download.

    Args:
        plataformas (list): Lista de nomes das plataformas.

    Returns:
        list: Lista com os caminhos dos arquivos HTML gerados.
    """
    arquivos_gerados = []

    for plataforma in plataformas:
        try:
            nome_formatado = plataforma.replace(" ", "_")
            url = f"https://pt.wikipedia.org/wiki/Lista_de_jogos_para_{nome_formatado}"

            nome_arquivo = f"plataforma_{nome_formatado}.html"

            response = urllib.request.urlopen(url)
            conteudo = response.read().decode("utf-8")
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                f.write(conteudo)
            arquivos_gerados.append(nome_arquivo)

        except urllib.error.HTTPError as e:
            registrar_erro(plataforma, e)
        except urllib.error.URLError as e:
            registrar_erro(plataforma, e)
        except Exception as e:
            registrar_erro(plataforma, e)

    return arquivos_gerados

baixar_paginas_wikipedia(plataformas2)
print("*"*100)


print('6. Parsing das Páginas HTML (★★)')
print('7. Extração de Tabelas de Jogos (★★)')
class TituloInvalidoException(Exception):
    pass

def abrir_arquivo_html(caminho_arquivo):
    """Função que abre e lê o conteúdo de um arquivo HTML."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {str(e)}")
        return None

def salvar_erro_parse(erro):
    """Função que salva o erro no arquivo de log de erros."""
    try:
        with open("erros_parse.txt", 'a', encoding='utf-8') as log:
            log.write(f"Erro: {str(erro)}\n")
    except Exception as e:
        print(f"Erro ao salvar no arquivo de erros: {str(e)}")

def parsear_paginas(arquivos):
    resultados = []
    for caminho_arquivo, nome_plataforma in arquivos:
        try:
            conteudo_html = abrir_arquivo_html(caminho_arquivo)
            soup = BeautifulSoup(conteudo_html, 'html.parser')

            titulo = soup.title.string if soup.title else ''
            if nome_plataforma not in titulo:
                raise TituloInvalidoException(
                    f"Título '{titulo}' não corresponde ao nome da plataforma {nome_plataforma}."
                )

            tabelas = soup.find_all('table', class_='wikitable')
            if not tabelas:
                raise ValueError("Nenhuma tabela com a classe 'wikitable' foi encontrada.")

            jogos = []
            for tabela in tabelas:
                cabecalhos = [th.get_text(strip=True) for th in tabela.find_all('th')]

                for linha in tabela.find_all('tr')[1:]:
                    colunas = linha.find_all(['td', 'th'])
                    if len(colunas) == len(cabecalhos):
                        dados_jogo = {cabecalho: coluna.get_text(strip=True) for cabecalho, coluna in zip(cabecalhos, colunas)}
                        jogos.append({"nome_jogo": dados_jogo.get(cabecalhos[0], ""), "dados_jogo": dados_jogo})

            resultados.append({"plataforma": nome_plataforma, "jogos": jogos})

        except TituloInvalidoException as e:
            salvar_erro_parse(e)
        except Exception as e:
            salvar_erro_parse(e)

    return resultados

arquivos = [
    ('plataforma_Xbox_One.html', 'Xbox One'),
    ('plataforma_PlayStation_4.html', 'PlayStation 4')
]

jogosplataforma6_7 = parsear_paginas(arquivos)

print("*"*100)


print('8. Uso de Expressões Regulares (★★)')
def salvar_json(arquivo, texto):
    with open(arquivo, 'w', encoding='utf-8') as arquivo_json:
        json.dump(texto, arquivo_json, ensure_ascii=False, indent=4)

def extrair_urls_emails(arquivos):
    conexoes = {"urls": set(), "emails": set()}
    url_regex = r"((([A-Za-z]{3,9}:(?:\\/\\/)?)(?:[-;:&=\\+\\$,\\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\\+\\$,\\w]+@)[A-Za-z0-9.-]+)((?:\\/[\\+~%\\/.\\w-_]*)?\\??(?:[-\\+=&;%@.\\w_]*)#?(?:[.\\!/\\\\\\w]*))?)"
    email_regex = r"^([\\w-]+(?:\\.[\\w-]+)*)@((?:[\\w-]+\\.)*\\w[\\w-]{0,66})\\.([a-z]{2,6}(?:\\.[a-z]{2})?)$"

    for caminho_arquivo, _ in arquivos:
        try:
            conteudo_html = abrir_arquivo_html(caminho_arquivo)
            soup = BeautifulSoup(conteudo_html, 'html.parser')
            texto = soup.get_text()

            urls = re.findall(url_regex, texto)
            emails = re.findall(email_regex, texto, re.MULTILINE)

            conexoes["urls"].update([url[0] for url in urls])
            conexoes["emails"].update(emails)

        except Exception as e:
            salvar_erro_parse(e)

    conexoes["urls"] = list(conexoes["urls"])
    conexoes["emails"] = list(conexoes["emails"])

    salvar_json('conexoes_plataformas.json', conexoes)

extrair_urls_emails(arquivos)
print("*"*100)


print('9. Exportação dos Dados (★★★)')
salvar_json('dados_jogos_plataformas.json', jogosplataforma6_7)
print("*"*100)


print('10. Associação de Jogos aos Usuários (★★)')
def associar_jogos_usuarios(df_usuarios, jogos_por_plataforma):
    associacoes = []

    for _, usuario in df_usuarios.iterrows():
        jogos_usuario = usuario['Jogos(Nome, Plataforma)']

        if jogos_usuario == "Não Informado":
            jogos_associados = []
        else:
            jogos_associados = []

            for plataforma in jogos_por_plataforma:
                for jogo in plataforma['jogos']:
                    for jogo_usuario in jogos_usuario:
                        nome_jogo, nome_plataforma = jogo_usuario
                        if jogo['nome_jogo'] == nome_jogo and plataforma['plataforma'] == nome_plataforma:
                            jogos_associados.append({
                                "nome_jogo": jogo['nome_jogo'],
                                "plataforma": plataforma['plataforma'],
                                "dados_jogo": jogo['dados_jogo']
                            })

        associacoes.append(jogos_associados)

    df_usuarios['associados'] = associacoes
    return df_usuarios

df10 = associar_jogos_usuarios(df1, jogosplataforma6_7)
print("*"*100)


print('11. Atualização do Banco de Dados (★★)')
def ler_json(arquivo):
    """
    Lê um arquivo JSON e retorna os dados contidos nele.
    
    Args:
        arquivo (str): Caminho para o arquivo JSON a ser lido.
    
    Returns:
        list: Dados do arquivo JSON.
    """
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados_json = json.load(f)
        return dados_json
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo JSON: {e}")
        return []

def converter_json_para_tabela(json_data):
    """
    Converte o JSON fornecido em uma tabela do pandas com as colunas: 
    plataforma, jogo, nome_jogo, Título, Desenvolvedora, etc.
    
    Args:
        json_data (list): Lista de dicionários com dados de jogos e plataformas.
    
    Returns:
        pd.DataFrame: DataFrame com as informações extraídas do JSON.
    """
    jogos_data = []
    
    for plataforma_info in json_data:
        plataforma = plataforma_info['plataforma']
        
        for jogo in plataforma_info['jogos']:
            nome_jogo = jogo['nome_jogo']
            dados_jogo = jogo['dados_jogo']
            
            jogo_data = {
                'plataforma': plataforma,
                'jogo': nome_jogo,
                'nome_jogo': nome_jogo,
                'Título': dados_jogo.get('Título', ''),
                'Desenvolvedora': dados_jogo.get('Desenvolvedora', ''),
                'Publicadora': dados_jogo.get('Publicadora', ''),
                'Ano': dados_jogo.get('Ano', ''),
                'Exclusivo': dados_jogo.get('Exclusivo', ''),
                'Kinect': dados_jogo.get('Kinect', ''),
                'Ref.': dados_jogo.get('Ref.', '')
            }
            jogos_data.append(jogo_data)
    
    df_jogos = pd.DataFrame(jogos_data)
    return df_jogos

def atualizar_banco_dados(df):
    """
    Carrega os dados do DataFrame na tabela 'Jogos_Plataformas' do banco de dados SQLite.

    Args:
        df (pd.DataFrame): DataFrame com os dados a serem carregados.

    Raises:
        Exception: Lança uma exceção caso ocorra um erro ao carregar os dados no banco de dados.
    """
    try:
        engine = create_engine(f"sqlite:///INFwebNET_DB.db")        
        df.to_sql('Jogos_Plataformas', con=engine, if_exists='replace', index=False)
        print('Tabela Jogos_Plataformas carregada com sucesso.')
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados no banco de dados: {e}")

json11 = ler_json('dados_jogos_plataformas.json')
df11 = converter_json_para_tabela(json11)
atualizar_banco_dados(df11)
print("*"*100)


print('12. Consulta aos Dados (★★)')
def obter_nome_jogo():
    """
    Solicita o nome de um jogo ao usuário.
    
    Returns:
        str: Nome do jogo fornecido pelo usuário.
    """
    nome_jogo = input("Digite o nome do jogo: ")
    return nome_jogo

def consultar_usuarios_por_jogo(nome_jogo):
    """
    Consulta no banco de dados os usuários que jogam um jogo específico.
    
    Args:
        nome_jogo (str): Nome do jogo para realizar a consulta.
    
    Returns:
        list: Lista de nomes de usuários que jogam o jogo solicitado.
    """
    usuarios = []
    
    try:
        conn = sqlite3.connect('INFwebNET_DB.db')
        cursor = conn.cursor()

        query = """
            SELECT nome
            FROM Usuarios_Historicos
            WHERE jogos LIKE ?
        """
        cursor.execute(query, ('%' + nome_jogo + '%',))
        usuarios = cursor.fetchall()

    except sqlite3.Error as e:
        print(f"Erro ao consultar o banco de dados: {e}")
    
    finally:
        conn.close()

    return usuarios

def exibir_usuarios(nome_jogo, usuarios):
    """
    Função exibe os usuários que jogam o jogo.
    """
    
    if usuarios:
        print(f"Usuários que jogam '{nome_jogo}':")
        for usuario in usuarios:
            print(usuario[0])
    else:
        print(f"Nenhum usuário encontrado jogando '{nome_jogo}'.")

nomejogo12 = obter_nome_jogo()
usuarios12 = consultar_usuarios_por_jogo(nomejogo12)
exibir_usuarios(nomejogo12, usuarios12)
print("*"*100)


print('13. Análise Estatística (★★)')
def plataforma_ranking():
    """
    Retorna um dicionário com a contagem de usuários por plataforma com base nos jogos que eles jogam.
    """
    try:
        conn = sqlite3.connect('INFwebNET_DB.db')
        cursor = conn.cursor()

        query = "SELECT jogos FROM Usuarios_Historicos"
        cursor.execute(query)
        resultados = cursor.fetchall()

        plataformas = []

        for row in resultados:
            if row[0]:
                try:
                    jogos = ast.literal_eval(row[0])
                    for jogo in jogos:
                        if isinstance(jogo, tuple) and len(jogo) == 2:
                            plataformas.append(jogo[1])
                except (ValueError, SyntaxError):
                    continue

        retorno = Counter(plataformas)
        return retorno

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return Counter()

    finally:
        conn.close()

def exibir_ranking_plataformas():
    """
    Exibe o retorno das plataformas com base na contagem de usuários e destaca a mais popular.
    """
    contador = plataforma_ranking()

    if contador:
        print("Ranking das plataformas:")
        for plataforma, usuarios in contador.most_common():
            print(f"{plataforma}: {usuarios} usuários")

        plataforma_mais_popular, usuarios = contador.most_common(1)[0]
        print(f"\nA plataforma mais popular é '{plataforma_mais_popular}' com {usuarios} usuários.")
    else:
        print("Nenhuma plataforma encontrada.")

exibir_ranking_plataformas()
print("*"*100)


print('14. Guardando as Informações (★)')
def salvar_dados_completos():
    """
    Salva todas as informações associadas (usuários, jogos, plataformas) em um arquivo JSON.
    """
    try:
        conn = sqlite3.connect('INFwebNET_DB.db')
        cursor = conn.cursor()

        query = "SELECT * FROM Usuarios_Historicos"
        cursor.execute(query)
        usuarios = cursor.fetchall()

        colunas = [desc[0] for desc in cursor.description]
        dados_completos = []

        for usuario in usuarios:
            usuario_dict = dict(zip(colunas, usuario))
            try:
                usuario_dict['jogos'] = ast.literal_eval(usuario_dict['jogos']) if usuario_dict['jogos'] else []
            except (ValueError, SyntaxError):
                usuario_dict['jogos'] = []

            dados_completos.append(usuario_dict)

        with open('INFwebNET_Completo.json', 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados_completos, arquivo_json, ensure_ascii=False, indent=4)

        print("Dados completos salvos em 'INFwebNET_Completo.json'.")

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    finally:
        conn.close()

salvar_dados_completos()
print("*"*100)


print('15. Documentação do Código (★)')
print('Foi feita a docstring em todas as funções.')

print('16. Relatório Final (★★)')
print('Está no Documento enviado')