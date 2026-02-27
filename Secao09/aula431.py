# explicação.

#rederizando template html

# se usa o render para renderizar o template html, e o HttpResponse para retornar uma resposta simples, como texto.

from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def home(request):
    # return HttpResponse('HOMEZAO')
    return render(request, 'home.html')


# no settings , bota o nome do seu app no array INSTALLED_APPS!

