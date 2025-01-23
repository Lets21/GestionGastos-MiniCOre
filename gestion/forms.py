from django import forms

class RangoFechasForm(forms.Form):
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget)
    fecha_fin = forms.DateField(widget=forms.SelectDateWidget)
