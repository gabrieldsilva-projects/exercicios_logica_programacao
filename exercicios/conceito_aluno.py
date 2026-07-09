nota_aluno = float(input("Informe sua nota (0 a 10): "))

if (nota_aluno >= 9 and nota_aluno <= 10):
    print("Conceito: A")
elif (nota_aluno >= 7 and nota_aluno <= 8.9):
    print("Conceito: B")
elif (nota_aluno >= 5 and nota_aluno <= 6.9):
    print("Conceito: C")
elif (nota_aluno < 5):
    print("Conceito: D")
else:
    print("Conceito incorreto!")