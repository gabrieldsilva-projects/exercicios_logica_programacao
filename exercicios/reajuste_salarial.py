salario = float(input("Informe seu salário: "))

if (salario <= 1500):
    ajuste = 15
    ajuste_salarial = salario * 0.15
    salario_novo = salario + ajuste_salarial
    print(f"Salário antigo: R${salario} \nPercentual aplicado: {ajuste}%  \nNovo salário: R${salario_novo:.2f}")

elif(salario <= 3000):
    ajuste = 10
    ajuste_salarial = salario * 0.10
    salario_novo = salario + ajuste_salarial
    print(f"Salário antigo: R${salario} \nPercentual aplicado: {ajuste}%  \nNovo salário: R${salario_novo:.2f}")

elif (salario  <= 5000):
    ajuste = 7
    ajuste_salarial = salario * 0.07
    salario_novo = salario + ajuste_salarial
    print(f"Salário antigo: R${salario} \nPercentual aplicado: {ajuste}%  \nNovo salário: R${salario_novo:.2f}")

elif (salario > 5000):
    ajuste = 5
    ajuste_salarial = salario * 0.5
    salario_novo = salario + ajuste_salarial
    print(f"Salário antigo: R${salario} \nPercentual aplicado: {ajuste}%  \nNovo salário: R${salario_novo:.2f}")

else:
    print("Erro no calculo")