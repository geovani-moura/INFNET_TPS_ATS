usuarios = [
    ["Maria da Silva", 45, "São Paulo", "SP"],
    ["José Santos", 52, "São Paulo", "SP"],
    ["Ana Oliveira", 28, "São Paulo", "SP"],
    ["João Pereira", 33, "São Paulo", "SP"],
    ["Carlos Sousa", 40, "São Paulo", "SP"]
]


perfis = []
for usuario in usuarios:
    perfil = {
        "nome": usuario[0],
        "idade": usuario[1],
        "localização": (usuario[2], usuario[3])
    }
    perfis.append(perfil)
print(perfis)


perfis_validos = []
for perfil in perfis:
    if perfil.get('nome') and perfil['localização'][0]:
        perfis_validos.append(perfil)
print(perfis_validos)


#Lista: É uma sequência de itens em ordem. Você pode adicionar, remover e alterar itens facilmente. Cada item na lista tem uma posição (índice). No INFwebNET, uma lista pode guardar vários usuários, onde cada usuário é uma lista de informações pessoais.
usuarios = [
    ["Maria", 45, "São Paulo", "SP"],
    ["José", 52, "São Paulo", "SP"]
]

#Dicionário: Guarda dados como pares "chave-valor". Cada chave é única e permite acessar o valor ligado a ela. No INFwebNET, podemos usar dicionários para guardar informações detalhadas de cada usuário, como nome, idade e localização.
usuario = {
    "nome": "Maria",
    "idade": 45,
    "localização": ("São Paulo", "SP")
}

#Tupla: É parecida com uma lista, mas seus itens não podem ser alterados. Útil para dados fixos que não vão mudar. No INFwebNET, uma tupla pode representar a localização de um usuário (cidade e estado), pois essa informação geralmente não muda.
localizacao = ("São Paulo", "SP")




































