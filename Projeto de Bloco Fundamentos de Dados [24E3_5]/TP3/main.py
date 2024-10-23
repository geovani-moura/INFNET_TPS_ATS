import csv
from numpy import int32
import pandas as pd
import sqlite3
from datetime import datetime, timedelta

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()

# DROP das tabelas
cursor.execute('DROP TABLE IF EXISTS TB_FUNCIONARIO;')
cursor.execute('DROP TABLE IF EXISTS TB_CARGO;')
cursor.execute('DROP TABLE IF EXISTS TB_DEPARTAMENTO;')
cursor.execute('DROP TABLE IF EXISTS TB_NIVEL;')
cursor.execute('DROP TABLE IF EXISTS TB_HISTORICO_SALARIO;')
cursor.execute('DROP TABLE IF EXISTS TB_DEPENDENTE;')

# Criação das tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS TB_NIVEL (
    Id INTEGER NOT NULL,
    Nome TEXT NOT NULL,
    PRIMARY KEY (Id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS TB_CARGO (
    Id INTEGER PRIMARY KEY NOT NULL,
    IdNivel INTEGER NOT NULL,
    Descricao TEXT,
    SalarioBase REAL NOT NULL,
    FOREIGN KEY (IdNivel) REFERENCES TB_NIVEL (Id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS TB_DEPARTAMENTO (
    Id INTEGER NOT NULL,
    IdFuncionario INTEGER NULL,
    Nome TEXT NOT NULL,	
    Andar INTEGER NOT NULL,
    PRIMARY KEY (Id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS TB_FUNCIONARIO (
    Id INTEGER PRIMARY KEY NOT NULL,
    Nome TEXT,
    IdCargo INTEGER NULL,
    IdDepartamento INTEGER NOT NULL,
    Salario REAL NOT NULL,
    FOREIGN KEY (IdDepartamento) REFERENCES TB_DEPARTAMENTO (Id),
    FOREIGN KEY (IdCargo) REFERENCES TB_CARGO (Id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS TB_HISTORICO_SALARIO (
    IdFuncionario INTEGER NOT NULL,
    MesAno DATE NOT NULL,
    SalarioRecebido REAL NOT NULL,
    PRIMARY KEY (IdFuncionario, MesAno),
    FOREIGN KEY (IdFuncionario) REFERENCES TB_FUNCIONARIO (Id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS TB_DEPENDENTE (
    Id INTEGER PRIMARY KEY NOT NULL,
    IdFuncionario INTEGER NOT NULL,
    Nome TEXT NOT NULL,
    DataNascimento DATE NOT NULL,
    Parentesco TEXT NOT NULL,
    FOREIGN KEY (IdFuncionario) REFERENCES TB_FUNCIONARIO (Id)
);
''')
print('Tabelas Criadas')


def ler_arquivo_csv(nome_arquivo):
  with open(nome_arquivo, mode="r", newline="") as csvfile:
    leitor_csv = csv.DictReader(csvfile)
    dados = [linha for linha in leitor_csv]
  return dados


# TB_NIVEL
dados_nivel = ler_arquivo_csv('CSV/TB_NIVEL.csv')
TB_NIVEL_LIST = [(int(nivel['Id']), nivel['Nome']) for nivel in dados_nivel]
cursor.executemany("INSERT INTO TB_NIVEL (Id, Nome) VALUES (?, ?)",
                   TB_NIVEL_LIST)

# TB_CARGO
dados_cargo = ler_arquivo_csv('CSV/TB_CARGO.csv')
TB_CARGO_LIST = [(int(cargo['IdNivel']), cargo['Descricao'],
                  float(cargo['SalarioBase'])) for cargo in dados_cargo]
cursor.executemany(
    "INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (?, ?, ?)",
    TB_CARGO_LIST)

# TB_DEPARTAMENTO
dados_departamento = ler_arquivo_csv('CSV/TB_DEPARTAMENTO.csv')
TB_DEPARTAMENTO_LIST = [(int(dep['Id']),
                         (int(dep['IdFuncionario']) if dep['IdFuncionario']
                          not in (None, '', 'NULL') else None), dep['Nome'],
                         int(dep['Andar'])) for dep in dados_departamento]
cursor.executemany(
    "INSERT INTO TB_DEPARTAMENTO (Id, IdFuncionario, Nome, Andar) VALUES (?, ?, ?, ?)",
    TB_DEPARTAMENTO_LIST)

# TB_FUNCIONARIO
dados_funcionario = ler_arquivo_csv('CSV/TB_FUNCIONARIO.csv')
TB_FUNCIONARIO_LIST = [
    (func['Nome'], (int(float(func['IdCargo']))
                    if func['IdCargo'] not in (None, '', 'NULL') else None),
     int(float(func['IdDepartamento']))
     if func['IdDepartamento'] not in (None, '', 'NULL') else None,
     float(func['Salario']) if func['Salario'] not in (None, '',
                                                       'NULL') else None)
    for func in dados_funcionario
]
cursor.executemany(
    "INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES (?, ?, ?, ?)",
    TB_FUNCIONARIO_LIST)

# TB_HISTORICO_SALARIO
dados_historico_salario = ler_arquivo_csv('CSV/TB_HISTORICO_SALARIO.csv')
TB_HISTORICO_SALARIO_LIST = [(int(hist['IdFuncionario']), hist['MesAno'],
                              float(hist['SalarioRecebido']))
                             for hist in dados_historico_salario]
cursor.executemany(
    "INSERT INTO TB_HISTORICO_SALARIO (IdFuncionario, MesAno, SalarioRecebido) VALUES (?, ?, ?)",
    TB_HISTORICO_SALARIO_LIST)

# TB_DEPENDENTE
dados_dependente = ler_arquivo_csv('CSV/TB_DEPENDENTE.csv')
TB_DEPENDENTE_LIST = [(int(dep['IdFuncionario']), dep['Nome'],
                       dep['DataNascimento'], dep['Parentesco'])
                      for dep in dados_dependente]
cursor.executemany(
    "INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (?, ?, ?, ?)",
    TB_DEPENDENTE_LIST)

# Salva as mudanças
conexao.commit()


print('-'*50)
print('1 - S/SQL - Listar individualmente as tabelas de: Funcionários, Cargos, Departamentos, Histórico de Salários e Dependentes em ordem crescente.')
funcionarios = ler_arquivo_csv('CSV/TB_FUNCIONARIO.csv')
cargos = ler_arquivo_csv('CSV/TB_CARGO.csv')
departamentos = ler_arquivo_csv('CSV/TB_DEPARTAMENTO.csv')
historico_salarios = ler_arquivo_csv('CSV/TB_HISTORICO_SALARIO.csv')
dependentes = ler_arquivo_csv('CSV/TB_DEPENDENTE.csv')

# Listar os dados em ordem crescente
print("Funcionários:")
for func in sorted(funcionarios, key=lambda x: x['Id']):
    print(func)

print("\nCargos:")
for cargo in sorted(cargos, key=lambda x: x['Id']):
    print(cargo)

print("\nDepartamentos:")
for depa in sorted(departamentos, key=lambda x: x['Id']):
    print(depa)

print("\nHistórico de Salários:")
for hist in sorted(historico_salarios, key=lambda x: x['IdFuncionario']):
    print(hist)

print("\nDependentes:")
for dep in sorted(dependentes, key=lambda x: x['Id']):
    print(dep)

print('-'*50)
print('2 - S/SQL - Listar os funcionários, com seus cargos, departamentos e os respectivos dependentes.')
print('-'*50)
resultado = []
for func in funcionarios:
    cargo = next((c for c in cargos if c['Id'] == func['IdCargo']), None)
    departamento = next((d for d in departamentos if d['Id'] == func['IdDepartamento']), None)
    dependente = [d for d in dependentes if d['IdFuncionario'] == func['Id']]

    resultado.append({
        'Funcionario': func['Nome'],
        'Cargo': cargo['Descricao'] if cargo else 'Desconhecido',
        'Departamento': departamento['Nome'] if departamento else 'Desconhecido',
        'Dependentes': [d['Nome'] for d in dependente] if dependente else ['Nenhum']
    })
print("Funcionários com Cargos, Departamentos e Dependentes:")
for res in resultado:
    print(f"Funcionário: {res['Funcionario']} | Cargo: {res['Cargo']} | Departamento: {res['Departamento']} | Dependentes: {', '.join(res['Dependentes'])}")


print('-'*50)
print('3 - S/SQL - Listar os funcionários que tiveram aumento salarial nos últimos 3 meses.')
print('-'*50)
tres_meses_antes = datetime.now() - timedelta(days=90)
aumentos_recent = [
    hist for hist in historico_salarios
    if datetime.strptime(hist['MesAno'], '%Y-%m-%d') >= tres_meses_antes
]
funcionarios_com_aumento = {}
for hist in aumentos_recent:
    func_id = hist['IdFuncionario']
    salario = float(hist['SalarioRecebido'])
    if func_id not in funcionarios_com_aumento:
        funcionarios_com_aumento[func_id] = salario
    else:
        funcionarios_com_aumento[func_id] = max(funcionarios_com_aumento[func_id], salario)
print("Funcionários que tiveram aumento salarial nos últimos 3 meses:")
for func_id, salario in funcionarios_com_aumento.items():
    funcionario = next((f for f in funcionarios if f['Id'] == func_id), None)
    if funcionario:
        print(f"Funcionário ID: {func_id} | Nome: {funcionario['Nome']} | Salário: {salario:.2f}")


print('-'*50)
print('4 - S/SQL - Listar a média de idade dos filhos dos funcionários por departamento.')
print('-'*50)
for dep in dependentes:
    dep['DataNascimento'] = datetime.strptime(dep['DataNascimento'], '%Y-%m-%d')
for dep in dependentes:
    dep['Idade'] = (datetime.now() - dep['DataNascimento']).days // 365
media_idade_por_depa = {}
for dep in dependentes:
    funcionario = next((f for f in funcionarios if f['Id'] == dep['IdFuncionario']), None)
    if funcionario:
        departamento = next((d for d in departamentos if d['Id'] == funcionario['IdDepartamento']), None)
        if departamento:
            dep_nome = departamento['Nome']
            if dep_nome not in media_idade_por_depa:
                media_idade_por_depa[dep_nome] = []
            media_idade_por_depa[dep_nome].append(dep['Idade'])
print("Média de idade dos filhos dos funcionários por departamento:")
for dep_nome, idades in media_idade_por_depa.items():
    media_idade = sum(idades) / len(idades) if idades else 0
    print(f"Departamento: {dep_nome} | Média de Idade: {media_idade:.2f}")


print('-'*50)
print('5 - S/SQL - Listar qual estagiário possui filho')
print('-'*50)
estagiario_ids = [cargo['Id'] for cargo in cargos if cargo['IdNivel'] == '1']
estagiarios = [] 
for func in funcionarios:
    if func['IdCargo'] in estagiario_ids:
        estagiarios.append(func) 
estagiarios_com_filho = []
for estagiario in estagiarios:
    filhos = [dep for dep in dependentes if dep['IdFuncionario'] == estagiario['Id']]
    if filhos:
        estagiarios_com_filho.append((estagiario['Nome'], [f['Nome'] for f in filhos]))
print("Estagiários que possuem filhos:")
for est_nome, filhos in estagiarios_com_filho:
    print(f"Estagiário: {est_nome} | Filhos: {', '.join(filhos)}")

print('-'*50)
print('6 - C/SQL - Listar o funcionário que teve o salário médio mais alto.')
print('-'*50)
cursor.execute('''
    SELECT 
        FUNC.Id AS FuncionarioId,
        FUNC.Nome AS FuncionarioNome,
        AVG(HISA.SalarioRecebido) AS SalarioMedio
    FROM TB_FUNCIONARIO FUNC
    JOIN TB_HISTORICO_SALARIO HISA ON FUNC.Id = HISA.IdFuncionario
    GROUP BY FUNC.Id, FUNC.Nome
    ORDER BY SalarioMedio DESC
    LIMIT 1;
''')
resultado = cursor.fetchall()
print("Funcionário com o salário médio mais alto:")
for linha in resultado:
    print(f"Funcionário ID: {linha[0]} | Nome: {linha[1]} | Salário Médio: {linha[2]:.2f}")

print('-'*50)
print('7 - C/SQL - Listar o analista que é pai de 2 (duas) meninas.')
print('-'*50)
cursor.execute('''
    SELECT 
        FUNC.Id AS FuncionarioId,
        FUNC.Nome AS FuncionarioNome
    FROM TB_FUNCIONARIO FUNC
    JOIN TB_CARGO CARG ON FUNC.IdCargo = CARG.Id
    JOIN TB_DEPENDENTE DEPE ON FUNC.Id = DEPE.IdFuncionario
    WHERE CARG.Descricao LIKE 'Analista%'
    AND DEPE.Parentesco = 'Filha'
    GROUP BY FUNC.Id, FUNC.Nome
    HAVING COUNT(DEPE.Id) = 2;
''')
resultado = cursor.fetchall()
print("Analista que é pai de 2 filhas:")
for linha in resultado:
    print(f"Funcionário ID: {linha[0]} | Nome: {linha[1]}")

print('-'*50)
print('8 - C/SQL - Listar o analista que tem o salário mais alto, e que ganhe entre 5000 e 9000')
print('-'*50)
cursor.execute('''
    SELECT 
        FUNC.Id AS FuncionarioId,
        FUNC.Nome AS FuncionarioNome,
        CARG.SalarioBase AS Salario
    FROM TB_FUNCIONARIO FUNC
    JOIN TB_CARGO CARG ON FUNC.IdCargo = CARG.Id
    WHERE CARG.Descricao LIKE 'Analista%'
    AND CARG.SalarioBase BETWEEN 5000 AND 9000
    ORDER BY CARG.SalarioBase DESC
    LIMIT 1;
''')
resultado = cursor.fetchall()
print("Analista com o salário mais alto (entre 5000 e 9000):")
for linha in resultado:
    print(f"Funcionário ID: {linha[0]} | Nome: {linha[1]} | Salário: {linha[2]:.2f}")

print('-'*50)
print('9 - C/SQL - Listar qual departamento possui o maior número de dependentes.')
print('-'*50)
cursor.execute('''
    SELECT 
        DEPA.Nome AS DepartamentoNome,
        COUNT(DEPE.Id) AS NumeroDependentes
    FROM TB_DEPENDENTE DEPE
    JOIN TB_FUNCIONARIO FUNC ON DEPE.IdFuncionario = FUNC.Id
    JOIN TB_DEPARTAMENTO DEPA ON FUNC.IdDepartamento = DEPA.Id
    GROUP BY DEPA.Id, DEPA.Nome
    ORDER BY NumeroDependentes DESC
    LIMIT 1;
''')
resultado = cursor.fetchall()
print("Departamento com o maior número de dependentes:")
for linha in resultado:
    print(f"Departamento: {linha[0]} | Número de Dependentes: {linha[1]}")

print('-'*50)
print('10 - C/SQL - Listar a média de salário por departamento em ordem decrescente.')
print('-'*50)
cursor.execute('''
    SELECT 
        DEPA.Nome AS DepartamentoNome,
        AVG(FUNC.Salario) AS MediaSalario
    FROM TB_FUNCIONARIO FUNC
    JOIN TB_DEPARTAMENTO DEPA ON FUNC.IdDepartamento = DEPA.Id
    GROUP BY DEPA.Id, DEPA.Nome
    ORDER BY MediaSalario DESC;
''')
resultado = cursor.fetchall()
print("Média de salário por departamento em ordem decrescente:")
for linha in resultado:
    print(f"Departamento: {linha[0]} | Média de Salário: {linha[1]:.2f}")


conexao.close()