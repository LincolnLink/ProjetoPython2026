valor01 = input('Digite um valor: ')
valor02 = input('Digite outro valor: ')

if valor01 > valor02:
    print(f'O valor {valor01} é maior que o valor {valor02}')
elif valor02 > valor01:
    print(f'O valor {valor02} é maior que o valor {valor01}')
else:
    print(f'Os valores {valor01} e {valor02} são iguais')