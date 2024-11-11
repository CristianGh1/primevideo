from django.urls import path, re_path
from django.contrib import admin
from moduloSeries import views
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.SerieListView, name='serie-list'),
    path('agregarserie/', views.agregar_serie, name='agregarserie'),
    path('<int:id>/', views.serie_detail, name='serie-detail'),
    path('editar/<int:id>/', views.editar_serie, name='editar-serie'),
    path('eliminar/<int:id>/', views.eliminar_serie, name='eliminar-serie'),
    path('gestionseries/', views.SerieListCrud, name='gestion_series'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


