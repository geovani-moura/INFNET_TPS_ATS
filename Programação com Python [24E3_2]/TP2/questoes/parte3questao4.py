print(
    """
    Parte 3 | Questão 4: 
    Quando o usuário digitar ‘Fim’ uma função (pode utilizar mais de uma função) deverá receber as duas listas do item anterior como 
    argumentos, calcular a média das temperaturas, ponderada pelo intervalo de tempo entre as medidas e imprimir se a média está dentro 
    do intervalo de segurança (20°C a 30°C) e exibir o horário e o valor da temperatura mais baixa e mais alta do dia.
    """
)
print()


def calcular_media_ponderada(horarios, temperaturas):
    if not horarios or not temperaturas or len(horarios) != len(temperaturas):
        return None

    total_tempo = 0
    total_temperatura_ponderada = 0

    for i in range(len(horarios) - 1):
        intervalo = horarios[i + 1] - horarios[i]
        total_tempo += intervalo
        total_temperatura_ponderada += temperaturas[i] * intervalo

    if total_tempo == 0:
        return None

    return total_temperatura_ponderada / total_tempo


def verificar_intervalo_segurança(media_ponderada):
    return 20 <= media_ponderada <= 30


def exibir_dados_final(horarios, temperaturas):
    if not horarios or not temperaturas:
        print("Nenhum dado disponível.")
        return

    media_ponderada = calcular_media_ponderada(horarios, temperaturas)

    if media_ponderada is not None:
        if verificar_intervalo_segurança(media_ponderada):
            print(
                f"Média ponderada das temperaturas: {media_ponderada:.2f}°C está dentro do intervalo de segurança."
            )
        else:
            print(
                f"Média ponderada das temperaturas: {media_ponderada:.2f}°C está fora do intervalo de segurança."
            )
    else:
        print("Não foi possível calcular a média ponderada.")

    temp_min = min(temperaturas)
    temp_max = max(temperaturas)
    hora_min = horarios[temperaturas.index(temp_min)]
    hora_max = horarios[temperaturas.index(temp_max)]

    print(f"Temperatura mais baixa: {temp_min:.2f}°C às {hora_min}h")
    print(f"Temperatura mais alta: {temp_max:.2f}°C às {hora_max}h")


horarios = []
temperaturas = []

while True:
    hora_str = input("Digite a hora do registro (ou 'Fim' para finalizar): ")
    if hora_str.lower() == "fim":
        break

    try:
        hora = int(hora_str)
        if hora < 0 or hora > 23:
            print("Hora inválida.")
            continue

        temperatura_str = input("Digite o valor da temperatura registrada: ")
        temperatura = float(temperatura_str)
        if temperatura < -15 or temperatura > 60:
            print("Temperatura inválida.")
            continue

        horarios.append(hora)
        temperaturas.append(temperatura)

    except ValueError:
        print("Entrada inválida.")

exibir_dados_final(horarios, temperaturas)
