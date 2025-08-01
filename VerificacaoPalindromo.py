print("Digite uma palavra para descobrir se ela é um palídromo")
print("Caso queira sair do programa basta escrever 'exit'")
print("________")
while True:
    texto = input("Digite a palavra: ")

    if(texto == texto[::-1]):
        print(texto)
        print(texto[::-1])
        print("Sua palavra é um palídromo")
    elif(texto == "exit"):
        break
    else:
        print(texto)
        print(texto[::-1])
        print("Sua palavra não é um palídromo")