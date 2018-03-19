# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-07 10:50
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atributos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('Point', 'Point'), ('Polygon', 'Polygon'), ('LineString', 'LineString'), ('Text', 'Text'), ('Int', 'Int'), ('Float', 'Float'), ('MultiPolygon', 'MultiPolygon'), ('MultiLineString', 'MultiLineString'), ('Image', 'Image'), ('Email', 'Email'), ('Date', 'Date'), ('DateTime', 'DateTime')], max_length=30)),
                ('descripcion', models.CharField(max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Capas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('Point', 'Point'), ('Polygon', 'Polygon'), ('LineString', 'LineString'), ('MultiPolygon', 'MultiPolygon'), ('MultiLineString', 'MultiLineString')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Casos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('fecha_creado', models.DateField()),
                ('hora_creado', models.TimeField()),
                ('visible', models.BooleanField(default=False)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('descripcion', models.CharField(max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Censo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=255)),
                ('totalFamilias', models.IntegerField(default=0)),
                ('totalHabitantes', models.IntegerField(default=0)),
                ('totalViviendas', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CentroEducativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('anyo_construccion', models.IntegerField(default=1900)),
                ('area', models.FloatField(default=0)),
                ('uso', models.CharField(blank=True, max_length=255, null=True)),
                ('tipoPisos', models.CharField(blank=True, max_length=255, null=True)),
                ('indiceOcupacional', models.FloatField(default=0)),
                ('codigoDEA', models.CharField(blank=True, max_length=255, null=True)),
                ('matricula', models.IntegerField(default=1)),
                ('tipoEscuela', models.CharField(blank=True, max_length=255, null=True)),
                ('turno', models.CharField(blank=True, max_length=255, null=True)),
                ('numedificios', models.IntegerField(default=1)),
                ('numpisos', models.IntegerField(default=1)),
                ('tipoEdificacion', models.CharField(blank=True, max_length=255, null=True)),
                ('tipoDependencia', models.CharField(blank=True, max_length=255, null=True)),
                ('danyo', models.CharField(blank=True, max_length=255, null=True)),
                ('indiceVulnerabilidad', models.FloatField(default=0)),
                ('indiceAmenaza', models.FloatField(default=0)),
                ('indiceRiesgo', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CentroSaludEmergencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('anyo_construccion', models.IntegerField(default=1900)),
                ('poblacionDiaria', models.IntegerField(default=0)),
                ('numCamas', models.IntegerField(default=0)),
                ('capacidad', models.IntegerField(default=0)),
                ('horarioAtencion', models.CharField(blank=True, max_length=255, null=True)),
                ('serviciosMedicos', models.CharField(blank=True, max_length=255, null=True)),
                ('numpisos', models.IntegerField(default=1)),
                ('numedificios', models.IntegerField(default=1)),
                ('area', models.FloatField(default=0)),
                ('indiceVulnerabilidad', models.FloatField(default=0)),
                ('indiceAmenaza', models.FloatField(default=0)),
                ('indiceRiesgo', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comunidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('poblacion', models.IntegerField(default=0)),
                ('area', models.FloatField(default=0)),
                ('indiceVulnerabilidad', models.FloatField(default=0)),
                ('indiceAmenaza', models.FloatField(default=0)),
                ('indiceRiesgo', models.FloatField(default=0)),
                ('statusSocial', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConsejoComunal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('poblacionDeterminada', models.IntegerField(default=0)),
                ('poblacionCenso', models.IntegerField(default=0)),
                ('area', models.FloatField(default=0)),
                ('servicios', models.CharField(blank=True, max_length=255, null=True)),
                ('representante', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono', models.CharField(blank=True, max_length=255, null=True)),
                ('indiceVulnerabilidad', models.IntegerField(default=0)),
                ('indiceAmenaza', models.IntegerField(default=0)),
                ('indiceRiesgo', models.IntegerField(default=0)),
                ('comunidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consejoscomunales', to='capas.Comunidad')),
            ],
        ),
        migrations.CreateModel(
            name='GeoUnidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('area', models.FloatField(default=0)),
                ('indiceAmenaza', models.FloatField(default=0)),
                ('indiceVulnerabilidad', models.FloatField(default=0)),
                ('indiceRiesgo', models.FloatField(default=0)),
                ('fuente', models.CharField(max_length=255, null=True)),
                ('anyo', models.IntegerField(default=1900)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.TextField()),
                ('caso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='capas.Casos')),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('tipo', models.CharField(choices=[('Text', 'Text'), ('Int', 'Int'), ('Float', 'Float'), ('Image', 'Image'), ('Email', 'Email'), ('Date', 'Date'), ('DateTime', 'DateTime')], max_length=30)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parametros', to='capas.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Riesgos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indiceVulnerabilidad', models.FloatField(default=0)),
                ('indiceAmenaza', models.FloatField(default=0)),
                ('indiceRiesgo', models.FloatField(default=0)),
                ('anyo', models.IntegerField(default=1900)),
                ('fuente', models.CharField(blank=True, max_length=255, null=True)),
                ('indiceModificado', models.CharField(blank=True, max_length=255, null=True)),
                ('activo', models.BooleanField(default=False)),
                ('geounidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='riesgos', to='capas.GeoUnidad')),
            ],
        ),
        migrations.CreateModel(
            name='Suceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sucesos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Territorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
                ('nombre', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=60)),
                ('poblacionCenso', models.IntegerField(default=0)),
                ('poblacionDeterminada', models.IntegerField(default=0)),
                ('estado', models.CharField(blank=True, max_length=255)),
                ('municipio', models.CharField(blank=True, max_length=255)),
                ('parroquia', models.CharField(blank=True, max_length=255)),
                ('parentid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dependencias', to='capas.Territorio')),
            ],
        ),
        migrations.CreateModel(
            name='TipologiaConstructiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('nombre_centro', models.CharField(max_length=255, unique=True)),
                ('estandar', models.CharField(max_length=255)),
                ('anyo', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(blank=True, max_length=255, null=True)),
                ('grupos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='auth.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('numero', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('anyo_construccion', models.IntegerField(default=1900)),
                ('numpisos', models.IntegerField(default=1)),
                ('tipoEstructura', models.CharField(blank=True, max_length=255, null=True)),
                ('uso', models.CharField(blank=True, max_length=255, null=True)),
                ('area', models.FloatField(default=0)),
                ('indiceOcupacional', models.FloatField(default=0)),
                ('numHabitacion', models.IntegerField(default=0)),
                ('numAmbientes', models.IntegerField(default=1)),
                ('tipo', models.CharField(blank=True, max_length=255, null=True)),
                ('tipoParedes', models.CharField(blank=True, max_length=255, null=True)),
                ('tipoPiso', models.CharField(blank=True, max_length=255, null=True)),
                ('tipoTecho', models.CharField(blank=True, max_length=255, null=True)),
                ('numBanos', models.IntegerField(default=0)),
                ('aguasBlancas', models.CharField(blank=True, max_length=2, null=True)),
                ('aguasServidas', models.CharField(blank=True, max_length=2, null=True)),
                ('gas', models.CharField(blank=True, max_length=255, null=True)),
                ('sistemaElectrico', models.CharField(blank=True, max_length=255, null=True)),
                ('aseo', models.CharField(blank=True, max_length=255, null=True)),
                ('telefonia', models.CharField(blank=True, max_length=255, null=True)),
                ('transporte', models.CharField(blank=True, max_length=255, null=True)),
                ('numFamilias', models.IntegerField(default=0)),
                ('numHabitantes', models.IntegerField(default=0)),
                ('numNinos', models.IntegerField(default=0)),
                ('numAdultos', models.IntegerField(default=0)),
                ('numTercera', models.IntegerField(default=0)),
                ('numMasculino', models.IntegerField(default=0)),
                ('numFemenino', models.IntegerField(default=0)),
                ('nacionalidad', models.CharField(blank=True, max_length=255, null=True)),
                ('indiceVulnerabilidad', models.FloatField(default=0)),
                ('indiceAmenaza', models.FloatField(default=0)),
                ('indiceRiesgo', models.FloatField(default=0)),
                ('comunidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='viviendas', to='capas.Comunidad')),
                ('consejoComunal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='viviendas', to='capas.ConsejoComunal')),
                ('tipologiaConstructiva', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='viviendas', to='capas.TipologiaConstructiva')),
            ],
        ),
        migrations.AddField(
            model_name='geounidad',
            name='territorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='geounidades', to='capas.Territorio'),
        ),
        migrations.AddField(
            model_name='comunidad',
            name='geounidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comunidades', to='capas.GeoUnidad'),
        ),
        migrations.AddField(
            model_name='comunidad',
            name='territorio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comunidades', to='capas.Territorio'),
        ),
        migrations.AddField(
            model_name='comunidad',
            name='tipologiaConstructiva',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comunidades', to='capas.TipologiaConstructiva'),
        ),
        migrations.AddField(
            model_name='centrosaludemergencia',
            name='comunidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='centrosaludemergencia', to='capas.Comunidad'),
        ),
        migrations.AddField(
            model_name='centrosaludemergencia',
            name='tipologiaConstructiva',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='centrosaludemergencia', to='capas.TipologiaConstructiva'),
        ),
        migrations.AddField(
            model_name='centroeducativo',
            name='comunidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='centroseducativos', to='capas.Comunidad'),
        ),
        migrations.AddField(
            model_name='centroeducativo',
            name='tipologiaConstructiva',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='centroseducativos', to='capas.TipologiaConstructiva'),
        ),
        migrations.AddField(
            model_name='censo',
            name='consejocomunal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='censo', to='capas.ConsejoComunal'),
        ),
        migrations.AddField(
            model_name='casos',
            name='suceso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='casos', to='capas.Suceso'),
        ),
        migrations.AddField(
            model_name='casos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='casos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='capas',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capas', to='capas.Categoria'),
        ),
        migrations.AddField(
            model_name='atributos',
            name='capa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atributos', to='capas.Capas'),
        ),
    ]
