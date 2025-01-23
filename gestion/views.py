from django.shortcuts import render
from .models import Gasto
from .forms import RangoFechasForm
from django.db.models import Sum

def filtrar_gastos(request):
    if request.method == 'POST':
        form = RangoFechasForm(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            
            # Obtener los gastos detallados
            gastos_detalle = Gasto.objects.filter(
                fecha__range=[fecha_inicio, fecha_fin]
            ).select_related('empleado', 'departamento')
            
            # Obtener el total por departamento
            gastos_total = Gasto.objects.filter(
                fecha__range=[fecha_inicio, fecha_fin]
            ).values('departamento__nombre').annotate(
                total=Sum('monto')
            )
            
            return render(request, 'gestion/resultado.html', {
                'gastos': gastos_detalle,
                'totales_departamento': gastos_total,
                'fecha_inicio': fecha_inicio,
                'fecha_fin': fecha_fin
            })
    else:
        form = RangoFechasForm()
    
    return render(request, 'gestion/filtrar_gastos.html', {'form': form})
