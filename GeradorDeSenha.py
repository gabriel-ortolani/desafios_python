import random

print("Gerador de Senha")
numero = int(input("Digite o número de caracteres desejados: "))

caracteres = 'abcdefghijkmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ1234567890!#$%&'

def tem_maiuscula(s):
    return any(c.isupper() for c in s)

def tem_minuscula(s):
    return any(c.islower() for c in s)

def tem_especial(s):
    especiais = '!#$%&'
    return any(c in especiais for c in s)

while True:
    senha = random.choices(caracteres, k=numero)
    if tem_maiuscula(senha) and tem_minuscula(senha) and tem_especial(senha):
        break

senha_str = ''.join(senha)
print("Senha gerada:", senha_str)
