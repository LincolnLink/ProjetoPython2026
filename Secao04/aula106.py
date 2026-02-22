
""""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parêmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retirnam None (nada). 
"""
# def Print():
#     print('Olá, Mundo!')
#     print('Bem-vindo ao curso de Python!')

# Print() # Chamando a função Print
# Print()


def imprimir_mensagem(a,b):
    mensagem = f"{a} {b}"
    print(mensagem)

imprimir_mensagem('Olá,', 'Mundo!')







