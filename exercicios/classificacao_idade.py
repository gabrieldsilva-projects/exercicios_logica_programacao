age = int(input("Informe sua idade: "))

if age >= 0 and age <= 12:
    print("Categoria: Criança")
elif age >= 13 and age <= 17:
    print("Categoria: Adolescente")
elif age >= 18 and age <= 59:
    print("Categoria: Adulto")
elif age > 60: 
    print("Categoria: idoso")
else: 
    print("Erro!")