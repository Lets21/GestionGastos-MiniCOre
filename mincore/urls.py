from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_gastos(request):
    return redirect('filtrar_gastos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls')),
    path('', redirect_to_gastos, name='home'),
]
