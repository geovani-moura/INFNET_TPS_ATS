#13. Desenvolva um programa que verifique se uma palavra ou frase inserida pelo usuário é um palíndromo (lê-se igual de trás para frente).
palavra = input("Digite uma palavra:")
if(palavra == palavra[::-1]):
  print("É um palíndromo")
else:
  print("Não é um palíndromo")