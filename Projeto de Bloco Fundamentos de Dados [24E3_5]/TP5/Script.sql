-- 1. Eventos com suas datas, localização e tipo de evento
select 
    eve.id as evento_id, 
    eve.nome as nome_evento, 
    eve.faixa_etaria, 
    dad.datade, 
    dad.dataate, 
    dad.localizacao
from tb_eventos eve
join tb_dados_eventos dad on eve.id = dad.id_evento;

-- 2. 2 eventos mais próximos de iniciar
select 
    eve.nome as nome_evento, 
    dad.datade, 
    dad.dataate, 
    dad.localizacao
from tb_eventos eve
join tb_dados_eventos dad on eve.id = dad.id_evento
order by dad.datade asc
limit 2;

-- 3. Eventos no Teatro Renaissance
select 
    eve.nome as nome_evento, 
    dad.datade, 
    dad.dataate, 
    dad.localizacao
from tb_eventos eve
join tb_dados_eventos dad on eve.id = dad.id_evento
where dad.localizacao like '%Teatro Renaissance%';

-- 4. Eventos ao ar livre
select 
    eve.nome as nome_evento, 
    dad.datade, 
    dad.dataate, 
    dad.localizacao
from tb_eventos eve
join tb_dados_eventos dad on eve.id = dad.id_evento
where dad.localizacao like '%Teatro Procópio Ferreira%';

-- 5. Metadados por evento
select 
    eve.nome as nome_evento, 
    met.metadado
from tb_eventos eve
join tb_metadados met on eve.id = met.id_evento;
