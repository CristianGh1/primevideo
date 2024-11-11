from django.contrib import admin
from .models import Serie

# Register your models here.

class SerieAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero', 'clasificacion', 'episodio', 'anio')
    list_filter = ( 'genero', 'clasificacion', 'anio')
    search_fields = ('nombre', 'anio')


admin.site.register(Serie)
