from os.path import dirname, join
import os
import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

diretorio_atual = os.path.dirname(os.path.realpath(__file__))

def obter_conexao():
    arquivo = os.path.join(diretorio_atual, "dados.db")    
    return sqlite3.connect(arquivo)

def CriarDB():
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
    response = requests.get('https://www.sampaingressos.com.br/')
    content = response.content
    return BeautifulSoup(content, 'html.parser')

def converter_datas(data):
    ano_atual = datetime.now().year
    data_atual = datetime.now().date()

    if data is None:
        return data_atual, data_atual

    if "até" in data:
        data_de, data_ate = data.split(" até ")
        de = datetime.strptime(f"{data_de}/{ano_atual}", "%d/%m/%Y").date()
        ate = datetime.strptime(f"{data_ate}/{ano_atual}", "%d/%m/%Y").date()
    else:
        de = datetime.strptime(f"{data}/{ano_atual}", "%d/%m/%Y").date()
        ate = de

    return de, ate

def obter_faixa_etaria(tag):
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
    metadado = str(evento)

    evento_entity = EventoEntity(nome=titulo, faixa_etaria=faixa_etaria)
    evento_id = evento_entity.salvar()

    dado_evento_entity = DadoEventoEntity(id_evento = evento_id, data_de = de, data_ate = ate, localizacao = local)
    dado_evento_id = dado_evento_entity.salvar()

    metadado_evento_entity = MetadadoEventoEntity(id_evento = evento_id, metadado = metadado)
    metadado_evento_id = metadado_evento_entity.salvar()


