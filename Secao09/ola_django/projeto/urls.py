"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def blog(request): #view
    print('blog7')  #pode fazer qualquer coisa aqui, como acessar banco de dados, etc
    return HttpResponse('Blog77') #resposta para o navegador, pode ser um html, json, etc

def home(request):
    return HttpResponse('Home')

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('blog/', blog, name='blog'),
]
