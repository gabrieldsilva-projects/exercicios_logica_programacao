preco = float(input("Informe o valor da compra: "))
print("Formas de pagamento: \n1 - Pix (15% desconto) \n2 - Dinheiro (10%) \n3 - Cartão de débito (5%) \n4 - Cartão de crédito (sem desconto)")
forma_pag = input("Informe a forma de pagamento: ")

pix = 0.15
money = 0.10
card_deb = 0.05

if forma_pag == "Pix" or "pix":
    desc = preco * pix
    valor_final = preco - desc
    print(f"A forma de pagamento é Pix com desconto de 15% e o valor final a ser pago é de R${valor_final:.2f}")
elif forma_pag == "Dinheiro" or "dinheiro":
    desc = preco * money
    valor_final = preco - desc
    print(f"A forma de pagamento é Dinheiro com desconto de 10%e o valor final a ser pago é de R${valor_final:.2f}")
elif forma_pag == "Cartão de débito" or "cartão de débito":
    desc = preco * card_deb
    valor_final = preco - desc
    print(f"A forma de pagamento é Cartão de Débito com desconto de 5% e o valor final a ser pago é de R${valor_final:.2f}")
elif forma_pag == "Cartão de crédito" or "cartão de crédito":
    print(f"A forma de pagamento é Cartão de crédito e não possui desconto e o valor final a ser pago é de R${preco:.2f}")
else:
    print("Forma de pagamento inválida")

