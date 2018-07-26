# Generated by Django 2.0.7 on 2018-07-26 00:44

from django.db import migrations, models
import servico.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, verbose_name='Servico')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=20)),
                ('descricao', models.TextField(null=True, verbose_name='descricao')),
                ('jornada', models.CharField(max_length=120, verbose_name='jornada')),
                ('imagem', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=servico.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
        ),
    ]
