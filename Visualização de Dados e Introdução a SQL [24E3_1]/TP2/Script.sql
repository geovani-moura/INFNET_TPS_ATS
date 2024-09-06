-- 7. Liste todos os times e seus respectivos rankings FIFA.
SELECT team, fifa_ranking
FROM teams;

-- 8. Recupere os nomes dos times e o nome de seus capitães.
SELECT team, captain
FROM teams;

-- 9. Liste os times que têm um ranking FIFA menor que 10.
SELECT team, fifa_ranking
FROM teams
WHERE fifa_ranking < 10;

-- 10. Recupere os times que tiveram uma mudança positiva em seus pontos ("change_in_points" maior que 0).
SELECT team, change_in_points
FROM teams
WHERE change_in_points > 0;

-- 11. Liste os times que têm um ranking FIFA menor que 10 e que também tiveram uma mudança negativa em seus pontos.
SELECT team, fifa_ranking, change_in_points
FROM teams
WHERE fifa_ranking < 10 AND change_in_points < 0;

-- 12. Recupere os times que têm um ranking FIFA maior que 30 ou que tiveram uma mudança em seus pontos maior que 5.
SELECT team, fifa_ranking, change_in_points
FROM teams
WHERE fifa_ranking > 30 OR change_in_points > 5;

-- 13. Liste os times que estão no "Group A" ou "Group B".
SELECT team, "group"
FROM teams
WHERE "group" IN ('Group A', 'Group B');

-- 14. Recupere os times cujos treinadores são 'Didier Deschamps', 'Gareth Southgate', ou 'Cristiano Ronaldo'.
SELECT team, manager_name
FROM teams
WHERE manager_name IN ('Didier Deschamps', 'Gareth Southgate', 'Cristiano Ronaldo');

-- 15. Liste os times que têm uma média de idade dos jogadores maior que 27 anos e cujo técnico está há mais de 3 anos no cargo.
SELECT team, average_age, installation_years
FROM teams
WHERE average_age > 27 AND installation_years > 3;

-- 16. Recupere o nome dos times e seus pontos totais, mas exclua os times que têm um técnico com menos de 2 anos de instalação.
SELECT team, total_points
FROM teams
WHERE installation_years >= 2;

-- 17. Recupere o nome dos times e seus locais de treinamento, ordenados pelo nome do time.
SELECT team, training_ground
FROM teams
ORDER BY team;
