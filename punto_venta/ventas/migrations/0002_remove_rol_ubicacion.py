# Generated by Django 5.0.3 on 2024-04-24 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rol',
            name='ubicacion',
        ),
    ]
