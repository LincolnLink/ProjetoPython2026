# ProjetoPython2026

Iniciando um curso de python

# Comandos basicos de configuracao python

- Get-ExecutionPolicy:

Verifica se pode executar comandos no powershell, se esta restrito ou não.

- py -m venv venv

Comando que cria ambiente virtual do python

- .\venv\Scripts\activate

Ativa o ambiente virtual do python.

- Set-ExecutionPolicy AllSigned -Force

Comando que deixa com restrição de comandos python no powerShell.(Só executa no powershell fora do vsCode)

- Set-ExecutionPolicy Unrestricted -Force

Comando que deixa Unrestricted (Só executa no powershell fora do vsCode)

# Comandos basicos configuracao VScode

abra o settings , clica no icone de arquivo com seta, e digita no jsom:

"window.zoomLevel": 2 (define valor de zoom)

"explorer.compactFolders": false, (define se a pasta vai ficar compactada.)

# plugin para Python:

- Python: é um plugin que torna o VScode uma IDE de python.

### Aula18

- fala sobre docstring
  print e comentario

### Aula19
### Aula20
- print

### Aula21

- print, type, int, str, float

### Aula22

- print, bool, type

### Aula23

- print, type e conversão str para int

### Aula24
### Aula25

- variaveis

### Aula27

- operadores

### Aula28

- variaveis

### Aula29
### Aula30

- calculos e IMC

### Aula31
### Aula32

- parametros, formatação.

### Aula34

- format e input

### Aula 35
### Aula 36
### Aula 37
### Aula 38

Operadores de comparação

if, elif, else

### Aula 38
### Aula 39
### Aula 40

sinal de maior e menor

### Aula 41

and, todas precisa ser verdadeira

### Aula 42

or, quanlquer condição verdadeira avalia.

### Aula 43

not

### Aula 44

in , not in

### Aula 45

interpolação.

### Aula 46

posicionamento.

### Aula 47
### Aula 48
### Aula 49

fatiamento, metodo len().
exercicio.
resultado do exercicio.

### Aula 50

Introdução ao try/except.

### Aula 51
### Aula 52

Boas praticas.
exercicio.

### Aula 53

id das variaveis em memoria.

### Aula 54

Flag, none, is, is not.
sempre criar a variavel fora do bloco de codigo.

### Aula 55
### Aula 56
### Aula 57
### Aula 58

exercicio.
resultado do exercicio1.
resultado do exercicio2.
resultado do exercicio3.

### Aula 59

tipos imutaveis, só criando outra varivel com outro valor.

### Aula 60
### Aula 61

while/break, repetição.
contador

### Aula 62

usando operadores no contador.

### Aula 63

while/continue, cuidado quando for usar o continue, para não da loop infinito.

### Aula 64

while dentro de while.

### Aula 65
### Aula 66

exercicio
solução do exercicio.

### Aula 67
### Aula 68
### Aula 69

exercicio explicado.

### Aula 70

while/else, executa algo depois que o while termina.

### Aula 71
### Aula 72

exercicio
solução do exercicio.

### Aula 73

For


### Aula 74

### Aula 75
### Aula 76
### Aula 77

### Aula 78
### Aula 79
### Aula 80

### Aula 81
### Aula 82
### Aula 83


# Seção 04: Python Intermediário - Funções, Dicionários, Módulos, Programação...

### Aula 105

explicação

### Aula 106

inicia a função com (def), parametros.

### Aula 107

argumento nomeado, e argumento posicional.

### Aula 108

parametro com valor definido

### Aula 109
### Aula 110

escopo de função local e escopo global.
global, uma palavra que faz referencia a variavel de fora, mas não é bom usar,
melhor passar por parametro.

Call stack, uma parte do debugger.

### Aula 111

return, define o que vai ser retornado na função.

### Aula 112
### Aula 113
*args (empacotamento e desempacotamento)

### Aula 114

exercicio, solução do exercicio.

### Aula 115
### Aula 116

Higher Order Functions, Funções de primeira classe
é passando para uma função, uma outra função por parametro,
e o segundo parametro é um *arg uma coleção de dados.

