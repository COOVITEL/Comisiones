# Generated by Django 4.2.1 on 2023-10-19 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaptacionAhorroVista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('since', models.CharField(max_length=50)),
                ('until', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
            ],
        ),
    ]
