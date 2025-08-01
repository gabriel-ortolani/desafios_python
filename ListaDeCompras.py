print("Lista de compras")
print("_________")
print("Digite 1 para adicionar um item")
print("Digite 2 para remover um item")
print("Digite 3 para ver a lista")
print("Digite 0 para sair")
print("_________")

lista_compras = []

while True:
    numero = int(input("Digite o numero do que desejá fazer: "))
    if(numero == 1):
        item = input("Digite o item que deseja adicionar: ")
        lista_compras.append(item)
    elif(numero == 2):
        item = input("Digite o item que deseja adicionar: ")
        lista_compras.remove(item)
    elif(numero == 3):
        print(lista_compras)
    elif(numero == 0):
        break
    else:
        print("Número não aceito tente um dos abaixo!")
        print("_________")
        print("Digite 1 para adicionar um item")
        print("Digite 2 para remover um item")
        print("Digite 3 para ver a lista")
        print("Digite 0 para sair")
        print("_________")