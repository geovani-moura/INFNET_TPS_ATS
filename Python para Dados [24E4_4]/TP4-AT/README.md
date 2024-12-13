[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/27P3yd49)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17447577)
# Enunciado:

---

Chegamos no momento mais importante\! Você veio ao longo dos TPs se preparando e agora chegou a hora da sua avaliação.

## **Contexto**

Você é um cientista de dados trabalhando para a **INFwebNET**, uma rede social fictícia. Ao longo dos Testes de Performance (TPs) anteriores, você desenvolveu várias ferramentas e scripts para manipular dados dos usuários, amigos, hobbies, jogos e plataformas. Agora, você precisa integrar essas informações com dados externos, realizando **web scraping** para enriquecer o banco de dados da INFwebNET.

Seu objetivo é extrair informações da **Wikipédia** sobre as plataformas de jogos citadas nos arquivos utilizados anteriormente, coletar informações de tabelas que contêm listas de jogos, encontrar todos os jogos que foram citados pelos usuários da INFwebNET, associá-los à plataforma e salvar em um arquivo JSON as informações extraídas.

## **Níveis de Dificuldade**

* **Fácil (★):** Envolve conceitos básicos e aplicação direta de métodos.
* **Médio (★★):** Requer maior compreensão dos conceitos e combinação de diferentes métodos.
* **Difícil (★★★):** Exige aplicação criativa dos conceitos, resolução de problemas e otimização de código.

## **Uso de IAs: Sinal Vermelho 🔴**

Todas as partes deste trabalho devem ser da autoria do aluno. Qualquer uso de ferramentas generativas de IA, como ChatGPT, é proibido. O uso de IA generativa será considerado má conduta acadêmica e estará sujeito à aplicação do código disciplinar, pois as tarefas deste trabalho foram elaboradas para desafiar o aluno a desenvolver conhecimentos de base, pensamento crítico e habilidades de resolução de problemas. O uso da tecnologia de IA limitaria sua capacidade de desenvolver essas competências e de atingir os objetivos de aprendizagem desta disciplina.

---

### **1\. Preparação dos Dados (★)**

Crie uma função chamada `carregar_dados` que não recebe parâmetros e retorna um DataFrame do Pandas contendo os dados do arquivo **"INFwebNet\_Data.json"** (criado no TP2). A função deve:

* Verificar se todas as colunas estão presentes e se os dados foram carregados corretamente.
* Preencher os campos vazios com o valor **"Não Informado"** onde houver dados faltantes.

---

### **2\. Extração de Plataformas (★)**

Crie uma função chamada `extrair_plataformas` que recebe como parâmetro o DataFrame retornado pela função `carregar_dados` e retorna um **set** contendo os nomes únicos das **plataformas de jogos** mencionadas pelos usuários na coluna "plataforma" associada aos jogos que eles jogam. Salve este set em um arquivo chamado **"plataformas.txt"**, com um nome de plataforma por linha.

**Observação:** Certifique-se de utilizar um **set** para garantir a unicidade dos nomes das plataformas.

---

### **3\. Tratamento de Exceções ao Carregar Plataformas (★)**

Implemente uma função chamada `carregar_plataformas` que tenta carregar o arquivo **"plataformas.txt"** e retorna uma lista com os nomes das plataformas. Se o arquivo não for encontrado, a função deve:

* Exibir uma mensagem de erro informando que o arquivo está em falta.
* Solicitar ao usuário que insira o caminho correto do arquivo ou digite **'sair'** para encerrar o programa.
* Se o usuário fornecer um novo caminho, tentar carregar o arquivo novamente.
* Se o usuário digitar **'sair'**, encerrar o programa.

---

### **4\. Download de Páginas da Wikipédia (★★)**

Crie uma função chamada `baixar_paginas_wikipedia` que recebe como parâmetro a lista de plataformas retornada pela função `carregar_plataformas` e retorna uma lista com os caminhos para os arquivos gerados. Para cada plataforma, a função deve:

