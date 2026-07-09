num1 = float(input("Informe o primeiro número: "))
operacao = input("Informe a operação (+, -, * ou /): ")
num2 = float(input("Informe o segundo número: "))

if (operacao == "+"):
    print(num1 + num2)

elif (operacao == "-"):
    print(num1 - num2)

elif (operacao == "*"):
    print(num1 * num2)

elif (operacao == "/"):
    print(num1 / num2)
else:
    print("Operação invalida!")