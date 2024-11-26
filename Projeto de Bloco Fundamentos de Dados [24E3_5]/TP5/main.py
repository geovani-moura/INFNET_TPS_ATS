import os
import csv
#from numpy import int32
#import pandas as pd
import sqlite3
#from datetime import datetime, timedelta
import json

diretorio_atual = os.path.dirname(os.path.realpath(__file__))
arquivo = os.path.join(diretorio_atual, "dados.db")
conexao = sqlite3.connect(arquivo)
cursor = conexao.cursor()

# DROP das tabelas
cursor.execute("DROP TABLE IF EXISTS TB_FUNCIONARIO;")
cursor.execute("DROP TABLE IF EXISTS TB_CARGO;")
cursor.execute("DROP TABLE IF EXISTS TB_DEPARTAMENTO;")
cursor.execute("DROP TABLE IF EXISTS TB_NIVEL;")
cursor.execute("DROP TABLE IF EXISTS TB_HISTORICO_SALARIO;")
cursor.execute("DROP TABLE IF EXISTS TB_DEPENDENTE;")
cursor.execute("DROP TABLE IF EXISTS TB_RECURSO_PROJETO  ;")
cursor.execute("DROP TABLE IF EXISTS TB_PROJETO ;")

# Criação das tabelas
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS TB_NIVEL (
    Id INTEGER NOT NULL,
    Nome TEXT NOT NULL,
    PRIMARY KEY (Id)
);
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS TB_CARGO (
    Id INTEGER PRIMARY KEY NOT NULL,
    IdNivel INTEGER NOT NULL,
    Descricao TEXT,
    SalarioBase REAL NOT NULL,
    FOREIGN KEY (IdNivel) REFERENCES TB_NIVEL (Id)
);
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS TB_DEPARTAMENTO (
    Id INTEGER NOT NULL,
    IdFuncionario INTEGER NULL,
    Nome TEXT NOT NULL,	
    Andar INTEGER NOT NULL,
    PRIMARY KEY (Id)
);
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS TB_FUNCIONARIO (
    Id INTEGER PRIMARY KEY NOT NULL,
    Nome TEXT,
    IdCargo INTEGER NULL,
    IdDepartamento INTEGER NOT NULL,
    Salario REAL NOT NULL,
    FOREIGN KEY (IdDepartamento) REFERENCES TB_DEPARTAMENTO (Id),
    FOREIGN KEY (IdCargo) REFERENCES TB_CARGO (Id)
);
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS TB_HISTORICO_SALARIO (
    IdFuncionario INTEGER NOT NULL,
    MesAno DATE NOT NULL,
    SalarioRecebido REAL NOT NULL,
    PRIMARY KEY (IdFuncionario, MesAno),
    FOREIGN KEY (IdFuncionario) REFERENCES TB_FUNCIONARIO (Id)
);
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS TB_DEPENDENTE (
    Id INTEGER PRIMARY KEY NOT NULL,
    IdFuncionario INTEGER NOT NULL,
    Nome TEXT NOT NULL,
    DataNascimento DATE NOT NULL,
    Parentesco TEXT NOT NULL,
    FOREIGN KEY (IdFuncionario) REFERENCES TB_FUNCIONARIO (Id)
);
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS TB_PROJETO (
    Id INTEGER PRIMARY KEY NOT NULL,
    Nome TEXT NOT NULL,
    Descricao TEXT,
    DataInicio DATE NOT NULL,
    DataConclusao DATE,
    IdFuncionario INTEGER NOT NULL,
    Custo REAL NOT NULL,
    Status TEXT NOT NULL,
    FOREIGN KEY (IdFuncionario) REFERENCES TB_FUNCIONARIO (Id)
);
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS TB_RECURSO_PROJETO (
    Id INTEGER PRIMARY KEY NOT NULL,
    IdProjeto INTEGER NOT NULL,
    Descricao TEXT NOT NULL,
    TipoRecurso TEXT NOT NULL,
    Quantidade REAL NOT NULL,
    DataUtilizacao DATE NOT NULL,
    FOREIGN KEY (IdProjeto) REFERENCES TB_PROJETO (Id)
);
"""
)
print("Tabelas Criadas")

def ler_arquivo_csv(nome_arquivo):
    diretorio_atual = os.path.dirname(os.path.realpath(__file__))
    arquivo = os.path.join(diretorio_atual, nome_arquivo)
    with open(arquivo, mode="r", newline="") as csvfile:
        leitor_csv = csv.DictReader(csvfile)
        dados = [linha for linha in leitor_csv]
    return dados

# TB_NIVEL
dados_nivel = ler_arquivo_csv("CSV/TB_NIVEL.csv")
TB_NIVEL_LIST = [(int(nivel["Id"]), nivel["Nome"]) for nivel in dados_nivel]
cursor.executemany("INSERT INTO TB_NIVEL (Id, Nome) VALUES (?, ?)", TB_NIVEL_LIST)

# TB_CARGO
dados_cargo = ler_arquivo_csv("CSV/TB_CARGO.csv")
TB_CARGO_LIST = [
    (int(cargo["IdNivel"]), cargo["Descricao"], float(cargo["SalarioBase"]))
    for cargo in dados_cargo
]
cursor.executemany(
    "INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (?, ?, ?)",
    TB_CARGO_LIST,
)

# TB_DEPARTAMENTO
dados_departamento = ler_arquivo_csv("CSV/TB_DEPARTAMENTO.csv")
TB_DEPARTAMENTO_LIST = [
    (
        int(dep["Id"]),
        (
            int(dep["IdFuncionario"])
            if dep["IdFuncionario"] not in (None, "", "NULL")
            else None
        ),
        dep["Nome"],
        int(dep["Andar"]),
    )
    for dep in dados_departamento
]
cursor.executemany(
    "INSERT INTO TB_DEPARTAMENTO (Id, IdFuncionario, Nome, Andar) VALUES (?, ?, ?, ?)",
    TB_DEPARTAMENTO_LIST,
)

# TB_FUNCIONARIO
dados_funcionario = ler_arquivo_csv("CSV/TB_FUNCIONARIO.csv")
TB_FUNCIONARIO_LIST = [
    (
        func["Nome"],
        (
            int(float(func["IdCargo"]))
            if func["IdCargo"] not in (None, "", "NULL")
            else None
        ),
        (
            int(float(func["IdDepartamento"]))
            if func["IdDepartamento"] not in (None, "", "NULL")
            else None
        ),
        float(func["Salario"]) if func["Salario"] not in (None, "", "NULL") else None,
    )
    for func in dados_funcionario
]
cursor.executemany(
    "INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES (?, ?, ?, ?)",
    TB_FUNCIONARIO_LIST,
)

# TB_HISTORICO_SALARIO
dados_historico_salario = ler_arquivo_csv("CSV/TB_HISTORICO_SALARIO.csv")
TB_HISTORICO_SALARIO_LIST = [
    (int(hist["IdFuncionario"]), hist["MesAno"], float(hist["SalarioRecebido"]))
    for hist in dados_historico_salario
]
cursor.executemany(
    "INSERT INTO TB_HISTORICO_SALARIO (IdFuncionario, MesAno, SalarioRecebido) VALUES (?, ?, ?)",
    TB_HISTORICO_SALARIO_LIST,
)

# TB_DEPENDENTE
dados_dependente = ler_arquivo_csv("CSV/TB_DEPENDENTE.csv")
TB_DEPENDENTE_LIST = [
    (int(dep["IdFuncionario"]), dep["Nome"], dep["DataNascimento"], dep["Parentesco"])
    for dep in dados_dependente
]
cursor.executemany(
    "INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (?, ?, ?, ?)",
    TB_DEPENDENTE_LIST,
)

# TB_PROJETO
dados_projeto = ler_arquivo_csv("CSV/TB_PROJETO.csv")
TB_PROJETO_LIST = [
    (
        int(proj["Id"]),
        int(proj["IdFuncionario"]),
        proj["Nome"],
        proj["Descricao"],
        proj["DataInicio"],
        proj["DataConclusao"],
        proj["Status"],
        float(proj["Custo"]),
    )
    for proj in dados_projeto
]
cursor.executemany(
    "INSERT INTO TB_PROJETO (Id, IdFuncionario, Nome, Descricao, DataInicio, DataConclusao, Status, Custo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    TB_PROJETO_LIST,
)

# TB_RECURSO_PROJETO
dados_recurso_projeto = ler_arquivo_csv("CSV/TB_RECURSO_PROJETO.csv")
TB_RECURSO_PROJETO_LIST = [
    (
        int(rec["Id"]),
        int(rec["IdProjeto"]),
        rec["Descricao"],
        rec["TipoRecurso"],
        float(rec["Quantidade"]),
        rec["DataUtilizacao"],
    )
    for rec in dados_recurso_projeto
]
cursor.executemany(
    "INSERT INTO TB_RECURSO_PROJETO (Id, IdProjeto, Descricao, TipoRecurso, Quantidade, DataUtilizacao) VALUES (?, ?, ?, ?, ?, ?)",
    TB_RECURSO_PROJETO_LIST,
)

# Salva as mudanças
conexao.commit()
print("-" * 50)

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
    arquivo = os.path.join(diretorio_atual, nomeArquivo)
    with open(arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

print("""
1. Trazer a média dos salários (atual) dos funcionários responsáveis por projetos concluídos, agrupados
por departamento.
""")
def media(cursor):
    """
    Retorna a média dos salários atuais dos funcionários responsáveis por projetos concluídos,
    agrupados por departamento.

    Parâmetros:
    cursor (sqlite3.Cursor): Cursor da conexão SQLite.

    Retorna:
    list: Lista de tuplas contendo o nome do departamento e a média salarial.
    """
    query = """
        SELECT 
            DEPA.Nome AS DepartamentoNome,
            AVG(FUNC.Salario) AS MediaSalario
        FROM TB_PROJETO PROJ
        JOIN TB_FUNCIONARIO FUNC ON PROJ.IdFuncionario = FUNC.Id
        JOIN TB_DEPARTAMENTO DEPA ON FUNC.IdDepartamento = DEPA.Id
        WHERE PROJ.Status = 'Concluído'
        GROUP BY DEPA.Id, DEPA.Nome
        ORDER BY MediaSalario DESC;
    """
    cursor.execute(query)
    colunas = [col[0] for col in cursor.description]
    resultados = cursor.fetchall()
    return [dict(zip(colunas, linha)) for linha in resultados]

resultado = media(cursor)

print("Média de salários por departamento:")
for linha in resultado:
    print(
        f"Departamento: {linha['DepartamentoNome']} "
        f"| Média Salarial: {linha['MediaSalario']:.2f}"
    )
EscreverJSON("Exercicio_1_Media.json", resultado)

print("-" * 50)


print(
    """
