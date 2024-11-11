from django import forms
from .models import Serie
from datetime import date


class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['nombre', 'genero', 'clasificacion', 'episodio', 'resena',
                  'anio','imagen']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la serie'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'clasificacion': forms.Select(attrs={'class': 'form-control'}),
            'episodio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de episodios'}),
            'resena': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Breve reseña del contenido de la serie'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Año de lanzamiento'}),
            'imagen': forms.ClearableFileInput(attrs={'accept': 'image/*', 'directory': 'series'}), }


