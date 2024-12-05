-- TipoUsuario
INSERT INTO TipoUsuario (TipoUsuario) VALUES
('Organizador'),
('Participante');

-- Usuários
INSERT INTO TB_Usuarios (Nickname, Senha, NomeCompleto, Email, TipoUsuarioID, Excluido) VALUES
('organizador1', 'senha123', 'João Silva', 'joao.silva@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Organizador'), FALSE),
('organizador2', 'senha123', 'Maria Oliveira', 'maria.oliveira@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Organizador'), FALSE),
('organizador3', 'senha123', 'Carlos Souza', 'carlos.souza@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Organizador'), FALSE),
('organizador4', 'senha123', 'Ana Lima', 'ana.lima@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Organizador'), FALSE),
('organizador5', 'senha123', 'Lucas Almeida', 'lucas.almeida@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Organizador'), FALSE),
('participante1', 'senha123', 'Fernanda Costa', 'fernanda.costa@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Participante'), FALSE),
('participante2', 'senha123', 'Ricardo Pereira', 'ricardo.pereira@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Participante'), FALSE),
('participante3', 'senha123', 'Juliana Cardoso', 'juliana.cardoso@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Participante'), FALSE),
('participante4', 'senha123', 'Gabriel Rocha', 'gabriel.rocha@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Participante'), FALSE),
('participante5', 'senha123', 'Larissa Santos', 'larissa.santos@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Participante'), FALSE),
('participante6', 'senha123', 'Felipe Araújo', 'felipe.araujo@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Participante'), FALSE),
('participante7', 'senha123', 'Camila Ribeiro', 'camila.ribeiro@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Participante'), FALSE),
('participante8', 'senha123', 'Gustavo Martins', 'gustavo.martins@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Participante'), FALSE),
('participante9', 'senha123', 'Patrícia Barros', 'patricia.barros@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Participante'), FALSE),
('participante10', 'senha123', 'Thiago Medeiros', 'thiago.medeiros@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Participante'), FALSE),
('organizador6', 'senha123', 'Bianca Monteiro', 'bianca.monteiro@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Organizador'), FALSE),
('organizador7', 'senha123', 'Eduardo Teixeira', 'eduardo.teixeira@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Organizador'), FALSE),
('organizador8', 'senha123', 'Rafaela Torres', 'rafaela.torres@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Organizador'), FALSE),
('organizador9', 'senha123', 'Vinícius Lima', 'vinicius.lima@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Organizador'), FALSE),
('organizador10', 'senha123', 'Mariana Borges', 'mariana.borges@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Organizador'), FALSE),
('participante11', 'senha123', 'Leandro Mendes', 'leandro.mendes@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Participante'), FALSE),
('participante12', 'senha123', 'Tatiane Freitas', 'tatiane.freitas@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Participante'), FALSE),
('participante13', 'senha123', 'Pedro Henrique', 'pedro.henrique@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Participante'), FALSE),
('participante14', 'senha123', 'Vanessa Faria', 'vanessa.faria@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Participante'), FALSE),
('participante15', 'senha123', 'Alexandre Cunha', 'alexandre.cunha@email.com', (SELECT TipoUsuarioID FROM TipoUsuario WHERE TipoUsuario = 'Participante'), FALSE);

--Eventos
INSERT INTO TB_Eventos (Titulo, Descricao, Data, Hora, Local, OrganizadorID, Excluido) VALUES
('Workshop de Programação', 'Aprenda os fundamentos de programação com especialistas.', '2024-12-10', '09:00:00', 'Centro de Convenções ABC', 1, FALSE),
('Palestra sobre IA', 'Descubra as últimas tendências em Inteligência Artificial.', '2024-12-15', '14:00:00', 'Auditório XYZ', 2, FALSE),
('Curso de Marketing Digital', 'Curso completo para alavancar negócios online.', '2024-12-20', '10:00:00', 'Sala de Treinamento 5', 3, FALSE),
('Encontro de Startups', 'Networking e troca de ideias entre empreendedores.', '2024-12-25', '16:00:00', 'Espaço Colaborativo Beta', 4, FALSE),
('Seminário de Sustentabilidade', 'Discussão sobre práticas sustentáveis no mercado.', '2024-12-30', '11:00:00', 'Green Center Hall', 5, FALSE);

--Inscricoes
INSERT INTO TB_Inscricoes (EventoID, ParticipanteID, DataInscricao, Excluido) VALUES
(1, 6, '2024-12-01', FALSE),
(1, 7, '2024-12-01', FALSE),
(1, 8, '2024-12-02', FALSE),
(1, 9, '2024-12-03', FALSE),
(1, 10, '2024-12-04', FALSE),
(2, 11, '2024-12-05', FALSE),
(2, 12, '2024-12-06', FALSE),
(2, 13, '2024-12-07', FALSE),
(2, 14, '2024-12-08', FALSE),
(2, 15, '2024-12-09', FALSE),
(3, 6, '2024-12-10', FALSE),
(3, 7, '2024-12-11', FALSE),
(3, 8, '2024-12-12', FALSE),
(3, 9, '2024-12-13', FALSE),
(3, 10, '2024-12-14', FALSE),
(4, 11, '2024-12-15', FALSE),
(4, 12, '2024-12-16', FALSE),
(4, 13, '2024-12-17', FALSE),
(4, 14, '2024-12-18', FALSE),
(4, 15, '2024-12-19', FALSE);

--Feedbacks
INSERT INTO TB_Feedbacks (EventoID, ParticipanteID, Nota, Comentario, Excluido) VALUES
(1, 6, 1, 'O evento foi abaixo do esperado.', FALSE),
(1, 7, 2, 'O conteúdo poderia ser melhor.', FALSE),
(1, 8, 3, 'Foi razoável, mas precisa melhorar.', FALSE),
(1, 9, 1, 'Não atendeu às expectativas.', FALSE),
(1, 10, 2, 'Mediocre, mas com alguns pontos positivos.', FALSE),
(2, 11, 2, 'A organização foi mediana.', FALSE),
(2, 12, 3, 'O evento foi bom, mas há espaço para melhorias.', FALSE),
(2, 13, 4, 'Gostei bastante, superou minhas expectativas.', FALSE),
(2, 14, 2, 'A palestra foi interessante, mas faltou algo.', FALSE),
(2, 15, 3, 'Uma experiência agradável, mas poderia melhorar.', FALSE),
(3, 6, 3, 'Bom evento, mas pode ser melhorado.', FALSE),
(3, 7, 4, 'Muito bom, recomendo a todos.', FALSE),
(3, 8, 5, 'Excelente evento, superou as expectativas!', FALSE),
(3, 9, 4, 'Gostei muito, aprendizados valiosos.', FALSE),
(3, 10, 5, 'Ótima organização e conteúdo excelente.', FALSE);

