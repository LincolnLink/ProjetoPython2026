"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

"""
#definição da função
def somaE(x, y):
    print(x + y)

#chamada da função
somaE(10, 20) # Argumentos não nomeados


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(1, y=2, z=5) # Argumento nomeado, o valor do argumento é passado com o nome do parâmetro

print(1, 2, 3, sep='-')