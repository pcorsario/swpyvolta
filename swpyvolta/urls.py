from django.contrib import admin
from django.urls import path
from .views import index, clientes, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('clientes/', clientes),
    path('dashboard/', dashboard),
]
