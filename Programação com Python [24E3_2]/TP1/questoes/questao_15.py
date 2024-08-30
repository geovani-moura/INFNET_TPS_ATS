#15. Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) e conduza a diferentes resultados com base nessas escolhas.
personagens = ["João", "Maria", "Pedro", "Ana"]
acoes = ["caiu", "foi roubado", "achou dinheiro", "está de ferias"]
locais = ["em casa", "no banco", "no hotel", "na farmácia"]
historia = [0, 0, 0]
print("Vamos começar uma pequena história")

print("Lista de Personagens:?")
for i in range(len(personagens)):
  print(f"N.ª[{i+1}] - {personagens[i]}")

historia[0] = int(input("Escolha o Personagem?"))-1

print("Qual a ação do seu personagem?")
for i in range(len(acoes)):
  print(f"N.ª[{i+1}] - {acoes[i]}")

historia[1] = int(input("Escolha a ação do seu Personagem?"))-1

print("Qual o local do seu personagem?:")
for i in range(len(locais)):
  print(f"N.ª[{i+1}] - {locais[i]}")

historia[2] = int(input("Escolha o local do seu seu Personagem?"))-1

print(f"{personagens[historia[0]]} {acoes[historia[1]]} {locais[historia[2]]}")