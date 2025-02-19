"""
URL configuration for bitacora_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),

    path('usuarios/', include('appweb.urls')),
    path('computadores/', include('appweb.urls')),
    path('activos/', include('appweb.urls')),
    path('accioncrud/', include('appweb.urls')),
    path('asignacion/', include('appweb.urls')),
    path('caracthardware/', include('appweb.urls')),
    path('caractsoftware/', include('appweb.urls')),
    path('dispositivo/', include('appweb.urls')),
    path('estadoactivo/', include('appweb.urls')),
    path('licencia/', include('appweb.urls')),
    path('mantencionactivo/', include('appweb.urls')),
    path('procesoservidor/', include('appweb.urls')),
    path('tiposervidor/', include('appweb.urls')),
    path('servidores/', include('appweb.urls')),
    path('registroaccion/', include('appweb.urls')),
    path('tipousuario/', include('appweb.urls')),
    path('sistemaoperativo/', include('appweb.urls'))
]
