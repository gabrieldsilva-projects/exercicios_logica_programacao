preco_prod = float(input("Informe o valor do produto: "))

if(preco_prod > 100):
    desconto = preco_prod * 0.10
    print(desconto)
else:
    print(preco_prod)