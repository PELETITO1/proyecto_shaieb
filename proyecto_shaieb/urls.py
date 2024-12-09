from django.contrib import admin
from django.urls import path
from .views import (
    saludo,
    muestra_nombre,
    probando_template,
    usando_loader
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('muestra_nombre/<nombre>/', muestra_nombre),
    path('probando_template/', probando_template),
    path('usando_loader/', usando_loader),
]