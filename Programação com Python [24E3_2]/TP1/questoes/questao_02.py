#2. Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, convertendo horas e minutos de volta para minutos totais.
minutos = int(input("Digite os minutos: "))

horas_convertida = minutos // 60
minutos_restantes_convertida = minutos % 60
print(f"{minutos} minutos equivalente a {horas_convertida} horas e {minutos_restantes_convertida} minutos")

minutos_convertido = horas_convertida * 60 + minutos_restantes_convertida
print(f"{horas_convertida} horas e {minutos_restantes_convertida} minutos reconvertidos em {minutos_convertido} minutos")