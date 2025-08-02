def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

lista = []

print("Lista de números primos")
print("_______")
print("1 - adicionar numero")
print("2 - ver lista(A lista exibirá apenas os números primos)")
print("3 - para sair")
print("_______")

while True:
    opcao = int(input("Digite o Número do que desejá fazer: "))
    if opcao == 1:
        numero = int(input("Digite o número a ser adicionado: "))
        lista.append(numero)
    elif opcao == 2:
        primos = [n for n in lista if eh_primo(n)]
        print(primos)
    elif opcao == 3:
        break
    else:
        print("Opção não existente")
    print("_______")
    print("1 - adicionar numero")
    print("2 - ver lista(A lista exibirá apenas os números primos)")
    print("3 - para sair")
    print("_______")