#9. Desenvolva um programa que aplique descontos diferentes com base no valor da compra: desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, etc.
valorCompra = float(input("Digite o valor da compra:"))
if valorCompra > 100 and valorCompra <= 200:
  print(
      f"Valor da compra R${valorCompra} desconto de 10% ficando {valorCompra * 0.9}"
  )
elif valorCompra > 200:
  print(
      f"Valor da compra R${valorCompra} desconto de 15% ficando {valorCompra * 0.85}"
  )
else:
  print(f"Valor da compra R${valorCompra}")
