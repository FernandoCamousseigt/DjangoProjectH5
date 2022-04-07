"""onlyflans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from web.views import indice, acerca, bienvenido, contacto, exito, sin_azucar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indice, name="indice"),
    path('acerca', acerca, name="acerca"),
    path('bienvenido', bienvenido, name="bienvenido"),
    path('contacto', contacto, name="contacto"),
    path('exito', exito, name="exito"),
    path('sin_azucar', sin_azucar, name="zero_azucar"),
    path('accounts/', include('django.contrib.auth.urls')),
]
