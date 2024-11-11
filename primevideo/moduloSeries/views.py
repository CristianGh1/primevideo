from django.shortcuts import render, redirect, get_object_or_404
from .models import Serie
from .forms import SerieForm
from django.contrib import messages


def SerieListView(request):

    series = Serie.objects.all()

    series = series.order_by('nombre')

    series = {"series":series}

    return render(request,"series_list.html",series)

def SerieListCrud(request):

    series = Serie.objects.all()

    series = series.order_by('nombre')

    series = {"series":series}

    return render(request,"series_crud.html",series)

def serie_detail(request, id):
    serie = get_object_or_404(Serie, id=id)
    return render(request, "serie_details.html", {'serie': serie})


def agregar_serie(request):
    if request.method == 'POST':
        form = SerieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # Redirige a la vista lista_articulos
            return SerieListView(request)
    else:
        form = SerieForm()

    return render(request, "serie_form.html", {'form': form})

def eliminar_serie(request, id):
    serie = Serie.objects.get(id=id)
    serie.delete()
    # Agrega un mensaje de confirmación
    messages.success(
        request, f'Se ha eliminado a {serie.nombre}')
    return redirect('serie-list')

def editar_serie(request, id):
    serie = get_object_or_404(Serie, id=id)
    if request.method == 'POST':
        form = SerieForm(request.POST, request.FILES, instance=serie)
        if form.is_valid():
            form.save()
            print("Formulario válido. Serie guardada.")
            return redirect('serie-list')
        else:
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = SerieForm(instance=serie)

    return render(request, 'serie_form.html', {'form': form})

