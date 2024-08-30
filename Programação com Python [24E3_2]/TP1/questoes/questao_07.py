#7. Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).
print("Vamos calcular o seu IMC")
altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}")  
if imc < 18.5:
  print("Abaixo do peso")
elif imc > 18.5 and imc < 24.9:
  print("Peso Normal")
elif imc > 25 and imc < 29.9:
  print("Sobrepeso")
elif imc > 30 and imc < 34.9:
  print("Obesidade classe I")
elif imc > 35 and imc < 39.9:
  print("Obesidade classe II")
elif imc > 40 :
  print("Obesidade classe III")