2. Identificar os três recursos materiais mais usados nos projetos, listando a descrição do recurso
e a quantidade total usada.
"""
)

def recursos(cursor, top=3):
    """
    Retorna os recursos materiais mais usados nos projetos, incluindo descrição e quantidade total utilizada.

    Parâmetros:
    cursor (sqlite3.Cursor): Cursor da conexão SQLite.
    top (int): Quantidade de recursos a serem retornados (padrão: 3).

    Retorna:
    list: Lista de tuplas contendo a descrição do recurso e a quantidade total usada.
    """
    query = f"""
        SELECT 
            RECU.Descricao AS RecursoDescricao,
            SUM(RECU.Quantidade) AS QuantidadeTotal
        FROM TB_RECURSO_PROJETO RECU
        WHERE RECU.TipoRecurso = 'Material'
        GROUP BY RECU.Descricao
        ORDER BY QuantidadeTotal DESC
        LIMIT {top};
    """
    cursor.execute(query)
    colunas = [col[0] for col in cursor.description]
    resultados = cursor.fetchall()
    return [dict(zip(colunas, linha)) for linha in resultados]

resultado = recursos(cursor)

print("Recursos materiais mais usados:")
for linha in resultado:
    print(
        f"Recurso: {linha['RecursoDescricao']} "
        f"| Quantidade Total: {linha['QuantidadeTotal']}"
    )

EscreverJSON("Exercicio_2_Recursos.json", resultado)

print("-" * 50)


print("""
3. Calcular o custo total dos projetos por departamento, considerando apenas os projetos
'Concluídos'.
""")

def custo(cursor):
    """
    Calcula o custo total dos projetos concluídos por departamento.

    Parâmetros:
    cursor (sqlite3.Cursor): Cursor da conexão SQLite.

    Retorna:
    list: Lista de tuplas contendo o nome do departamento e o custo total dos projetos concluídos.
    """
    query = """
        SELECT 
            DEPA.Nome AS DepartamentoNome,
            SUM(PROJ.Custo) AS CustoTotal
        FROM TB_PROJETO PROJ
        JOIN TB_FUNCIONARIO FUNC ON PROJ.IdFuncionario = FUNC.Id
        JOIN TB_DEPARTAMENTO DEPA ON FUNC.IdDepartamento = DEPA.Id
        WHERE PROJ.Status = 'Concluído'
        GROUP BY DEPA.Id, DEPA.Nome
        ORDER BY CustoTotal DESC;
    """
    cursor.execute(query)
    colunas = [col[0] for col in cursor.description]
    resultados = cursor.fetchall()
    return [dict(zip(colunas, linha)) for linha in resultados]

resultado = custo(cursor)
print("Custo total dos projetos concluídos por departamento:")
for linha in resultado:
    print(
        f"Departamento: {linha['DepartamentoNome']} "
        f"| Custo Total: {linha['CustoTotal']:.2f}"
    )

EscreverJSON("Exercicio_3_Custo.json", resultado)

print("-" * 50)


print(
    """
