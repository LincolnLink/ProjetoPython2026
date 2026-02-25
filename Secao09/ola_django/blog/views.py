# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request): #view
    print('blog7')  #pode fazer qualquer coisa aqui, como acessar banco de dados, etc
    return HttpResponse('Template do Blog')
