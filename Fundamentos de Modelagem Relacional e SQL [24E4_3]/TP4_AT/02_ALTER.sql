ALTER TABLE TipoUsuario RENAME TO TB_TipoUsuario;

UPDATE TB_Eventos
SET Titulo = 'TITULO NOVO'
WHERE EventoID = 3;

UPDATE TB_Usuarios
SET NomeCompleto = 'NOME COMPPLETO', Senha = 'SENHANOVA123'
WHERE UsuarioID = 5;

DELETE FROM TB_Inscricoes
WHERE InscricaoID IN (5, 8, 12);

DELETE FROM TB_Feedbacks
WHERE Nota = 1;

UPDATE TB_Feedbacks
SET Excluido = 1
WHERE FeedbackID = 10;

DROP TABLE IF EXISTS TB_Feedbacks;















