
from django.contrib import admin
from django.urls import path, include
from perfis import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('perfis.urls')),
    path('', include('usuarios.urls'))
]
