[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/lXi71Ddk)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17034524)
Chegamos em uma das etapas de preparação! A cada Teste de Performance (TP) você terá a oportunidade de praticar os conhecimentos adquiridos e receber feedbacks relevantes para o seu aprendizado.


# TP2

## Competencias Avaliadas:

Manipulação de Arquivos (CSV e JSON) e utilizando o pandas para criar a rede INFwebNET.

---

**Contexto:** Você continua sendo um cientista de dados na INFwebNET, mas agora o foco é a manipulação de arquivos em diferentes formatos. A INFwebNET armazena dados em arquivos CSV e JSON, e você precisa usar suas habilidades em Python e pandas para processar esses dados de forma eficiente e organizada.

## Níveis de Dificuldade:

* *Fácil*  (★):  Leitura e escrita básica de arquivos.
* *Médio* (★★):  Manipulação de dados, formatação e uso de módulos.
* *Difícil* (★★★):  Processamento avançado, otimização e  integração de  ferramentas.

**Disclaimer:** Desculpem a falta de criatividade, podem me sacanear, mas precisei utilizar o termo *INFNETianos* para distinguir o usuário que opera o sistema do usuário da rede social INFwebNet.

---

## Enunciados:

1. **(★) "Abrindo as Portas":** Escreva um programa que leia o arquivo ""rede_INFNET_atualizado.txt" que foi elaborado no seu TP1, que contém dados básicos dos usuários (nome, idade, cidade, estado) - INFNETianos, e utilizando a biblioteca csv, exporte um arquivo “INFwebNet.csv” contendo os mesmos dados.--
   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2. **(★★) "Estruturando os Dados”:** Utilizando apenas as bibliotecas csv e json, leia os dados do arquivo csv criado no item anterior, parseie as informações para uma estrutura json e exporte o arquivo “INFwebNET.json” devidamente estruturado.
   ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
3. **(★★) "Cadastro Simplificado"**:  Crie um programa que permita ao usuário inserir novos INFNETianos (nome, idade, cidade, estado) e salve essas informações no arquivo "“INFwebNET.json", utilizando o módulo json.
   -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
4. **(★) "Análise com Pandas":** Utilize o Pandas para ler o arquivo "“INFwebNET.json". Calcule a média de idade dos INFNETianos e exiba o resultado.
   --------------------------------------------------------------------------------------------------------------------------------------------------
5. **(★★★) "Ampliando as Informações”:** Elabore uma função que permita inserir novos INFNETianos na rede INFwebNet incluindo novos campos de dados. Além dos dados já existentes poderão serem incluídos os campos “hobbys” que conterá uma lista de atividades de interesse do INFNETiano, um campo “coding” que deverá conter uma lista de linguagens de programação que INFNETiano utiliza e uma lista de dicionários contendo os campos “jogos” e “plataforma”, onde o usuário poderá informar os jogos favoritos e a respectiva plataforma na qual o INFNETiano jogou aquele jogo.
   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
6. **(★★) "Dados Delimitados":**  A INFwebNET recebeu um arquivo "dados_usuarios_novos.txt" com dados dos novos INFNETianos separados por ponto e vírgula (;).  Utilize o módulo csv para ler esse arquivo, especificando o delimitador correto. (O arquivo está disponível no repositório específico do TP2).
   ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
7. **(★★★) “Organizando a Bagunça”:** Após ter obtido dados de diferentes bases de dados você precisa avançar um passo e reunir todas as informações do INFwebNet em um único DataFrame Pandas. (Lembre-se de estruturar as Séries adequadamente).
   --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
8. **(★★) “Criando Informações”:** Crie uma nova coluna no dataset chamada “ano_nascimento” considerando a data atual e informação presente na coluna idade.
   ---------------------------------------------------------------------------------------------------------------------------------------------------------------
9. **(★★) “Completando os Dados”:** Considerando os campos existentes no dataset obtido, utilize o Pandas para preencher adequadamente 2 campos onde houverem valores ausentes. Explique e justifique o critério utilizado.
   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
10. **(★) “Guardando as Informações”:** Utilizando o Pandas salve todo o banco de dados do INFwebNet em um arquivo json chamado “INFwebNet_Data.json".
    ----------------------------------------------------------------------------------------------------------------------------------------------------
11. **(★★) “Selecionando Grupos”:** Utilize o pandas para filtrar os INFNETianos pelo estado onde mora. Salve os usuários de cada estado em um arquivo csv nomeado como “grupo_##.csv”, onde ## deve ser substituído pela sigla do estado.
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
12. **(★) “Agrupando INFNETianos”:** Crie uma função que seja capaz de filtrar usuários por ano de nascimento, dado dois valores de ano e exiba todos os usuários que nasceram nestes anos.
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
13. **(★★★) “Selecionando INFNETiano”:** Crie uma função que permita buscar um usuário pelo nome e exiba o(s) INFNETiano(s) que possui(em) este nome e permita o usuário selecionar o INFNETiano.
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
14. **(★★) “Atualizando Dados”:** Após o INFNETiano ter sido selecionado no item anterior permita que seus dados sejam atualizados. Lembrando que deve haver um limite de até 5 hobbies e 5 jogos.
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
15. **(★★) “Trending”:** Elabore um recurso que permita exibir as 5 linguagens mais citadas entre os INFNETianos e exiba contagem de vezes que cada uma foi citada.4
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------

### *`Sinal Amarelo* `

- É permitida a consulta a ferramentas de IA apenas se for para adicionar complexidades para além do escopo do curso e apenas nas questões marcadas com (★★★). Ao usar deverá ser informado a ferramenta escolhida e o prompt fornecido. Todas os demais casos: sinal vermelho.