4. Listar todos os projetos com seus respectivos nomes, custo, data de início, data de conclusão
e o nome do funcionário responsável, que estejam 'Em Execução'.
"""
)

def listar_projetos(cursor):
    """
    Lista todos os projetos 'Em Execução' com informações detalhadas.

    Parâmetros:
    cursor (sqlite3.Cursor): Cursor da conexão SQLite.

    Retorna:
    list: Lista de tuplas contendo nome do projeto, custo, data de início, data de conclusão e nome do funcionário responsável.
    """
    query = """
        SELECT 
            PROJ.Nome AS NomeProjeto,
            PROJ.Custo AS Custo,
            PROJ.DataInicio AS DataInicio,
            PROJ.DataConclusao AS DataConclusao,
            FUNC.Nome AS FuncionarioResponsavel
        FROM TB_PROJETO PROJ
        JOIN TB_FUNCIONARIO FUNC ON PROJ.IdFuncionario = FUNC.Id
        WHERE PROJ.Status = 'Em Execução'
        ORDER BY PROJ.Nome;
    """
    cursor.execute(query)
    colunas = [col[0] for col in cursor.description]
    resultados = cursor.fetchall()
    return [dict(zip(colunas, linha)) for linha in resultados]

resultado = listar_projetos(cursor)
print("Projetos 'Em Execução':")
for linha in resultado:
    print(
        f"Projeto: {linha['NomeProjeto']} "
        f"| Custo: {linha['Custo']:.2f} "
        f"| Início: {linha['DataInicio']} "
        f"| Conclusão: {linha['DataConclusao']} "
        f"| Responsável: {linha['FuncionarioResponsavel']}"
    )

EscreverJSON("Exercicio_4_Listar_Projetos.json", resultado)

print("-" * 50)


print(
    """
