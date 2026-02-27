# from django.shortcuts import render
# from django.http import HttpResponse

from django.shortcuts import render # type: ignore

def exemplo(request):
    return render(request, 'blog/exemplo.html')

# Create your views here.
def blog(request): #view
    print('blog7')  #pode fazer qualquer coisa aqui, como acessar banco de dados, etc
    return render(request, 'blog/home.html') #resposta para o navegador, pode ser um html, json, etc
