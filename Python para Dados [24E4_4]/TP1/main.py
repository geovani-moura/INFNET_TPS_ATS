usuarios = [
    ["Maria da Silva", 45, "S�o Paulo", "SP"],
    ["Jos� Santos", 52, "S�o Paulo", "SP"],
    ["Ana Oliveira", 28, "S�o Paulo", "SP"],
    ["Jo�o Pereira", 33, "S�o Paulo", "SP"],
    ["Carlos Sousa", 40, "S�o Paulo", "SP"]
]


perfis = []
for usuario in usuarios:
    perfil = {
        "nome": usuario[0],
        "idade": usuario[1],
        "localiza��o": (usuario[2], usuario[3])
    }
    perfis.append(perfil)
print(perfis)


perfis_validos = []
for perfil in perfis:
    if perfil.get('nome') and perfil['localiza��o'][0]:
        perfis_validos.append(perfil)
print(perfis_validos)


#Lista: � uma sequ�ncia de itens em ordem. Voc� pode adicionar, remover e alterar itens facilmente. Cada item na lista tem uma posi��o (�ndice). No INFwebNET, uma lista pode guardar v�rios usu�rios, onde cada usu�rio � uma lista de informa��es pessoais.
usuarios = [
    ["Maria", 45, "S�o Paulo", "SP"],
    ["Jos�", 52, "S�o Paulo", "SP"]
]

#Dicion�rio: Guarda dados como pares "chave-valor". Cada chave � �nica e permite acessar o valor ligado a ela. No INFwebNET, podemos usar dicion�rios para guardar informa��es detalhadas de cada usu�rio, como nome, idade e localiza��o.
usuario = {
    "nome": "Maria",
    "idade": 45,
    "localiza��o": ("S�o Paulo", "SP")
}

#Tupla: � parecida com uma lista, mas seus itens n�o podem ser alterados. �til para dados fixos que n�o v�o mudar. No INFwebNET, uma tupla pode representar a localiza��o de um usu�rio (cidade e estado), pois essa informa��o geralmente n�o muda.
localizacao = ("S�o Paulo", "SP")




































