valor1 = input("digite um numero inteiro: ")

try :
    valor1 = int(valor1)
    if valor1 % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
except ValueError:
    print("Isso não é um número inteiro.")

horario = input("Qual é o horário? ")

try:
    horario = int(horario)
    if 0 <= horario <= 11:
        print("Bom dia!")
    elif 12 <= horario <= 17:
        print("Boa tarde!")
    elif 18 <= horario <= 23:
        print("Boa noite!")
    else:
        print("Horário inválido. Por favor, insira um número entre 0 e 23.")
except ValueError:
    print("Isso não é um número inteiro.")

nome = input("Digite seu nome: ")
if len(nome) <= 4:
    print("Seu nome é curto.")
elif 5 <= len(nome) <= 6:
    print("Seu nome é médio.")
else:
    print("Seu nome é longo.")