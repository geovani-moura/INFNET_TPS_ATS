print(
    """
    Parte 3 | Questão 2: 
    Cálculo de Consumo de Combustível
    Escreva um programa que ajude um motorista a calcular o consumo de combustível de seu veículo. O programa deve solicitar ao usuário que insira a 
    distância percorrida e a quantidade de combustível consumido em várias viagens. Essas informações devem ser armazenadas em uma lista. 
    Em seguida, crie uma função que percorra essa lista e calcule o consumo médio de combustível (km/l) para cada viagem e para o total de todas as viagens.

    Monitoramento de Temperatura

    Você foi contratado para desenvolver um software que monitora as temperaturas registradas por sensores em uma fábrica ao longo do dia. 
    """
)
print()


def calcular_consumo(lista_viagens):
    consumos = []
    total_distancia = 0
    total_combustivel = 0

    for distancia, combustivel in lista_viagens:
        consumo = distancia / combustivel
        consumos.append(consumo)
        total_distancia += distancia
        total_combustivel += combustivel

    consumo_medio_total = (
        total_distancia / total_combustivel if total_combustivel > 0 else 0
    )

    return consumos, consumo_medio_total


viagens = []
while True:
    distancia = float(input("Digite a distância percorrida (ou 0 para sair): "))
    if distancia == 0:
        break
    combustivel = float(input("Digite a quantidade de combustível consumido: "))
    viagens.append((distancia, combustivel))

consumos, consumo_medio_total = calcular_consumo(viagens)

for i, consumo in enumerate(consumos, start=1):
    print(f"Consumo da viagem {i}: {consumo:.2f} km/l")

print(f"Consumo médio total: {consumo_medio_total:.2f} km/l")