* Formar a URL correspondente na Wikipédia em português no formato `https://pt.wikipedia.org/wiki/Lista_de_jogos_para_{Nome_da_Plataforma}`, substituindo **`{Nome_da_Plataforma}`** pelo nome da plataforma, utilizando underscores (`_`) no lugar de espaços.
* Utilizar a biblioteca **urllib** para fazer o download da página HTML.
* Salvar o conteúdo HTML em arquivos individuais chamados **"plataforma\_Nome.html"**, onde **Nome** é o nome da plataforma, substituindo espaços por underscores.

**Exemplo:**

Para a plataforma **"PlayStation 4"**, a URL seria `https://pt.wikipedia.org/wiki/Lista_de_jogos_para_PlayStation_4` e o arquivo salvo seria **"plataforma\_PlayStation\_4.html"**.

---

### **5\. Tratamento de Exceções no Download (★★)**

Modifique a função `baixar_paginas_wikipedia` para incluir tratamento de exceções durante o download. Se ocorrer um erro (como `HTTPError` ou `URLError`):

* Registrar o nome da plataforma e o erro em um arquivo de log chamado **"erros\_download.txt"**.
* Continuar o processo de download para as próximas plataformas.
* **Desafio recurso extra (implementação opcional):**

  * Caso a página retorne erro 404, parsear a estrutura similar à:
* `<p> <b>A Wikipédia não possui um artigo com este nome exato.</b> Por favor, <a href="/wiki/Especial:Pesquisar/Lista_de_jogos_para_Nintendo_switch" title="Especial:Pesquisar/Lista de jogos para Nintendo switch">procure por <i>Lista de jogos para Nintendo switch</i> na Wikipédia</a> para buscar por títulos alternativos. </p>`
* Utilizar o valor de `href` para baixar a página correta.

---

### **6\. Parsing das Páginas HTML (★★)**

Crie uma função chamada `parsear_paginas` que recebe o caminho do arquivo HTML criado como parâmetro. A função deve:

* Utilizar o **BeautifulSoup** para parsear o conteúdo HTML do arquivo.
* Extrair o **título da página** (tag `<title>`) e confirmar se ao menos parte do título extraído corresponde ao nome da plataforma. Ignore diferenças de maiúsculas/minúsculas e acentuação.
* Se o título não corresponder, levantar uma exceção personalizada e registrar o caso em um arquivo **"erros\_parse.txt"**.

---

### **7\. Extração de Tabelas de Jogos (★★)**

Dentro da função `parsear_paginas`, após a verificação do título, a função deve:

* Localizar a ou as **tabelas** que contêm a lista de jogos disponíveis para a plataforma. Essas tabelas geralmente estão identificadas pela classe `"wikitable"` ou possuem um cabeçalho específico.
* Extrair os dados dos jogos, incluindo as colunas disponíveis (por exemplo, "Título", "Desenvolvedor", "Data de lançamento", etc.).
* Armazenar os dados em uma estrutura de dados conforme o formato especificado no item 9\.

**Observação:** Certifique-se de capturar todas as tabelas relevantes que contêm listas de jogos.

---

### **8\. Uso de Expressões Regulares (★★)**

Crie uma função chamada `extrair_urls_emails` que percorre todos os arquivos **"plataforma\_Nome.html"** e, utilizando **expressões regulares** em conjunto com o BeautifulSoup, extrai todas as **URLs** e **e-mails** presentes nas páginas. Armazene esses dados em um dicionário com as chaves "urls" e "emails" e salve em um arquivo JSON chamado **"conexoes\_plataformas.json"**.

- **regex e-mail: `r"^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$"`**
- **regex urls: `r"((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[.\!\/\\w]*))?)"`**

---

### **9\. Exportação dos Dados (★★★)**

**Enunciado:**

Crie uma função chamada `exportar_dados_jogos` que recebe a estrutura de dados com os jogos extraídos e salva em um arquivo JSON chamado **"dados\_jogos\_plataformas.json"** no seguinte formato:

```json

[  {    "plataforma": "Nome_da_Plataforma",    "jogos": [    {    "nome_jogo": "Nome_do_Jogo",    "dados_jogo": {    "campo_1": "valor_1",    "campo_2": "valor_2",    ...    }    },    ...    ]  },  ...]
```


**Observações:**

* Os "campos" em "dados\_jogo" devem ser os nomes das colunas da tabela extraída.
* Certifique-se de que todos os dados estão corretamente estruturados conforme o formato acima.

---

### **10\. Associação de Jogos aos Usuários (★★)**

