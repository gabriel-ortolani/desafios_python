import random

def soma():
    return jogador1 + jogador2


jogador1 = int(input("Digite um número de 1 a 10: "))
jogador2 = random.randint(0, 10)
escolha = input("Digite se você sera par ou ímpar: ")

resposta = soma()
print("__________")
print("Seu número:", jogador1)
print("__________")
print("Número do adversario:", jogador2)
print("__________")
print("Resultado:")

if(escolha == "par" and resposta % 2 == 0):
    print("Você ganhou")   
elif(escolha == "ímpar" and resposta % 2 != 0):
    print("Você ganhou")
else:
    print("Você perdeu")