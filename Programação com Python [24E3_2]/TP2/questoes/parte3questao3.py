print(
    """
    Parte 3 | Questão 3: 
    Escreva um programa que utilize um laço while para solicitar ao usuário que informe a hora do registro da temperatura (em um número inteiro) 
    seguido do valor da temperatura registrada. Seu programa deverá conter função de validação da entrada do usuário para garantir que a hora descrita esteja 
    entre 0h e 23h e que a temperatura informada esteja entre -15ºC e 60ºC. E em seguida armazene as informações em duas listas, uma com os horários e outra 
    com as temperaturas.
    """
)
print()


def validar_hora(hora):
    return 0 <= hora <= 23


def validar_temperatura(temperatura):
    return -15 <= temperatura <= 60


horarios = []
temperaturas = []

while True:
    hora_str = input("Digite a hora do registro (ou 'sair' para finalizar): ")
    if hora_str.lower() == "sair":
        break

    try:
        hora = int(hora_str)
        if not validar_hora(hora):
            print("Hora inválida.")
            continue

        temperatura_str = input("Digite o valor da temperatura registrada: ")
        temperatura = float(temperatura_str)
        if not validar_temperatura(temperatura):
            print("Temperatura inválida.")
            continue

        horarios.append(hora)
        temperaturas.append(temperatura)

    except ValueError:
        print("Entrada inválida.")

for hora, temperatura in zip(horarios, temperaturas):
    print(f"Hora: {hora}h, Temperatura: {temperatura:.2f}°C")
