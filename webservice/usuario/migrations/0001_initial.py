# Generated by Django 2.0.7 on 2018-07-27 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, verbose_name='Nome')),
                ('telefone_celular', models.IntegerField(verbose_name='Celular')),
                ('email', models.EmailField(max_length=120, verbose_name='Email')),
                ('usuario', models.CharField(max_length=50, verbose_name='Usuario')),
                ('senha', models.CharField(max_length=80, verbose_name='Senha')),
            ],
        ),
    ]