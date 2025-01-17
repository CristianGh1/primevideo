# Generated by Django 5.1 on 2024-11-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la película', max_length=50)),
                ('genero', models.CharField(choices=[('Accion', 'Acción'), ('Comedia', 'Comedia'), ('Drama', 'Drama'), ('Suspenso', 'Suspenso'), ('Crimen', 'Crimen'), ('Romance', 'Romance'), ('Terror', 'Terror'), ('Musical', 'Musical')], help_text='Género de la película', max_length=20)),
                ('clasificacion', models.CharField(choices=[('TE', 'TE'), ('TE+7', 'TE+7'), ('14+', '14+'), ('18+', '18+')], help_text='Clasificación de la película', max_length=8)),
                ('episodio', models.PositiveIntegerField(help_text='Cantidad de episodios')),
                ('resena', models.TextField(blank=True, help_text='Breve reseña del contenido de la película')),
                ('anio', models.PositiveIntegerField(help_text='Año de lanzamiento')),
                ('imagen', models.ImageField(upload_to='series/')),
            ],
        ),
    ]