Crie uma função chamada `associar_jogos_usuarios` que recebe como parâmetros:

* O DataFrame dos usuários retornado por `carregar_dados`.
* A estrutura de dados com os jogos extraídos no formato especificado.

A função deve:

* Para cada usuário, verificar quais jogos mencionados por ele estão presentes na lista de jogos extraídos das páginas das plataformas.
* Criar uma associação entre o usuário, o jogo e a plataforma correspondente.
* Atualizar o DataFrame dos usuários, adicionando uma coluna que contém uma lista de dicionários com os jogos e plataformas associados.

---

### **11\. Atualização do Banco de Dados (★★)**

Crie uma função chamada `atualizar_banco_dados` que atualiza o banco de dados SQLite **"INFwebNET\_DB.db"**, criado no TP3, adicionando uma nova tabela chamada **"Jogos\_Plataformas"** que contém as informações dos jogos e plataformas extraídos. Use **SQLAlchemy** e **Pandas** para realizar esta operação.

---

### **12\. Consulta aos Dados (★★)**

Crie uma função chamada `consultar_usuarios_por_jogo` que recebe como parâmetro o nome de um jogo e retorna uma lista de usuários que jogam esse jogo. A função deve:

* Permitir que o nome do jogo seja fornecido pelo usuário via `input()`.
* Realizar a consulta no banco de dados atualizado.
* Exibir os nomes dos usuários encontrados.

---

### **13\. Análise Estatística (★★)**

Crie uma função chamada `plataforma_mais_popular` que utiliza o banco de dados para calcular qual é a **plataforma mais popular** entre os usuários da INFwebNET, com base nos jogos que eles jogam. A função deve:

* Contar o número de usuários que jogam jogos em cada plataforma.
* Exibir o nome da plataforma mais popular e o número de usuários.

---

### **14\. Guardando as Informações (★)**

Crie uma função chamada `salvar_dados_completos` que não recebe parâmetros e salva todas as informações associadas (usuários, jogos, plataformas) em um arquivo JSON chamado **"INFwebNET\_Completo.json"**. O arquivo deve conter uma lista de usuários, onde cada usuário possui seus dados pessoais e uma lista de jogos que ele joga, com as respectivas plataformas.

---

### **15\. Documentação do Código (★)**

Documente adequadamente ao menos as **cinco funções que você considere mais importantes e complexas** do seu código usando **docstrings** no formato **PEP 257**, explicando o propósito de cada função, os parâmetros esperados e os valores retornados.

---

### **16\. Relatório Final (★★)**

Elabore um **breve relatório** (máximo de duas páginas) descrevendo as etapas realizadas, as dificuldades encontradas e como as competências foram aplicadas na resolução do problema. E, opcionalmente, sua percepção e feedback sobre o curso.

---

## **Observações Importantes**

* **Interação com o Usuário:** Todas as entradas do usuário devem ser solicitadas através da função `input()`, seguindo as instruções de cada item.
* **Nomes de Funções e Arquivos:** Utilize exatamente os nomes especificados para funções e arquivos, podendo utilizar outras funções auxiliares caso julgue necessário.
* **Formatação do Código:** Siga as normas de estilo recomendadas na **PEP 8** ao escrever seu código. Use indentação consistente, nomes de variáveis significativos e comentários quando necessário.
* **Dados Faltantes:** Onde houver dados faltantes, insira o valor **"Não Informado"**.
* **Endereços da Wikipédia:** Utilize as URLs formadas no formato `https://pt.wikipedia.org/wiki/Lista_de_jogos_para_Nome_da_Plataforma`, substituindo espaços por underscores.
* **Uso de Sets:** Certifique-se de utilizar **sets** quando especificado para garantir a unicidade dos elementos.

---

**Boa sorte\!** Lembre-se de seguir as instruções cuidadosamente e de aplicar as competências adquiridas ao longo do curso.

---

---

## **Entrega**

Você deve entregar **todos os arquivos** utilizados e gerados na solução, incluindo códigos-fonte, arquivos de dados e outros recursos, compactados em um arquivo zip nomeado conforme a regra:

nome\_sobrenome\_DR4\_AT.ZIP

Além disso, realize o **commit** e **push** no repositório criado para este fim.
