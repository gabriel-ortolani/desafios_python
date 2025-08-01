import random

numero = random.randint(1, 20)

while True:
    chute = int(input("Insira um numero de 1 a 20: "))
    if(chute == numero):
        print("Você acertou!")
        break
    elif(chute >= numero):
        print("O numero é menor")
    else:
        print("O numero é maior")
    print("_________")