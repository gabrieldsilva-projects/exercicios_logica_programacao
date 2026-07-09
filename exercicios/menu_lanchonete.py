print("Menu: \n1 - Hambúrguer \n2 - Pizza \n3 - Cachorro-quente \n4 - Refrigerante")
pedido = int(input("Faça seu pedido (1 a 4): "))

if pedido == 1:
    print("1 - Hambúrguer")
elif pedido == 2: 
    print("2 - Pizza")
elif pedido == 3:
    print("3 - Cachorro-quente")
elif pedido == 4:
    print("4 - Refigerante")
else:
    print("Opção inválida.")