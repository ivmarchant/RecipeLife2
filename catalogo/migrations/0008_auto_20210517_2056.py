# Generated by Django 3.1.2 on 2021-05-18 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0007_receta_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manga',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='mangaka',
        ),
        migrations.DeleteModel(
            name='Figuras',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
        migrations.DeleteModel(
            name='Manga',
        ),
        migrations.DeleteModel(
            name='Mangaka',
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
    ]
