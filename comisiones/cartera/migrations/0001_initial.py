# Generated by Django 4.2.1 on 2023-10-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasaMin', models.CharField(max_length=50)),
                ('tasaMax', models.CharField(max_length=50)),
                ('sinde', models.CharField(max_length=50)),
                ('until', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
            ],
        ),
    ]
