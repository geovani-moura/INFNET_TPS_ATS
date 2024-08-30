#4. Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão) e dois números, e então execute a operação escolhida com os números.
operacao = int(input("Escolha uma operação: \n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \nResposta:"))
n1 = int(input("Escreva o 1ª número:"))
n2 = int(input("Escreva o 2ª número:"))

if operacao == 1:
  print(f"A soma é: {n1+n2}")
elif operacao == 2:
  print(f"A subtração é: {n1-n2}")
elif operacao == 3:
  print(f"A Multiplicação é: {n1*n2}")
elif operacao == 4:
  print(f"A Divisão é: {n1/n2}")
else:  
  print("Operação não encontrada")
