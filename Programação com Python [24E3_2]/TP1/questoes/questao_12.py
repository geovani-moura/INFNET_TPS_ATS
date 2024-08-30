#12. Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais).
palavra = input("Digite uma palavra:")
if len(palavra) < 5:
  print("Palavra curta")
else:
  print("Palavra longa")