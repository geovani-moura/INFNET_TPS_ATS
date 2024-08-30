#14. Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção.
opcoes = ["Lula", "Bolsonaro", "Ciro Gomes"]
votos = [0, 0, 0]
quantidadeVotos = int(input("Quantos votos você quer dar?"))
for i in range(quantidadeVotos):
  print(f"Voto N.ª[{i+1}], Em quem você irá votar?")
  for x in range(len(opcoes)):
    print(f"N.ª[{x+1}] - {opcoes[x]}")
  voto = int(input("N.ª:"))
  votos[voto-1] += 1

print("\n")
for i in range(len(votos)):
  print(f"Votos para {opcoes[i]}: {votos[i]}")