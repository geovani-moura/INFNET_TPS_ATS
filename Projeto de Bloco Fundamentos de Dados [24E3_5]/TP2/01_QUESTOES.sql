--1) Listar individualmente a tabela de Funcionários, Cargos e Departamentos em ordem alfabética.
-- Funcionários em ordem alfabética
SELECT * FROM TB_FUNCIONARIO ORDER BY Nome;

-- Cargos em ordem alfabética
SELECT * FROM TB_CARGO ORDER BY Descricao;

-- Departamentos em ordem alfabética
SELECT * FROM TB_DEPARTAMENTO ORDER BY Nome;

--2) Listar todos os departamentos que ficam no quinto andar.
SELECT * FROM TB_DEPARTAMENTO WHERE Andar = 5;

--3) Listar o analista que tem o salário mais alto.
SELECT TOP 1 f.Nome, f.Salario
FROM TB_FUNCIONARIO f
JOIN TB_CARGO c ON f.IdCargo = c.Id
WHERE c.Descricao LIKE '%Analista%'
ORDER BY f.Salario DESC;

--4) Listar os funcionários que têm seu salário maior ou igual ao salário base no departamento de TI.
SELECT f.Nome, f.Salario
FROM TB_FUNCIONARIO f
JOIN TB_CARGO c ON f.IdCargo = c.Id
JOIN TB_DEPARTAMENTO d ON f.IdDepartamento = d.Id
WHERE d.Nome = 'TI' AND f.Salario >= c.SalarioBase;

--5) Listar qual departamento que possui o maior número de estagiários.
SELECT TOP 1 d.Nome,
	COUNT(*) AS NumeroEstagiarios
FROM TB_FUNCIONARIO f
INNER JOIN TB_CARGO c ON f.IdCargo = c.Id
INNER JOIN TB_DEPARTAMENTO d ON f.IdDepartamento = d.Id
WHERE c.IdNivel = 1
GROUP BY d.Nome
ORDER BY NumeroEstagiarios DESC;

--6) Listar todos os funcionários que não possuem um cargo associado.
SELECT * FROM TB_FUNCIONARIO WHERE IdCargo IS NULL;

--7) Listar todos os funcionários que estão no andar mais alto.
SELECT f.Nome, d.Nome AS Departamento, d.Andar
FROM TB_FUNCIONARIO f
JOIN TB_DEPARTAMENTO d ON f.IdDepartamento = d.Id
WHERE d.Andar = (SELECT MAX(Andar) FROM TB_DEPARTAMENTO);

--8) Listar o cargo que possui funcionários que ganham entre 3000 e 5000.
SELECT DISTINCT c.Descricao
FROM TB_FUNCIONARIO f
JOIN TB_CARGO c ON f.IdCargo = c.Id
WHERE f.Salario BETWEEN 3000 AND 5000;

--9) Listar o nome de todos os gerentes que efetivamente chefiam pelo menos 2 departamentos.
SELECT f.Nome
FROM TB_FUNCIONARIO f
JOIN TB_CARGO c ON f.IdCargo = c.Id
JOIN TB_DEPARTAMENTO d ON d.IdFuncionario = f.Id
WHERE c.IdNivel = 5
GROUP BY f.Nome
HAVING COUNT(DISTINCT d.Id) >= 2;

--10) Listar o cargo que possui o salário mais baixo.
SELECT TOP 1 c.Descricao, c.SalarioBase
FROM TB_CARGO c
ORDER BY c.SalarioBase ASC;

--11) Listar o departamento que o salário mais alto.
SELECT TOP 1 d.Nome, MAX(f.Salario) AS SalarioMaisAlto
FROM TB_FUNCIONARIO f
JOIN TB_DEPARTAMENTO d ON f.IdDepartamento = d.Id
GROUP BY d.Nome
ORDER BY SalarioMaisAlto DESC;

--12) Listar o andar onde ficam os diretores.
SELECT DISTINCT d.Andar
FROM TB_FUNCIONARIO f
JOIN TB_CARGO c ON f.IdCargo = c.Id
JOIN TB_DEPARTAMENTO d ON f.IdDepartamento = d.Id
WHERE c.IdNivel = 6

--13) Listar funcionários em ordem alfabética, que atendam a uma lógica criada por você, a partir do campo escolhido, que foi definido na tabela de funcionários.
SELECT Nome, Salario
FROM TB_FUNCIONARIO
ORDER BY Salario;

--14) Listar cargos em ordem alfabética, que atendam a uma lógica criada por você, a partir do campo escolhido, que foi definido na tabela de cargos.
SELECT Descricao, SalarioBase
FROM TB_CARGO
ORDER BY Descricao;

--15) Listar departamentos em ordem alfabética, que atendam a uma lógica criada por você, a partir do campo escolhido, que foi definido na tabela de departamentos.
SELECT Nome, Andar
FROM TB_DEPARTAMENTO
ORDER BY Nome;





