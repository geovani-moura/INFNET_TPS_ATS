--Parte 3 - Queries SQL

--1. Crie queries SQL simples para recuperar informações:
--a. Mostre todos os países e suas respectivas contagens de medalhas por esporte.
SELECT 
	Country, 
	Sport, 
	Gold, 
	Silver, 
	Bronze 
FROM 
	olimpiadas;

--b. Filtre países que tenham ganhado mais de 10 medalhas de ouro em um único esporte.
SELECT 
	Country, 
	Sport, 
	Gold
FROM 
	olimpiadas
WHERE 
	Gold > 10;

--c. Mostre todos os países que têm entre 3 e 15 medalhas(total) em esportes de combate (ex.: Boxing, Judo, Karate, Taekwondo).
SELECT 
	Country,
	Sport,
	Total
FROM olimpiadas
WHERE Sport IN ('Boxing', 'Judo', 'Karate', 'Taekwondo')
	AND Total BETWEEN 3 AND 15;

--d. Liste os países que ganharam exatamente 3 medalhas de bronze em esportes aquáticos limitando a 5 resultados.
SELECT 
	Country,
	Sport,
	Bronze
FROM olimpiadas
WHERE Sport IN ('Swimming', 'Diving', 'Artistic Swimming', 'Water Polo')
	AND Bronze = 3 LIMIT 5;

--2. Questão Reflexiva: Os dados das Olimpíadas revelam padrões interessantes sobre o desempenho de diferentes países em vários esportes. Com base nos resultados das consultas e na sua própria pesquisa, reflita sobre os seguintes pontos:
--a. Esportes de Combate: O Japão é frequentemente associado a esportes de combate, como judô e karatê. No entanto, será que os dados das Olimpíadas confirmam essa suposição? Quais fatores culturais, históricos ou de treinamento podem explicar o desempenho do Japão nesses esportes? Compare os resultados do Japão com os de outros países que também se destacam em esportes de combate.
SELECT 
	Country,
	SUM(Total)[TOTAL]
FROM olimpiadas A
WHERE 
	A.Sport IN ('Boxing', 'Judo', 'Taekwondo', 'Wrestling', 'Karate')
GROUP BY 
	Country,
	Total
ORDER BY
	TOTAL DESC

--Parte 4 - Agrupamento e Ordenação

--1. Utilize GROUP BY e ORDER BY para realizar as seguintes tarefas:
--a. Agrupe os países por nome e esporte e mostre a soma total de medalhas.
SELECT 
	Country,
	Sport,
	SUM(Total)[TOTAL]
FROM olimpiadas
GROUP BY 
	Country,
	Sport
ORDER BY 
	Country,
	Sport;

--b. Ordene os países em ordem decrescente pelo número de medalhas de ouro em um esporte específico (ex.: atletismo).
SELECT 
	Country,
	Gold
FROM olimpiadas
WHERE Sport = 'Taekwondo'
ORDER BY Gold DESC;

--2. Realize consultas utilizando HAVING e DISTINCT:
--a. (Desafiador) Liste os países que ganharam medalhas em pelo menos três esportes diferentes e onde o número total de medalhas seja maior que a soma das medalhas de ouro e prata.
SELECT 
	Country,
	SUM(Total)[TOTAL],
	SUM(Gold) + SUM(Silver)[GOLD_SILVER]
FROM olimpiadas
GROUP BY 
	Country
HAVING COUNT(DISTINCT Sport) >= 3
	AND SUM(Total) > SUM(Gold) + SUM(Silver);

--b. Filtre apenas os países que têm mais de 5 medalhas em esportes de precisão (ex.: tiro, arco e flecha).
SELECT 
	Country,
	SUM(Total)[TOTAL]	
FROM olimpiadas
WHERE Sport IN ('Shooting', 'Archery')
GROUP BY Country
HAVING SUM(Total) > 5;

--3. Questão Reflexiva: 
--a. Esportes Nacionais e Cultura: Escolha um país e explore como um esporte específico reflete a cultura e a história desse país. Por exemplo, por que o Quênia se destaca tanto nas corridas de longa distância? O que torna esse país uma potência no atletismo? Ou, por que os Estados Unidos têm tanto sucesso em várias modalidades?
SELECT 
	A.* 
FROM olimpiadas A
JOIN (
	SELECT 
		id, 
		Sport, 
		MAX(Total) AS Max_Total
    FROM olimpiadas
    GROUP BY Sport
) B ON A.id = B.id
WHERE 1=1
	AND A.Country = 'France'
















































