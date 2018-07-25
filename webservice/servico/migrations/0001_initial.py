# Generated by Django 2.0.7 on 2018-07-25 14:41

from django.db import migrations, models


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
            ],
        ),
    ]