5. Identificar o projeto com o maior número de dependentes envolvidos, considerando que os
dependentes são associados aos funcionários que estão gerenciando os projetos.
"""
)
def dependentes(cursor):
    """
    Identifica o projeto com o maior número de dependentes associados ao funcionário responsável.

    Parâmetros:
    cursor (sqlite3.Cursor): Cursor da conexão SQLite.

    Retorna:
    tuple: Dados do projeto com o maior número de dependentes (Nome do Projeto, Nome do Funcionário, Quantidade de Dependentes).
    """
    query = """
        SELECT 
            PROJ.Nome AS NomeProjeto,
            FUNC.Nome AS FuncionarioResponsavel,
            COUNT(DEP.Id) AS QuantidadeDependentes
        FROM TB_PROJETO PROJ
        JOIN TB_FUNCIONARIO FUNC ON PROJ.IdFuncionario = FUNC.Id
        LEFT JOIN TB_DEPENDENTE DEP ON FUNC.Id = DEP.IdFuncionario
        GROUP BY PROJ.Id, PROJ.Nome, FUNC.Nome
        ORDER BY QuantidadeDependentes DESC
        LIMIT 1;
    """
    cursor.execute(query)
    colunas = [col[0] for col in cursor.description]
    resultados = cursor.fetchall()
    return [dict(zip(colunas, linha)) for linha in resultados]

resultado = dependentes(cursor)
if resultado:
    for linha in resultado:
        print(
            f"Projeto: {linha['NomeProjeto']} "
            f"| Responsável: {linha['FuncionarioResponsavel']} "
            f"| Dependentes: {linha['QuantidadeDependentes']}"
        )
else:
    print("Nenhum projeto com dependentes foi encontrado.")

EscreverJSON("Exercicio_5_Listar_Dependentes.json", resultado)

print("-" * 50)

conexao.close()
