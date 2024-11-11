from django.db import models
 


class Serie(models.Model):

    GENERO_CHOICES = [
        ('Accion', 'Acción'),
        ('Comedia', 'Comedia'),
        ('Drama', 'Drama'),
        ('Suspenso', 'Suspenso'),
        ('Crimen', 'Crimen'),
        ('Romance', 'Romance'),
        ('Terror', 'Terror'),
        ('Musical', 'Musical'),

    ]

    CLASIFICACION_CHOICES = [
        ('TE', 'TE'),
        ('TE+7', 'TE+7'),
        ('14+', '14+'),
        ('18+', '18+'),
    ]

    nombre = models.CharField(max_length=50, help_text='Nombre de la película')
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES,
                              help_text='Género de la película', blank=False)
    clasificacion = models.CharField(
        max_length=8, choices=CLASIFICACION_CHOICES, help_text='Clasificación de la película', blank=False)
    episodio = models.PositiveIntegerField(
        help_text='Cantidad de episodios')
    resena = models.TextField(
        blank=True, help_text='Breve reseña del contenido de la película')
    anio = models.PositiveIntegerField(help_text='Año de lanzamiento' )
    imagen = models.ImageField(upload_to='series/')

    def __str__(self):
        return self.nombre
