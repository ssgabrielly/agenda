# Generated by Django 2.0.8 on 2018-10-10 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180913_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereço', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('0', 'Feminino'), ('1', 'Masculino')], max_length=1)),
                ('cor', models.CharField(choices=[('0', 'Branco'), ('1', 'Pardo'), ('2', 'Negro'), ('3', 'Amarelo')], max_length=1)),
            ],
        ),
    ]