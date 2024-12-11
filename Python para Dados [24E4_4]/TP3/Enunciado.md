**Contexto**: Você continua como cientista de dados na INFwebNET, agora com novas responsabilidades relacionadas ao gerenciamento e análise de dados armazenados em arquivos Excel e um banco de dados SQL. Os exercícios a seguir irão guiá-lo por situações práticas que abrangem a manipulação de dados, tratamento de exceções e o uso do SQL para nossa rede social fictícia.   
Prepare-se para consolidar e expandir suas habilidades\!  
Leia todo o enunciado.   
Você pode decidir atender a mais de um item com uma única função se achar conveniente, indique quais itens estão sendo atendidos em cada trecho ou bloco de código.

* Sinal vermelho.

---

### Questões:

1) **Tratamento de Erros ao Carregar Arquivo**  
   Abra o arquivo "dados\_usuarios.csv" usando o bloco try...except. Exiba uma mensagem de erro se o arquivo não for encontrado (erro específico) e informe ao usuário que o arquivo está em falta.

2) **Explorando Dados do Excel**  
   Abra o arquivo "dados\_usuarios.csv", que contém informações dos usuários. Exiba as 10 primeiras linhas do arquivo e liste todas as colunas presentes no arquivo.

3) **Manipulação de Dados Básica**  
   Usando Pandas, selecione apenas os usuários com idade maior que 30 e salve esses dados em um novo arquivo chamado "INFwebNET\_30mais.xlsx".

**Limpeza de Dados**  
Para o DataFrame anterior proceda com as seguintes tarefas de limpeza de dados:

4) Remova todos os usuários que não possuírem e-mail válido cadastrado.  
5) Preencha os valores ausente do campo “cidade” com o texto “Não Informada”.  
6) Preencha os dados ausentes na coluna “estado” com “ZZ”.

7) **Combinação de Arquivos Excel**  
   A INFwebNET possui dados históricos de usuários em arquivo Excel com o nome “INFwebNET\_Historico.xlsx”, onde há duas tabelas, “INFwebNET2022” e “INFwebNET2023”, cada uma referente a um ano.   
   Use um bloco try...except para carregar as planilhas do arquivo "INFwebNET\_Historico.xlsx" e, se o arquivo for carregado com sucesso, exiba o número total de linhas de cada planilha. Caso ocorra uma exceção, mostre uma mensagem de erro apropriada.

8) **Combinação de Arquivos Excel**   
   Carregue a informação das duas planilhas, combine as informações em um único DataFrame e remova duplicatas baseado na coluna "id".  
     
9) **Carregando Dados em SQL**  
   Conecte-se a um banco de dados SQLite chamado "INFwebNET\_DB.db" usando SQLAlchemy. Carregue os dados combinados do item anterior para uma tabela chamada "Usuarios\_Historicos".  
     
10) **Consultando o Banco de Dados SQL**  
    Escreva uma consulta usando Pandas que retorne apenas os usuários com idade entre 22 e 30 anos existentes na tabela “Usuarios\_Historicos”. Exiba o resultado na tela.  
      
11) **Consolidando Dados**  
    Utilizando o Pandas e SQLAlchemy crie uma nova tabela no banco de dados chamada “Consolidado” e insira nesta tabela todos os dados obtidos nos itens anteriores.  
      
12) **Atualizando idade**  
    Consulte todos os dados da tabela “Consolidado” e recalcule a idade de todos os usuários considerando a data de 22 de julho de 2024\. Exporte os dados atualizados para uma tabela SQL chamada “Consolidado\_Atualizado”.  
      
13) **Exceção Customizada para Dados Ausentes**  
    Implemente uma função que leia os dados da tabela “Consolidado” e lance uma exceção customizada chamada "DadosAusentesError" se alguma coluna apresentar um dado faltante. Utilize um bloco try...except para capturar essa exceção e listar o e-mail do INFNETiano em questão caso a exceção seja levantada, e salve o e-mail em um arquivo txt chamado, “dados\_ausentes.txt”.  
    

**Try…Except Completo**  
Escreva uma função que leia todos os arquivos: “dados\_usuario.csv”, “INFwebNET\_30mais.xlsx", “INFwebNET\_Historico.xlsx”, "INFwebNET\_DB.db" e “dados\_ausentes.txt” utilizando uma estrutura `try...except` completa de forma que cada tentativa de leitura seja feita dentro de um try que capture e lide com os seguintes tipos de exceções: \`FileNotFoundError\`, \`MemoryError\`, \`RuntimeError\`, \`EOFError\`, \`OSError\`, \`ConnectionError\`, \`TimeoutError\` e \`PermissionError\`.

14) Lide com cada tipo de exceção exibindo uma mensagem apropriada e segua para o próximo arquivo ou encerre o programa quando for apropriado.  
15) Utilize um bloco else para exibir a quantidade de linhas existentes no arquivo lido  
16) Utilize um bloco finally para garantir o fechamento do arquivo ou da conexão.

---

### Entrega:

Para a entrega, certifique-se de incluir o banco de dados SQLite e arquivos resultantes de todas as manipulações e códigos em .py ou .ipynb.  
A entrega deverá ser feita pelo repositório desta atividade e em um arquivo zip através da plataforma.
