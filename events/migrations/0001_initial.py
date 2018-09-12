# Generated by Django 2.0.8 on 2018-09-11 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('event', models.CharField(max_length=100)),
                ('priority', models.CharField(choices=[('0', 'Sem prioridade'), ('1', 'Normal'), ('2', 'Urgente'), ('3', 'Muito urgente'), ('4', 'Ultra Mega Hiper Urgente')], max_length=1)),
            ],
        ),
    ]
