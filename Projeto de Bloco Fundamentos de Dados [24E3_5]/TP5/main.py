from os.path import dirname, join
import os
import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

diretorio_atual = os.path.dirname(os.path.realpath(__file__))

def obter_conexao():
    """
    Cria e retorna uma conexão com o banco de dados SQLite.

    A função localiza o arquivo de banco de dados chamado "dados.db" 
    no diretório atual e estabelece uma conexão com ele.

    Returns:
        sqlite3.Connection: Objeto de conexão com o banco de dados SQLite.
    """
    arquivo = os.path.join(diretorio_atual, "dados.db")    
    return sqlite3.connect(arquivo)

def CriarDB():
    """
    Cria as tabelas necessárias no banco de dados SQLite.

    A função remove as tabelas `TB_EVENTOS`, `TB_DADOS_EVENTOS` e 
    `TB_METADADOS_EVENTOS`, caso existam, e recria suas estruturas 
    com os seguintes propósitos:

    - `TB_EVENTOS`: Armazena informações básicas sobre eventos.
      Colunas: `Id`, `Nome`, `Faixa_Etaria`.
    - `TB_DADOS_EVENTOS`: Contém informações sobre as datas e localização 
      dos eventos. 
      Colunas: `Id`, `Id_Evento`, `DataDe`, `DataAte`, `Localizacao`.
      Possui uma chave estrangeira que referencia a tabela `TB_EVENTOS`.
    - `TB_METADADOS`: Registra informações adicionais (metadados) dos eventos.
      Colunas: `Id`, `Id_Evento`, `Metadado`.
      Também possui uma chave estrangeira para a tabela `TB_EVENTOS`.

    Após a execução, imprime uma mensagem indicando que as tabelas foram criadas.
    """
    with obter_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute("DROP TABLE IF EXISTS TB_EVENTOS;")
        cursor.execute("DROP TABLE IF EXISTS TB_DADOS_EVENTOS;")
        cursor.execute("DROP TABLE IF EXISTS TB_METADADOS_EVENTOS;")

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS TB_EVENTOS (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome TEXT NOT NULL,
                Faixa_Etaria INT NULL
            );
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS TB_DADOS_EVENTOS (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Id_Evento INTEGER NOT NULL,
                DataDe TIMESTAMP NOT NULL,
                DataAte TIMESTAMP NOT NULL,
                Localizacao TEXT NOT NULL,
                FOREIGN KEY (Id_Evento) REFERENCES TB_EVENTOS(Id)
            );
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS TB_METADADOS (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Id_Evento INTEGER NOT NULL,
                Metadado TEXT NOT NULL,
                FOREIGN KEY (Id_Evento) REFERENCES TB_EVENTOS(Id)
            );
            """
        )

        print("Tabelas Criadas")

class EventoEntity:
    """
    Representa a entidade de um evento no sistema e fornece métodos para manipulação de seus dados.

    Attributes:
        nome (str): O nome do evento.
        faixa_etaria (int): A faixa etária recomendada para o evento.

    Methods:
        salvar():
            Insere as informações do evento na tabela `TB_EVENTOS` do banco de dados.
            Retorna o ID do registro recém-inserido.
    """
    def __init__(self, nome, faixa_etaria):
        self.nome = nome
        self.faixa_etaria = faixa_etaria

    def salvar(self):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO TB_EVENTOS (Nome, Faixa_Etaria) VALUES (?, ?)", (self.nome, self.faixa_etaria)
            )
            return cursor.lastrowid

class DadoEventoEntity:
    """
    Representa os dados detalhados de um evento, incluindo datas e localização, 
    e fornece métodos para manipulação desses dados no banco de dados.

    Attributes:
        id_evento (int): O ID do evento associado.
        data_de (str): A data de início do evento, no formato TIMESTAMP.
        data_ate (str): A data de término do evento, no formato TIMESTAMP.
        localizacao (str): A localização do evento.

    Methods:
        salvar():
            Insere os detalhes do evento na tabela `TB_DADOS_EVENTOS` do banco de dados.
            Retorna o ID do registro recém-inserido.
    """
    def __init__(self, id_evento, data_de, data_ate, localizacao):
        self.id_evento = id_evento
        self.data_de = data_de
        self.data_ate = data_ate
        self.localizacao = localizacao

    def salvar(self):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO TB_DADOS_EVENTOS (Id_Evento, DataDe, DataAte, Localizacao) VALUES (?, ?, ?, ?)",
                (self.id_evento, self.data_de, self.data_ate, self.localizacao)
            )
            return cursor.lastrowid

class MetadadoEventoEntity:
    """
    Representa os metadados de um evento, permitindo a associação de informações adicionais, 
    e fornece métodos para manipulação desses dados no banco de dados.

    Attributes:
        id_evento (int): O ID do evento associado.
        metadado (str): A informação adicional relacionada ao evento.

    Methods:
        salvar():
            Insere os metadados do evento na tabela `TB_METADADOS` do banco de dados.
            Retorna o ID do registro recém-inserido.
    """
    def __init__(self, id_evento, metadado):
        self.id_evento = id_evento
        self.metadado = metadado

    def salvar(self):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO TB_METADADOS (Id_Evento, Metadado) VALUES (?, ?)",
                (self.id_evento, self.metadado)
            )
            return cursor.lastrowid

def obter_site_html():
    """
    Faz uma requisição HTTP para o site "sampaingressos.com.br" e retorna o conteúdo HTML.

    Utiliza a biblioteca `requests` para obter o conteúdo da página e o 
    `BeautifulSoup` para parsear o HTML.

    Returns:
        BeautifulSoup: Objeto representando o conteúdo HTML da página, pronto para ser analisado.
    """
    response = requests.get('https://www.sampaingressos.com.br/')
    content = response.content
    return BeautifulSoup(content, 'html.parser')

def converter_datas(data):
    """
    Converte uma string representando uma data ou intervalo de datas no formato brasileiro para objetos `date`.

    Se a entrada for nula, retorna a data atual como início e término. Se o formato da data estiver incorreto, 
    retorna a data atual.

    Se a string contiver "até", será interpretada como um intervalo de datas.
    Caso contrário, será tratada como uma única data.

    Args:
        data (str): Data ou intervalo de datas no formato "dd/mm até dd/mm" ou "dd/mm".

    Returns:
        tuple: Um par de objetos `date` representando a data de início (`de`) e a data de término (`ate`).
        
    Exemplo:
        Se a entrada for "10/05 até 15/05", retornará (10/05/2024, 15/05/2024).
        Se a entrada for "10/05", retornará (10/05/2024, 10/05/2024).
        Se o formato da data for inválido, retornará a data atual.
    """
    ano_atual = datetime.now().year
    data_atual = datetime.now().date()

    if data is None:
        return data_atual, data_atual

    try:
        if "até" in data:
            data_de, data_ate = data.split(" até ")
            de = datetime.strptime(f"{data_de}/{ano_atual}", "%d/%m/%Y").date()
            ate = datetime.strptime(f"{data_ate}/{ano_atual}", "%d/%m/%Y").date()
        else:
            de = datetime.strptime(f"{data}/{ano_atual}", "%d/%m/%Y").date()
            ate = de
        return de, ate
    except ValueError:
        return data_atual, data_atual

def obter_faixa_etaria(tag):
    """
    Determina a faixa etária de um evento com base no atributo `src` de uma tag de imagem HTML.

    A função verifica o caminho da imagem associada e retorna a faixa etária correspondente. 
    Se nenhuma faixa conhecida for identificada, retorna o valor do atributo `src` da imagem.

    Args:
        tag (bs4.element.Tag): Objeto BeautifulSoup representando a tag HTML que contém a imagem.

    Returns:
        str: A faixa etária correspondente (e.g., "Livre", "10 anos", "12 anos", etc.) 
             ou o caminho do atributo `src` caso a faixa não seja reconhecida.
    """
    img_src = tag.find('img')['src']
    if 'livre' in img_src.lower():
        return 'Livre'
    elif '10anos' in img_src.lower():
        return '10 anos'
    elif '12anos' in img_src.lower():
        return '12 anos'
    elif '14anos' in img_src.lower():
        return '14 anos'
    elif '16anos' in img_src.lower():
        return '16 anos'
    elif '18anos' in img_src.lower():
        return '18 anos'
    else:
        return img_src  
    return None  

def converter_html_in_db():
    """
    Extrai informações de eventos de uma página HTML e insere os dados no banco de dados.

    A função:
    1. Cria as tabelas do banco de dados usando `CriarDB()`.
    2. Faz o parse do site HTML obtido pela função `obter_site_html()`.
    3. Para cada evento encontrado:
        - Extrai informações como título, localização, temporada (datas), faixa etária e metadados.
        - Converte as datas utilizando `converter_datas()` e a faixa etária com `obter_faixa_etaria()`.
        - Salva os dados do evento nas tabelas `TB_EVENTOS`, `TB_DADOS_EVENTOS` e `TB_METADADOS` usando as classes `EventoEntity`, `DadoEventoEntity` e `MetadadoEventoEntity`.

    Returns:
        None
    """
    CriarDB()
    site = obter_site_html()
    eventos = site.findAll('div', attrs={'id': 'box_espetaculo'})
    for evento in eventos:
        titulo_tag = evento.find('b', attrs={'class': 'titulo'})
        titulo = titulo_tag.text
        local_tag = evento.find('span', attrs={'class': 'local'})
        local = local_tag.text
        temporada_tag = evento.find('span', attrs={'class': 'temporada'})
        temporada = temporada_tag.text if temporada_tag else None
        de, ate = converter_datas(temporada)
        faixa_etaria_tag = evento.find('span', attrs={'class': 'rec_etaria_card'})
        faixa_etaria = obter_faixa_etaria(faixa_etaria_tag)
        metadado = str(''.join(evento.stripped_strings))

        evento_entity = EventoEntity(nome=titulo, faixa_etaria=faixa_etaria)
        evento_id = evento_entity.salvar()

        dado_evento_entity = DadoEventoEntity(id_evento = evento_id, data_de = de, data_ate = ate, localizacao = local)
        dado_evento_id = dado_evento_entity.salvar()

        metadado_evento_entity = MetadadoEventoEntity(id_evento = evento_id, metadado = metadado)
        metadado_evento_id = metadado_evento_entity.salvar()


converter_html_in_db()


print("1. Mostrar todos os eventos com suas datas, localização, e tipo de evento.")
def consulta1():
    """
    Realiza uma consulta no banco de dados para obter informações detalhadas sobre eventos.

    A função executa um `JOIN` entre as tabelas `tb_eventos` e `tb_dados_eventos` para recuperar:
    - `Id`, `Nome`, `Faixa_Etaria` do evento (da tabela `tb_eventos`).
    - `DataDe`, `DataAte`, `Localizacao` do evento (da tabela `tb_dados_eventos`).
    
    O resultado é retornado como uma lista de dicionários, onde as chaves são os nomes das colunas 
    e os valores são os dados correspondentes.

    Returns:
        list: Lista de dicionários contendo os resultados da consulta, 
        cada dicionário representa uma linha.
    """
    query = """
        select 
            eve.Id, 
            eve.Nome, 
            eve.Faixa_Etaria, 
            dad.DataDe, 
            dad.DataAte, 
            dad.Localizacao
        from tb_eventos eve
        join tb_dados_eventos dad on eve.id = dad.id_evento;
    """    
    with obter_conexao() as conexao: 
        cursor = conexao.cursor()
        cursor.execute(query)
        colunas = [col[0] for col in cursor.description]
        resultados = cursor.fetchall()
    
    return [dict(zip(colunas, linha)) for linha in resultados]

resultado1 = consulta1()
for linha in resultado1:
    data_de = datetime.strptime(linha['DataDe'], '%Y-%m-%d')
    data_ate = datetime.strptime(linha['DataAte'], '%Y-%m-%d')
    print(
        f"Id Evento: {linha['Id']} "
        f"Nome Evento: {linha['Nome']} "
        f"| Faixa Etaria: {linha['Faixa_Etaria']}"
        f"| Data De: {data_de.strftime('%m/%d/%Y')}"
        f"| Data Até: {data_ate.strftime('%m/%d/%Y')}"
        f"| Localização: {linha['Localizacao']}"
    )
print("-" * 100)


print("2. Mostrar os dados dos 2 eventos mais próximos de iniciar.")
def consulta2():
    """
    Realiza uma consulta no banco de dados para obter os primeiros dois eventos em ordem cronológica.

    A função executa um `JOIN` entre as tabelas `tb_eventos` e `tb_dados_eventos` para recuperar:
    - `Nome` do evento (da tabela `tb_eventos`).
    - `DataDe`, `DataAte`, `Localizacao` do evento (da tabela `tb_dados_eventos`).
    
    Os resultados são ordenados pela data de início (`DataDe`) em ordem crescente, e o número 
    máximo de resultados retornados é limitado a 2.

    Returns:
        list: Lista de dicionários contendo os dois primeiros resultados da consulta, 
        cada dicionário representa uma linha.
    """
    query = """
        select 
            eve.Nome, 
            dad.DataDe, 
            dad.DataAte, 
            dad.Localizacao
        from tb_eventos eve
        join tb_dados_eventos dad on eve.id = dad.id_evento
        order by dad.datade asc
        limit 2;
    """    
    with obter_conexao() as conexao: 
        cursor = conexao.cursor()
        cursor.execute(query)
        colunas = [col[0] for col in cursor.description]
        resultados = cursor.fetchall()
    
    return [dict(zip(colunas, linha)) for linha in resultados]

resultado2 = consulta2()
for linha in resultado2:
    data_de = datetime.strptime(linha['DataDe'], '%Y-%m-%d')
    data_ate = datetime.strptime(linha['DataAte'], '%Y-%m-%d')
    print(
        f"Nome Evento: {linha['Nome']} "
        f"| Data De: {data_de.strftime('%m/%d/%Y')}"
        f"| Data Até: {data_ate.strftime('%m/%d/%Y')}"
        f"| Localização: {linha['Localizacao']}"
    )
print("-" * 100)


print("3. Mostrar os eventos que acontecem no Rio de Janeiro. (Trocado para Teatro Renaissance)")
def consulta3():
    """
    Realiza uma consulta no banco de dados para obter eventos localizados no "Teatro Renaissance".

    A função executa um `JOIN` entre as tabelas `tb_eventos` e `tb_dados_eventos` para recuperar:
    - `Nome` do evento (da tabela `tb_eventos`).
    - `DataDe`, `DataAte`, `Localizacao` do evento (da tabela `tb_dados_eventos`).
    
    A consulta é filtrada para retornar apenas os eventos cuja localização contenha o texto "Teatro Renaissance".

    Returns:
        list: Lista de dicionários contendo os resultados da consulta, cada dicionário representa uma linha.
    """
    query = """
        select 
            eve.Nome, 
            dad.DataDe, 
            dad.DataAte, 
            dad.Localizacao
        from tb_eventos eve
        join tb_dados_eventos dad on eve.id = dad.id_evento
        where dad.localizacao like '%Teatro Renaissance%';
    """    
    with obter_conexao() as conexao: 
        cursor = conexao.cursor()
        cursor.execute(query)
        colunas = [col[0] for col in cursor.description]
        resultados = cursor.fetchall()
    
    return [dict(zip(colunas, linha)) for linha in resultados]

resultado3 = consulta3()
for linha in resultado3:
    data_de = datetime.strptime(linha['DataDe'], '%Y-%m-%d')
    data_ate = datetime.strptime(linha['DataAte'], '%Y-%m-%d')
    print(
        f"Nome Evento: {linha['Nome']} "
        f"| Data De: {data_de.strftime('%m/%d/%Y')}"
        f"| Data Até: {data_ate.strftime('%m/%d/%Y')}"
        f"| Localização: {linha['Localizacao']}"
    )
print("-" * 100)


print("4. Mostrar todos os eventos que são ao ar livre. (Trocado para Teatro Procópio Ferreira)")
def consulta4():
    """
    Realiza uma consulta no banco de dados para obter eventos localizados no "Teatro Procópio Ferreira".

    A função executa um `JOIN` entre as tabelas `tb_eventos` e `tb_dados_eventos` para recuperar:
    - `Nome` do evento (da tabela `tb_eventos`).
    - `DataDe`, `DataAte`, `Localizacao` do evento (da tabela `tb_dados_eventos`).
    
    A consulta é filtrada para retornar apenas os eventos cuja localização contenha o texto "Teatro Procópio Ferreira".

    Returns:
        list: Lista de dicionários contendo os resultados da consulta, cada dicionário representa uma linha.
    """
    query = """
        select 
            eve.Nome, 
            dad.DataDe, 
            dad.DataAte, 
            dad.Localizacao
        from tb_eventos eve
        join tb_dados_eventos dad on eve.id = dad.id_evento
        where dad.localizacao like '%Teatro Procópio Ferreira%';
    """    
    with obter_conexao() as conexao: 
        cursor = conexao.cursor()
        cursor.execute(query)
        colunas = [col[0] for col in cursor.description]
        resultados = cursor.fetchall()
    
    return [dict(zip(colunas, linha)) for linha in resultados]

resultado4 = consulta4()
for linha in resultado4:
    data_de = datetime.strptime(linha['DataDe'], '%Y-%m-%d')
    data_ate = datetime.strptime(linha['DataAte'], '%Y-%m-%d')
    print(
        f"Nome Evento: {linha['Nome']} "
        f"| Data De: {data_de.strftime('%m/%d/%Y')}"
        f"| Data Até: {data_ate.strftime('%m/%d/%Y')}"
        f"| Localização: {linha['Localizacao']}"
    )
print("-" * 100)


print("5. Mostrar todos os Metadados por evento.")
def truncar_texto(texto, limite=80):
    """
    Trunca um texto para um comprimento máximo, adicionando '...' caso o limite seja excedido.

    A função verifica se o comprimento do texto é maior que o limite especificado. Se for, o texto é truncado
    até o limite e '...' é adicionado ao final. Caso contrário, o texto original é retornado.

    Args:
        texto (str): O texto a ser truncado.
        limite (int, opcional): O comprimento máximo permitido para o texto. O valor padrão é 80.

    Returns:
        str: O texto truncado, com ou sem '...' no final, dependendo do comprimento.
    """
    if len(texto) > limite:
        return texto[:limite] + "..."
    return texto

def consulta5():
    """
    Realiza uma consulta no banco de dados para obter os metadados associados aos eventos.

    A função executa um `JOIN` entre as tabelas `tb_eventos` e `tb_metadados` para recuperar:
    - `Nome` do evento (da tabela `tb_eventos`).
    - `Metadado` associado ao evento (da tabela `tb_metadados`).

    Returns:
        list: Lista de dicionários contendo os resultados da consulta, cada dicionário representa uma linha.
    """
    query = """
        select 
            eve.Nome, 
            met.Metadado
        from tb_eventos eve
        join tb_metadados met on eve.id = met.id_evento;
    """    
    with obter_conexao() as conexao: 
        cursor = conexao.cursor()
        cursor.execute(query)
        colunas = [col[0] for col in cursor.description]
        resultados = cursor.fetchall()
    
    return [dict(zip(colunas, linha)) for linha in resultados]

resultado5 = consulta5()
for linha in resultado5:
    print(
        f"Nome Evento: {linha['Nome']} "
        f"| Metadado: {truncar_texto(linha['Metadado'])}"
    )
print("-" * 100)