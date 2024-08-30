#1. Crie um programa que peça ao usuário para inserir dois números e, em seguida, calcule e exiba a soma, subtração, multiplicação, divisão e divisão inteira desses números.
n1 = float(input("Escreva o Primeiro número:"))
n2 = float(input("Escreva o Segundo número:"))

print(f"\nSoma: {n1 + n2}")
print(f"\nSubtração: {n1 - n2}")
print(f"\nmultiplicação: {n1 * n2}")
print(f"\nDivisão: {n1 / n2}")
print(f"\nDivisão: {int(n1 / n2)}")
