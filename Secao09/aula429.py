from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from home import views #importa as views do app home
from blog import views as blog_views #importa as views do app blog, usando um alias para evitar conflito de nomes


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('blog/', blog_views.blog, name='blog'), # link para a view blog do app blog
]