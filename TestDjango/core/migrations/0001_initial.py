# Generated by Django 3.2.5 on 2021-07-09 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('idServicios', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cambio_aceite', models.CharField(max_length=20, verbose_name='id de cambio de aceite')),
                ('cambio_filtro_aire', models.CharField(max_length=20, verbose_name='cambio filtro aire')),
                ('cambio_filtro_combustible', models.CharField(max_length=20, verbose_name='cambio filtro combustible')),
                ('cambio_bujias', models.CharField(max_length=20, verbose_name='cambio bujias')),
                ('cambio_rotulas', models.CharField(max_length=20, verbose_name='cambio rotulas')),
                ('cambio_terminal', models.CharField(max_length=20, verbose_name='cambio terminal')),
                ('cambio_pastillas', models.CharField(max_length=20, verbose_name='cambio pastillas')),
                ('cambio_diferencial', models.CharField(max_length=20, verbose_name='cambio diferencial')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.servicios')),
            ],
        ),
    ]
