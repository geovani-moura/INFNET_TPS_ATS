#10. Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) para criar uma história curiosa.
import random

personagens = ["João", "Maria", "Pedro", "Ana"]
acoes = ["caiu", "foi roubado", "achou dinheiro", "está de ferias"]
locais = ["em casa", "no banco", "no hotel", "na farmácia"]
print(f"{random.choice(personagens)} {random.choice(acoes)} {random.choice(locais)}")
