--Recuperar dados de usuários e seus eventos
SELECT 
	USU.Nickname,
	USU.NomeCompleto,
	EVT.Titulo AS Evento
FROM TB_Usuarios USU
INNER JOIN TB_Eventos EVT ON USU.UsuarioID = EVT.OrganizadorID
WHERE USU.Excluido = 0
	AND EVT.Excluido = 0;

--Listar todos os eventos e seus organizadores
SELECT 
	EVT.Titulo AS Evento,
	USU.NomeCompleto AS Organizador
FROM TB_Eventos EVT
INNER JOIN TB_Usuarios USU ON EVT.OrganizadorID = USU.UsuarioID
WHERE EVT.Excluido = 0
	AND USU.Excluido = 0;

--Mostrar todos os eventos, mesmo aqueles sem inscrições
SELECT 
	EVT.Titulo AS Evento,
	COALESCE(INS.ParticipanteID, 'Sem Inscrições') AS Inscrições
FROM TB_Eventos EVT
LEFT JOIN TB_Inscricoes INS ON EVT.EventoID = INS.EventoID
WHERE EVT.Excluido = 0;

--Usar COUNT para contar o número de participantes em cada evento
SELECT 
	EVT.Titulo AS Evento,
	COUNT(INS.ParticipanteID) AS NumParticipantes
FROM TB_Eventos EVT
LEFT JOIN TB_Inscricoes INS ON EVT.EventoID = INS.EventoID
WHERE EVT.Excluido = 0
GROUP BY EVT.EventoID;

--Calcular a nota média de feedbacks de um evento
SELECT 
	EVT.Titulo AS Evento,
	AVG(FBK.Nota) AS NotaMedia
FROM TB_Eventos EVT
LEFT JOIN TB_Feedbacks FBK ON EVT.EventoID = FBK.EventoID
WHERE EVT.Excluido = 0
	AND FBK.Excluido = 0
GROUP BY EVT.EventoID;

-- Agrupar por evento
SELECT 
	EVT.Titulo AS Evento,
	COUNT(INS.ParticipanteID) AS NumParticipantes
FROM TB_Eventos EVT
LEFT JOIN TB_Inscricoes INS ON EVT.EventoID = INS.EventoID
WHERE EVT.Excluido = 0
GROUP BY EVT.EventoID;

-- Agrupar por organizador
SELECT 
	USU.NomeCompleto AS Organizador,
	COUNT(EVT.EventoID) AS NumEventos
FROM TB_Usuarios USU
INNER JOIN TB_Eventos EVT ON USU.UsuarioID = EVT.OrganizadorID
WHERE USU.Excluido = 0
	AND EVT.Excluido = 0
GROUP BY USU.UsuarioID;



