peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / altura
if (imc < 18.5):
    print(f"IMC: {imc:.2f} \nSituação: Abaixo do peso!")
elif (imc >= 18.5 and imc >= 24.9):
    print(f"IMC: {imc:.2f} \nSituação: Peso normal!")
elif (imc >= 25 and imc <= 29.9):
    print(f"IMC: {imc:.2f} \nSituação: Sobrepeso!")
elif (imc > 30):
    print(f"IMC: {imc:.2f} \nSituação: Obesidade")
else:
    print("Informações incorretas!")
