# Instalando projeto Django.

# 1) criando pasta que fica o projeto e o env que é o ambiente virtual.
# 2) criando ambiente virtual dentro da pasta do projeto.
# 3) com o comando: python -m venv venv.
# 4) ativa o ambiente virtual.
# 5) com o comando: venv/Scripts/activate.
# 6) caso de erro ativa o powershell.
# 7) com o comando: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser 
# 8) instala o djando.
# 9) com o comando: pip install django.
# 10) ele pede para atualizar.
# 11) com o comando: pip install pip --upgrade
# 12) ou esse comando: venv\Scripts\python.exe -m pip install pip --upgrade
# 13) comando que mostra o que esta instalado:
# 14) com o comando: pip freeze

# 15) Cria o projeto:
# 16) com o comando: django-admin startproject project .
# 17) tem que ter o ponto no final do comando para não gerar outra pasta.

# 18) startando o projeto
# 19) com o comando: python manage.py runserver
# 20) o link do servidor: http://127.0.0.1:8000/