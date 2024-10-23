-- Remover constraints
IF OBJECT_ID('FK_FUNCIONARIO_DEPARTAMENTO', 'F') IS NOT NULL
	ALTER TABLE TB_FUNCIONARIO DROP CONSTRAINT FK_FUNCIONARIO_DEPARTAMENTO;

IF OBJECT_ID('FK_CARGO_FUNCIONARIO', 'F') IS NOT NULL
	ALTER TABLE TB_FUNCIONARIO DROP CONSTRAINT FK_CARGO_FUNCIONARIO;

IF OBJECT_ID('FK_NIVEL_CARGO', 'F') IS NOT NULL
	ALTER TABLE TB_CARGO DROP CONSTRAINT FK_NIVEL_CARGO;

IF OBJECT_ID('FK_DEPARTAMENTO_FUNCIONARIO', 'F') IS NOT NULL
	ALTER TABLE TB_DEPARTAMENTO DROP CONSTRAINT FK_DEPARTAMENTO_FUNCIONARIO;

-- Remover tabelas se existirem
DROP TABLE IF EXISTS TB_FUNCIONARIO;
DROP TABLE IF EXISTS TB_CARGO;
DROP TABLE IF EXISTS TB_DEPARTAMENTO;
DROP TABLE IF EXISTS TB_NIVEL;

--Cria Tabelas
CREATE TABLE TB_NIVEL (
	Id INT NOT NULL,
	Nome VARCHAR(50) NOT NULL,
	CONSTRAINT PK_NIVEL PRIMARY KEY (Id),
);

CREATE TABLE TB_CARGO (
	Id INT IDENTITY(1,1) NOT NULL,
	IdNivel INT NOT NULL,
	Descricao VARCHAR(250),
	SalarioBase DECIMAL NOT NULL,
	CONSTRAINT PK_CARGO PRIMARY KEY (Id),
	CONSTRAINT FK_NIVEL_CARGO FOREIGN KEY (IdNivel) REFERENCES TB_NIVEL (Id),
);

CREATE TABLE TB_DEPARTAMENTO (
	Id INT NOT NULL,
	IdFuncionario INT NULL,
	Nome VARCHAR(150) NOT NULL,	
	Andar INT NOT NULL,
	CONSTRAINT PK_DEPARTAMENTO PRIMARY KEY (Id),	
);

CREATE TABLE TB_FUNCIONARIO (
	Id INT IDENTITY(1,1) NOT NULL,
	Nome VARCHAR(150),
	IdCargo INT NULL,
	IdDepartamento INT NOT NULL,
	Salario DECIMAL NOT NULL,	
	CONSTRAINT PK_FUNCIONARIO PRIMARY KEY (Id),
	CONSTRAINT FK_FUNCIONARIO_DEPARTAMENTO FOREIGN KEY (IdDepartamento) REFERENCES TB_DEPARTAMENTO (Id),
	CONSTRAINT FK_CARGO_FUNCIONARIO FOREIGN KEY (IdCargo) REFERENCES TB_CARGO (Id),
);

ALTER TABLE TB_DEPARTAMENTO
ADD CONSTRAINT FK_DEPARTAMENTO_FUNCIONARIO
FOREIGN KEY (IdFuncionario) REFERENCES TB_FUNCIONARIO (Id);

CREATE TABLE TB_HISTORICO_SALARIO (
	IdFuncionario INT NOT NULL,
	MesAno DATE NOT NULL,
	SalarioRecebido DECIMAL NOT NULL,
	CONSTRAINT PK_HISTORICO_SALARIO PRIMARY KEY (IdFuncionario, MesAno),
	CONSTRAINT FK_FUNCIONARIO_HISTORICO FOREIGN KEY (IdFuncionario) REFERENCES TB_FUNCIONARIO (Id)
);

CREATE TABLE TB_DEPENDENTE (
	Id INT IDENTITY(1,1) NOT NULL,
	IdFuncionario INT NOT NULL,
	Nome VARCHAR(150) NOT NULL,
	DataNascimento DATE NOT NULL,
	Parentesco VARCHAR(50) NOT NULL,
	CONSTRAINT PK_DEPENDENTE PRIMARY KEY (Id),
	CONSTRAINT FK_FUNCIONARIO_DEPENDENTE FOREIGN KEY (IdFuncionario) REFERENCES TB_FUNCIONARIO (Id)
);

