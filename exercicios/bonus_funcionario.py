salario = float(input("Informe seu salário: R$"))

if (salario < 2000):
    bonus_maior = salario * 0.15
    salario_novo = bonus_maior + salario
    print(f"Salário original: {salario} \nValor bônus: {bonus_maior:.2f} \nSalário final: {salario_novo:.2f}")
else:
    bonus_menor = salario * 0.08
    salario_novo = bonus_menor + salario
    print(f"Salário original: R${salario} \nValor bônus: R${bonus_menor:.2f} \nSalário final: R${salario_novo:.2f}")
