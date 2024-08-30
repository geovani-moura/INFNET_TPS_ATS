#6. Escreva um programa onde o usuário deve adivinhar um número secreto. O programa deve dizer se o palpite está correto, muito alto ou muito baixo.
numeroSecreto = 7
palpite = int(input("Adivinhe o número secreto:"))
if palpite == numeroSecreto:
  print("Parabéns, você acertou o número secreto!")
elif palpite > numeroSecreto:
  print("O número secreto é menor que o seu palpite.")
else:
  print("O número secreto é maior que o seu palpite.")
