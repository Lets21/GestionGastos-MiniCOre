from django.urls import path
from . import views

urlpatterns = [
    path('filtrar_gastos/', views.filtrar_gastos, name='filtrar_gastos'),
]
