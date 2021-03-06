"""cv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from mycv import views as mycvView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', views.hola),
    path('cv/', mycvView.mySimpleFunction, name="cv"),
    path('proyectosTecnologia/', mycvView.muestraDemosPorTecnologia, name="tecnologyProjects"),
    path('SendMessage/', mycvView.SendMessage, name='SendMessage'),
    path("RegisterMessage/", mycvView.RegisterMessage, name="RegisterMessage"),
    path("Login/", mycvView.SingIn, name="Login"),
    path("Singup/", mycvView.SingUp, name="Singup"),
    path("Logout/",mycvView.Logout, name="Logout")
]