### Aula 117
### Aula 118

Closure e funções que retornam outras funções


# Seção 05: Introdução á programação orientada a objetos em python - POO

### Aula 199

recomendação de livro.

### Aula 200
### Aula 201

class, atributos, metodos.
self, criando o metodo init, que constroi os objetos.

# Aula 202

Métodos em instâncias de classes Python

# Aula 203

pode usar a classe para chamar o metodo, mas tem que passar
uma instancia como parametro.

# Aula 204

metodo que chama outro metodo.

# Aula 205

Multiplos métodos e varias chamadas dos metodos.

# Aula 206

Atributos de classe

# Aula 207

"__dict__" ele mostra o objeto e inclui propriedade e valor.
"vars" exibe o conteudo do objeto.

# Aula 208
# Aula 209 (VDPS)

importar json, importar metodo de outra classe
instanciar objeto de outra classe.

# Aula 210

dicas

# Aula 211

@classmethod
Um metodo que cria instancia da classe

# Aula 212

metodo estatico, parece que não serve pra nada.

# Aula 213

resumo do metodo.

# Aula 214

@property
um metodo que quando chamado é igual um atributo.

# Seção 9: Django no Python - Básico

# Aula 421

explicação

# Aula 422

Instalando projeto Django.

1) criando pasta que fica o projeto e o env que é o ambiente virtual.
2) criando ambiente virtual dentro da pasta do projeto.
3) com o comando: python -m venv venv.
4) ativa o ambiente virtual.
5) com o comando: venv/Scripts/activate.
6) caso de erro ativa o powershell.
7) com o comando: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser 
8) instala o djando.
9) com o comando: pip install django.
10) ele pede para atualizar.
11) com o comando: pip install pip --upgrade
12) ou esse comando: venv\Scripts\python.exe -m pip install pip --upgrade
13) comando que mostra o que esta instalado:
14) com o comando: pip freeze

15) Cria o projeto:
16) com o comando: django-admin startproject project .
17) tem que ter o ponto no final do comando para não gerar outra pasta.

18) startando o projeto
19) com o comando: python manage.py runserver
20) o link do servidor: http://127.0.0.1:8000/

# Aula 423

startando o projeto
com o comando: python manage.py runserver
o link do servidor: http://127.0.0.1:8000/

# Aula 424

apresentando o django

# Aula 425

1) Comando que mostra opções de comando
com o comando: django-admin help

2) O django-admin ele gerencia o django.

3) só vai ser usando o django-amin para criar projetos.

4) para iniciar usa o: python manage.py runserver.

5) O arquivo manage.py ele inicia o servidor.

6) pode configurar comando nele para personizar quando inicia.

7) ele cria uma variavel de ambiente.

8) e pega dados do arquivo settings.py do proejto.

9) .parent ele volta para pasta pai.

10) exemplo: BASE_DIR = Path(__file__).resolve().parent.parent

11) no settings se configura os APPS

12) no settings se configura os MIDDLEWARE

13) no projeto tem o arquivo que configura as rotas

14) passando a rota e urls

15) no settings se configura os TEMPLATES

16) no settings se configura os DATABASES

17) é usado sqlite.

18) no settings se configura os AUTH_PASSWORD_VALIDATORS

19) no settings se configura os idioma e hora.

20) no settings se configura arquivos staticos.

21) no settings se configura

22) no settings se configura

# Aula 426

Criando um path('blog/', blog, name='blog'),

# Aula 427

MVC - Model, View, Controler
MVT - Model, View, Template

# Aula 428

1) O django trabalhacom o settings, usando APPS
2) criando App
3) com o comando: python manage.py startapp 'nomeDoApp'

4) arquivos dentro do app
5) __init__.py: configura algo que inicia no app
6) admin.py: cria model para o admin, acho que e crud
7) apps.py: configuração do app
8) models.py: model do app
9) test.py: teste.
10) views.py: layout

11) existe 2 tipos de view, de função e de classe


# Aula 429

faz a conexao do view do app com o projeto principal.

# Aula 430
# Aula 431