--Popula tabelas
-- Inserindo dados na tabela TB_NIVEL
INSERT INTO TB_NIVEL (Id, Nome) VALUES (1, 'Estagiario');
INSERT INTO TB_NIVEL (Id, Nome) VALUES (2, 'Junior');
INSERT INTO TB_NIVEL (Id, Nome) VALUES (3, 'Pleno');
INSERT INTO TB_NIVEL (Id, Nome) VALUES (4, 'Senior');
INSERT INTO TB_NIVEL (Id, Nome) VALUES (5, 'Gerente');
INSERT INTO TB_NIVEL (Id, Nome) VALUES (6, 'Diretor');

-- Inserindo dados na tabela TB_CARGO
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (1, 'Analista de Sistemas', 1000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (2, 'Analista de Sistemas', 2000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (3, 'Analista de Sistemas', 4000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (4, 'Analista de Sistemas', 8000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (1, 'Analista de RH', 1000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (2, 'Analista de RH', 3000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (3, 'Analista de RH', 4500.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (4, 'Analista de RH', 6500.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (1, 'Contador', 1000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (2, 'Contador', 3000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (3, 'Contador', 5000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (4, 'Contador', 7000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (1, 'Analista de Marketing', 1000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (2, 'Analista de Marketing', 2000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (3, 'Analista de Marketing', 3000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (4, 'Analista de Marketing', 4000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (1, 'Vendedor', 1000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (2, 'Vendedor', 2000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (3, 'Vendedor', 3000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (4, 'Vendedor', 5000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (5, 'Gerente', 15000.00);
INSERT INTO TB_CARGO (IdNivel, Descricao, SalarioBase) VALUES (6, 'Diretor', 25000.00);

-- Inserindo dados na tabela TB_DEPARTAMENTO
INSERT INTO TB_DEPARTAMENTO (Id, Nome, Andar) VALUES (1, 'TI', 1);
INSERT INTO TB_DEPARTAMENTO (Id, Nome, Andar) VALUES (2, 'RH', 2);
INSERT INTO TB_DEPARTAMENTO (Id, Nome, Andar) VALUES (3, 'Financeiro', 3);
INSERT INTO TB_DEPARTAMENTO (Id, Nome, Andar) VALUES (4, 'Marketing', 4);
INSERT INTO TB_DEPARTAMENTO (Id, Nome, Andar) VALUES (5, 'Vendas', 5);
INSERT INTO TB_DEPARTAMENTO (Id, Nome, Andar) VALUES (6, 'Limpeza', 6);

-- Inserindo dados na tabela TB_FUNCIONARIO
-- Inserindo dados na tabela TB_FUNCIONARIO
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Lucas Ferreira', 1, 1, 1000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Lucas Almeida', 1, 1, 1000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Fernanda Oliveira', 2, 1, 2000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Ricardo Costa', 3, 1, 4000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Júlia Silva', 4, 1, 8000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Pedro Santos', 5, 2, 1000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Mariana Almeida', 6, 2, 3000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Carlos Pereira', 7, 2, 4500.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Ana Costa', 8, 2, 6500.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Gabriel Lima', 9, 3, 1000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Roberta Martins', 10, 3, 3000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Tatiane Rocha', 11, 3, 5000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Felipe Souza', 12, 3, 7000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Laura Nunes', 13, 4, 1000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Luana Almeida', 14, 4, 2000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Renato Silva', 15, 4, 3000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Marcela Costa', 16, 4, 4000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Eduardo Santos', 17, 5, 1000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Priscila Lima', 18, 5, 2000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Leonardo Rocha', 19, 5, 3000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Paula Pereira', 20, 5, 5000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('João Fernandes', 21, 1, 15000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Cristina Andrade', 22, 2, 25000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Juliano Lima', 21, 3, 15000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Aline Costa', 21, 4, 15000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Sandra Oliveira', 21, 5, 15000.00);
INSERT INTO TB_FUNCIONARIO (Nome, IdCargo, IdDepartamento, Salario) VALUES ('Janaina Pereira', NULL, 6, 1500.00);

-- Gerente do Departamento
UPDATE TB_DEPARTAMENTO SET IdFuncionario = (SELECT Id FROM TB_FUNCIONARIO WHERE Nome = 'João Fernandes') WHERE Nome = 'TI';
UPDATE TB_DEPARTAMENTO SET IdFuncionario = (SELECT Id FROM TB_FUNCIONARIO WHERE Nome = 'João Fernandes') WHERE Nome = 'RH';
UPDATE TB_DEPARTAMENTO SET IdFuncionario = (SELECT Id FROM TB_FUNCIONARIO WHERE Nome = 'Juliano Lima') WHERE Nome = 'Financeiro';
UPDATE TB_DEPARTAMENTO SET IdFuncionario = (SELECT Id FROM TB_FUNCIONARIO WHERE Nome = 'Aline Costa') WHERE Nome = 'Marketing';
UPDATE TB_DEPARTAMENTO SET IdFuncionario = (SELECT Id FROM TB_FUNCIONARIO WHERE Nome = 'Sandra Oliveira') WHERE Nome = 'Vendas';

--CRIAR HISTORICO DE SALARIOS
DECLARE @meses INT = 6;
DECLARE @dataAtual DATE = GETDATE();
DECLARE @i INT = 1;

WHILE @i <= @meses
BEGIN
    INSERT INTO TB_HISTORICO_SALARIO (IdFuncionario, MesAno, SalarioRecebido)
    SELECT Id, DATEADD(MONTH, -@i, @dataAtual), Salario FROM TB_FUNCIONARIO;

    SET @i = @i + 1;
END;

--Dependentes
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (1, 'Maria Ferreira', '2010-05-10', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (1, 'João Ferreira', '2012-08-20', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (2, 'Beatriz Almeida', '2015-09-15', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (2, 'Carlos Almeida', '2018-03-25', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (3, 'Sofia Oliveira', '2011-07-12', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (3, 'Lucas Oliveira', '2013-11-30', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (4, 'Pedro Costa', '2009-04-22', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (4, 'Julia Costa', '2012-10-05', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (5, 'Alice Silva', '2014-02-28', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (5, 'Eduardo Silva', '2017-06-19', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (6, 'Mariana Santos', '2012-08-23', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (6, 'Felipe Santos', '2015-11-13', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (7, 'Ana Almeida', '2010-05-10', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (7, 'Bruno Almeida', '2014-02-25', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (8, 'Gabriel Pereira', '2011-12-11', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (8, 'Isabela Pereira', '2014-09-01', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (9, 'João Costa', '2013-03-04', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (9, 'Laura Costa', '2016-07-17', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (10, 'Daniel Lima', '2010-01-09', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (10, 'Rafaela Lima', '2012-11-23', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (11, 'Henrique Martins', '2012-04-03', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (11, 'Luana Martins', '2015-09-14', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (12, 'Samuel Rocha', '2011-07-22', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (12, 'Carla Rocha', '2013-10-06', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (13, 'Eduardo Souza', '2010-05-15', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (13, 'Fernanda Souza', '2014-11-27', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (14, 'Paulo Nunes', '2013-01-19', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (14, 'Mariana Nunes', '2016-06-10', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (15, 'Lucas Almeida', '2012-12-05', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (15, 'Juliana Almeida', '2017-03-21', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (16, 'Gustavo Silva', '2011-08-02', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (16, 'Alice Silva', '2015-02-13', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (17, 'Daniel Costa', '2013-10-18', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (17, 'Clara Costa', '2016-04-11', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (18, 'André Santos', '2010-07-07', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (18, 'Isabel Santos', '2012-09-29', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (19, 'Bruno Lima', '2013-05-04', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (19, 'Sofia Lima', '2015-08-15', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (20, 'Ricardo Rocha', '2011-11-17', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (20, 'Laura Rocha', '2014-07-09', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (21, 'Carlos Pereira', '2012-06-24', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (21, 'Isabela Pereira', '2015-12-18', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (22, 'Miguel Fernandes', '2010-10-13', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (22, 'Amanda Fernandes', '2014-09-27', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (23, 'Lucas Andrade', '2011-01-02', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (23, 'Fernanda Andrade', '2013-08-19', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (24, 'Pedro Lima', '2012-02-14', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (24, 'Letícia Lima', '2016-05-23', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (25, 'Enzo Costa', '2013-11-06', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (25, 'Sabrina Costa', '2017-07-01', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (26, 'Tiago Oliveira', '2011-03-17', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (26, 'Mariana Oliveira', '2014-08-08', 'Filha');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (27, 'João Pereira', '2011-10-22', 'Filho');
INSERT INTO TB_DEPENDENTE (IdFuncionario, Nome, DataNascimento, Parentesco) VALUES (27, 'Maria Pereira', '2015-03-30', 'Filha');

