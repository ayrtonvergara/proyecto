# Generated by Django 3.2.5 on 2021-07-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210709_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='idCategoria',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='IdCategoria'),
        ),
    ]