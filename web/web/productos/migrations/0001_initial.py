# Generated by Django 2.2.1 on 2019-09-06 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.PositiveIntegerField()),
                ('color_codigo', models.PositiveSmallIntegerField()),
                ('activo', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=6, unique=True)),
                ('visualizaciones', models.IntegerField(default=0)),
            ],
            options={
                'unique_together': {('referencia', 'color_codigo')},
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagen')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='productos.Producto')),
            ],
        ),
    ]
